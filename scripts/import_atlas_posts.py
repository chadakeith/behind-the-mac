#!/usr/bin/env python3
"""Import Atlas Carolina blog posts into Behind the Mac markdown + HTML."""

from __future__ import annotations

import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import html2text
from bs4 import BeautifulSoup
from markdown import markdown as render_markdown

ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = ROOT / "posts"
BLOG_DIR = ROOT / "blog"
STATE_DIR = Path("/tmp/atlas-export")
SITEMAP_URL = "https://www.atlascarolina.com/sitemap.xml"
BLOG_JSON_URL = "https://www.atlascarolina.com/blog?format=json"
USER_AGENT = "BehindTheMacMigration/1.0 (chad@atlascarolina.com)"
TZ = ZoneInfo("America/New_York")
OPAQUE_SLUG = re.compile(r"^[a-z0-9]{16,}$")
WRITTEN_BY = re.compile(r"^\s*written by\s+atlas solutions\s*$", re.I)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} | Behind the Mac</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="https://behindthemac.com/blog/{slug}/">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="Behind the Mac">
  <meta property="og:title" content="{title} | Behind the Mac">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="https://behindthemac.com/blog/{slug}/">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{title} | Behind the Mac">
  <meta name="twitter:description" content="{description}">
  <link rel="icon" href="../../favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="../../css/styles.css">
</head>
<body>
  <a class="skip" href="#content">Skip to content</a>
  <header class="site-header">
    <nav class="nav-inner" aria-label="Primary">
      <a class="logo" href="../../index.html">Behind the Mac</a>
      <ul class="nav-links">
        <li><a href="../../index.html">Home</a></li>
        <li><a href="../">Blog</a></li>
        <li><a href="../../about/">About</a></li>
      </ul>
    </nav>
  </header>

  <main id="content">
    <article class="post">
      <header class="page">
        <p class="post-meta"><time datetime="{date}">{pretty_date}</time></p>
        <h1>{title}</h1>
      </header>
      <div class="post-body">
        {body}
      </div>
      <p class="post-source"><a href="{original_url}">First published on the Atlas blog</a></p>
    </article>
  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <p>Mac and Apple notes by Chad Keith.</p>
      <p>
        <a href="https://chadwickkeith.com">chadwickkeith.com</a>
        · <a href="https://overcomingaverage.net">overcomingaverage.net</a>
        · <a class="quiet-link" href="https://atlascarolina.com">Atlas</a>
      </p>
    </div>
  </footer>
</body>
</html>
"""


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def slugify(title: str) -> str:
    text = title.lower()
    text = text.replace("’", "").replace("'", "").replace("“", "").replace("”", "")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "post"


def is_opaque_slug(slug: str) -> bool:
    return bool(OPAQUE_SLUG.fullmatch(slug)) or "/" in slug


def request(url: str, retries: int = 6) -> bytes:
    delay = 2.0
    last_error = None
    for attempt in range(retries):
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.read()
        except urllib.error.HTTPError as exc:
            last_error = exc
            if exc.code in {429, 500, 502, 503, 504}:
                time.sleep(delay)
                delay = min(delay * 2, 60)
                continue
            raise
        except (urllib.error.URLError, TimeoutError) as exc:
            last_error = exc
            time.sleep(delay)
            delay = min(delay * 2, 60)
    raise RuntimeError(f"Failed to fetch {url}: {last_error}")


def sitemap_post_urls() -> list[str]:
    xml = request(SITEMAP_URL).decode("utf-8")
    locs = re.findall(r"<loc>(.*?)</loc>", xml)
    posts = []
    seen = set()
    for loc in locs:
        if "/blog/" not in loc:
            continue
        url = loc.rstrip("/")
        if url in seen:
            continue
        seen.add(url)
        posts.append(url)
    return posts


def paginate_collection() -> list[dict]:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    raw_path = STATE_DIR / "items.json"
    if raw_path.exists():
        return json.loads(raw_path.read_text())

    items: list[dict] = []
    url = BLOG_JSON_URL
    while url:
        payload = json.loads(request(url))
        page_items = payload.get("items") or []
        items.extend(page_items)
        pagination = payload.get("pagination") or {}
        if pagination.get("nextPage") and pagination.get("nextPageUrl"):
            next_url = urllib.parse.urljoin("https://www.atlascarolina.com", pagination["nextPageUrl"])
            parsed = urllib.parse.urlparse(next_url)
            query = urllib.parse.parse_qs(parsed.query)
            query["format"] = ["json"]
            url = urllib.parse.urlunparse(
                parsed._replace(query=urllib.parse.urlencode(query, doseq=True))
            )
            time.sleep(0.6)
        else:
            url = ""
    raw_path.write_text(json.dumps(items))
    return items


def fetch_missing(url: str) -> dict:
    json_url = url + ("&" if "?" in url else "?") + "format=json"
    payload = json.loads(request(json_url))
    item = payload.get("item")
    if not item:
        raise RuntimeError(f"No item in {url}")
    return item


def abs_image_url(src: str) -> str:
    if not src:
        return ""
    if src.startswith("//"):
        return "https:" + src
    if src.startswith("/"):
        return "https://www.atlascarolina.com" + src
    return src


def clean_html(body: str) -> str:
    soup = BeautifulSoup(body, "lxml")
    for tag in soup.find_all(["style", "script", "noscript"]):
        tag.decompose()

    for img in soup.find_all("img"):
        src = img.get("data-src") or img.get("data-image") or img.get("src") or ""
        src = abs_image_url(src)
        alt = (img.get("alt") or "").strip()
        img.attrs = {"src": src, "alt": alt} if src else None
        if not src:
            img.decompose()

    for a in soup.find_all("a"):
        href = a.get("href") or ""
        if href.startswith("/"):
            a["href"] = "https://www.atlascarolina.com" + href

    text = str(soup)
    text = WRITTEN_BY.sub("", text)
    return text


def html_to_markdown(body: str) -> str:
    cleaned = clean_html(body)
    converter = html2text.HTML2Text()
    converter.body_width = 0
    converter.ignore_images = False
    converter.ignore_links = False
    converter.unicode_snob = True
    converter.wrap_links = False
    converter.protect_links = True
    md = converter.handle(cleaned)
    lines = []
    for line in md.splitlines():
        if WRITTEN_BY.match(line):
            continue
        lines.append(line.rstrip())
    md = "\n".join(lines)
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    return md


def excerpt_from_markdown(md: str) -> str:
    for line in md.splitlines():
        text = re.sub(r"[*_`>#\[\]]", "", line).strip()
        if text and not text.startswith("http") and not text.startswith("!"):
            return text[:180]
    return "A note from Behind the Mac."


def pretty_date(date_str: str) -> str:
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return dt.strftime("%b %-d, %Y")


def unique_slug(base: str, used: set[str]) -> str:
    slug = base
    n = 2
    while slug in used:
        slug = f"{base}-{n}"
        n += 1
    used.add(slug)
    return slug


def write_post(item: dict, original_url: str, used_slugs: set[str]) -> dict:
    title = (item.get("title") or "Untitled").strip()
    raw_slug = (item.get("urlId") or original_url.rstrip("/").split("/")[-1]).strip()
    if is_opaque_slug(raw_slug):
        slug = unique_slug(slugify(title), used_slugs)
    else:
        slug = unique_slug(slugify(raw_slug), used_slugs)

    published = datetime.fromtimestamp(item["publishOn"] / 1000, tz=TZ)
    date = published.strftime("%Y-%m-%d")
    md_body = html_to_markdown(item.get("body") or "")
    html_body = render_markdown(md_body, extensions=["extra", "sane_lists"])

    front = [
        "---",
        f"title: {yaml_quote(title)}",
        f"date: {date}",
        f"slug: {yaml_quote(slug)}",
        f"original_url: {yaml_quote(original_url)}",
        'author: "Chad Keith"',
        "source: atlascarolina",
        "---",
        "",
        md_body,
        "",
    ]
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    (POSTS_DIR / f"{date}-{slug}.md").write_text("\n".join(front))

    page_dir = BLOG_DIR / slug
    page_dir.mkdir(parents=True, exist_ok=True)
    description = excerpt_from_markdown(md_body)
    (page_dir / "index.html").write_text(
        HTML_TEMPLATE.format(
            title=html_escape(title),
            description=html_escape(description),
            slug=urllib.parse.quote(slug),
            date=date,
            pretty_date=pretty_date(date),
            body=html_body,
            original_url=html_escape(original_url),
        )
    )
    return {
        "title": title,
        "date": date,
        "slug": slug,
        "original_url": original_url,
        "author": "Chad Keith",
        "source": "atlascarolina",
    }


def html_escape(value: str) -> str:
    return (
        value.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def write_sitemap(entries: list[dict]) -> None:
    urls = [
        "https://behindthemac.com/",
        "https://behindthemac.com/about/",
        "https://behindthemac.com/blog/",
    ]
    urls.extend(f"https://behindthemac.com/blog/{e['slug']}/" for e in entries)
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for url in urls:
        lines.append("  <url>")
        lines.append(f"    <loc>{url}</loc>")
        lines.append("  </url>")
    lines.append("</urlset>")
    lines.append("")
    (ROOT / "sitemap.xml").write_text("\n".join(lines))


def main() -> None:
    sitemap_urls = sitemap_post_urls()
    print(f"sitemap posts: {len(sitemap_urls)}")
    items = paginate_collection()
    print(f"collection items: {len(items)}")

    by_url = {}
    for item in items:
        full = item.get("fullUrl") or ""
        if not full:
            continue
        url = urllib.parse.urljoin("https://www.atlascarolina.com", full).rstrip("/")
        by_url[url] = item

    missing = [url for url in sitemap_urls if url not in by_url]
    print(f"missing from collection: {len(missing)}")
    for i, url in enumerate(missing, 1):
        print(f"  fetch {i}/{len(missing)} {url}")
        try:
            by_url[url] = fetch_missing(url)
        except Exception as exc:
            print(f"  FAIL {url}: {exc}")
        time.sleep(0.6)

    used_slugs: set[str] = set()
    exported: list[dict] = []
    failures: list[str] = []

    for url in sitemap_urls:
        item = by_url.get(url)
        if not item:
            failures.append(url)
            continue
        try:
            exported.append(write_post(item, url, used_slugs))
        except Exception as exc:
            failures.append(f"{url} ({exc})")

    exported.sort(key=lambda row: (row["date"], row["slug"]), reverse=True)
    (POSTS_DIR / "index.json").write_text(json.dumps(exported, indent=2, ensure_ascii=False) + "\n")
    write_sitemap(exported)
    (STATE_DIR / "failures.json").write_text(json.dumps(failures, indent=2))
    print(f"wrote {len(exported)} posts")
    print(f"failures {len(failures)}")
    for row in failures[:20]:
        print(" ", row)


if __name__ == "__main__":
    main()

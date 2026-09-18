#!/usr/bin/env python3
"""Rebuild posts/index.json from markdown sources in posts/."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = ROOT / "posts"
BLOG_DIR = ROOT / "blog"
sys.path.insert(0, str(Path(__file__).resolve().parent))

from post_meta import first_image, make_excerpt, parse_front_matter  # noqa: E402

SKIP_NAMES = {"README.md", "_template.md"}


def iter_posts() -> list[Path]:
    return sorted(
        path
        for path in POSTS_DIR.glob("*.md")
        if path.name not in SKIP_NAMES
    )


def entry_from_markdown(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    meta, body = parse_front_matter(text)
    title = (meta.get("title") or path.stem).strip()
    date = (meta.get("date") or "").strip()
    slug = (meta.get("slug") or "").strip()
    if not date or not slug:
        raise ValueError(f"{path.name} is missing date or slug")

    image, image_alt = first_image(body)
    excerpt = (meta.get("excerpt") or "").strip() or make_excerpt(body)
    if meta.get("image"):
        image = meta["image"].strip() or image
    if meta.get("image_alt"):
        image_alt = meta["image_alt"].strip()

    entry = {
        "title": title,
        "date": date,
        "slug": slug,
        "original_url": (meta.get("original_url") or "").strip(),
        "author": (meta.get("author") or "Chad Keith").strip(),
        "source": (meta.get("source") or "").strip(),
        "excerpt": excerpt,
    }
    if image:
        entry["image"] = image
        entry["image_alt"] = image_alt or title
    return entry


def html_escape(value: str) -> str:
    return (
        value.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def polish_post_html(entry: dict) -> bool:
    """Promote the first body image to a hero and add social image tags."""
    path = BLOG_DIR / entry["slug"] / "index.html"
    if not path.exists():
        return False
    html = path.read_text(encoding="utf-8")
    original = html
    image = entry.get("image") or ""

    if image and 'property="og:image"' not in html:
        safe = html_escape(image)
        html = html.replace(
            f'<meta property="og:url" content="https://behindthemac.com/blog/{entry["slug"]}/">',
            (
                f'<meta property="og:url" content="https://behindthemac.com/blog/{entry["slug"]}/">\n'
                f'  <meta property="og:image" content="{safe}">'
            ),
            1,
        )
        html = html.replace(
            '<meta name="twitter:card" content="summary">',
            '<meta name="twitter:card" content="summary_large_image">',
            1,
        )
        if 'name="twitter:image"' not in html:
            html = html.replace(
                '<meta name="twitter:title"',
                f'<meta name="twitter:image" content="{safe}">\n  <meta name="twitter:title"',
                1,
            )

    html = re.sub(
        r'(<div class="post-body">\s*)<p>\s*(<img\b[^>]*>)\s*</p>',
        r'\1<figure class="post-hero">\2</figure>',
        html,
        count=1,
        flags=re.I,
    )
    if 'class="post-hero"' in html:
        html = re.sub(
            r'(<figure class="post-hero"><img\b[^>]*\balt=")(")',
            r"\1" + html_escape(entry["title"]) + r"\2",
            html,
            count=1,
            flags=re.I,
        )

    if html == original:
        return False
    path.write_text(html, encoding="utf-8")
    return True


def build_index() -> list[dict]:
    entries = [entry_from_markdown(path) for path in iter_posts()]
    entries.sort(key=lambda row: (row["date"], row["slug"]), reverse=True)
    out = POSTS_DIR / "index.json"
    out.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return entries


def main() -> None:
    entries = build_index()
    polished = sum(1 for entry in entries if polish_post_html(entry))
    with_images = sum(1 for row in entries if row.get("image"))
    print(f"wrote {len(entries)} posts ({with_images} with images)")
    print(f"polished {polished} article pages")


if __name__ == "__main__":
    main()

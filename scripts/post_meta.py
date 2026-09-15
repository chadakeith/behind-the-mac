"""Shared helpers for post listings: featured image + excerpt from markdown."""

from __future__ import annotations

import html
import re
from urllib.parse import urlparse

IMAGE_MD_RE = re.compile(
    r"!\[([^\]]*)\]\(\s*<?((?:https?:)?//[^)\s>]+|https?://[^)\s>]+)>?\s*\)",
    re.I,
)
IMAGE_HTML_RE = re.compile(
    r'<img\b[^>]*\bsrc=["\']([^"\']+)["\'][^>]*>',
    re.I,
)
IMAGE_HTML_ALT_RE = re.compile(r'\balt=["\']([^"\']*)["\']', re.I)
FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.S)
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(\s*<?[^>\)]+>?\s*\)")
MD_MARKUP_RE = re.compile(r"[*_`#>]+")
HTML_TAG_RE = re.compile(r"<[^>]+>")

SKIP_EXCERPT_PREFIXES = (
    "written by",
    "featured image",
    "photo by",
    "image by",
)


def abs_https_url(src: str) -> str:
    src = (src or "").strip()
    if not src:
        return ""
    if src.startswith("//"):
        src = "https:" + src
    if src.startswith("http://"):
        src = "https://" + src[len("http://") :]
    parsed = urlparse(src)
    if parsed.scheme != "https" or not parsed.netloc:
        return ""
    return src


def first_image(markdown: str) -> tuple[str, str]:
    """Return (absolute https url, alt text) for the first body image."""
    match = IMAGE_MD_RE.search(markdown)
    if match:
        return abs_https_url(match.group(2)), (match.group(1) or "").strip()

    html_match = IMAGE_HTML_RE.search(markdown)
    if html_match:
        alt_match = IMAGE_HTML_ALT_RE.search(html_match.group(0))
        alt = alt_match.group(1).strip() if alt_match else ""
        return abs_https_url(html_match.group(1)), alt
    return "", ""


def _plain_line(line: str) -> str:
    text = IMAGE_MD_RE.sub("", line)
    text = MD_LINK_RE.sub(r"\1", text)
    text = HTML_TAG_RE.sub("", text)
    text = MD_MARKUP_RE.sub("", text)
    text = html.unescape(text)
    text = text.replace("\u00a0", " ").replace("​", "")
    text = re.sub(r"\s+", " ", text).strip()
    text = text.strip("[]()#>- ")
    return text


def make_excerpt(markdown: str, min_len: int = 140, max_len: int = 220) -> str:
    """Short plain-text summary from the first usable paragraph."""
    chunks: list[str] = []
    for raw in markdown.splitlines():
        line = raw.strip()
        if not line:
            if chunks:
                break
            continue
        if line.startswith("!") or line.startswith("<img"):
            continue
        text = _plain_line(line)
        if not text:
            continue
        lower = text.lower()
        if any(lower.startswith(prefix) for prefix in SKIP_EXCERPT_PREFIXES):
            continue
        if text.startswith("http://") or text.startswith("https://"):
            continue
        chunks.append(text)
        joined = " ".join(chunks)
        if len(joined) >= min_len:
            break

    excerpt = " ".join(chunks).strip()
    if not excerpt:
        return "A note from Behind the Mac."
    if len(excerpt) <= max_len:
        return excerpt
    budget = max_len - 1
    clipped = excerpt[: budget + 1]
    cut = clipped.rfind(" ")
    if cut < min_len:
        cut = budget
    excerpt = clipped[:cut].rstrip(" ,;:-")
    if not excerpt.endswith((".", "…")):
        excerpt += "…"
    return excerpt[:max_len]


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return {}, text
    meta: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value[:1] in {'"', "'"} and value[-1:] == value[:1] and len(value) >= 2:
            value = value[1:-1]
        meta[key] = value
    return meta, text[match.end() :]

#!/usr/bin/env python3
"""Sanity checks for excerpt and featured-image extraction."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from post_meta import first_image, make_excerpt, parse_front_matter


def test_image_and_excerpt() -> None:
    md = """---
title: "Example"
date: 2026-09-11
slug: "example"
---

![](https://images.squarespace-cdn.com/content/v1/site/photo.jpg)

The latest scam making the rounds preys on your trust and sociability. You receive what appears to be a party invite from a friend via an invitation service like Paperless Post or Punchbowl.
"""
    meta, body = parse_front_matter(md)
    assert meta["slug"] == "example"
    url, alt = first_image(body)
    assert url.startswith("https://images.squarespace-cdn.com")
    assert alt == ""
    excerpt = make_excerpt(body)
    assert 140 <= len(excerpt) <= 220
    assert "scam" in excerpt.lower()
    assert "!" not in excerpt


def test_protocol_relative_and_alt() -> None:
    url, alt = first_image(
        "![Mailbox](//images.squarespace-cdn.com/content/v1/site/box.jpg)"
    )
    assert url == "https://images.squarespace-cdn.com/content/v1/site/box.jpg"
    assert alt == "Mailbox"


def test_skips_image_only_intro() -> None:
    excerpt = make_excerpt("Featured image by iStock.com/megaflopp\n\nQuick Look saves time.")
    assert excerpt.startswith("Quick Look")


if __name__ == "__main__":
    test_image_and_excerpt()
    test_protocol_relative_and_alt()
    test_skips_image_only_intro()
    print("post_meta ok")

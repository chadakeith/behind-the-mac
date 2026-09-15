# Posts

Markdown source for Behind the Mac. The first import is the Atlas Carolina blog archive (562 posts). New posts can be added the same way.

## Filename

```
YYYY-MM-DD-slug.md
```

Example: `2024-03-12-macos-sequoia-first-look.md`

## Front matter

```yaml
---
title: "Post title"
date: 2024-03-12
slug: "macos-sequoia-first-look"
original_url: "https://www.atlascarolina.com/blog/example"
author: "Chad Keith"
source: atlascarolina
---
```

| Field | Required | Notes |
| --- | --- | --- |
| `title` | yes | Display title |
| `date` | yes | `YYYY-MM-DD` (same as the filename prefix) |
| `slug` | yes | URL slug; match the filename after the date |
| `original_url` | no | Source URL if this is a migrated Atlas post |
| `author` | no | Use `Chad Keith` |
| `source` | no | `atlascarolina` for migrated posts |

Opaque Squarespace ID slugs were rewritten from the title (kebab-case, unique). Human-readable Atlas slugs were kept.

Body is markdown after the closing `---`. Copy [`_template.md`](_template.md) to start a post. Each published post also has a static page at `/blog/{slug}/`.

## Listing index

Home (latest 10) and `/blog/` (full archive, grouped by year) read [`index.json`](index.json). Keep that file in sync when adding posts. Sort newest-first.

Re-import helper: `scripts/import_atlas_posts.py`

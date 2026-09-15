# Posts

Markdown posts for Behind the Mac. A follow-up PR will drop the Atlas Carolina blog export here (~560 posts). Do not scrape or import that archive in this change.

## Filename

```
YYYY-MM-DD-slug.md
```

Example: `2024-03-12-macos-sequoia-first-look.md`

## Front matter

```yaml
---
title: Post title
date: 2024-03-12
slug: macos-sequoia-first-look
original_url: https://atlascarolina.com/blog/example
---
```

| Field | Required | Notes |
| --- | --- | --- |
| `title` | yes | Display title |
| `date` | yes | `YYYY-MM-DD` (same as the filename prefix) |
| `slug` | yes | URL slug; match the filename after the date |
| `original_url` | no | Source URL on the Atlas blog, if this is a migrated post |

Body is markdown after the closing `---`. Copy [`_template.md`](_template.md) to start a post.

## Listing index

Home (latest 10) and `/blog/` (full archive, grouped by year) read [`index.json`](index.json). Keep that file in sync when adding posts:

```json
[
  {
    "title": "Post title",
    "date": "2024-03-12",
    "slug": "macos-sequoia-first-look",
    "original_url": "https://atlascarolina.com/blog/example"
  }
]
```

Sort newest-first. `original_url` is optional. Published URL for a post is `/blog/{slug}/`.

# Posts

Markdown posts for Behind the Mac. Drop files here in a follow-up when migrating Atlas Apple write-ups.

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

Body is markdown after the closing `---`.

Copy [`_template.md`](_template.md) to start a post. The homepage and `/blog/` list will pick these up once the migration build is wired.

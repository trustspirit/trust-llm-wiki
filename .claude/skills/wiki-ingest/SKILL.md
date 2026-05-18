---
name: wiki-ingest
description: Ingest a new source (URL, PDF, transcript, note) into the LLM wiki. Saves raw source under sources/, then extracts entities and creates/updates wiki/ pages following SCHEMA.md. Triggers on "위키에 넣어줘", "ingest", "이거 위키화", or when a URL/PDF path is given in the llm-wiki directory.
---

# wiki-ingest

Read `SCHEMA.md` at the repo root FIRST — it is the authoritative spec. Skill is the operational checklist.

## Steps

### 1. Identify source type and acquire content

| Input | Action |
|---|---|
| URL (article/blog) | WebFetch the page, ask user to confirm extracted markdown looks clean |
| PDF path | Use `pdftotext <file> -` via Bash, save .txt next to .pdf |
| YouTube URL | Bash: `yt-dlp --write-auto-sub --skip-download --sub-format vtt <url>`, convert vtt → plain text |
| `.md`/`.txt` file path | Read directly |
| Free text in prompt | Treat as a note, ask for a title |

### 2. Write source file

- Slug: kebab-case from title, max 60 chars
- Path: `sources/<type>/<YYYY-MM-DD>-<slug>.md` (date = today, from `currentDate` in context)
- Frontmatter per SCHEMA.md (id, type, title, url, author, published, ingested, tags)
- If a file with the same slug exists, append `-2`, `-3`, etc. — never overwrite a source.

### 3. Extract entities

Read the source and identify:

- **People**: named individuals
- **Concepts**: technical concepts, patterns, ideas with a name
- **Topics**: broader subject areas the content fits under
- **Tools/Products**: named software, services, libraries

For each, decide: does a `wiki/` page already exist? Search:
```bash
ls wiki/people wiki/concepts wiki/topics
grep -rli "<entity name or aliases>" wiki/
```

### 4. Update or create wiki pages

For each entity:

**If page exists**:
1. Read current page
2. Add new claims as bullets under the appropriate section, each with `[source: sources/<path>]`
3. If new info contradicts existing claim, DO NOT silently overwrite. Add a `<!-- CONFLICT: ... -->` HTML comment and surface in summary to user.
4. Append new source path to frontmatter `sources:`
5. Update `updated:` to today

**If page does not exist**:
1. Create `wiki/<type>/<slug>.md`
2. Fill frontmatter (title, type, aliases, updated, sources)
3. Write a 1-2 sentence TL;DR
4. Add sections with cited claims from the source
5. Add `## See also` with `[[wikilink]]` to other entities you touched in this ingest

### 5. Update index.md

If a new topic page was created, add it under the appropriate section in `wiki/index.md`. If `wiki/index.md` doesn't exist yet, create it with a flat list grouped by type.

### 6. Log the ingest

Append one JSON line to `.meta/ingest-log.jsonl`:

```json
{"ingested_at": "<ISO-8601>", "source": "sources/articles/...", "wiki_changed": ["wiki/concepts/foo.md", "wiki/people/bar.md"], "wiki_created": ["wiki/concepts/foo.md"]}
```

### 7. Summary to user

Report:
- Source file written: `<path>`
- Wiki pages created: list
- Wiki pages updated: list
- Conflicts surfaced: list (if any) — ask user to resolve
- Suggested next ingests: if the source mentions other URLs/papers, list them as candidates

## Anti-patterns

- **Do not** edit `sources/` files after they're written. If extraction was wrong, write a corrected re-extraction as a new note in `sources/notes/`.
- **Do not** invent facts not in the source. Every wiki claim must be traceable.
- **Do not** create speculative pages for entities only mentioned in passing. Threshold: the entity must have at least one substantive claim attached, otherwise just mention it in prose without making a page.
- **Do not** overwrite a conflicting claim — surface as CONFLICT and ask the user.

## Sanity checks before finishing

- [ ] All new/updated wiki pages have frontmatter
- [ ] All factual claims have `[source: ...]`
- [ ] No broken `[[wikilink]]` introduced (if introduced, it must be intentional and listed in summary as "candidate for next page")
- [ ] `.meta/ingest-log.jsonl` updated

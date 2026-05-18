---
name: wiki-lint
description: Audit the LLM wiki for quality issues — broken wikilinks, orphan pages, uncited claims, duplicate pages, contradictions, outdated sources. Produces a report; does NOT auto-fix unless user approves each change. Triggers on "위키 점검", "wiki lint", "위키 정리".
---

# wiki-lint

Audit-only by default. Surface issues, propose fixes, but wait for user approval before modifying wiki pages.

Read `SCHEMA.md` first.

## Checks (run all, in order)

### 1. Broken wikilinks

```bash
grep -rohE '\[\[[a-z0-9-]+\]\]' wiki/ | sort -u
```
For each `[[slug]]`, check whether `wiki/*/slug.md` exists. List broken ones with the page they appear in.

### 2. Orphan pages

For each `wiki/<type>/<slug>.md` (excluding `index.md`):
```bash
grep -rl "\[\[<slug>\]\]" wiki/
```
If no other page links to it AND `wiki/index.md` doesn't reference it → orphan.

### 3. Uncited claims

For each wiki page, scan lines that look like factual statements (declarative sentences, not headers, not lists with `[source: ...]` already). Heuristic: any line in a section that doesn't contain `[source:` and isn't a synthesis (`> Synthesis:`) is suspicious. Flag, don't auto-remove.

### 4. Duplicate / near-duplicate pages

Within each `wiki/<type>/`, compare page titles and aliases. Surface pairs where:
- titles share ≥ 70% tokens, or
- aliases overlap, or
- both reference the same set of sources

### 5. Contradictions

Grep for `<!-- CONFLICT:` markers across `wiki/`. List them.

### 6. Outdated sources

For each page, look at `sources:` frontmatter. If ALL sources are older than 365 days (use ingested date from source frontmatter) AND the topic is in a fast-moving area (heuristic: tags include `ai`, `ml`, `llm`, `web`, `framework`, or user provides list), flag as potentially stale.

## Report format

```markdown
# Wiki Lint Report — <YYYY-MM-DD>

## Broken wikilinks (N)
- `wiki/concepts/foo.md` → `[[bar-baz]]` (no such page)

## Orphan pages (N)
- `wiki/people/qux.md`

## Uncited claims (N)
- `wiki/topics/web.md:L23` — "X is the most popular framework"

## Duplicates (N pairs)
- `wiki/concepts/rag.md` ↔ `wiki/concepts/retrieval-augmented-generation.md`

## Contradictions (N)
- `wiki/concepts/foo.md:L45` — CONFLICT marker

## Potentially stale (N)
- `wiki/topics/llm-tooling.md` — all 3 sources ingested 2024-12 or earlier
```

## Proposed fixes (only after report)

Ask user which issues to address. For each accepted issue, propose a concrete change:

- Broken wikilink → create stub page OR remove the link
- Orphan → add link from index.md OR delete page
- Uncited claim → mark with `<!-- UNCITED -->` for human review, or remove
- Duplicate → propose merge with canonical = older page, redirect others via alias
- Contradiction → ask user which version is correct
- Stale → suggest sources to re-ingest

NEVER batch-apply fixes without per-item approval.

## Anti-patterns

- **Do not** delete pages automatically — always ask.
- **Do not** "fix" uncited claims by inventing citations.
- **Do not** merge pages without user confirming which is canonical.

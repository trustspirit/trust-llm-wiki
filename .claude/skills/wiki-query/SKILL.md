---
name: wiki-query
description: Answer questions from the LLM wiki. Searches wiki/ markdown pages, synthesizes an answer with citations back to source files. Triggers on "위키에서 X 찾아줘", "내가 Y에 대해 뭐 알고 있지?", "wiki query", or any question asked while in the llm-wiki directory.
---

# wiki-query

Read `SCHEMA.md` for page format first if not already cached this session.

## Steps

### 1. Understand the question

Identify: is the user asking about
- a specific entity (person, concept, topic) → look up the page directly
- a relationship between entities → walk wikilinks
- a factual claim → grep across wiki/ for the claim's keywords

### 2. Locate relevant pages

Strategies, in order:

1. **Direct lookup**: if question names an entity, try `wiki/{people,concepts,topics}/<slug>.md` with kebab-case of the entity name.
2. **Alias lookup**: grep frontmatter `aliases:` field across `wiki/`.
3. **Full-text grep**: `grep -rli "<keyword>" wiki/`.
4. **Wikilink expansion**: from initial hits, follow `[[wikilinks]]` 1 hop.

Stop when you have enough — usually 2-5 pages.

### 3. Synthesize answer

- Quote or paraphrase from wiki pages, preserving their `[source: ...]` citations.
- If multiple pages contribute, label which page each claim came from: `(from wiki/concepts/foo.md)`.
- If the user asks for opinion or speculation, mark synthesis explicitly: `> Synthesis: ...`.
- If the wiki has nothing relevant, say so plainly — do not fall back to general knowledge without flagging it.

### 4. Cite at two levels

Final answer should let the user trace:
- **Wiki citation**: which wiki page(s) the answer came from
- **Source citation**: which raw source(s) those pages cite

Format:
```
<answer text>

— from [[concept-llm-wiki]], cited to sources/articles/2026-05-18-karpathy-llm-wiki.md
```

### 5. Suggest follow-ups

If the question touched pages with `<!-- CONFLICT: -->` markers, broken wikilinks, or sparse content, mention it so the user can decide to ingest more or trigger wiki-lint.

## Anti-patterns

- **Do not** answer from general knowledge silently. If wiki has nothing, say "위키에 관련 정보 없음" and optionally offer general knowledge with a clear "(외부 지식)" tag.
- **Do not** fabricate citations. Every `[source: ...]` in your answer must come from an actual wiki page you read.
- **Do not** rewrite wiki content during a query — that's wiki-ingest's job.

---
title: RAG (Retrieval-Augmented Generation)
type: concept
aliases: [RAG, retrieval-augmented generation]
updated: 2026-05-18
sources: [sources/articles/2026-05-18-karpathy-llm-wiki.md]
---

# RAG (Retrieval-Augmented Generation)

> 쿼리 시점에 raw 문서 컬렉션에서 관련 chunk를 retrieve해서 LLM이 답을 생성하는 표준 방식. NotebookLM, ChatGPT 파일 업로드 등 대부분의 문서 기반 LLM 워크플로우의 기본 패턴.

## 동작 방식

- 사용자가 파일 컬렉션을 업로드 → 쿼리 시점에 관련 chunk를 retrieve → LLM이 답 생성 [source: sources/articles/2026-05-18-karpathy-llm-wiki.md].
- NotebookLM, ChatGPT file uploads, 대부분의 RAG 시스템이 이 방식 [source: sources/articles/2026-05-18-karpathy-llm-wiki.md].

## Karpathy의 비판

- LLM이 매 질문마다 지식을 "from scratch"로 다시 발견해야 한다 — accumulation이 없다 [source: sources/articles/2026-05-18-karpathy-llm-wiki.md].
- 5개 문서를 합성해야 하는 미묘한 질문에서, LLM은 매번 관련 fragment를 다시 찾아 piece together해야 한다 [source: sources/articles/2026-05-18-karpathy-llm-wiki.md].
- 아무것도 build up되지 않는다는 점이 [[llm-wiki]] 패턴의 출발점 [source: sources/articles/2026-05-18-karpathy-llm-wiki.md].

## LLM Wiki와의 대비

| 측면 | RAG | [[llm-wiki]] |
|---|---|---|
| 합성 시점 | 쿼리 시점 | ingest 시점 |
| Cross-reference | 매번 재발견 | 미리 위키에 박혀 있음 |
| 모순 처리 | 컨텍스트 안에서 즉석 처리 | ingest 시 명시적으로 표시 |
| 지식 누적 | 없음 (raw 문서만 누적) | persistent compounding artifact |

[source: sources/articles/2026-05-18-karpathy-llm-wiki.md]

## See also

- [[llm-wiki]]
- [[karpathy]]

---
title: LLM Wiki
type: concept
aliases: [LLM-maintained wiki, persistent wiki pattern, compounding knowledge base]
updated: 2026-05-18
sources: [sources/articles/2026-05-18-karpathy-llm-wiki.md]
---

# LLM Wiki

> LLM이 유지·갱신하는 markdown 위키를 raw source와 사용자 사이에 두는 개인 지식 관리 패턴. RAG와 달리 매 쿼리마다 retrieval하지 않고 ingest 시점에 합성을 미리 컴파일해 둔다.

## 핵심 아이디어

- LLM이 새 source를 받으면 단순 인덱싱이 아니라 본문을 읽고 기존 위키의 엔티티/토픽 페이지를 갱신, 모순을 표시하고, 합성을 강화한다 [source: sources/articles/2026-05-18-karpathy-llm-wiki.md].
- 위키는 "한 번 컴파일되고 계속 유지되는 persistent, compounding artifact"이다 — cross-reference·모순·합성이 쿼리 시점이 아니라 ingest 시점에 이미 처리되어 있다 [source: sources/articles/2026-05-18-karpathy-llm-wiki.md].
- 사람은 sourcing/탐색/질문에만 관여하고, LLM이 요약·교차참조·정리 등 bookkeeping을 전담한다 [source: sources/articles/2026-05-18-karpathy-llm-wiki.md].
- Karpathy의 운영 비유: "Obsidian은 IDE, LLM은 프로그래머, 위키는 codebase" [source: sources/articles/2026-05-18-karpathy-llm-wiki.md].

## 아키텍처 (3-layer)

1. **Raw sources** — 사용자가 curate한 immutable 문서(아티클·논문·이미지·데이터). LLM은 읽기만 한다 [source: sources/articles/2026-05-18-karpathy-llm-wiki.md].
2. **Wiki** — LLM이 전적으로 소유하는 markdown 디렉토리. 요약·엔티티·개념·비교 페이지가 들어간다. 사람은 읽고, LLM이 쓴다 [source: sources/articles/2026-05-18-karpathy-llm-wiki.md].
3. **Schema** — `CLAUDE.md`(Claude Code)나 `AGENTS.md`(Codex) 같은 설정 문서. LLM을 "규율 있는 위키 관리자"로 만드는 핵심 구성요소이며, 도메인에 맞게 사용자-LLM이 co-evolve한다 [source: sources/articles/2026-05-18-karpathy-llm-wiki.md].

## 3가지 핵심 Operation

**Ingest** — 새 source를 raw에 추가하고 LLM에게 처리시킨다. 예시 flow: 본문 읽기 → 핵심 takeaway 논의 → 위키에 요약 페이지 작성 → index 갱신 → 관련 엔티티/개념 페이지 다수 갱신 → log에 entry 추가. 한 source가 10–15개 페이지를 건드릴 수 있다 [source: sources/articles/2026-05-18-karpathy-llm-wiki.md].

**Query** — 위키에 질문하면 LLM이 관련 페이지를 찾아 인용과 함께 답한다. 답변 형식은 markdown, 비교 표, Marp 슬라이드, matplotlib 차트 등 다양할 수 있다. **핵심 인사이트: 좋은 답변은 새 위키 페이지로 다시 fileback**해서 탐색이 chat history에서 사라지지 않게 한다 [source: sources/articles/2026-05-18-karpathy-llm-wiki.md].

**Lint** — 주기적으로 위키 건강 점검. 페이지 간 모순, stale 주장, 인바운드 링크 없는 orphan 페이지, 페이지가 없는 중요 개념, 누락된 cross-reference, 웹 검색으로 채울 수 있는 데이터 갭을 찾는다 [source: sources/articles/2026-05-18-karpathy-llm-wiki.md].

## index.md vs log.md

| 파일 | 성격 | 역할 |
|---|---|---|
| `index.md` | content-oriented | 위키 전체 카탈로그. 페이지·요약·메타데이터를 카테고리로 묶음. LLM이 매 ingest마다 갱신. 쿼리 시 LLM이 가장 먼저 읽음 [source: sources/articles/2026-05-18-karpathy-llm-wiki.md]. |
| `log.md` | chronological | append-only 기록(ingest·query·lint). 일관된 prefix(예: `## [2026-04-02] ingest \| Article Title`)를 쓰면 `grep "^## \[" log.md \| tail -5` 같은 unix 도구로 파싱 가능 [source: sources/articles/2026-05-18-karpathy-llm-wiki.md]. |

> **Synthesis** (from: sources/articles/2026-05-18-karpathy-llm-wiki.md): 이 저장소는 `wiki/index.md`는 두지만 `log.md` 대신 `.meta/ingest-log.jsonl`을 쓴다 — JSON line이 grep+jq 양쪽에서 파싱하기 쉽고 schema validation 가능성을 열어둔다.

## 스케일과 도구

- 인덱스 기반 단순 탐색이 ~100 sources / 수백 페이지 수준에서는 잘 작동하며, embedding-RAG 인프라가 필요 없다 [source: sources/articles/2026-05-18-karpathy-llm-wiki.md].
- 위키가 커지면 [qmd](https://github.com/tobi/qmd) 같은 로컬 markdown 검색엔진(BM25/벡터 하이브리드 + LLM 재랭킹, on-device, CLI/MCP 양쪽 제공)을 추가 가능 [source: sources/articles/2026-05-18-karpathy-llm-wiki.md].
- 위키는 그 자체로 git repo이므로 버전 관리·브랜칭·협업이 무료로 따라온다 [source: sources/articles/2026-05-18-karpathy-llm-wiki.md].

## 작동하는 이유

- 지식 베이스 유지의 병목은 읽기·사고가 아니라 bookkeeping(교차 참조 갱신, 요약 최신화, 모순 표시, 일관성 유지)이다. 사람은 유지 비용이 가치보다 빨리 자라 위키를 포기한다 [source: sources/articles/2026-05-18-karpathy-llm-wiki.md].
- LLM은 지치지 않고, cross-reference 갱신을 잊지 않고, 한 번에 15개 파일을 건드릴 수 있어 유지 비용이 0에 수렴한다 [source: sources/articles/2026-05-18-karpathy-llm-wiki.md].

## 적용 도메인

개인 저널·헬스/심리, 깊은 리서치, 책 한 권을 읽으며 동반 위키 구축, 회사/팀 내부 위키(Slack·미팅·고객 통화 입력), 경쟁사 분석, due diligence, 여행 계획, 강의 노트, 취미 deep-dive 등 — 시간에 걸쳐 지식이 누적되는 모든 도메인 [source: sources/articles/2026-05-18-karpathy-llm-wiki.md].

## See also

- [[karpathy]] — 패턴 제안자
- [[rag]] — 대조되는 기존 방식
- [[memex]] — 1945년의 사상적 선조
- [[vannevar-bush]] — Memex 제안자
- [[personal-knowledge-management]] — 상위 도메인

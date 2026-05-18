# Wiki Schema

> LLM이 이 위키를 ingest/query/lint 할 때 반드시 따라야 하는 규칙. 이 문서는 수동으로 사람이 관리한다.

## 원칙

1. **Source는 불변(immutable)**. `sources/`의 파일은 절대 수정하지 않는다. 새 정보가 오면 새 source 파일로 추가하고, `wiki/`만 재작성한다.
2. **모든 주장은 인용**. wiki 페이지의 사실 주장(claim)은 반드시 `[source: sources/<path>]` 형식으로 출처를 단다. 추론·종합은 별도 표기.
3. **하나의 사실은 한 곳에**. 같은 정보가 두 페이지에 중복되면 한 곳을 정본(canonical)으로 두고 다른 곳은 `[[wikilink]]`로 참조.
4. **현재형으로 쓴다**. "Karpathy는 ~라고 주장했다"가 아니라 "Karpathy의 LLM 위키 패턴은 ~이다 [source: ...]". 단, 시점이 중요한 사실(발표일, 버전 등)은 날짜를 명시.
5. **추가는 보수적으로, 삭제는 적극적으로**. 확실하지 않은 정보는 추가하지 말 것. 모순되거나 outdated된 정보는 즉시 제거.

## 디렉토리

| 경로 | 용도 | 누가 쓰나 |
|---|---|---|
| `sources/articles/` | 웹 아티클, 블로그 (markdown 변환본) | LLM (ingest 시 저장) |
| `sources/pdfs/` | 논문, 책 (원본 PDF + 추출된 .txt) | 사람 (PDF 넣기) + LLM (txt 추출) |
| `sources/transcripts/` | 유튜브 자막, 강연 transcript | 사람 (yt-dlp로 받기) |
| `sources/notes/` | 직접 쓴 노트, 회의록, 메모 | 사람 |
| `wiki/people/` | 인물 페이지 (1인 1파일) | LLM (사람 검수) |
| `wiki/concepts/` | 추상 개념 페이지 | LLM |
| `wiki/topics/` | 주제·도메인 페이지 (여러 개념을 묶음) | LLM |
| `wiki/index.md` | 토픽 허브, 최상위 탐색 | LLM |

## Source 파일 형식

각 source 파일은 markdown으로 저장하되 frontmatter 필수:

```markdown
---
id: <kebab-case-slug>
type: article | pdf | transcript | note
title: <원본 제목>
url: <원본 URL, pdf/note는 생략>
author: <저자>
published: <YYYY-MM-DD, 모르면 생략>
ingested: <YYYY-MM-DD>
tags: [tag1, tag2]
---

<원본 본문 또는 본문에서 추출한 markdown>
```

파일명: `sources/<type>/<YYYY-MM-DD>-<slug>.md`

## Wiki 페이지 형식

```markdown
---
title: <페이지 제목>
type: person | concept | topic
aliases: [<별칭1>, <별칭2>]
updated: <YYYY-MM-DD>
sources: [sources/articles/foo.md, sources/pdfs/bar.md]
---

# <제목>

> 1-2문장 TL;DR. 이 페이지가 무엇에 대한 것인지.

## <섹션>

내용 작성. 사실 주장은 반드시 인용:

- LLM 위키 패턴은 ingest/query/lint 3가지 워크플로우로 구성된다 [source: sources/articles/2026-05-18-karpathy-llm-wiki.md].

추론·종합 표시:

> **Synthesis** (from: sources/articles/foo.md, sources/articles/bar.md): 이 패턴은 RAG와 달리 "한 번 컴파일, 계속 유지" 방식이다 — 매 쿼리마다 retrieval하지 않아 latency가 낮다.

## See also

- [[rag]]
- [[karpathy]]
```

파일명: `wiki/<type>/<kebab-case-slug>.md` (예: `wiki/people/karpathy.md`)

### Frontmatter 세부 규약

- **`updated:`** — `YYYY-MM-DD`. 같은 날 여러 번 갱신된 경우의 정확한 순서는 `.meta/ingest-log.jsonl`의 ISO-8601 타임스탬프가 정본.
- **`sources:`** — 시간순(오래된 것 먼저). 새 ingest는 배열 끝에 append. 같은 날 추가된 항목 간 순서는 의미 없음.
- **`aliases:`** — 검색·역참조 보조용. 표제어 자체는 포함하지 않는다.

### 인용 세부 규약

- **단일 사실 주장**: 문장 끝에 `[source: <path>]`.
- **여러 source가 한 주장을 뒷받침**: `[source: <path1>, <path2>]` (콤마 구분, 시간순).
- **표(table)**: 행마다 인용이 다르면 셀 안에 직접, 표 전체가 한 source면 표 바로 아래 한 줄로 `[source: <path>]`.
- **Synthesis 블록**: `> **Synthesis** (from: <path1>, <path2>): ...` — 합성에 사용된 source를 명시. 단일 source의 직접 인용이면 Synthesis가 아니라 일반 인용으로 표기.

### 엔티티 페이지 생성 임계값

새 위키 페이지는 **substantive claim 최소 1개**(한 줄 이상의 인용 가능한 사실)가 있을 때만 만든다. 그렇지 않은 언급은 본문 산문에서 외부 링크나 평문으로 처리하고 페이지를 만들지 않는다. 예시: gist에서 단 한 번 "qmd를 쓸 수 있다"고만 언급된 도구는 페이지 없음 — `[qmd](https://...)` 외부 링크로 충분.

## 링크 규약

- 내부 링크: `[[slug]]` (Obsidian 스타일). slug는 파일명에서 `.md` 제거한 것.
- 외부 링크: `[label](https://...)`.
- 깨진 wikilink(존재하지 않는 페이지)는 lint가 검출 → 신규 페이지 생성 후보로 리포트.

## Ingest 작업 순서

1. source 파일을 `sources/<type>/`에 frontmatter와 함께 저장
2. 본문에서 핵심 엔티티(인물·개념·도구·주장) 추출
3. 각 엔티티에 대해:
   - 기존 `wiki/` 페이지 존재? → 새 정보로 보강 (인용 추가, 모순 시 사람 검수 요청)
   - 없음? → 새 페이지 생성
4. 변경된 페이지의 `sources:` frontmatter에 새 source 추가, `updated:` 갱신
5. `.meta/ingest-log.jsonl`에 한 줄 추가:
   ```json
   {"ingested_at": "2026-05-18T10:34:00Z", "source": "sources/articles/...", "wiki_changed": ["wiki/concepts/llm-wiki.md", "wiki/people/karpathy.md"]}
   ```

## Lint 체크 항목

- [ ] 깨진 wikilink (`[[X]]`인데 `wiki/`에 X가 없음)
- [ ] 고아 페이지 (어떤 페이지에서도 링크되지 않음, index.md 제외)
- [ ] 인용 없는 사실 주장 (`source:` 표기 없는 단정문)
- [ ] 중복 페이지 (같은 주제로 보이는 페이지 2개 이상)
- [ ] 모순 (같은 사실에 대해 페이지마다 다른 진술)
- [ ] outdated source (페이지의 sources가 모두 1년 이상 전이고 빠르게 변하는 주제)

## 기록 안 하는 것

- 의견·감상 (가치 판단). 노트로 sources/notes/에 별도 저장하되 wiki/에는 반영하지 않음. (위키는 검증 가능한 합성을 위한 공간)
- ephemeral 정보 (날씨, 일정 등)
- 비밀번호·개인정보

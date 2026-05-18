# CLAUDE.md — LLM Operating Rules for This Wiki

> 이 파일은 Claude(또는 동등한 LLM agent)가 이 저장소에서 ingest/query/lint를 수행할 때 **항상 먼저 읽어야** 하는 운영 entry point다. 상세 규약은 `.claude/references/`로 분기되어 있으며, 각 reference는 **필요한 작업이 발생할 때만** Read한다.

## 1. 위키 스코프

이 위키의 **1차 source**는 예수 그리스도 후기성도 교회(The Church of Jesus Christ of Latter-day Saints)의 공식 자료다.

| 등급 | 기준 |
| --- | --- |
| **1차** | 교회 공식 발간물·연설·경전. 도메인: `churchofjesuschrist.org`, `speeches.byu.edu`, `newsroom.churchofjesuschrist.org`. 화자: 사도·선지자·일반 권위자(General Authority) |
| **보조** | 1차 source가 *명시적으로 인용·참조한* 외부 자료 (그 인용 맥락 안에서만) |
| **스코프 외** | 그 외 자료. 사용자 명시 요청 시 별도 클러스터로 유지하되, 신앙 클러스터와 cross-link는 1차 source가 그 연결을 명시할 때만 |

## 2. 지시 우선순위 (충돌 시 위가 우선)

1. **사용자 명시 지시** (현재 대화)
2. **CLAUDE.md** (이 파일 — entry + 스코프)
3. **`.claude/references/*.md`** (이 파일이 pointer로 가리키는 상세 규약)
4. **SCHEMA.md** (위키 구조·인용 규약)
5. **개별 skill SKILL.md** (ingest/query/lint 절차)
6. 일반 LLM 기본 거동

## 3. Reference 인덱스

작업 종류별로 필요한 reference만 Read. **자동 로드되지 않음** — 명시 Read 필요.

| 파일 | 언제 Read | 다루는 것 |
| --- | --- | --- |
| [`.claude/references/glossary.md`](.claude/references/glossary.md) | 매 ingest·query 시작 (글쓰기 전 권장) | 교회 명칭, 사도·선지자 호칭, 경전, 핵심 교리 용어 표, 공식 문서 인용 형식, 본문 언어 정책 |
| [`.claude/references/ingest-protocols.md`](.claude/references/ingest-protocols.md) | ingest 작업 시작 시 | Source 관리 (불변/삭제/타입/다국어/SPA/published), Wiki 페이지 관리 (임계값/직함/succession), 인용 hierarchy + 위치 표기, 충돌·정리 |
| [`.claude/references/guardrails.md`](.claude/references/guardrails.md) | source 평가 시 / 분기별 audit | Sensitivity (위키 포함 금지), Copyright |
| [`.claude/references/lint.md`](.claude/references/lint.md) | wiki-lint skill 시 | Lint 체크 항목 + 자동화 명령어 |

## 4. 핵심 must-know (요약)

자세한 내용은 위 references에 있으나, 다음은 매 작업에 적용되는 핵심:

- **`sources/` 본문은 원문 보존, `wiki/`에만 정규화 적용** (SCHEMA §원칙 1).
- **공식 용어 핵심 3가지** (자세한 표는 `glossary.md`):
  - 약어 "LDS" 단독 사용 금지 / "Mormon" 단독 사용 금지 (예외: *Book of Mormon* 등)
  - 사도 = "Elder [Last Name]", 칠십인 = "Elder [Last Name] of the Seventy" (첫 언급 누락 금지)
  - "God" → "하나님" / "moral agency" → "도덕적 선택의지" (LDS 공식 한국어)
- **본문 언어**: wiki는 한국어 산문 + 핵심 영어 용어 그대로, 인용은 항상 원문 보존.
- **모든 사실 주장**에 `[source: sources/...]` 인용 (SCHEMA §원칙 2).
- **CONFLICT 마커는 활성 분쟁에만**. 해소 시 마커 제거, audit trail은 `ingest-log.jsonl`로.

## 5. 작업 절차

### 5.1. SCHEMA.md 로드 의무

`SCHEMA.md`는 자동 로드되지 않음. 각 wiki skill 시작 시 Read 의무 (skill SKILL.md의 "Read SCHEMA.md first").

재 Read 강제 트리거:

- SCHEMA.md를 본 세션에서 수정한 직후.
- context compaction 의심 시.
- 세션 시작 후 처음 wiki 작업 시.

(같은 세션 내 미수정이면 캐시 인정.)

### 5.2. References 로드 패턴

Reference도 자동 로드 X. 작업 시작 시 §3 표에 따라 필요한 reference를 Read.

- **ingest**: `glossary.md` + `ingest-protocols.md` (+ source가 민감 영역 의심 시 `guardrails.md`)
- **query**: `glossary.md` (인용·답변 형식)
- **lint**: `lint.md` (+ 필요 시 `ingest-protocols.md` §4 충돌·정리)

세션 내 캐시 인정. 단 reference를 본 세션에서 수정했다면 재 Read.

### 5.3. Ingest 핵심 규칙 (요약)

1. Source 본문은 원문 그대로 (공식 용어 정규화는 `wiki/`에만).
2. 인물 페이지 직함은 현 시점 기준 (Succession 시 `ingest-protocols.md` §2.4).
3. 직접 인용은 원문 언어 보존.
4. 비-LDS 자료 ingest 시 §1 스코프 규칙 적용.
5. 신규/수정 wiki 페이지는 frontmatter + 모든 사실 주장에 `[source: ...]` + 깨진 wikilink 없음.
6. 매 ingest마다 `.meta/ingest-log.jsonl`에 한 줄.

### 5.4. Query 핵심 규칙 (요약)

- 답변·요약은 `glossary.md` §A–G 적용.
- 사도·선지자 인용에는 항상 source 경로.
- 사용자가 비공식 용어로 질문해도 답변은 공식 용어로 (정정은 X, 답변만 공식).
- 위키에 정보 없으면 "위키에 관련 정보 없음" 명시. 외부 지식은 "(외부 지식)" 태그.

## 6. 참고

- `SCHEMA.md` — 위키 디렉토리·frontmatter·인용 규약 (권위 source)
- `.meta/ingest-log.jsonl` — 모든 ingest·삭제·CONFLICT 결정의 audit trail
- [Newsroom Style Guide](https://newsroom.churchofjesuschrist.org/style-guide)
- President Russell M. Nelson, "The Correct Name of the Church" (October 2018 General Conference)

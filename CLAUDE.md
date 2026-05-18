# CLAUDE.md — LLM Operating Rules for This Wiki

> 이 파일은 Claude(또는 동등한 LLM agent)가 이 저장소에서 ingest/query/lint를 수행할 때 **항상 먼저 읽어야** 하는 운영 규칙이다. SCHEMA.md는 위키 구조의 사양이고, 이 파일은 위키의 **스코프**와 **용어 규약**을 정의한다.

## 1. 위키 스코프 (Scope)

이 위키는 **예수 그리스도 후기성도 교회**(The Church of Jesus Christ of Latter-day Saints)의 공식 자료를 1차 source로 삼는다.

- **1차 source**: 교회의 공식 발간물·연설·경전·공식 웹사이트(`churchofjesuschrist.org`, `speeches.byu.edu`, `newsroom.churchofjesuschrist.org` 등) — 사도, 선지자, 일반 권위자(General Authority)의 발언 및 공식 출판물.
- **보조 source**: 1차 source가 명시적으로 인용·참조한 외부 자료(예: _Antiqua et Nova_ 같은 다른 신앙 전통 문서, 학술 논문, 역사적 인물의 언설)는 그 인용 맥락 안에서만 wiki에 포함한다.
- **범위 밖**: 본 교회 공식 입장과 무관한 일반 기술·지식 자료라도, 사용자가 명시적으로 ingest를 요청하면 별도 클러스터로 유지하되, 신앙 관련 페이지와의 cross-link는 1차 source가 그 연결을 명시할 때에만 만든다.

## 2. 공식 용어 (Required Terminology)

교회의 공식 [Style Guide](https://newsroom.churchofjesuschrist.org/style-guide) 원칙을 따른다. 핵심 규칙:

### 교회 명칭

| ✅ 사용                                             | ❌ 사용 금지 / 회피 |
| --------------------------------------------------- | ------------------- |
| The Church of Jesus Christ of Latter-day Saints     | The Mormon Church   |
| 예수 그리스도 후기성도 교회                         | 몰몬 교회           |
| the Church (이미 본문에서 풀네임이 한 번 등장한 후) | LDS Church          |
| the restored Church of Jesus Christ                 | the Saints' Church  |
| 첫 언급 후: the Church of Jesus Christ              | —                   |

- **약어 "LDS" 단독 사용 금지**. 부득이한 경우(URL slug, 태그 등 기술적 식별자)에만 허용.
- **"Mormon" 단독 사용 금지** — 단, 다음은 예외: _Book of Mormon_ (경전 명), Mormon Tabernacle Choir의 옛 명칭(역사적 문맥), 선지자 Mormon(인물).
- 멤버 호칭: **"member of the Church"**, **"Latter-day Saint"**, **"Latter-day Saint Christian"**. ❌ "Mormon" / "Mormons".

### 사도·선지자 호칭

- 십이사도 정원회: **the Quorum of the Twelve Apostles** (약어 사용 금지)
- 사도 개인: **Elder [Last Name]** (예: Elder Gong, Elder Bednar) — 초기 언급 시 정식 직함을 풀어 쓴다: "Elder Gerrit W. Gong of the Quorum of the Twelve Apostles".
- 제일회장단 / 교회장: **President [Last Name]** (예: President Russell M. Nelson). 교회 회장 풀네임은 "President of The Church of Jesus Christ of Latter-day Saints".
- 칠십인 정원회: **the Quorum of the Seventy**. 호칭은 **Elder [Last Name] of the Seventy** — 첫 언급에서 "of the Seventy" 누락 금지(사도와 동일한 "Elder" 직함이라 정원회 구분이 중요). 예: "Elder John C. Pingree of the Seventy", "Elder Ronald M. Barcellos of the Seventy".

### 경전 (the Standard Works)

- **the Holy Bible** (KJV 기본)
- **the Book of Mormon: Another Testament of Jesus Christ** (부제 포함이 공식, 짧게는 "the Book of Mormon")
- **the Doctrine and Covenants** (약어 D&C는 본문 인용에서 허용)
- **the Pearl of Great Price**
- 한국어: 성경, 몰몬경(또 하나의 예수 그리스도의 성약), 교리와 성약, 값진 진주

### 핵심 교리 용어

| 한국어                    | 영어 (공식)                                                                 | 비고                                                                                                        |
| ------------------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **하나님**                | **God**                                                                     | **일반어 "신" 단독 사용 금지 — LDS 공식 번역은 "하나님"**                                                   |
| 하나님 아버지 / 천부      | Heavenly Father / the Father                                                | 첫 언급은 "하나님 아버지", 약식 "천부"는 본문 흐름상 자연스러울 때                                          |
| 영원하신 아버지           | the Eternal Father                                                          |                                                                                                             |
| 주 / 주님                 | the Lord                                                                    |                                                                                                             |
| 구주                      | Savior                                                                      |                                                                                                             |
| 구속주                    | Redeemer                                                                    |                                                                                                             |
| 전능하신 (분)             | (the) Almighty                                                              |                                                                                                             |
| 신성 / 신성한             | Divine / divine                                                             | 명사 "Divine/Deity"는 "신성" 또는 "하나님" — 단독 "신" 금지. 형용사 "신적", "신성한"은 OK (예: "신적 영감") |
| 구원의 계획 / 행복의 계획 | the plan of salvation / the plan of happiness / the great plan of happiness | 본문 맥락에 맞게                                                                                            |
| 복원된 복음               | the restored gospel of Jesus Christ                                         | "예수 그리스도의" 수식 유지 권장                                                                            |
| 속죄                      | the Atonement of Jesus Christ                                               | 단독 "Atonement"는 두 번째 언급 이후 허용                                                                   |
| 도덕적 선택의지           | moral agency                                                                | LDS 공식 번역. "도덕 행위성" / "free will" 사용 금지 (2026-05-18 사용자 명시)                               |
| 언약의 길                 | the covenant path                                                           |                                                                                                             |
| 언약적 소속               | covenant belonging                                                          |                                                                                                             |
| 성신                      | the Holy Ghost / the Spirit                                                 | 일관되게                                                                                                    |
| 신권                      | the priesthood                                                              |                                                                                                             |
| 회복                      | the Restoration (대문자)                                                    | 1820년대 이후 사건 지칭                                                                                     |
| 만세 시대의 충만          | the dispensation of the fulness of times                                    |                                                                                                             |

> **중요 (사용자 명시 정정 2026-05-18)**: 영문 인용을 한국어 산문으로 옮길 때 **God = 하나님** 일관 적용. "AI is not God" → "AI는 하나님이 아니다" (X "AI는 신이 아니다"). 단, 영문 원문 직접 인용 안은 보존 (CLAUDE.md §9.2). Lint 검출: `grep -rn '\b신[이은을의과께]' wiki/` 후 compound (신체·신앙·신뢰·신학·신성·신적·신중·신권·신호·미신·자신 등) 제외.

### 제도·조직

- **the First Presidency** (제일회장단)
- **General Conference** (연차 / 반년차)
- **temple / temples** (성전) — 특정 성전은 풀네임 (예: Newport Beach California Temple)
- **stake / ward / branch** (스테이크 / 와드 / 지부)
- **sacrament meeting / Sunday School / Primary / Relief Society / Young Men / Young Women / Elders Quorum**
- **missionary / missionaries**, **the work of salvation and exaltation**

### 공식 문서 인용 형식

- **General Handbook**: 인용 시 정식 명칭은 _General Handbook: Serving in The Church of Jesus Christ of Latter-day Saints_. 본문 인용은 섹션 번호로 — **§38.8.48** (장.절.항 형식). 하위 절은 **§38.8.48.1**, **§38.8.48.3** 등.
- **For the Strength of Youth**: 인용 시 정식 명칭 _For the Strength of Youth: A Guide for Making Choices_ (현행판은 2022) 또는 _For the Strength of Youth_ 매거진(_FSOY_).
- **Liahona / Ensign**: 호 인용 — _Liahona_, May 2018, 94 형식.
- **General Conference**: April / October + 연도. 예: "April 2020 general conference".

## 3. Ingest 시 적용 규칙

1. 1차 source에서 등장한 용어가 위 가이드와 다르면 **공식 용어로 정규화**해서 wiki 페이지에 기록한다. 다만 source 파일 자체(`sources/`)는 원문 보존 — 절대 수정 금지(SCHEMA.md §원칙 1).
2. 인물 페이지의 직함은 source 시점이 아니라 **현 시점 기준**으로 작성하되, 과거 직함이 source의 맥락에서 중요하면 본문에 명시한다. (예: 2009년 발언이지만 현재도 사도라면 "Elder Bednar".)
3. 페이지 제목 표제어와 `aliases:`에는 공식 용어를 우선 두고, 비공식 표현(예: "LDS Apostle", "Mormon")은 검색용으로 aliases에 한정 등재 가능.
4. 직접 인용은 원문을 그대로 옮긴다. 인용 안의 비공식 용어는 수정하지 않는다 (왜곡 금지).
5. 사용자가 외부(비교회) 자료를 ingest 요청할 때는 별도 클러스터(예: `[[llm-wiki]]`, `[[karpathy]]` 클러스터)로 처리하되, 신앙 관련 페이지와의 cross-link는 1차 source가 그 연결을 명시할 때에만 만든다.

## 4. Query 시 적용 규칙

- 답변·요약·인용 모두 위 공식 용어 가이드를 따른다.
- 사도·선지자의 가르침을 인용할 때는 반드시 source 파일 경로를 함께 표기 (SCHEMA.md §인용 세부 규약).
- 사용자가 "Mormon Church" 같은 표현으로 질문해도, 답변은 공식 용어로 한다 (사용자 표현을 정정할 필요는 없으되 정확히 기술).

## 5. Lint 시 추가 체크 항목

SCHEMA.md §Lint 체크 항목에 더해:

- [ ] `wiki/` 내에서 "LDS" 약어 단독 사용 (URL/태그 외)
- [ ] `wiki/` 내에서 "Mormon"이 _Book of Mormon_ / 선지자 Mormon 외 맥락에서 사용
- [ ] 사도 호칭에서 "Elder" / "President" 누락
- [ ] 경전명 약식 사용 (첫 언급에서 풀네임 누락은 권장이지 강제 아님)

## 6. Ingest 운영 학습 (실전 적용)

이 위키를 운영하며 ingest 절차에서 반복 발견된 패턴들. SCHEMA.md를 보완.

### 6.1. 사용자가 텍스트로 직접 제공한 공식 자료

URL fetch 대신 사용자가 본문을 prompt에 붙여넣은 경우(예: _General Handbook_ 발췌):

- **type**: `note` 사용 (SKILL의 "Free text in prompt → note" 규칙 유지).
- **저장 위치**: `sources/notes/<YYYY-MM-DD>-<slug>.md`.
- **frontmatter**: `url` 생략 가능. `author`는 출판 주체(교회 자체이면 "The Church of Jesus Christ of Latter-day Saints"). 본문 머리말에 "Text provided by the user (extracted from ...)" 명시해 provenance 구분.
- 본문에서 인용할 때는 다른 source와 동일한 `[source: sources/notes/...]` 형식.

### 6.2. 다국어 변형 URL

같은 공식 컨텐츠의 다른 언어판(예: `?lang=kor`)이 사용자에 의해 제공되는 경우:

1. 먼저 fetch해서 실제로 다른 컨텐츠인지(번역됐는지) 확인.
2. **컨텐츠가 동일(미번역)** → 별도 source 파일 생성 금지. ingest log에 `multilingual_variant` 메모만 남긴다.
3. **컨텐츠가 실제 번역됨** → 별도 source 파일 생성. 영어 source의 frontmatter나 본문 머리말에 `translations:` 또는 "Translations:" 섹션으로 상호 참조.
4. wiki 페이지의 본문 인용은 항상 영어 권위본을 1차로, 번역본은 보조.

### 6.3. 페이지가 없는 인물의 본문 표기

CLAUDE.md §1의 임계값(substantive claim 1개 미만)으로 인물 페이지를 만들지 않기로 결정한 사람을 본문에서 언급할 때:

- **wikilink 사용 금지** — 깨진 링크 발생.
- **첫 언급에서 풀네임 + 직함**을 산문으로: "Elder John C. Pingree of the Seventy", "Elder Ronald M. Barcellos of the Seventy", "President Russell M. Nelson".
- 이후 언급은 짧은 형식 가능: "Elder Pingree", "Elder Barcellos".
- 향후 ingest로 substantive claim이 누적되면 페이지 신설.

### 6.4. 인용 위치 부가 표기

긴 source에서 특정 위치(footnote, 섹션)를 정확히 지목할 때 `[source: ...]` 뒤에 괄호로 부가 표기:

- footnote: `[source: sources/articles/foo.md] (footnote vi)`
- 핸드북 절: `[source: sources/notes/foo.md] (§38.8.48.3)`
- 인용된 강연 시점: `[source: sources/articles/foo.md] (Rome 2025-10)` — 동일 인물이 여러 무대에서 같은 명제를 변형 발언하는 경우.

부가 표기는 권장이지 강제 아님.

### 6.5. 다년·다무대 시리즈 표

동일 인물·개념이 여러 무대에서 반복 다뤄지는 경우(예: Elder Gong의 Istanbul → BYU → Rome 시리즈), 인물·개념 페이지에 **"주요 무대" 표**를 추가하면 시간순 진화를 한눈에 볼 수 있다. 권장 형식: `날짜 | 자리 | 주제 [source: ...]`.

### 6.6. 사도가 다른 사도를 인용하는 경우

Elder Gong이 Elder Bednar의 명제를 다시 인용하는 식의 사례:

- 두 source 모두 인용 권장: `[source: <bednar-source>, <gong-source>]` (시간순).
- 단, Bednar 원문이 wiki에 이미 ingest됐다면 wiki 페이지에서 다시 인용할 때 Gong의 second-hand만 인용해도 무방. 핵심은 _원전_이 트래킹 가능해야 한다는 것 — Gong source의 본문에는 원전 정보가 들어 있으므로 chain은 유지된다.

### 6.8. SCHEMA.md 로드 의무

`CLAUDE.md`는 Claude Code가 세션 시작 시 자동 로드하지만 **`SCHEMA.md`는 자동 로드되지 않는다**. 다음 규칙을 따른다:

- **각 wiki skill (`wiki-ingest`, `wiki-lint`, `wiki-query`) 작업 시작 시 `SCHEMA.md`를 Read 의무**. skill SKILL.md의 "Read SCHEMA.md first" 지시를 그대로 따른다.
- **세션 내 캐시 인정**: 같은 세션에서 이미 Read했고 그 후 SCHEMA가 수정되지 않았다면 재 Read 생략 가능.
- **재 Read 강제 트리거**:
  - SCHEMA.md를 본 세션에서 직접 수정한 직후 (다음 wiki 작업 전).
  - 컨텍스트 압축(context compaction)이 일어났다고 의심될 때.
  - 세션 시작 후 처음 wiki 작업에 들어갈 때.
- CLAUDE.md만으로는 인용 규약·디렉토리 매핑 등 SCHEMA의 핵심 정보가 부족하므로 SCHEMA를 임베드로 복사하지 않는다 — sync drift 방지.

### 6.9. Source 본문의 published 날짜 추출

URL이 발표/게재 날짜를 query string·meta·본문 머리말 등 다양한 곳에 둠. fetch 후 본문에서 명확한 published 날짜를 찾을 수 없으면:

- URL 경로의 연-월(예: `/2024/11/`)을 1차 추정으로 사용.
- 본문에 "delivered on ... at ..." 같은 명시가 있으면 그것을 우선.
- 끝내 모르면 `published:` 필드 생략 (SCHEMA가 허용).
- `ingested:`는 항상 오늘 날짜.

## 7. 자료 처리 가드레일

### 7.1. Sensitivity — 위키에 절대 포함하지 않는 것

_General Handbook_ §38.8.48.3의 정신을 이 위키 운영 차원으로 확장:

- **회원 개인정보** — 이름, 연락처, 주소, 가족 관계 등 식별 가능 정보. 단, 일반 권위자(General Authority)의 공개된 약력은 1차 source(예: Istanbul footnote의 Elder Gong 약력)에 한해 인용 가능.
- **신권 회의록 / 비공개 모임 메모** — Bishopric, Stake Presidency, Elders Quorum, Relief Society 등 비공개 회의 내용.
- **사적 영적 체험** — 본인 또는 타인의 개인 계시, 환상, 치유 체험. 단, 사도/선지자가 공개 발언에서 직접 공유한 것은 인용 가능 (예: Elder Barcellos의 São Paulo 선교 _몰몬경_ 확증 체험은 공개 강연에서 본인이 공유했으므로 OK).
- **성전 의식의 비공개 부분** — 성전 의식의 약속·언어·세부 사항.
- **AI 시스템에 입력 금지된 정보** — Church 기록·회원 데이터·기밀 통신을 외부 AI 도구로 처리한 결과물은 어떤 형태로든 위키에 반영 금지.

이 가드레일은 wiki/, sources/ 양쪽 모두에 적용. 발견 시 즉시 제거.

### 7.2. Copyright

- 교회 공식 컨텐츠(연설·아티클·핸드북·_Liahona_/_Ensign_ 등)는 **© Intellectual Reserve, Inc.** All rights reserved.
- 이 위키가 개인 학습·연구 용도로 운영되는 한 source 본문 통째 저장은 fair use 범주. 단, 위키를 공개·배포할 때는 운영자가 별도로 인용 정책을 검토해야 한다 (전체 본문 재배포는 fair use 범위를 넘을 수 있음).
- 위키 페이지(`wiki/`)의 합성·요약·구조화는 운영자의 저작이지만, 직접 인용된 문구는 여전히 원저작권자에게 귀속됨 — 인용 표기로 출처를 명확히 한다.

## 8. 인용 신뢰도 Hierarchy

같은 명제·사건이 여러 source에 등장할 때, 위키 페이지의 claim에 단 source는 다음 우선순위로 선택한다:

| 등급                | 종류                                                          | 예시                                                                                                                                                         |
| ------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **1차 (원전)**      | 사도·선지자 본인의 speech, article, book; 교회 공식 문서 원문 | `bednar-things-as-they-really-are-2-0.md`; `general-handbook-38-8-48-ai.md`; `church-ai-learn-page.md`                                                       |
| **2차 (보도/요약)** | Newsroom 발표 보도, 공식 매거진 요약, Press release           | `newsroom-church-ai-guiding-principles.md` (2024-03-13 발표를 Newsroom이 요약)                                                                               |
| **3차 (재인용)**    | 다른 사도·기자가 1차 source를 인용한 것                       | `ftsoy-7-advantages-latter-day-saint-ai.md` (Bednar/Gong을 FSOY 기자가 인용); `gong-istanbul-faith-ethics-ai-call-to-action.md` (President Nelson 인용 부분) |

**규칙:**

- 가능하면 **1차 source를 우선 인용**. 1차가 이 위키에 ingest되어 있으면 거기서 직접.
- 1차 source가 없을 때만 2차/3차로 대체.
- 1차와 2차가 같은 명제를 다르게 표현하면 1차의 표현을 우선 채택하되, 2차에 추가 맥락(예: 발표 자리·청중·반응)이 있으면 별도 bullet으로 추가.
- 1차가 위키에 없는데 3차에서 인용된 경우 — `[source: <3차>]` 사용하되, 페이지 본문에 "원전 인용: <원전 title>"을 산문으로 명시하고 향후 1차 ingest 후보로 표시.

**예외**: 같은 명제가 사도 본인이 여러 무대(Istanbul → BYU → Rome)에서 변형 발언한 경우, 모두 1차로 취급하고 시간순으로 모두 인용 가능: `[source: <istanbul>, <byu>, <rome>]`.

## 9. 본문 언어 정책

### 9.1. wiki 페이지 본문

- **한국어 산문** + **핵심 영어 용어는 영어 그대로**.
- 사도·선지자 호칭, 정원회·기관 명칭, 핵심 교의 용어(moral agency, covenant belonging, Holy Ghost, plan of salvation 등), 경전 서명 등은 §2 공식 용어대로 영어 유지. 한국어 번역이 더 자연스러우면 첫 등장에서 "도덕적 선택의지(moral agency)"처럼 병기.
- 표 헤더, frontmatter는 영어 우선. body는 한국어.

### 9.2. 인용

- **항상 원문 언어 보존**. 영어 source에서 인용하면 영어로, 한국어 source에서 인용하면 한국어로.
- 본인이 의역·번역을 한 경우 명시: `> [원문] ...` + `> [의역] ...` 형식. 위키에서 사도의 명제를 한국어 번역으로 옮기는 것은 권장하지 않음 — 원문 우선.

### 9.3. 페이지 제목과 slug

- 페이지 제목(`title:`)은 source의 원어를 따른다 — Elder Gong, Things as They Really Are 등 영어.
- slug는 영어 kebab-case (검색·URL 안정성).
- 한국어 alias가 자주 검색될 가능성이 있으면 `aliases:` 배열에 한국어 표기 추가.

## 10. Lint 자동화 명령어

SCHEMA.md §Lint 체크 항목과 CLAUDE.md §5의 추가 항목을 빠르게 점검하는 실용 명령어. wiki 루트(`/Users/young/Documents/Workspace/llm-wiki`)에서 실행 가정.

### 10.1. 용어 위반 검출

```bash
# "LDS" 단독 사용 (URL/태그 제외)
grep -rn '\bLDS\b' wiki/ | grep -v 'sources/' | grep -v 'tags:'

# "Mormon" 단독 사용 (Book of Mormon / 선지자 Mormon 외)
grep -rn '\bMormon\b' wiki/ | grep -v 'Book of Mormon' | grep -v 'sources/'

# 사도 호칭에서 "Elder" / "President" 누락 추정 (성만 단독)
grep -rEn '\b(Gong|Bednar|Nelson|Pingree|Barcellos)\b' wiki/ | \
  grep -vE '\b(Elder|President|Sister|Brother)\s+(Gerrit|David|Russell|John|Ronald)'
```

### 10.2. 깨진 wikilink

```bash
# 모든 wikilink 추출
grep -rohE '\[\[([a-z0-9-]+)' wiki/ | sed -E 's/\[\[([a-z0-9-]+).*/\1/' | sort -u > /tmp/wl_used.txt

# 존재하는 wiki 페이지 slug
find wiki/ -name '*.md' -exec basename {} .md \; | sort -u > /tmp/wl_existing.txt

# 깨진 링크 (참조됐지만 존재하지 않음)
comm -23 /tmp/wl_used.txt /tmp/wl_existing.txt
```

### 10.3. 인용 없는 단정문 휴리스틱

```bash
# 마침표·물음표·느낌표로 끝나지만 같은 줄에 [source: 가 없는 행
grep -rn -E '[.!?]\s*$' wiki/ | grep -v '\[source:' | grep -v '>' | grep -v '^#'
```

(휴리스틱이므로 false positive 많음 — 결과를 사람이 검토.)

### 10.4. 고아 페이지 (인바운드 링크 없음)

```bash
for f in $(find wiki/ -name '*.md' ! -name 'index.md'); do
  slug=$(basename "$f" .md)
  count=$(grep -rl "\[\[$slug" wiki/ | grep -v "$f" | wc -l)
  if [ "$count" -eq 0 ]; then echo "ORPHAN: $f"; fi
done
```

### 10.5. Source staleness

```bash
# 한 페이지의 모든 source가 N년 이상 전이면 표시 (빠르게 변하는 주제용)
# 수동: 각 페이지 frontmatter sources: 의 published 날짜 확인
grep -rn 'published:' sources/ | sort
```

## 11. 사도 정원회 변동 시 갱신 절차

사도가 별세하거나 회장이 교체되는 등 정원회 구성 변동 시:

### 11.1. 갱신

- **wiki/people/`<person>`.md**의 frontmatter `title:`과 본문 첫 줄(직함) 갱신.
- **wiki/index.md**의 인물 묘사 갱신.
- 새 회장이 교체되면 **CLAUDE.md §참고**의 권위 출처 인용도 점검.
- **wiki/topics/ai-and-faith.md** 등 타임라인이 있는 페이지에서 신규 사건(예: 새 사도 임명, 새 가르침) 추가.

### 11.2. 갱신하지 않음 (SCHEMA §1 불변)

- **sources/ 파일 본문은 절대 수정 금지**. 과거 source는 그 시점의 직함 그대로 유지 (예: Elder Gong이 칠십인이었던 시기의 source가 있다면 그 호칭 그대로).
- 직함 변동의 _시간 정보_가 중요해지면 **wiki/people/`<person>`.md**의 별도 "Historical positions" 섹션에 명시.

### 11.3. 인용 처리

- wiki 페이지에서 사도를 호명할 때는 **현 시점 직함**을 사용 (`Elder Gong` 또는 `President Gong`). 예외: source 인용 맥락에서 그 시점 직함이 정확성에 중요하면 원래 직함 유지.
- "이전 직함이었던 ...로서 ... 발언했다" 같은 historical context가 의미 있으면 산문으로 명시.

## 12. 우선순위

지시가 충돌하면 다음 우선순위를 따른다 (위가 우선):

1. **사용자의 명시적 지시** (현재 대화)
2. **CLAUDE.md** (이 파일) — 위키 스코프·용어
3. **SCHEMA.md** — 위키 구조·인용 규약
4. **개별 skill SKILL.md** — wiki-ingest / wiki-query / wiki-lint 절차
5. 일반 LLM 기본 거동

## 13. 참고

공식 Style Guide는 분기별로 갱신될 수 있다. 권위 있는 출처:

- [Newsroom Style Guide](https://newsroom.churchofjesuschrist.org/style-guide)
- President Russell M. Nelson, "The Correct Name of the Church" (October 2018 General Conference)

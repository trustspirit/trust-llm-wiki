# CLAUDE.md — LLM Operating Rules for This Wiki

> 이 파일은 Claude(또는 동등한 LLM agent)가 이 저장소에서 ingest/query/lint를 수행할 때 **항상 먼저 읽어야** 하는 운영 규칙이다. SCHEMA.md는 위키 구조의 사양이고, 이 파일은 위키의 **스코프**와 **용어 규약**을 정의한다.

## 1. 위키 스코프 (Scope)

이 위키는 **예수 그리스도 후기성도 교회**(The Church of Jesus Christ of Latter-day Saints)의 공식 자료를 1차 source로 삼는다.

- **1차 source**: 교회의 공식 발간물·연설·경전·공식 웹사이트(`churchofjesuschrist.org`, `speeches.byu.edu`, `newsroom.churchofjesuschrist.org` 등) — 사도, 선지자, 일반 권위자(General Authority)의 발언 및 공식 출판물.
- **보조 source**: 1차 source가 명시적으로 인용·참조한 외부 자료(예: *Antiqua et Nova* 같은 다른 신앙 전통 문서, 학술 논문, 역사적 인물의 언설)는 그 인용 맥락 안에서만 wiki에 포함한다.
- **범위 밖**: 본 교회 공식 입장과 무관한 일반 기술·지식 자료라도, 사용자가 명시적으로 ingest를 요청하면 별도 클러스터로 유지하되, 신앙 관련 페이지와의 cross-link는 1차 source가 그 연결을 명시할 때에만 만든다.

## 2. 공식 용어 (Required Terminology)

교회의 공식 [Style Guide](https://newsroom.churchofjesuschrist.org/style-guide) 원칙을 따른다. 핵심 규칙:

### 교회 명칭

| ✅ 사용 | ❌ 사용 금지 / 회피 |
|---|---|
| The Church of Jesus Christ of Latter-day Saints | The Mormon Church |
| 예수 그리스도 후기성도 교회 | 몰몬 교회 |
| the Church (이미 본문에서 풀네임이 한 번 등장한 후) | LDS Church |
| the restored Church of Jesus Christ | the Saints' Church |
| 첫 언급 후: the Church of Jesus Christ | — |

- **약어 "LDS" 단독 사용 금지**. 부득이한 경우(URL slug, 태그 등 기술적 식별자)에만 허용.
- **"Mormon" 단독 사용 금지** — 단, 다음은 예외: *Book of Mormon* (경전 명), Mormon Tabernacle Choir의 옛 명칭(역사적 문맥), 선지자 Mormon(인물).
- 멤버 호칭: **"member of the Church"**, **"Latter-day Saint"**, **"Latter-day Saint Christian"**. ❌ "Mormon" / "Mormons".

### 사도·선지자 호칭

- 십이사도 정원회: **the Quorum of the Twelve Apostles** (약어 사용 금지)
- 사도 개인: **Elder [Last Name]** (예: Elder Gong, Elder Bednar) — 초기 언급 시 정식 직함을 풀어 쓴다: "Elder Gerrit W. Gong of the Quorum of the Twelve Apostles".
- 제일회장단 / 교회장: **President [Last Name]** (예: President Russell M. Nelson). 교회 회장 풀네임은 "President of The Church of Jesus Christ of Latter-day Saints".
- 칠십인 정원회: **Quorum of the Seventy**. 호칭은 **Elder [Last Name]**.

### 경전 (the Standard Works)

- **the Holy Bible** (KJV 기본)
- **the Book of Mormon: Another Testament of Jesus Christ** (부제 포함이 공식, 짧게는 "the Book of Mormon")
- **the Doctrine and Covenants** (약어 D&C는 본문 인용에서 허용)
- **the Pearl of Great Price**
- 한국어: 성경, 몰몬경(또 하나의 예수 그리스도의 성약), 교리와 성약, 값진 진주

### 핵심 교리 용어

| 한국어 | 영어 (공식) | 비고 |
|---|---|---|
| 구원의 계획 / 행복의 계획 | the plan of salvation / the plan of happiness / the great plan of happiness | 본문 맥락에 맞게 |
| 복원된 복음 | the restored gospel of Jesus Christ | "예수 그리스도의" 수식 유지 권장 |
| 속죄 | the Atonement of Jesus Christ | 단독 "Atonement"는 두 번째 언급 이후 허용 |
| 도덕 행위성 | moral agency | "free will" 대신 |
| 언약의 길 | the covenant path | |
| 언약적 소속 | covenant belonging | |
| 성신 | the Holy Ghost / the Spirit | 일관되게 |
| 신권 | the priesthood | |
| 회복 | the Restoration (대문자) | 1820년대 이후 사건 지칭 |
| 만세 시대의 충만 | the dispensation of the fulness of times | |

### 제도·조직

- **the First Presidency** (제일회장단)
- **General Conference** (연차 / 반년차)
- **temple / temples** (성전) — 특정 성전은 풀네임 (예: Newport Beach California Temple)
- **stake / ward / branch** (스테이크 / 와드 / 지부)
- **sacrament meeting / Sunday School / Primary / Relief Society / Young Men / Young Women / Elders Quorum**
- **missionary / missionaries**, **the work of salvation and exaltation**

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
- [ ] `wiki/` 내에서 "Mormon"이 *Book of Mormon* / 선지자 Mormon 외 맥락에서 사용
- [ ] 사도 호칭에서 "Elder" / "President" 누락
- [ ] 경전명 약식 사용 (첫 언급에서 풀네임 누락은 권장이지 강제 아님)

## 6. 우선순위

지시가 충돌하면 다음 우선순위를 따른다 (위가 우선):

1. **사용자의 명시적 지시** (현재 대화)
2. **CLAUDE.md** (이 파일) — 위키 스코프·용어
3. **SCHEMA.md** — 위키 구조·인용 규약
4. **개별 skill SKILL.md** — wiki-ingest / wiki-query / wiki-lint 절차
5. 일반 LLM 기본 거동

## 참고

공식 Style Guide는 분기별로 갱신될 수 있다. 권위 있는 출처:
- [Newsroom Style Guide](https://newsroom.churchofjesuschrist.org/style-guide)
- President Russell M. Nelson, "The Correct Name of the Church" (October 2018 General Conference)

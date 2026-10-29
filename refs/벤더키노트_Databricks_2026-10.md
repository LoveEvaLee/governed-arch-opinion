# 자료 — Databricks 키노트 「DATA+AI 플랫폼」 (2026-10)

| 항목 | 내용 |
|---|---|
| 원본 | `~/Downloads/[Databricks] 키노트 l DATA+AI 플랫폼.pdf` (43장, 한국어) — raw/는 쓰기 금지라 경로만 기록. PDF는 .gitignore(`*.pdf`) 대상이라 어차피 저장소에 안 올라간다 |
| 출처 | Databricks 공식 키노트 슬라이드 (©2026 Databricks, Inc.). 입수 2026-10-29 유경. 행사 특정 자료 — AWS AI WAVE 2026 추정 〔미정〕 |
| 등급 | **C — 벤더 공식 주장**(제품 구성·방향성 확인용). 슬라이드 속 성능·건수 수치는 전부 **D**(벤더 전후 비교 주장) — 3-2 결정대로 근거로 쓰지 않는다 |
| 용도 | ① 동향수집 3-3(데이터 플랫폼)·3-2 보강(AI/에이전트 플랫폼)의 선택지 후보 식별용. 개별 주장은 공식 문서·독립 출처로 재수집해 등급을 다시 매긴 뒤에만 refs 본문에 넣는다 |

## 키노트 골격

프레임은 "에이전틱 엔터프라이즈를 위한 오픈 Data+AI 플랫폼" — **Context · Control · Cost · Choice** 4개 축으로 전개. AI를 데이터에 연결하는 어려움(Context), AI·데이터 동시 통제(Control), 비용 최적화(Cost), 벤더 종속 회피(Choice)를 문제로 놓고 자사 스택을 답으로 제시한다.

최종 스택 그림(p.41) 기준 층 구성:

| 층 | 구성 요소 (키노트 명칭) | 요지 |
|---|---|---|
| 오픈 인프라 | 오픈 포맷 데이터 레이크 — Delta Lake · Iceberg | 모든 클라우드·모든 모델·모든 데이터, 데이터 직접 소유 |
| 에이전틱 데이터 | **Lakeflow**(수집·스트리밍·ETL) · **Lakehouse**(SQL DW) + **Lakehouse RT**(실시간 DW) · **Lakebase**(서버리스 Postgres) | Lakeflow는 Connect / Spark Declarative Pipelines / Designer(노코드) / Jobs 4개 모듈. Lakehouse RT는 "데이터 복사 없이 레이크 위에서" 실시간 서빙 주장. Lakebase는 에이전트용 OLTP — serverless · branching(time travel) · scale-to-zero |
| 통합 거버넌스 | **Unity Catalog** · **Unity Gateway** | Catalog 거버넌스 대상을 테이블·파일 넘어 모델·에이전트·**MCP/도구**·스킬까지 확장(검색·시맨틱·리니지·접근 제어·품질·비용·OpenSharing). Gateway는 "기업 AI 단일 컨트롤 플레인" — 스마트 라우팅·추론 용량·AI 비용 관리(사용자/팀/에이전트별 예산)·자산 레지스트리·보안/접근·추적 |
| 에이전틱 개발·업무 | **Genie Ontology**(OntoRank — 권한 인식 지식 추론) · **Genie**(ONE/AGENTS/CODE/App Builder/ZeroOps/AI·BI) · **Agent Bricks**(+Omnigent — 멀티 하네스 에이전트 개발: 모든 모델·프레임워크·MCP&스킬, 구축-배포-최적화) | 전사 직원용 "데이터 스마트 AI 동료" + 개발자용 에이전트 플랫폼 |
| 에이전틱 앱 | AI/BI · 맞춤형 앱 · Lakewatch(에이전틱 보안) · CustomerLake(마케팅) | 부서 단위 적용 사례 층 |

## 수치 주장 (전부 D — 참고만)

- Lakehouse RT: 최저 10ms latency, 최대 12,000 QPS, "최대 100배 성능 향상"
- SQL DW: AI 기능 3배 가속, "지난 1년 신규 기능 110개+"
- Lakebridge(EDW 마이그레이션): "성공 사례 1,300건+"
- 데이터 웨어하우스 한계 논거로 Reddit 사용자 불만 캡처(Snowflake·Redshift·Fabric latency) 인용 — 출처가 익명 커뮤니티라 그대로는 못 쓴다

## 이 프로젝트와의 접점

1. **3-3 데이터 플랫폼(미착수)**: Lakehouse(+RT)·Lakebase가 선택지 후보. 기존 refs/데이터플랫폼.md 보강 때 공식 문서(GA 여부·서울 리전·요금)로 재수집할 것 〔미정〕
2. **3-2 AI 플랫폼(완료분 보강 후보)**: Unity Gateway는 refs/AI플랫폼.md의 LiteLLM(모델 게이트웨이·비용 통제) 층과, Agent Bricks는 Bedrock AgentCore·Vertex Agent Engine(에이전트 런타임) 층과 같은 자리를 주장. 3-2 결정의 "MCP 지원 방식" 확인 항목 관점에서는 Unity Catalog의 MCP/도구 거버넌스 포함이 눈에 띄나, 키노트에는 방식 세부(서버/게이트웨이/클라이언트)가 없다 〔미정〕
3. **3-1 ETL·오케스트레이션(완료분)**: Lakeflow가 수집·ETL 층 선택지 후보 — refs/ETL오케스트레이션.md에는 현재 미포함
4. **평가 축 관련**: 키노트의 Cost(팀·에이전트별 AI 예산)·Control(에이전트/MCP 접근 제어·가드레일·추적) 논점은 02_기획안 평가 축의 비용·거버넌스 축 질문거리와 겹친다 — 운영사 안 검증(⑤) 때 "이 수준의 AI 거버넌스를 어디서 담당하는가"를 질문 후보로 쓸 수 있다

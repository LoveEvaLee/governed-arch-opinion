# 참조 — ETL · 오케스트레이션

수집일: 2026-10-11 · 검색 29회 / 상한 40회 · 버린 건 27건 · 선택지당 근거 상한 10건 · 영역 3-1

**이 파일의 결정 (2026-10-11 유경)**

- 선택지 6개. ETL 층과 오케스트레이션 층을 섞는다 — ③ 제안이 "ETL 도구 + 오케스트레이터" 조합 단위로 안을 짠다
- 타사 대응은 Cloud Composer(관리형 Airflow — MWAA와 직접 비교)
- 운영사 제안 도구는 이름을 아직 받지 않았다. 목록에 없으면 하나를 바꿔 넣는다 〔미정〕
- 날짜가 없는 공식 문서 · 요금 페이지는 「상시 갱신 — 확인일 기준」으로 적고 등급을 유지한다. 확인일 현재 상태의 근거로만 쓴다

**읽는 법.** 판정(상 · 중 · 하)은 없다 — ③④⑤가 이 근거로 판정한다. 근거 칸에 "D"로 적힌 수치(벤더 · 고객의 전후 비교 주장)는 근거로 쓰지 않는다. 〔미정〕은 열어 본 페이지에서 확인하지 못한 것이다. 원문은 요지만 옮겼다.

## 선택지 요약

| 선택지 | 맡는 층 | 종류 | 상태 (확인 2026-10-11) | 근거 건수 (A/B/C/D) |
|---|---|---|---|---|
| AWS Glue | ETL (+ 워크플로) | 관리형 | GA — 6.0 GA 2026-08-21, 0.9 · 1.0 · 2.0은 2026-04-01 EOL | 10 / 0 / 0 / 0 |
| Amazon MWAA | 오케스트레이션 | 관리형 (오픈소스 Airflow) | GA — 최신 지원 v3.3.1(2026-09-01) | 8 / 1 / 0 / 0 |
| AWS Step Functions | 오케스트레이션 | 관리형 (서버리스) | 〔미정〕 — GA 명시 페이지 미확인, 지원 종료 예고 없음 | 7 / 1 / 0 / 0 |
| Apache Airflow 직접 운영 | 오케스트레이션 | 직접 운영 | GA — Airflow 3 Maintenance, Airflow 2는 2026-04-22 EOL | 8 / 1 / 0 / 0 |
| dbt | 변환 (ELT) | 직접 운영(Core) · 타사 SaaS(platform) | GA — v2.0 2026-09-14 출시 | 8 / 1 / 0 / 0 |
| Cloud Composer | 오케스트레이션 | 타사 관리형 (GCP Airflow) | GA — Gen 1은 2026-09-15 지원 종료, 2026-04-15 Managed Service for Apache Airflow로 개명 | 8 / 1 / 0 / 0 |

---

## AWS Glue

관리형 ETL — Glue 작업 · 워크플로 · Data Catalog 포함. 상태: GA — 최신 런타임 Glue 6.0이 2026-08-21 GA(근거 2). 구버전 0.9 / 1.0 / 2.0은 2026-04-01 EOL, Python shell 3.6은 2026-06-01 EOL(근거 3).

### 근거 1 — 과금 단위와 단가 (DPU-시간, 초 단위 과금)

| 항목 | 내용 |
|---|---|
| 출처 | AWS Glue 요금 · AWS · https://aws.amazon.com/glue/pricing/ |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — Spark ETL · 크롤러 · 대화형 세션 · Data Quality는 DPU-시간당 $0.44, 초 단위 과금. Flex(SLA 없는 실행) $0.29/DPU-시간(페이지 예시 기준). Data Catalog는 객체 100만 개 · 요청 100만 건까지 무료, 그 위로 객체 10만 개당 월 $1, 요청 100만 건당 $1. DataBrew 작업 노드-시간당 $0.48. 일부 항목은 최소 1분 과금 |
| 적용 상황 | 서버를 상시 띄우지 않고 작업 실행 시간만큼 내는 일괄 · 스트리밍 ETL |
| 구성 요소 | ETL 작업(Spark / Ray / Python shell), 크롤러, 대화형 세션, Data Catalog, Data Quality, DataBrew |
| 전제 조건 | 표시 단가가 어느 리전 값인지 명시 없음 → 리전별 단가 〔미정〕. Ray · Python shell 단가 〔미정〕. 근거 2의 "6.0 30% 인하"가 이 단가에 반영됐는지 〔미정〕 |
| 걸리는 평가 축 | 비용 — 과금 단위 · 단가, 인프라 사용료 |

### 근거 2 — Glue 6.0 GA: 30% 가격 인하, Spark 4.1, 실시간 모드, 업그레이드 경로

| 항목 | 내용 |
|---|---|
| 출처 | AWS Glue 6.0 delivers 30% price reduction and Iceberg v3 support · AWS What's New · https://aws.amazon.com/about-aws/whats-new/2026/08/aws-glue-6-0-price-reduction-iceberg-v3/ |
| 날짜 | 발행 2026-08-21 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — 6.0 GA(상용 · GovCloud(US) · 중국 리전 전체). 가격 30% 인하(비교 기준 버전 명시 없음). Spark 4.1 / Python 3.13 / Scala 2.13. 1초 미만 지연의 Real-Time Mode 스트리밍, Spark Declarative Pipelines, Apache Iceberg v3, 최신 Hudi · Delta Lake 지원. 기존 작업은 생성형 AI 기반 Spark 업그레이드 에이전트로 이관 |
| 적용 상황 | 신규 작업은 6.0으로 시작하고 구버전 작업은 업그레이드 에이전트로 옮기는 경우 |
| 구성 요소 | Glue 6.0 Spark 런타임, Glue 콘솔 / SageMaker Unified Studio, Spark 업그레이드 에이전트 |
| 전제 조건 | 구버전 스크립트가 Spark 4.1과 호환돼야 함. 깨지는 변경 상세(6.0 마이그레이션 가이드) 〔미정〕 |
| 걸리는 평가 축 | 동향 적합성 — GA 여부, 릴리스 활동, 공개 포맷(Iceberg / Hudi / Delta) / 효과 — 일괄 · 실시간 처리 방식 / 비용 — 단가 변화 / 효율 — 업그레이드 부담 |

### 근거 3 — 버전 지원 정책 (EOS / EOL 일정)

| 항목 | 내용 |
|---|---|
| 출처 | AWS Glue version support policy · AWS 문서 · https://docs.aws.amazon.com/glue/latest/dg/glue-version-support-policy.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — 주요 구성요소의 커뮤니티 LTS가 끝나면 그 버전의 지원도 끝낸다는 정책. EOS가 되면 보안 패치 · 기술 지원이 끊기고 SLA 미보장. EOL이 되면 새로 만들기 · 실행이 막히고, 돌던 실행이 중지되며, SDK / API에서 빠짐. 0.9 / 1.0 / 2.0은 2026-04-01 EOL, Python shell 3.6은 2026-03-31 EOS · 2026-06-01 EOL. 이관 대상으로 6.0 안내 |
| 적용 상황 | 작업을 장기 운영하면서 런타임 버전을 주기적으로 올려야 하는 경우 |
| 구성 요소 | Glue 버전(Spark / Python shell), 마이그레이션 가이드 |
| 전제 조건 | 지원 버전 안에 머물도록 버전을 올리는 운영 절차. 현행 5.x · 6.0의 EOS 예정일은 페이지에 없음 〔미정〕 |
| 걸리는 평가 축 | 동향 적합성 — 지원 종료 계획 / 효율 — 업그레이드 · 패치 부담 |

### 근거 4 — Glue 워크플로: 작업 의존성 · 일정 · 이벤트 트리거

| 항목 | 내용 |
|---|---|
| 출처 | Overview of workflows in AWS Glue · AWS 문서 · https://docs.aws.amazon.com/glue/latest/dg/workflows_overview.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — 워크플로가 작업 · 크롤러 · 트리거를 묶어 실행하고 상태를 기록하며 그래프로 보여 줌. 시작 트리거는 일정(cron), 수동, EventBridge 이벤트(배치 크기, 최대 15분 창). 완료를 조건으로 다음 단계를 잇는 트리거로 의존 체인 구성. 실행 속성으로 작업 간 상태 공유. 워크플로당 구성요소 100개 이하 권고. 동시 실행 한도를 넘어 실패한 실행은 재시도하지 않음 |
| 적용 상황 | Glue 안에서 끝나는 ETL 체인을 별도 오케스트레이터 없이 일정 · 이벤트로 돌리는 경우 |
| 구성 요소 | 워크플로, 트리거(일정 / 수동 / EventBridge / 조건), 작업, 크롤러, 블루프린트 |
| 전제 조건 | 의존 관계가 Glue 작업 · 크롤러 범위 안에 있어야 함. Glue 밖 서비스까지 엮는 방법은 페이지에 없음 〔미정〕 |
| 걸리는 평가 축 | 효과 — 작업 의존성 · 일정, 이벤트 기반 처리 / 효율 — 관리할 구성요소 수 |

### 근거 5 — Lake Formation 세밀 접근 통제(FGAC) 연동의 범위와 제약

| 항목 | 내용 |
|---|---|
| 출처 | Considerations and limitations (Glue with Lake Formation) · AWS 문서 · https://docs.aws.amazon.com/glue/latest/dg/security-lf-enable-considerations.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — FGAC는 Spark 작업에서만, Hive(Parquet / ORC / CSV) · Iceberg 테이블에만 적용. 작업 파라미터 `--enable-lakeformation-fine-grained-access`로 켬. 시스템 드라이버와 사용자 드라이버를 분리 실행해 워커가 더 필요. 교차 계정 테이블은 같은 이름의 리소스 링크로만 조회. RDD, Spark streaming, Lake Formation 권한으로의 쓰기, 중첩 컬럼 통제는 미지원(쓰기는 IAM). 사용자 정의 클래스 UDF · 커스텀 소스 · 추가 jar 차단. 시스템 드라이버 로그는 사용자 열람 불가 |
| 적용 상황 | 데이터레이크 테이블에 행 · 열 · 셀 단위 읽기 통제를 걸고 Glue Spark로 처리하는 경우 |
| 구성 요소 | Glue Spark 작업, Lake Formation 권한, Data Catalog, 리소스 링크(교차 계정) |
| 전제 조건 | 테이블 위치가 Lake Formation에 등록돼 있어야 함. 처리 코드가 위 제약 안에 들어와야 함. 지원 Glue 버전 〔미정〕 |
| 걸리는 평가 축 | 데이터 정책 — 접근 통제 / 커스터마이징 — 계정 배치(교차 계정 리소스 링크) / 효율 — 로그 접근 제한 / 비용 — 추가 워커만큼 DPU 증가 |

### 근거 6 — Glue Spark 작업의 리니지 수집 (OpenLineage → SageMaker Catalog)

| 항목 | 내용 |
|---|---|
| 출처 | Amazon SageMaker now supports data lineage in IAM-based domains · AWS What's New · https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-sagemaker-data-lineage-iam-domain/ ; 보조: Automate lineage capture from tools · AWS 문서 · https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/datazone-data-lineage-automate-capture-from-tools.html |
| 날짜 | What's New 발행 2026-07-07 · 확인 2026-10-11 · 오래됨 아님 / 보조 문서: 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — SageMaker Unified Studio가 Glue를 포함한 Spark 작업의 OpenLineage 호환 리니지 이벤트를 수집. IAM Identity Center 도메인에 이어 IAM 기반 도메인도 지원. 리니지를 API로 게시 · 조회 · 삭제. 보조 문서: OpenLineage 라이브러리는 Glue 5.0 이상에 내장, Spark DataFrame만 지원(DynamicFrame 불가), 이벤트당 300KB 한도, 컬럼 단위 리니지는 설정으로 켬 |
| 적용 상황 | ETL 작업의 테이블 · 컬럼 단위 흐름을 중앙 카탈로그에 남겨야 하는 경우 |
| 구성 요소 | Glue 5.0+ Spark, OpenLineage Spark 리스너, SageMaker Catalog(DataZone) 도메인, Data Catalog |
| 전제 조건 | SageMaker Unified Studio / DataZone 도메인. 작업 코드가 DataFrame 기반. FGAC 모드와 함께 쓸 수 있는지 〔미정〕 |
| 걸리는 평가 축 | 데이터 정책 — 리니지 · 카탈로그 연결 / 동향 적합성 — 공개 표준(OpenLineage) / AI 인프라 적합성 — 메타데이터 노출(리니지 API) |

### 근거 7 — AWS Labs Data Processing MCP Server (Glue 작업 · 카탈로그를 에이전트에 노출)

| 항목 | 내용 |
|---|---|
| 출처 | Accelerating development with the AWS Data Processing MCP Server and Agent · AWS Big Data Blog (Shubham Mehta 외) · https://aws.amazon.com/blogs/big-data/accelerating-development-with-the-aws-data-processing-mcp-server-and-agent |
| 날짜 | 발행 2025-07-22 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — AWS Labs 오픈소스 MCP 서버(github.com/awslabs/mcp, `aws-dataprocessing-mcp-server`)가 Glue 작업 상태, Data Catalog 메타데이터 · 통계, 크롤러 구성 · 실행을 EMR · Athena와 함께 하나의 인터페이스로 에이전트에 노출. 쓰기는 `--allow-write`로 따로 켬. 읽기에는 카탈로그 · CloudWatch · EMR · Athena 권한, 쓰기에는 AWSGlueServiceRole 관리형 정책 필요. Glue 워크플로 언급 없음 |
| 적용 상황 | AI 에이전트가 카탈로그 스키마를 읽고, 작업을 호출하고, 결과를 받는 구조 |
| 구성 요소 | MCP 서버(로컬 uvx 실행), MCP 클라이언트, IAM 역할 |
| 전제 조건 | 에이전트 실행 환경에 AWS 자격 증명과 IAM 정책. Lake Formation 권한까지 전파되는지 〔미정〕 |
| 걸리는 평가 축 | AI 인프라 적합성 — 공개 표준 연계(MCP), 메타데이터 · 스키마 노출, 작업 호출 · 결과 수신, 권한 전파(IAM) |

### 근거 8 — CloudTrail로 Glue API 호출 기록

| 항목 | 내용 |
|---|---|
| 출처 | Logging AWS Glue API calls with AWS CloudTrail · AWS 문서 · https://docs.aws.amazon.com/glue/latest/dg/monitor-cloudtrail.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — Glue의 모든 API 작업(콘솔 · 코드 호출 모두)이 CloudTrail 이벤트로 남음 — 누가(루트 / IAM / 임시 자격 증명 / 다른 AWS 서비스), 언제, 어느 IP에서, 어떤 파라미터로. 트레일을 만들면 S3로 계속 전달, 여러 리전 · 계정 로그를 모을 수 있음. 연결 요청의 `ConnectionProperties` 같은 민감 값은 기록하지 않고, GetTable · GetJobRun · GetPartitions 등 여러 Get 계열 응답은 null로 남김 |
| 적용 상황 | Glue 작업 · 카탈로그 · 연결을 누가 만들고 바꾸고 지웠는지를 중앙 감사 로그로 추적 |
| 구성 요소 | AWS CloudTrail(Event history, 트레일), 로그 수신 S3 버킷, 필요 시 SNS |
| 전제 조건 | 오래 보관하려면 트레일 필요. API(관리) 호출 기록만 다룸 — 작업이 S3 데이터를 실제로 읽고 쓴 기록(데이터 이벤트)은 〔미정〕 |
| 걸리는 평가 축 | 효율 — 기존 로깅 · 감사 연결 / 데이터 정책 — 접근 기록(API 수준) / 커스터마이징 — 중앙 로깅(여러 계정 · 리전 수집) |

### 근거 9 — Data Catalog의 Iceberg REST 엔드포인트 (공개 사양 API)

| 항목 | 내용 |
|---|---|
| 출처 | Connecting to the Data Catalog using AWS Glue Iceberg REST endpoint · AWS 문서 · https://docs.aws.amazon.com/glue/latest/dg/connect-glu-iceberg-rest.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — Data Catalog가 Apache Iceberg REST 사양 API 제공(`https://glue.{리전}.amazonaws.com/iceberg`). Iceberg REST 클라이언트를 쓰는 엔진이 SigV4로 접속. 지원 API: GetConfig, 네임스페이스 생성 · 조회 · 수정 · 삭제, 테이블 목록 · 생성 · 로드 · 존재 확인 · 수정 · 삭제. Iceberg 테이블 사양 v1 · v2(기본 v2). S3와 S3 Tables의 Iceberg 테이블 모두. 네임스페이스는 한 단계, 다단계 카탈로그는 `catalog.namespace.table` 표기 |
| 적용 상황 | Glue 밖의 엔진 · 애플리케이션이 공개 표준 API로 같은 카탈로그를 읽고 쓰거나, 다른 카탈로그로 옮길 경로를 확보할 때 |
| 구성 요소 | Glue Data Catalog(Iceberg REST 엔드포인트), Iceberg REST 클라이언트, IAM(SigV4) |
| 전제 조건 | 테이블이 Iceberg 형식, 호출 주체의 SigV4 서명. Lake Formation 권한 적용 방식 · 지원 엔진 목록 〔미정〕 |
| 걸리는 평가 축 | 동향 적합성 — 종속성(공개 포맷 · 이관 경로) / AI 인프라 적합성 — 데이터 읽기 인터페이스, 공개 표준 연계, 메타데이터 · 스키마 노출 |

### 근거 10 — VPC 안에서 실행: ENI · 사설 IP · 보안 그룹, 인터넷은 NAT 경유

| 항목 | 내용 |
|---|---|
| 출처 | Setting up network access to data stores · AWS 문서 · https://docs.aws.amazon.com/glue/latest/dg/start-connecting.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — S3 → S3 작업은 VPC 설정 불필요. 사설 서브넷 JDBC 원천처럼 VPC 안에서 돌아야 하는 작업은 지정 서브넷에 ENI를 만들어 사설 IP만 붙이고(공인 IP 없음) Glue 연결의 보안 그룹 적용. VPC 안에서 S3 접근은 VPC 엔드포인트, VPC 자원과 인터넷 모두 접근은 NAT 게이트웨이 필요. 작업 하나는 VPC · 서브넷 하나에만 붙음. 다른 VPC 원천은 피어링이나 S3 중간 저장. VPC DNS 설정 필요 |
| 적용 상황 | 사설망 DB 원천을 처리하면서 네트워크 경로를 VPC · 보안 그룹 · 엔드포인트로 묶을 때 |
| 구성 요소 | Glue 연결, 서브넷, 보안 그룹, ENI, S3 VPC 엔드포인트, (필요 시) NAT 게이트웨이, VPC 피어링 |
| 전제 조건 | 원천이 지정 서브넷에서 닿고 VPC DNS 설정. 여러 VPC에 걸친 원천은 피어링이나 작업 분할 |
| 걸리는 평가 축 | 커스터마이징 — 네트워크(VPC) / 데이터 정책 — 반출 경로 통제(공인 IP 없음, 인터넷은 NAT 경유) |

### 비어 있는 것

- 비용 — 운영 인력, 전환 비용
- 효과 — 처리량 · 지연 · 가용성의 정량 SLA, 원천 · 대상 연결(커넥터 목록), 기존 작업 이관 사례
- 효율 — 관리형 / 직접 운영 비중의 명시 근거
- 동향 적합성 — 운영 사례, 로드맵 방향, 현행 5.x · 6.0의 지원 종료 예정일
- 커스터마이징 — 중앙 ID · SSO 연동, 가드레일 예외 필요 여부, 태깅
- 데이터 정책 — 분류 · 민감정보 식별, 처리 위치, 보존 · 삭제, 데이터 수준 접근 기록(S3 데이터 이벤트)

상한 10건에 닿아 넣지 못한 것(열어 본 페이지): Detect PII 문서(https://docs.aws.amazon.com/glue/latest/dg/detect-PII.html — 민감정보 식별). Transport for NSW 고객 사례는 날짜가 없어 D라 넣지 않았다.

---

## Amazon MWAA

Amazon Managed Workflows for Apache Airflow. 상태: GA — 첫 버전 v1.10.12가 2020-11-24부터 제공, 현재 최신 지원 v3.3.1(MWAA 제공 2026-09-01)(근거 2. 페이지에 "GA"라는 단어가 직접 나오지는 않음).

### 근거 1 — 과금 단위: 환경 · 추가 인스턴스는 시간, 메타DB는 GB-월, Serverless는 태스크 시간

| 항목 | 내용 |
|---|---|
| 출처 | Amazon MWAA Pricing · AWS · https://aws.amazon.com/managed-workflows-for-apache-airflow/pricing/ |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — 과금 항목 세 가지, 초 단위 계산: 환경 인스턴스 시간, 추가 워커 · 스케줄러 · 웹서버 인스턴스 시간, 메타DB 저장량(GB-월). us-east-1 예시 단가: 환경 small $0.49/h · large $0.99/h, 워커 small $0.055/h · large $0.22/h, 스케줄러 large $0.22/h, 웹서버 large $0.11/h, 메타DB $0.10/GB-월. MWAA Serverless는 large 기준 태스크 시간당 $0.080, 최소 1분 |
| 적용 상황 | 상시 기동 Provisioned 환경과 실행 시간만큼 내는 Serverless의 비용 비교 |
| 구성 요소 | 환경(크기별), 추가 워커 · 스케줄러 · 웹서버, 메타데이터 DB 저장소, (Serverless) 관리형 태스크 |
| 전제 조건 | 리전마다 단가가 다름. medium 크기, small · medium 스케줄러 · 웹서버 단가는 표가 렌더링되지 않아 〔미정〕. CloudWatch 요금 별도(근거 3) |
| 걸리는 평가 축 | 비용 — 과금 단위 · 단가, 인프라 사용료 |

### 근거 2 — 버전 지원 정책: 마이너 버전 3개 이상 동시 지원, 종료 180일 전 공지, 버전마다 최소 12개월

| 항목 | 내용 |
|---|---|
| 출처 | Apache Airflow versions on Amazon MWAA · AWS 문서 · https://docs.aws.amazon.com/mwaa/latest/userguide/airflow-versions.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 (본문 표 최신 항목 v3.3.1, 2026-09-01) |
| 등급 | A — 지원 버전 v3.3.1, v3.2.1, v2.11.2, v2.11.0, v3.0.6, v2.10.3, v2.10.1, v2.9.2, v2.8.1, v2.7.2. v2.4.3 · v2.5.1 · v2.6.3은 2025-12-30 지원 종료. 마이너 버전 최소 3개 동시 지원, 종료일 최소 180일 전 Health Dashboard 공지, 버전마다 최소 12개월 지원. 업 · 다운그레이드는 마이너 사이만 가능(메이저 불가). 종료일 뒤 기존 환경은 돌지만 새로 만들 수 없고 기술 지원 없음. 버전 최신 유지 책임은 고객. 스케줄러 기본 2개(2~5), 워커 기본 10개(1~25) |
| 적용 상황 | 업그레이드 주기와 지원 종료 위험을 따질 때, 2.x → 3.x 이관 계획 |
| 구성 요소 | MWAA 컨테이너 이미지(Airflow + Python 3.11 / 3.12), 스케줄러, 워커, Migration Guide |
| 전제 조건 | 메이저 버전을 바꾸려면 새 환경을 만들어 옮겨야 함. v2.7.2부터 requirements 파일에 `--constraint` 필요 |
| 걸리는 평가 축 | 동향 적합성 — GA 여부 · 지원 종료 계획 · 릴리스 활동 / 효율 — 업그레이드 · 패치 부담 / 효과 — 기존 작업 이관 |

### 근거 3 — CloudWatch 내장 모니터링

| 항목 | 내용 |
|---|---|
| 출처 | Amazon MWAA adds built-in monitoring with Amazon CloudWatch · AWS What's New · https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-mwaa-cloudwatch-monitoring/ |
| 날짜 | 발행 2026-09-03 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — 콘솔 환경 상세 페이지에 주요 CloudWatch 지표 대시보드와 알람 목록. AWS 관리형 템플릿으로 권장 알람을 한 번에 생성. Provisioned 환경 대상, MWAA가 있는 전 리전. CloudWatch 표준 요금 |
| 적용 상황 | CloudWatch를 표준 모니터링으로 쓰는 조직에서 관측 도구를 따로 들이지 않을 때 |
| 구성 요소 | CloudWatch 지표 · 알람, MWAA 콘솔 |
| 전제 조건 | Provisioned 환경(Serverless 대상 아님). CloudWatch 요금 별도 |
| 걸리는 평가 축 | 효율 — 기존 모니터링 · 로깅 연결 / 비용 — 부대 사용료 |

### 근거 4 — VPC 네트워킹: 자기 계정 VPC와 공유 VPC, 인터넷 없는 프라이빗 라우팅

| 항목 | 내용 |
|---|---|
| 출처 | About networking on Amazon MWAA · AWS 문서 · https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — 환경을 만드는 계정의 VPC와 여러 계정이 함께 쓰는 공유 VPC를 모두 지원. 서로 다른 AZ에 프라이빗 서브넷 2개 필요. 보안그룹 최대 5개, 자기참조 인바운드 규칙 필요. 퍼블릭 라우팅은 NAT · IGW 필요, 프라이빗 라우팅은 사용하는 AWS 서비스마다 VPC 엔드포인트(Private DNS) 필요. 웹서버 접근 모드 Public / Private / Both(v3.2.1 이상), Private은 VPC 안 접근 수단(Client VPN 등) 필요 |
| 적용 상황 | 랜딩존의 공유 VPC(네트워크 계정)에 워크로드 계정이 환경을 띄울 때, 인터넷 반출을 금지할 때 |
| 구성 요소 | 프라이빗 서브넷 2개, 보안그룹, NACL, (퍼블릭) NAT · IGW, (프라이빗) 서비스별 VPC 엔드포인트, S3 게이트웨이 엔드포인트 정책 |
| 전제 조건 | 보안그룹 아웃바운드 전체 허용, NACL 인 · 아웃바운드 전체 허용 규칙 요구. 조직 가드레일과 부딪히는지 〔미정〕 |
| 걸리는 평가 축 | 커스터마이징 — 계정 · 조직 배치, 네트워크(VPC), 가드레일 예외 필요 여부 / 데이터 정책 — 반출 경로 통제 |

### 근거 5 — 고객 관리형 KMS 키로 저장 데이터 암호화

| 항목 | 내용 |
|---|---|
| 출처 | Using customer-managed keys for encryption · AWS 문서 · https://docs.aws.amazon.com/mwaa/latest/userguide/custom-keys-certs.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — 고객 관리형 키는 선택 사항. 키는 환경 · S3 버킷과 같은 리전에 있어야 함. 다른 계정의 키는 ARN으로 지정 가능. 키 별칭과 멀티리전 키는 미지원. MWAA가 키에 grant 4개를 붙여 CloudWatch Logs · SQS · Aurora PostgreSQL · Secrets Manager · S3 · DynamoDB를 암호화. CloudWatch Logs용 키 정책은 따로 추가. 키를 지정하지 않을 때의 기본 동작은 페이지 본문에서 확인 못 함 〔미정〕 |
| 적용 상황 | 중앙 보안 계정의 키로 데이터를 암호화해야 하는 정책이 있을 때 |
| 구성 요소 | AWS KMS 고객 관리형 키, grant 4개, CloudWatch Logs 키 정책 |
| 전제 조건 | 키가 같은 리전에 있을 것, 키 정책과 grant 관리 권한 |
| 걸리는 평가 축 | 데이터 정책 — 접근 통제 · 처리 위치(리전) / 커스터마이징 — 중앙 계정(키) 연동 |

### 근거 6 — IAM(SigV4)으로 Airflow REST API 호출(InvokeRestApi)

| 항목 | 내용 |
|---|---|
| 출처 | Using the Apache Airflow REST API · AWS 문서 · https://docs.aws.amazon.com/mwaa/latest/userguide/access-mwaa-apache-airflow-rest-api.html ; 같은 기능 What's New(2024-10-23) · https://aws.amazon.com/about-aws/whats-new/2024/10/amazon-mwaa-simplifies-interaction-airflow-rest-api/ |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 (기능 발표 2024-10-23) |
| 등급 | A — v2.4.3 이상에서 AWS 자격증명으로 Airflow REST API 호출 — DAG 실행 트리거, 데이터셋 관리, 컴포넌트 상태 조회. `airflow:InvokeRestApi` 권한을 Admin · Op · User · Viewer · Public 역할 ARN 단위로 부여. `aws:SourceVpc` · `aws:SourceVpce` 조건으로 VPC 안 호출만 허용 가능. 기본 타임아웃 10초, 응답 상한 6MB. 10 TPS 초과 시 웹 세션 토큰 방식 안내(12시간). v3부터 경로 `/api/v2` |
| 적용 상황 | 외부 시스템이나 에이전트가 IAM 권한으로 작업을 호출하고 결과를 받을 때 |
| 구성 요소 | MWAA InvokeRestApi API, IAM 정책, Airflow REST API, 웹서버 오토스케일링 |
| 전제 조건 | v2.4.3 이상, 호출 주체의 IAM 권한, 10초 · 6MB 안에 끝나는 호출 |
| 걸리는 평가 축 | AI 인프라 적합성 — 작업 호출 · 결과 수신, 권한 전파(IAM ↔ Airflow 역할 매핑) / 커스터마이징 — 중앙 ID(IAM) 연동 / 데이터 정책 — 접근 통제 |

### 근거 7 — LaunchDarkly 이관 사례: 다른 클라우드의 관리형 Airflow에서 MWAA + ECS Fargate로

| 항목 | 내용 |
|---|---|
| 출처 | How LaunchDarkly migrated to Amazon MWAA to achieve efficiency and scale · AWS Big Data Blog(LaunchDarkly 공저 — Asena Uyar · Dean Verhey · Daniel Lopes) · https://aws.amazon.com/blogs/big-data/how-launchdarkly-migrated-to-amazon-mwaa-to-achieve-efficiency-and-scale/ |
| 날짜 | 발행 2025-05-16 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | B(사업자 선정 사례) — Airflow 1.12에서 MWAA 2.5.1로 옮긴 뒤 하루 태스크 약 100건 → 14,000건 이상, 쓰는 팀 1 → 3개, 서비스 2 → 4개. "비용 증가가 미미했다"는 자기평가는 D라 근거로 쓰지 않음 |
| 적용 상황 | 다른 관리형 · 자체 운영 Airflow에서 옮겨 올 때, 무거운 태스크를 워커 밖(Fargate)으로 격리할 때 |
| 구성 요소 | MWAA(오케스트레이션), ECS on Fargate(실행), ECR, S3, Secrets Manager, CloudWatch + Datadog |
| 전제 조건 | Celery 워커는 태스크 간 격리가 약함. 이 사례에서는 커스텀 오퍼레이터가 워커 디스크에 만든 가상환경이 서로 간섭해, 그대로 옮기려던(rehost) 계획이 구조를 고치는(refactor) 작업으로 바뀜 |
| 걸리는 평가 축 | 효과 — 처리량, 기존 작업 이관 / 동향 적합성 — 운영 사례 / 비용 — 전환 비용(재구성 부담) |

### 근거 8 — MWAA Serverless: 환경 관리 없이 워크플로 실행, 워크플로마다 IAM 격리

| 항목 | 내용 |
|---|---|
| 출처 | Amazon MWAA Introduces Serverless Deployment Option for Apache Airflow Workflows · AWS What's New · https://aws.amazon.com/about-aws/whats-new/2025/11/mwaa-serverless-deployment-apache-airflow-workflows/ |
| 날짜 | 발행 2025-11-17 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — Serverless 옵션은 Airflow 환경 관리 부담 없이 인프라를 자동 확장. 태스크 실행 시간만 과금. 워크플로는 YAML이나 Python DAG. 워크플로마다 격리 실행되고 IAM 권한도 따로. Airflow v3.0의 AWS 오퍼레이터 80개 이상 지원. 출시 시점 15개 리전(서울 포함) |
| 적용 상황 | 상시 환경(스케줄러 · 워커 · 웹서버) 없이 워크플로를 돌릴 때, 실행이 드문 배치 위주 워크로드 |
| 구성 요소 | MWAA Serverless 워크플로(YAML 또는 Python DAG), 워크플로별 IAM 역할, AWS 오퍼레이터 |
| 전제 조건 | Airflow v3.0 기준, 지원 오퍼레이터는 AWS 오퍼레이터 80여 개. 그 밖의 오퍼레이터 · 커스텀 플러그인 사용 가능 여부 〔미정〕, 태스크 실행 방식 〔미정〕. 근거 3의 내장 모니터링은 Provisioned만 대상 |
| 걸리는 평가 축 | 효율 — 관리형 / 직접 운영 비중, 관리할 구성요소 수 / 비용 — 과금 단위 / AI 인프라 적합성 — 권한 전파 |

### 근거 9 — Airflow 3.3.1 지원: Task · Asset State Store, asset 파티셔닝, 재시도 정책 플러그인

| 항목 | 내용 |
|---|---|
| 출처 | Amazon MWAA supports Apache Airflow version 3.3.1 · AWS What's New · https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-mwaa-apache-airflow-3-3-1/ |
| 날짜 | 발행 2026-09-01 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — 3.3.1 환경에서: 재시도 · 재실행을 거쳐도 태스크 상태 유지(Task · Asset State Store — 커서 추적, 장시간 작업 재접속), asset 파티셔닝 확장, 재시도 정책 플러그인 교체, DAG 실행 · 태스크 인스턴스 일괄 작업, Java · Go Language Task SDK(실험). 새 환경 생성 또는 3.2 이상에서 업그레이드 |
| 적용 상황 | 재시도 사이에 상태를 이어 가야 하는 장시간 · 증분 처리, 데이터(asset) 단위 의존성 · 일정 |
| 구성 요소 | Airflow 3.3.1 환경, Task · Asset State Store, asset 파티셔닝, 재시도 정책 플러그인 |
| 전제 조건 | v3.2 이상이어야 바로 업그레이드, 2.x는 메이저 이관(근거 2). asset 파티셔닝 · 재시도 정책의 세부 동작 〔미정〕. Language Task SDK는 실험 기능 |
| 걸리는 평가 축 | 효과 — 작업 의존성 · 일정(세부 동작은 〔미정〕) / 동향 적합성 — 릴리스 활동 |

### 비어 있는 것

- 비용 — 운영 인력, medium 크기 · small · medium 스케줄러 · 웹서버 단가
- 효과 — 실시간 처리 여부, 가용성 SLA 수치(서브넷 2개를 다른 AZ에 둔다는 것만 확인), Provisioned 환경의 원천 · 대상 연결(커넥터 · 오퍼레이터 범위), 작업 의존성 세부 동작
- 효율 — 관리할 구성요소 수의 구체 수치
- 동향 적합성 — 종속성(공개 포맷 · 이관 경로)을 다룬 별도 근거, 로드맵 방향
- 커스터마이징 — SSO(IAM Identity Center) 연동, 태깅, 중앙 로깅 계정 전송, CloudTrail 기록 대상
- 데이터 정책 — 분류 · 민감정보 식별, 접근 기록(CloudTrail), 보존 · 삭제, 리니지 · 카탈로그 연결
- AI 인프라 적합성 — 메타데이터 · 스키마 노출. MCP: AWS 공식 MCP 저장소(https://github.com/awslabs/mcp, `src/` 목록 2026-10-11 확인)에 MWAA · Airflow 서버 없음, `aws-dataprocessing-mcp-server`에도 MWAA 언급 없음

넣지 않은 버린 건: CloudWatch 로그 유형 문서 · SageMaker Unified Studio의 MWAA 연결 What's New(2026-07-07) · REST API What's New(2024-10-23)는 새로 채우는 빈칸이 없음.

---

## AWS Step Functions

관리형 서버리스 워크플로 오케스트레이션. 상태: 〔미정〕 — GA를 명시한 페이지는 열어 보지 못함. What's New(2025-10-30, https://aws.amazon.com/about-aws/whats-new/2025/10/aws-step-functions-metrics-dashboard)에는 "Step Functions가 제공되는 모든 리전"이라고만 있고, 열어 본 자료 안에 지원 종료 예고는 없음.

### 근거 1 — Standard는 상태 전환 단위, Express는 요청 수 + 실행 시간(GB-시간) 단위 과금

| 항목 | 내용 |
|---|---|
| 출처 | AWS Step Functions Pricing · AWS · https://aws.amazon.com/step-functions/pricing/ |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — Standard는 상태 전환 1회당 $0.000025(us-east-1), 재시도도 전환으로 계산, 무료 4,000회/월(12개월 후에도 유지). Express는 요청 100만 건당 $1.00, 실행 시간은 64MB 단위 메모리 · 100ms 올림. 구간 단가 첫 1,000 GB-시간 $0.06, 다음 4,000 GB-시간 $0.03, 그 이상 $0.01642. Express 무료 구간은 페이지에 없음 |
| 적용 상황 | 단계가 많은 장기 배치(Standard)와 대량 · 단시간 이벤트 처리(Express)의 비용 산정 |
| 구성 요소 | Standard 워크플로, Express 워크플로 |
| 전제 조건 | 워크플로 유형을 고르고 단계 수 · 실행 빈도 · 메모리를 추정해야 함 |
| 걸리는 평가 축 | 비용 — 과금 단위 · 단가 |

### 근거 2 — VPC 인터페이스 엔드포인트(PrivateLink)와 엔드포인트 정책

| 항목 | 내용 |
|---|---|
| 출처 | Creating Amazon VPC endpoints for Step Functions · AWS 개발자 안내서 · https://docs.aws.amazon.com/step-functions/latest/dg/vpc-endpoints.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — 인터페이스 VPC 엔드포인트로 퍼블릭 인터넷 · IGW · NAT · VPN 없이 VPC에서 Step Functions 호출. Standard · Express · 동기 Express 모두 지원(서비스 이름 states / sync-states). 엔드포인트에 IAM 엔드포인트 정책을 붙여 주체 · 액션 · 리소스 제한 가능. CloudFormation(AWS::EC2::VPCEndpoint)으로 구성 |
| 적용 상황 | 워크로드 계정 VPC 안에서만 워크플로를 시작 · 조회하도록 네트워크 경로를 묶는 구조 |
| 구성 요소 | 인터페이스 VPC 엔드포인트(PrivateLink), 프라이빗 DNS, 엔드포인트 정책, CloudFormation |
| 전제 조건 | VPC · 서브넷. 동기 Express에서 SDK 엔드포인트를 직접 지정하려면 DisableHostPrefixInjection 설정 |
| 걸리는 평가 축 | 커스터마이징 — 네트워크(VPC) / 데이터 정책 — 접근 통제(엔드포인트 정책) |

### 근거 3 — Glue · EMR · Athena · Bedrock 등과의 최적화 통합과 통합 패턴

| 항목 | 내용 |
|---|---|
| 출처 | Integrating optimized services with Step Functions · AWS 개발자 안내서 · https://docs.aws.amazon.com/step-functions/latest/dg/integrate-optimized.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — 최적화 통합에 Athena, Batch, Glue, Glue DataBrew, EMR, EMR on EKS, EMR Serverless, ECS / EKS, SageMaker AI, Bedrock, Bedrock AgentCore 등. 다수가 작업 완료까지 기다리는 .sync를 Standard에서 지원. AWS SDK 통합으로 200개 넘는 서비스를 Request Response 방식으로 호출. Express는 Request Response만 지원 |
| 적용 상황 | Glue / EMR / Athena 작업을 순서대로 실행하고 완료를 기다리는 일괄 파이프라인 오케스트레이션 |
| 구성 요소 | Task 상태의 Resource 필드, 패턴 3종(Request Response / Run a Job .sync / Wait for Callback .waitForTaskToken) |
| 전제 조건 | 대상 서비스가 같은 AWS 환경에 있어야 함. .sync와 콜백은 Standard에서만 |
| 걸리는 평가 축 | 효과 — 처리 방식(.sync로 완료 대기), 원천 · 대상 연결, 작업 의존성 / 효율 — 관리형 서비스 직접 호출 / AI 인프라 적합성 — 작업 호출 · 결과 수신(Bedrock · AgentCore 통합) |

### 근거 4 — 워크플로는 JSON 기반 Amazon States Language(ASL)로 정의

| 항목 | 내용 |
|---|---|
| 출처 | Using Amazon States Language to define Step Functions workflows · AWS 개발자 안내서 · https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — ASL은 JSON 구조 언어(.asl.json), 쿼리 언어로 JSONata 지정 가능. 문서가 별도 사양 페이지(states-language.net)와 검증 도구 Statelint(awslabs GitHub)를 링크(두 곳은 직접 열지 않음). 예시 정의의 Task Resource는 AWS ARN을 가리킴 |
| 적용 상황 | 종속성(이관 경로)을 검토할 때 정의 형식 확인 |
| 구성 요소 | ASL 정의(Task / Choice / Fail 등 상태), JSONata / JSONPath, Statelint |
| 전제 조건 | 정의가 AWS 리소스 ARN에 묶여 있어, 다른 실행 엔진으로 옮길 때 변환이 필요한지 〔미정〕 |
| 걸리는 평가 축 | 동향 적합성 — 종속성(공개 포맷 · 이관 경로) |

### 근거 5 — 저장 데이터 암호화(고객 관리형 KMS 키)와 CloudTrail 감사

| 항목 | 내용 |
|---|---|
| 출처 | Data at rest encryption in Step Functions · AWS 개발자 안내서 · https://docs.aws.amazon.com/step-functions/latest/dg/encryption-at-rest.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — AWS 소유 키로 항상 암호화, 고객 관리형 대칭 KMS 키로 2차 암호화 추가 가능(상태 머신 정의 · 실행 이력, Activity 입력). 암호화 컨텍스트(stateMachineArn)와 kms:ViaService로 키 사용 범위 제한. 다른 계정의 키 지정 가능. CloudWatch 로그 그룹도 KMS 암호화. KMS 호출은 CloudTrail에 기록. 메타데이터만 반환하는 API 옵션(METADATA_ONLY). CMK 사용 시 EventBridge 상태 변경 이벤트에서 입력 · 출력이 빠짐. 키 삭제 시 데이터 복구 불가 |
| 적용 상황 | 민감 데이터가 워크플로 입력 · 출력으로 흐를 때 접근 통제와 감사 |
| 구성 요소 | AWS KMS(CMK), 키 정책 · IAM 정책, CloudTrail, CloudWatch Logs, CloudFormation EncryptionConfiguration |
| 전제 조건 | KMS 키와 키 정책 설계, 실행 역할에 kms:Decrypt / GenerateDataKey 권한, KMS 요금 별도 |
| 걸리는 평가 축 | 데이터 정책 — 접근 통제 · 접근 기록, 보존 · 삭제(키 삭제 시 복구 불가) / 효율 — 기존 감사(CloudTrail) · 로깅(CloudWatch) 연결 / 커스터마이징 — 계정 배치(다른 계정 키 참조), 중앙 로깅 / 비용 — KMS 별도 과금 |

### 근거 6 — awslabs 오픈소스 MCP 서버로 상태 머신을 AI 도구로 노출

| 항목 | 내용 |
|---|---|
| 출처 | AWS Step Functions Tool MCP Server · AWS Labs 공식 문서 · https://awslabs.github.io/mcp/servers/stepfunctions-tool-mcp-server |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — MCP 클라이언트가 기존 상태 머신을 정의 수정 없이 도구로 실행. 노출 범위는 이름 목록 · 접두사 · 태그로 제한. 입력은 EventBridge Schema Registry(JSON Schema)로 검증, 스키마 · 설명 · Comment로 도구 문서 생성. IAM 인증 · 인가, 모델은 다른 AWS 서비스에 직접 접근하지 못하고 상태 머신이 자기 IAM 역할로 호출. Standard · Express 모두 지원 |
| 적용 상황 | 에이전트가 데이터 파이프라인 작업을 호출하고 결과를 받는 구조 |
| 구성 요소 | MCP 서버(Python 3.10, uv 실행), EventBridge Schema Registry, IAM, 상태 머신 태그 |
| 전제 조건 | 서버 실행 환경, 상태 머신 호출 권한, 노출 대상 태깅 · 스키마 등록 |
| 걸리는 평가 축 | AI 인프라 적합성 — 공개 표준 연계(MCP), 작업 호출 · 결과 수신, 메타데이터 · 스키마 노출, 권한 전파(IAM 역할 경유) |

### 근거 7 — 실시간 이벤트 파이프라인 운영 사례(KnowBe4)

| 항목 | 내용 |
|---|---|
| 출처 | Orchestrating real-time data processing pipelines in AWS · KnowBe4 Engineering Blog(Atish Kathpal) · https://www.knowbe4.com/careers/blogs/engineering/orchestrating-real-time-data-processing-pipelines-in-aws |
| 날짜 | 발행 2023-01-17 · 갱신 2026-06-19 · 확인 2026-10-11 · 갱신일 기준 오래됨 아님(발행일 기준이면 오래됨) |
| 등급 | B — 하루 수천만 건 보안 이벤트 파이프라인의 조건부 단계를 Step Functions(Standard)로 오케스트레이션. MWAA는 장기 배치에 더 맞는다고 보고 실시간 용도로 Step Functions 선택. 운영 제약으로 단계 간 페이로드 256KB 한도(청크 분할 대응), 자체 스케줄러 없음(CloudWatch Events로 트리거), Lambda 15분 한도. 병렬 시험의 오케스트레이션 오버헤드 100~900ms(회사 자체 측정) |
| 적용 상황 | 이벤트 기반 실시간 처리에 조건부 단계를 덧붙이는 구조 |
| 구성 요소 | Step Functions(Standard, Workflow Studio, Choice / Retry), Lambda, ECS, SNS, SQS, S3, RDS, DynamoDB, ElastiCache |
| 전제 조건 | 페이로드 256KB 이하 설계, 스케줄 트리거(EventBridge 등) 별도 |
| 걸리는 평가 축 | 동향 적합성 — 운영 사례 / 효과 — 처리 방식(실시간), 일정(외부 스케줄러 필요), 처리량 · 지연 / 효율 — 관리형 · 서버리스 |

### 근거 8 — 지표 대시보드 출시(계정 · 상태 머신 단위 사용량 · 과금 지표)

| 항목 | 내용 |
|---|---|
| 출처 | AWS Step Functions announces a new metrics dashboard · AWS What's New · https://aws.amazon.com/about-aws/whats-new/2025/10/aws-step-functions-metrics-dashboard |
| 날짜 | 발행 2025-10-30 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — 콘솔에 지표 대시보드가 추가돼 계정 수준과 상태 머신 수준의 사용량 · 과금 지표를 한곳에서 봄. Standard · Express 모두, ApproximateOpenMapRunCount 같은 기존 지표도 표시. Step Functions가 제공되는 모든 리전 |
| 적용 상황 | 서비스의 최근 기능 추가 흐름(릴리스 활동) 확인, 사용량 · 과금을 콘솔에서 바로 볼 때 |
| 구성 요소 | Step Functions 콘솔 지표 대시보드, CloudWatch 지표 |
| 전제 조건 | Step Functions 콘솔 접근 권한 |
| 걸리는 평가 축 | 동향 적합성 — 릴리스 활동 / 효율 — 기존 모니터링 연결 |

### 비어 있는 것

- 비용 — 운영 인력, 전환 비용
- 효과 — 가용성(SLA · 실행 보장 수치), 기존 작업 이관(다른 오케스트레이터 정의를 ASL로 옮기는 경로)
- 효율 — 업그레이드 · 패치 부담을 직접 다룬 근거, X-Ray 추적 연동(문서 미열람)
- 동향 적합성 — GA 명시 근거, 지원 종료 계획, 로드맵 방향
- 커스터마이징 — 중앙 ID · SSO 연동, 가드레일 예외 필요 여부, 태깅
- 데이터 정책 — 분류 · 민감정보 식별, 반출 경로 통제 · 처리 위치, 리니지 · 카탈로그 연결
- AI 인프라 적합성 — 에이전트가 데이터를 직접 읽는 인터페이스(오케스트레이터라 해당 여부 〔미정〕)

넣지 않은 버린 건(새로 채우는 빈칸 없음): 워크플로 유형 비교 문서, What's New 2025-09-18 Distributed Map 확장, CloudWatch Logs 로깅 문서, AWS Compute Blog CMK 글(2024-08-27, 오래됨). CloudThat 사례는 날짜가 없어 D.

---

## Apache Airflow 직접 운영

오픈소스, EKS / Kubernetes 또는 EC2에 직접 설치 · 운영. 상태: GA — Airflow 3는 2025-04-22 첫 릴리스 후 Maintenance 상태. Airflow 2는 2025-10-22부터 제한 유지보수, 2026-04-22 EOL(근거 2).

### 근거 1 — 3.x 릴리스가 매달 나온다 (3.3.0 → 3.3.2)

| 항목 | 내용 |
|---|---|
| 출처 | apache/airflow GitHub Releases · Apache Software Foundation · https://github.com/apache/airflow/releases/tag/3.3.2 · https://api.github.com/repos/apache/airflow/releases?per_page=8 |
| 날짜 | 발행: 3.3.2 2026-09-17 / 3.3.1 2026-08-12 / 3.3.0 2026-07-06 / Java SDK 1.0.0-beta1 2026-07-13 (API published_at) · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — 3.x 마이너 · 패치가 약 1개월 간격. 3.3.2에 버그 수정 99건, 주요 변경 2건은 보안 · 인증(백필 엔드포인트 권한 범위 축소, 명시한 Bearer / OAuth2 토큰이 세션 쿠키보다 우선). Helm 차트 1.22.0은 목록에 '13 Jun'으로만 나와 연도 미표기 |
| 적용 상황 | 오픈소스를 직접 받아 설치하고 패치를 따라갈 주기를 스스로 정하는 구조 |
| 구성 요소 | Airflow 코어 릴리스, 공식 Helm 차트 릴리스(별도 버전 체계), Java SDK(베타) |
| 전제 조건 | 패치마다 변경사항을 검토할 운영 인력. API 동작이 바뀌면 API 클라이언트도 수정 |
| 걸리는 평가 축 | 동향 적합성 — 릴리스 · 커뮤니티 활동, 로드맵 방향 / 효율 — 업그레이드 · 패치 부담 |

### 근거 2 — 버전 지원 · EOL 정책

| 항목 | 내용 |
|---|---|
| 출처 | Supported versions · Apache Airflow 공식 문서 · https://airflow.apache.org/docs/apache-airflow/stable/installation/supported-versions.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — Airflow 3은 Maintenance, 제한 유지보수 시작일 · EOL은 TBD. Airflow 2는 2.11.2를 끝으로 2026-04-22 EOL. 제한 지원 기간엔 보안 · 중대 버그 수정만, EOL 이후 수정 없음. 최신 버전 설치 권고. Python · Kubernetes 지원은 각 상위 프로젝트 일정을 따름 |
| 적용 상황 | 직접 운영 시 버전 수명을 스스로 관리. 2.x 운영 중이면 이미 EOL |
| 구성 요소 | Airflow 메이저 버전 수명주기, Python · Kubernetes 지원 매트릭스 |
| 전제 조건 | 메이저 업그레이드(2 → 3) 계획과 인력, Kubernetes 업그레이드 주기와의 정렬 |
| 걸리는 평가 축 | 동향 적합성 — GA 여부 · 지원 종료 계획 / 효율 — 업그레이드 · 패치 부담 / 비용 — 전환 비용(2 → 3 이관) |

### 근거 3 — 공식 Helm 차트 프로덕션 가이드

| 항목 | 내용 |
|---|---|
| 출처 | Production Guide (Helm Chart 1.22.0, Airflow v3.3.0 기준) · Apache Airflow 공식 문서 · https://airflow.apache.org/docs/helm-chart/stable/production-guide.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — 프로덕션에서는 내장 Postgres 대신 외부 메타DB, Postgres에는 PgBouncer 권장. API · JWT 비밀키는 고정값을 Kubernetes Secret으로. 모든 노드 시계 동기화. Celery 브로커 외부 교체 가능. Kubernetes 워커 safeToEvict 기본값 false. `airflow db clean` 크론잡으로 메타DB 보존 기간 관리. OpenShift SCC · securityContext 지원 |
| 적용 상황 | EKS 같은 Kubernetes 클러스터에 공식 차트로 설치 |
| 구성 요소 | 외부 메타DB(PostgreSQL), PgBouncer, (Celery 시) Redis 등 브로커, Kubernetes Secret, 실행기(Celery / CeleryKubernetes / Kubernetes / LocalKubernetes), DB 정리 크론잡 |
| 전제 조건 | Kubernetes 클러스터, 외부 DB, 비밀정보 관리 수단, 노드 시간 동기화, 실행기 선택 |
| 걸리는 평가 축 | 효과 — 처리 방식(실행기), 가용성(오토스케일러 축출 정책) / 효율 — 관리할 구성요소 수, 직접 운영 비중 / 커스터마이징 — 비밀정보 · 보안 컨텍스트 / 데이터 정책 — 보존 · 삭제(메타DB 정리) / 비용 — 인프라 사용료(외부 DB · 브로커 별도) |

### 근거 4 — 실행 기반(EKS)의 과금 단위

| 항목 | 내용 |
|---|---|
| 출처 | Amazon EKS pricing · AWS · https://aws.amazon.com/eks/pricing/ |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — 컨트롤 플레인 클러스터당 시간당 $0.10(표준 지원), 확장 지원 시 $0.60. Kubernetes 버전은 처음 14개월 표준 지원, 다음 12개월 확장 지원. 워커는 별도 — EC2(인스턴스 · EBS · 퍼블릭 IPv4) 또는 Fargate(vCPU · 메모리 초 단위, 최소 1분) |
| 적용 상황 | Airflow를 EKS 위에 직접 올릴 때의 기반 비용 구조. Airflow 라이선스 무료 여부는 별도 근거로 확인하지 않음 〔미정〕 |
| 구성 요소 | EKS 컨트롤 플레인, EC2 또는 Fargate 워커, EBS, 퍼블릭 IPv4 |
| 전제 조건 | AWS 계정과 EKS 클러스터. Kubernetes 버전을 제때 올리지 않으면 확장 지원 할증 |
| 걸리는 평가 축 | 비용 — 과금 단위 · 단가, 인프라 사용료 / 효율 — 업그레이드 부담(Kubernetes 버전 수명) |

### 근거 5 — 보안 모델, API 인증, 인증 관리자

| 항목 | 내용 |
|---|---|
| 출처 | Airflow Security Model · https://airflow.apache.org/docs/apache-airflow/stable/security/security_model.html ; API 인증 · https://airflow.apache.org/docs/apache-airflow/stable/security/api.html ; Auth managers · https://airflow.apache.org/docs/apache-airflow-providers/core-extensions/auth-managers.html (모두 Apache Airflow 공식 문서) |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — 사용자 유형: 배포 관리자 / DAG 작성자 / 역할별 UI 사용자. 감사 로그는 기본적으로 Admin만 열람. Airflow 3부터 Connection 설정 역할은 비밀값을 쓸 수만 있고 볼 수 없음. 태스크 단위 격리 불완전 — 태스크 JWT가 DAG 단위로 나뉘지 않아 다른 DAG의 Variable · Connection · XCom에 접근 가능, 토큰 회수 불가. 로그 마스킹은 값을 인식할 때만. 멀티팀 모드는 실험 단계. TLS · 네트워크 격리 · 요청 크기 제한 · DAG 코드 리뷰는 배포 관리자 책임. REST API(/api/v2)는 `/auth/token`의 JWT Bearer 인증. 인증 관리자: Simple(기본), 프로바이더로 AwsAuthManager · FabAuthManager · KeycloakAuthManager |
| 적용 상황 | 여러 팀이 같이 쓰거나 중앙 ID와 연결해 접근을 통제해야 하는 경우 |
| 구성 요소 | 인증 관리자, JWT 서명키(비대칭 권장), Execution API, 역할 기반 권한, 감사 로그, 리버스 프록시 |
| 전제 조건 | 네트워크 격리, 프록시 설정, DAG 코드 검토 절차. SSO는 해당 인증 관리자 프로바이더 설치 필요, IdP별 연동 범위 〔미정〕 |
| 걸리는 평가 축 | 데이터 정책 — 접근 통제 · 접근 기록, 비밀정보 노출 경로 / 커스터마이징 — 중앙 ID · SSO 연동, 네트워크 격리 / AI 인프라 적합성 — 작업 호출 인터페이스(REST API v2, JWT), 권한 전파 한계 |

### 근거 6 — OpenLineage 프로바이더(리니지)

| 항목 | 내용 |
|---|---|
| 출처 | apache-airflow-providers-openlineage · Apache Airflow 공식 문서 · https://airflow.apache.org/docs/apache-airflow-providers-openlineage/stable/index.html · https://airflow.apache.org/docs/apache-airflow-providers-openlineage/stable/guides/structure.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 (프로바이더 2.20.2) |
| 등급 | A — OpenLineageListener를 등록해 DAG · 태스크 시작 · 완료 · 실패 때 이벤트 생성. DAG 단위는 스케줄러, 태스크 단위는 워커에서 발생. 입력 · 출력 데이터셋, run · job 메타데이터, 오퍼레이터별 메타데이터 포함. 전송 방식 HTTP · Kafka · file · 사용자 정의. Airflow 2.11.0 이상 |
| 적용 상황 | 오케스트레이션 이력을 외부 리니지 · 카탈로그로 보내야 하는 경우 |
| 구성 요소 | OpenLineage 프로바이더, openlineage-python 클라이언트, 리니지 수신 백엔드 〔미정〕 |
| 전제 조건 | 리니지를 받을 백엔드, 오퍼레이터의 extractor 지원(지원 목록 〔미정〕) |
| 걸리는 평가 축 | 데이터 정책 — 리니지 · 카탈로그 연결 / 동향 적합성 — 종속성(공개 표준 OpenLineage) / AI 인프라 적합성 — 메타데이터 · 스키마 노출 |

### 근거 7 — 직접 운영하는 Airflow에 붙는 MCP 서버(벤더 오픈소스)

| 항목 | 내용 |
|---|---|
| 출처 | astronomer/agents (astro-airflow-mcp) · Astronomer 공식 GitHub · https://github.com/astronomer/agents |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 (벤더 공식 저장소, 릴리스 날짜 표시 없음) |
| 등급 | A — 기능 사실만. Airflow 2.x · 3.x REST API 위의 MCP 서버와 `af` CLI. DAG 관리 · 실행 트리거 · 태스크 로그 · 상태 점검. `AIRFLOW_API_URL`로 직접 운영 인스턴스에 연결. 인증은 사용자명 · 비밀번호 또는 Bearer 토큰. Apache 2.0. Apache 재단이 직접 낸 MCP 서버는 찾지 못함 |
| 적용 상황 | AI 에이전트가 오케스트레이터를 조회하거나 작업을 호출하는 경우(REST API만 열려 있으면 연결) |
| 구성 요소 | astro-airflow-mcp(stdio), Airflow REST API, 인증 정보 |
| 전제 조건 | 에이전트에서 Airflow API까지 네트워크 도달, 에이전트용 계정 권한 범위(근거 5의 토큰 한계). 관리형 전용 기능 의존 여부 〔미정〕 |
| 걸리는 평가 축 | AI 인프라 적합성 — 공개 표준 연계(MCP), 작업 호출 · 결과 수신, 데이터 읽기 인터페이스 / 동향 적합성 — 종속성(제3자 벤더 저장소) |

### 근거 8 — 메트릭 · 원격 로그 연결

| 항목 | 내용 |
|---|---|
| 출처 | Metrics Configuration · https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/metrics.html ; Logging for Tasks · https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/logging-tasks.html (Apache Airflow 공식 문서) |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 (문서 버전 3.3.2) |
| 등급 | A — 메트릭은 StatsD와 OpenTelemetry로 내보냄(`[metrics]`의 statsd_* · otel_* 키, 허용 · 차단 목록). 타이밍 메트릭은 OTel 지수 히스토그램이라 Prometheus로 받으려면 native histogram을 켜고 OTel Collector 0.115.0 이상 필요. 태스크 로그는 원격 저장소로 — 블롭형(S3 · GCS · WASB · HDFS · OSS)과 스트리밍형(Elasticsearch · AWS CloudWatch · GCP 로깅), `remote_logging` · `remote_base_log_folder`로 설정, `delete_local_logs`로 업로드 뒤 로컬 삭제 |
| 적용 상황 | 직접 운영 Airflow를 조직이 이미 쓰는 모니터링 · 중앙 로깅에 붙이는 경우 |
| 구성 요소 | StatsD 수신기 또는 OTel Collector, (선택) Prometheus, 원격 로그 저장소(S3 · CloudWatch 등), 로그 핸들러 프로바이더 |
| 전제 조건 | 받는 쪽 모니터링 · 로그 시스템을 따로 운영하거나 연결. 감사 로그(근거 5)를 중앙 로깅으로 보내는 경로 〔미정〕 |
| 걸리는 평가 축 | 효율 — 기존 모니터링 · 로깅 연결 / 커스터마이징 — 중앙 로깅 |

### 근거 9 — 기업 자체 운영 사례: Kubernetes에 직접 올리고 클러스터 팀에 의존 (오래됨)

| 항목 | 내용 |
|---|---|
| 출처 | Self-hosted vs. managed Apache Airflow (Ariel Sosnovsky, Senior ML Engineer) · Sumo Logic 기술 블로그 · https://www.sumologic.com/blog/self-hosted-vs-managed-apache-airflow |
| 날짜 | 발행 2022-11-07 · 확인 2026-10-11 · **「오래됨」** — 운영 구조 설명의 근거로만, 동향 근거로는 쓰지 않음 |
| 등급 | B — Airflow를 Kubernetes에 직접 올려 운영. 비용 항목은 RDS · Kubernetes 호스팅(금액 미공개). Kubernetes 클러스터는 별도 내부 팀이 관리해 업그레이드 · 비용 추적이 그 팀에 달림. 워커 용량은 할당 자원에 묶임. 직접 운영 이유로 조직의 기존 모니터링 · 알림 재사용, git에서 DAG 직접 동기화(롤백 용이)를 듦. 2.x 이관 때 커스텀 오퍼레이터가 깨지고 DB 버전이 맞지 않는 문제. 공식 차트가 아닌 커뮤니티 Helm 차트(airflow-helm) 사용 |
| 적용 상황 | Kubernetes 운영 조직이 따로 있고 그 위에 Airflow를 얹어 직접 운영하는 경우 |
| 구성 요소 | Kubernetes 클러스터(별도 팀), RDS 메타DB, 커뮤니티 Helm 차트, git 기반 DAG 동기화, 조직 공통 모니터링 · 알림 |
| 전제 조건 | Kubernetes를 운영하는 별도 인력 · 팀. 메이저 업그레이드 때 커스텀 코드와 DB 호환성 점검 |
| 걸리는 평가 축 | 비용 — 운영 인력(질적, 수치 없음) / 효과 — 기존 작업 이관(메이저 업그레이드 때 깨진 항목) / 효율 — 기존 모니터링 연결 |

### 비어 있는 것

- 비용 — 운영 인력의 수치(인원 · 인건비). 질적 근거는 근거 9 하나이고 「오래됨」
- 효과 — 처리량 · 지연 수치, Airflow 3로 이관한 최신 공개 사례(근거 9는 2022년 2.x 이관)
- 동향 적합성 — **직접 운영을 명시한 최근(2024-10-11 이후) 공개 기업 운영 사례 0건.** Airflow Summit의 Uber · OpenAI 세션 페이지는 날짜가 없고(D) 직접 운영인지도 적혀 있지 않음
- 커스터마이징 — 계정 · 조직 배치, 태깅, 가드레일 예외
- 데이터 정책 — 분류 · 민감정보 식별, 반출 경로 통제 · 처리 위치(마스킹 한계만 근거 5), 감사 로그를 중앙 로깅으로 보내는 경로
- AI 인프라 적합성 — Apache 재단 공식 MCP 서버 없음

넣지 않은 버린 건: 아키텍처 개요 문서(새 빈칸 없음), Airflow Summit 2025 세션 페이지 3건(날짜 없음 D), Summit 슬라이드 PDF(본문 읽기 불가).

---

## dbt (dbt Core / dbt platform)

ELT 변환 계층. 종류: 직접 운영(dbt Core v1 · dbt-oss v2를 자체 컴퓨트에서 실행) · 타사(dbt platform — dbt Labs가 운영하는 SaaS, 구 dbt Cloud) · 상태: GA. dbt v2.0이 2026-09-14에 출시됐고 2027-09-13까지 active 지원(https://docs.getdbt.com/docs/dbt-versions/core). v1.12는 2027-07-15까지 active. v2용 어댑터는 Snowflake · BigQuery · Redshift · Databricks가 GA, Spark · ClickHouse는 beta(https://docs.getdbt.com/docs/dbt-versions/dbt-cloud-release-notes, 2026-09 항목, 월 단위 표기).

### 근거 1 — dbt platform 요금제별 단가와 기능 배치

| 항목 | 내용 |
|---|---|
| 출처 | dbt Pricing · dbt Labs · https://www.getdbt.com/pricing |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — Developer는 무료(1석 · 월 3,000 모델), Starter는 사용자당 월 $100(5석 · 월 15,000 모델 · 초과분 과금, 초과 단가는 페이지에 없음), Enterprise · Enterprise+는 별도 견적. SSO · RBAC · SCIM · 컬럼 단위 리니지는 Enterprise부터, PrivateLink · IP 제한 · Hybrid Projects는 Enterprise+ |
| 적용 상황 | 관리형 dbt platform을 쓸 때 요금제를 고르는 기준 |
| 구성 요소 | dbt platform(브라우저 IDE, 잡 스케줄러, CI, Catalog, Semantic Layer, API) |
| 전제 조건 | 과금 단위가 좌석과 '월간 성공 모델 빌드 수'. 웨어하우스 컴퓨트 비용은 따로 듦(페이지에 언급 없음) |
| 걸리는 평가 축 | 비용 — 과금 단위 · 단가 / 커스터마이징 — 중앙 ID · SSO(SCIM), 네트워크(PrivateLink는 Enterprise+) / 데이터 정책 — 접근 통제(RBAC), 리니지(컬럼 단위는 Enterprise) |

### 근거 2 — 버전 지원 정책: v1 · v2 지원 기간과 업그레이드 방식

| 항목 | 내용 |
|---|---|
| 출처 | About dbt Core versions · dbt Labs 문서 · https://docs.getdbt.com/docs/dbt-versions/core |
| 날짜 | 갱신 2026-09-16 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — 마이너 버전마다 출시 후 1년 지원. v1.12 active(~2027-07-15), v1.11 critical(~2026-12-18). v1.3~1.7은 2027-01-31에 dbt platform에서 제거. v2.0은 2026-09-14 출시. v2 채널은 latest / canary / dev. dbt platform은 release track이 자동 업그레이드(Developer · Starter는 release track 필수) |
| 적용 상황 | 직접 운영할 때 버전을 고정하고 업그레이드 주기를 짜는 경우, 관리형에서 자동 업그레이드에 맡기는 경우 |
| 구성 요소 | dbt v1(Python) 계열, dbt v2(Rust 엔진) 계열, dbt platform release track |
| 전제 조건 | 직접 운영이면 매년 마이너 업그레이드가 필요 |
| 걸리는 평가 축 | 동향 적합성 — GA 여부 · 지원 종료 계획, 릴리스 활동 / 효율 — 업그레이드 · 패치 부담(관리형은 자동, 직접 운영은 직접 관리) |

### 근거 3 — 라이선스 분리: v1은 Apache 2.0, v2는 독점 배포판과 OSS 배포판

| 항목 | 내용 |
|---|---|
| 출처 | dbt licensing · dbt Labs 문서 · https://docs.getdbt.com/docs/dbt-licensing?version=2 |
| 날짜 | 갱신 2026-09-16 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — dbt v1은 Apache 2.0. dbt v2 기본 배포판(`dbt`)은 dbt Labs 소유로 dbt Product Licensing Agreement를 따름. `dbt-oss`는 v2의 Apache 2.0 배포판. v2 설치 · 실행은 무료이고 일부 기능은 로그인이나 유료 계정이 필요. 기업 규모 · 경쟁 서비스 제한 같은 조건은 이 페이지에 없음 → 〔미정〕. 문서는 엄격한 OSS 정책이 있는 조직에만 dbt-oss를 권함 |
| 적용 상황 | 라이선스 정책상 OSS만 쓸 수 있는지에 따라 배포판을 고르는 경우 |
| 구성 요소 | `dbt`(독점, SQL 린터 등 추가 기능), `dbt-oss`(Apache 2.0), dbt v1 `dbt-core` |
| 전제 조건 | 조직의 오픈소스 · 상용 라이선스 정책 |
| 걸리는 평가 축 | 동향 적합성 — 종속성(라이선스, 이관 경로), 로드맵 방향 / 비용 — 전환 비용(배포판 선택에 따른 기능 차이) |

### 근거 4 — dbt platform 호스팅 리전과 테넌시

| 항목 | 내용 |
|---|---|
| 출처 | Access, Regions, & IP addresses · dbt Labs 문서 · https://docs.getdbt.com/docs/cloud/about-cloud/access-regions-ip-addresses |
| 날짜 | 갱신 2026-09-09 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — dbt platform은 AWS · GCP · Azure에서 호스팅. AWS 리전은 us-east-1(모든 요금제), us-west-2 · eu-central-1 · ap-southeast-2 · ap-northeast-1 도쿄(이 넷은 Enterprise 전용). AWS 서울(ap-northeast-2)은 목록에 없음. dbt 계정 하나는 리전 하나만 쓸 수 있음. 단일 테넌트 · Virtual Private 배치는 Enterprise. dbt State는 현재 GCP US 리전에서만 제공 |
| 적용 상황 | 관리형 dbt platform이 메타데이터를 어느 리전에서 처리할지 정해야 할 때 |
| 구성 요소 | dbt platform 멀티테넌트 · 셀 기반 리전, Virtual Private · 단일 테넌트 배치 |
| 전제 조건 | us-east-1이 아닌 리전이나 단일 테넌트를 쓰려면 Enterprise |
| 걸리는 평가 축 | 데이터 정책 — 처리 위치 / 커스터마이징 — 계정 · 조직 배치(리전당 dbt 계정 1개, 단일 테넌트 선택지) |

### 근거 5 — dbt platform 감사 로그: 기록 범위 · 보존 · 내보내기

| 항목 | 내용 |
|---|---|
| 출처 | The audit log for dbt · dbt Labs 문서 · https://docs.getdbt.com/docs/cloud/manage-access/audit-log |
| 날짜 | 갱신 2026-07-23 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — 인증(SSO · 토큰), 권한 · 라이선스, 연결 · 자격 증명, 잡 · 환경, IP 제한, SCIM 이벤트 등을 행위자 · 시각과 함께 기록. 최소 12개월 보존(UI는 최근 90일). CSV 내보내기, Admin API v3로 조회 · 일괄 내보내기. Enterprise · Enterprise+ 전용 |
| 적용 상황 | 관리형 dbt platform의 사용자 · 설정 변경 이력을 중앙 감사 체계로 모을 때 |
| 구성 요소 | dbt platform 감사 로그, Administrative API v3 |
| 전제 조건 | Enterprise 이상 요금제, Account admin · Account viewer · Security admin 중 하나의 권한. CloudTrail · CloudWatch 직접 연동 서술은 없음(API로 가져와야 함) |
| 걸리는 평가 축 | 데이터 정책 — 접근 기록, 보존 / 효율 — 기존 감사 체계 연결(API 경유) |

### 근거 6 — dbt MCP 서버: 에이전트가 메타데이터 · 리니지 · 메트릭에 접근하는 경로

| 항목 | 내용 |
|---|---|
| 출처 | About dbt MCP server · dbt Labs 문서 · https://docs.getdbt.com/docs/dbt-ai/about-mcp |
| 날짜 | 갱신 2026-07-23 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — MCP 지원. 자체 호스팅(`uvx dbt-mcp`, v1 · v2 · 로컬 프로젝트, run · build · test 같은 CLI 명령 호출 가능)과 원격(dbt 호스팅 HTTP, CLI 명령 불가) 두 형태. Semantic Layer, SQL(text-to-SQL 포함), Discovery API 메타데이터(리니지 포함), Admin API 제공. OAuth나 토큰 인증. 도구 범위는 요금제에 포함된 API에 따라 다름. IP당 분당 5,000회. GA · 베타 여부와 권한 전파 모델은 서술 없음 → 〔미정〕 |
| 적용 상황 | AI 에이전트가 dbt가 관리하는 모델 · 메트릭 · 리니지를 조회하거나 dbt 작업을 호출할 때 |
| 구성 요소 | dbt-mcp 서버(자체 호스팅 또는 원격), Discovery · Semantic Layer · Admin API, MCP 클라이언트 |
| 전제 조건 | MCP 클라이언트. platform 연동 기능은 dbt platform 계정과 해당 API가 포함된 요금제 |
| 걸리는 평가 축 | AI 인프라 적합성 — 읽기 인터페이스, 메타데이터 · 스키마 노출, 작업 호출 · 결과 수신, 공개 표준 연계(MCP) |

### 근거 7 — DeNA 사례: dbt Core를 ECS Fargate와 Redshift Serverless로 운영

| 항목 | 내용 |
|---|---|
| 출처 | How DeNA Co., Ltd. accelerated anonymized data quality tests up to 100 times faster using Amazon Redshift Serverless and dbt · AWS Big Data Blog(DeNA 2명, AWS Japan 1명 공저) · https://aws.amazon.com/blogs/big-data/how-dena-co-ltd-accelerated-anonymized-data-quality-tests-up-to-100-times-faster-using-amazon-redshift-serverless-and-dbt |
| 날짜 | 발행 2024-12-17 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | B(사업자 선정 사례) — dbt Core 데이터 테스트를 ECS Fargate 컨테이너에서 실행. S3 파일 도착 → EventBridge → Step Functions로 기동. Redshift Serverless는 workgroup을 나눠 IAM으로 접근 통제. 로그는 CloudWatch Logs, 알람은 SNS → Lambda. 매월 테스트 약 1,300건 · 데이터 약 10TB. 처리 시간 단축과 비용 약 90% 절감 수치는 고객 측 주장이라 근거로 쓰지 않음 |
| 적용 상황 | 이벤트 기반 일괄 변환 · 품질 테스트를 dbt Core 직접 운영으로 처리하는 구조 |
| 구성 요소 | dbt Core, ECS / Fargate, EventBridge, Step Functions, Redshift Serverless(workgroup 분리), CloudWatch Logs · Alarms, SNS, Lambda, elementary CLI |
| 전제 조건 | 컨테이너 실행 환경과 오케스트레이터(Step Functions)를 직접 구성. 원천 측이 완료 파일로 전송 완료를 알려야 함 |
| 걸리는 평가 축 | 효과 — 처리 방식(이벤트 기반 일괄), 원천 · 대상 연결(S3 → Redshift Serverless), 작업 의존성 · 일정 / 효율 — 관리할 구성요소 수, 기존 모니터링 · 로깅 연결(CloudWatch) / 동향 적합성 — 운영 사례 / 비용 — 인프라 사용료(서버리스 종량제) / 커스터마이징 — workgroup 배치, IAM |

### 근거 8 — dbt platform의 AWS PrivateLink 사설 연결

| 항목 | 내용 |
|---|---|
| 출처 | About private connectivity(PrivateLink) · dbt Labs 문서 · https://docs.getdbt.com/docs/cloud/secure/about-privatelink |
| 날짜 | 갱신 2026-07-23 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — AWS PrivateLink로 dbt 환경과 AWS 데이터 플랫폼을 연결하면 트래픽이 공용 인터넷을 지나지 않음. dbt와 데이터 플랫폼이 같은 클라우드에 있어야 함. Enterprise+와 Virtual Private에서만, 북미 · 유럽 · 아시아 대부분 리전 지원. 사설 엔드포인트 설정에는 Extended Attributes 사용(환경 변수 불가). Admin API v3로 엔드포인트 조회 · 생성 · 수정 · 삭제. 연결 가능한 AWS 서비스 목록은 이 페이지에 없음 〔미정〕 |
| 적용 상황 | 관리형 dbt platform이 사설망 웨어하우스에 붙고 데이터 경로를 공용 인터넷에서 떼야 할 때 |
| 구성 요소 | dbt platform(Enterprise+ 또는 Virtual Private), AWS PrivateLink 엔드포인트, Extended Attributes, Admin API v3 |
| 전제 조건 | Enterprise+ 이상(영업 문의), 데이터 플랫폼이 AWS에 있을 것, 리전의 PrivateLink 지원 |
| 걸리는 평가 축 | 데이터 정책 — 반출 경로 통제 / 커스터마이징 — 네트워크(사설 연결) |

### 근거 9 — dbt v1에서 v2로 옮기는 공식 절차

| 항목 | 내용 |
|---|---|
| 출처 | dbt Core v2 is here · dbt Labs 공식 블로그(Joel Labes, Grace Goheen) · https://docs.getdbt.com/blog/dbt-core-v2-is-here |
| 날짜 | 발행 2026-06-01 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — 공식 이관 절차 4단계: ① v1.12(또는 dbt platform Latest track)로 올림 ② dbt-autofix 패키지와 migrating-dbt-core-to-v2 에이전트 스킬로 자동 수정 ③ `dbt parse --use-v2-parser`로 파싱 호환성 확인 ④ v2 설치. v1은 PyPI · GitHub에 계속 남음. 당장 옮기지 않아도 되지만 앞으로 일부 기능은 업그레이드 필요. 글 발행 시점 v2는 알파(GA는 근거 2) |
| 적용 상황 | dbt v1으로 운영 중인 변환 작업을 v2 엔진으로 옮길 때 |
| 구성 요소 | dbt v1.12, dbt-autofix, migrating-dbt-core-to-v2 에이전트 스킬, v2 파서 |
| 전제 조건 | v1.12 동작 변경과 파싱 호환성 점검 통과. dbt가 아닌 도구에서 옮겨 오는 경로는 없음 |
| 걸리는 평가 축 | 효과 — 기존 작업 이관(v1 → v2) / 비용 — 전환 비용(자동 수정 도구가 있다는 사실까지, 공수 수치 없음) |

### 비어 있는 것

- 비용 — Starter 초과 모델 단가, Enterprise 단가(별도 견적), 운영 인력 규모, 전환 비용 수치
- 효과 — 실시간(스트리밍) 처리 지원 여부, dbt platform 가용성 SLA 수치, dbt가 아닌 변환 도구에서 옮겨 오는 이관 경로
- 효율 — dbt platform 로그의 CloudWatch · CloudTrail 직접 연동(API 경유만 확인)
- 커스터마이징 — 랜딩존 안에서 어느 AWS 계정에 둘지, 가드레일(SCP) 예외 필요 여부, 태깅 · 중앙 로깅 연동
- 데이터 정책 — 분류 · 민감정보 식별, 보존 · 삭제(감사 로그 보존 외), PrivateLink로 연결할 수 있는 AWS 서비스 목록
- AI 인프라 적합성 — MCP 서버의 GA 여부, 사용자 권한이 에이전트까지 이어지는 방식
- 동향 적합성 — dbt Product Licensing Agreement 세부 조건(약관 원문 미확인)

넣지 않은 버린 건(새로 채우는 빈칸 없음): Redshift · Athena · Glue 어댑터 문서(Glue 어댑터는 dbt Labs 지원 대상이 아닌 커뮤니티 플러그인), Fivetran 합병 완료 보도자료(2026-06-01), 컬럼 단위 리니지 문서, dbt Summit 2026 프리뷰 블로그(예고 · 자기 주장 D).

---

## Cloud Composer

GCP 관리형 Apache Airflow(현 명칭 Managed Service for Apache Airflow) — 타사 비교용, MWAA 대응. 상태: GA. Gen 3 빌드는 각각 12개월 지원, Gen 1은 2026-09-15 지원 종료(근거 1). 2026-04-15 공지로 개명, 같은 날 Gen 3에서 Airflow 3 GA(https://docs.cloud.google.com/composer/docs/release-notes). Gen 3 자체의 GA 날짜 〔미정〕. 문서는 Composer 1 / 2 / 3을 Gen 1 / 2 / 3으로 부른다.

### 근거 1 — 세대별 버전 지원 정책과 지원 종료 일정

| 항목 | 내용 |
|---|---|
| 출처 | Managed Service for Apache Airflow versioning overview · Google Cloud · https://docs.cloud.google.com/composer/docs/composer-versioning-overview |
| 날짜 | 갱신 2026-10-08 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — Gen 3 Airflow 빌드는 릴리스 후 12개월 지원, Airflow 2 · 3 모두 제공. 2025-07-01 이전 빌드 중 종료일이 없던 것은 2026-07-01까지. Gen 2는 버전당 12개월, 2.0.x는 2026-09-15 수명 종료, 2026년 9월부터 Airflow 2.11 빌드만 새로 나옴. Gen 1은 2024-03-25 사후 유지보수 모드, 2026-09-15 전 환경 수명 종료, Gen 3 이관 권고 |
| 적용 상황 | 세대 · 버전을 고르고 업그레이드 주기를 계획할 때 |
| 구성 요소 | Gen 1 / 2 / 3 환경, Airflow 빌드 |
| 전제 조건 | Gen 3는 인프라만 자동 업데이트, Airflow 버전은 사용자가 올림. Gen 2 · 1은 자동 업그레이드 없음. 지원 끝난 빌드도 돌지만 보안 취약점은 업그레이드로만 해결되는 경우가 있음 |
| 걸리는 평가 축 | 동향 적합성 — GA 여부 · 지원 종료 계획, 릴리스 활동 / 효율 — 업그레이드 · 패치 부담 |

### 근거 2 — Gen 3 구조: Google이 운영하는 구성요소와 사용자가 맡는 범위

| 항목 | 내용 |
|---|---|
| 출처 | Managed Airflow (Gen 3) overview · Google Cloud · https://docs.cloud.google.com/composer/docs/composer-3/composer-overview |
| 날짜 | 갱신 2026-10-08 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — Google이 프로비저닝 · 운영: 환경당 GKE 클러스터 1개(스케줄러 · 트리거러 · 워커), 웹 서버, 관리형 메타데이터 DB(사용자 DB 지정 불가, 표준은 단일 존, 고복원성은 멀티존 primary / standby), Cloud Storage 버킷(DAG · 로그 · 플러그인). 사용자 담당: 환경 설정, DAG · 플러그인 · PyPI 패키지, 커넥션, 설정 오버라이드, IAM, Airflow UI 접근 통제. 로그는 Cloud Logging, 메트릭은 Cloud Monitoring. CMEK · 리니지 연동 지원 |
| 적용 상황 | 직접 운영 Airflow와 관리 부담을 비교할 때 |
| 구성 요소 | GKE 클러스터, 웹 서버, 관리형 메타DB, Cloud Storage 버킷 |
| 전제 조건 | GCP 프로젝트 단위 보안 관리. 상세 책임 분담 문서는 열지 않음 |
| 걸리는 평가 축 | 효율 — 관리할 구성요소 수, 관리형 / 직접 운영 비중, 기존 모니터링 · 로깅 연결 / 효과 — 가용성(고복원성 DB) |

### 근거 3 — VPC 연결 방식과 Shared VPC에서의 프로젝트 배치

| 항목 | 내용 |
|---|---|
| 출처 | Connect an environment to a VPC network (Gen 3) · Google Cloud · https://docs.cloud.google.com/composer/docs/composer-3/connect-vpc-network |
| 날짜 | 갱신 2026-10-08 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — 네트워크 연결은 network attachment. 네트워크 · 서브넷을 지정하면 attachment를 만들고 환경 삭제 때 같이 지움. 기존 attachment 재사용은 같은 프로젝트에서만. Shared VPC에서는 attachment가 서비스 프로젝트에 있고 Shared VPC 네트워크에 연결. Private IP 기본 라우팅은 Private Google Access 대상 외 트래픽을 VPC로 보내고 VPC 사설 DNS 영역을 자동 사용. 인터넷 접근은 VPC 설정을 따름 |
| 적용 상황 | 환경을 고객 VPC나 Shared VPC(호스트 / 서비스 프로젝트 구조)에 붙일 때 |
| 구성 요소 | network attachment, VPC · 서브넷, Shared VPC 호스트 / 서비스 프로젝트 |
| 전제 조건 | 서브넷에 환경당 빈 IP 4개. 내부 대역 /20(기본 100.64.128.0/20)은 서브넷과 겹치면 안 되고 생성 후 변경 불가. 사용자 .internal DNS 영역 미지원, 전이 DNS 피어링 2홉까지. Terraform으로 VPC 분리 불가 |
| 걸리는 평가 축 | 커스터마이징 — 계정 · 조직 배치(Shared VPC 서비스 프로젝트), 네트워크(VPC) |

### 근거 4 — 보안 기능: Private IP, VPC Service Controls, CMEK, IAM, Secret Manager, 데이터 위치

| 항목 | 내용 |
|---|---|
| 출처 | Managed Airflow security overview (Gen 3) · Google Cloud · https://docs.cloud.google.com/composer/docs/composer-3/composer-security-overview |
| 날짜 | 갱신 2026-10-08 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — Private IP 환경(공인 인터넷 직접 접근 없음). VPC SC 경계로 반출 위험 감소(Private IP 환경만 경계 안에 생성 가능). CMEK(기본은 Google 관리 키). IAM 역할로 환경 작업 통제, Airflow UI는 별도 RBAC. Domain Restricted Sharing. Secret Manager를 커넥션 · 변수 백엔드로. 데이터 상주 · 위치 제한을 지원 항목으로 표기(설정 문서는 링크만). 감사 로그는 링크만 있고 내용 설명 없음 |
| 적용 상황 | 네트워크 격리, 반출 통제, 키 관리 요건이 있는 조직 |
| 구성 요소 | Private IP, VPC SC, CMEK, IAM, Airflow RBAC, Secret Manager |
| 전제 조건 | VPC SC를 쓰려면 생성 시점에 Private IP로 만들어야 함 |
| 걸리는 평가 축 | 커스터마이징 — 네트워크(VPC), 중앙 ID 연동(IAM · 도메인 제한) / 데이터 정책 — 접근 통제, 반출 경로 통제 · 처리 위치 |

### 근거 5 — 데이터 리니지 연동(OpenLineage → Data Lineage API)

| 항목 | 내용 |
|---|---|
| 출처 | Data lineage integration (Gen 3) · Google Cloud · https://docs.cloud.google.com/composer/docs/composer-3/lineage-integration |
| 날짜 | 갱신 2026-10-08 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — 리니지를 Knowledge Catalog 기능으로 표기. 미리 설치된 apache-airflow-providers-openlineage가 이벤트를 만들고 Data Lineage API가 받음. API가 켜져 있으면 환경 생성 때 자동 활성화, 환경별 켜고 끄기. 지원 오퍼레이터는 provider 패키지마다 다름, 미지원은 inlets / outlets로 직접 정의. 리니지 API 쿼터 · 요금 별도, 태스크 끝에 평균 1~2초 추가. 리니지 보고 실패해도 태스크는 실패하지 않음 |
| 적용 상황 | 오케스트레이션 작업의 원천 → 대상 흐름을 카탈로그에 남겨야 할 때 |
| 구성 요소 | OpenLineage 프로바이더, Data Lineage API, Knowledge Catalog |
| 전제 조건 | Data Lineage API 활성화, 커스텀 Lineage Backend 미설정. 기능에 따라 VPC SC 준수 범위가 다름 |
| 걸리는 평가 축 | 데이터 정책 — 리니지 · 카탈로그 연결 / 동향 적합성 — 종속성(공개 표준 OpenLineage) / AI 인프라 적합성 — 메타데이터 노출 |

### 근거 6 — 원격 MCP 서버(에이전트용 인터페이스)

| 항목 | 내용 |
|---|---|
| 출처 | Use the Managed Service for Apache Airflow remote MCP server · Google Cloud · https://docs.cloud.google.com/composer/docs/composer-2/use-composer-mcp ; GA는 릴리스 노트 2026-08-25 항목 · https://docs.cloud.google.com/composer/docs/release-notes |
| 날짜 | 갱신 2026-10-08 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — 엔드포인트 composer.{region}.rep.googleapis.com/mcp, Streamable HTTP. OAuth 2.0 + IAM 인증, 읽기 전용 / 읽기 · 쓰기 scope 구분, 도구 호출에 MCP Tool User 역할. 도구 예: list_environments, create_environment, manage_pypi_packages, find_last_failed_dag_runs, list_failed_task_instances, get_task_instance, get_dag_source_code. IAM allow / deny 정책으로 주체 · 읽기 전용 속성 · 도구 이름 · OAuth 클라이언트별 필터링. 에이전트용 별도 ID 권장. Model Armor 로깅을 켜면 payload 전체가 기록될 수 있다는 주의 |
| 적용 상황 | AI 에이전트가 환경과 DAG 실행 상태를 조회하거나 조작할 때 |
| 구성 요소 | 원격 MCP 엔드포인트, OAuth 2.0, IAM 역할 · 정책 |
| 전제 조건 | MCP 서버 활성화(Service Usage Admin), 에이전트 ID에 역할 부여 |
| 걸리는 평가 축 | AI 인프라 적합성 — 에이전트 인터페이스, 권한 전파, 작업 호출 · 결과 수신, 공개 표준 연계(MCP) |

### 근거 7 — Checkout.com: 다른 하이퍼스케일러의 자체 운영 Airflow를 Gen 3로 이관

| 항목 | 내용 |
|---|---|
| 출처 | How Checkout.com tallies data with Managed Service for Apache Airflow · Google Cloud Blog(Google PM 등, Checkout.com 엔지니어 협조) · https://cloud.google.com/blog/products/data-analytics/how-checkout-com-tallies-data-with-cloud-composer-3 |
| 날짜 | 발행 2026-07-23 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | B(사업자 선정 사례) — 도입 배경과 구성. 이관 전: 피크 기준 고정 프로비저닝, 패치 · 업그레이드 부담, DAG 하나가 환경 전체에 영향, DAG 동기화 약 6분. 이관 후: 동적 스케일링, DAG별 실행 격리, 정기 유지보수 시간대에 Google이 패치, DAG 동기화 거의 즉시, 컨테이너화된 dbt 실행. 월 비용 약 30% 절감 추정 · MTTR 단축 같은 전후 비교는 D라 근거로 쓰지 않음 |
| 적용 상황 | 직접 운영하던 Airflow(다른 클라우드, S3 DAG 저장)를 관리형으로 옮기는 경우 |
| 구성 요소 | Gen 3 환경, Cloud Storage DAG 동기화, 컨테이너 dbt, Cloud Logging · Monitoring |
| 전제 조건 | DAG와 의존성을 Gen 3 패키지 구성에 맞출 수 있어야 함(상세 없음). 네트워크 구성은 다루지 않음 |
| 걸리는 평가 축 | 효과 — 기존 작업 이관, 지연 / 동향 적합성 — 운영 사례 / 효율 — 업그레이드 · 패치 부담 |

### 근거 8 — Airflow 3.1 GA 스케줄링 기능과 서비스 간 배포 프레임워크

| 항목 | 내용 |
|---|---|
| 출처 | Managed Apache Airflow: Scaling Data & AI Workloads · Google Cloud Blog(Piotr Wieczorek, Rafal Biegacz — Google) · https://cloud.google.com/blog/products/data-analytics/managed-apache-airflow-scaling-data-and-ai-workloads |
| 날짜 | 발행 2026-05-05 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — 벤더 공식 블로그의 기능 사실. Airflow 3.1 GA: 실행 계층 분리, DAG 버전 관리(구조 · 실행 이력 보존), 스케줄러가 관리하는 백필, asset 기반 · 외부 이벤트(예: 메시지 큐 도착) 트리거, Human-in-the-Loop 일시정지, 시간 기준 deadline alert. YAML로 정의하는 오케스트레이션 파이프라인, 서비스 간 Deployment Automation Framework 번들(예시 dbt · Spark · DTS), GitHub Actions로 검증 · 배포. MTTR 단축 같은 효과 주장은 수치 없는 벤더 주장이라 쓰지 않음. 이 글의 MCP Public Preview 표기는 이후 GA(근거 6)로 바뀌어 쓰지 않음 |
| 적용 상황 | 데이터 · 이벤트 기반 트리거, 백필, 마감 경보가 필요한 흐름. dbt · Spark 같은 처리 서비스를 묶어 한 단위로 배포 |
| 구성 요소 | Airflow 3.1, asset · 이벤트 트리거, YAML 파이프라인, Deployment Automation Framework, GitHub Actions |
| 전제 조건 | Gen 3 환경에서 Airflow 3.1 이상. 스트리밍 · 실시간 처리 설명은 없음(이벤트 트리거까지). 앞으로의 계획은 밝히지 않음 |
| 걸리는 평가 축 | 효과 — 작업 의존성 · 일정, 처리 방식(이벤트 트리거까지), 원천 · 대상 연결(번들 예시까지) |

### 근거 9 — Gen 3 과금 단위: DCU-시간 + DB 스토리지 GiB-시간

| 항목 | 내용 |
|---|---|
| 출처 | Managed Service for Apache Airflow 가격 책정 · Google Cloud · https://cloud.google.com/products/managed-service-for-apache-airflow/pricing (https://cloud.google.com/composer/pricing 에서 넘어감, 내장 브라우저로 열어 확인) |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — Gen 3는 실제 실행 기간만 청구. SKU는 ① 표준 milliDCU-시간 — Iowa(us-central1) 기준 1,000 milliDCU-시간(= 1 DCU-시간)당 $0.06, 1년 약정 $0.054 · 3년 약정 $0.048 ② DB 스토리지 GiB-시간당 $0.000232877(Cloud SQL 최소 10GiB, 늘어나면 줄지 않음) ③ 네트워크 데이터 전송은 VPC 네트워크 요금을 따름. DCU는 Airflow 작업자 · 스케줄러 · DAG 프로세서 · 트리거 · 웹 서버의 vCPU · 메모리 · 스토리지와 환경 크기(관리형 인프라)를 합친 단위이고, 작업자 자동 확장을 따라 변함. 고복원성 모드는 단가는 같고 DCU 소비가 늘며, DB 스토리지 비용은 약 2배. 별도 비용: 환경의 Cloud Storage 버킷(저장 · 작업 요금), 스냅샷, Cloud Monitoring, CMEK 사용 시 KMS. Gen 2는 CPU · 메모리 · 스토리지 SKU + 환경 크기 요금(소형 $0.35/h 등)으로 과금 모델이 다름 |
| 적용 상황 | Gen 3 환경의 비용 산정, MWAA(인스턴스 시간)와 과금 단위 비교 |
| 구성 요소 | milliDCU-시간 SKU, DB 스토리지 SKU, 네트워크 전송 SKU, 약정 사용 할인(Gen 3만) |
| 전제 조건 | 페이지 표는 us-central1 단가. 서울 등 다른 리전 단가 〔미정〕. DCU 사용량은 작업자 수 · 환경 크기에 따라 달라 산식에 추정치가 필요 |
| 걸리는 평가 축 | 비용 — 과금 단위 · 단가, 인프라 사용료 |

### 비어 있는 것

- 비용 — 서울 등 us-central1 외 리전 단가, 전환 비용(MWAA → Composer)
- 효과 — 스트리밍 · 실시간 처리 지원 여부, 커넥터 · 오퍼레이터 지원 범위
- 동향 적합성 — 로드맵 방향
- 커스터마이징 — 가드레일 예외 필요 여부, 태깅 · 중앙 로깅
- 데이터 정책 — 분류 · 민감정보 식별, 보존 · 삭제, 접근 기록(감사 로그 세부)
- AI 인프라 적합성 — 스키마 노출(리니지 이벤트 외)

넣지 않은 버린 건(새로 채우는 빈칸 없음): Scale environments · Optimize environments · Access control · Migrate to Gen 3 · composer-versions 페이지.

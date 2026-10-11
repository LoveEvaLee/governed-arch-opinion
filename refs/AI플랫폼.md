# 참조 — AI · 에이전트 플랫폼

수집일: 2026-10-11 · 검색 27회 / 상한 40회 · 버린 건 46건 · 선택지당 근거 상한 10건 · 영역 3-2

**이 파일의 결정 (2026-10-11 유경)**

- 선택지 6개. 모델 접근 · 에이전트 런타임 · 지식(RAG) · 도구 연계 층을 섞어서 본다 — 실제 점검은 층을 나누지 않고 함께 하기 때문
- **MCP는 선택지가 아니라 확인 기능으로 쓴다.** 선택지마다 MCP 지원 방식(공식 MCP 서버 / MCP 게이트웨이 / 클라이언트 / 미지원)을 AI 인프라 적합성 축의 필수 확인 항목으로 수집했다
- 타사 대응은 GCP(Vertex AI) — 3-1 Cloud Composer와 같은 사업자로 맞춤
- 선택지 이름은 회사 쪽 지정 없이 Claude가 넣었다(유경 위임). 꼭 넣을 선택지가 생기면 바꿔 넣는다 〔미정〕
- 「오래됨」 기준은 이 영역만 12개월 — 발행 · 갱신이 2025-10-11 이전이면 동향 근거로 쓰지 않는다
- 날짜가 없는 공식 문서 · 요금 페이지는 「상시 갱신 — 확인일 기준」으로 적고 등급을 유지한다

**읽는 법.** 판정(상 · 중 · 하)은 없다 — ③④⑤가 이 근거로 판정한다. 근거 칸에 "D"로 적힌 수치(벤더 · 고객의 전후 비교 주장)는 근거로 쓰지 않는다. 〔미정〕은 열어 본 페이지에서 확인하지 못한 것이다. 원문은 요지만 옮겼다.

## 선택지 요약

| 선택지 | 맡는 층 | 종류 | 상태 (확인 2026-10-11) | MCP 지원 방식 | 근거 건수 (A/B/C/D) |
|---|---|---|---|---|---|
| Amazon Bedrock AgentCore | 에이전트 런타임 · 게이트웨이 · 아이덴티티 · 메모리 · 관측 | 관리형 | GA 2025-10-13. 서울은 GA 이후 추가(Runtime V2 · Registry 등 일부 미지원) | 관리형 MCP 게이트웨이(Gateway) | 9 / 1 / 0 / 0 |
| Amazon Bedrock | 모델 접근 · 지식(RAG) · 안전 장치 | 관리형 | Managed KB GA 2026-06-17(서울 없음). customer-managed KB 일부 커넥터 신규 생성 중단 2026-09-30. 본체 GA 명시 〔미정〕 | Bedrock이 MCP 클라이언트(Responses API 서버 측 도구, 일부 모델) | 9 / 1 / 0 / 0 |
| LangGraph | 에이전트 프레임워크 · 런타임 | 직접 운영(OSS) · 타사 관리형(LangSmith Deployment) | OSS GA 1.0 2025-10-17. LangSmith Deployment GA 표기 〔미정〕 | 서버 /mcp(공식) · 클라이언트 langchain.mcp(베타) | 10 / 0 / 0 / 0 |
| LiteLLM 직접 운영 | 모델 게이트웨이 · 라우팅 · 비용 통제 | 직접 운영(OSS + Enterprise 라이선스) | 〔미정〕 — 주간 안정판 릴리스, GA 표기 없음 | MCP 게이트웨이(OSS 포함) | 10 / 0 / 0 / 0 |
| Vertex AI Agent Engine | 에이전트 런타임 + 모델 접근 | 타사 관리형 | GA 2025-03-04. 2026-04-22 "Agent Runtime on Gemini Enterprise Agent Platform"으로 개명 | 관리형 MCP 게이트웨이(Agent Gateway, 서울 미지원) · ADK 클라이언트 · 플랫폼 원격 MCP 서버 | 9 / 1 / 0 / 0 |
| vLLM 직접 운영 | 모델 서빙 | 직접 운영(OSS, PyTorch Foundation) | 〔미정〕 — 0.x 2주 주기 릴리스, 최신 v0.31.0 | 엔진 내장 MCP 클라이언트(gpt-oss · Responses API 한정) | 9 / 1 / 0 / 0 |

---

## Amazon Bedrock AgentCore

AWS 관리형 에이전트 실행 기반. 상태: GA — 2025-10-13 What's New(근거 1). 하위 기능마다 상태가 다르다 — Runtime V2는 2026-09-18 공지에 "now available"만 있고 GA · 프리뷰 표기가 없어 〔미정〕(근거 10), AgentCore Insights는 요금 페이지에 퍼블릭 프리뷰로 표기.

### 근거 1 — GA 발표: 9개 리전 GA(서울 없음), VPC · PrivateLink · CloudFormation · 태깅 지원

| 항목 | 내용 |
|---|---|
| 출처 | Amazon Bedrock AgentCore is now generally available · AWS What's New · https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available/ |
| 날짜 | 발행 2025-10-13 · 확인 2026-10-11 · 오래됨 아님(기준일 2025-10-11보다 이틀 뒤) |
| 등급 | A — GA 리전 9곳(us-east-1/2, us-west-2, 뭄바이, 싱가포르, 시드니, 도쿄, 프랑크푸르트, 아일랜드 — 서울 없음). 모든 서비스에서 VPC · PrivateLink · CloudFormation · 리소스 태깅 지원. Gateway가 기존 MCP 서버 연결, Runtime이 A2A 지원. Observability는 CloudWatch 대시보드 기반, OTEL 호환 |
| 적용 상황 | 관리형 에이전트 실행 기반을 프로덕션에 들일 때 GA 여부와 기본 거버넌스 기능 확인 |
| 구성 요소 | Runtime, Memory, Gateway, Identity(identity-aware 권한 부여, refresh token 보관소), Observability |
| 전제 조건 | 지원 리전의 AWS 계정. 서울 지원은 근거 2에서 따로 확인 |
| 걸리는 평가 축 | 동향 적합성 — GA 여부 · 로드맵 방향 / 커스터마이징 — 네트워크(VPC), 태깅 / 효율 — 기존 모니터링 연결(CloudWatch · OTEL) / AI 인프라 적합성 — 공개 표준 연계(MCP · A2A) |

### 근거 2 — 기능별 지원 리전: 서울은 핵심 기능 대부분 지원, 일부 미지원

| 항목 | 내용 |
|---|---|
| 출처 | Supported AWS Regions · AgentCore Developer Guide · https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-regions.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — 서울(ap-northeast-2)은 harness, Runtime microVMs, Memory, Gateway, Identity, Built-in Tools, Observability, Policy, Evaluations, optimization 지원. Runtime Instances, payments, AWS Agent Registry, Web Search Tool은 서울 미지원 |
| 적용 상황 | 처리 위치를 국내 리전에 두려 할 때 쓸 수 있는 기능 판단 |
| 구성 요소 | 기능별 · 리전별 지원 매트릭스(22개 리전과 GovCloud) |
| 전제 조건 | 쓰려는 기능이 서울 지원 목록에 있어야 함. Runtime V2는 서울 없음(근거 10). 서울이 언제 추가됐는지 〔미정〕 |
| 걸리는 평가 축 | 동향 적합성 — GA 범위(리전) / 데이터 정책 — 처리 위치 / 커스터마이징 — 계정 · 리전 배치 |

### 근거 3 — 요금: 구성요소별 사용량 과금, 선불 · 최소 요금 없음

| 항목 | 내용 |
|---|---|
| 출처 | Amazon Bedrock AgentCore Pricing · AWS · https://aws.amazon.com/bedrock/agentcore/pricing/ |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — Runtime microVM v1 vCPU-시간 $0.0895 · GB-시간 $0.00945, v2(사용량 기준) vCPU-시간 $0.1276 · GB-시간 $0.0169(v2 약정 베이스라인은 2026년 10월까지 출시 예정). Runtime Instances는 EC2 요금 + 관리 수수료(%). Gateway API 호출 1,000건당 $0.005, Search 호출 1,000건당 $0.025, 도구 100개 인덱싱당 월 $0.02, VPC로 나가는 egress GB당 $0.006. Identity는 비AWS 자원용 토큰 · API 키 요청 1,000건당 $0.010(Runtime · Gateway 경유 시 무료). Memory 단기는 2026-10-06부터 수집 GB당 $1.00, 장기는 저장 레코드 1,000건당 월 $0.75. Observability는 CloudWatch 요금. Policy 권한 요청당 $0.000025. Evaluations는 토큰 · 건수 단위 |
| 적용 상황 | 실행 · 도구 호출 · 메모리 · 관측 비용을 구성요소별로 추정 |
| 구성 요소 | Runtime, Gateway, Identity, Memory, Observability, Browser, Code Interpreter, Policy, Evaluations |
| 전제 조건 | 리전별 단가 표기 없음(Gateway egress만 "상용 리전" 명시) — 서울 단가 〔미정〕. Policy 자연어 작성 단가가 표와 기능 설명에서 단위가 다르게 적혀 있음 |
| 걸리는 평가 축 | 비용 — 과금 단위 · 단가, 인프라 사용료 |

### 근거 4 — 서비스 개요: 모듈형, 프레임워크 · 모델 제약 없음, 고객 콘텐츠 활용 고지

| 항목 | 내용 |
|---|---|
| 출처 | What is Amazon Bedrock AgentCore? · AgentCore Developer Guide · https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — 서비스를 따로 또는 함께 사용(Harness, Runtime, Memory, Gateway, Identity, Code Interpreter, Browser, Observability, Payments, Evaluations, Optimization, Policy, Registry). Runtime은 CrewAI · LangGraph · LlamaIndex · Google ADK · OpenAI Agents SDK · Strands Agents, Bedrock 안팎 모델, MCP · A2A 지원. Memory는 LangGraph · LangChain · Strands · LlamaIndex 연동. 실시간 상호작용과 비동기 장기 실행, 세션 격리. "AgentCore가 서비스 개선을 위해 고객 콘텐츠를 사용 · 저장할 수 있다"(해당 고객 사용분 개선 한정)는 고지가 있음 |
| 적용 상황 | 오픈소스 프레임워크로 만든 에이전트를 관리형 실행 기반으로 옮길 때 |
| 구성 요소 | 위 13개 서비스. Registry는 에이전트 · MCP 서버 · 도구 · 스킬 카탈로그 |
| 전제 조건 | 에이전트를 컨테이너 이미지나 코드로 배포할 수 있어야 함 |
| 걸리는 평가 축 | 효과 — 처리 방식(실시간 · 비동기), 기존 작업 이관(프레임워크 호환) / 동향 적합성 — 종속성(오픈소스 프레임워크 · 공개 프로토콜) / 데이터 정책 — 반출 경로(서비스 개선용 콘텐츠 사용 고지) / AI 인프라 적합성 — 작업 호출 · 결과 수신 |

### 근거 5 — Gateway의 MCP 지원: 관리형 MCP 게이트웨이(집계 모드)

| 항목 | 내용 |
|---|---|
| 출처 | AgentCore Gateway 개요 · Supported targets · MCP targets · AgentCore Developer Guide · https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html · https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-supported-targets.html · https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-targets-mcp.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — **MCP 지원 방식: 관리형 MCP 게이트웨이.** Lambda, API Gateway REST 스테이지, OpenAPI, Smithy, 기존 MCP 서버, 통합 템플릿, 빌트인 커넥터를 MCP 도구로 바꿔 하나의 가상 MCP 서버로 묶어 노출(통합 `tools/list`). 대상 종류는 MCP · HTTP 패스스루(A2A 포함) · 추론 라우팅. 시맨틱 도구 검색, 대상별 3LO OAuth, 인바운드 · 아웃바운드 인증, 대상별 자격증명 주입. Salesforce · Slack · Jira · Asana · Zendesk 1-클릭 연동 |
| 적용 상황 | 사내 API · Lambda를 바꾸지 않고 MCP 도구로 노출해 여러 에이전트가 공유할 때 |
| 구성 요소 | Gateway 엔드포인트, 대상(MCP / HTTP / Inference), 자격증명 공급자, 세분화 권한 |
| 전제 조건 | 대상 API의 OpenAPI · Smithy 스키마나 Lambda, 아웃바운드 인증용 자격증명 공급자(Identity) |
| 걸리는 평가 축 | AI 인프라 적합성 — 공개 표준 연계(MCP), 데이터 읽기 인터페이스, 메타데이터 노출(도구 목록 · 검색), 권한 전파 / 효과 — 원천 · 대상 연결 |

### 근거 6 — Identity: 기존 IdP 연동, 토큰 보관소, 사용자 위임(3LO)

| 항목 | 내용 |
|---|---|
| 출처 | Features of AgentCore Identity · AgentCore Developer Guide · https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/key-features-and-benefits.html (상위 https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — 에이전트를 워크로드 아이덴티티(고유 ARN, 계층형 디렉터리)로 관리. 토큰 보관소가 OAuth 토큰 · 클라이언트 자격증명 · API 키를 KMS(고객 관리형 또는 서비스 관리형)로 암호화. OAuth 2.0 client credentials(2LO)와 authorization code(3LO, 사용자 동의 기반 위임). 사용자 대신 동작하는 impersonation 흐름, 요청마다 서명 · 만료 · scope 검증과 상세 로그. Cognito · Okta · Entra ID · Auth0 같은 IdP 호환 |
| 적용 상황 | 사내 SSO 사용자 권한을 에이전트의 외부 도구 호출까지 전파할 때 |
| 구성 요소 | 워크로드 아이덴티티 디렉터리, 인바운드 JWT 권한 부여기, 자격증명 공급자, 토큰 보관소, SDK 데코레이터 |
| 전제 조건 | OAuth 2.0 · OIDC 호환 IdP, 3LO는 사용자 동의 흐름(리턴 URL) 설정 |
| 걸리는 평가 축 | 커스터마이징 — 중앙 ID · SSO 연동 / 데이터 정책 — 접근 통제 · 접근 기록 / AI 인프라 적합성 — 권한 전파 |

### 근거 7 — VPC 연결과 PrivateLink

| 항목 | 내용 |
|---|---|
| 출처 | Configure AgentCore Runtime and tools for VPC · Use interface VPC endpoints (AWS PrivateLink) · AgentCore Developer Guide · https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-vpc.html · https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/vpc-interface-endpoints.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — Runtime · Code Interpreter · Browser는 서비스 연결 역할로 고객 VPC에 ENI를 만들어 사설 자원에 접근(서울 AZ apne2-az1~3 지원). VPC 모드는 기본 인터넷 차단, NAT 경유로만 나감. PrivateLink 엔드포인트 3종(데이터 플레인 `bedrock-agentcore`, 컨트롤 플레인 `bedrock-agentcore-control`, `bedrock-agentcore.gateway`)이 Runtime · Memory · Tools · Identity · Gateway · Evaluations · Policy 지원. 엔드포인트 정책은 IAM 주체로만 제한 가능, OAuth 호출을 통과시키려면 Principal을 `*`로 둬야 함 |
| 적용 상황 | 인터넷 없이 사내 DB · API에 에이전트를 붙이거나 에이전트 API 호출을 사설 경로로 제한할 때 |
| 구성 요소 | ENI, 보안 그룹, 서비스 연결 역할, 인터페이스 엔드포인트, 필요한 VPC 엔드포인트(ECR dkr · api, S3 gateway, CloudWatch Logs) |
| 전제 조건 | 지원 AZ의 사설 서브넷. 인터넷 없는 VPC면 ECR · S3 · Logs 엔드포인트 필요 |
| 걸리는 평가 축 | 커스터마이징 — 네트워크(VPC) / 데이터 정책 — 반출 경로 통제 / 효율 — 관리할 구성요소 수(엔드포인트 · NAT) |

### 근거 8 — 데이터 보호와 교차 리전 추론: 저장은 원 리전, 추론은 다른 리전으로 갈 수 있음

| 항목 | 내용 |
|---|---|
| 출처 | Data protection in AgentCore · Cross-region inference in AgentCore Memory, Policy, Evaluations · AgentCore Developer Guide · https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/data-protection.html · https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/cross-region-inference.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — Gateway 데이터는 DynamoDB · S3에 서비스 키 또는 고객 관리형 KMS 키로 암호화 저장. Gateway는 고객 콘텐츠를 서비스 제공 · 유지에 쓰지 않는다고 명시. TLS 1.2 이상 필수. Memory · Policy · Evaluations는 교차 리전 추론을 써서, 저장은 원 리전에 남지만 입력 · 출력이 같은 지리권의 다른 리전(APAC: 도쿄 · 서울 · 뭄바이 · 싱가포르 · 시드니 등)으로 이동 가능. 서울발 Evaluations는 전 세계 상용 리전으로 라우팅되는 글로벌 교차 리전 추론 대상. CloudWatch · CloudTrail 로그에 추론 리전이 남지 않음. Memory는 built-in with overrides 전략, Evaluations는 커스텀 평가기로 교차 리전 추론을 피할 수 있음 |
| 적용 상황 | 처리 위치(국외 이전) 요건이 있는 데이터를 에이전트 메모리 · 평가에 넣을 때 |
| 구성 요소 | KMS, DynamoDB / S3(Gateway 메타데이터), 교차 리전 추론 프로파일 |
| 전제 조건 | 처리 위치를 고정하려면 교차 리전 추론을 피하는 옵션 선택 |
| 걸리는 평가 축 | 데이터 정책 — 처리 위치 · 반출 경로, 접근 통제(암호화) |

### 근거 9 — 고객 사례: KTern.AI(SAP 전환) 6개 구성요소로 프로덕션 운영

| 항목 | 내용 |
|---|---|
| 출처 | How KTern.AI built agentic AI for SAP on Amazon Bedrock AgentCore · AWS Machine Learning Blog · https://aws.amazon.com/blogs/machine-learning/how-ktern-ai-built-agentic-ai-for-sap-on-amazon-bedrock-agentcore/ |
| 날짜 | 발행 2026-07-10 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | B(사업자 선정 사례) — Runtime(멀티테넌트 세션 격리) · Memory · Gateway(MCP 계층으로 SAP API · ERP 연결) · Identity · Observability · Evaluations를 Strands Agents SDK와 함께 프로덕션 운영. 성과 수치(인프라 비용 약 70% 절감, 가동률 99.8% 등)는 회사 자체 측정이라 D로 보고 쓰지 않음 |
| 적용 상황 | 기업 업무 시스템(ERP)을 MCP 게이트웨이로 에이전트에 연결하는 운영 사례 |
| 구성 요소 | Runtime, Memory, Gateway, Identity, Observability, Evaluations, Bedrock 모델 |
| 전제 조건 | Strands 기반 멀티 에이전트 패턴, 설정 기반 도구 등록 |
| 걸리는 평가 축 | 동향 적합성 — 운영 사례 / AI 인프라 적합성 — 작업 호출(MCP 경유) |

### 근거 10 — Runtime V2: 콜드스타트 단축, 실제 사용 메모리만 과금

| 항목 | 내용 |
|---|---|
| 출처 | The new AgentCore Runtime is now available in Amazon Bedrock AgentCore · AWS What's New · https://aws.amazon.com/about-aws/whats-new/2026/09/new-agentcore-runtime-generally-available/ |
| 날짜 | 발행 2026-09-18 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — 세션 메모리가 필요한 만큼 늘고 줄며 실제 사용량으로 과금. 스냅샷 복원으로 P75 콜드스타트가 200MB~2GB 이미지에서 1.9~2.0초(V1은 5.4~30초, AWS 자체 테스트). 서버리스 · scale-to-zero · 하드웨어 기반 세션 격리 유지. `platformVersion=V2`로 켬. 제공 리전 us-east-1/2, us-west-2, eu-west-1, ap-northeast-1 — 서울 없음. GA 표기 없음 |
| 적용 상황 | 대화형 에이전트의 첫 응답 지연과 메모리 비용을 줄일 때 |
| 구성 요소 | Runtime(V1 / V2 플랫폼 버전) |
| 전제 조건 | 지원 리전에서만 V2. 서울은 현재 V1만 |
| 걸리는 평가 축 | 효과 — 지연 · 처리량 / 비용 — 과금 단위 / 효율 — 업그레이드 부담(플랫폼 버전 전환) |

### 비어 있는 것

- 비용 — 운영 인력, 전환 비용, 서울 리전 단가
- 효과 — 작업 의존성 · 일정(스케줄 실행), 가용성 SLA 수치
- 효율 — 패치 · 업그레이드 책임 범위(V1 지원 종료 계획 포함)
- 동향 적합성 — 지원 종료 계획, 릴리스 · 커뮤니티 활동 수치, 공개 포맷 · 이관 경로(다른 실행 기반으로 옮기는 방법)
- 커스터마이징 — 멀티 계정 · Organizations 배치, 가드레일(SCP) 예외 필요 여부, 중앙 로깅 구성
- 데이터 정책 — 분류 · 민감정보 식별, 보존 · 삭제(Memory 보존 기간), 리니지 · 데이터 카탈로그 연결(Registry는 에이전트 · 도구 카탈로그일 뿐 데이터 리니지가 아님), CloudTrail 접근 기록 범위
- AI 인프라 적합성 — 지원 MCP 프로토콜 버전. MCP 지원 자체는 근거 5에서 확인(관리형 MCP 게이트웨이)

상한 때문에 넣지 못한 것: AWS Labs 「Amazon Bedrock AgentCore MCP Server」(관리용 오픈소스 — 날짜 미확인). Cox Automotive 사례는 발행일이 없어 D.

---

## Amazon Bedrock

모델 접근 + Knowledge Bases + Guardrails — AWS 관리형 모델 접근 · RAG · 안전 장치 층(AgentCore는 별도 선택지). 상태: Bedrock Managed Knowledge Base는 2026-06-17 GA(https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-managed-knowledge-base/ — 버지니아 · 오리건 · GovCloud(US-West) · 시드니 · 도쿄 · 더블린 · 프랑크푸르트 · 런던, 서울 없음). 지원 종료 예고 1건 — 2026-09-30부터 customer-managed KB에 Confluence · SharePoint · Salesforce · Web Crawler 커넥터 신규 생성 불가(근거 7). 모델 접근 · Guardrails 본체의 GA 명시 페이지는 열지 않음 〔미정〕.

### 근거 1 — 요금 체계: 온디맨드 · 배치 · 프로비저닝 · Guardrails · 관리형 KB

| 항목 | 내용 |
|---|---|
| 출처 | Amazon Bedrock Pricing · AWS · https://aws.amazon.com/bedrock/pricing/ |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 (개별 단가에 "2025-12-01부터 적용" 같은 적용일 표기) |
| 등급 | A — 온디맨드는 모델 · 리전별 1M 토큰당 입출력 단가(Flex −50%, Priority +75%). 배치는 일부 모델 −50%. Provisioned Throughput은 모델 유닛 × 시간, 약정 없음 · 1개월 · 6개월. Guardrails는 필터마다 1,000 텍스트 유닛(유닛당 최대 1,000자)당 과금(예: 콘텐츠 필터 $0.15), 정규식 민감정보 필터 · 단어 필터는 무료. 관리형 KB는 인덱스 저장 $5/GB · 월, 표준 검색 $1/1,000회, 에이전틱 검색 $4/1,000회(기본 Retrieve $1/1,000회 별도), 관리형 모델로 하는 파싱 · 임베딩 · 리랭킹은 $0 |
| 적용 상황 | 호출량 비례 온디맨드와 처리량을 미리 확보하는 프로비저닝 중 고를 때 |
| 구성 요소 | 온디맨드 / 배치 / Provisioned Throughput / Guardrails 정책별 과금 / 관리형 KB 저장 · 검색 과금 |
| 전제 조건 | 모델 · 리전마다 단가가 다르고 일부 모델은 PT 영업 문의. customer-managed KB의 벡터 저장소 비용 〔미정〕 |
| 걸리는 평가 축 | 비용 — 과금 단위 · 단가, 인프라 사용료 / 효과 — 처리량(PT) |

### 근거 2 — 교차 리전 추론(CRIS)이 요청을 보내는 곳과 통제 수단

| 항목 | 내용 |
|---|---|
| 출처 | Route model inference requests across AWS Regions with cross-Region inference · AWS 문서 · https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — Geographic 프로파일은 US · EU · APAC 같은 지리 경계 안 상용 리전으로, Global 프로파일은 전 세계 상용 리전으로 보냄. Global은 약 10% 저렴, 라우팅 추가 요금 없음(호출 리전 단가 기준). 계정에서 켜지 않은 리전으로도 라우팅될 수 있음. 데이터는 AWS 네트워크 안에서만 이동, 리전 간 구간 암호화. CloudTrail은 원본 리전에 남고 `additionalEventData.inferenceRegion`에 실제 처리 리전 기록. SCP는 Geographic이면 목적지 리전 전부 허용, Global이면 `aws:RequestedRegion: unspecified` 허용 필요. 추론 프로파일로는 PT 불가 |
| 적용 상황 | 단일 리전 처리량 한도를 넘어야 하는데 처리 위치 제약은 지켜야 할 때 |
| 구성 요소 | 추론 프로파일(Geographic / Global), SCP 리전 조건, CloudTrail inferenceRegion 필드 |
| 전제 조건 | 조직 SCP가 목적지 리전을 허용해야 함. 처리 위치 요건이 있으면 Geographic |
| 걸리는 평가 축 | 데이터 정책 — 반출 경로 통제 · 처리 위치, 접근 기록 / 커스터마이징 — 가드레일 예외 필요 여부(SCP 리전 허용) / 효과 — 처리량 · 가용성 / 비용 — 단가 차이 |

### 근거 3 — 데이터 보존 모드(ZDR 포함)와 모델 제공자 공유 여부

| 항목 | 내용 |
|---|---|
| 출처 | Data retention · AWS 문서 · https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — 보존은 리전마다 계정 · 프로젝트 단위로 정하고 모드는 none(ZDR) < default < aws_review < provider_data_share(레거시). 현재는 어느 모드에서도 내용을 모델 제공자와 공유하지 않음. 인적 검토가 필요한 모델은 aws_review 이상이어야 호출 가능하고 이때 AWS 경계 안에 최대 30일 보존. CRIS를 쓰면 보존 데이터는 처리된 목적지 리전에 저장. SCP 조건 키 `bedrock:DataRetentionMode` · `bedrock-mantle:DataRetentionMode`로 조직 전체에 none 강제 가능. 출시 시점엔 콘솔 UI 없이 API로만 설정 |
| 적용 상황 | 프롬프트 · 응답 보존 금지나 보존 기간을 조직 정책으로 강제할 때 |
| 구성 요소 | 계정 / 프로젝트 보존 모드, 모델별 allowed_modes, SCP 조건 키 |
| 전제 조건 | 모델마다 최소 모드가 달라 none을 강제하면 일부 모델은 못 씀 |
| 걸리는 평가 축 | 데이터 정책 — 보존 · 삭제, 반출 경로 통제 · 처리 위치 / 커스터마이징 — 가드레일(SCP) 연동 |

### 근거 4 — Guardrails 민감정보(PII) 필터: 범위와 한계

| 항목 | 내용 |
|---|---|
| 출처 | Remove PII from conversations by using sensitive information filters · AWS 문서 · https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — ML 기반 문맥 탐지로 내장 PII 유형(일반 · 금융 · IT · 미국 · 캐나다 · 영국)과 사용자 정의 정규식(lookaround 미지원)을 입력 · 출력 각각에서 Block / Mask / Detect. 한계: 도구 호출 인자 · 도구 결과 · 도구 정의 안의 PII는 검사하지 않음. 모델 호출 로그 input 필드와 Guardrails trace match 필드에 원문이 남음(CloudWatch 로그 데이터 보호로 따로 가려야 함). 고객 관리형 KMS 키 · 태그 지원. 한국 고유 식별자 유형은 목록에 없음, 지원 언어 〔미정〕 |
| 적용 상황 | 프롬프트 · 응답에서 개인정보를 막거나 가려야 하는 RAG · 상담 앱 |
| 구성 요소 | Guardrail(piiEntitiesConfig, regexesConfig), KMS 키 |
| 전제 조건 | 한국 식별자는 정규식으로 직접 정의. 에이전트 · 도구 호출 경로와 로그는 따로 막아야 함 |
| 걸리는 평가 축 | 데이터 정책 — 분류 · 민감정보 식별 / 커스터마이징 — 태깅 / AI 인프라 적합성 — 도구 호출 경로의 PII 미검사 |

### 근거 5 — Managed KB와 Customer-managed KB의 운영 분담

| 항목 | 내용 |
|---|---|
| 출처 | Build a managed knowledge base · AWS 문서 · https://docs.aws.amazon.com/bedrock/latest/userguide/kb-build-managed.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 (GA 2026-06-17) |
| 등급 | A — Managed KB는 수집 · 저장 · 인덱싱 · 검색 인프라를 Bedrock이 맡고, 관리형 임베딩 · 리랭커를 추가 요금 없이 제공, 에이전틱 검색 지원. 네이티브 커넥터 7개(S3 · SharePoint · Confluence · Web Crawler · Google Drive · OneDrive · Custom), AgentCore Gateway 연동. Customer-managed KB는 벡터 DB를 고객이 고르고 운영, 커넥터는 S3 · Custom. ACL 인식 · 교차 계정 리소스 정책 · 관측성 하위 문서 있음 |
| 적용 상황 | 벡터 DB 없이 사내 문서 원천을 RAG로 연결(Managed) / 벡터 DB를 직접 통제(Customer-managed) |
| 구성 요소 | Managed KB 또는 Customer-managed KB + 고객 벡터 DB |
| 전제 조건 | Managed KB 지원 리전 · 쿼터 안에서만. 사용자 정의 임베딩은 float32 · 1024차원만 |
| 걸리는 평가 축 | 효율 — 관리할 구성요소 수, 관리형 / 직접 운영 비중 / 효과 — 원천 · 대상 연결 / AI 인프라 적합성 — 데이터 읽기 인터페이스(에이전틱 검색, Gateway 연동) / 데이터 정책 — 접근 통제(ACL 인식) |

### 근거 6 — Customer-managed KB의 벡터 저장소 선택지와 네트워크 · 계정 제약

| 항목 | 내용 |
|---|---|
| 출처 | Prerequisites for using a vector store you created for a knowledge base · AWS 문서 · https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — 지원 벡터 저장소: OpenSearch Serverless, OpenSearch Managed Cluster, S3 Vectors, Aurora PostgreSQL, Neptune Analytics(GraphRAG), Pinecone, Redis Enterprise Cloud, MongoDB Atlas. OpenSearch Serverless는 VPC 엔드포인트로 비공개 구성 가능, OpenSearch Managed는 VPC 뒤 도메인 미지원이라 공개 접근 필요. Aurora는 KB와 같은 계정이어야 함. 타사 저장소는 Secrets Manager로 자격 증명 전달, MongoDB Atlas는 PrivateLink 선택 가능. 바이너리 벡터는 OpenSearch만, S3 Vectors는 float만 |
| 적용 상황 | 기존 벡터 DB나 네트워크 격리 요건에 맞춰 저장소를 고를 때 |
| 구성 요소 | 벡터 저장소, 필드 매핑, Secrets Manager, KMS |
| 전제 조건 | 저장소별 인덱스 · 필드를 미리 만들고 임베딩 차원을 맞춤 |
| 걸리는 평가 축 | 커스터마이징 — 네트워크(VPC · PrivateLink), 계정 배치 / 동향 적합성 — 종속성(저장소 선택 폭) / 효율 — 직접 운영 비중 |

### 근거 7 — Customer-managed KB 일부 커넥터 신규 생성 중단

| 항목 | 내용 |
|---|---|
| 출처 | Connect a data source to your knowledge base · AWS 문서 · https://docs.aws.amazon.com/bedrock/latest/userguide/data-source-connectors.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 (공지 적용일 2026-09-30) |
| 등급 | A — 2026-09-30부터 customer-managed KB에 Confluence · SharePoint · Salesforce · Web Crawler 커넥터 신규 생성 불가. 기존 커넥터 수집 · 검색은 계속 동작, 이런 원천은 Managed KB 권장. 쿼리 엔진을 거쳐 정형 데이터 저장소에도 연결 가능. 멀티모달은 S3 · Custom 원천만. dataDeletionPolicy(RETAIN / DELETE)와 동기화 중 임시 데이터 KMS 암호화 설정 |
| 적용 상황 | 사내 SaaS 문서를 원천으로 KB를 새로 설계할 때 |
| 구성 요소 | CreateDataSource, 삭제 정책, KMS |
| 전제 조건 | 2026-09-30 이후 SaaS 원천을 새로 붙이려면 Managed KB |
| 걸리는 평가 축 | 동향 적합성 — 지원 종료 계획, 로드맵 방향(관리형으로 이동) / 효과 — 원천 연결 / 데이터 정책 — 보존 · 삭제(임베딩 삭제 정책) / 비용 — 전환 비용 |

### 근거 8 — CloudTrail 기록 범위: 관리 이벤트와 데이터 이벤트

| 항목 | 내용 |
|---|---|
| 출처 | Monitor Amazon Bedrock API calls using CloudTrail · AWS 문서 · https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — InvokeModel · Converse(스트림 포함)는 관리 이벤트로 기본 기록. KB의 Retrieve · RetrieveAndGenerate와 ApplyGuardrail(조직 강제 가드레일 평가 포함)은 데이터 이벤트라 고급 이벤트 선택기로 따로 켜야 하고 추가 요금. 여러 가드레일이 평가하면 assessments가 어느 가드레일 것인지 구분되지 않음. 스트리밍 완료 이벤트가 토큰 수와 inferenceRegion 기록. GuardDuty가 가드레일 제거 같은 의심 활동 분석 |
| 적용 상황 | 모델 · KB · 가드레일 호출을 중앙 감사 로그에 남길 때 |
| 구성 요소 | CloudTrail 트레일(관리 + 데이터 이벤트 선택기), S3 전달, GuardDuty |
| 전제 조건 | KB · 가드레일 호출까지 남기려면 데이터 이벤트를 켜고 비용 부담 |
| 걸리는 평가 축 | 효율 — 기존 모니터링 · 로깅 · 감사 연결 / 데이터 정책 — 접근 기록 / 커스터마이징 — 중앙 로깅 / 비용 — 데이터 이벤트 추가 요금 |

### 근거 9 — MCP 지원 방식: Responses API의 서버 측 도구(MCP)

| 항목 | 내용 |
|---|---|
| 출처 | Server-side tool use · AWS 문서 · https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use-server-side.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — **MCP 지원 방식: Bedrock이 MCP 클라이언트(공식 기능).** Responses API의 `type: "mcp"` 도구에 connector_id로 MCP를 구현한 Lambda ARN이나 AgentCore Gateway ARN을 넣으면 Bedrock이 tools/list로 찾고 tools/call로 실행. 호출 앱과 같은 IAM 정책을 쓰고 Gateway는 IAM 인증만. require_approval은 "never"만. 문서상 GPT OSS 20B / 120B부터 지원, 다른 모델은 "곧 지원". 도구 정의 가져오기와 도구 호출 토큰만 과금 |
| 적용 상황 | 모델이 사내 도구 · 데이터 API를 서버 측에서 호출하게 할 때 |
| 구성 요소 | Responses API(bedrock-mantle 엔드포인트), MCP 구현 Lambda 또는 AgentCore Gateway, IAM |
| 전제 조건 | Responses API 지원 모델, bedrock-mantle 경로 |
| 걸리는 평가 축 | AI 인프라 적합성 — 공개 표준 연계(MCP), 작업 호출 · 결과 수신, 권한 전파(IAM 동일 정책) / 비용 — 도구 호출 과금 |

### 근거 10 — 운영 사례: Ring의 다국어 고객지원 RAG

| 항목 | 내용 |
|---|---|
| 출처 | How Ring scales global customer support with Amazon Bedrock Knowledge Bases · AWS Machine Learning Blog(AWS 1명, Ring 2명) · https://aws.amazon.com/blogs/machine-learning/how-ring-scales-global-customer-support-with-amazon-bedrock-knowledge-bases/ |
| 날짜 | 발행 2026-03-30 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | B(사업자 선정 사례, Ring은 Amazon 자회사) — KB + OpenSearch Serverless + Titan Embeddings로 10개 리전 다국어 지원 챗봇 운영. 버전마다 KB를 따로 만들고 Step Functions로 매일 평가 · 승격, 롤백용 버전은 30일 보관. Guardrails 사용 언급 없음. "로케일 추가 비용 21% 감소"는 회사 자체 수치라 쓰지 않음 |
| 적용 상황 | 자주 바뀌는 지원 문서를 다국어 · 다리전 RAG로 서비스할 때 |
| 구성 요소 | Bedrock KB, OpenSearch Serverless, S3, Lambda, Step Functions, LLM-as-a-judge 평가 |
| 전제 조건 | S3 적재 파이프라인, 로케일 메타데이터 필터, 자동 평가 체계 |
| 걸리는 평가 축 | 동향 적합성 — 운영 사례 / 효과 — 작업 의존성 · 일정(일일 평가 · 승격) / 데이터 정책 — 보존(30일 버전 보관) |

### 비어 있는 것

- 동향 적합성 — 모델 접근 · Guardrails 본체의 GA 명시 근거
- 효과 — 런타임 지연 · 가용성 SLA 수치
- 효율 — 업그레이드 · 패치 부담(모델 버전 수명 주기 · 지원 종료 정책)
- 커스터마이징 — 중앙 ID · SSO 연동(IAM Identity Center 연결 방식), 엔드포인트별 PrivateLink 지원 목록
- 데이터 정책 — 리니지 · 카탈로그 연결, Guardrails PII 필터의 한국어 지원 · 한국 식별자 내장 여부
- AI 인프라 적합성 — 메타데이터 · 스키마 노출 방식

상한 때문에 넣지 못한 것(열어 본 페이지): 학습 미사용 · 인증 목록(https://aws.amazon.com/bedrock/security-compliance/), 모델 제공자 접근 차단(https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html), PrivateLink(https://docs.aws.amazon.com/bedrock/latest/userguide/usingVPC.html), Guardrails 조직 단위 중앙 강제 · ApplyGuardrail로 Bedrock 밖 모델에도 적용(https://aws.amazon.com/bedrock/guardrails/), AWS Labs KB 조회 MCP 서버(https://awslabs.github.io/mcp/servers/bedrock-kb-retrieval-mcp-server). Cox Automotive 사례는 발행일이 없어 D.

---

## LangGraph

오픈소스 프레임워크 + LangChain사 관리형(LangSmith Deployment). 종류: 직접 운영(OSS 프레임워크 · Standalone Agent Server) · 타사 관리형(LangSmith Deployment Cloud, Hybrid · Self-Hosted는 Enterprise). 상태: OSS GA — langgraph 1.0.0 2025-10-17, 분류자 "5 - Production/Stable"(https://pypi.org/project/langgraph/#history). LangSmith Deployment는 GA 표기를 찾지 못해 〔미정〕. MCP 클라이언트 `langchain.mcp`는 베타(근거 6). 이름 변경: 요금 · 문서는 "LangGraph Platform" 대신 "LangSmith Deployment", 서버 런타임은 "Agent Server".

### 근거 1 — OSS 라이선스 · 릴리스 주기 · 커뮤니티 규모

| 항목 | 내용 |
|---|---|
| 출처 | langchain-ai/langgraph 저장소 · Releases · GitHub · https://github.com/langchain-ai/langgraph · https://github.com/langchain-ai/langgraph/releases |
| 날짜 | 최신 릴리스 langgraph 1.2.14 2026-10-06(연도는 PyPI 이력으로 대조), langgraph-cli 0.4.33 2026-10-07 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — MIT 라이선스. 스타 43.0k, 포크 7.3k(저장소에서 직접 본 값). 2026-09-21~10-06 사이 패치 3건(1.2.12~1.2.14)과 sdk · cli 릴리스. 저장소의 사용사 소개 문구(Klarna · Replit · Elastic)는 날짜 없는 벤더 주장이라 D로 쓰지 않음 |
| 적용 상황 | 상태를 가진 장기 실행 에이전트를 저수준 그래프 오케스트레이션으로 직접 짤 때 |
| 구성 요소 | langgraph(코어), langgraph-sdk, langgraph-cli |
| 전제 조건 | Python / JS 런타임, 직접 운영 시 실행 인프라 |
| 걸리는 평가 축 | 동향 적합성 — 릴리스 · 커뮤니티 활동, 종속성(MIT 공개 코드) / 비용 — 프레임워크 라이선스료 없음 |

### 근거 2 — 요금 · 플랜별 배포 옵션 · 데이터 위치

| 항목 | 내용 |
|---|---|
| 출처 | Pricing · LangChain · https://www.langchain.com/pricing |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — Developer $0(1석, 기본 트레이스 5k/월), Plus $39/석/월(10k/월, Deployment 포함, 소형 서버리스 배포 1개 무료), Enterprise 별도 견적. 추가 배포는 LSU($1) 종량: 런타임 0.0675 LSU/vCPU-hr · 0.0090 LSU/GiB-hr, DB 0.177 LSU/vCPU-hr · 0.025 LSU/GiB-hr(가동 시간 기준은 DB가 살아 있는 시간). 트레이스 초과 단가 미표시. Hybrid · Self-Hosted는 Enterprise 전용. 데이터는 Cloud · Hybrid가 LangChain 클라우드(US 또는 EU), Self-Hosted가 고객 VPC. 커스텀 SSO · RBAC · ABAC는 Enterprise |
| 적용 상황 | 관리형 배포 · 관측 비용 추산, 셀프호스팅 필요 여부 판단 |
| 구성 요소 | LangSmith(관측 · 평가), LangSmith Deployment, Fleet, Engine |
| 전제 조건 | Hybrid · Self-Hosted는 Enterprise 계약(연 선불) |
| 걸리는 평가 축 | 비용 — 과금 단위 · 단가 / 커스터마이징 — 중앙 ID · SSO(Enterprise) / 데이터 정책 — 처리 위치 |

### 근거 3 — 셀프호스팅 토폴로지 3종과 운영 부담

| 항목 | 내용 |
|---|---|
| 출처 | Self-hosted deployment overview · LangChain Docs · https://docs.langchain.com/langsmith/deploy-to-self-hosted-overview |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — ① 전체 셀프호스팅(컨트롤 플레인 · 데이터 플레인 · 관측 모두 고객망) ② Hybrid(LangChain이 컨트롤 플레인 호스팅, 고객 VPC가 Agent Server · DB 운영) ③ Standalone Server(Agent Server 컨테이너 + 고객 PostgreSQL · Redis, 컨트롤 플레인 없음 — 에어갭 적합). 셀프호스팅은 Enterprise 플랜과 라이선스 키 필요. 업그레이드 · 확장 · 백업 · CI/CD는 고객 몫. 메트릭은 Prometheus · Datadog으로 내보냄 |
| 적용 상황 | 데이터를 고객 VPC에 두거나 에어갭 환경에서 운영할 때 |
| 구성 요소 | Agent Server(API · 큐 워커), PostgreSQL, Redis, Kubernetes(Helm) 또는 Docker, 리스너 |
| 전제 조건 | Enterprise 계약, K8s 클러스터, 직접 운영할 DB |
| 걸리는 평가 축 | 효율 — 관리할 구성요소 수, 관리형 / 직접 운영 비중, 업그레이드 부담, 모니터링 연결 / 커스터마이징 — 네트워크(VPC) 배치 / 비용 — 운영 인력 |

### 근거 4 — 체크포인터 기반 지속 실행

| 항목 | 내용 |
|---|---|
| 출처 | Persistence · LangChain Docs(OSS LangGraph) · https://docs.langchain.com/oss/python/langgraph/persistence |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — 체크포인터가 스레드 단위 그래프 상태를 저장해 human-in-the-loop, time travel, 장애 내성을 받침. InMemory · SQLite는 개발용, Postgres(동기 · 비동기)는 운영 권장. Agent Server를 쓰면 체크포인팅을 서버가 자동 처리 |
| 적용 상황 | 오래 걸리는 에이전트 작업을 중단 후 재개하거나 사람 승인을 끼울 때 |
| 구성 요소 | 체크포인터(PostgresSaver 등), 스레드 |
| 전제 조건 | 운영 환경에서는 Postgres 같은 영속 저장소 |
| 걸리는 평가 축 | 효과 — 처리 방식, 작업 의존성, 가용성(장애 복구) |

### 근거 5 — 배포된 에이전트를 MCP 서버로 노출(/mcp)

| 항목 | 내용 |
|---|---|
| 출처 | MCP endpoint in Agent Server · LangChain Docs · https://docs.langchain.com/langsmith/server-mcp |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — **MCP 지원 방식(서버 측): 벤더 공식.** Agent Server가 `/mcp`로 배포된 에이전트를 MCP 도구로 노출. 전송은 Streamable HTTP. 인증은 LangGraph API와 동일, 커스텀 인증으로 사용자 범위 도구 가능. 세션 미지원(요청마다 무상태). `langgraph-api` 0.2.3 이상 필요, `disable_mcp`로 끔 |
| 적용 상황 | 다른 에이전트 · MCP 클라이언트가 이 에이전트를 도구로 호출할 때 |
| 구성 요소 | Agent Server, /mcp 엔드포인트 |
| 전제 조건 | Agent Server로 배포(LangSmith Deployment 또는 셀프호스팅) |
| 걸리는 평가 축 | AI 인프라 적합성 — 공개 표준 연계(MCP), 작업 호출 · 결과 수신 |

### 근거 6 — MCP 클라이언트는 `langchain.mcp`(베타)로 이관

| 항목 | 내용 |
|---|---|
| 출처 | MCP · LangChain Docs · https://docs.langchain.com/oss/python/langchain/mcp (보조 https://github.com/langchain-ai/langchain-mcp-adapters) |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — **MCP 지원 방식(클라이언트 측): 벤더 오픈소스, 베타.** `langchain[mcp]>=1.4.0`의 `langchain.mcp`(FastMCP 기반 MCPAdapter), API가 바뀔 수 있음. 전송 Streamable HTTP · stdio · 인프로세스. 인증 방식으로 bearer · OAuth 2.1 · 사용자별 서버 인증이 이름만 나옴. 이전 패키지 langchain-mcp-adapters(MIT)는 아카이브돼 유지보수 중단. 이 페이지에 LangGraph 직접 언급 없음 |
| 적용 상황 | LangGraph · LangChain 에이전트가 외부 MCP 서버 도구를 쓸 때 |
| 구성 요소 | langchain.mcp MCPAdapter, (구) MultiServerMCPClient |
| 전제 조건 | langchain 1.4.0 이상. 구 어댑터 코드는 이관 필요 |
| 걸리는 평가 축 | AI 인프라 적합성 — MCP 클라이언트 지원 방식, 데이터 읽기 인터페이스 / 동향 적합성 — 이관 경로(아카이브된 패키지) |

### 근거 7 — Agent Server 인증 · 리소스 단위 인가

| 항목 | 내용 |
|---|---|
| 출처 | Authentication & access control · LangChain Docs · https://docs.langchain.com/langsmith/auth |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — 기본 인증은 LangSmith API 키(`x-api-key`). 셀프호스팅은 기본 인증이 없어 직접 구현. `@auth.authenticate` 커스텀 인증은 모든 플랜, 외부 IdP(Auth0 · Okta 등) 토큰 검증 예시. `@auth.on`으로 전역 · 리소스(스레드 · 어시스턴트 · 크론) · 액션 단위 필터 또는 403 거부. 사용자 정보가 실행 설정으로 전달돼 사용자 범위 자격 증명으로 외부 호출 가능 |
| 적용 상황 | 멀티테넌트로 스레드를 격리하거나 에이전트가 사용자 대신 외부 시스템을 호출할 때 |
| 구성 요소 | Auth 핸들러, 외부 IdP |
| 전제 조건 | 인증 · 인가 코드를 직접 작성 |
| 걸리는 평가 축 | AI 인프라 적합성 — 권한 전파 / 데이터 정책 — 접근 통제 / 커스터마이징 — 중앙 ID 연동 |

### 근거 8 — 조직 · 워크스페이스 RBAC, SCIM · SSO 그룹 동기화, 감사 로그

| 항목 | 내용 |
|---|---|
| 출처 | Role-based access control · LangChain Docs · https://docs.langchain.com/langsmith/rbac |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — 조직 역할 4종(Admin · Operator · User · Viewer), 워크스페이스 역할 3종. 워크스페이스 RBAC · 커스텀 역할은 Enterprise. IdP가 SCIM 그룹 · SSO Groups Sync로 역할 자동 부여. 감사 로그는 Enterprise, 조직 Admin · Operator가 열람 |
| 적용 상황 | 중앙 IdP로 LangSmith 사용자와 권한을 관리할 때 |
| 구성 요소 | 조직 · 워크스페이스, SCIM, SSO |
| 전제 조건 | Enterprise 플랜(워크스페이스 RBAC · 감사 로그) |
| 걸리는 평가 축 | 커스터마이징 — 계정 · 조직 배치, 중앙 ID · SSO / 데이터 정책 — 접근 기록 |

### 근거 9 — 트레이스 보존 기간 · 삭제 API

| 항목 | 내용 |
|---|---|
| 출처 | Data purging for compliance · LangChain Docs · https://docs.langchain.com/langsmith/data-purging-compliance |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 (본문에 "SaaS 확장 보존 상한 180일, 2026-09-14 발효") |
| 등급 | A — 기본 보존 14일. 확장 보존은 SaaS 최대 180일, Enterprise는 30~180일 중 기본값 지정. 변경은 새 트레이스에만 적용. 삭제 API는 trace ID 기준(요청당 1,000건)과 메타데이터 기준, 주말에 비동기 처리되고 완료 확인 없음. 셀프호스팅은 180일 상한이 없지만 기간마다 blob 수명주기 규칙 필요 |
| 적용 상황 | 보존 · 삭제 규정을 맞춰야 할 때 |
| 구성 요소 | 트레이싱 프로젝트, 삭제 API, (셀프호스팅) blob 스토리지 |
| 전제 조건 | 워크스페이스 기본값 설정은 Enterprise |
| 걸리는 평가 축 | 데이터 정책 — 보존 · 삭제 |

### 근거 10 — 트레이스 입력 · 출력 마스킹(민감정보)

| 항목 | 내용 |
|---|---|
| 출처 | Mask inputs and outputs · LangChain Docs · https://docs.langchain.com/langsmith/mask-inputs-outputs |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — `LANGSMITH_HIDE_INPUTS` / `OUTPUTS` / `METADATA`로 통째로 숨김. 함수 단위 `hide_inputs` · `process_inputs`, 정규식 기반 anonymizer(API 키 · 토큰 패턴 내장), 요청 단위 `tracing_context`. 아예 남기지 않으려면 조건부 트레이싱. Presidio · Comprehend 연동은 예시일 뿐 검증이 필요하다고 명시 |
| 적용 상황 | 트레이스에 개인정보 · 비밀값이 남지 않게 할 때 |
| 구성 요소 | LangSmith SDK(Python 0.1.81+, TS 0.1.33+) |
| 전제 조건 | 앱 코드 · SDK 설정에서 적용(서버 측 자동 분류가 아님) |
| 걸리는 평가 축 | 데이터 정책 — 분류 · 민감정보 식별(SDK 측 마스킹), 반출 통제 |

### 비어 있는 것

- 동향 적합성 — LangGraph를 명시하고 날짜가 있는 최근 12개월 공개 기업 운영 사례 없음(customers 페이지는 날짜 없어 D, Rippling 사례 2026-06-01은 LangGraph 미언급). 지원 종료 계획 · 로드맵 공식 근거, LangSmith Deployment GA 표기
- 효과 — 처리량 · 지연 수치, 가용성 SLA(Enterprise "support SLA"만), 다른 프레임워크에서 옮기는 경로
- 비용 — 트레이스 초과 단가, 전환 비용
- 커스터마이징 — PrivateLink 등 사설 연결 지원 여부, 태깅 · 중앙 로깅 전송 방식(OTel 문서는 상한 때문에 빠짐)
- 데이터 정책 — 리니지 · 카탈로그 연결. **처리 리전 표기가 문서마다 다름**(요금 페이지는 US / EU, Hybrid · OTel 문서는 GCP US / EU / APAC · AWS US 엔드포인트) — 사람 확인 필요
- AI 인프라 적합성 — 메타데이터 · 스키마 노출. MCP는 확인(서버 /mcp 공식, 클라이언트 langchain.mcp 베타)

---

## LiteLLM 직접 운영

오픈소스 LLM 게이트웨이 · 프록시(여러 모델 제공사를 하나의 API로, 라우팅 · 키 관리 · 예산 · 로깅). 종류: 직접 운영 — MIT 코어를 자체 호스팅, Enterprise 기능은 같은 이미지에 라이선스 키로 켬(근거 1). 상태: 〔미정〕 — 안정판을 정기 릴리스(GitHub 'Latest' v1.104.2), "GA" 표기 · 지원 종료 예고는 공식 근거에서 찾지 못함.

### 근거 1 — 오픈소스와 Enterprise의 기능 경계, 라이선스, 가격 방식

| 항목 | 내용 |
|---|---|
| 출처 | Enterprise · LiteLLM 공식 문서 · https://docs.litellm.ai/docs/enterprise ; LICENSE · BerriAI 공식 GitHub · https://raw.githubusercontent.com/BerriAI/litellm/main/LICENSE |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — `enterprise/` 디렉터리만 별도 상용 라이선스, 나머지는 MIT. **OSS 포함:** 가상 키, 예산 · 레이트 리밋, 지출 추적, Admin UI, 로드밸런싱, MCP 게이트웨이, Presidio PII 마스킹, 커스텀 가드레일 프레임워크. **Enterprise 전용:** Admin UI SSO(6명 이상) · SCIM, JWT 인증, 보존 정책이 있는 감사 로그, RBAC(조직 · 팀 · 역할), IP ACL, 키 자동 로테이션, 시크릿 매니저 연동(AWS 등), 팀별 로깅, 키 · 팀별 가드레일, 멀티테넌트, 태그 기반 예산. SSO는 5명까지 무료. Enterprise 가격은 비공개 견적 · 30일 체험, 지원 대상은 최근 안정판 마이너 라인 4개 |
| 적용 상황 | 무료 OSS로 운영할지, 거버넌스 기능 때문에 Enterprise 라이선스를 살지 판단할 때 |
| 구성 요소 | OSS 코어, Enterprise 라이선스 키, 조달 경로(AWS · Azure Marketplace, 직접 인보이스) |
| 전제 조건 | 6명 이상 SSO, 감사 로그, 시크릿 매니저 연동이 필요하면 Enterprise 계약 |
| 걸리는 평가 축 | 비용 — 과금 단위 · 단가(OSS 0원, Enterprise 비공개) / 동향 적합성 — 종속성(MIT 코어), 지원 종료 계획(마이너 4개 라인) / 커스터마이징 — 중앙 ID · SSO 연동 / 데이터 정책 — 접근 기록(감사 로그는 Enterprise) |

### 근거 2 — 프록시 배포 구조

| 항목 | 내용 |
|---|---|
| 출처 | Deploy · LiteLLM 공식 문서 · https://docs.litellm.ai/docs/proxy/deploy |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — 프로덕션은 무상태 프록시 2개 이상, PostgreSQL(필수), Redis(인스턴스 2개 이상이면 필수), 마이그레이션 잡. `ghcr.io/berriai/litellm` 이미지, Helm 차트 2종(모놀리식 · 마이크로서비스), 공식 Terraform 모듈(AWS ECS Fargate, GCP Cloud Run), HPA · KEDA 오토스케일, 1,000 RPS 이상이면 Redis 트랜잭션 버퍼 권장. `LITELLM_SALT_KEY`는 모델 추가 후 바꿀 수 없음. Redis가 없으면 레이트 리밋 · 예산이 프로세스별로 따로 계산됨 |
| 적용 상황 | 직접 운영 시 관리 대상과 확장 방식을 정할 때 |
| 구성 요소 | 프록시 컨테이너, Postgres, Redis, 마이그레이션 잡, `/health/readiness` |
| 전제 조건 | 이미지 태그 고정, 비밀값은 클라우드 시크릿 매니저, 레플리카 × 커넥션 풀(기본 10)에 맞춘 Postgres 연결 한도 |
| 걸리는 평가 축 | 효율 — 관리할 구성요소 수, 직접 운영 비중, 업그레이드 부담(스키마 마이그레이션) / 효과 — 가용성 · 처리량(레플리카 · 오토스케일) / 비용 — 인프라 사용료(구성 요소 종류만, 금액 없음) |

### 근거 3 — 가상 키로 하는 접근 · 예산 통제

| 항목 | 내용 |
|---|---|
| 출처 | Virtual Keys · LiteLLM 공식 문서 · https://docs.litellm.ai/docs/proxy/virtual_keys |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — 키 단위로 호출 가능 모델, 예산(`max_budget` · 기간), TPM · RPM · 동시 요청 수, 만료, 차단. 지출은 키 · 사용자 · 팀별 기록. 예약 로테이션은 Enterprise |
| 적용 상황 | 여러 팀 · 앱이 하나의 게이트웨이로 모델을 쓸 때 팀별 권한 · 비용 분리 |
| 구성 요소 | 마스터 키, 가상 키, user_id · team_id 계층, 모델 별칭, `allowed_routes` |
| 전제 조건 | Postgres와 마스터 키. 키 한도를 안 정하면 소유자 한도를 물려받음 |
| 걸리는 평가 축 | 데이터 정책 — 접근 통제(모델 허용 목록 · 키 차단) / 커스터마이징 — 계정 · 조직 배치(팀 · 사용자 계층) / 비용 — 팀별 예산 통제 |

### 근거 4 — 로깅 · 관측 연결과 프롬프트 비저장 옵션

| 항목 | 내용 |
|---|---|
| 출처 | Logging · LiteLLM 공식 문서 · https://docs.litellm.ai/docs/proxy/logging |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — OpenTelemetry, Langfuse, Datadog, S3, SQS, DynamoDB 등으로 로그 전송. `turn_off_message_logging`이면 프롬프트 · 응답은 빼고 메타데이터(지출 등)만 남김. 요청 단위 redaction, 키 식별정보 redaction, `no-log` 파라미터(전역 차단 가능) |
| 적용 상황 | 게이트웨이 로그를 중앙 로깅 · 관측에 붙이면서 민감한 본문은 저장하지 않을 때 |
| 구성 요소 | 콜백(otel · langfuse · s3_v2 · sqs · datadog 등), `generic_api` 커스텀 엔드포인트 |
| 전제 조건 | 수신처(OTel 수집기, S3 버킷 등) 별도 준비. CloudWatch는 이 페이지에 직접 나오지 않음 |
| 걸리는 평가 축 | 효율 — 기존 모니터링 · 로깅 연결 / 커스터마이징 — 중앙 로깅 / 데이터 정책 — 보존(본문 비저장 선택), 접근 기록(메타데이터) |

### 근거 5 — Amazon Bedrock 연동(인증 · 리전 · 가드레일)

| 항목 | 내용 |
|---|---|
| 출처 | AWS Bedrock (Providers) · LiteLLM 공식 문서 · https://docs.litellm.ai/docs/providers/bedrock |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — boto3 자격증명 체인, 프로필(SSO 로그인 포함), STS AssumeRole(`aws_role_name`), IAM Roles Anywhere, Bedrock API 키. 교차 리전 추론 프로필(`us.` · `global.`), Converse · Invoke 경로, Bedrock Guardrails(`guardrailConfig`) 전달 |
| 적용 상황 | 게이트웨이 뒤에 Bedrock을 두고 다른 계정의 Bedrock을 역할 위임으로 부르는 구조 |
| 구성 요소 | `aws_region_name`, `aws_role_name` · `aws_session_name`, `aws_bedrock_runtime_endpoint`, guardrailConfig |
| 전제 조건 | `sts:AssumeRole` 권한과 대상 역할 신뢰 정책, Bedrock 모델 접근 활성화. PrivateLink · VPC 엔드포인트는 페이지에 없음(커스텀 엔드포인트 설정만) |
| 걸리는 평가 축 | 효과 — 원천 · 대상 연결 / 커스터마이징 — 계정 배치(교차 계정 AssumeRole), 네트워크 / 데이터 정책 — 처리 위치(리전 지정 · 교차 리전 프로필) |

### 근거 6 — MCP 게이트웨이(공식 기능, OSS 포함)

| 항목 | 내용 |
|---|---|
| 출처 | MCP Overview · LiteLLM 공식 문서 · https://docs.litellm.ai/docs/mcp |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — **MCP 지원 방식: MCP 게이트웨이(OSS 포함).** 고정 엔드포인트 하나로 여러 MCP 서버의 도구를 노출하고 키 · 팀 · 조직 단위로 접근 통제. 전송 Streamable HTTP · SSE · stdio(기본 꺼짐). 도구 이름에 서버명 접두어. LLM 없이 쓰는 REST 경로(`/mcp-rest/tools/list` · `/call`), `x-litellm-end-user-id`로 최종 사용자 권한 · 예산 적용. 업스트림 인증은 API 키 · bearer · OAuth2 · 토큰 교환 · 패스스루 · AWS SigV4 |
| 적용 상황 | 에이전트가 여러 MCP 서버를 한곳에서 권한을 통제받으며 쓰게 할 때 |
| 구성 요소 | MCP 게이트웨이 엔드포인트, 서버별 권한 설정 |
| 전제 조건 | 클라이언트는 LiteLLM 키로 인증, 서버별 권한(`allow_all_keys` 또는 키 · 팀 지정) 설정 |
| 걸리는 평가 축 | AI 인프라 적합성 — 공개 표준 연계(MCP 게이트웨이), 작업 호출 · 결과 수신, 권한 전파(최종 사용자 헤더) |

### 근거 7 — AWS 공식 레퍼런스 아키텍처(LiteLLM 기반 멀티 제공사 게이트웨이)

| 항목 | 내용 |
|---|---|
| 출처 | Guidance for Multi-Provider Generative AI Gateway on AWS · AWS Solutions Library · https://docs.aws.amazon.com/solutions/multi-provider-generative-ai-gateway-on-aws/ ; Streamline AI operations with the Multi-Provider Generative AI Gateway reference architecture · AWS Machine Learning Blog · https://aws.amazon.com/blogs/machine-learning/streamline-ai-operations-with-the-multi-provider-generative-ai-gateway-reference-architecture |
| 날짜 | Guidance는 상시 갱신 — 확인 2026-10-11 기준 / 블로그 발행 2025-11-21 · 오래됨 아님 |
| 등급 | A — AWS가 LiteLLM을 ECS Fargate나 EKS에 올리는 공식 레퍼런스(CloudFormation · CDK 샘플 코드) 제공. API / 미들웨어 계층이 "LiteLLM 오픈소스가 지원하지 않는 기능"을 Bedrock 네이티브 연동으로 보완한다고 명시. 네트워크는 글로벌 공개 / 리전 ALB 직결 / 프라이빗 VPC 전용 중 선택, 사설 연결은 VPN · Direct Connect · VPC 피어링 · Transit Gateway |
| 적용 상황 | AWS 계정 안에 LiteLLM 게이트웨이를 직접 운영하는 표준 구성 |
| 구성 요소 | Route 53 · CloudFront, AWS WAF, ALB(ACM), ECS Fargate · EKS, ECR, RDS, ElastiCache Redis, Secrets Manager, S3(로그), CloudWatch, 선택적 Langfuse |
| 전제 조건 | Bedrock 모델 접근 활성화, 외부 제공사 자격증명은 Secrets Manager. 멀티 계정 배치 패턴은 다루지 않음 |
| 걸리는 평가 축 | 커스터마이징 — 네트워크(VPC 전용 배치 · 사설 연결) / 효율 — 관리형 / 직접 운영 비중, 기존 모니터링 연결(CloudWatch) / 동향 적합성 — 운영 사례(사업자 공식 레퍼런스) |

### 근거 8 — 에이전트용 신원 기반 접근 · 권한 전파 · 지출 통제

| 항목 | 내용 |
|---|---|
| 출처 | Secure shared AI agents with identity-aware access and spend controls · LiteLLM 공식 블로그 · https://docs.litellm.ai/blog/ai-gateway-identity-and-finops |
| 날짜 | 발행 2026-09-08 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — Agent Gateway가 OIDC 등으로 호출자를 인증하고 사용자 · 팀을 확인한 뒤 팀 권한으로 접근 가능한 에이전트 · MCP 서버를 제한. 사용자 · 팀 ID는 헤더(`X-LiteLLM-User-Id` · `Team-Id`)로 에이전트에 전달. MCP는 사용자별 OAuth(authorization code + PKCE), 예산 초과 시 제공사 호출 전에 429. OSS / Enterprise 구분은 글에 없음 〔미정〕 |
| 적용 상황 | 여러 사용자가 공유하는 에이전트가 사용자 권한 범위 안에서만 도구 · 모델을 쓰게 할 때 |
| 구성 요소 | Agent Gateway, 팀 오브젝트 권한, 사용자별 MCP 자격증명 저장, 키 · 팀 · 에이전트 · 고객 단위 예산, End User 필터 로그 |
| 전제 조건 | OIDC 등 IdP 연동. 최종 인가는 업스트림 MCP 서버가 판단 |
| 걸리는 평가 축 | AI 인프라 적합성 — 권한 전파, 작업 호출 · 결과 수신 / 데이터 정책 — 접근 통제 · 접근 기록 / 커스터마이징 — 중앙 ID 연동 |

### 근거 9 — 보안 사고 · 취약점 공지(공급망 침해, CVE)

| 항목 | 내용 |
|---|---|
| 출처 | Security Update: Suspected Supply Chain Incident · https://docs.litellm.ai/blog/security-update-march-2026 ; Security Update: CVE-2026-42208 in LiteLLM Proxy · https://docs.litellm.ai/blog/cve-2026-42208-litellm-proxy-sql-injection ; September Townhall Updates · https://docs.litellm.ai/blog/september-townhall-updates (모두 LiteLLM 공식 블로그) |
| 날짜 | 발행 2026-03-24(갱신 2026-03-27) · 2026-04-29 · 2026-09-24 · 확인 2026-10-11 · 모두 오래됨 아님 |
| 등급 | A — 2026-03-24 PyPI 배포본 1.82.7 · 1.82.8이 침해돼 자격증명을 빼내는 코드가 들어감(CI의 Trivy 경유 추정). 공식 Docker 이미지는 영향 없었고 정상판 v1.83.0을 새 CI/CD로 배포. 노출 시간은 글 안에서 약 40분과 10:39~16:00 UTC로 엇갈림. CVE-2026-42208은 인증 없이 Authorization 헤더로 들어오는 SQL 인젝션, 영향 v1.81.16~v1.83.6, v1.83.7에서 수정. 9월 한 달 보안 수정 52건, 마스터 키가 없거나 기본값이면 기동 거부로 변경 |
| 적용 상황 | 직접 운영 시 패치 주기와 공급망 위험을 따질 때 |
| 구성 요소 | 공식 보안 공지 채널, cosign 이미지 서명, 비공개 취약점 신고, 버그 바운티 |
| 전제 조건 | 이미지 태그 고정 · 서명 검증, 보안 공지 상시 확인과 빠른 패치, 침해 의심 시 자격증명 전면 교체 |
| 걸리는 평가 축 | 효율 — 업그레이드 · 패치 부담 / 동향 적합성 — 운영 성숙도(보안 대응 이력) / 데이터 정책 — 반출 경로 통제(공급망 침해 시 자격증명 유출) |

### 근거 10 — 릴리스 체계 · 커뮤니티 규모 · 로드맵

| 항목 | 내용 |
|---|---|
| 출처 | Releases · https://github.com/BerriAI/litellm/releases ; 저장소 · https://github.com/BerriAI/litellm ; May Townhall Updates · LiteLLM 공식 블로그 · https://docs.litellm.ai/blog/may-townhall-updates |
| 날짜 | 저장소 · 릴리스는 상시 갱신 — 확인 2026-10-11 기준 / 블로그 발행 2026-05-26 · 오래됨 아님 |
| 등급 | A — Stars 60.9k, Forks 12.2k, 커밋 54,205건(저장소에서 직접 확인). 최신 v1.104.2, `stable/1.104.x` · `stable/1.102.x` 브랜치와 `-rc` · `-dev` 프리릴리스 분리. v1.84.0부터 SemVer, 안정판 마이너를 매주 올림. 5월 시점 이전 릴리스 지원 기간은 "정의 예정". 로드맵은 에이전트 플랫폼(템플릿 · 스킬 · 프로젝트)과 Rust 전환(근거 9의 9월 글: 12/1 목표, 진척 5%) |
| 적용 상황 | 업그레이드 주기와 버전 고정 전략, 프로젝트 지속성 판단 |
| 구성 요소 | 주간 마이너 릴리스, stable · rc 브랜치, PR별 자동 보안 리뷰 |
| 전제 조건 | 주 단위 릴리스를 따라가며 검증 · 업그레이드할 절차 |
| 걸리는 평가 축 | 동향 적합성 — 릴리스 · 커뮤니티 활동, 로드맵 방향, 지원 종료 계획(OSS 지원 기간 미정) / 효율 — 업그레이드 부담 |

### 비어 있는 것

- 비용 — Enterprise 단가(비공개), 인프라 사용료 금액, 운영 인력 규모, 전환 비용
- 효과 — 처리량 · 지연 · 가용성의 공식 SLA, 기존 SDK · 직접 호출 코드를 게이트웨이로 옮기는 절차
- 커스터마이징 — 랜딩존 멀티 계정 안 배치 패턴, 가드레일(SCP) 예외 필요 여부, 태깅, Bedrock PrivateLink · VPC 엔드포인트
- 데이터 정책 — 민감정보 식별은 Presidio PII 마스킹이 OSS에 있다는 언급까지만(상세 미확인), 감사 로그 보존 · 삭제 방식(Enterprise), 리니지 · 카탈로그 연결
- AI 인프라 적합성 — 데이터 스키마 노출(MCP 도구 목록 노출까지만)
- 동향 적합성 — **날짜가 붙은 공개 기업 도입 사례(B) 없음.** 홈페이지 고객 추천사(Netflix · Lemonade · Okta · AT&T · NVIDIA)는 날짜가 없어 D. 지금 사례성 근거는 AWS 공식 레퍼런스(근거 7)뿐

---

## Vertex AI Agent Engine

현 명칭 **Agent Runtime on Gemini Enterprise Agent Platform**(2026-04-22 개명). GCP 관리형 에이전트 런타임 — 타사 비교용, Bedrock AgentCore 대응. 상태: GA — Vertex AI Agent Engine 시절 2025-03-04 GA(근거 3). 새 문서에는 Runtime의 GA를 다시 밝힌 문구가 없고, 하위 기능마다 단계가 다름(예: 리비전 · 트래픽 분할은 프리뷰, 근거 2).

### 근거 1 — 공식 명칭 변경표: Agent Engine → Agent Runtime

| 항목 | 내용 |
|---|---|
| 출처 | Gemini Enterprise Agent Platform name changes · Google Cloud 문서 · https://docs.cloud.google.com/gemini-enterprise-agent-platform/vertex-ai-name-changes |
| 날짜 | 갱신 2026-10-07 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — Vertex AI Agent Engine의 현재 공식 명칭은 "Agent Runtime on Gemini Enterprise Agent Platform". Sessions · Memory Bank · Code Execution 앞에도 "Gemini Enterprise Agent Platform"이 붙음 |
| 적용 상황 | 구 명칭으로 된 문서 · 견적 · 운영사 자료를 현재 명칭에 맞춰 대조할 때 |
| 구성 요소 | Agent Runtime, Agent Platform Sessions, Memory Bank, Code Execution |
| 전제 조건 | Vertex AI Platform이 Gemini Enterprise Agent Platform으로 편입된 상태 |
| 걸리는 평가 축 | 동향 적합성 — 로드맵 방향, 종속성(명칭 · 문서 경로 변경) |

### 근거 2 — Agent Platform 릴리스 노트

| 항목 | 내용 |
|---|---|
| 출처 | Gemini Enterprise Agent Platform release notes · Google Cloud 문서 · https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes |
| 날짜 | 항목별 2026-04-22 ~ 2026-09-30 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — 2026-04-22: Agent Engine → Agent Runtime 개명, 최대 7일 장기 실행, 1초 미만 콜드 스타트, 1분 이내 프로비저닝, 커스텀 컨테이너(BYOC). 같은 날 Agent Platform 원격 MCP 서버 GA, Agent Registry가 MCP 서버를 카탈로그화. 2026-05-19: 에이전트 리비전 · 트래픽 분할 공개 프리뷰. 2026-06-18: Agent Observability GA(새 ADK 에이전트는 OpenTelemetry 트레이싱 기본). 2026-06-17: Sessions · Memory Bank 멀티리전 · global 엔드포인트 GA(global은 CMEK 불가). 2026-09-01: Sessions · Memory Bank 사용량을 Agent Platform 컴퓨트 SKU로 계량, 임베딩 SKU 변경 |
| 적용 상황 | 장기 실행 에이전트, 컨테이너로 가져온 에이전트, 무중단 배포(트래픽 분할) |
| 구성 요소 | Agent Runtime, Sessions, Memory Bank, Agent Gateway, Agent Registry, Agent Identity, Agent Observability, 원격 MCP 서버 |
| 전제 조건 | 기능별 GA · 프리뷰 단계가 다름 |
| 걸리는 평가 축 | 동향 적합성 — GA 여부 · 릴리스 활동 / 효과 — 처리 방식(장기 실행) · 지연(콜드 스타트) / 비용 — 과금 단위 / 효율 — 모니터링 연결 / AI 인프라 적합성 — MCP(공식 원격 MCP 서버, Registry의 MCP 카탈로그) |

### 근거 3 — Vertex AI 릴리스 노트: Agent Engine GA, Sessions · Memory Bank GA, HIPAA, 문서 갱신 중단

| 항목 | 내용 |
|---|---|
| 출처 | Vertex AI release notes (Generative AI) · Google Cloud 문서 · https://docs.cloud.google.com/vertex-ai/generative-ai/docs/release-notes |
| 날짜 | 항목 2025-03-04(GA) · 2025-08-21(HIPAA) · 2025-12-16(Sessions · Memory Bank GA) · 확인 2026-10-11 · **GA · HIPAA 항목은 「오래됨」**(구조 근거로만), 2025-12-16 항목은 오래됨 아님 |
| 등급 | A — Agent Engine GA 2025-03-04(과금도 같은 날 시작). Sessions · Memory Bank GA 2025-12-16. HIPAA 워크로드 지원 2025-08-21. 페이지 상단에 Vertex AI 문서는 더 이상 갱신하지 않으며 Agent Platform 문서를 보라는 배너 |
| 적용 상황 | GA 이력과 운영 성숙도 확인, 구 문서를 근거로 쓸 수 있는지 판단 |
| 구성 요소 | Agent Engine Runtime, Sessions, Memory Bank |
| 전제 조건 | — |
| 걸리는 평가 축 | 동향 적합성 — GA 여부, 지원 종료 계획(구 문서 갱신 중단) / 데이터 정책 — 처리 위치 · 규제(HIPAA) |

### 근거 4 — Agent Runtime 개요: 지원 프레임워크 · 배포 방식 · 보안 · 관측

| 항목 | 내용 |
|---|---|
| 출처 | Agent Runtime · Google Cloud 문서 · https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime |
| 날짜 | 갱신 2026-10-07 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — 완전 관리형 런타임. ADK는 완전 통합(Python `adk`, Go `adkgo` CLI 배포). LangChain · LangGraph · AG2 · LlamaIndex는 SDK 통합, CrewAI와 기타는 커스텀 템플릿. A2A 멀티에이전트는 프리뷰. Artifact Registry 컨테이너 이미지나 Dockerfile로 배포. VPC-SC 준수, 인증 · IAM 설정. OpenTelemetry로 Cloud Trace. Agents CLI가 Terraform 프로비저닝과 Cloud Build CI/CD 제공. 무료 등급. MCP는 "MCP Toolbox for Databases와 함께 배포" 예제로만 언급 |
| 적용 상황 | 프레임워크 종속을 줄이면서 관리형 런타임에 에이전트를 올릴 때 |
| 구성 요소 | Agent Runtime, ADK / LangGraph 등, Artifact Registry, Cloud Build, Cloud Trace, Agents CLI(Terraform) |
| 전제 조건 | GCP 프로젝트, 배포 가능한 형태(템플릿 · 컨테이너)의 에이전트 |
| 걸리는 평가 축 | 효과 — 기존 작업 이관(다중 프레임워크 · 컨테이너) / 효율 — 관리형 비중, 모니터링 · 로깅 연결 / 동향 적합성 — 종속성 · 이관 경로(오픈 프레임워크, BYOC) / AI 인프라 적합성 — 작업 호출(함수 호출, A2A 프리뷰) |

### 근거 5 — 엔터프라이즈 보안 표(VPC-SC · CMEK · 데이터 상주), IAM, PSC-I, 관측

| 항목 | 내용 |
|---|---|
| 출처 | Gemini Enterprise Agent Platform: Scale your agents · Google Cloud 문서 · https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale |
| 날짜 | 갱신 2026-10-07 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — Agent Runtime 열에 VPC Service Controls, CMEK, 저장 데이터 상주, HIPAA, Access Transparency · Access Approval이 모두 "지원". 접근은 에이전트 ID · 서비스 계정 · API 키 · OAuth 클라이언트로 관리, Sessions · Memory Bank에 IAM Conditions. Private Service Connect 인터페이스로 고객 VPC 연결 · 인터넷 접근 관리. Agent Gateway가 런타임 트래픽 중계. Cloud Trace · Logging · Monitoring 연동. Memory Bank의 메모리 생성은 모델 엔드포인트의 리전 또는 멀티리전에서 처리 |
| 적용 상황 | 규제 환경에서 네트워크 경계 안에 에이전트를 배치할 때 |
| 구성 요소 | Agent Runtime, VPC-SC 경계, CMEK(Cloud KMS), PSC 인터페이스, IAM · 에이전트 ID, Agent Gateway, Cloud Logging · Monitoring · Trace |
| 전제 조건 | VPC-SC 경계, KMS 키, PSC 네트워크 구성 |
| 걸리는 평가 축 | 커스터마이징 — 네트워크(VPC · PSC-I), 중앙 로깅 / 데이터 정책 — 접근 통제(IAM Conditions), 접근 기록(Access Transparency), 반출 통제(VPC-SC), 처리 위치(데이터 상주) / 효율 — 기존 모니터링 · 로깅 · 감사 연결 / AI 인프라 적합성 — 권한 전파(에이전트 ID) |

### 근거 6 — 지원 리전: 서울 포함, 서울은 Gateway 제외, 엔드포인트별 CMEK 제약

| 항목 | 내용 |
|---|---|
| 출처 | Supported locations for agents · Google Cloud 문서 · https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/agent-locations |
| 날짜 | 갱신 2026-10-07 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — Runtime · Sessions · Memory Bank · Sandboxes(Code Execution)는 23개 리전. 서울(asia-northeast3) 포함, 단 서울에서는 Agent Gateway 미지원. 도쿄(asia-northeast1)는 제한 없음. 멀티리전(us · eu) 엔드포인트, Sessions · Memory Bank는 global 엔드포인트도 있음. CMEK는 Memory Bank · Sessions global 엔드포인트와 Runtime 멀티리전 엔드포인트에서 불가 |
| 적용 상황 | 국내 리전 배치와 데이터 상주 요건 검토 |
| 구성 요소 | 리전 · 멀티리전 · global 엔드포인트 |
| 전제 조건 | CMEK가 필요하면 리전 엔드포인트 |
| 걸리는 평가 축 | 커스터마이징 — 배치 리전, 네트워크(서울 Gateway 미지원) / 데이터 정책 — 처리 위치 / 효과 — 가용성(멀티리전) |

### 근거 7 — Agent Gateway: MCP 트래픽 파싱 · 도구 단위 정책, 기본 거부, Model Armor

| 항목 | 내용 |
|---|---|
| 출처 | Agent Gateway overview · Google Cloud 문서 · https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview |
| 날짜 | 갱신 2026-10-07 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — **MCP 지원 방식: MCP 게이트웨이(관리형).** ingress(Client-to-Agent) · egress(Agent-to-Anywhere) 모드, Agent Runtime은 둘 다 지원. HTTP 기반 MCP와 A2A를 중계하고 MCP 요청을 파싱해 도구 단위로 접근 제한. MCP · REST · gRPC 간 변환. egress는 에이전트 ID에 `iap.resources.egressViaIAP` 권한을 주는 IAM 정책이 있어야 하고 없으면 기본 거부. Model Armor(선택)로 프롬프트 인젝션 · 민감정보 유출 · 유해 콘텐츠 검사. 인스턴스 하나가 Registry 등록 리소스 최대 5,000개 관리 |
| 적용 상황 | 에이전트가 사내 · 타사 MCP 서버나 API를 부를 때 중앙에서 통제 |
| 구성 요소 | Agent Gateway, Agent Registry, IAM(IAP Egressor, Principal Access Boundary), Model Armor, Service Extensions |
| 전제 조건 | 목적지를 Agent Registry에 등록, 에이전트 ID와 IAM 정책. 서울 리전은 Gateway 미지원(근거 6) |
| 걸리는 평가 축 | AI 인프라 적합성 — MCP 지원 방식, 권한 전파, 메타데이터 노출(Registry 카탈로그) / 데이터 정책 — 반출 경로 통제, 민감정보 식별(Model Armor) / 커스터마이징 — 가드레일 |

### 근거 8 — ADK의 MCP 클라이언트(McpToolset)

| 항목 | 내용 |
|---|---|
| 출처 | MCP tools · Agent Development Kit 공식 문서(Google) · https://adk.dev/tools-custom/mcp-tools/ |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — **MCP 클라이언트(벤더 오픈소스 ADK).** `McpToolset`으로 외부 MCP 서버 도구를 찾아 쓰고 `tool_filter`로 노출 도구를 좁힘. 전송 stdio · Streamable HTTP · SSE. 원격 연결은 헤더나 `auth_scheme` · `auth_credential`로 인증, OAuth2 토큰 갱신 처리. 운영 배포에서는 `agent.py`에 McpToolset을 동기 방식으로 정의해야 하고, 세션 복원 시 MCP 연결이 자동으로 다시 맺어지지 않음. ADK 도구를 MCP 서버로 노출하는 패턴(`to_mcp_server`)도 있음 |
| 적용 상황 | Agent Runtime에 올린 ADK 에이전트가 MCP 도구를 소비할 때 |
| 구성 요소 | ADK, McpToolset, 원격 MCP 서버 |
| 전제 조건 | ADK로 개발한 에이전트, 원격 MCP 서버 인증 정보 |
| 걸리는 평가 축 | AI 인프라 적합성 — 공개 표준 연계(MCP 클라이언트), 데이터 읽기 인터페이스 |

### 근거 9 — 요금: 에이전트 컴퓨팅 vCPU-시간 · 메모리 GiB-시간, 무료 등급

| 항목 | 내용 |
|---|---|
| 출처 | Gemini 플랫폼 가격 책정 · Google Cloud · https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing (내장 브라우저로 열어 확인 — WebFetch는 용량 초과로 실패) |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — Runtime과 샌드박스(코드 실행 · 컴퓨터 사용)는 에이전트 컴퓨팅 vCPU-시간 **$0.085**(월 50시간 무료) + 에이전트 메모리 GiB-시간 **$0.009**(월 100 GiB-시간 무료), 1년 · 3년 Flexible Savings Plan 할인($0.0765 · $0.068 / $0.0081 · $0.0072). 초 단위 반올림, **턴 사이 다음 프롬프트를 기다리는 유휴 시간은 과금하지 않음.** 에이전트 스토리지 $0.30/GiB-월. Agent Gateway(Agent-to-Anywhere)는 API 호출 · 승인 15,000건당 vCPU-시간 1개($0.085), 2026-07-13부터 과금. Sessions · Memory Bank · Skill Registry는 2026-09-01부터 저장 $0.30/GiB-월 + 읽기 300만 건 · 쓰기 100만 건당 vCPU-시간 1개($0.085), 모델 토큰은 별도 |
| 적용 상황 | 런타임 · 메모리 · 게이트웨이 비용 추정, AgentCore와 과금 단위 비교 |
| 구성 요소 | 에이전트 컴퓨팅 · 메모리 · 스토리지 SKU, Agent Gateway, Sessions, Memory Bank, Skill Registry |
| 전제 조건 | 표시 단가의 리전 〔미정〕(표에 리전 표기 확인 못 함). 시맨틱 거버넌스 정책 과금은 "2026년 후반" 시작 예정 |
| 걸리는 평가 축 | 비용 — 과금 단위 · 단가, 인프라 사용료 |

### 근거 10 — 출시 발표의 고객 사례

| 항목 | 내용 |
|---|---|
| 출처 | Introducing Gemini Enterprise Agent Platform · Google Cloud 공식 블로그(Michael Gerstenhaber, Michael Bachman) · https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform |
| 날짜 | 발행 2026-04-23 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | B(사업자 선정 사례) — Comcast는 Xfinity Assistant를 ADK와 Agent Runtime 기반 멀티에이전트로 재구축, Color Health는 ADK로 만든 Color Assistant를 Agent Runtime에서 운영, Gurunavi는 Memory Bank 사용, L'Oréal은 MCP로 데이터 소스 연결. Payhawk의 "경비 제출 시간 50% 이상 단축"은 회사 자체 수치라 쓰지 않음. 같은 글의 "모든 Vertex AI 서비스와 로드맵은 Agent Platform으로만 제공된다"는 방향 선언은 A 사실로 쓸 수 있음 |
| 적용 상황 | 대고객 어시스턴트 같은 운영 사례 확인 |
| 구성 요소 | Agent Runtime, ADK, Memory Bank, MCP |
| 전제 조건 | — |
| 걸리는 평가 축 | 동향 적합성 — 운영 사례, 로드맵 방향 |

### 비어 있는 것

- 비용 — 서울 리전 단가, 운영 인력, 전환 비용
- 효과 — 처리량 수치 · 가용성 SLA
- 효율 — 업그레이드 · 패치 부담(런타임 버전 · SDK 교체 주기)
- 동향 적합성 — 오픈소스 저장소의 릴리스 · 기여자 수치, 구 Vertex AI API · SDK의 지원 종료 일정
- 커스터마이징 — 조직 · 폴더 단위 배치, 중앙 ID · SSO(Workforce Identity 등) 연동, 태깅 · 라벨
- 데이터 정책 — 보존 · 삭제(Sessions · Memory Bank TTL, 삭제 API), 리니지 · 카탈로그(Dataplex 등) 연결. 민감정보 식별은 Model Armor(근거 7)뿐
- AI 인프라 적합성 — Agent Runtime이 MCP 서버를 직접 호스팅하는 공식 방식. 확인된 MCP 지원은 공식 원격 MCP 서버(근거 2, 플랫폼 관리용) · MCP 게이트웨이(근거 7) · ADK MCP 클라이언트(근거 8)

상한 10건에 닿아 바꿔 뺀 것: 요금 변경 공지 블로그(2025-12-19 — 2026-09-01 계량 변경 이전 단가라 근거 9 요금 페이지로 대체), Agent Platform 데이터 상주 문서, 2026-07-30 "What's new" 블로그.

---

## vLLM 직접 운영

오픈소스 LLM 서빙 엔진을 EKS / Kubernetes 위에 직접 올려 모델을 자체 호스팅 — 데이터가 모델 제공사로 나가지 않는 구조의 대조군. 상태: 〔미정〕 — 오픈소스라 "GA" 표기 없음. 릴리스 라인은 0.x, 최신 v0.31.0(2026-10-05, GitHub API published_at으로 확인).

### 근거 1 — PyTorch Foundation 호스팅 프로젝트로 편입 (오래됨)

| 항목 | 내용 |
|---|---|
| 출처 | PyTorch Foundation Welcomes vLLM as a Hosted Project · PyTorch Foundation · https://pytorch.org/blog/pytorch-foundation-welcomes-vllm/ |
| 날짜 | 갱신 2025-05-06 · 확인 2026-10-11 · **「오래됨」** — 거버넌스 구조 설명용으로만, 동향 근거로는 쓰지 않음 |
| 등급 | A — vLLM은 UC Berkeley가 기여한 프로젝트로 PyTorch Foundation의 중립 거버넌스 아래 호스팅 |
| 적용 상황 | 특정 벤더에 묶이지 않은 재단 소속 서빙 엔진이 필요할 때 |
| 구성 요소 | vLLM 엔진(PyTorch 기반), NVIDIA · AMD GPU, TPU, AWS Neuron, Intel 등 하드웨어 백엔드 |
| 전제 조건 | PyTorch 생태계에 맞춘 하드웨어 · 드라이버 |
| 걸리는 평가 축 | 동향 적합성 — 종속성(재단 거버넌스) |

### 근거 2 — 릴리스 주기와 커뮤니티 규모

| 항목 | 내용 |
|---|---|
| 출처 | vllm-project/vllm Releases · 저장소 · GitHub · https://github.com/vllm-project/vllm/releases · https://github.com/vllm-project/vllm |
| 날짜 | v0.31.0 2026-10-05 · v0.30.0 2026-09-22 · v0.29.0 2026-09-09 (연도는 GitHub API published_at으로 확인) · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — 약 2주 간격 마이너 릴리스. v0.31.0은 요청별 `mm_processor_kwargs`를 기본 거부하는 호환성 깨짐(breaking) 변경과 보안 수정 포함. 스타 93.5k, 포크 23.2k, Apache-2.0, README 기준 기여자 2000명 이상 |
| 적용 상황 | 업그레이드 주기와 커뮤니티 활동 판단 |
| 구성 요소 | 엔진 릴리스(도구 호출 파서, XGrammar 스키마 제약 등) |
| 전제 조건 | 2주 단위 릴리스를 따라가며 회귀 시험을 돌릴 운영 체계 |
| 걸리는 평가 축 | 동향 적합성 — 릴리스 · 커뮤니티 활동, 공개 포맷(Apache-2.0) / 효율 — 업그레이드 · 패치 부담(호환성 깨짐 변경) |

### 근거 3 — 보안 공지 빈도와 공개 정책

| 항목 | 내용 |
|---|---|
| 출처 | Security (Advisories, Security policy) · vllm-project/vllm GitHub · https://github.com/vllm-project/vllm/security |
| 날짜 | 최신 공지 2026-10-06 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — 2026-09-03~10-06에 공지 10건. High 3건 중 요청값으로 원격 코드 실행이 가능한 건(GHSA-h3rc-6mm3-gc2m), 인증 없이 엔진을 멈추게 하는 DoS 건 여러 개. Critical · High는 비공개 포크에서 수정 후 사전 통보 그룹과 조율해 공개 |
| 적용 상황 | 직접 운영 시 패치를 얼마나 자주 받아야 하는지 가늠할 때 |
| 구성 요소 | GHSA 공지, CVE 발급, 사전 통보 제도(대규모 배포 조직 대상) |
| 전제 조건 | 공지를 감시하고 빠르게 이미지를 재배포할 체계 |
| 걸리는 평가 축 | 효율 — 업그레이드 · 패치 부담 / 동향 적합성 — 운영 성숙도(보안 대응 체계) |

### 근거 4 — 보안 가이드: 인증 범위 · 네트워크 격리 · 멀티테넌시

| 항목 | 내용 |
|---|---|
| 출처 | Security · vLLM 공식 문서 · https://docs.vllm.ai/en/latest/usage/security.html |
| 날짜 | 갱신 2026-10-09 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — `--api-key`는 `/v1` · `/v2` · `/inference` · `/cohere` 경로만 보호. `/pooling` · `/rerank` · `/update_weights` · `/health` · `/tokenize` 등은 인증이 없어 허용 엔드포인트만 통과시키는 리버스 프록시 권고. 노드 간 통신(분산 처리 · KV 전송)은 기본 비보안이라 격리 네트워크 필요. 한 프로세스 안에서 테넌트를 격리하지 않으므로 인스턴스 분리나 인증 게이트웨이 필요. 프리픽스 캐시 타이밍 사이드채널은 사용자별 `cache_salt`로 막음. 미디어 URL 출처는 `--allowed-media-domains`로 제한(SSRF 방지) |
| 적용 상황 | 사내망 · VPC 안에서 자체 모델 엔드포인트를 노출할 때 |
| 구성 요소 | vLLM API 서버, 리버스 프록시 또는 인증 게이트웨이, 격리 서브넷 · 방화벽 |
| 전제 조건 | 앞단 게이트웨이(인증 · 엔드포인트 허용목록)와 노드 간 네트워크 분리 |
| 걸리는 평가 축 | 커스터마이징 — 네트워크(VPC 격리), 중앙 ID · SSO 연동(엔진 자체는 정적 API 키뿐) / 데이터 정책 — 접근 통제, 반출 경로 통제(미디어 fetch 제한) / AI 인프라 적합성 — 권한 전파(엔진은 사용자 단위 권한을 모름) |

### 근거 5 — OpenAI 호환 API 서버

| 항목 | 내용 |
|---|---|
| 출처 | Online Serving (OpenAI-Compatible Server) · vLLM 공식 문서 · https://docs.vllm.ai/en/latest/serving/online_serving/ |
| 날짜 | 갱신 2026-10-08 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — `/v1/completions`, `/v1/chat/completions`, `/v1/responses`(조회 · 취소 포함), `/v1/embeddings` 지원. `suffix` 미지원, `user` 무시 |
| 적용 상황 | 기존 OpenAI SDK 클라이언트 · 에이전트 프레임워크를 엔드포인트 URL만 바꿔 자체 모델로 돌릴 때 |
| 구성 요소 | `vllm serve` API 서버 |
| 전제 조건 | 대상 모델에 chat template이 있어야 chat 엔드포인트 사용 |
| 걸리는 평가 축 | 효과 — 처리 방식(실시간 온라인 서빙), 원천 · 대상 연결 / 동향 적합성 — 이관 경로(OpenAI API 형식) / AI 인프라 적합성 — 에이전트가 쓰는 인터페이스 |

### 근거 6 — MCP: vLLM이 MCP 클라이언트로 동작(gpt-oss · Responses API 한정)

| 항목 | 내용 |
|---|---|
| 출처 | GPT OSS — vLLM Recipes · vLLM 공식 문서 · https://docs.vllm.ai/projects/recipes/en/stable/OpenAI/GPT-OSS.html |
| 날짜 | 갱신 2026-04-15 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — **MCP 지원 방식: 엔진에 내장된 MCP 클라이언트(공식 MCP 서버 · 게이트웨이는 아님).** `--tool-server ip:port,...`로 MCP SSE 서버를 붙이면 vLLM이 MCP 클라이언트가 되고 도구 설명을 시스템 프롬프트에 주입. 내장 도구와 MCP는 Responses API에서만, Chat Completions는 미지원(함수 호출만). `--tool-server demo`는 데모 용도 |
| 적용 상황 | 자체 호스팅 모델이 사내 MCP 도구 서버를 직접 호출해야 할 때 |
| 구성 요소 | vLLM(MCP 클라이언트), 외부 MCP SSE 도구 서버, Harmony 형식 모델(gpt-oss) |
| 전제 조건 | Harmony 형식 모델, MCP 서버가 server info에 instructions 제공 |
| 걸리는 평가 축 | AI 인프라 적합성 — 공개 표준 연계(MCP), 작업 호출 · 결과 수신 |

### 근거 7 — Harmony 외 모델로 MCP를 넓히자는 요청은 자동 종료

| 항목 | 내용 |
|---|---|
| 출처 | Issue #30115 "[Feature]: MCP Support for Non Harmony Models" · vllm-project/vllm GitHub · https://github.com/vllm-project/vllm/issues/30115 |
| 날짜 | 개설 2025-12-05, 봇이 2026-06-26에 "not planned"로 종료 · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | A — 일반 chat template 모델의 Responses API MCP 지원 요청. 하위 작업 일부(비Harmony 파이썬 도구 호출 파싱 등)는 병합, 범용 MCP 도구 · 스트리밍 등은 남은 채 비활성으로 자동 종료, 메인테이너 결정 표명 없음 |
| 적용 상황 | gpt-oss가 아닌 모델(Llama · Qwen 등)로 MCP를 쓰려 할 때의 지원 범위 확인 |
| 구성 요소 | Responses API 파서, MCP 도구 경로 |
| 전제 조건 | — |
| 걸리는 평가 축 | AI 인프라 적합성 — 공개 표준 연계(모델별 MCP 지원 범위) / 동향 적합성 — 로드맵 방향 |

### 근거 8 — AWS 공식 EKS 가이드: vLLM 배포 구조

| 항목 | 내용 |
|---|---|
| 출처 | Load & Serve Models on Amazon EKS (vLLM) · Amazon EKS User Guide · https://docs.aws.amazon.com/eks/latest/userguide/ml-realtime-inference-llm-inference-vllm.html |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — AWS DLC vLLM 0.21.0 이미지(SOCI, 보안 패치 포함), 자체 S3 버킷에서 Run:ai Model Streamer로 GPU 메모리에 직접 로드(10.4GB를 약 5초), EKS Auto Mode 또는 Karpenter GPU 노드풀(예시 g6e.4xlarge), ClusterIP 서비스, ServiceMonitor로 `/metrics` 수집 → kube-prometheus-stack · Grafana. 도구 호출은 `--enable-auto-tool-choice --tool-call-parser`. 인터넷 공개 ALB는 소스 IP 제한 필수, 내부 스킴 · TLS · 인증 권고 |
| 적용 상황 | AWS 계정 안 EKS에서 모델 가중치와 추론을 모두 자체 VPC 안에 두는 구조 |
| 구성 요소 | EKS, GPU 노드풀, S3(가중치), DLC 이미지, Prometheus · Grafana, AWS Load Balancer Controller · ALB |
| 전제 조건 | EKS AI/ML 클러스터 셋업, GPU 인스턴스 쿼터, 가중치 반입(Hugging Face 등) |
| 걸리는 평가 축 | 효율 — 관리할 구성요소 수, 직접 운영 비중, 기존 모니터링 연결(Prometheus) / 커스터마이징 — 네트워크(ALB 스킴 · CIDR) / 데이터 정책 — 처리 위치(가중치 · 추론 모두 자기 계정 안) / 효과 — 기동 지연 |

### 근거 9 — EKS 요금(컨트롤 플레인 · Auto Mode)

| 항목 | 내용 |
|---|---|
| 출처 | Amazon EKS pricing · AWS · https://aws.amazon.com/eks/pricing/ |
| 날짜 | 상시 갱신 — 확인 2026-10-11 기준 |
| 등급 | A — 클러스터당 시간당 $0.10(표준 지원), 연장 지원 $0.60(14개월 표준 기간 이후 12개월). Auto Mode 관리비는 EC2 요금과 따로 초 단위(예: c6a.2xlarge에 $0.03672/h). EC2 노드 요금 별도 |
| 적용 상황 | 직접 운영 시 플랫폼 고정비 산정 |
| 구성 요소 | EKS 컨트롤 플레인, Auto Mode 관리비 |
| 전제 조건 | GPU 인스턴스 단가는 이 페이지에 없음 〔미정〕 |
| 걸리는 평가 축 | 비용 — 과금 단위 · 단가(인프라 사용료) / 동향 적합성 — 지원 종료 계획(Kubernetes 버전 지원 기간) |

### 근거 10 — 공식 vLLM Conference의 기업 운영 사례 세션

| 항목 | 내용 |
|---|---|
| 출처 | vLLM Conference 2026 (Ray Summit 공동 개최) · vllm.ai · https://vllm.ai/events/vllm-conference/2026 |
| 날짜 | 행사 2026-08-24~26(세션 08-25 · 26) · 확인 2026-10-11 · 오래됨 아님 |
| 등급 | B — 세션 제목만 확인: Red Hat "Production-Grade Distributed Inference with llm-d"(멀티노드 Kubernetes 실트래픽), Inferact "Serving vLLM on Agentic Production Workloads", MiniMax "Serving MiniMax M3 at Scale". 사업자 측 발표 |
| 적용 상황 | 대규모 · 에이전트 워크로드의 운영 사례 확인 |
| 구성 요소 | llm-d(분산 추론 오케스트레이션), vLLM |
| 전제 조건 | 세션 내용은 제목 수준만 확인 〔미정〕 |
| 걸리는 평가 축 | 동향 적합성 — 운영 사례 |

### 비어 있는 것

- 비용 — GPU 인스턴스 시간당 단가(EC2 On-Demand · G6e 페이지 모두 단가가 렌더링되지 않음), 운영 인력 규모, 전환 비용
- 효과 — 처리량 · 지연 · 가용성 수치(공식 벤치마크), 일괄(batch) 처리, 작업 의존성 · 일정, 기존 작업 이관
- 커스터마이징 — 랜딩존 안 계정 배치, 중앙 ID · SSO(엔진은 정적 API 키뿐이라 게이트웨이에 의존), 가드레일 예외 필요 여부, 태깅 · 중앙 로깅
- 데이터 정책 — 분류 · 민감정보 식별, 접근 기록(프롬프트 · 응답 로깅 기본 동작), 보존 · 삭제, 리니지 · 카탈로그 연결
- AI 인프라 적합성 — 메타데이터 · 스키마 노출. MCP는 "gpt-oss + Responses API 한정 MCP 클라이언트"까지만 확인(근거 6 · 7). 공식 MCP 서버 · 게이트웨이 없음

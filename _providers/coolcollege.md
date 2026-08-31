---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Coolcollege Agentic Access
  operation_count: 25
  slug: coolcollege-agentic-access
  summary_line: 25 operations · 8 acting
api_count: 1
apis:
- description: '* 访问学习相关的操作以及数据 * ```{enterprise-id}```可在系统内获取 * 学习的```{plan-id}```可以通过获取学习任务列表的API得到'
  name: 酷学院 (Cool College) 学习 API
  slug: coolcollege-default-api
- description: Everything about your Pets
  name: 酷学院 (Cool College) pet API
  slug: coolcollege-pet-api
- description: '* OA系统 人员/部门变动事件推送API * 访问该目录下接口时header中需要携带参数 `access-token` 和 `enterprise-id` * access-token 参数来自鉴权接口返回的token值'
  name: 酷学院 (Cool College) thirdoa API
  slug: coolcollege-thirdoa-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: 酷学院 REST 学习 API
  slug: open-coolcollege-default-api
- collection_type: open
  name: 酷学院 REST 学习 pet API
  slug: open-coolcollege-pet-api
- collection_type: open
  name: 酷学院 REST 学习 thirdoa API
  slug: open-coolcollege-thirdoa-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/beisen/
- group: other
  title: ''
  type: Overlay
  url: overlays/coolcollege-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.coolcollege.cn/
- group: docs
  title: ''
  type: APIReference
  url: https://open.coolcollege.cn/
- group: docs
  title: ''
  type: Documentation
  url: https://help.coolcollege.cn/
- group: operate
  title: ''
  type: Support
  url: https://help.coolcollege.cn/
- group: company
  title: ''
  type: Blog
  url: https://www.coolcollege.com/originalnews
- group: start
  title: ''
  type: SignUp
  url: https://www.coolcollege.com/freeTrial.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coolcollege.com/service.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coolcollege.com/wp-content/uploads/2025/04/酷学院平台隐私政策-2025.pdf
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coolcollege.cn/
- group: auth
  title: ''
  type: Authentication
  url: authentication/coolcollege-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/coolcollege-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/coolcollege-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/coolcollege-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/coolcollege-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/coolcollege-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/coolcollege-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coolcollege-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coolcollege-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coolcollege-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coolcollege.com
created: '2026-07-17'
description: 酷学院 (Cool College) is an enterprise training and talent-development SaaS platform operated by 酷渲（北京）科技发展有限公司 (Cool Render (Beijing) Technology Co., Ltd.), founded in 2017 and acquired by Beisen in 2025. It provides AI-assisted corporate e-learning — course libraries, learning tasks, learning projects, exams, certificates, credits, and instructor management — with deep integration into DingTalk, Feishu, and WeChat Work. Its Open API (v2) lets integrators sync organization data (users, departments, positions) and read learning, exam, certificate, credit, and archive data for an enterprise tenant, authenticated via an HMAC-SHA256 signature exchange that issues an access_token.
image: https://oss.coolcollege.cn/1553567081676c%402x.png
layout: provider
mcp_servers:
- description: ''
  name: 酷学院 (Cool College) MCP Server
  slug: 酷学院-cool-college-mcp-server
modified: '2026-07-18'
name: 酷学院 (Cool College)
nav: Providers
network: true
overview: '酷学院 (Cool College) publishes 3 APIs on the [APIs.io](https://apis.io/) network: 学习 API, pet API, and thirdoa API. Tagged areas include Company, Corporate Training, E-Learning, Talent Development, and Human Resources.


  酷学院 (Cool College)''s developer surface includes API reference, documentation, support, engineering blog, signup flow, authentication, and 17 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 4.5
    contract_quality: 44.0
    developer_ergonomics: 38.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 35.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 42.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coolcollege/refs/heads/main/screenshots/coolcollege-2026-07-25T210405.png
security:
- kind: authentication
  name: Coolcollege Authentication
  slug: coolcollege-authentication
  summary_line: signature/token · 1 scheme
- kind: domain-security
  name: Coolcollege Domain Security
  slug: coolcollege-domain-security
  summary_line: TLSv1.2
slug: coolcollege
tags:
- Company
- Corporate Training
- E-Learning
- Talent Development
- Human Resources
- Software-as-a-Service
- Learning Management
- China
website: https://www.coolcollege.com
---

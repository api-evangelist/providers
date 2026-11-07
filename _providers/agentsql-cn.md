---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AgentSQL provides a database security gateway and autonomous query interface.
  name: AgentSQL API
  slug: agentsql-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: Security
  url: https://github.com/cuipengdba/agentsql/security/policy
- group: auth
  href: https://artifacts.apis.io/agentsql-cn/authentication/agentsql-cn-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentsql-cn-authentication.yml
- group: auth
  href: https://artifacts.apis.io/agentsql-cn/well-known/agentsql-cn-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentsql-cn-security.txt
- group: agent
  href: https://artifacts.apis.io/agentsql-cn/well-known/agentsql-cn-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentsql-cn-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentsql-cn/hosts/agentsql-cn-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentsql-cn-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentsql-cn/vendors/agentsql-cn-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentsql-cn-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agentsql-cn/security/agentsql-cn-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentsql-cn-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentsql-cn/security/agentsql-cn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentsql-cn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentsql.cn/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/cuipengdba/agentsql/tree/main/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/cuipengdba/agentsql/blob/main/docs/GETTING_STARTED.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cuipengdba
coverage:
  checked: '2026-11-01'
  detail: The provider’s API reference is only available as PDF documents, with no machine‑readable OpenAPI or other spec.
  evidence:
  - status: 200
    url: https://agentsql.cn/assets/docs/agentsql-user-guide-v4.3.0.pdf
  reason: pdf-only-docs
  state: unreadable
created: '2026-11-01'
description: AgentSQL（中文名：智盾）是面向 AI Agent 的数据库安全网关与 MCP Server。模型发出的 PostgreSQL / MySQL 请求在到达数据库前，经过身份认证、SQL 解析、静态与动态风险检查、四态决策与受控执行；结果按配置脱敏，并在应用层留下持久审计。AgentSQL 自有问数、图表、仪表板和嵌入应用页面，模型生成的 SQL 继续经过数据库安全网关。已有 SQLBot 部署也可接入 AgentSQL 做数据库访问控制；完整社区版功能、全部页面和现有系统零改动替换仍待逐项验收。
image: https://agentsql.cn/assets/og-cover.png?v=3.6.0
layout: provider
modified: '2026-11-01'
name: AgentSQL
nav: Providers
network: true
overview: 'AgentSQL is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Database, Security, Artificial Intelligence, Open Source, and Gateways.


  AgentSQL''s developer surface includes authentication, documentation, getting-started guide, and 9 more developer resources.'
random_paper: 13
scopes:
- name: Agentsql Cn Scopes
  scope_count: 0
  slug: agentsql-cn-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.2
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 16.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentsql Cn Authentication
  slug: agentsql-cn-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agentsql Cn Domain Security
  slug: agentsql-cn-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Agentsql Cn Vulnerability Disclosure
  slug: agentsql-cn-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: agentsql-cn
tags:
- Database
- Security
- Artificial Intelligence
- Open Source
- Gateways
website: https://agentsql.cn/
---

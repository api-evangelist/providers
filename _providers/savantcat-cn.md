---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: near-conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 6.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/savantcat-cn/security/savantcat-cn-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/savantcat-cn-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/savantcat-cn/llms/savantcat-cn-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/savantcat-cn-llms.txt
- group: other
  href: https://artifacts.apis.io/savantcat-cn/a2a/savantcat-cn-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/savantcat-cn-a2a.yml
- group: agent
  href: https://artifacts.apis.io/savantcat-cn/mcp/savantcat-cn-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/savantcat-cn-mcp.yml
- group: auth
  href: https://artifacts.apis.io/savantcat-cn/well-known/savantcat-cn-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/savantcat-cn-security.txt
- group: agent
  href: https://artifacts.apis.io/savantcat-cn/well-known/savantcat-cn-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/savantcat-cn-well-known.yml
- group: other
  href: https://artifacts.apis.io/savantcat-cn/hosts/savantcat-cn-hosts.yml
  title: ''
  type: Hosts
  url: hosts/savantcat-cn-hosts.yml
- group: auth
  href: https://artifacts.apis.io/savantcat-cn/security/savantcat-cn-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/savantcat-cn-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/savantcat-cn/security/savantcat-cn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/savantcat-cn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://savantcat.cn/
coverage:
  checked: '2026-10-29'
  detail: Provider site returns HTML with no machine‑readable API specification or documentation host.
  evidence:
  - status: 200
    url: https://savantcat.cn/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: 合尘猫（SavantCat）是一家专注于中小企业专属知识库建设与 AI 客服落地的公司，提供将分散的产品资料、政策条款、服务规范整理成 AI 可读的知识底座，并依据 GB/T 47746—2026 国家标准进行达标自查与整改。其解决方案帮助企业内部喂养 AI 客服，同时让外部大模型主动引用，实现内部效率提升和外部曝光双重价值。
layout: provider
mcp_servers:
- description: Remote MCP server at savantcat.cn.
  name: savantcat-cn MCP Server
  slug: savantcat-cn-mcp-yml
modified: '2026-10-29'
name: savantcat-cn
nav: Providers
network: true
overview: savantcat-cn is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Knowledge Base, Small Business, and Enterprise.
random_paper: 19
score:
  band: minimal
  composite: 5.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.7
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 5.4
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/savantcat-cn/savantcat-cn-2026-11-03T142741.png
security:
- kind: domain-security
  name: Savantcat Cn Domain Security
  slug: savantcat-cn-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Savantcat Cn Vulnerability Disclosure
  slug: savantcat-cn-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: savantcat-cn
tags:
- Company
- Artificial Intelligence
- Knowledge Base
- Small Business
- Enterprise
website: https://savantcat.cn/
---

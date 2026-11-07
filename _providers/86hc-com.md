---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: 86Hc Com Agentic Access
  operation_count: 9
  slug: 86hc-com-agentic-access
  summary_line: 9 operations · 7 acting
api_count: 1
apis:
- baseURL: https://86hc.com
  baseurl_source: declared
  description: Official 86hc.com (HC Business / 恒诚) Hong Kong Corporate Holographic Intelligence & Statutory Filing API.
  name: Hong Kong Company MCP & Corporate Registry API
  slug: hong-kong-company-mcp-corporate-registry-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/86hc-com/agentic-access/86hc-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/86hc-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/86hc-com/plans/86hc-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/86hc-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/86hc-com/rules/86hc-com-rules.yml
  title: ''
  type: Spectral
  url: rules/86hc-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/86hc-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://www.86hc.com/terms-of-service
- group: design
  href: https://artifacts.apis.io/86hc-com/conformance/86hc-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/86hc-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/86hc-com/llms/86hc-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/86hc-com-llms.txt
- group: other
  href: https://artifacts.apis.io/86hc-com/a2a/86hc-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/86hc-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/86hc-com/mcp/86hc-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/86hc-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/86hc-com/well-known/86hc-com-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/86hc-com-www-security.txt
- group: auth
  href: https://artifacts.apis.io/86hc-com/well-known/86hc-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/86hc-com-security.txt
- group: agent
  href: https://artifacts.apis.io/86hc-com/well-known/86hc-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/86hc-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/86hc-com/hosts/86hc-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/86hc-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.86hc.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.86hc.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.86hc.com/pricing
- group: auth
  href: https://artifacts.apis.io/86hc-com/authentication/86hc-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/86hc-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/86hc-com/security/86hc-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/86hc-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/86hc-com/security/86hc-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/86hc-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.86hc.com/
created: '2026-10-31'
description: 恒诚是一家提供香港公司注册、董事股东查询、商业尽职调查及相关法定文件调阅服务的平台。通过其网站，用户可以在线进行公司设立、变更、年报提交、银行开户、司法诉讼查询等业务，支持多语言界面并提供快速电子交付。平台聚合香港公司注册处、商业登记署及法院等官方数据，帮助金融机构和企业进行合规审查和风险评估。服务覆盖公司全生命周期管理，提供专业顾问支持，致力于提升企业合规效率和信息透明度。
image: https://www.86hc.com/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.86hc.com requiring an API key.
  name: 恒诚 MCP Server
  slug: 86hc-com-mcp-yml
modified: '2026-10-31'
name: 恒诚
nav: Providers
network: true
overview: '恒诚 is listed with 1 API on the [APIs.io](https://apis.io/) network: Hong Kong Company MCP & Corporate Registry API. Tagged areas include Hong Kong, Business Intelligence, Due Diligence, Corporate Services, and Compliance.


  The 恒诚 catalog on APIs.io includes 1 Spectral governance ruleset.


  恒诚''s developer surface includes pricing, authentication, and 18 more developer resources.'
plans:
- name: 86Hc Com Plans Pricing
  plan_count: 6
  slug: 86hc-com-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: 恒诚 API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: 86hc-com-rules
score:
  band: thin
  composite: 34.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 48.5
    catalog_earned_first_party: 12.0
    catalog_gap: 66.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 43.5
    developer_ergonomics: 18.3
    discoverability: 56.7
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: platform-generated
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 86Hc Com Authentication
  slug: 86hc-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: 86Hc Com Domain Security
  slug: 86hc-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: 86Hc Com Vulnerability Disclosure
  slug: 86hc-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: company-search
  slug: 86hc-com-company-search
slug: 86hc-com
tags:
- Hong Kong
- Business Intelligence
- Due Diligence
- Corporate Services
- Compliance
website: https://www.86hc.com/
---

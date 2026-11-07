---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Public API for batch WHOIS, ICP, and WeChat domain queries; requires bearer token authentication.
  name: Batch Domain Query API
  slug: batch-domain-query-api
- description: '爱域查 API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: 爱域查 API
  slug: aiyucha-com-api
artifact_total: 11
common:
- group: operate
  href: https://artifacts.apis.io/aiyucha-com/rate-limits/aiyucha-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aiyucha-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/aiyucha-com/plans/aiyucha-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aiyucha-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aiyucha-com/rules/aiyucha-com-rules.yml
  title: ''
  type: Spectral
  url: rules/aiyucha-com-rules.yml
- group: design
  href: https://artifacts.apis.io/aiyucha-com/json-ld/aiyucha-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aiyucha-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/aiyucha-com/vocabulary/aiyucha-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aiyucha-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aiyucha-com/data-model/aiyucha-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aiyucha-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/aiyucha-com/authentication/aiyucha-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aiyucha-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/aiyucha-com/conformance/aiyucha-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aiyucha-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/aiyucha-com/hosts/aiyucha-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aiyucha-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aiyucha-com/vendors/aiyucha-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aiyucha-com-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://aiyucha.com/zh/pricing
- group: start
  title: ''
  type: Login
  url: https://aiyucha.com/zh/login
- group: auth
  href: https://artifacts.apis.io/aiyucha-com/security/aiyucha-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiyucha-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiyucha.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aiyucha.com/zh/api
- group: docs
  title: ''
  type: APIReference
  url: https://aiyucha.com/zh/api
- group: start
  title: ''
  type: GettingStarted
  url: https://aiyucha.com/zh/guides
- group: operate
  title: ''
  type: Support
  url: https://aiyucha.com/zh/feedback
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aiyucha.com/zh/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aiyucha.com/zh/terms
coverage:
  checked: '2026-11-01'
  detail: API documentation requires a bearer token for all endpoints, preventing public access.
  evidence:
  - status: 200
    url: https://aiyucha.com/zh/api
  reason: auth-required
  state: gated
created: '2026-11-01'
description: 爱域查是一款面向中文用户的老域名查询与评估平台，提供批量域名 WHOIS、备案信息、建站历史、历史快照、外链/反链、域名被墙、DNS 污染以及微信拦截检测等多维度数据。用户可通过公开 API 进行批量查询，系统复用已有后台任务队列，实现高效查询与结果获取。平台同时提供 AI 深度评估、工作流自定义以及积分计费规则，支持免费单项查询和付费高级套餐，帮助用户在域名购买、出售和风险评估过程中做出精准判断。
image: https://aiyucha.com/static/aiyucha-logo-mark.svg?v=20260913-openring
json_schemas:
- name: GetV1BatchQueryJobidResponse
  property_count: 9
  slug: aiyucha-com-get-v1-batch-query-jobid-response
- name: PostV1BatchQueryRequest
  property_count: 3
  slug: aiyucha-com-post-v1-batch-query-request
- name: PostV1BatchQueryResponse
  property_count: 9
  slug: aiyucha-com-post-v1-batch-query-response
jsonld:
- class_count: 3
  name: Aiyucha Com Context
  property_count: 11
  slug: aiyucha-com-context
layout: provider
modified: '2026-11-01'
name: 爱域查
nav: Providers
network: true
overview: '爱域查 is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Domain, Lookup, SEO, Chinese, and Analytics.


  The 爱域查 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  爱域查''s developer surface includes authentication, pricing, documentation, API reference, getting-started guide, support, and 14 more developer resources.'
plans:
- name: Aiyucha Com Plans Pricing
  plan_count: 4
  slug: aiyucha-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Aiyucha Com Rate Limits
  slug: aiyucha-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: 爱域查 API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: aiyucha-com-rules
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 78.8
    catalog_earned_first_party: 24.0
    catalog_gap: 36.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 22.4
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 31.6
  previous_composite: 43.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aiyucha Com Authentication
  slug: aiyucha-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aiyucha Com Domain Security
  slug: aiyucha-com-domain-security
  summary_line: TLSv1.3
slug: aiyucha-com
tags:
- Domain
- Lookup
- SEO
- Chinese
- Analytics
website: https://aiyucha.com/
---

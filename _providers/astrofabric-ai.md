---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/astrofabric-ai/llms/astrofabric-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/astrofabric-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/astrofabric-ai/well-known/astrofabric-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/astrofabric-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/astrofabric-ai/vendors/astrofabric-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/astrofabric-ai-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/astrofabric-ai/plans/astrofabric-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/astrofabric-ai-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/astrofabric-ai/hosts/astrofabric-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/astrofabric-ai-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fokals.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fokals.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fokals.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.fokals.com/press
- group: start
  title: ''
  type: Login
  url: https://www.fokals.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://www.fokals.com/docs
- group: company
  title: ''
  type: Blog
  url: https://www.fokals.com/blog
- group: auth
  href: https://artifacts.apis.io/astrofabric-ai/security/astrofabric-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/astrofabric-ai-domain-security.yml
coverage:
  checked: '2026-11-02'
  detail: API reference page is HTML with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.fokals.com/docs/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: Fokals provides company intelligence data sets that include firmographic, technographic, hiring, intent, and announcement signals for public and private companies worldwide. The data is refreshed daily and delivered via API or bulk files for integration into research, investment, and product workflows. It offers licensing for redistribution and tools such as an AI readiness checker and technology stack lookup.
image: https://www.fokals.com/opengraph-image?74253cba8bfbd79a
json_schemas:
- name: GetApiV1CompaniesIdResponse
  property_count: 32
  slug: astrofabric-ai-get-api-v1-companies-id-response
- name: GetApiV1NewsResponse
  property_count: 13
  slug: astrofabric-ai-get-api-v1-news-response
- name: GetApiV1PostingsResponse
  property_count: 20
  slug: astrofabric-ai-get-api-v1-postings-response
- name: GetApiV1SeriesMoversResponse
  property_count: 14
  slug: astrofabric-ai-get-api-v1-series-movers-response
- name: GetApiV1SeriesResponse
  property_count: 14
  slug: astrofabric-ai-get-api-v1-series-response
- name: PostV1MarketTrendsRequest
  property_count: 10
  slug: astrofabric-ai-post-v1-market-trends-request
jsonld:
- class_count: 67
  name: Astrofabric Ai Context
  property_count: 227
  slug: astrofabric-ai-context
layout: provider
modified: '2026-11-02'
name: astrofabric-ai
nav: Providers
network: true
overview: 'astrofabric-ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company Intelligence, Data Licensing, Technographics, Hiring Data, and Intent Data.


  The astrofabric-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  astrofabric-ai''s developer surface includes pricing, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Astrofabric Ai Plans Pricing
  plan_count: 3
  slug: astrofabric-ai-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 6
  name: Astrofabric Ai Rate Limits
  slug: astrofabric-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: astrofabric-ai API Rules
  rule_count: 48
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 6
  slug: astrofabric-ai-rules
scopes:
- name: Astrofabric Ai Scopes
  scope_count: 0
  slug: astrofabric-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 28
    catalog_earned: 66.5
    catalog_earned_first_party: 24.0
    catalog_gap: 48.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.3
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 16.3
    developer_ergonomics: 6.0
    discoverability: 49.1
    operational_transparency: 31.6
  previous_composite: 34.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Astrofabric Ai Authentication
  slug: astrofabric-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Astrofabric Ai Domain Security
  slug: astrofabric-ai-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: find-companies
  slug: astrofabric-ai-find-companies
slug: astrofabric-ai
tags:
- Company Intelligence
- Data Licensing
- Technographics
- Hiring Data
- Intent Data
- Market Data
---

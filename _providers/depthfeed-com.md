---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.depthfeed.com
  baseurl_source: declared
  description: 'DepthFeed API as documented publicly: 79 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: DepthFeed API
  slug: depthfeed-com-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/depthfeed-com/plans/depthfeed-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/depthfeed-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/depthfeed-com/rules/depthfeed-com-rules.yml
  title: ''
  type: Spectral
  url: rules/depthfeed-com-rules.yml
- group: design
  href: https://artifacts.apis.io/depthfeed-com/json-ld/depthfeed-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/depthfeed-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/depthfeed-com/vocabulary/depthfeed-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/depthfeed-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/depthfeed-com/data-model/depthfeed-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/depthfeed-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/depthfeed-com/conformance/depthfeed-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/depthfeed-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/depthfeed-com/llms/depthfeed-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/depthfeed-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/depthfeed-com/mcp/depthfeed-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/depthfeed-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/depthfeed-com/hosts/depthfeed-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/depthfeed-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/depthfeed-com/vendors/depthfeed-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/depthfeed-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://depthfeed.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://depthfeed.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://depthfeed.com/pricing
- group: start
  title: ''
  type: Login
  url: https://depthfeed.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://depthfeed.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.depthfeed.com<!--
- group: auth
  href: https://artifacts.apis.io/depthfeed-com/security/depthfeed-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/depthfeed-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://depthfeed.com/
coverage:
  checked: '2026-11-05'
  detail: Documentation provides API reference but no OpenAPI/AsyncAPI/GraphQL spec is published.
  evidence:
  - status: 200
    url: https://depthfeed.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: DepthFeed provides Polymarket and Kalshi historical order‑book data with aligned reference prices, offering REST access, live WebSocket updates, and explicit coverage documentation for prediction‑market depth data.
json_schemas:
- name: GetV3ScreenerResponse
  property_count: 4
  slug: depthfeed-com-get-v3-screener-response
- name: GetV3SportsBooksAssetidHistoryResponse
  property_count: 4
  slug: depthfeed-com-get-v3-sports-books-assetid-history-response
- name: GetV3WhoamiResponse
  property_count: 2
  slug: depthfeed-com-get-v3-whoami-response
- name: PostPaperHookTokenRequest
  property_count: 6
  slug: depthfeed-com-post-paper-hook-token-request
- name: PostPaperHookTokenResponse
  property_count: 7
  slug: depthfeed-com-post-paper-hook-token-response
- name: PostV3SportsWebhooksRequest
  property_count: 3
  slug: depthfeed-com-post-v3-sports-webhooks-request
jsonld:
- class_count: 63
  name: Depthfeed Com Context
  property_count: 29
  slug: depthfeed-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.depthfeed.com.
  name: DepthFeed MCP Server
  slug: depthfeed-com-mcp-yml
modified: '2026-11-05'
name: DepthFeed
nav: Providers
network: true
overview: 'DepthFeed is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Data, Market Data, and Prediction Markets.


  The DepthFeed catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DepthFeed''s developer surface includes pricing, documentation, and 16 more developer resources.'
plans:
- name: Depthfeed Com Plans Pricing
  plan_count: 4
  slug: depthfeed-com-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: DepthFeed API Rules
  rule_count: 46
  severity_counts:
    error: 40
    hint: 0
    info: 3
    warn: 3
  slug: depthfeed-com-rules
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 67.8
    catalog_earned_first_party: 12.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 19.0
    discoverability: 60.0
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 23.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Depthfeed Com Domain Security
  slug: depthfeed-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: depthfeed-com
tags:
- Finance
- Data
- Market Data
- Prediction Markets
website: https://depthfeed.com/
---

---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
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
    auth_clarity: bearer
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: FanLine Wire provides real-time FanDuel odds via REST and WebSocket.
  name: FanLine Wire API
  slug: fanline-wire-api
- baseURL: https://api.fanlinewire.com
  baseurl_source: declared
  description: 'fanlinewire-com API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: fanlinewire-com API
  slug: fanlinewire-com-api
artifact_total: 17
common:
- group: operate
  href: https://artifacts.apis.io/fanlinewire-com/rate-limits/fanlinewire-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fanlinewire-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/fanlinewire-com/rules/fanlinewire-com-rules.yml
  title: ''
  type: Spectral
  url: rules/fanlinewire-com-rules.yml
- group: design
  href: https://artifacts.apis.io/fanlinewire-com/json-ld/fanlinewire-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fanlinewire-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/fanlinewire-com/vocabulary/fanlinewire-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fanlinewire-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/fanlinewire-com/data-model/fanlinewire-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fanlinewire-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/fanlinewire-com/authentication/fanlinewire-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fanlinewire-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/fanlinewire-com/conformance/fanlinewire-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fanlinewire-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/fanlinewire-com/llms/fanlinewire-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fanlinewire-com-llms.txt
- group: build
  href: https://artifacts.apis.io/fanlinewire-com/mcp/fanlinewire-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/fanlinewire-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/fanlinewire-com/mcp/fanlinewire-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/fanlinewire-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/fanlinewire-com/hosts/fanlinewire-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fanlinewire-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/fanlinewire-com/vendors/fanlinewire-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fanlinewire-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/fanlinewire-com/security/fanlinewire-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fanlinewire-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fanlinewire.com/
- group: docs
  title: ''
  type: Documentation
  url: https://fanlinewire.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://fanlinewire.com/fanduel-api-pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://fanlinewire.com/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fanlinewire.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fanlinewire.com/privacy
created: '2026-10-30'
description: FanLine Wire provides a real-time FanDuel odds API delivering live and pre‑match moneyline, spread, totals, futures and outrights. Data is available via a push WebSocket stream and a REST discovery endpoint. The service covers all major US sports, offering comprehensive market coverage for developers building betting, analytics, or odds‑comparison applications. The API includes endpoints for board snapshots, market listings, state‑specific events, and detailed market data, with flexible authentication via API key header or query parameter. Documentation, pricing, status, and legal pages are publicly accessible.
examples:
- key_count: 3
  name: Fanlinewire Com Mcp Tools
  slug: fanlinewire-com-mcp-tools
image: https://fanlinewire.com/favicon-fanlinewire.com.png
json_schemas:
- name: GetV1BoardJsonResponse
  property_count: 7
  slug: fanlinewire-com-get-v1-board-json-response
- name: GetV1MarketsResponse
  property_count: 4
  slug: fanlinewire-com-get-v1-markets-response
- name: GetV1StateEventsResponse
  property_count: 12
  slug: fanlinewire-com-get-v1-state-events-response
- name: GetV1StateMarketsResponse
  property_count: 25
  slug: fanlinewire-com-get-v1-state-markets-response
- name: PostMcpRequest
  property_count: 4
  slug: fanlinewire-com-post-mcp-request
- name: PostMcpResponse
  property_count: 1
  slug: fanlinewire-com-post-mcp-response
jsonld:
- class_count: 7
  name: Fanlinewire Com Context
  property_count: 38
  slug: fanlinewire-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.fanlinewire.com.
  name: fanlinewire-com MCP Server
  slug: fanlinewire-com-mcp-yml
modified: '2026-10-30'
name: fanlinewire-com
nav: Providers
network: true
overview: 'fanlinewire-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Sports, Betting, Odds API, Real-Time, and FanDuel.


  The fanlinewire-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  fanlinewire-com''s developer surface includes authentication, documentation, pricing, and 16 more developer resources.'
plans:
- name: Fanlinewire Com Plans Pricing
  plan_count: 0
  slug: fanlinewire-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Fanlinewire Com Rate Limits
  slug: fanlinewire-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: fanlinewire-com API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: fanlinewire-com-rules
scopes:
- name: Fanlinewire Com Scopes
  scope_count: 0
  slug: fanlinewire-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 29
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 26.0
    developer_ergonomics: 16.7
    discoverability: 65.0
    operational_transparency: 39.5
  previous_composite: 35.3
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/fanlinewire-com/fanlinewire-com-2026-11-03T131833.png
security:
- kind: authentication
  name: Fanlinewire Com Authentication
  slug: fanlinewire-com-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Fanlinewire Com Domain Security
  slug: fanlinewire-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fanlinewire-com
tags:
- Sports
- Betting
- Odds API
- Real-Time
- FanDuel
- Data
website: https://fanlinewire.com/
---

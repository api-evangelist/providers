---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
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
    error_semantics: documented
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
  score: 23.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Real-time Pinnacle odds API (REST, WebSocket, SSE) as documented.
  name: PinnWire API
  slug: pinnwire-api
- description: 'pinnwire-com API as documented publicly: 10 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: pinnwire-com API
  slug: pinnwire-com-api
artifact_total: 14
common:
- group: operate
  href: https://artifacts.apis.io/pinnwire-com/rate-limits/pinnwire-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/pinnwire-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/pinnwire-com/plans/pinnwire-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pinnwire-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/pinnwire-com/rules/pinnwire-com-rules.yml
  title: ''
  type: Spectral
  url: rules/pinnwire-com-rules.yml
- group: design
  href: https://artifacts.apis.io/pinnwire-com/json-ld/pinnwire-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pinnwire-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/pinnwire-com/vocabulary/pinnwire-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pinnwire-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/pinnwire-com/data-model/pinnwire-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pinnwire-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/pinnwire-com/conventions/pinnwire-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pinnwire-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/pinnwire-com/authentication/pinnwire-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pinnwire-com-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://pinnwire.com/status.html
- group: design
  href: https://artifacts.apis.io/pinnwire-com/lifecycle/pinnwire-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pinnwire-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/pinnwire-com/errors/pinnwire-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pinnwire-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/pinnwire-com/conformance/pinnwire-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pinnwire-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/pinnwire-com/llms/pinnwire-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pinnwire-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/pinnwire-com/mcp/pinnwire-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/pinnwire-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/pinnwire-com/hosts/pinnwire-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pinnwire-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/pinnwire-com/vendors/pinnwire-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pinnwire-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/pinnwire-com/packages/pinnwire-com-packages.yml
  title: ''
  type: SDKs
  url: packages/pinnwire-com-packages.yml
- group: build
  href: https://artifacts.apis.io/pinnwire-com/packages/pinnwire-com-packages.yml
  title: ''
  type: Packages
  url: packages/pinnwire-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/pinnwire-com/security/pinnwire-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pinnwire-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pinnwire.com/
- group: docs
  title: ''
  type: Documentation
  url: https://pinnwire.com/docs.html
- group: docs
  title: ''
  type: APIReference
  url: https://pinnwire.com/docs.html
- group: start
  title: ''
  type: GettingStarted
  url: https://pinnwire.com/docs.html
- group: operate
  title: ''
  type: Support
  url: https://pinnwire.com/status.html
- group: company
  title: ''
  type: Blog
  url: https://pinnwire.com/blog.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PinnWire
- group: commercial
  title: ''
  type: Pricing
  url: https://pinnwire.com/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://pinnwire.com/#signup
created: '2026-10-30'
description: PinnWire provides real-time Pinnacle sportsbook odds for 13 sports via REST, WebSocket, and Server‑Sent Events (SSE) drop alerts. It offers a public demo key with no signup required, delivering live and prematch odds, recent price drops, and no‑vig fair prices on drop records. The independent, data‑only API and MCP server support developers, data scientists, and betting‑model builders with flexible pricing plans, including a free tier and paid options for higher request limits.
image: https://pinnwire.com/og-cover.png?v=2
json_schemas:
- name: GetKitV1PrematchLinesResponse
  property_count: 1
  slug: pinnwire-com-get-kit-v1-prematch-lines-response
- name: GetOddsDropPrematchResponse
  property_count: 7
  slug: pinnwire-com-get-odds-drop-prematch-response
- name: GetOddsDropResponse
  property_count: 7
  slug: pinnwire-com-get-odds-drop-response
- name: GetV1DropsResponse
  property_count: 3
  slug: pinnwire-com-get-v1-drops-response
jsonld:
- class_count: 4
  name: Pinnwire Com Context
  property_count: 10
  slug: pinnwire-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at pinnwire.com.
  name: pinnwire-com MCP Server
  slug: pinnwire-com-mcp-yml
modified: '2026-10-30'
name: pinnwire-com
nav: Providers
network: true
overview: 'pinnwire-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sports, Betting, Odds, and Real-Time.


  The pinnwire-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  pinnwire-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 21 more developer resources.'
plans:
- name: Pinnwire Com Plans Pricing
  plan_count: 5
  slug: pinnwire-com-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Pinnwire Com Rate Limits
  slug: pinnwire-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: pinnwire-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: pinnwire-com-rules
scopes:
- name: Pinnwire Com Scopes
  scope_count: 0
  slug: pinnwire-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 78.8
    catalog_earned_first_party: 24.0
    catalog_gap: 36.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.3
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 22.1
    developer_ergonomics: 36.9
    discoverability: 56.7
    operational_transparency: 42.1
  previous_composite: 44.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/pinnwire-com/pinnwire-com-2026-11-03T141243.png
security:
- kind: authentication
  name: Pinnwire Com Authentication
  slug: pinnwire-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Pinnwire Com Domain Security
  slug: pinnwire-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pinnwire-com
tags:
- Company
- Sports
- Betting
- Odds
- Real-Time
website: https://pinnwire.com/
---

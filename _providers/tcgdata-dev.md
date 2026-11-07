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
    agent_skills: unknown
    agentic_access: derived
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Tcgdata Dev Agentic Access
  operation_count: 17
  slug: tcgdata-dev-agentic-access
  summary_line: 17 operations · 1 acting
api_count: 1
apis:
- description: 'tcgdata-dev API as documented publicly: 15 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: tcgdata-dev API
  slug: tcgdata-dev-api
artifact_total: 24
common:
- group: commercial
  href: https://artifacts.apis.io/tcgdata-dev/plans/tcgdata-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tcgdata-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/tcgdata-dev/rules/tcgdata-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/tcgdata-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/tcgdata-dev/json-ld/tcgdata-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tcgdata-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/tcgdata-dev/vocabulary/tcgdata-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tcgdata-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/tcgdata-dev/data-model/tcgdata-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tcgdata-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/tcgdata-dev/conventions/tcgdata-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tcgdata-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/tcgdata-dev/conformance/tcgdata-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tcgdata-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tcgdata-dev/llms/tcgdata-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tcgdata-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/tcgdata-dev/mcp/tcgdata-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tcgdata-dev-mcp.yml
- group: other
  href: https://artifacts.apis.io/tcgdata-dev/hosts/tcgdata-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tcgdata-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/tcgdata-dev/vendors/tcgdata-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tcgdata-dev-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://tcgdata.dev/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://tcgdata.dev/changelog
- group: auth
  href: https://artifacts.apis.io/tcgdata-dev/security/tcgdata-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tcgdata-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tcgdata.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://tcgdata.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://tcgdata.dev/api-reference
- group: commercial
  title: ''
  type: Pricing
  url: https://tcgdata.dev/pricing
- group: company
  title: ''
  type: Blog
  url: https://tcgdata.dev/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tcgdata.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tcgdata.dev/privacy
- group: start
  title: ''
  type: SignUp
  url: https://tcgdata.dev/signup
- group: start
  title: ''
  type: Login
  url: https://tcgdata.dev/login
created: '2026-10-31'
description: TCGData.dev provides a unified API for pricing and historical data of trading card games (TCGs) in Europe. It covers popular games such as Pokémon, Magic, Lorcana, One Piece, and Yu‑Gi‑Oh!, offering real‑time price lookups, trend analysis, and batch data retrieval. The service includes free tier access with 500 calls for 30 days and detailed documentation for developers to integrate pricing data into apps, marketplaces, and analytics platforms.
image: https://tcgdata.dev/icon-512.png
json_schemas:
- name: BatchResponse
  property_count: 2
  slug: tcgdata-dev-batch-response
- name: CatalogueCardList
  property_count: 2
  slug: tcgdata-dev-catalogue-card-list
- name: CatalogueSetList
  property_count: 2
  slug: tcgdata-dev-catalogue-set-list
- name: CatalogueVariantRecordList
  property_count: 2
  slug: tcgdata-dev-catalogue-variant-record-list
- name: GetV1CardsIdHistoryResponse
  property_count: 26
  slug: tcgdata-dev-get-v1-cards-id-history-response
- name: GetV1CardsIdPricesResponse
  property_count: 24
  slug: tcgdata-dev-get-v1-cards-id-prices-response
- name: GetV1CardsIdResponse
  property_count: 12
  slug: tcgdata-dev-get-v1-cards-id-response
- name: GetV1CatalogSetsResponse
  property_count: 6
  slug: tcgdata-dev-get-v1-catalog-sets-response
- name: GetV1UsageResponse
  property_count: 30
  slug: tcgdata-dev-get-v1-usage-response
- name: PostV1PricesBatchRequest
  property_count: 3
  slug: tcgdata-dev-post-v1-prices-batch-request
- name: ReadableCardList
  property_count: 2
  slug: tcgdata-dev-readable-card-list
- name: UsageResponse
  property_count: 2
  slug: tcgdata-dev-usage-response
jsonld:
- class_count: 16
  name: Tcgdata Dev Context
  property_count: 81
  slug: tcgdata-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at tcgdata.dev requiring an API key.
  name: tcgdata-dev MCP Server
  slug: tcgdata-dev-mcp-yml
modified: '2026-10-31'
name: tcgdata-dev
nav: Providers
network: true
overview: 'tcgdata-dev publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Trading Cards, Pricing, and Europe.


  The tcgdata-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  tcgdata-dev''s developer surface includes changelog, documentation, API reference, pricing, engineering blog, signup flow, and 17 more developer resources.'
plans:
- name: Tcgdata Dev Plans Pricing
  plan_count: 4
  slug: tcgdata-dev-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Tcgdata Dev Rate Limits
  slug: tcgdata-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: tcgdata-dev API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: tcgdata-dev-rules
scopes:
- name: Tcgdata Dev Scopes
  scope_count: 0
  slug: tcgdata-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.0
  coverage:
    artifact_dirs: 34
    catalog_earned: 72.8
    catalog_earned_first_party: 20.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.8
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 46.5
    developer_ergonomics: 9.5
    discoverability: 48.3
    operational_transparency: 36.8
  previous_composite: 46.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 88.9
      derived: 1
      marker_coverage: 11.1
      total: 9
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tcgdata-dev/tcgdata-dev-2026-11-03T144342.png
security:
- kind: authentication
  name: Tcgdata Dev Authentication
  slug: tcgdata-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Tcgdata Dev Domain Security
  slug: tcgdata-dev-domain-security
  summary_line: TLSv1.3
skill_count: 2
skills:
- name: list-games
  slug: tcgdata-dev-list-games
- name: search-cards
  slug: tcgdata-dev-search-cards
slug: tcgdata-dev
tags:
- Company
- Trading Cards
- Pricing
- Europe
website: https://tcgdata.dev/
---

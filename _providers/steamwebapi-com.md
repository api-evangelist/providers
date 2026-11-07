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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Complete Steam API documentation with live examples. Access Steam Market prices, player inventories, game data and more.
  name: SteamWebAPI
  slug: steamwebapi
- description: 'steamwebapi-com API as documented publicly: 73 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: steamwebapi-com API
  slug: steamwebapi-com-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/steamwebapi-com/rules/steamwebapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/steamwebapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/steamwebapi-com/json-ld/steamwebapi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/steamwebapi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/steamwebapi-com/vocabulary/steamwebapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/steamwebapi-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/steamwebapi-com/data-model/steamwebapi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/steamwebapi-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/steamwebapi-com/authentication/steamwebapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/steamwebapi-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/steamwebapi-com/conformance/steamwebapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/steamwebapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/steamwebapi-com/llms/steamwebapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/steamwebapi-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/steamwebapi-com/well-known/steamwebapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/steamwebapi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/steamwebapi-com/hosts/steamwebapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/steamwebapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/steamwebapi-com/vendors/steamwebapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/steamwebapi-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/steamwebapi-com/packages/steamwebapi-com-packages.yml
  title: ''
  type: SDKs
  url: packages/steamwebapi-com-packages.yml
- group: build
  href: https://artifacts.apis.io/steamwebapi-com/packages/steamwebapi-com-packages.yml
  title: ''
  type: Packages
  url: packages/steamwebapi-com-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.steamwebapi.com/trust
- group: company
  title: ''
  type: Blog
  url: https://www.steamwebapi.com/blog/cs2-items-price-api
- group: docs
  title: ''
  type: APIReference
  url: https://www.steamwebapi.com/llms-full.txt
- group: auth
  href: https://artifacts.apis.io/steamwebapi-com/security/steamwebapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/steamwebapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://steamwebapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.steamwebapi.com/api/steam/documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://www.steamwebapi.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.steamwebapi.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.steamwebapi.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.steamwebapi.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/steamwebapi
coverage:
  checked: '2026-10-31'
  detail: Documentation is publicly readable but provides no OpenAPI, AsyncAPI, GraphQL SDL, or other machine‑readable specification.
  evidence:
  - status: 200
    url: https://www.steamwebapi.com/api/steam/documentation
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: SteamWebAPI.com is a third‑party Steam market, inventory, profile, float and trade API provider, not Valve’s official Steam Web API. It offers production‑ready CS2 skin prices, Rust/Dota/TF2 market data, third‑party marketplace prices, Steam inventories, profile enrichment, float values, trade offer automation and Steam Guard workflows without building direct Steam scraping, marketplace scraping or handling Steam 429 rate‑limit errors. LLM and agent resources are available via llms.txt and related docs.
image: http://www.steamwebapi.com/images/og/og-default.png
json_schemas:
- name: GetApiAssetsResponse
  property_count: 5
  slug: steamwebapi-com-get-api-assets-response
- name: GetSteamApiItemsPreviewResponse
  property_count: 6
  slug: steamwebapi-com-get-steam-api-items-preview-response
- name: PostSteamApiItemsHistoryRequest
  property_count: 4
  slug: steamwebapi-com-post-steam-api-items-history-request
- name: PostSteamApiSteamloginsecureRequest
  property_count: 4
  slug: steamwebapi-com-post-steam-api-steamloginsecure-request
- name: PostSteamApiTradeCreateRequest
  property_count: 6
  slug: steamwebapi-com-post-steam-api-trade-create-request
- name: PutSteamApiTradeAcceptRequest
  property_count: 3
  slug: steamwebapi-com-put-steam-api-trade-accept-request
jsonld:
- class_count: 26
  name: Steamwebapi Com Context
  property_count: 31
  slug: steamwebapi-com-context
layout: provider
modified: '2026-10-31'
name: steamwebapi-com
nav: Providers
network: true
overview: 'steamwebapi-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Steam, Gaming, Marketplace, and Inventory.


  The steamwebapi-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  steamwebapi-com''s developer surface includes authentication, engineering blog, API reference, documentation, pricing, and 18 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: steamwebapi-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: steamwebapi-com-rules
scopes:
- name: Steamwebapi Com Scopes
  scope_count: 0
  slug: steamwebapi-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.4
  coverage:
    artifact_dirs: 27
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.1
  facets:
    access_clarity: 19.7
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 28.6
    discoverability: 48.2
    operational_transparency: 10.5
  previous_composite: 36.5
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
    score: 32.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/steamwebapi-com/steamwebapi-com-2026-11-03T143812.png
security:
- kind: authentication
  name: Steamwebapi Com Authentication
  slug: steamwebapi-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Steamwebapi Com Domain Security
  slug: steamwebapi-com-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: steamwebapi-com
tags:
- Steam
- Gaming
- Marketplace
- Inventory
website: https://steamwebapi.com/
---

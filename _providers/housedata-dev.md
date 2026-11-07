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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: HouseData provides a read‑only Zillow data API delivering listings, Zestimate histories, agent info, market stats, and mortgage rates.
  name: HouseData API
  slug: housedata-api
- description: 'housedata-dev API as documented publicly: 21 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: housedata-dev API
  slug: housedata-dev-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/housedata-dev/rules/housedata-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/housedata-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/housedata-dev/json-ld/housedata-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/housedata-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/housedata-dev/vocabulary/housedata-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/housedata-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/housedata-dev/data-model/housedata-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/housedata-dev-data-model.yml
- group: auth
  href: https://artifacts.apis.io/housedata-dev/authentication/housedata-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/housedata-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/housedata-dev/conformance/housedata-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/housedata-dev-conformance.yml
- group: other
  href: https://artifacts.apis.io/housedata-dev/hosts/housedata-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/housedata-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/housedata-dev/vendors/housedata-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/housedata-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/housedata-dev/security/housedata-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/housedata-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://housedata.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://housedata.dev/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://housedata.dev/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://housedata.dev/docs/
- group: operate
  title: ''
  type: Support
  url: https://housedata.dev/status/
- group: operate
  title: ''
  type: StatusPage
  url: https://housedata.dev/status/
- group: commercial
  title: ''
  type: Pricing
  url: https://rapidapi.com/bachhungcong/api/zillow-full-data-api/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://housedata.dev/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://housedata.dev/privacy/
coverage:
  checked: '2026-10-30'
  detail: Documentation is publicly readable but provides no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable specification.
  evidence:
  - status: 200
    url: https://housedata.dev/docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: HouseData provides a read‑only Zillow data API that delivers listings for sale, rent, or sold properties across the United States. It returns full property records, Zestimate histories, agent information, market statistics, and mortgage rates in clean JSON format. Users can access the API via RapidAPI, Apify, or private MCP keys, with tiered pricing plans ranging from a free tier to enterprise volumes. The service is public, requires no login, and is not affiliated with Zillow.
image: https://housedata.dev/opengraph-image.png?opengraph-image.1m83t3ixt32wx.png
json_schemas:
- name: GetPropertyAgentResponse
  property_count: 13
  slug: housedata-dev-get-property-agent-response
- name: GetPropertyFactsResponse
  property_count: 21
  slug: housedata-dev-get-property-facts-response
- name: GetPropertyTopAgentsResponse
  property_count: 13
  slug: housedata-dev-get-property-top-agents-response
- name: PostPropertyResponse
  property_count: 20
  slug: housedata-dev-post-property-response
- name: PostSearchRequest
  property_count: 8
  slug: housedata-dev-post-search-request
- name: PostSearchResponse
  property_count: 10
  slug: housedata-dev-post-search-response
jsonld:
- class_count: 23
  name: Housedata Dev Context
  property_count: 121
  slug: housedata-dev-context
layout: provider
modified: '2026-10-30'
name: housedata-dev
nav: Providers
network: true
overview: 'housedata-dev is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Zillow, Data API, US, and Property.


  The housedata-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  housedata-dev''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, and 12 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: housedata-dev API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: housedata-dev-rules
scopes:
- name: Housedata Dev Scopes
  scope_count: 0
  slug: housedata-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.1
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 34.8
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
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/housedata-dev/housedata-dev-2026-11-03T133502.png
security:
- kind: authentication
  name: Housedata Dev Authentication
  slug: housedata-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Housedata Dev Domain Security
  slug: housedata-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: housedata-dev
tags:
- Real Estate
- Zillow
- Data API
- US
- Property
website: https://housedata.dev/
---

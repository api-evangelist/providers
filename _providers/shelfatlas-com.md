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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Shelfatlas Com Agentic Access
  operation_count: 24
  slug: shelfatlas-com-agentic-access
  summary_line: 24 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.shelfatlas.com
  baseurl_source: declared
  description: The Chains API from shelfatlas-com — 1 operation(s) for chains.
  name: shelfatlas-com Chains API
  slug: shelfatlas-com-chains-api
- baseURL: https://api.shelfatlas.com
  baseurl_source: declared
  description: The MCP API from shelfatlas-com — 1 operation(s) for mcp.
  name: shelfatlas-com MCP API
  slug: shelfatlas-com-mcp-api
- baseURL: https://api.shelfatlas.com
  baseurl_source: declared
  description: The Observations API from shelfatlas-com — 3 operation(s) for observations.
  name: shelfatlas-com Observations API
  slug: shelfatlas-com-observations-api
- baseURL: https://api.shelfatlas.com
  baseurl_source: declared
  description: The ObservedPrices API from shelfatlas-com — 1 operation(s) for observedprices.
  name: shelfatlas-com Observed Prices API
  slug: shelfatlas-com-observedprices-api
- baseURL: https://api.shelfatlas.com
  baseurl_source: declared
  description: The Offers API from shelfatlas-com — 8 operation(s) for offers.
  name: shelfatlas-com Offers API
  slug: shelfatlas-com-offers-api
- baseURL: https://api.shelfatlas.com
  baseurl_source: declared
  description: The Price history API from shelfatlas-com — 1 operation(s) for price history.
  name: shelfatlas-com Price history API
  slug: shelfatlas-com-price-history-api
- baseURL: https://api.shelfatlas.com
  baseurl_source: declared
  description: The Products API from shelfatlas-com — 3 operation(s) for products.
  name: shelfatlas-com Products API
  slug: shelfatlas-com-products-api
- baseURL: https://api.shelfatlas.com
  baseurl_source: declared
  description: The SeoTerms API from shelfatlas-com — 1 operation(s) for seoterms.
  name: shelfatlas-com Seo Terms API
  slug: shelfatlas-com-seoterms-api
- baseURL: https://api.shelfatlas.com
  baseurl_source: declared
  description: The Stats API from shelfatlas-com — 1 operation(s) for stats.
  name: shelfatlas-com Stats API
  slug: shelfatlas-com-stats-api
- baseURL: https://api.shelfatlas.com
  baseurl_source: declared
  description: The Stores API from shelfatlas-com — 5 operation(s) for stores.
  name: shelfatlas-com Stores API
  slug: shelfatlas-com-stores-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/shelfatlas-com/agentic-access/shelfatlas-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/shelfatlas-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/shelfatlas-com/rules/shelfatlas-com-rules.yml
  title: ''
  type: Spectral
  url: rules/shelfatlas-com-rules.yml
- group: design
  href: https://artifacts.apis.io/shelfatlas-com/json-ld/shelfatlas-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/shelfatlas-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/shelfatlas-com/vocabulary/shelfatlas-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/shelfatlas-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/shelfatlas-com/data-model/shelfatlas-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/shelfatlas-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/shelfatlas-com/errors/shelfatlas-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/shelfatlas-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/shelfatlas-com/conformance/shelfatlas-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/shelfatlas-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/shelfatlas-com/llms/shelfatlas-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shelfatlas-com-llms.txt
- group: other
  href: https://artifacts.apis.io/shelfatlas-com/hosts/shelfatlas-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shelfatlas-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/shelfatlas-com/vendors/shelfatlas-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/shelfatlas-com-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://shelfatlas.com/app/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shelfatlas.com/legal/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://shelfatlas.com/status
- group: start
  title: ''
  type: SignUp
  url: https://shelfatlas.com/sign-up?redirect_url=/auth/redirect
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shelfatlas.com/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://shelfatlas.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://docs.shelfatlas.com/
- group: docs
  title: ''
  type: APIReference
  url: https://shelfatlas.com/docs
- group: auth
  href: https://artifacts.apis.io/shelfatlas-com/authentication/shelfatlas-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/shelfatlas-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/shelfatlas-com/security/shelfatlas-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shelfatlas-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shelfatlas.com/
created: '2026-10-31'
description: ShelfAtlas provides a Danish grocery catalog and price data API, aggregating offers from over 20 chains such as Netto, Rema 1000, Føtex, Bilka, and Lidl. The service offers REST endpoints and webhooks delivering real‑time shelf intelligence, enabling businesses to replace manual spreadsheet tracking with up‑to‑date product, pricing, and store information across Denmark.
image: https://shelfatlas.com/opengraph-image
json_schemas:
- name: NearbyLocalPrices
  property_count: 2
  slug: shelfatlas-com-nearby-local-prices
- name: OfferHistorySummary
  property_count: 5
  slug: shelfatlas-com-offer-history-summary
- name: Offer
  property_count: 23
  slug: shelfatlas-com-offer
- name: PriceDrop
  property_count: 25
  slug: shelfatlas-com-price-drop
- name: TermHistorySummary
  property_count: 14
  slug: shelfatlas-com-term-history-summary
- name: TermHistoryWeek
  property_count: 12
  slug: shelfatlas-com-term-history-week
jsonld:
- class_count: 35
  name: Shelfatlas Com Context
  property_count: 185
  slug: shelfatlas-com-context
layout: provider
modified: '2026-10-31'
name: shelfatlas-com
nav: Providers
network: true
overview: 'shelfatlas-com publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Chains API, MCP API, Observations API, and 7 more. Tagged areas include Company, Grocery, Denmark, and Retail.


  The shelfatlas-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  shelfatlas-com''s developer surface includes signup flow, pricing, documentation, API reference, authentication, and 16 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: shelfatlas-com API Rules
  rule_count: 18
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 3
  slug: shelfatlas-com-rules
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.2
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 61.6
    developer_ergonomics: 20.2
    discoverability: 57.1
    operational_transparency: 11.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - denmark
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 43.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
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
screenshot: https://apis.io/screenshots/shelfatlas-com/shelfatlas-com-2026-11-03T143122.png
security:
- kind: authentication
  name: Shelfatlas Com Authentication
  slug: shelfatlas-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Shelfatlas Com Domain Security
  slug: shelfatlas-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: shelfatlas-com
tags:
- Company
- Grocery
- Denmark
- Retail
website: https://shelfatlas.com/
---

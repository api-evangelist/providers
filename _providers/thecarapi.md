---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-09-16'
api_count: 1
apis:
- baseURL: https://api.thecarapi.com
  baseurl_source: declared
  description: Retrieve source-aware listing detail, galleries, price changes, and VIN history. A running openlane or ecarstrade auction has its bid read from the auction house at the moment you request the detail —
  name: TheCarApi Auctions & history API
  slug: thecarapi-auctions-history-api
- baseURL: https://api.thecarapi.com
  baseurl_source: declared
  description: Build slug-addressable manufacturer and model-group navigation. All catalog list routes paginate with a default limit of 50 and are capped at offset 5000 — a deeper page is a 400 naming the limit. The
  name: TheCarApi Catalog API
  slug: thecarapi-catalog-api
- baseURL: https://api.thecarapi.com
  baseurl_source: declared
  description: 'A retail price surface of roughly 9.8M live listings gathered from 681 origin portals — national classifieds sites, dealer groups and manufacturer stock pages — across 39 European countries: mobile.de'
  name: TheCarApi European classifieds API
  slug: thecarapi-european-classifieds-api
- baseURL: https://api.thecarapi.com
  baseurl_source: declared
  description: Discover live filter values and counts. Every facet endpoint accepts the search filters, so a facet describes whatever slice of inventory you are looking at rather than the whole of it — each dimensio
  name: TheCarApi Filter facets API
  slug: thecarapi-filter-facets-api
- baseURL: https://api.thecarapi.com
  baseurl_source: declared
  description: Check service dependencies and inspect the API index.
  name: TheCarApi Health & contract API
  slug: thecarapi-health-contract-api
- baseURL: https://api.thecarapi.com
  baseurl_source: declared
  description: Estimate the landed cost of importing a vehicle. These are estimates, not a binding quote.
  name: TheCarApi Import calculator API
  slug: thecarapi-import-calculator-api
- baseURL: https://api.thecarapi.com
  baseurl_source: declared
  description: 'Precomputed price snapshots for a brand, model, and year window — one for the Bulgarian retail market, one for our own auction inventory. Scope: market. Neither is enabled on a new key by default; ask'
  name: TheCarApi Market intelligence API
  slug: thecarapi-market-intelligence-api
- baseURL: https://api.thecarapi.com
  baseurl_source: declared
  description: Build popular landing pages and resolve brand/model URL slugs.
  name: TheCarApi SEO helpers API
  slug: thecarapi-seo-helpers-api
- baseURL: https://api.thecarapi.com
  baseurl_source: declared
  description: Live auctions our pipeline judged to be priced below their market reference. Same deals as /api/search?sort=top_offers, but each card additionally carries the reference the verdict was made against.
  name: TheCarApi Top offers API
  slug: thecarapi-top-offers-api
- baseURL: https://api.thecarapi.com
  baseurl_source: declared
  description: Fetch a full source payload from cache or, when needed, from the upstream source.
  name: TheCarApi Vehicle details API
  slug: thecarapi-vehicle-details-api
- baseURL: https://api.thecarapi.com
  baseurl_source: declared
  description: Search live auction inventory, then resolve lightweight full-text matches. Ended lots are hidden by default; is_active=false / include_ended=true shows them as well as live ones.
  name: TheCarApi Search and Discovery API
  slug: thecarapi-search-and-discovery-api
artifact_total: 16
common:
- group: company
  title: ''
  type: Website
  url: https://thecarapi.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thecarapi/refs/heads/main/security/thecarapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thecarapi-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thecarapi/refs/heads/main/authentication/thecarapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/thecarapi-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thecarapi/refs/heads/main/scopes/thecarapi-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/thecarapi-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thecarapi/refs/heads/main/conventions/thecarapi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/thecarapi-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thecarapi/refs/heads/main/errors/thecarapi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/thecarapi-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thecarapi/refs/heads/main/lifecycle/thecarapi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/thecarapi-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://thecarapi.com/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://thecarapi.com/changelog
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/thecarapi/refs/heads/main/changelog/thecarapi-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/thecarapi-changelog.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/thecarapi/refs/heads/main/plans/thecarapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/thecarapi-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://thecarapi.com/pricing
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/thecarapi/refs/heads/main/rate-limits/thecarapi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/thecarapi-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thecarapi/refs/heads/main/conformance/thecarapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/thecarapi-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thecarapi/refs/heads/main/vocabulary/thecarapi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/thecarapi-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: https://thecarapi.com/docs/code-examples
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/thecarapi/refs/heads/main/examples/thecarapi-examples.yml
  title: ''
  type: Examples
  url: examples/thecarapi-examples.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thecarapi/refs/heads/main/data-model/thecarapi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/thecarapi-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thecarapi/refs/heads/main/overlays/thecarapi-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thecarapi-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/thecarapi/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: https://thecarapi.com/llms.txt
- group: build
  title: ''
  type: Postman
  url: https://thecarapi.com/thecarapi.postman_collection.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://thecarapi.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://thecarapi.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://thecarapi.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://thecarapi.com/docs/thecarapi-api-reference.md
- group: operate
  title: ''
  type: Support
  url: https://thecarapi.com/contact
- group: company
  title: ''
  type: Blog
  url: https://thecarapi.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thecarapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thecarapi.com/privacy
created: '2026-09-01'
description: A multi-source vehicle auction inventory REST/JSON API aggregating live and archived auction listings and European retail classifieds. Provides search, facets, catalog, auction detail & price history, VIN history, market intelligence, and import cost calculators. Fully specified via OpenAPI 3.1 with Postman collection and agent-native documentation (llms.txt).
image: https://thecarapi.com/og-image.png
layout: provider
modified: '2026-09-02'
name: TheCarApi
nav: Providers
network: true
overview: 'TheCarApi publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Auctions & history API, Catalog API, European classifieds API, and 8 more. Tagged areas include Automotive, Vehicle Data, Car Auctions, Used Cars, and Vehicle Inventory.


  TheCarApi''s developer surface includes authentication, changelog, pricing, code examples, documentation, getting-started guide, API reference, and 23 more developer resources.'
plans:
- name: Thecarapi Plans Pricing
  plan_count: 3
  slug: thecarapi-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 3
  name: Thecarapi Rate Limits
  slug: thecarapi-rate-limits
scopes:
- name: Thecarapi Scopes
  scope_count: 0
  slug: thecarapi-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 57.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 62.3
    catalog_earned_first_party: 24.0
    catalog_gap: 52.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.6
  facets:
    access_clarity: 63.2
    contract_governance: 8.3
    contract_quality: 62.6
    developer_ergonomics: 63.7
    discoverability: 75.9
    operational_transparency: 63.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - japan-korea
  previous_composite: 51.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/thecarapi/refs/heads/main/screenshots/thecarapi-2026-09-02T163425.png
security:
- kind: authentication
  name: Thecarapi Authentication
  slug: thecarapi-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Thecarapi Domain Security
  slug: thecarapi-domain-security
  summary_line: TLSv1.3
slug: thecarapi
tags:
- Automotive
- Vehicle Data
- Car Auctions
- Used Cars
- Vehicle Inventory
- Classifieds
- Market Intelligence
- Pricing
- VIN
- Image CDN
- Europe
- South Korea
- Japan Auctions
website: https://thecarapi.com/
---

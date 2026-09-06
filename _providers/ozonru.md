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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: RPC-over-HTTP JSON API for OZON marketplace sellers to manage products, prices, stock, warehouses, orders (FBO/FBS), returns, analytics, and finances. POST-only endpoints under a per-operation version
  name: OZON Seller API
  slug: ozon-seller-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: http://ozon.ru
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ozon.ru/api/seller/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ozon.ru/api/seller/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/ozonru-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ozonru-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: security/ozonru-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ozonru-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ozonru-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/ozonru-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ozonru-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ozonru-llms.txt
created: '2026-07-17'
description: OZON is one of Russia's largest e-commerce marketplaces, offering retail across electronics, apparel, groceries, and more, plus its own logistics and fulfillment network (FBO/FBS). For developers, OZON exposes the OZON Seller API, a POST-based RPC-over-HTTP JSON API at https://api-seller.ozon.ru that lets marketplace sellers manage products, prices, stock, warehouses, orders, returns, analytics, and finances programmatically. Authentication uses two headers, a numeric Client-Id and a secret Api-Key issued in the seller cabinet. OZON was surfaced as a portfolio company of Index Ventures and enriched by the API Evangelist pipeline from live probes of its API host and public developer documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ozonru.png
layout: provider
modified: '2026-07-20'
name: OZON.ru
nav: Providers
network: true
overview: 'OZON.ru publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Marketplace, and Seller API.


  OZON.ru''s developer surface includes documentation and 10 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 14.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - russia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 14.8
  provenance:
    conformance: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Ozonru Authentication
  slug: ozonru-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ozonru Domain Security
  slug: ozonru-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Ozonru Vulnerability Disclosure
  slug: ozonru-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ozonru
tags:
- Company
- Retail
- E-Commerce
- Marketplace
- Seller API
- Russia
- Logistics
website: http://ozon.ru
---

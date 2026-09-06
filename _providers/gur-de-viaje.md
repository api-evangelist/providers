---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gur-de-viaje-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gurudeviaje.com
created: '2026-07-17'
description: Gurú de Viaje is a Mexico-based travel-deals company and flight-deal hunter ("cazador de ofertas de viaje") that publishes daily cheap-flight promotions and airfare offers so travelers can fly cheaply and see the world. Its Spanish-language consumer website and mobile/push experience surface daily discounted airline tickets and travel promotions, with a focus on departures from Mexican cities such as Guadalajara and Mexico City. Surfaced as a portfolio company of 500 Global and added to the API Evangelist network. As of this pass Gurú de Viaje operates a consumer Next.js web property (gurudeviaje.com) and publishes no public developer program, API reference, or machine-readable API specification.
image: https://gurudeviaje.com/favicon.ico
layout: provider
modified: '2026-07-19'
name: Gurú de Viaje
nav: Providers
network: true
overview: Gurú de Viaje is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Flights, Travel Deals, and Airfare.
random_paper: 18
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - mexico
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gur-de-viaje/refs/heads/main/screenshots/gur-de-viaje-2026-07-25T220437.png
security:
- kind: domain-security
  name: Gur De Viaje Domain Security
  slug: gur-de-viaje-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: gur-de-viaje
tags:
- Company
- Travel
- Flights
- Travel Deals
- Airfare
- Mexico
- Consumer
website: https://gurudeviaje.com
---

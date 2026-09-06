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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: CKAN API for University of Bologna Open Data, ~34 datasets.
  name: University of Bologna Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dati-unibo-it-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dati.unibo.it
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/dati-unibo-it-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dati-unibo-it-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dati-unibo-it-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: University of Bologna Open Data is a university open-data portal for Italy running CKAN. It exposes the CKAN catalog API over approximately 34 datasets.
finops:
- name: Dati Unibo It Finops
  service_category: ''
  slug: dati-unibo-it-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dati-unibo-it.png
layout: provider
modified: '2026-06-07'
name: University of Bologna Open Data
nav: Providers
network: true
overview: 'University of Bologna Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and University Data.


  University of Bologna Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Dati Unibo It Plans Pricing
  plan_count: 0
  slug: dati-unibo-it-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Dati Unibo It Rate Limits
  slug: dati-unibo-it-rate-limits
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - italy
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - italy-southern-europe
  previous_composite: 6.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dati-unibo-it/refs/heads/main/screenshots/dati-unibo-it-2026-06-20T175707.png
security:
- kind: domain-security
  name: Dati Unibo It Domain Security
  slug: dati-unibo-it-domain-security
  summary_line: TLSv1.2 · DMARC
slug: dati-unibo-it
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- University Data
- University
- Italy
website: https://dati.unibo.it
---

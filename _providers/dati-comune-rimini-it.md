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
- description: CKAN Action API for Rimini Open Data, ~72 datasets.
  name: Rimini Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dati-comune-rimini-it-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dati.comune.rimini.it
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/dati-comune-rimini-it-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dati-comune-rimini-it-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dati-comune-rimini-it-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Rimini Open Data is a municipal government open-data portal for Italy running CKAN. It exposes the CKAN catalog API over approximately 72 datasets.
finops:
- name: Dati Comune Rimini It Finops
  service_category: ''
  slug: dati-comune-rimini-it-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dati-comune-rimini-it.png
layout: provider
modified: '2026-06-07'
name: Rimini Open Data
nav: Providers
network: true
overview: 'Rimini Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Rimini Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Dati Comune Rimini It Plans Pricing
  plan_count: 0
  slug: dati-comune-rimini-it-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Dati Comune Rimini It Rate Limits
  slug: dati-comune-rimini-it-rate-limits
score:
  band: minimal
  composite: 7.8
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
  previous_composite: 7.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dati-comune-rimini-it/refs/heads/main/screenshots/dati-comune-rimini-it-2026-06-20T175658.png
security:
- kind: domain-security
  name: Dati Comune Rimini It Domain Security
  slug: dati-comune-rimini-it-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dati-comune-rimini-it
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Municipal Government
- Italy
website: https://dati.comune.rimini.it
---

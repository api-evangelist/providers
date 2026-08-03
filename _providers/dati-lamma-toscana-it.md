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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: CKAN Action API for LAMMA Toscana Open Data, ~184 datasets.
  name: LAMMA Toscana Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dati-lamma-toscana-it-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dati.lamma.toscana.it
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/dati-lamma-toscana-it-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dati-lamma-toscana-it-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dati-lamma-toscana-it-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: LAMMA Toscana Open Data is a government agency open-data portal for Italy running CKAN. It exposes the CKAN catalog API over approximately 184 datasets from Tuscany's meteorological and environmental research agency.
finops:
- name: Dati Lamma Toscana It Finops
  service_category: ''
  slug: dati-lamma-toscana-it-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dati-lamma-toscana-it.png
layout: provider
modified: '2026-06-07'
name: LAMMA Toscana Open Data
nav: Providers
network: true
overview: 'LAMMA Toscana Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  LAMMA Toscana Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Dati Lamma Toscana It Plans Pricing
  plan_count: 0
  slug: dati-lamma-toscana-it-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 0
  name: Dati Lamma Toscana It Rate Limits
  slug: dati-lamma-toscana-it-rate-limits
score:
  band: minimal
  composite: 10.3
  delta: 0.0
  facets:
    commercial_clarity: 7.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dati-lamma-toscana-it/refs/heads/main/screenshots/dati-lamma-toscana-it-2026-06-20T175701.png
security:
- kind: domain-security
  name: Dati Lamma Toscana It Domain Security
  slug: dati-lamma-toscana-it-domain-security
  summary_line: no transport/DNS hardening detected
slug: dati-lamma-toscana-it
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Government Agency
- Italy
website: https://dati.lamma.toscana.it
---

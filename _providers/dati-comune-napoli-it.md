---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: CKAN Action API for Naples Open Data, ~36 datasets. Base URL https://dati.comune.napoli.it/api/3/action/.
  name: Naples Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dati-comune-napoli-it-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dati.comune.napoli.it
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/dati-comune-napoli-it-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dati-comune-napoli-it-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dati-comune-napoli-it-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Naples Open Data is a municipal government open-data portal for Italy running CKAN. It exposes the CKAN catalog API over approximately 36 datasets.
finops:
- name: Dati Comune Napoli It Finops
  service_category: ''
  slug: dati-comune-napoli-it-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dati-comune-napoli-it.png
layout: provider
modified: '2026-06-07'
name: Naples Open Data
nav: Providers
network: true
overview: 'Naples Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Naples Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Dati Comune Napoli It Plans Pricing
  plan_count: 1
  slug: dati-comune-napoli-it-plans-pricing
random_paper: 92
rate_limits:
- limit_count: 0
  name: Dati Comune Napoli It Rate Limits
  slug: dati-comune-napoli-it-rate-limits
score:
  band: emerging
  composite: 13.1
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dati-comune-napoli-it/refs/heads/main/screenshots/dati-comune-napoli-it-2026-06-20T175659.png
security:
- kind: domain-security
  name: Dati Comune Napoli It Domain Security
  slug: dati-comune-napoli-it-domain-security
  summary_line: TLSv1.2 · HSTS
slug: dati-comune-napoli-it
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- Municipal Government
- Italy
website: https://dati.comune.napoli.it
---

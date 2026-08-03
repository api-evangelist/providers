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
random_paper: 35
rate_limits:
- limit_count: 0
  name: Dati Unibo It Rate Limits
  slug: dati-unibo-it-rate-limits
score:
  band: minimal
  composite: 9.5
  delta: 0.0
  facets:
    commercial_clarity: 7.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.9
  scored_at: '2026-08-03'
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

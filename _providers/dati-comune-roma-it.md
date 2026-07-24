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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: CKAN API for Rome Open Data, ~365 datasets.
  name: Rome Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dati-comune-roma-it-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dati.comune.roma.it/catalog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/dati-comune-roma-it-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dati-comune-roma-it-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dati-comune-roma-it-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Rome Open Data is a municipal government open-data portal for Italy running CKAN. It exposes the CKAN catalog API over approximately 365 datasets.
finops:
- name: Dati Comune Roma It Finops
  service_category: ''
  slug: dati-comune-roma-it-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dati-comune-roma-it.png
layout: provider
modified: '2026-06-07'
name: Rome Open Data
nav: Providers
network: true
overview: 'Rome Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Rome Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Dati Comune Roma It Plans Pricing
  plan_count: 0
  slug: dati-comune-roma-it-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Dati Comune Roma It Rate Limits
  slug: dati-comune-roma-it-rate-limits
score:
  band: minimal
  composite: 11.6
  delta: 0.3
  facets:
    commercial_clarity: 7.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.3
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dati-comune-roma-it/refs/heads/main/screenshots/dati-comune-roma-it-2026-06-20T175657.png
security:
- kind: domain-security
  name: Dati Comune Roma It Domain Security
  slug: dati-comune-roma-it-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dati-comune-roma-it
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Municipal Government
- Italy
website: https://dati.comune.roma.it/catalog
---

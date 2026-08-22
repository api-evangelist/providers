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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: CKAN Action API for Bahia Blanca Open Data, ~221 datasets. Base URL https://datos.bahia.gob.ar/api/3/action/.
  name: Bahia Blanca Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datos-bahia-gob-ar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datos.bahia.gob.ar
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/datos-bahia-gob-ar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/datos-bahia-gob-ar-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/datos-bahia-gob-ar-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Bahia Blanca Open Data is a municipal government open-data portal for Argentina running CKAN. It exposes the CKAN catalog API over approximately 221 datasets.
finops:
- name: Datos Bahia Gob Ar Finops
  service_category: ''
  slug: datos-bahia-gob-ar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datos-bahia-gob-ar.png
layout: provider
modified: '2026-06-07'
name: Bahia Blanca Open Data
nav: Providers
network: true
overview: 'Bahia Blanca Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Bahia Blanca Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Datos Bahia Gob Ar Plans Pricing
  plan_count: 1
  slug: datos-bahia-gob-ar-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Datos Bahia Gob Ar Rate Limits
  slug: datos-bahia-gob-ar-rate-limits
score:
  band: emerging
  composite: 12.0
  delta: -1.1
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
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
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datos-bahia-gob-ar/refs/heads/main/screenshots/datos-bahia-gob-ar-2026-06-20T175714.png
security:
- kind: domain-security
  name: Datos Bahia Gob Ar Domain Security
  slug: datos-bahia-gob-ar-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: datos-bahia-gob-ar
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- Municipal Government
- Argentina
website: https://datos.bahia.gob.ar
---

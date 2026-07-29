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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: CKAN Action API for Sonora Open Data, ~90 datasets. Base URL https://datos.sonora.gob.mx/api/3/action/.
  name: Sonora Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datos-sonora-gob-mx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datos.sonora.gob.mx
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/datos-sonora-gob-mx-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/datos-sonora-gob-mx-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/datos-sonora-gob-mx-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Sonora Open Data is a state government open-data portal for Mexico running CKAN. It exposes the CKAN catalog API over approximately 90 datasets.
finops:
- name: Datos Sonora Gob Mx Finops
  service_category: ''
  slug: datos-sonora-gob-mx-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datos-sonora-gob-mx.png
layout: provider
modified: '2026-06-07'
name: Sonora Open Data
nav: Providers
network: true
overview: 'Sonora Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Sonora Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Datos Sonora Gob Mx Plans Pricing
  plan_count: 0
  slug: datos-sonora-gob-mx-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 0
  name: Datos Sonora Gob Mx Rate Limits
  slug: datos-sonora-gob-mx-rate-limits
score:
  band: minimal
  composite: 9.5
  delta: -2.1
  facets:
    commercial_clarity: 7.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datos-sonora-gob-mx/refs/heads/main/screenshots/datos-sonora-gob-mx-2026-06-20T175726.png
security:
- kind: domain-security
  name: Datos Sonora Gob Mx Domain Security
  slug: datos-sonora-gob-mx-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: datos-sonora-gob-mx
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- State Government
- Mexico
website: https://datos.sonora.gob.mx
---

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
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: CKAN Action API for Datos Provincia de Misiones, a consistent JSON-over-HTTP interface over a catalog of 2 datasets. Standard actions include package_search, package_show, package_list, organization_l
  name: Datos Provincia de Misiones CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datos-misiones-gob-ar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datos.misiones.gob.ar
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/datos-misiones-gob-ar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/datos-misiones-gob-ar-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/datos-misiones-gob-ar-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Datos Provincia de Misiones is a state government open-data portal for Argentina running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 2 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Datos Misiones Gob Ar Finops
  service_category: Open Data
  slug: datos-misiones-gob-ar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datos-misiones-gob-ar.png
layout: provider
modified: '2026-06-04'
name: Datos Provincia de Misiones
nav: Providers
network: true
overview: 'Datos Provincia de Misiones publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Datos Provincia de Misiones'' developer surface includes documentation and 6 more developer resources.'
plans:
- name: Datos Misiones Gob Ar Plans Pricing
  plan_count: 1
  slug: datos-misiones-gob-ar-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 1
  name: Datos Misiones Gob Ar Rate Limits
  slug: datos-misiones-gob-ar-rate-limits
score:
  band: emerging
  composite: 18.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 18.5
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datos-misiones-gob-ar/refs/heads/main/screenshots/datos-misiones-gob-ar-2026-06-20T175722.png
security:
- kind: domain-security
  name: Datos Misiones Gob Ar Domain Security
  slug: datos-misiones-gob-ar-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: datos-misiones-gob-ar
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- State Government
- Argentina
website: https://datos.misiones.gob.ar
---

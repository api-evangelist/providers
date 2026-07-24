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
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: CKAN Action API for Datos Turismo y Deportes Argentina, a consistent JSON-over-HTTP interface over a catalog of 15 datasets. Standard actions include package_search, package_show, package_list, organi
  name: Datos Turismo y Deportes Argentina CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datos-yvera-tur-ar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datos.yvera.tur.ar
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/datos-yvera-tur-ar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/datos-yvera-tur-ar-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/datos-yvera-tur-ar-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Datos Turismo y Deportes Argentina is a government agency open-data portal for Argentina running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 15 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Datos Yvera Tur Ar Finops
  service_category: Open Data
  slug: datos-yvera-tur-ar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datos-yvera-tur-ar.png
layout: provider
modified: '2026-06-04'
name: Datos Turismo y Deportes Argentina
nav: Providers
network: true
overview: 'Datos Turismo y Deportes Argentina publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Datos Turismo y Deportes Argentina''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Datos Yvera Tur Ar Plans Pricing
  plan_count: 1
  slug: datos-yvera-tur-ar-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 1
  name: Datos Yvera Tur Ar Rate Limits
  slug: datos-yvera-tur-ar-rate-limits
score:
  band: emerging
  composite: 18.5
  delta: -1.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 19.5
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datos-yvera-tur-ar/refs/heads/main/screenshots/datos-yvera-tur-ar-2026-06-20T175728.png
security:
- kind: domain-security
  name: Datos Yvera Tur Ar Domain Security
  slug: datos-yvera-tur-ar-domain-security
  summary_line: DNSSEC
slug: datos-yvera-tur-ar
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Government Agency
- Argentina
website: https://datos.yvera.tur.ar
---

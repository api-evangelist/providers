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
- description: CKAN Action API for Datos Energia Argentina, a consistent JSON-over-HTTP interface over a catalog of 178 datasets. Standard actions include package_search, package_show, package_list, organization_lis
  name: Datos Energia Argentina CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datos-energia-gob-ar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datos.energia.gob.ar
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/datos-energia-gob-ar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/datos-energia-gob-ar-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/datos-energia-gob-ar-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Datos Energia Argentina is a government agency open-data portal for Argentina running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 178 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Datos Energia Gob Ar Finops
  service_category: Open Data
  slug: datos-energia-gob-ar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datos-energia-gob-ar.png
layout: provider
modified: '2026-06-04'
name: Datos Energia Argentina
nav: Providers
network: true
overview: 'Datos Energia Argentina publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Datos Energia Argentina''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Datos Energia Gob Ar Plans Pricing
  plan_count: 1
  slug: datos-energia-gob-ar-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 1
  name: Datos Energia Gob Ar Rate Limits
  slug: datos-energia-gob-ar-rate-limits
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
screenshot: https://raw.githubusercontent.com/api-evangelist/datos-energia-gob-ar/refs/heads/main/screenshots/datos-energia-gob-ar-2026-06-20T175718.png
security:
- kind: domain-security
  name: Datos Energia Gob Ar Domain Security
  slug: datos-energia-gob-ar-domain-security
  summary_line: TLSv1.2 · DNSSEC
slug: datos-energia-gob-ar
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Government Agency
- Argentina
website: https://datos.energia.gob.ar
---

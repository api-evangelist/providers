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
- description: CKAN Action API for Entre Rios Open Data, covering ~121 datasets. Base URL https://datos.entrerios.gov.ar/api/3/action/.
  name: Entre Rios Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datos-entrerios-gov-ar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datos.entrerios.gov.ar
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/datos-entrerios-gov-ar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/datos-entrerios-gov-ar-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/datos-entrerios-gov-ar-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Entre Rios Open Data is a state government open-data portal for Argentina running CKAN. It exposes the CKAN catalog API over approximately 121 datasets.
finops:
- name: Datos Entrerios Gov Ar Finops
  service_category: ''
  slug: datos-entrerios-gov-ar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datos-entrerios-gov-ar.png
layout: provider
modified: '2026-06-07'
name: Entre Rios Open Data
nav: Providers
network: true
overview: 'Entre Rios Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Entre Rios Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Datos Entrerios Gov Ar Plans Pricing
  plan_count: 1
  slug: datos-entrerios-gov-ar-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 0
  name: Datos Entrerios Gov Ar Rate Limits
  slug: datos-entrerios-gov-ar-rate-limits
score:
  band: emerging
  composite: 15.1
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.1
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datos-entrerios-gov-ar/refs/heads/main/screenshots/datos-entrerios-gov-ar-2026-06-20T175716.png
security:
- kind: domain-security
  name: Datos Entrerios Gov Ar Domain Security
  slug: datos-entrerios-gov-ar-domain-security
  summary_line: TLSv1.3 · DMARC
slug: datos-entrerios-gov-ar
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- State Government
- Argentina
website: https://datos.entrerios.gov.ar
---

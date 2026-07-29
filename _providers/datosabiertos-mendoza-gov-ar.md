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
- description: CKAN Action API for Mendoza Open Data, ~204 datasets. Base URL https://datosabiertos.mendoza.gov.ar/api/3/action/.
  name: Mendoza Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datosabiertos-mendoza-gov-ar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datosabiertos.mendoza.gov.ar
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/datosabiertos-mendoza-gov-ar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/datosabiertos-mendoza-gov-ar-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/datosabiertos-mendoza-gov-ar-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Mendoza Open Data is a state government open-data portal for Argentina running CKAN. It exposes the CKAN catalog API over approximately 204 datasets.
finops:
- name: Datosabiertos Mendoza Gov Ar Finops
  service_category: ''
  slug: datosabiertos-mendoza-gov-ar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datosabiertos-mendoza-gov-ar.png
layout: provider
modified: '2026-06-07'
name: Mendoza Open Data
nav: Providers
network: true
overview: 'Mendoza Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Mendoza Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Datosabiertos Mendoza Gov Ar Plans Pricing
  plan_count: 1
  slug: datosabiertos-mendoza-gov-ar-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 0
  name: Datosabiertos Mendoza Gov Ar Rate Limits
  slug: datosabiertos-mendoza-gov-ar-rate-limits
score:
  band: emerging
  composite: 13.1
  delta: -2.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datosabiertos-mendoza-gov-ar/refs/heads/main/screenshots/datosabiertos-mendoza-gov-ar-2026-06-20T175733.png
security:
- kind: domain-security
  name: Datosabiertos Mendoza Gov Ar Domain Security
  slug: datosabiertos-mendoza-gov-ar-domain-security
  summary_line: TLSv1.3
slug: datosabiertos-mendoza-gov-ar
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- State Government
- Argentina
website: https://datosabiertos.mendoza.gov.ar
---

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
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: CKAN Action API for Irish Housing Open Data, ~461 datasets. Base URL https://opendata.housing.gov.ie/api/3/action/.
  name: Irish Housing Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opendata-housing-gov-ie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opendata.housing.gov.ie
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/opendata-housing-gov-ie-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opendata-housing-gov-ie-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/opendata-housing-gov-ie-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Irish Housing Open Data is a federal government open-data portal for Ireland running CKAN. It exposes the CKAN catalog API over approximately 461 datasets.
finops:
- name: Opendata Housing Gov Ie Finops
  service_category: ''
  slug: opendata-housing-gov-ie-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opendata-housing-gov-ie.png
layout: provider
modified: '2026-06-07'
name: Irish Housing Open Data
nav: Providers
network: true
overview: 'Irish Housing Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Irish Housing Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Opendata Housing Gov Ie Plans Pricing
  plan_count: 0
  slug: opendata-housing-gov-ie-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 0
  name: Opendata Housing Gov Ie Rate Limits
  slug: opendata-housing-gov-ie-rate-limits
score:
  band: minimal
  composite: 11.6
  delta: 0.0
  facets:
    commercial_clarity: 7.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.6
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opendata-housing-gov-ie/refs/heads/main/screenshots/opendata-housing-gov-ie-2026-06-20T190938.png
security:
- kind: domain-security
  name: Opendata Housing Gov Ie Domain Security
  slug: opendata-housing-gov-ie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: opendata-housing-gov-ie
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Federal Government
- Ireland
website: https://opendata.housing.gov.ie
---

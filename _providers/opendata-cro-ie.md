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
- description: CKAN Action API for Companies Registration Office Open Data, ~2 datasets. Base URL https://opendata.cro.ie/api/3/action/.
  name: Companies Registration Office Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opendata-cro-ie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opendata.cro.ie
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/opendata-cro-ie-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opendata-cro-ie-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/opendata-cro-ie-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Companies Registration Office Open Data is a government agency open-data portal for Ireland running CKAN. It exposes the CKAN catalog API over approximately 2 datasets.
finops:
- name: Opendata Cro Ie Finops
  service_category: ''
  slug: opendata-cro-ie-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opendata-cro-ie.png
layout: provider
modified: '2026-06-07'
name: Companies Registration Office Open Data
nav: Providers
network: true
overview: 'Companies Registration Office Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Companies Registration Office Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Opendata Cro Ie Plans Pricing
  plan_count: 0
  slug: opendata-cro-ie-plans-pricing
random_paper: 39
rate_limits:
- limit_count: 0
  name: Opendata Cro Ie Rate Limits
  slug: opendata-cro-ie-rate-limits
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
screenshot: https://raw.githubusercontent.com/api-evangelist/opendata-cro-ie/refs/heads/main/screenshots/opendata-cro-ie-2026-06-20T190935.png
security:
- kind: domain-security
  name: Opendata Cro Ie Domain Security
  slug: opendata-cro-ie-domain-security
  summary_line: TLSv1.3 · DMARC
slug: opendata-cro-ie
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Government Agency
- Ireland
website: https://opendata.cro.ie
---

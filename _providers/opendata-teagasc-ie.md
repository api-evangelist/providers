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
- description: CKAN Action API for Teagasc Open Data, ~18 datasets. Base URL https://opendata.teagasc.ie/api/3/action/.
  name: Teagasc Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opendata-teagasc-ie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opendata.teagasc.ie
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/opendata-teagasc-ie-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opendata-teagasc-ie-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/opendata-teagasc-ie-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Teagasc Open Data is a government agency open-data portal for Ireland running CKAN. It exposes the CKAN catalog API over approximately 18 datasets.
finops:
- name: Opendata Teagasc Ie Finops
  service_category: ''
  slug: opendata-teagasc-ie-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opendata-teagasc-ie.png
layout: provider
modified: '2026-06-07'
name: Teagasc Open Data
nav: Providers
network: true
overview: 'Teagasc Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Teagasc Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Opendata Teagasc Ie Plans Pricing
  plan_count: 0
  slug: opendata-teagasc-ie-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 0
  name: Opendata Teagasc Ie Rate Limits
  slug: opendata-teagasc-ie-rate-limits
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
screenshot: https://raw.githubusercontent.com/api-evangelist/opendata-teagasc-ie/refs/heads/main/screenshots/opendata-teagasc-ie-2026-06-20T190948.png
security:
- kind: domain-security
  name: Opendata Teagasc Ie Domain Security
  slug: opendata-teagasc-ie-domain-security
  summary_line: TLSv1.3 · DMARC
slug: opendata-teagasc-ie
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Government Agency
- Ireland
website: https://opendata.teagasc.ie
---

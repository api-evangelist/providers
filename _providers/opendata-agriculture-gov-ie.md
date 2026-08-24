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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: CKAN Action API for Irish Agriculture Open Data, ~56 datasets. Base URL https://opendata.agriculture.gov.ie/api/3/action/.
  name: Irish Agriculture Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opendata-agriculture-gov-ie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opendata.agriculture.gov.ie
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/opendata-agriculture-gov-ie-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opendata-agriculture-gov-ie-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/opendata-agriculture-gov-ie-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Irish Agriculture Open Data is a federal government open-data portal for Ireland running CKAN. It exposes the CKAN catalog API over approximately 56 datasets.
finops:
- name: Opendata Agriculture Gov Ie Finops
  service_category: ''
  slug: opendata-agriculture-gov-ie-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opendata-agriculture-gov-ie.png
layout: provider
modified: '2026-06-07'
name: Irish Agriculture Open Data
nav: Providers
network: true
overview: 'Irish Agriculture Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Irish Agriculture Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Opendata Agriculture Gov Ie Plans Pricing
  plan_count: 0
  slug: opendata-agriculture-gov-ie-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Opendata Agriculture Gov Ie Rate Limits
  slug: opendata-agriculture-gov-ie-rate-limits
score:
  band: minimal
  composite: 7.8
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opendata-agriculture-gov-ie/refs/heads/main/screenshots/opendata-agriculture-gov-ie-2026-06-20T190926.png
security:
- kind: domain-security
  name: Opendata Agriculture Gov Ie Domain Security
  slug: opendata-agriculture-gov-ie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: opendata-agriculture-gov-ie
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Federal-Government
- Ireland
website: https://opendata.agriculture.gov.ie
---

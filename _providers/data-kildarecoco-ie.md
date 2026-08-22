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
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: CKAN Action API for Kildare County Council Open Data, ~80 datasets. Base URL https://data.kildarecoco.ie/api/3/action/.
  name: Kildare County Council Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-kildarecoco-ie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.kildarecoco.ie
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-kildarecoco-ie-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-kildarecoco-ie-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-kildarecoco-ie-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Kildare County Council Open Data is a county government open-data portal for Ireland running CKAN. It exposes the CKAN catalog API over approximately 80 datasets.
finops:
- name: Data Kildarecoco Ie Finops
  service_category: ''
  slug: data-kildarecoco-ie-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-kildarecoco-ie.png
layout: provider
modified: '2026-06-07'
name: Kildare County Council Open Data
nav: Providers
network: true
overview: 'Kildare County Council Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Kildare County Council Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Data Kildarecoco Ie Plans Pricing
  plan_count: 0
  slug: data-kildarecoco-ie-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Data Kildarecoco Ie Rate Limits
  slug: data-kildarecoco-ie-rate-limits
score:
  band: minimal
  composite: 7.8
  delta: -1.7
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
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
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/data-kildarecoco-ie/refs/heads/main/screenshots/data-kildarecoco-ie-2026-06-20T175545.png
security:
- kind: domain-security
  name: Data Kildarecoco Ie Domain Security
  slug: data-kildarecoco-ie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: data-kildarecoco-ie
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- County Government
- Ireland
website: https://data.kildarecoco.ie
---

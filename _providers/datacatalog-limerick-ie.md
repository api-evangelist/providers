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
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: CKAN Action API for Limerick Open Data Catalogue, ~82 datasets. Base URL https://datacatalog.limerick.ie/api/3/action/.
  name: Limerick Open Data Catalogue CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datacatalog-limerick-ie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datacatalog.limerick.ie
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/datacatalog-limerick-ie-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/datacatalog-limerick-ie-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/datacatalog-limerick-ie-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Limerick Open Data Catalogue is a municipal government open-data portal for Ireland running CKAN. It exposes the CKAN catalog API over approximately 82 datasets.
finops:
- name: Datacatalog Limerick Ie Finops
  service_category: ''
  slug: datacatalog-limerick-ie-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datacatalog-limerick-ie.png
layout: provider
modified: '2026-06-07'
name: Limerick Open Data Catalogue
nav: Providers
network: true
overview: 'Limerick Open Data Catalogue publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Limerick Open Data Catalogue''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Datacatalog Limerick Ie Plans Pricing
  plan_count: 0
  slug: datacatalog-limerick-ie-plans-pricing
random_paper: 81
rate_limits:
- limit_count: 0
  name: Datacatalog Limerick Ie Rate Limits
  slug: datacatalog-limerick-ie-rate-limits
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
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datacatalog-limerick-ie/refs/heads/main/screenshots/datacatalog-limerick-ie-2026-06-20T175632.png
security:
- kind: domain-security
  name: Datacatalog Limerick Ie Domain Security
  slug: datacatalog-limerick-ie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: datacatalog-limerick-ie
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Municipal Government
- Ireland
website: https://datacatalog.limerick.ie
---

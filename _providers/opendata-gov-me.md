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
- description: 'CKAN Action API for Montenegro Open Data, a consistent JSON-over-HTTP interface over a catalog of 894 datasets. Standard actions include package_search, package_show, package_list, organization_list, '
  name: Montenegro Open Data CKAN Action API
  slug: catalog
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://opendata.gov.me
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/opendata-gov-me-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opendata-gov-me-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/opendata-gov-me-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Montenegro Open Data is a national government open-data portal for Montenegro running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 894 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Opendata Gov Me Finops
  service_category: Open Data
  slug: opendata-gov-me-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opendata-gov-me.png
layout: provider
modified: '2026-06-07'
name: Montenegro Open Data
nav: Providers
network: true
overview: 'Montenegro Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Montenegro Open Data''s developer surface includes documentation and 5 more developer resources.'
plans:
- name: Opendata Gov Me Plans Pricing
  plan_count: 1
  slug: opendata-gov-me-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 1
  name: Opendata Gov Me Rate Limits
  slug: opendata-gov-me-rate-limits
score:
  band: emerging
  composite: 14.5
  delta: -2.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 16.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 0.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opendata-gov-me/refs/heads/main/screenshots/opendata-gov-me-2026-06-20T190939.png
slug: opendata-gov-me
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- National Government
- Montenegro
website: https://opendata.gov.me
---

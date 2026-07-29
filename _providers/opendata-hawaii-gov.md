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
- description: CKAN Action API for Hawaii Open Data Portal, a consistent JSON-over-HTTP interface over a catalog of 976 datasets. Standard actions include package_search, package_show, package_list, organization_lis
  name: Hawaii Open Data Portal CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opendata-hawaii-gov-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opendata.hawaii.gov
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/opendata-hawaii-gov-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opendata-hawaii-gov-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/opendata-hawaii-gov-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Hawaii Open Data Portal is a state government open-data portal for United States running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 976 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Opendata Hawaii Gov Finops
  service_category: Open Data
  slug: opendata-hawaii-gov-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opendata-hawaii-gov.png
layout: provider
modified: '2026-06-04'
name: Hawaii Open Data Portal
nav: Providers
network: true
overview: 'Hawaii Open Data Portal publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Hawaii Open Data Portal''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Opendata Hawaii Gov Plans Pricing
  plan_count: 1
  slug: opendata-hawaii-gov-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 1
  name: Opendata Hawaii Gov Rate Limits
  slug: opendata-hawaii-gov-rate-limits
score:
  band: emerging
  composite: 16.2
  delta: -2.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 18.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opendata-hawaii-gov/refs/heads/main/screenshots/opendata-hawaii-gov-2026-06-20T190939.png
security:
- kind: domain-security
  name: Opendata Hawaii Gov Domain Security
  slug: opendata-hawaii-gov-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: opendata-hawaii-gov
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- State Government
- United States
website: https://opendata.hawaii.gov
---

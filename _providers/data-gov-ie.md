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
- description: CKAN Action API for data.gov.ie, a consistent JSON-over-HTTP interface over a catalog of 22,200 datasets. Standard actions include package_search, package_show, package_list, organization_list, group_
  name: data.gov.ie CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-gov-ie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.gov.ie
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-gov-ie-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-gov-ie-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-gov-ie-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: data.gov.ie is a open data portal open-data portal for Ireland running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 22,200 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Data Gov Ie Finops
  service_category: Open Data
  slug: data-gov-ie-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-gov-ie.png
layout: provider
modified: '2026-06-04'
name: data.gov.ie
nav: Providers
network: true
overview: 'data.gov.ie publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  data.gov.ie''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Data Gov Ie Plans Pricing
  plan_count: 1
  slug: data-gov-ie-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 1
  name: Data Gov Ie Rate Limits
  slug: data-gov-ie-rate-limits
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
screenshot: https://raw.githubusercontent.com/api-evangelist/data-gov-ie/refs/heads/main/screenshots/data-gov-ie-2026-06-20T175536.png
security:
- kind: domain-security
  name: Data Gov Ie Domain Security
  slug: data-gov-ie-domain-security
  summary_line: TLSv1.3 · HSTS
slug: data-gov-ie
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- Ireland
website: https://data.gov.ie
---

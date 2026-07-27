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
- description: CKAN Action API for Queensland Government Data, a consistent JSON-over-HTTP interface over a catalog of 188,778 datasets. Standard actions include package_search, package_show, package_list, organizat
  name: Queensland Government Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-qld-gov-au-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.qld.gov.au
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-qld-gov-au-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-qld-gov-au-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-qld-gov-au-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://www.data.qld.gov.au/article/news-and-events
created: '2026-06-04'
description: Queensland Government Data is a open data portal open-data portal for Australia running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 188,778 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Data Qld Gov Au Finops
  service_category: Open Data
  slug: data-qld-gov-au-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-qld-gov-au.png
layout: provider
modified: '2026-06-04'
name: Queensland Government Data
nav: Providers
network: true
overview: 'Queensland Government Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Queensland Government Data''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Data Qld Gov Au Plans Pricing
  plan_count: 1
  slug: data-qld-gov-au-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 1
  name: Data Qld Gov Au Rate Limits
  slug: data-qld-gov-au-rate-limits
score:
  band: emerging
  composite: 18.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 18.9
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/data-qld-gov-au/refs/heads/main/screenshots/data-qld-gov-au-2026-06-20T175614.png
security:
- kind: domain-security
  name: Data Qld Gov Au Domain Security
  slug: data-qld-gov-au-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: data-qld-gov-au
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- Australia
website: https://data.qld.gov.au
---

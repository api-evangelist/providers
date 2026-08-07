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
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: CKAN Action API for Milwaukee Open Data, a consistent JSON-over-HTTP interface over a catalog of 186 datasets. Standard actions include package_search, package_show, package_list, organization_list, g
  name: Milwaukee Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-milwaukee-gov-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.milwaukee.gov
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-milwaukee-gov-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-milwaukee-gov-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-milwaukee-gov-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Milwaukee Open Data is a municipal government open-data portal for United States running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 186 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Data Milwaukee Gov Finops
  service_category: Open Data
  slug: data-milwaukee-gov-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-milwaukee-gov.png
layout: provider
modified: '2026-06-07'
name: Milwaukee Open Data
nav: Providers
network: true
overview: 'Milwaukee Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Milwaukee Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Data Milwaukee Gov Plans Pricing
  plan_count: 1
  slug: data-milwaukee-gov-plans-pricing
random_paper: 101
rate_limits:
- limit_count: 1
  name: Data Milwaukee Gov Rate Limits
  slug: data-milwaukee-gov-rate-limits
score:
  band: emerging
  composite: 16.2
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 16.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/data-milwaukee-gov/refs/heads/main/screenshots/data-milwaukee-gov-2026-06-20T175547.png
security:
- kind: domain-security
  name: Data Milwaukee Gov Domain Security
  slug: data-milwaukee-gov-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: data-milwaukee-gov
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Municipal Government
- United States
website: https://data.milwaukee.gov
---

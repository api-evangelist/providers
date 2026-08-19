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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: CKAN Action API for opendata.gov.je, a consistent JSON-over-HTTP interface over a catalog of 118 datasets. Standard actions include package_search, package_show, package_list, organization_list, group
  name: opendata.gov.je CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opendata-gov-je-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opendata.gov.je
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/opendata-gov-je-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opendata-gov-je-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/opendata-gov-je-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: opendata.gov.je is a open data portal open-data portal for JE running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 118 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Opendata Gov Je Finops
  service_category: Open Data
  slug: opendata-gov-je-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opendata-gov-je.png
layout: provider
modified: '2026-06-04'
name: opendata.gov.je
nav: Providers
network: true
overview: 'opendata.gov.je publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  opendata.gov.je''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Opendata Gov Je Plans Pricing
  plan_count: 1
  slug: opendata-gov-je-plans-pricing
random_paper: 132
rate_limits:
- limit_count: 1
  name: Opendata Gov Je Rate Limits
  slug: opendata-gov-je-rate-limits
score:
  band: emerging
  composite: 15.7
  delta: -0.5
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
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
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opendata-gov-je/refs/heads/main/screenshots/opendata-gov-je-2026-06-20T190935.png
security:
- kind: domain-security
  name: Opendata Gov Je Domain Security
  slug: opendata-gov-je-domain-security
  summary_line: TLSv1.3
slug: opendata-gov-je
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- JE
website: https://opendata.gov.je
---

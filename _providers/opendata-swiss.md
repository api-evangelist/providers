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
- description: CKAN Action API for opendata.swiss, a consistent JSON-over-HTTP interface over a catalog of 14,544 datasets. Standard actions include package_search, package_show, package_list, organization_list, gro
  name: opendata.swiss CKAN Action API
  slug: catalog
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/opendata-swiss-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opendata-swiss-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opendata.swiss
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/opendata-swiss-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opendata-swiss-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/opendata-swiss-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: opendata.swiss is a national government open-data portal for Switzerland running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 14,544 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Opendata Swiss Finops
  service_category: Open Data
  slug: opendata-swiss-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opendata-swiss.png
layout: provider
modified: '2026-06-04'
name: opendata.swiss
nav: Providers
network: true
overview: 'opendata.swiss publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  opendata.swiss'' developer surface includes documentation and 7 more developer resources.'
plans:
- name: Opendata Swiss Plans Pricing
  plan_count: 1
  slug: opendata-swiss-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 1
  name: Opendata Swiss Rate Limits
  slug: opendata-swiss-rate-limits
score:
  band: emerging
  composite: 20.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 20.5
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 26.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opendata-swiss/refs/heads/main/screenshots/opendata-swiss-2026-06-20T190946.png
security:
- kind: domain-security
  name: Opendata Swiss Domain Security
  slug: opendata-swiss-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Opendata Swiss Vulnerability Disclosure
  slug: opendata-swiss-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: opendata-swiss
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- National Government
- Switzerland
website: https://opendata.swiss
---

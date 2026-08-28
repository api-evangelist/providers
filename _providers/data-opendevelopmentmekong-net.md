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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: CKAN Action API for Open Development Mekong, a consistent JSON-over-HTTP interface over a catalog of 13,483 datasets. Standard actions include package_search, package_show, package_list, organization_
  name: Open Development Mekong CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-opendevelopmentmekong-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.opendevelopmentmekong.net
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-opendevelopmentmekong-net-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-opendevelopmentmekong-net-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-opendevelopmentmekong-net-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://opendevelopmentmekong.net/feed/
created: '2026-06-04'
description: Open Development Mekong is a organization open-data portal for Mekong Region running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 13,483 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Data Opendevelopmentmekong Net Finops
  service_category: Open Data
  slug: data-opendevelopmentmekong-net-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-opendevelopmentmekong-net.png
layout: provider
modified: '2026-06-04'
name: Open Development Mekong
nav: Providers
network: true
overview: 'Open Development Mekong publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Organization.


  Open Development Mekong''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Data Opendevelopmentmekong Net Plans Pricing
  plan_count: 1
  slug: data-opendevelopmentmekong-net-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Data Opendevelopmentmekong Net Rate Limits
  slug: data-opendevelopmentmekong-net-rate-limits
score:
  band: emerging
  composite: 16.2
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
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
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/data-opendevelopmentmekong-net/refs/heads/main/screenshots/data-opendevelopmentmekong-net-2026-06-20T175607.png
security:
- kind: domain-security
  name: Data Opendevelopmentmekong Net Domain Security
  slug: data-opendevelopmentmekong-net-domain-security
  summary_line: TLSv1.3
slug: data-opendevelopmentmekong-net
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Organization
- Mekong Region
website: https://data.opendevelopmentmekong.net
---

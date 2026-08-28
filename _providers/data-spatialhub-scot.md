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
- description: 'CKAN Action API for Spatial Hub Scotland, a consistent JSON-over-HTTP interface over a catalog of 496 datasets. Standard actions include package_search, package_show, package_list, organization_list, '
  name: Spatial Hub Scotland CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-spatialhub-scot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.spatialhub.scot
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-spatialhub-scot-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-spatialhub-scot-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-spatialhub-scot-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Spatial Hub Scotland is a regional government open-data portal for United Kingdom running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 496 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Data Spatialhub Scot Finops
  service_category: Open Data
  slug: data-spatialhub-scot-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-spatialhub-scot.png
layout: provider
modified: '2026-06-04'
name: Spatial Hub Scotland
nav: Providers
network: true
overview: 'Spatial Hub Scotland publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Spatial Hub Scotland''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Data Spatialhub Scot Plans Pricing
  plan_count: 1
  slug: data-spatialhub-scot-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Data Spatialhub Scot Rate Limits
  slug: data-spatialhub-scot-rate-limits
score:
  band: emerging
  composite: 15.7
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 15.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/data-spatialhub-scot/refs/heads/main/screenshots/data-spatialhub-scot-2026-06-20T175619.png
security:
- kind: domain-security
  name: Data Spatialhub Scot Domain Security
  slug: data-spatialhub-scot-domain-security
  summary_line: TLSv1.2
slug: data-spatialhub-scot
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Regional Government
- United Kingdom
website: https://data.spatialhub.scot
---

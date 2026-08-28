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
- description: CKAN Action API for DATA.GOV.HK, a consistent JSON-over-HTTP interface over a catalog of 218 datasets. Standard actions include package_search, package_show, package_list, organization_list, group_lis
  name: DATA.GOV.HK CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-gov-hk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.gov.hk/en-data
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-gov-hk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-gov-hk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-gov-hk-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: DATA.GOV.HK is a national government open-data portal for Hong Kong running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 218 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Data Gov Hk Finops
  service_category: Open Data
  slug: data-gov-hk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-gov-hk.png
layout: provider
modified: '2026-06-04'
name: DATA.GOV.HK
nav: Providers
network: true
overview: 'DATA.GOV.HK publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  DATA.GOV.HK''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Data Gov Hk Plans Pricing
  plan_count: 1
  slug: data-gov-hk-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Data Gov Hk Rate Limits
  slug: data-gov-hk-rate-limits
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
screenshot: https://raw.githubusercontent.com/api-evangelist/data-gov-hk/refs/heads/main/screenshots/data-gov-hk-2026-06-20T175534.png
security:
- kind: domain-security
  name: Data Gov Hk Domain Security
  slug: data-gov-hk-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: data-gov-hk
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- National Government
- Hong Kong
website: https://data.gov.hk/en-data
---

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
- description: CKAN Action API for Donnees Ouvertes Montreal, a consistent JSON-over-HTTP interface over a catalog of 401 datasets. Standard actions include package_search, package_show, package_list, organization_l
  name: Donnees Ouvertes Montreal CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/donnees-montreal-ca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://donnees.montreal.ca
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/donnees-montreal-ca-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/donnees-montreal-ca-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/donnees-montreal-ca-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Donnees Ouvertes Montreal is a municipal government open-data portal for Canada running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 401 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Donnees Montreal Ca Finops
  service_category: Open Data
  slug: donnees-montreal-ca-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/donnees-montreal-ca.png
layout: provider
modified: '2026-06-04'
name: Donnees Ouvertes Montreal
nav: Providers
network: true
overview: 'Donnees Ouvertes Montreal publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Donnees Ouvertes Montreal''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Donnees Montreal Ca Plans Pricing
  plan_count: 1
  slug: donnees-montreal-ca-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 1
  name: Donnees Montreal Ca Rate Limits
  slug: donnees-montreal-ca-rate-limits
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
screenshot: https://raw.githubusercontent.com/api-evangelist/donnees-montreal-ca/refs/heads/main/screenshots/donnees-montreal-ca-2026-06-20T180149.png
security:
- kind: domain-security
  name: Donnees Montreal Ca Domain Security
  slug: donnees-montreal-ca-domain-security
  summary_line: TLSv1.3 · DMARC
slug: donnees-montreal-ca
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Municipal Government
- Canada
website: https://donnees.montreal.ca
---

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
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: CKAN Action API for Aragón Open Data, a consistent JSON-over-HTTP interface over a catalog of 2,429 datasets. Standard actions include package_search, package_show, package_list, organization_list, gr
  name: Aragón Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opendata-aragon-es-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opendata.aragon.es
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/opendata-aragon-es-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opendata-aragon-es-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/opendata-aragon-es-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Aragón Open Data is a open data portal open-data portal for Spain running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 2,429 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Opendata Aragon Es Finops
  service_category: Open Data
  slug: opendata-aragon-es-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opendata-aragon-es.png
layout: provider
modified: '2026-06-04'
name: Aragón Open Data
nav: Providers
network: true
overview: 'Aragón Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Aragón Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Opendata Aragon Es Plans Pricing
  plan_count: 1
  slug: opendata-aragon-es-plans-pricing
random_paper: 143
rate_limits:
- limit_count: 1
  name: Opendata Aragon Es Rate Limits
  slug: opendata-aragon-es-rate-limits
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
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opendata-aragon-es/refs/heads/main/screenshots/opendata-aragon-es-2026-06-20T190931.png
security:
- kind: domain-security
  name: Opendata Aragon Es Domain Security
  slug: opendata-aragon-es-domain-security
  summary_line: TLSv1.2 · DMARC
slug: opendata-aragon-es
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- Spain
website: https://opendata.aragon.es
---

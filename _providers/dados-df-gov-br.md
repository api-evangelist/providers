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
- description: CKAN Action API for Dados abertos Distrito Federal, a consistent JSON-over-HTTP interface over a catalog of 176 datasets. Standard actions include package_search, package_show, package_list, organizat
  name: Dados abertos Distrito Federal CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dados-df-gov-br-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dados.df.gov.br
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/dados-df-gov-br-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dados-df-gov-br-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dados-df-gov-br-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Dados abertos Distrito Federal is a open data portal open-data portal for Brazil running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 176 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Dados Df Gov Br Finops
  service_category: Open Data
  slug: dados-df-gov-br-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dados-df-gov-br.png
layout: provider
modified: '2026-06-04'
name: Dados abertos Distrito Federal
nav: Providers
network: true
overview: 'Dados abertos Distrito Federal publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Dados abertos Distrito Federal''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Dados Df Gov Br Plans Pricing
  plan_count: 1
  slug: dados-df-gov-br-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 1
  name: Dados Df Gov Br Rate Limits
  slug: dados-df-gov-br-rate-limits
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
screenshot: https://raw.githubusercontent.com/api-evangelist/dados-df-gov-br/refs/heads/main/screenshots/dados-df-gov-br-2026-06-20T175454.png
security:
- kind: domain-security
  name: Dados Df Gov Br Domain Security
  slug: dados-df-gov-br-domain-security
  summary_line: DMARC
slug: dados-df-gov-br
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- Brazil
website: https://dados.df.gov.br
---

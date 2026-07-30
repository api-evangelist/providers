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
- description: CKAN Action API for Portale Dati aperti del Comune di Matera, a consistent JSON-over-HTTP interface over a catalog of 250 datasets. Standard actions include package_search, package_show, package_list,
  name: Portale Dati aperti del Comune di Matera CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dati-comune-matera-it-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dati.comune.matera.it
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/dati-comune-matera-it-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dati-comune-matera-it-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dati-comune-matera-it-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Portale Dati aperti del Comune di Matera is a open data portal open-data portal for Italy running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 250 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Dati Comune Matera It Finops
  service_category: Open Data
  slug: dati-comune-matera-it-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dati-comune-matera-it.png
layout: provider
modified: '2026-06-04'
name: Portale Dati aperti del Comune di Matera
nav: Providers
network: true
overview: 'Portale Dati aperti del Comune di Matera publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Portale Dati aperti del Comune di Matera''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Dati Comune Matera It Plans Pricing
  plan_count: 1
  slug: dati-comune-matera-it-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Dati Comune Matera It Rate Limits
  slug: dati-comune-matera-it-rate-limits
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
screenshot: https://raw.githubusercontent.com/api-evangelist/dati-comune-matera-it/refs/heads/main/screenshots/dati-comune-matera-it-2026-06-20T175656.png
security:
- kind: domain-security
  name: Dati Comune Matera It Domain Security
  slug: dati-comune-matera-it-domain-security
  summary_line: TLSv1.2
slug: dati-comune-matera-it
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- Italy
website: https://dati.comune.matera.it
---

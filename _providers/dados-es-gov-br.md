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
- description: CKAN Action API for Espirito Santo Open Data, covering ~452 datasets. Base URL https://dados.es.gov.br/api/3/action/.
  name: Espirito Santo Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dados-es-gov-br-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dados.es.gov.br
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/dados-es-gov-br-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dados-es-gov-br-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dados-es-gov-br-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Espirito Santo Open Data is a state government open-data portal for Brazil running CKAN. It exposes the CKAN catalog API over approximately 452 datasets.
finops:
- name: Dados Es Gov Br Finops
  service_category: ''
  slug: dados-es-gov-br-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dados-es-gov-br.png
layout: provider
modified: '2026-06-07'
name: Espirito Santo Open Data
nav: Providers
network: true
overview: 'Espirito Santo Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Espirito Santo Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Dados Es Gov Br Plans Pricing
  plan_count: 1
  slug: dados-es-gov-br-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 0
  name: Dados Es Gov Br Rate Limits
  slug: dados-es-gov-br-rate-limits
score:
  band: emerging
  composite: 13.1
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dados-es-gov-br/refs/heads/main/screenshots/dados-es-gov-br-2026-06-20T175426.png
security:
- kind: domain-security
  name: Dados Es Gov Br Domain Security
  slug: dados-es-gov-br-domain-security
  summary_line: TLSv1.2 · HSTS
slug: dados-es-gov-br
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- State Government
- Brazil
website: https://dados.es.gov.br
---

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
- description: CKAN Action API for Santa Catarina Open Data, covering ~112 datasets. Base URL https://dados.sc.gov.br/api/3/action/.
  name: Santa Catarina Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dados-sc-gov-br-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dados.sc.gov.br
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/dados-sc-gov-br-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dados-sc-gov-br-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dados-sc-gov-br-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Santa Catarina Open Data is a state government open-data portal for Brazil running CKAN. It exposes the CKAN catalog API over approximately 112 datasets.
finops:
- name: Dados Sc Gov Br Finops
  service_category: ''
  slug: dados-sc-gov-br-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dados-sc-gov-br.png
layout: provider
modified: '2026-06-07'
name: Santa Catarina Open Data
nav: Providers
network: true
overview: 'Santa Catarina Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Santa Catarina Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Dados Sc Gov Br Plans Pricing
  plan_count: 1
  slug: dados-sc-gov-br-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Dados Sc Gov Br Rate Limits
  slug: dados-sc-gov-br-rate-limits
score:
  band: emerging
  composite: 12.0
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dados-sc-gov-br/refs/heads/main/screenshots/dados-sc-gov-br-2026-06-20T175435.png
security:
- kind: domain-security
  name: Dados Sc Gov Br Domain Security
  slug: dados-sc-gov-br-domain-security
  summary_line: TLSv1.2 · DNSSEC
slug: dados-sc-gov-br
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- State-Government
- Brazil
website: https://dados.sc.gov.br
---

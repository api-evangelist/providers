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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: CKAN Action API for Dados Abertos POA, a consistent JSON-over-HTTP interface over a catalog of an open datasets. Standard actions include package_search, package_show, package_list, organization_list,
  name: Dados Abertos POA CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dados-portoalegre-rs-gov-br-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dados.portoalegre.rs.gov.br
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/dados-portoalegre-rs-gov-br-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dados-portoalegre-rs-gov-br-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dados-portoalegre-rs-gov-br-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Dados Abertos POA is a open data portal open-data portal for Brazil running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately an open datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Dados Portoalegre Rs Gov Br Finops
  service_category: Open Data
  slug: dados-portoalegre-rs-gov-br-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dados-portoalegre-rs-gov-br.png
layout: provider
modified: '2026-06-04'
name: Dados Abertos POA
nav: Providers
network: true
overview: 'Dados Abertos POA publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Dados Abertos POA''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Dados Portoalegre Rs Gov Br Plans Pricing
  plan_count: 1
  slug: dados-portoalegre-rs-gov-br-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Dados Portoalegre Rs Gov Br Rate Limits
  slug: dados-portoalegre-rs-gov-br-rate-limits
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
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dados-portoalegre-rs-gov-br/refs/heads/main/screenshots/dados-portoalegre-rs-gov-br-2026-06-20T175432.png
security:
- kind: domain-security
  name: Dados Portoalegre Rs Gov Br Domain Security
  slug: dados-portoalegre-rs-gov-br-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dados-portoalegre-rs-gov-br
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- Brazil
website: https://dados.portoalegre.rs.gov.br
---

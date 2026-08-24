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
- description: CKAN Action API for Portal oficial Ayuntamiento de Rivas Vaciamadrid, a consistent JSON-over-HTTP interface over a catalog of 7 datasets. Standard actions include package_search, package_show, package
  name: Portal oficial Ayuntamiento de Rivas Vaciamadrid CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datosabiertos-rivasciudad-es-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datosabiertos.rivasciudad.es
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/datosabiertos-rivasciudad-es-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/datosabiertos-rivasciudad-es-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/datosabiertos-rivasciudad-es-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Portal oficial Ayuntamiento de Rivas Vaciamadrid is a open data portal open-data portal for Spain running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 7 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Datosabiertos Rivasciudad Es Finops
  service_category: Open Data
  slug: datosabiertos-rivasciudad-es-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datosabiertos-rivasciudad-es.png
layout: provider
modified: '2026-06-04'
name: Portal oficial Ayuntamiento de Rivas Vaciamadrid
nav: Providers
network: true
overview: 'Portal oficial Ayuntamiento de Rivas Vaciamadrid publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Portal oficial Ayuntamiento de Rivas Vaciamadrid''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Datosabiertos Rivasciudad Es Plans Pricing
  plan_count: 1
  slug: datosabiertos-rivasciudad-es-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Datosabiertos Rivasciudad Es Rate Limits
  slug: datosabiertos-rivasciudad-es-rate-limits
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
screenshot: https://raw.githubusercontent.com/api-evangelist/datosabiertos-rivasciudad-es/refs/heads/main/screenshots/datosabiertos-rivasciudad-es-2026-06-20T175731.png
security:
- kind: domain-security
  name: Datosabiertos Rivasciudad Es Domain Security
  slug: datosabiertos-rivasciudad-es-domain-security
  summary_line: TLSv1.3 · DMARC
slug: datosabiertos-rivasciudad-es
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- Spain
website: https://datosabiertos.rivasciudad.es
---

---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
- description: CKAN Action API for Montevideo Open Data, ~155 datasets. Base URL https://ckan.montevideo.gub.uy/api/3/action/.
  name: Montevideo Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ckan-montevideo-gub-uy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ckan.montevideo.gub.uy
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/ckan-montevideo-gub-uy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ckan-montevideo-gub-uy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ckan-montevideo-gub-uy-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Montevideo Open Data is a municipal government open-data portal for Uruguay running CKAN. It exposes the CKAN catalog API over approximately 155 datasets.
finops:
- name: Ckan Montevideo Gub Uy Finops
  service_category: ''
  slug: ckan-montevideo-gub-uy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ckan-montevideo-gub-uy.png
layout: provider
modified: '2026-06-07'
name: Montevideo Open Data
nav: Providers
network: true
overview: 'Montevideo Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Montevideo Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Ckan Montevideo Gub Uy Plans Pricing
  plan_count: 0
  slug: ckan-montevideo-gub-uy-plans-pricing
random_paper: 39
rate_limits:
- limit_count: 0
  name: Ckan Montevideo Gub Uy Rate Limits
  slug: ckan-montevideo-gub-uy-rate-limits
score:
  band: minimal
  composite: 9.5
  delta: 0.0
  facets:
    commercial_clarity: 7.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ckan-montevideo-gub-uy/refs/heads/main/screenshots/ckan-montevideo-gub-uy-2026-06-20T174434.png
security:
- kind: domain-security
  name: Ckan Montevideo Gub Uy Domain Security
  slug: ckan-montevideo-gub-uy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: ckan-montevideo-gub-uy
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Municipal Government
- Uruguay
website: https://ckan.montevideo.gub.uy
---

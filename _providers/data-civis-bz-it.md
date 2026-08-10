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
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: CKAN API for South Tyrol Civis Open Data, ~938 datasets.
  name: South Tyrol Civis Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-civis-bz-it-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.civis.bz.it
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-civis-bz-it-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-civis-bz-it-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-civis-bz-it-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: South Tyrol Civis Open Data is a regional government open-data portal for Italy running CKAN. It exposes the CKAN catalog API over approximately 938 datasets.
finops:
- name: Data Civis Bz It Finops
  service_category: ''
  slug: data-civis-bz-it-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-civis-bz-it.png
layout: provider
modified: '2026-06-07'
name: South Tyrol Civis Open Data
nav: Providers
network: true
overview: 'South Tyrol Civis Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  South Tyrol Civis Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Data Civis Bz It Plans Pricing
  plan_count: 0
  slug: data-civis-bz-it-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Data Civis Bz It Rate Limits
  slug: data-civis-bz-it-rate-limits
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
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/data-civis-bz-it/refs/heads/main/screenshots/data-civis-bz-it-2026-06-20T175518.png
security:
- kind: domain-security
  name: Data Civis Bz It Domain Security
  slug: data-civis-bz-it-domain-security
  summary_line: TLSv1.2 · HSTS
slug: data-civis-bz-it
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Regional Government
- Italy
website: https://data.civis.bz.it
---

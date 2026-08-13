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
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: CKAN API for UPM YODA Open Data Portal, ~201 datasets.
  name: UPM YODA Open Data Portal CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/portal-yoda-dit-upm-es-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://portal-yoda.dit.upm.es
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/portal-yoda-dit-upm-es-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/portal-yoda-dit-upm-es-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/portal-yoda-dit-upm-es-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: UPM YODA Open Data Portal is a university open-data portal for Spain running CKAN. It exposes the CKAN catalog API over approximately 201 datasets.
finops:
- name: Portal Yoda Dit Upm Es Finops
  service_category: ''
  slug: portal-yoda-dit-upm-es-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/portal-yoda-dit-upm-es.png
layout: provider
modified: '2026-06-07'
name: UPM YODA Open Data Portal
nav: Providers
network: true
overview: 'UPM YODA Open Data Portal publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and University Data.


  UPM YODA Open Data Portal''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Portal Yoda Dit Upm Es Plans Pricing
  plan_count: 0
  slug: portal-yoda-dit-upm-es-plans-pricing
random_paper: 102
rate_limits:
- limit_count: 0
  name: Portal Yoda Dit Upm Es Rate Limits
  slug: portal-yoda-dit-upm-es-rate-limits
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
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/portal-yoda-dit-upm-es/refs/heads/main/screenshots/portal-yoda-dit-upm-es-2026-06-20T191931.png
security:
- kind: domain-security
  name: Portal Yoda Dit Upm Es Domain Security
  slug: portal-yoda-dit-upm-es-domain-security
  summary_line: TLSv1.2 · DMARC
slug: portal-yoda-dit-upm-es
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- University Data
- University
- Spain
website: https://portal-yoda.dit.upm.es
---

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
- description: CKAN Action API for Cali Open Data, ~663 datasets. Base URL https://datos.cali.gov.co/api/3/action/.
  name: Cali Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datos-cali-gov-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datos.cali.gov.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/datos-cali-gov-co-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/datos-cali-gov-co-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/datos-cali-gov-co-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Cali Open Data is a municipal government open-data portal for Colombia running CKAN. It exposes the CKAN catalog API over approximately 663 datasets.
finops:
- name: Datos Cali Gov Co Finops
  service_category: ''
  slug: datos-cali-gov-co-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datos-cali-gov-co.png
layout: provider
modified: '2026-06-07'
name: Cali Open Data
nav: Providers
network: true
overview: 'Cali Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Cali Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Datos Cali Gov Co Plans Pricing
  plan_count: 0
  slug: datos-cali-gov-co-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 0
  name: Datos Cali Gov Co Rate Limits
  slug: datos-cali-gov-co-rate-limits
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
screenshot: https://raw.githubusercontent.com/api-evangelist/datos-cali-gov-co/refs/heads/main/screenshots/datos-cali-gov-co-2026-06-20T175713.png
security:
- kind: domain-security
  name: Datos Cali Gov Co Domain Security
  slug: datos-cali-gov-co-domain-security
  summary_line: TLSv1.3 · DMARC
slug: datos-cali-gov-co
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Municipal Government
- Colombia
website: https://datos.cali.gov.co
---

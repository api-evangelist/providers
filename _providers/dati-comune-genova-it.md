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
- description: CKAN Action API for Genoa Open Data, ~163 datasets.
  name: Genoa Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dati-comune-genova-it-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dati.comune.genova.it
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/dati-comune-genova-it-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dati-comune-genova-it-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dati-comune-genova-it-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Genoa Open Data is a municipal government open-data portal for Italy running CKAN (~163 datasets).
finops:
- name: Dati Comune Genova It Finops
  service_category: ''
  slug: dati-comune-genova-it-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dati-comune-genova-it.png
layout: provider
modified: '2026-06-07'
name: Genoa Open Data
nav: Providers
network: true
overview: 'Genoa Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Genoa Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Dati Comune Genova It Plans Pricing
  plan_count: 0
  slug: dati-comune-genova-it-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Dati Comune Genova It Rate Limits
  slug: dati-comune-genova-it-rate-limits
score:
  band: minimal
  composite: 9.5
  delta: -2.1
  facets:
    commercial_clarity: 7.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dati-comune-genova-it/refs/heads/main/screenshots/dati-comune-genova-it-2026-06-20T175653.png
security:
- kind: domain-security
  name: Dati Comune Genova It Domain Security
  slug: dati-comune-genova-it-domain-security
  summary_line: TLSv1.3
slug: dati-comune-genova-it
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Municipal Government
- Italy
website: https://dati.comune.genova.it
---

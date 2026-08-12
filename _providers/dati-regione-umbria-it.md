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
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: CKAN API for Umbria Region Open Data, ~457 datasets.
  name: Umbria Region Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dati-regione-umbria-it-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dati.regione.umbria.it
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/dati-regione-umbria-it-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dati-regione-umbria-it-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dati-regione-umbria-it-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://dati.regione.umbria.it/feed/
created: '2026-06-07'
description: Umbria Region Open Data is a regional government open-data portal for Italy running CKAN. It exposes the CKAN catalog API over approximately 457 datasets.
finops:
- name: Dati Regione Umbria It Finops
  service_category: ''
  slug: dati-regione-umbria-it-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dati-regione-umbria-it.png
layout: provider
modified: '2026-06-07'
name: Umbria Region Open Data
nav: Providers
network: true
overview: 'Umbria Region Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Umbria Region Open Data''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Dati Regione Umbria It Plans Pricing
  plan_count: 0
  slug: dati-regione-umbria-it-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 0
  name: Dati Regione Umbria It Rate Limits
  slug: dati-regione-umbria-it-rate-limits
score:
  band: minimal
  composite: 9.9
  delta: 0.0
  facets:
    commercial_clarity: 7.9
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dati-regione-umbria-it/refs/heads/main/screenshots/dati-regione-umbria-it-2026-06-20T175707.png
security:
- kind: domain-security
  name: Dati Regione Umbria It Domain Security
  slug: dati-regione-umbria-it-domain-security
  summary_line: TLSv1.3
slug: dati-regione-umbria-it
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Regional Government
- Italy
website: https://dati.regione.umbria.it
---

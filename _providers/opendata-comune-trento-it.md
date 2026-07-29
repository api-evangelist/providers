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
- description: CKAN Action API for Trento Open Data, ~0 datasets. Base URL https://opendata.comune.trento.it/api/3/action/.
  name: Trento Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opendata-comune-trento-it-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opendata.comune.trento.it
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/opendata-comune-trento-it-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opendata-comune-trento-it-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/opendata-comune-trento-it-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Trento Open Data is a municipal government open-data portal for Italy running CKAN. It exposes the CKAN catalog API over approximately 0 datasets.
finops:
- name: Opendata Comune Trento It Finops
  service_category: ''
  slug: opendata-comune-trento-it-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opendata-comune-trento-it.png
layout: provider
modified: '2026-06-07'
name: Trento Open Data
nav: Providers
network: true
overview: 'Trento Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Trento Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Opendata Comune Trento It Plans Pricing
  plan_count: 0
  slug: opendata-comune-trento-it-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 0
  name: Opendata Comune Trento It Rate Limits
  slug: opendata-comune-trento-it-rate-limits
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
screenshot: https://raw.githubusercontent.com/api-evangelist/opendata-comune-trento-it/refs/heads/main/screenshots/opendata-comune-trento-it-2026-06-20T190933.png
security:
- kind: domain-security
  name: Opendata Comune Trento It Domain Security
  slug: opendata-comune-trento-it-domain-security
  summary_line: TLSv1.3
slug: opendata-comune-trento-it
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Municipal Government
- Italy
website: https://opendata.comune.trento.it
---

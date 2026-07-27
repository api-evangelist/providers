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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: CKAN Action API for Cork City Open Data, ~32 datasets.
  name: Cork City Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-corkcity-ie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.corkcity.ie
- group: commercial
  title: ''
  type: Plans
  url: plans/data-corkcity-ie-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-corkcity-ie-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-corkcity-ie-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Cork City Open Data is a municipal government open-data portal for Ireland running CKAN. It exposes the CKAN catalog API over approximately 32 datasets.
finops:
- name: Data Corkcity Ie Finops
  service_category: ''
  slug: data-corkcity-ie-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-corkcity-ie.png
layout: provider
modified: '2026-06-07'
name: Cork City Open Data
nav: Providers
network: true
overview: Cork City Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.
plans:
- name: Data Corkcity Ie Plans Pricing
  plan_count: 0
  slug: data-corkcity-ie-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Data Corkcity Ie Rate Limits
  slug: data-corkcity-ie-rate-limits
score:
  band: minimal
  composite: 10.1
  delta: 0.0
  facets:
    commercial_clarity: 7.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.1
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/data-corkcity-ie/refs/heads/main/screenshots/data-corkcity-ie-2026-06-20T175523.png
security:
- kind: domain-security
  name: Data Corkcity Ie Domain Security
  slug: data-corkcity-ie-domain-security
  summary_line: TLSv1.3 · DMARC
slug: data-corkcity-ie
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Municipal Government
- Ireland
website: https://data.corkcity.ie
---

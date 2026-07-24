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
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: DKAN open-data API for Incheon Open Data.
  name: Incheon Open Data DKAN API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-incheon-go-kr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.incheon.go.kr
- group: docs
  title: ''
  type: Documentation
  url: https://dkan.readthedocs.io/en/latest/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-incheon-go-kr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-incheon-go-kr-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-incheon-go-kr-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Incheon Open Data is a municipal government open-data portal for South Korea running DKAN.
finops:
- name: Data Incheon Go Kr Finops
  service_category: ''
  slug: data-incheon-go-kr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-incheon-go-kr.png
layout: provider
modified: '2026-06-07'
name: Incheon Open Data
nav: Providers
network: true
overview: 'Incheon Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, DKAN, Data Catalog, DCAT, and Government Data.


  Incheon Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Data Incheon Go Kr Plans Pricing
  plan_count: 0
  slug: data-incheon-go-kr-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 0
  name: Data Incheon Go Kr Rate Limits
  slug: data-incheon-go-kr-rate-limits
score:
  band: minimal
  composite: 11.6
  delta: 0.3
  facets:
    commercial_clarity: 7.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.3
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/data-incheon-go-kr/refs/heads/main/screenshots/data-incheon-go-kr-2026-06-20T175558.png
security:
- kind: domain-security
  name: Data Incheon Go Kr Domain Security
  slug: data-incheon-go-kr-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: data-incheon-go-kr
tags:
- Open Data
- DKAN
- Data Catalog
- DCAT
- Government Data
- Municipal Government
- South Korea
website: https://data.incheon.go.kr
---

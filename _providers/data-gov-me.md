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
- description: CKAN API for Montenegro Open Data (data.gov.me), ~894 datasets.
  name: Montenegro Open Data (data.gov.me) CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-gov-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.gov.me
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-gov-me-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-gov-me-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-gov-me-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://data.gov.me/blog
created: '2026-06-07'
description: Montenegro Open Data (data.gov.me) is a national government open-data portal for Montenegro running CKAN. It exposes the CKAN catalog API over approximately 894 datasets.
finops:
- name: Data Gov Me Finops
  service_category: ''
  slug: data-gov-me-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-gov-me.png
layout: provider
modified: '2026-06-07'
name: Montenegro Open Data (data.gov.me)
nav: Providers
network: true
overview: 'Montenegro Open Data (data.gov.me) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Montenegro Open Data (data.gov.me)''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Data Gov Me Plans Pricing
  plan_count: 0
  slug: data-gov-me-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Data Gov Me Rate Limits
  slug: data-gov-me-rate-limits
score:
  band: minimal
  composite: 11.9
  delta: 0.1
  facets:
    commercial_clarity: 7.9
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.8
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/data-gov-me/refs/heads/main/screenshots/data-gov-me-2026-06-20T175540.png
security:
- kind: domain-security
  name: Data Gov Me Domain Security
  slug: data-gov-me-domain-security
  summary_line: TLSv1.3 · DMARC
slug: data-gov-me
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- National Government
- Montenegro
website: https://data.gov.me
---

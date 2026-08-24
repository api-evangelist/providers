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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
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
random_paper: 13
rate_limits:
- limit_count: 0
  name: Data Gov Me Rate Limits
  slug: data-gov-me-rate-limits
score:
  band: minimal
  composite: 8.3
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
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

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
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: CKAN Action API for Zurich Open Data, ~925 datasets. Base URL https://data.stadt-zuerich.ch/api/3/action/.
  name: Zurich Open Data CKAN Action API
  slug: catalog
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/data-stadt-zuerich-ch-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-stadt-zuerich-ch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.stadt-zuerich.ch
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-stadt-zuerich-ch-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-stadt-zuerich-ch-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-stadt-zuerich-ch-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Zurich Open Data is a municipal government open-data portal for Switzerland running CKAN. It exposes the CKAN catalog API over approximately 925 datasets.
finops:
- name: Data Stadt Zuerich Ch Finops
  service_category: ''
  slug: data-stadt-zuerich-ch-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-stadt-zuerich-ch.png
layout: provider
modified: '2026-06-07'
name: Zurich Open Data
nav: Providers
network: true
overview: 'Zurich Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Zurich Open Data''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Data Stadt Zuerich Ch Plans Pricing
  plan_count: 0
  slug: data-stadt-zuerich-ch-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Data Stadt Zuerich Ch Rate Limits
  slug: data-stadt-zuerich-ch-rate-limits
score:
  band: minimal
  composite: 9.5
  delta: -1.7
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/data-stadt-zuerich-ch/refs/heads/main/screenshots/data-stadt-zuerich-ch-2026-06-20T175620.png
security:
- kind: domain-security
  name: Data Stadt Zuerich Ch Domain Security
  slug: data-stadt-zuerich-ch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Data Stadt Zuerich Ch Vulnerability Disclosure
  slug: data-stadt-zuerich-ch-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: data-stadt-zuerich-ch
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Municipal Government
- Switzerland
website: https://data.stadt-zuerich.ch
---

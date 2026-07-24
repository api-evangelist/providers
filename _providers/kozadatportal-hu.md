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
- description: CKAN API for Kozadat Hungary Open Data, ~2,283 datasets.
  name: Kozadat Hungary Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kozadatportal-hu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kozadatportal.hu
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/kozadatportal-hu-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kozadatportal-hu-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kozadatportal-hu-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Kozadat Hungary Open Data is a national government open-data portal for Hungary running CKAN. It exposes the CKAN catalog API over approximately 2,283 datasets.
finops:
- name: Kozadatportal Hu Finops
  service_category: ''
  slug: kozadatportal-hu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kozadatportal-hu.png
layout: provider
modified: '2026-06-07'
name: Kozadat Hungary Open Data
nav: Providers
network: true
overview: 'Kozadat Hungary Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Kozadat Hungary Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Kozadatportal Hu Plans Pricing
  plan_count: 0
  slug: kozadatportal-hu-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 0
  name: Kozadatportal Hu Rate Limits
  slug: kozadatportal-hu-rate-limits
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
screenshot: https://raw.githubusercontent.com/api-evangelist/kozadatportal-hu/refs/heads/main/screenshots/kozadatportal-hu-2026-06-20T184151.png
security:
- kind: domain-security
  name: Kozadatportal Hu Domain Security
  slug: kozadatportal-hu-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: kozadatportal-hu
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- National Government
- Hungary
website: https://kozadatportal.hu
---

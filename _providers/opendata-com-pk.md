---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
- description: CKAN Action API for Pakistan Open Data, covering ~1,471 datasets. Base URL https://opendata.com.pk/api/3/action/.
  name: Pakistan Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opendata-com-pk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opendata.com.pk
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/opendata-com-pk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opendata-com-pk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/opendata-com-pk-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Pakistan Open Data is a national government open-data portal for Pakistan running CKAN. It exposes the CKAN catalog API over approximately 1,471 datasets.
finops:
- name: Opendata Com Pk Finops
  service_category: ''
  slug: opendata-com-pk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opendata-com-pk.png
layout: provider
modified: '2026-06-07'
name: Pakistan Open Data
nav: Providers
network: true
overview: 'Pakistan Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Pakistan Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Opendata Com Pk Plans Pricing
  plan_count: 1
  slug: opendata-com-pk-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 0
  name: Opendata Com Pk Rate Limits
  slug: opendata-com-pk-rate-limits
score:
  band: emerging
  composite: 13.1
  delta: -2.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opendata-com-pk/refs/heads/main/screenshots/opendata-com-pk-2026-06-20T190931.png
security:
- kind: domain-security
  name: Opendata Com Pk Domain Security
  slug: opendata-com-pk-domain-security
  summary_line: TLSv1.2 · DMARC
slug: opendata-com-pk
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- National Government
- Pakistan
website: https://opendata.com.pk
---

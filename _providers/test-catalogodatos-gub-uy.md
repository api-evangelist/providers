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
- description: CKAN Action API for Uruguay Open Data Catalogue, ~2,515 datasets. Base URL https://test.catalogodatos.gub.uy/api/3/action/.
  name: Uruguay Open Data Catalogue CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/test-catalogodatos-gub-uy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://test.catalogodatos.gub.uy
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/test-catalogodatos-gub-uy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/test-catalogodatos-gub-uy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/test-catalogodatos-gub-uy-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Uruguay Open Data Catalogue is a national government open-data portal for Uruguay running CKAN. It exposes the CKAN catalog API over approximately 2,515 datasets.
finops:
- name: Test Catalogodatos Gub Uy Finops
  service_category: ''
  slug: test-catalogodatos-gub-uy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/test-catalogodatos-gub-uy.png
layout: provider
modified: '2026-06-07'
name: Uruguay Open Data Catalogue
nav: Providers
network: true
overview: 'Uruguay Open Data Catalogue publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Uruguay Open Data Catalogue''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Test Catalogodatos Gub Uy Plans Pricing
  plan_count: 0
  slug: test-catalogodatos-gub-uy-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Test Catalogodatos Gub Uy Rate Limits
  slug: test-catalogodatos-gub-uy-rate-limits
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
screenshot: https://raw.githubusercontent.com/api-evangelist/test-catalogodatos-gub-uy/refs/heads/main/screenshots/test-catalogodatos-gub-uy-2026-06-20T195147.png
security:
- kind: domain-security
  name: Test Catalogodatos Gub Uy Domain Security
  slug: test-catalogodatos-gub-uy-domain-security
  summary_line: TLSv1.2 · DNSSEC
slug: test-catalogodatos-gub-uy
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- National Government
- Uruguay
website: https://test.catalogodatos.gub.uy
---

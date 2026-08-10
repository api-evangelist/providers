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
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: CKAN Action API for Gifu Prefecture Open Data, a consistent JSON-over-HTTP interface over a catalog of 1,881 datasets. Standard actions include package_search, package_show, package_list, organization
  name: Gifu Prefecture Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gifu-opendata-pref-gifu-lg-jp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gifu-opendata.pref.gifu.lg.jp
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/gifu-opendata-pref-gifu-lg-jp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gifu-opendata-pref-gifu-lg-jp-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gifu-opendata-pref-gifu-lg-jp-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Gifu Prefecture Open Data is a regional government open-data portal for Japan running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 1,881 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Gifu Opendata Pref Gifu Lg Jp Finops
  service_category: Open Data
  slug: gifu-opendata-pref-gifu-lg-jp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gifu-opendata-pref-gifu-lg-jp.png
layout: provider
modified: '2026-06-04'
name: Gifu Prefecture Open Data
nav: Providers
network: true
overview: 'Gifu Prefecture Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Gifu Prefecture Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Gifu Opendata Pref Gifu Lg Jp Plans Pricing
  plan_count: 1
  slug: gifu-opendata-pref-gifu-lg-jp-plans-pricing
random_paper: 113
rate_limits:
- limit_count: 1
  name: Gifu Opendata Pref Gifu Lg Jp Rate Limits
  slug: gifu-opendata-pref-gifu-lg-jp-rate-limits
score:
  band: emerging
  composite: 16.2
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 16.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gifu-opendata-pref-gifu-lg-jp/refs/heads/main/screenshots/gifu-opendata-pref-gifu-lg-jp-2026-06-20T181825.png
security:
- kind: domain-security
  name: Gifu Opendata Pref Gifu Lg Jp Domain Security
  slug: gifu-opendata-pref-gifu-lg-jp-domain-security
  summary_line: TLSv1.2 · HSTS
slug: gifu-opendata-pref-gifu-lg-jp
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Regional Government
- Japan
website: https://gifu-opendata.pref.gifu.lg.jp
---

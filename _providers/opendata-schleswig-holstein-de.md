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
- description: CKAN Action API for Open Data Schleswig-Holstein, a consistent JSON-over-HTTP interface over a catalog of 32,414 datasets. Standard actions include package_search, package_show, package_list, organiza
  name: Open Data Schleswig-Holstein CKAN Action API
  slug: catalog
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/opendata-schleswig-holstein-de-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opendata-schleswig-holstein-de-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opendata.schleswig-holstein.de
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/opendata-schleswig-holstein-de-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opendata-schleswig-holstein-de-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/opendata-schleswig-holstein-de-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Open Data Schleswig-Holstein is a state government open-data portal for Germany running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 32,414 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Opendata Schleswig Holstein De Finops
  service_category: Open Data
  slug: opendata-schleswig-holstein-de-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opendata-schleswig-holstein-de.png
layout: provider
modified: '2026-06-04'
name: Open Data Schleswig-Holstein
nav: Providers
network: true
overview: 'Open Data Schleswig-Holstein publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Open Data Schleswig-Holstein''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Opendata Schleswig Holstein De Plans Pricing
  plan_count: 1
  slug: opendata-schleswig-holstein-de-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Opendata Schleswig Holstein De Rate Limits
  slug: opendata-schleswig-holstein-de-rate-limits
score:
  band: emerging
  composite: 17.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 17.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opendata-schleswig-holstein-de/refs/heads/main/screenshots/opendata-schleswig-holstein-de-2026-06-20T190946.png
security:
- kind: domain-security
  name: Opendata Schleswig Holstein De Domain Security
  slug: opendata-schleswig-holstein-de-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Opendata Schleswig Holstein De Vulnerability Disclosure
  slug: opendata-schleswig-holstein-de-vulnerability-disclosure
  summary_line: disclosure policy published
slug: opendata-schleswig-holstein-de
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- State Government
- Germany
website: https://opendata.schleswig-holstein.de
---

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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: CKAN Action API for Leipzig Open Data, ~395 datasets. Base URL https://opendata.leipzig.de/api/3/action/.
  name: Leipzig Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opendata-leipzig-de-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opendata.leipzig.de
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/opendata-leipzig-de-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opendata-leipzig-de-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/opendata-leipzig-de-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Leipzig Open Data is a municipal government open-data portal for Germany running CKAN. It exposes the CKAN catalog API over approximately 395 datasets.
finops:
- name: Opendata Leipzig De Finops
  service_category: ''
  slug: opendata-leipzig-de-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opendata-leipzig-de.png
layout: provider
modified: '2026-06-07'
name: Leipzig Open Data
nav: Providers
network: true
overview: 'Leipzig Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Leipzig Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Opendata Leipzig De Plans Pricing
  plan_count: 1
  slug: opendata-leipzig-de-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Opendata Leipzig De Rate Limits
  slug: opendata-leipzig-de-rate-limits
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 5
    catalog_gap: 72.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opendata-leipzig-de/refs/heads/main/screenshots/opendata-leipzig-de-2026-06-20T190942.png
security:
- kind: domain-security
  name: Opendata Leipzig De Domain Security
  slug: opendata-leipzig-de-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: opendata-leipzig-de
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- Municipal Government
- Germany
website: https://opendata.leipzig.de
---

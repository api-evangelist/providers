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
- description: CKAN Action API for SmartDublin Open Data, ~929 datasets.
  name: SmartDublin Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-smartdublin-ie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.smartdublin.ie
- group: commercial
  title: ''
  type: Plans
  url: plans/data-smartdublin-ie-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-smartdublin-ie-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-smartdublin-ie-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: SmartDublin Open Data is a municipal government open-data portal for Ireland running CKAN. It exposes the CKAN catalog API over approximately 929 datasets.
finops:
- name: Data Smartdublin Ie Finops
  service_category: ''
  slug: data-smartdublin-ie-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-smartdublin-ie.png
layout: provider
modified: '2026-06-07'
name: SmartDublin Open Data
nav: Providers
network: true
overview: SmartDublin Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.
plans:
- name: Data Smartdublin Ie Plans Pricing
  plan_count: 0
  slug: data-smartdublin-ie-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Data Smartdublin Ie Rate Limits
  slug: data-smartdublin-ie-rate-limits
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 5
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/data-smartdublin-ie/refs/heads/main/screenshots/data-smartdublin-ie-2026-06-20T175616.png
security:
- kind: domain-security
  name: Data Smartdublin Ie Domain Security
  slug: data-smartdublin-ie-domain-security
  summary_line: TLSv1.3 · HSTS
slug: data-smartdublin-ie
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Municipal Government
- Ireland
website: https://data.smartdublin.ie
---

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
- description: CKAN Action API for South Tyrol Retecivica Data, ~938 datasets.
  name: South Tyrol Retecivica Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dati-retecivica-bz-it-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dati.retecivica.bz.it
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/dati-retecivica-bz-it-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dati-retecivica-bz-it-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dati-retecivica-bz-it-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: South Tyrol Retecivica Data is a regional government open-data portal for Italy running CKAN (~938 datasets).
finops:
- name: Dati Retecivica Bz It Finops
  service_category: ''
  slug: dati-retecivica-bz-it-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dati-retecivica-bz-it.png
layout: provider
modified: '2026-06-07'
name: South Tyrol Retecivica Data
nav: Providers
network: true
overview: 'South Tyrol Retecivica Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  South Tyrol Retecivica Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Dati Retecivica Bz It Plans Pricing
  plan_count: 0
  slug: dati-retecivica-bz-it-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Dati Retecivica Bz It Rate Limits
  slug: dati-retecivica-bz-it-rate-limits
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
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dati-retecivica-bz-it/refs/heads/main/screenshots/dati-retecivica-bz-it-2026-06-20T175704.png
security:
- kind: domain-security
  name: Dati Retecivica Bz It Domain Security
  slug: dati-retecivica-bz-it-domain-security
  summary_line: TLSv1.2
slug: dati-retecivica-bz-it
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Regional Government
- Italy
website: https://dati.retecivica.bz.it
---

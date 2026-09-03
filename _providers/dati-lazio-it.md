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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: CKAN Action API for Lazio Open Data, covering ~406 datasets. Base URL https://dati.lazio.it/api/3/action/.
  name: Lazio Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dati-lazio-it-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dati.lazio.it
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/dati-lazio-it-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dati-lazio-it-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dati-lazio-it-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Lazio Open Data is a regional government open-data portal for Italy running CKAN. It exposes the CKAN catalog API over approximately 406 datasets.
finops:
- name: Dati Lazio It Finops
  service_category: ''
  slug: dati-lazio-it-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dati-lazio-it.png
layout: provider
modified: '2026-06-07'
name: Lazio Open Data
nav: Providers
network: true
overview: 'Lazio Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Lazio Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Dati Lazio It Plans Pricing
  plan_count: 1
  slug: dati-lazio-it-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Dati Lazio It Rate Limits
  slug: dati-lazio-it-rate-limits
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dati-lazio-it/refs/heads/main/screenshots/dati-lazio-it-2026-06-20T175706.png
security:
- kind: domain-security
  name: Dati Lazio It Domain Security
  slug: dati-lazio-it-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dati-lazio-it
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Regional Government
- Italy
website: https://dati.lazio.it
---

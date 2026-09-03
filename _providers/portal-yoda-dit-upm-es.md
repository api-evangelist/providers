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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: CKAN API for UPM YODA Open Data Portal, ~201 datasets.
  name: UPM YODA Open Data Portal CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/portal-yoda-dit-upm-es-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://portal-yoda.dit.upm.es
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/portal-yoda-dit-upm-es-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/portal-yoda-dit-upm-es-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/portal-yoda-dit-upm-es-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: UPM YODA Open Data Portal is a university open-data portal for Spain running CKAN. It exposes the CKAN catalog API over approximately 201 datasets.
finops:
- name: Portal Yoda Dit Upm Es Finops
  service_category: ''
  slug: portal-yoda-dit-upm-es-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/portal-yoda-dit-upm-es.png
layout: provider
modified: '2026-06-07'
name: UPM YODA Open Data Portal
nav: Providers
network: true
overview: 'UPM YODA Open Data Portal publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and University Data.


  UPM YODA Open Data Portal''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Portal Yoda Dit Upm Es Plans Pricing
  plan_count: 0
  slug: portal-yoda-dit-upm-es-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Portal Yoda Dit Upm Es Rate Limits
  slug: portal-yoda-dit-upm-es-rate-limits
score:
  band: minimal
  composite: 6.9
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
  previous_composite: 6.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/portal-yoda-dit-upm-es/refs/heads/main/screenshots/portal-yoda-dit-upm-es-2026-06-20T191931.png
security:
- kind: domain-security
  name: Portal Yoda Dit Upm Es Domain Security
  slug: portal-yoda-dit-upm-es-domain-security
  summary_line: TLSv1.2 · DMARC
slug: portal-yoda-dit-upm-es
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- University Data
- University
- Spain
website: https://portal-yoda.dit.upm.es
---

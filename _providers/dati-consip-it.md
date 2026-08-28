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
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: CKAN API for Consip Open Data, ~16 datasets.
  name: Consip Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dati-consip-it-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dati.consip.it
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/dati-consip-it-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dati-consip-it-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dati-consip-it-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Consip Open Data is a government agency open-data portal for Italy running CKAN. It exposes the CKAN catalog API over approximately 16 datasets.
finops:
- name: Dati Consip It Finops
  service_category: ''
  slug: dati-consip-it-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dati-consip-it.png
layout: provider
modified: '2026-06-07'
name: Consip Open Data
nav: Providers
network: true
overview: 'Consip Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Consip Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Dati Consip It Plans Pricing
  plan_count: 0
  slug: dati-consip-it-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Dati Consip It Rate Limits
  slug: dati-consip-it-rate-limits
score:
  band: minimal
  composite: 7.8
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
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dati-consip-it/refs/heads/main/screenshots/dati-consip-it-2026-06-20T175659.png
security:
- kind: domain-security
  name: Dati Consip It Domain Security
  slug: dati-consip-it-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dati-consip-it
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Government Agency
- Italy
website: https://dati.consip.it
---

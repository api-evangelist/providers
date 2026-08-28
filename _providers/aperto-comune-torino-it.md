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
- description: CKAN API for Turin Open Data, ~2,076 datasets.
  name: Turin Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aperto-comune-torino-it-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aperto.comune.torino.it
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/aperto-comune-torino-it-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aperto-comune-torino-it-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/aperto-comune-torino-it-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Turin Open Data is a municipal government open-data portal for Italy running CKAN. It exposes the CKAN catalog API over approximately 2,076 datasets.
finops:
- name: Aperto Comune Torino It Finops
  service_category: ''
  slug: aperto-comune-torino-it-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aperto-comune-torino-it.png
layout: provider
modified: '2026-06-07'
name: Turin Open Data
nav: Providers
network: true
overview: 'Turin Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Turin Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Aperto Comune Torino It Plans Pricing
  plan_count: 0
  slug: aperto-comune-torino-it-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Aperto Comune Torino It Rate Limits
  slug: aperto-comune-torino-it-rate-limits
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
screenshot: https://raw.githubusercontent.com/api-evangelist/aperto-comune-torino-it/refs/heads/main/screenshots/aperto-comune-torino-it-2026-06-20T172202.png
security:
- kind: domain-security
  name: Aperto Comune Torino It Domain Security
  slug: aperto-comune-torino-it-domain-security
  summary_line: TLSv1.3
slug: aperto-comune-torino-it
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Municipal Government
- Italy
website: https://aperto.comune.torino.it
---

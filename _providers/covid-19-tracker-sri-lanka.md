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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Provides situation of the COVID-19 patients reported in Sri Lanka
  name: COVID-19 Tracker Sri Lanka
  slug: covid-19-tracker-sri-lanka
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/covid-19-tracker-sri-lanka-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hpb.health.gov.lk/en/api-documentation
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Provides situation of the COVID-19 patients reported in Sri Lanka
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/covid-19-tracker-sri-lanka.png
layout: provider
modified: '2026-05-28'
name: COVID-19 Tracker Sri Lanka
nav: Providers
network: true
overview: COVID-19 Tracker Sri Lanka publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health and Public APIs.
random_paper: 5
score:
  band: minimal
  composite: 4.1
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/covid-19-tracker-sri-lanka/refs/heads/main/screenshots/covid-19-tracker-sri-lanka-2026-06-20T175154.png
security:
- kind: domain-security
  name: Covid 19 Tracker Sri Lanka Domain Security
  slug: covid-19-tracker-sri-lanka-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: covid-19-tracker-sri-lanka
tags:
- Health
- Public APIs
website: https://www.hpb.health.gov.lk/en/api-documentation
---

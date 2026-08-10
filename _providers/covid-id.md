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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Indonesian government Covid data per province
  name: COVID-ID
  slug: covid-id
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/covid-id-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.covid19.go.id/public/api/prov.json
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Indonesian government Covid data per province
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/covid-id.png
layout: provider
modified: '2026-05-28'
name: COVID-ID
nav: Providers
network: true
overview: COVID-ID publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health and Public APIs.
random_paper: 87
score:
  band: minimal
  composite: 6.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: domain-security
  name: Covid Id Domain Security
  slug: covid-id-domain-security
  summary_line: DNSSEC
slug: covid-id
tags:
- Health
- Public APIs
website: https://data.covid19.go.id/public/api/prov.json
---

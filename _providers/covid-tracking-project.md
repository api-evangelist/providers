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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Covid-19 data for the US
  name: Covid Tracking Project
  slug: covid-tracking-project
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/covid-tracking-project-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://covidtracking.com/data/api/version-2
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Covid-19 data for the US
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/covid-tracking-project.png
layout: provider
modified: '2026-05-28'
name: Covid Tracking Project
nav: Providers
network: true
overview: Covid Tracking Project publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health and Public APIs.
random_paper: 7
score:
  band: minimal
  composite: 4.1
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
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/covid-tracking-project/refs/heads/main/screenshots/covid-tracking-project-2026-06-20T175143.png
security:
- kind: domain-security
  name: Covid Tracking Project Domain Security
  slug: covid-tracking-project-domain-security
  summary_line: TLSv1.3 · DMARC
slug: covid-tracking-project
tags:
- Health
- Public APIs
website: https://covidtracking.com/data/api/version-2
---

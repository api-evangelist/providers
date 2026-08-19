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
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Government measures tracker to fight against the Covid-19 pandemic
  name: Covid-19 Government Response
  slug: covid-19-government-response
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/covid-19-government-response-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://covidtracker.bsg.ox.ac.uk
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Government measures tracker to fight against the Covid-19 pandemic
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/covid-19-government-response.png
layout: provider
modified: '2026-05-28'
name: Covid-19 Government Response
nav: Providers
network: true
overview: Covid-19 Government Response publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health and Public APIs.
random_paper: 64
score:
  band: minimal
  composite: 4.1
  delta: -1.9
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
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
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/covid-19-government-response/refs/heads/main/screenshots/covid-19-government-response-2026-06-20T175142.png
security:
- kind: domain-security
  name: Covid 19 Government Response Domain Security
  slug: covid-19-government-response-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: covid-19-government-response
tags:
- Health
- Public APIs
website: https://covidtracker.bsg.ox.ac.uk
---

---
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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://soccer-api.com/
- group: commercial
  title: ''
  type: Plans
  url: https://soccer-api.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://soccer-api.com/blog
coverage:
  checked: '2026-08-27'
  detail: 'Soccer API markets a football data API but does not yet operate one: its documentation, pricing and coverage pages each carry a notice declaring their own contents placeholders "until the final production Soccer API specification is supplied", the published base URL is the literal https://api.example.com/v1, and api.soccer-api.com does not resolve.'
  evidence:
  - status: 200
    url: https://soccer-api.com/api-documentation/
  - status: 200
    url: https://soccer-api.com/api-pricing/
  - status: 404
    url: https://soccer-api.com/openapi.json
  - status: 404
    url: https://soccer-api.com/.well-known/api-catalog
  - status: 404
    url: https://soccer-api.com/apis.json
  reason: no-developer-program
  state: none
created: '2026-08-24'
description: Soccer API sells live football data — live scores, statistics, odds and predictions — to developers building sports applications. The site publishes coverage and pricing pages and a blog, and gates access behind a sign-up.
layout: provider
modified: '2026-08-24'
name: Soccer API
nav: Providers
network: true
overview: 'Soccer API is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Sports, Football, Live Scores, Odds, and Data.


  Soccer API''s developer surface includes engineering blog and 2 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 4.6
  delta: -0.5
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
slug: soccer-api
tags:
- Sports
- Football
- Live Scores
- Odds
- Data
website: https://soccer-api.com/
---

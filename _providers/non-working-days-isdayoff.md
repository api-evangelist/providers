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
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: Simple REST API for checking working, non-working or short days for Russia, CIS, USA and other
  name: Non-Working Days
  slug: non-working-days
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/non-working-days-isdayoff-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://isdayoff.ru
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Simple REST API for checking working, non-working or short days for Russia, CIS, USA and other
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/non-working-days-isdayoff.png
layout: provider
modified: '2026-05-28'
name: Non-Working Days
nav: Providers
network: true
overview: Non-Working Days publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Calendar and Public APIs.
random_paper: 85
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/non-working-days-isdayoff/refs/heads/main/screenshots/non-working-days-isdayoff-2026-06-20T190401.png
security:
- kind: domain-security
  name: Non Working Days Isdayoff Domain Security
  slug: non-working-days-isdayoff-domain-security
  summary_line: TLSv1.3
slug: non-working-days-isdayoff
tags:
- Calendar
- Public APIs
website: https://isdayoff.ru
---

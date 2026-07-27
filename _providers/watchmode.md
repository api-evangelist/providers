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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: API for finding out the streaming availability of movies & shows
  name: Watchmode
  slug: watchmode
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/watchmode-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://api.watchmode.com/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: API for finding out the streaming availability of movies & shows
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/watchmode.png
layout: provider
modified: '2026-05-28'
name: Watchmode
nav: Providers
network: true
overview: Watchmode publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Video and Public APIs.
random_paper: 4
score:
  band: minimal
  composite: 6.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/watchmode/refs/heads/main/screenshots/watchmode-2026-06-20T201246.png
security:
- kind: domain-security
  name: Watchmode Domain Security
  slug: watchmode-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: watchmode
tags:
- Video
- Public APIs
website: https://api.watchmode.com/
---

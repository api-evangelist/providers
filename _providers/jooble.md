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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Job search engine
  name: Jooble
  slug: jooble
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jooble-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jooble.org/api/about
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Job search engine
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jooble.png
layout: provider
modified: '2026-05-28'
name: Jooble
nav: Providers
network: true
overview: Jooble publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Jobs and Public APIs.
random_paper: 19
score:
  band: minimal
  composite: 5.7
  delta: -1.1
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jooble/refs/heads/main/screenshots/jooble-2026-07-25T223241.png
security:
- kind: domain-security
  name: Jooble Domain Security
  slug: jooble-domain-security
  summary_line: TLSv1.3 · DMARC
slug: jooble
tags:
- Jobs
- Public APIs
website: https://jooble.org/api/about
---

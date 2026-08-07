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
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Movie information
  name: Open Movie Database
  slug: open-movie-database
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-movie-database-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.omdbapi.com/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Movie information
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-movie-database.png
layout: provider
modified: '2026-05-28'
name: Open Movie Database
nav: Providers
network: true
overview: Open Movie Database publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Video and Public APIs.
random_paper: 81
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
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-movie-database/refs/heads/main/screenshots/open-movie-database-2026-06-20T190843.png
security:
- kind: domain-security
  name: Open Movie Database Domain Security
  slug: open-movie-database-domain-security
  summary_line: TLSv1.3 · DMARC
slug: open-movie-database
tags:
- Video
- Public APIs
website: http://www.omdbapi.com/
---

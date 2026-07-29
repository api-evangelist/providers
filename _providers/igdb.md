---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Igdb Agentic Access
  operation_count: 17
  slug: igdb-agentic-access
  summary_line: 17 operations · 17 acting
api_count: 8
apis:
- description: Companies and developers/publishers in the gaming industry.
  name: IGDB Companies API
  slug: igdb-companies-api
- description: Video game records and related metadata.
  name: IGDB Games API
  slug: igdb-games-api
- description: Game genres and themes.
  name: IGDB Genres API
  slug: igdb-genres-api
- description: Covers, screenshots, artworks, and other media.
  name: IGDB Media API
  slug: igdb-media-api
- description: Gaming platforms and hardware.
  name: IGDB Platforms API
  slug: igdb-platforms-api
- description: Reference data such as keywords, collections, and franchises.
  name: IGDB Reference API
  slug: igdb-reference-api
- description: Release dates and regional releases.
  name: IGDB Releases API
  slug: igdb-releases-api
- description: Cross-entity search.
  name: IGDB Search API
  slug: igdb-search-api
artifact_total: 16
collections:
- collection_type: open
  name: IGDB API
  slug: open-igdb
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/igdb-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/igdb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/igdb-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.igdb.com/
- group: start
  title: ''
  type: Portal
  url: https://www.igdb.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.igdb.com/
- group: operate
  title: ''
  type: Support
  url: https://www.igdb.com/contact
created: '2025-02-08'
description: IGDB (Internet Game Database) is the world's most comprehensive video game database. The IGDB API provides access to a complete, holistic, accurate, and up-to-date data representation of the video game market, including game products, consumer opinions, and gaming industry information.
finops:
- name: Igdb Finops
  service_category: API
  slug: igdb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/igdb.png
layout: provider
modified: '2026-05-19'
name: IGDB
nav: Providers
network: true
overview: 'IGDB publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Companies API, Games API, Genres API, and 5 more. Tagged areas include Entertainment, Game Database, Gaming, and Video Games.


  The IGDB catalog on APIs.io includes 1 Spectral governance ruleset.


  IGDB''s developer surface includes authentication, developer portal, documentation, support, and 3 more developer resources.'
plans:
- name: Igdb Plans Pricing
  plan_count: 3
  slug: igdb-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Igdb Rate Limits
  slug: igdb-rate-limits
rules:
- name: IGDB API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: igdb-rules
score:
  band: thin
  composite: 39.5
  delta: -3.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 53.0
    developer_ergonomics: 32.6
    discoverability: 64.8
    governance: 10.4
    operational_transparency: 31.6
  previous_composite: 42.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/igdb/refs/heads/main/screenshots/igdb-2026-06-20T183218.png
security:
- kind: authentication
  name: Igdb Authentication
  slug: igdb-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Igdb Domain Security
  slug: igdb-domain-security
  summary_line: TLSv1.3 · DMARC
slug: igdb
tags:
- Entertainment
- Game Database
- Gaming
- Video Games
website: https://www.igdb.com/
---

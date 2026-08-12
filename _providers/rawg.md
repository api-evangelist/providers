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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Rawg Agentic Access
  operation_count: 60
  slug: rawg-agentic-access
  summary_line: 60 operations
api_count: 9
apis:
- description: The creator-roles API from RAWG — 1 operation(s) for creator-roles.
  name: RAWG creator-roles API
  slug: rawg-creator-roles-api
- description: The creators API from RAWG — 2 operation(s) for creators.
  name: RAWG creators API
  slug: rawg-creators-api
- description: The developers API from RAWG — 2 operation(s) for developers.
  name: RAWG developers API
  slug: rawg-developers-api
- description: The games API from RAWG — 14 operation(s) for games.
  name: RAWG games API
  slug: rawg-games-api
- description: The genres API from RAWG — 2 operation(s) for genres.
  name: RAWG genres API
  slug: rawg-genres-api
- description: The platforms API from RAWG — 3 operation(s) for platforms.
  name: RAWG platforms API
  slug: rawg-platforms-api
- description: The publishers API from RAWG — 2 operation(s) for publishers.
  name: RAWG publishers API
  slug: rawg-publishers-api
- description: The stores API from RAWG — 2 operation(s) for stores.
  name: RAWG stores API
  slug: rawg-stores-api
- description: The tags API from RAWG — 2 operation(s) for tags.
  name: RAWG tags API
  slug: rawg-tags-api
artifact_total: 25
collections:
- collection_type: open
  name: RAWG Video Games Database API
  slug: open-rawg
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rawg-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rawg-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rawg-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rawg
- group: company
  title: ''
  type: Website
  url: https://rawg.io
- group: docs
  title: ''
  type: Documentation
  url: https://rawg.io/apidocs
- group: start
  title: ''
  type: Signup
  url: https://rawg.io/login?forward=developer
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rawg.io/terms
- group: company
  title: ''
  type: Blog
  url: https://rawg.io/blog
created: '2025-02-08'
description: RAWG is the largest video game database and game discovery service, providing access to more than 350,000 games across 50+ platforms with rich metadata including tags, genres, developers, publishers, creators, release dates, Metacritic ratings, store links, ESRB ratings, average playtime, achievements, screenshots, trailers, and social media data. RAWG offers a free REST API for personal and small commercial use with API key authentication, enabling developers to search and filter games by platform, genre, developer, publisher, tag, release date, and rating. The API also provides endpoints for exploring game series, DLCs, development team members, and visually similar games (enterprise tier). RAWG is used by developers building game discovery apps, recommendation engines, gaming dashboards, and data warehouses.
examples:
- key_count: 38
  name: Rawg Game Detail Example
  slug: rawg-game-detail-example
- key_count: 4
  name: Rawg Games List Example
  slug: rawg-games-list-example
- key_count: 4
  name: Rawg Genres List Example
  slug: rawg-genres-list-example
- key_count: 4
  name: Rawg Platforms List Example
  slug: rawg-platforms-list-example
finops:
- name: Rawg Finops
  service_category: API
  slug: rawg-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rawg.png
json_schemas:
- name: RAWG Game
  property_count: 34
  slug: rawg-game
json_structures:
- name: Rawg Game Structure
  property_count: 0
  slug: rawg-game-structure
jsonld:
- class_count: 39
  name: Rawg Context
  property_count: 12
  slug: rawg-context
layout: provider
modified: '2026-05-19'
name: RAWG
nav: Providers
network: true
overview: 'RAWG publishes 9 APIs on the [APIs.io](https://apis.io/) network, including creator-roles API, creators API, developers API, and 6 more. Tagged areas include Database, Entertainment, Game Discovery, Games, and Gaming.


  The RAWG catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  RAWG''s developer surface includes authentication, documentation, signup flow, engineering blog, and 5 more developer resources.'
plans:
- name: Rawg Plans Pricing
  plan_count: 3
  slug: rawg-plans-pricing
random_paper: 85
rate_limits:
- limit_count: 5
  name: Rawg Rate Limits
  slug: rawg-rate-limits
rules:
- name: RAWG API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: rawg-jsonschema-spectral-rules
- name: RAWG API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 4
  slug: rawg-rules
score:
  band: developing
  composite: 42.2
  delta: -5.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 7.9
  previous_composite: 47.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/rawg/refs/heads/main/screenshots/rawg-2026-06-20T192612.png
security:
- kind: authentication
  name: Rawg Authentication
  slug: rawg-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Rawg Domain Security
  slug: rawg-domain-security
  summary_line: TLSv1.3 · HSTS
slug: rawg
tags:
- Database
- Entertainment
- Game Discovery
- Games
- Gaming
- Metadata
- Video Games
website: https://rawg.io
---

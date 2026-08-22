---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: The Game API is the primary client-side interface integrated into game builds for communication between the game and the LootLocker backend. It handles player session management, inventory, characters
  name: LootLocker Game API
  slug: game-api
- description: The Server API is intended for trusted server-side communication between a developer-managed game server and the LootLocker backend. It enables secure operations on behalf of players from dedicated ga
  name: LootLocker Server API
  slug: server-api
- description: The Admin API provides direct programmatic access to LootLocker's platform management features, enabling game editor integrations and tooling that interact with backend configuration. It is used for m
  name: LootLocker Admin API
  slug: admin-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lootlocker-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lootlocker.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lootlocker.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/lootlocker
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lootlocker
- group: company
  title: ''
  type: Blog
  url: https://lootlocker.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://lootlocker.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lootlocker.com/
- group: other
  title: ''
  type: X
  url: https://x.com/mylootlocker
- group: operate
  title: ''
  type: ChangeLog
  url: https://lootlocker.com/changelog
- group: build
  title: ''
  type: SDKs
  url: https://lootlocker.com/sdk
- group: commercial
  title: ''
  type: Plans
  url: plans/lootlocker-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lootlocker-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lootlocker-finops.yml
created: '2026-06-12'
description: LootLocker is a game backend-as-a-service platform that provides a REST API for building cross-platform game features without managing server infrastructure. The platform covers player authentication across Steam, Epic Games, PlayStation, Xbox, Nintendo Switch, Apple, Google, and custom white-label flows, as well as leaderboards, player progressions, virtual economies, persistent storage, cloud saves, and player file hosting. Developers can also access character systems, asset management, in-app purchasing, missions, collectibles, and Twitch Drops integration through a unified API surface. SDKs are available for Unity, Unreal Engine, and Godot, with basic integration support for GameMaker, Construct 3, and GDevelop.
finops:
- name: Lootlocker Finops
  service_category: ''
  slug: lootlocker-finops
graphqls:
- description: 'This document describes the conceptual GraphQL schema derived from the LootLocker Game API, Server API, and Admin API REST surfaces. LootLocker is a game backend-as-a-service platform offering player '
  name: LootLocker GraphQL Schema
  slug: lootlocker-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lootlocker.png
jsonld:
- class_count: 25
  name: Lootlocker Context
  property_count: 1
  slug: lootlocker-context
layout: provider
modified: '2026-06-12'
name: LootLocker
nav: Providers
network: true
overview: 'LootLocker publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Games, Game Backend, Game Backend as a Service, Player Authentication, and Leaderboards.


  The LootLocker catalog on APIs.io includes 1 JSON-LD context.


  LootLocker''s developer surface includes documentation, engineering blog, pricing, changelog, and 10 more developer resources.'
plans:
- name: Lootlocker Plans Pricing
  plan_count: 4
  slug: lootlocker-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Lootlocker Rate Limits
  slug: lootlocker-rate-limits
score:
  band: thin
  composite: 39.0
  delta: -1.2
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 52.2
    developer_ergonomics: 19.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lootlocker/refs/heads/main/screenshots/lootlocker-2026-06-20T184721.png
security:
- kind: domain-security
  name: Lootlocker Domain Security
  slug: lootlocker-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lootlocker
tags:
- Games
- Game Backend
- Game Backend as a Service
- Player Authentication
- Leaderboards
- Progressions
- Virtual Economy
- Cloud Save
- Cross-Platform
- Multiplayer
website: https://lootlocker.com/
---

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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
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
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Nakama Agentic Access
  operation_count: 27
  slug: nakama-agentic-access
  summary_line: 27 operations · 19 acting
api_count: 11
apis:
- description: Persistent WebSocket connection carrying realtime features - status presence, realtime chat channels, relayed and authoritative multiplayer matches, matchmaking, parties, and realtime notification del
  name: Nakama Realtime Socket API
  slug: nakama-realtime-api
- description: Administrative API behind the Nakama Developer Console for managing users, storage, leaderboards, matches, runtime configuration, and server status. It is an internal operations surface (not published
  name: Nakama Console API
  slug: nakama-console-api
- description: Read, update, and delete the current account and link identities.
  name: Nakama Account API
  slug: nakama-account-api
- description: Authenticate users and issue or refresh session tokens.
  name: Nakama Authentication API
  slug: nakama-authentication-api
- description: Manage the friend graph.
  name: Nakama Friends API
  slug: nakama-friends-api
- description: Create and manage groups (clans) and their members.
  name: Nakama Groups API
  slug: nakama-groups-api
- description: Write and list leaderboard records.
  name: Nakama Leaderboards API
  slug: nakama-leaderboards-api
- description: List and delete in-app notifications.
  name: Nakama Notifications API
  slug: nakama-notifications-api
- description: Call custom runtime functions.
  name: Nakama RPC API
  slug: nakama-rpc-api
- description: Read, write, list, and delete storage objects.
  name: Nakama Storage API
  slug: nakama-storage-api
- description: List, join, and submit to tournaments.
  name: Nakama Tournaments API
  slug: nakama-tournaments-api
artifact_total: 20
asyncapis:
- description: AsyncAPI 2.6 description of Nakama's **realtime socket API**. Unlike the request/response REST surface (modeled in `openapi/nakama-openapi.yml`), Nakama exposes a genuine bidirectional **WebSocket** t
  name: Nakama Realtime Socket API (WebSocket)
  slug: nakama-asyncapi
collections:
- collection_type: open
  name: Nakama API
  slug: open-nakama
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nakama-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nakama-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nakama-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/heroiclabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/heroic-labs
- group: company
  title: ''
  type: Website
  url: https://heroiclabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://heroiclabs.com/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/nakama-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nakama-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nakama-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://heroiclabs.com/blog/
created: '2026-07-01'
description: Nakama by Heroic Labs is an open-source (Apache-2.0) game and app backend server providing user accounts and authentication, social features (friends, groups, chat), collaborative storage, realtime multiplayer and authoritative matches, matchmaking, leaderboards and tournaments, notifications, and a server runtime with custom RPCs in Go, TypeScript/JavaScript, and Lua. Nakama exposes a gRPC-gateway-generated REST API plus a realtime WebSocket socket API, and is available self-hosted or as the managed Heroic Cloud.
finops:
- name: Nakama Finops
  service_category: Game Backend and Realtime Infrastructure
  slug: nakama-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nakama.png
layout: provider
modified: '2026-07-01'
name: Nakama
nav: Providers
network: true
overview: 'Nakama publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Realtime Socket API, Account API, Authentication API, and 7 more. Tagged areas include Gaming, Game Backend, Backend, Realtime, and Multiplayer.


  The Nakama catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Nakama''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Nakama Plans Pricing
  plan_count: 3
  slug: nakama-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Nakama Rate Limits
  slug: nakama-rate-limits
rules:
- name: Nakama API Rules
  rule_count: 7
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 7
  slug: nakama-asyncapi-spectral-rules
score:
  band: developing
  composite: 45.8
  delta: -4.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 52.1
    operational_transparency: 36.8
  previous_composite: 50.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Nakama Authentication
  slug: nakama-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Nakama Domain Security
  slug: nakama-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: nakama
tags:
- Gaming
- Game Backend
- Backend
- Realtime
- Multiplayer
- Matchmaking
- Leaderboards
- Social
- Open Source
website: https://heroiclabs.com/
---

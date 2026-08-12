---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-11'
api_count: 6
apis:
- description: The PowerSync Service exposes a streaming sync protocol over HTTP/WebSocket that client SDKs connect to using JWT authentication. Clients submit their current bucket state and the service streams real
  name: PowerSync Sync Service API
  slug: sync-service
- description: 'Client SDK for JavaScript and browser environments using Wasm-backed SQLite. Provides a PowerSyncDatabase class for local SQLite management with reactive queries, offline write queuing, and automatic '
  name: PowerSync JavaScript / Web SDK
  slug: javascript-sdk
- description: Client SDK for React Native and Expo applications, enabling offline-first mobile apps backed by embedded SQLite synced to Postgres, MongoDB, MySQL, or SQL Server.
  name: PowerSync React Native SDK
  slug: react-native-sdk
- description: Client SDK for Flutter and Dart applications providing embedded SQLite sync with Rust-backed native connection pools and built-in encryption support.
  name: PowerSync Flutter / Dart SDK
  slug: flutter-sdk
- description: Client SDK for Kotlin Multiplatform applications, enabling offline-first Android and cross-platform apps with embedded SQLite synced to backend databases.
  name: PowerSync Kotlin SDK
  slug: kotlin-sdk
- description: Client SDK for Swift applications enabling offline-first iOS and macOS apps with embedded SQLite synced to backend databases via the PowerSync Service.
  name: PowerSync Swift SDK
  slug: swift-sdk
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/powersync-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://powersync.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.powersync.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/powersync-ja
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/journeyapps-powersync/
- group: company
  title: ''
  type: Blog
  url: https://powersync.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://powersync.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.powersync.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/powersync_
- group: operate
  title: ''
  type: ChangeLog
  url: https://releases.powersync.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/powersync-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/powersync-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/powersync-finops.yml
created: '2026-06-12'
description: 'PowerSync is a sync engine that automatically synchronizes backend databases (Postgres, MongoDB, MySQL, SQL Server) with client-side SQLite, enabling offline-first and local-first applications. It consists of two components: the PowerSync Service (available as a managed cloud service or self-hosted via Docker) and a set of open-source client SDKs. Client SDKs are available for JavaScript/Web, React Native, Flutter/Dart, Kotlin, Swift, Node.js, .NET, and Rust. Authentication is handled via JWT tokens, with support for major providers including Auth0, Firebase, Supabase, Amazon Cognito, and Azure AD. PowerSync streams database changes in real-time so clients can query and mutate local SQLite without waiting on the network.'
finops:
- name: Powersync Finops
  service_category: Database
  slug: powersync-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/powersync.png
jsonld:
- class_count: 4
  name: Powersync Context
  property_count: 37
  slug: powersync-context
layout: provider
modified: '2026-06-12'
name: PowerSync
nav: Providers
network: true
overview: 'PowerSync publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Developer Tools, Database, Sync, Offline-First, and SQLite.


  The PowerSync catalog on APIs.io includes 1 JSON-LD context.


  PowerSync''s developer surface includes documentation, engineering blog, pricing, changelog, and 9 more developer resources.'
plans:
- name: Powersync Plans Pricing
  plan_count: 4
  slug: powersync-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 10
  name: Powersync Rate Limits
  slug: powersync-rate-limits
score:
  band: thin
  composite: 30.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 68.4
  previous_composite: 30.8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/powersync/refs/heads/main/screenshots/powersync-2026-06-20T192032.png
security:
- kind: domain-security
  name: Powersync Domain Security
  slug: powersync-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: powersync
tags:
- Developer Tools
- Database
- Sync
- Offline-First
- SQLite
- Local-First
- Real-Time
website: https://powersync.com/
---

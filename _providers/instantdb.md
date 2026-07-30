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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Instantdb Agentic Access
  operation_count: 14
  slug: instantdb-agentic-access
  summary_line: 14 operations · 12 acting
api_count: 6
apis:
- description: The realtime sync transport - a persistent WebSocket at wss://api.instantdb.com/runtime/session over which the client Reactor sends init, add-query, transact, and presence ops and the server streams q
  name: InstantDB Realtime Sync API
  slug: instantdb-realtime-sync-api
- description: Server-side authentication, tokens, and users.
  name: InstantDB Auth API
  slug: instantdb-auth-api
- description: Room presence lookups.
  name: InstantDB Presence API
  slug: instantdb-presence-api
- description: InstaQL read queries.
  name: InstantDB Query API
  slug: instantdb-query-api
- description: File upload, listing, and deletion.
  name: InstantDB Storage API
  slug: instantdb-storage-api
- description: InstaML transaction writes.
  name: InstantDB Transactions API
  slug: instantdb-transactions-api
artifact_total: 15
asyncapis:
- description: 'AsyncAPI 2.6 description of InstantDB''s **realtime sync** surface. Unlike a request/response REST API, InstantDB is a sync engine. The client SDK''s **Reactor** opens a persistent WebSocket connection '
  name: InstantDB Realtime Sync (WebSocket)
  slug: instantdb-asyncapi
collections:
- collection_type: open
  name: InstantDB Admin HTTP API
  slug: open-instantdb
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/instantdb-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/instantdb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/instantdb-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/instantdb
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/instantdb
- group: company
  title: ''
  type: Website
  url: https://www.instantdb.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.instantdb.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/instantdb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/instantdb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/instantdb-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.instantdb.com/rss.xml
created: '2026-06-20'
description: InstantDB (Instant) is a realtime client-side database and Firebase alternative that gives apps a sync engine with multiplayer, offline mode, and optimistic updates by default. It exposes an HTTP Admin API (api.instantdb.com) for server-side InstaQL queries and InstaML transactions, plus auth, storage, presence, and a realtime WebSocket sync layer.
finops:
- name: Instantdb Finops
  service_category: Databases
  slug: instantdb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/instantdb.png
layout: provider
modified: '2026-06-20'
name: InstantDB
nav: Providers
network: true
overview: 'InstantDB publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Realtime Sync API, Auth API, Presence API, and 3 more. Tagged areas include Database, Realtime, Sync, Backend, and Local First.


  The InstantDB catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  InstantDB''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Instantdb Plans Pricing
  plan_count: 4
  slug: instantdb-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 5
  name: Instantdb Rate Limits
  slug: instantdb-rate-limits
rules:
- name: InstantDB API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: instantdb-asyncapi-spectral-rules
score:
  band: developing
  composite: 47.4
  delta: -4.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 69.0
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 47.9
    operational_transparency: 36.8
  previous_composite: 51.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/instantdb/refs/heads/main/screenshots/instantdb-2026-06-20T183415.png
security:
- kind: authentication
  name: Instantdb Authentication
  slug: instantdb-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Instantdb Domain Security
  slug: instantdb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: instantdb
tags:
- Database
- Realtime
- Sync
- Backend
- Local First
website: https://www.instantdb.com
---

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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Instantdb Agentic Access
  operation_count: 14
  slug: instantdb-agentic-access
  summary_line: 14 operations · 12 acting
api_count: 1
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
artifact_total: 21
asyncapis:
- description: 'AsyncAPI 2.6 description of InstantDB''s **realtime sync** surface. Unlike a request/response REST API, InstantDB is a sync engine. The client SDK''s **Reactor** opens a persistent WebSocket connection '
  name: InstantDB Realtime Sync (WebSocket)
  slug: instantdb-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: InstantDB Admin HTTP Auth API
  slug: open-instantdb-auth-api
- collection_type: open
  name: InstantDB Admin HTTP Auth Presence API
  slug: open-instantdb-presence-api
- collection_type: open
  name: InstantDB Admin HTTP Auth Query API
  slug: open-instantdb-query-api
- collection_type: open
  name: InstantDB Admin HTTP Auth Storage API
  slug: open-instantdb-storage-api
- collection_type: open
  name: InstantDB Admin HTTP Auth Transactions API
  slug: open-instantdb-transactions-api
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
overview: 'InstantDB publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Realtime Sync API, Auth API, Presence API, and 3 more. Tagged areas include Database, Real-Time, Sync, Backend, and Local-First.


  The InstantDB catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  InstantDB''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Instantdb Plans Pricing
  plan_count: 4
  slug: instantdb-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Instantdb Rate Limits
  slug: instantdb-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: InstantDB API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: instantdb-asyncapi-spectral-rules
score:
  band: developing
  composite: 43.7
  coverage:
    artifact_dirs: 12
    catalog_gap: 46.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 13.6
    contract_quality: 62.8
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 34.2
  previous_composite: 43.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
- Real-Time
- Sync
- Backend
- Local-First
website: https://www.instantdb.com
---

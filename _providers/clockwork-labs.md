---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'The SpacetimeDB HTTP API lets clients and tools interact with SpacetimeDB databases: publish and delete database modules, manage database names, retrieve schema and logs, invoke reducers, run SQL quer'
  name: SpacetimeDB HTTP API
  slug: spacetimedb-http-api
artifact_total: 4
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://spacetimedb.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://spacetimedb.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://spacetimedb.com/docs/http/database/
- group: start
  title: ''
  type: GettingStarted
  url: https://spacetimedb.com/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clockworklabs
- group: company
  title: ''
  type: Blog
  url: https://spacetimedb.com/blog
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/spacetimedb
- group: operate
  title: ''
  type: StatusPage
  url: https://status.spacetimedb.com
- group: commercial
  title: ''
  type: Pricing
  url: https://spacetimedb.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://spacetimedb.com/login
- group: start
  title: ''
  type: Login
  url: https://spacetimedb.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://spacetimedb.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spacetimedb.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clockwork-labs-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/clockwork-labs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/clockwork-labs-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/clockwork-labs-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/clockwork-labs-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clockwork-labs-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/clockwork-labs-openid-configuration.json
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/clockwork-labs-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/clockwork-labs-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/clockwork-labs-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clockwork-labs-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/clockwork-labs-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/clockwork-labs-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clockwork-labs-domain-security.yml
created: '2026-07-17'
description: 'Clockwork Labs is a San Francisco software company (founded 2019) that builds SpacetimeDB, a relational database that is also an application server: developers upload their schema and server-side business logic as a WebAssembly "module" (written in Rust, C#, TypeScript, or C++) directly into the database, and clients connect over WebSocket to invoke reducers and subscribe to real-time state updates with no separate application server in between. SpacetimeDB exposes a versioned HTTP API (/v1/database and /v1/identity) for publishing modules, invoking reducers, running SQL, streaming subscriptions, and managing identities and JWT tokens, plus a first-party `spacetime` CLI and client SDKs for TypeScript, C#/Unity, Rust, Python, and C++. It is the production backend of BitCraft, the company''s MMO. Clockwork Labs is backed by a16z, Supercell, Firstminute Capital, Skycatcher, 1Up Ventures, and Supernode.'
image: https://spacetimedb.com/og-home.png
layout: provider
mcp_servers:
- description: ''
  name: clockwork-labs-mcp.yml
  slug: clockwork-labs-mcpyml
modified: '2026-07-18'
name: Clockwork Labs
nav: Providers
network: true
overview: 'Clockwork Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Database, Real-Time, WebSocket, and Game Backend.


  Clockwork Labs'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 21 more developer resources.'
random_paper: 44
score:
  band: thin
  composite: 37.7
  delta: -1.4
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 69.0
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 36.8
  previous_composite: 39.1
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clockwork-labs/refs/heads/main/screenshots/clockwork-labs-2026-07-25T205640.png
security:
- kind: authentication
  name: Clockwork Labs Authentication
  slug: clockwork-labs-authentication
  summary_line: http/openIdConnect · 2 schemes
- kind: domain-security
  name: Clockwork Labs Domain Security
  slug: clockwork-labs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: clockwork-labs
tags:
- Company
- Database
- Real-Time
- WebSocket
- Game Backend
- Multiplayer
- Serverless
- WebAssembly
- Developer Tools
- Infrastructure
website: https://spacetimedb.com/docs
---

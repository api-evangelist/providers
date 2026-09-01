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
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Rivet Agentic Access
  operation_count: 24
  slug: rivet-agentic-access
  summary_line: 24 operations · 10 acting
api_count: 1
apis:
- description: The Actors API from Rivet — 3 operation(s) for actors.
  name: Rivet Actors API
  slug: rivet-actors-api
- description: The Gateway API from Rivet — 12 operation(s) for gateway.
  name: Rivet Gateway API
  slug: rivet-gateway-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: RivetKit Actors API
  slug: open-rivet-actors-api
- collection_type: open
  name: RivetKit Actors Gateway API
  slug: open-rivet-gateway-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/rivet-rivetkit-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rivet-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rivet-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.rivet.dev/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.rivet.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.rivet.dev/typedoc
- group: start
  title: ''
  type: GettingStarted
  url: https://www.rivet.dev/docs/actors/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rivet-dev
- group: company
  title: ''
  type: Blog
  url: https://www.rivet.dev/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.rivet.dev/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://rivet.betteruptime.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rivet.dev/cloud
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.rivet.dev
- group: operate
  title: ''
  type: Support
  url: https://www.rivet.dev/discord
- group: build
  title: ''
  type: SDKs
  url: packages/rivet-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/rivet-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/rivet-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rivet-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rivet-llms.txt
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/rivet-rivetkit-asyncapi.json
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rivet-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rivet-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rivet-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rivet-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rivet-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rivet-changelog.yml
created: '2026-07-17'
description: Rivet is infrastructure for the agentic era, providing durable, stateful compute for AI agents and realtime applications. Its core primitive, Rivet Actors (RivetKit), is a runtime for long-lived processes that co-locate in-memory state with compute, support built-in WebSockets, workflows, queues, scheduling and cron, hibernate when idle, and scale from zero to thousands of instances across a global edge network. Rivet also ships agentOS, a lightweight WebAssembly-powered alternative to sandboxes for running coding agents, and Rivet Cloud, a managed serverless platform. RivetKit is open source (Apache-2.0), self-hostable on Postgres, the file system, or FoundationDB, with client SDKs for JavaScript, React, Rust, Swift and SwiftUI, a CLI, an OpenAPI-described gateway/inspector HTTP API and an AsyncAPI WebSocket protocol. Rivet is backed by Y Combinator and a16z Speedrun.
image: https://rivet.dev/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Rivet MCP Server
  slug: rivet-mcp-server
modified: '2026-07-21'
name: Rivet
nav: Providers
network: true
overview: 'Rivet publishes 2 APIs on the [APIs.io](https://apis.io/) network: Actors API and Gateway API. Tagged areas include Company, Infrastructure, Actors, Stateful Compute, and AI Agents.


  Rivet''s developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, pricing, signup flow, and 20 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 37.4
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rivet/refs/heads/main/screenshots/rivet-2026-08-17T081626.png
security:
- kind: authentication
  name: Rivet Authentication
  slug: rivet-authentication
  summary_line: bearer/custom-token · 2 schemes
- kind: domain-security
  name: Rivet Domain Security
  slug: rivet-domain-security
  summary_line: TLSv1.3
slug: rivet
tags:
- Company
- Infrastructure
- Actors
- Stateful Compute
- AI Agents
- Real-Time
- Serverless
- Edge
- WebSockets
- Durable Execution
- Developer Tools
website: https://www.rivet.dev/docs
---

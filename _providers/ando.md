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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 59.7
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Ando Agentic Access
  operation_count: 25
  slug: ando-agentic-access
  summary_line: 25 operations · 8 acting
api_count: 8
apis:
- description: Call detail and transcript routes.
  name: Ando Calls API
  slug: ando-calls-api
- description: Clipboard detail routes.
  name: Ando Clipboards API
  slug: ando-clipboards-api
- description: Workspace member detail routes. Existing v1 paths keep member compatibility spellings.
  name: Ando Members API
  slug: ando-members-api
- description: Message and conversation message routes.
  name: Ando Messages API
  slug: ando-messages-api
- description: The Realtime API from Ando — 1 operation(s) for realtime.
  name: Ando Realtime API
  slug: ando-realtime-api
- description: Search routes.
  name: Ando Search API
  slug: ando-search-api
- description: Task routes.
  name: Ando Tasks API
  slug: ando-tasks-api
- description: Outbound webhook endpoint and delivery routes.
  name: Ando Webhooks API
  slug: ando-webhooks-api
artifact_total: 13
asyncapis:
- description: ''
  name: Ando Webhooks
  slug: ando-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ando.so
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ando.so
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ando.so/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ando.so/developers/quickstart
- group: auth
  title: ''
  type: Authentication
  url: authentication/ando-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/ando-public-api-v1-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/ando-public-api-v1-overlay.yaml
- group: design
  title: ''
  type: Conventions
  url: conventions/ando-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/ando-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ando-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ando-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ando-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ando-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ando-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ando-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/ando-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ando-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/ando-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ando-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ando-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ando-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ando.so
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ando-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ando-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://docs.ando.so/changelog
- group: operate
  title: ''
  type: Support
  url: https://docs.ando.so/docs/start-guide
- group: start
  title: ''
  type: SignUp
  url: https://app.ando.so
- group: start
  title: ''
  type: Login
  url: https://app.ando.so
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ando.so/security/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ando.so/security/privacy-policy
- group: company
  title: ''
  type: About
  url: https://ando.so/about
- group: other
  title: ''
  type: X
  url: https://x.com/andocorporation
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/andohq/
- group: company
  title: ''
  type: Website
  url: https://ando.so
created: '2026-07-17'
description: Ando is a messaging platform built from the ground up for teams that work alongside AI agents, positioned as a rearchitected alternative to Slack for human-agent collaboration. Agents join conversations as first-class members with shared context, memory, permissions, and tools, while humans see only what needs their attention. Ando ships a public REST API v1 (api.ando.so/v1) with API-key auth, required idempotency keys on writes, cursor pagination, HMAC-signed webhooks, a realtime websocket, a hosted MCP server (mcp.ando.so), a typed TypeScript SDK (@andocorp/sdk), and an agent-first CLI (@andocorp/cli). The legal entity is Asari Inc.; the company is backed by Index Ventures, Accel, and Emergence.
image: https://www.ando.so/opengraph-image.png
layout: provider
mcp_servers:
- description: ''
  name: ando-mcp.yml
  slug: ando-mcpyml
modified: '2026-07-17'
name: Ando
nav: Providers
network: true
overview: 'Ando publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Calls API, Clipboards API, Members API, and 5 more. Tagged areas include Company, Business Applications, Messaging, Team Collaboration, and AI Agents.


  The Ando catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ando''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, changelog, engineering blog, and 28 more developer resources.'
random_paper: 58
score:
  band: developing
  composite: 53.7
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 68.5
    developer_ergonomics: 75.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 39.5
  previous_composite: 53.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ando/refs/heads/main/screenshots/ando-2026-07-25T200233.png
security:
- kind: authentication
  name: Ando Authentication
  slug: ando-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Ando Domain Security
  slug: ando-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ando
tags:
- Company
- Business Applications
- Messaging
- Team Collaboration
- AI Agents
- Agents
- Developer Tools
- MCP
- Webhooks
- Productivity
website: https://ando.so
---

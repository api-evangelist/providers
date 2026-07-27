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
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 71.2
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 118
  human_in_the_loop: 2
  name: Heroic Labs Agentic Access
  operation_count: 179
  slug: heroic-labs-agentic-access
  summary_line: 179 operations · 118 acting · 2 human-in-the-loop
api_count: 2
apis:
- description: The Console API from Heroic Labs — 73 operation(s) for console.
  name: Heroic Labs Console API
  slug: heroic-labs-console-api
- description: The Nakama API from Heroic Labs — 73 operation(s) for nakama.
  name: Heroic Labs Nakama API
  slug: heroic-labs-nakama-api
artifact_total: 7
asyncapis:
- description: ''
  name: Heroic Labs Nakama Realtime Events
  slug: heroic-labs-nakama-realtime-events
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/heroic-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://heroiclabs.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://heroiclabs.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://heroiclabs.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://heroiclabs.com/docs/nakama/
- group: start
  title: ''
  type: GettingStarted
  url: https://heroiclabs.com/docs/nakama/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://forum.heroiclabs.com
- group: company
  title: ''
  type: Blog
  url: https://heroiclabs.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/heroiclabs
- group: commercial
  title: ''
  type: Pricing
  url: https://heroiclabs.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://cloud.heroiclabs.com/register
- group: start
  title: ''
  type: Login
  url: https://cloud.heroiclabs.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://heroiclabs.com/tos.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://heroiclabs.com/privacypolicy.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/heroic-labs-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/heroic-labs-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/heroic-labs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/heroic-labs-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/heroic-labs-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/heroic-labs-llms.txt
- group: other
  title: ''
  type: Protobuf
  url: grpc/heroic-labs-nakama-realtime.proto
- group: design
  title: ''
  type: Conformance
  url: conformance/heroic-labs-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://heroiclabs.com/docs/heroic-cloud/enterprise/privacy-compliance/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/heroic-labs-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/heroic-labs-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/heroic-labs-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/heroic-labs-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/heroic-labs-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/heroic-labs-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/heroic-labs-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/heroic-labs-nakama-realtime-events.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Heroic Labs builds the composable game technology stack behind online, social, and multiplayer games. Its flagship product Nakama is the leading open-source game backend, providing authentication, user accounts, friends and groups, real-time and authoritative multiplayer matches, matchmaking, chat, leaderboards, tournaments, a versioned storage engine, in-app-purchase validation, and server-side runtime code in Go, TypeScript, or Lua. Satori adds a LiveOps platform (events, audiences, feature flags, experiments, and messaging) and Hiro provides a toolkit of standardized meta-game features (economy, energy, achievements, auctions). Heroic Cloud is the managed platform for deploying and scaling Nakama and Satori clusters. The company powers titles for publishers including Electronic Arts, Paradox Interactive, and Remedy.
image: https://github.com/heroiclabs.png
layout: provider
mcp_servers:
- description: ''
  name: heroic-labs-mcp.yml
  slug: heroic-labs-mcpyml
modified: '2026-07-19'
name: Heroic Labs
nav: Providers
network: true
overview: 'Heroic Labs publishes 2 APIs on the [APIs.io](https://apis.io/) network: Console API and Nakama API. Tagged areas include Company, Gaming, Game Backend, Multiplayer, and Real-Time.


  The Heroic Labs catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Heroic Labs'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
random_paper: 9
score:
  band: developing
  composite: 56.0
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 60.4
    developer_ergonomics: 87.0
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 56.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/heroic-labs/refs/heads/main/screenshots/heroic-labs-2026-07-25T221028.png
security:
- kind: authentication
  name: Heroic Labs Authentication
  slug: heroic-labs-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Heroic Labs Domain Security
  slug: heroic-labs-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: heroic-labs
tags:
- Company
- Gaming
- Game Backend
- Multiplayer
- Real-Time
- LiveOps
- Open Source
- Developer Tools
- Backend as a Service
website: https://heroiclabs.com
---

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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 52.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Sentio Agentic Access
  operation_count: 81
  slug: sentio-agentic-access
  summary_line: 81 operations · 31 acting
api_count: 11
apis:
- description: The AI API from Sentio — 4 operation(s) for ai.
  name: Sentio AI API
  slug: sentio-ai-api
- description: The Alerts API from Sentio — 4 operation(s) for alerts.
  name: Sentio Alerts API
  slug: sentio-alerts-api
- description: The Data API from Sentio — 25 operation(s) for data.
  name: Sentio Data API
  slug: sentio-data-api
- description: The Debug and Simulation API from Sentio — 9 operation(s) for debug and simulation.
  name: Sentio Debug and Simulation API
  slug: sentio-debug-and-simulation-api
- description: The Forks API from Sentio — 8 operation(s) for forks.
  name: Sentio Forks API
  slug: sentio-forks-api
- description: The Move API from Sentio — 2 operation(s) for move.
  name: Sentio Move API
  slug: sentio-move-api
- description: The Price API from Sentio — 5 operation(s) for price.
  name: Sentio Price API
  slug: sentio-price-api
- description: The Prices API from Sentio — 6 operation(s) for prices.
  name: Sentio Prices API
  slug: sentio-prices-api
- description: The Processor API from Sentio — 2 operation(s) for processor.
  name: Sentio Processor API
  slug: sentio-processor-api
- description: The ProcessorExt API from Sentio — 1 operation(s) for processorext.
  name: Sentio ProcessorExt API
  slug: sentio-processorext-api
- description: The Web API from Sentio — 8 operation(s) for web.
  name: Sentio Web API
  slug: sentio-web-api
artifact_total: 16
asyncapis:
- description: ''
  name: Sentio Webhooks
  slug: sentio-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sentio-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sentio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sentio-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sentio.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sentio.xyz/docs/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sentio.xyz/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sentio.xyz/docs/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://app.sentio.xyz/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sentio.xyz/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.sentio.xyz/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sentio.xyz/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sentio.xyz/privacy
- group: operate
  title: ''
  type: Support
  url: https://docs.sentio.xyz/docs/getting-support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sentioxyz
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.sentio.xyz/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sentio.xyz
- group: other
  title: ''
  type: X
  url: https://twitter.com/sentioxyz
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/vSdkMYqnjb
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sentio-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/sentio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sentio-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/sentio-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sentio-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sentio-well-known.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sentio-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sentio-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sentio-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sentio-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sentio-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sentio-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sentio-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Sentio is a developer-first, AI-powered Web3 data and observability platform for building, monitoring, and debugging on-chain applications. It provides indexing processors and hosted subgraphs across EVM, Aptos, Sui, IOTA, Solana and Fuel; a Data API that turns SQL or GraphQL into REST endpoints; metrics, event logs, dashboards and alerts; a crypto price API; and a transaction debugger with forks, simulations and call-trace/fund-tracing tools. Sentio exposes a REST API at api.sentio.xyz (api-key auth), TypeScript SDK and CLI, webhooks, and an official Model Context Protocol server. Backed by Lightspeed Faction and added to the API Evangelist network; profile enriched from Sentio's published developer surface.
image: https://www.sentio.xyz/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: sentio-mcp.yml
  slug: sentio-mcpyml
modified: '2026-07-21'
name: Sentio
nav: Providers
network: true
overview: 'Sentio publishes 11 APIs on the [APIs.io](https://apis.io/) network, including AI API, Alerts API, Data API, and 8 more. Tagged areas include Web3, Blockchain, Observability, Analytics, and Data.


  The Sentio catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sentio''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, pricing, engineering blog, and 25 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 55.4
  delta: -0.3
  facets:
    commercial_clarity: 44.7
    contract_quality: 59.5
    developer_ergonomics: 75.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 55.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Sentio Authentication
  slug: sentio-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Sentio Domain Security
  slug: sentio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sentio
tags:
- Web3
- Blockchain
- Observability
- Analytics
- Data
- Indexing
- Monitoring
- Developer Tools
- Crypto
- API
website: https://docs.sentio.xyz
---

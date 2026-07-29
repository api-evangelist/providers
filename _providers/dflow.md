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
    agent_skills: true
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Dflow Agentic Access
  operation_count: 14
  slug: dflow-agentic-access
  summary_line: 14 operations · 3 acting
api_count: 7
apis:
- description: The admin API from DFlow — 1 operation(s) for admin.
  name: DFlow admin API
  slug: dflow-admin-api
- description: Intent trading endpoints
  name: DFlow intent API
  slug: dflow-intent-api
- description: Order API endpoints
  name: DFlow order API
  slug: dflow-order-api
- description: Prediction market endpoints
  name: DFlow prediction_market API
  slug: dflow-prediction-market-api
- description: Swap API endpoints
  name: DFlow swap API
  slug: dflow-swap-api
- description: Token endpoints
  name: DFlow tokens API
  slug: dflow-tokens-api
- description: Venue endpoints
  name: DFlow venues API
  slug: dflow-venues-api
artifact_total: 12
asyncapis:
- description: DERIVED event surface for the DFlow Trading API real-time WebSocket streams. Modeled by API Evangelist from the published DFlow docs (https://pond.dflow.net/resources/trading-api/websockets/overview a
  name: DFlow Trading API WebSocket Streams
  slug: dflow-trading-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://dflow.net
- group: start
  title: ''
  type: DeveloperPortal
  url: https://pond.dflow.net
- group: docs
  title: ''
  type: Documentation
  url: https://pond.dflow.net/resources/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://pond.dflow.net/resources/trading-api/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://pond.dflow.net/get-started/what-is-dflow
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DFlowProtocol
- group: operate
  title: ''
  type: Support
  url: https://t.me/+GubbVyulzDFjZTkx
- group: start
  title: ''
  type: SignUp
  url: https://forms.gle/eX3cghbMF8VBB9qa9
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dflow-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dflow-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/dflow-spot-trading.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/dflow-platform-fees.md
- group: build
  title: ''
  type: CLI
  url: cli/dflow-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/dflow-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dflow-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dflow-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dflow-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dflow-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dflow-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/dflow-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dflow-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dflow-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dflow-domain-security.yml
created: '2026-07-17'
description: 'DFlow is a trading protocol and aggregator for spot trading natively on Solana, offering a Trading API that powers tens of billions of dollars in transacted value for traders, applications, and financial institutions. It provides imperative and declarative (intent-based) swaps, JIT routing across liquidity venues, MEV / sandwich protection, priority-fee and slippage controls, builder platform-fee monetization (platformFeeBps), sponsored (gasless) swaps, WebSocket market-data streams (quotes, order-book depth, priority fees), and prediction-market initialization. DFlow is agent-native: a single-binary agent CLI with an encrypted local wallet, published Claude Code Skills, and a hosted documentation MCP server. Authentication is via an x-api-key header; REST responses can be cryptographically signed with ed25519 per RFC 9421. Backed by Multicoin Capital.'
image: https://dflow.net/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: dflow-mcp.yml
  slug: dflow-mcpyml
modified: '2026-07-18'
name: DFlow
nav: Providers
network: true
overview: 'DFlow publishes 7 APIs on the [APIs.io](https://apis.io/) network, including admin API, intent API, order API, and 4 more. Tagged areas include Company, Crypto Web3, Solana, Trading API, and DeFi.


  The DFlow catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  DFlow''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, CLI, authentication, and 16 more developer resources.'
random_paper: 66
score:
  band: developing
  composite: 44.8
  delta: 0.4
  facets:
    commercial_clarity: 13.2
    contract_quality: 60.5
    developer_ergonomics: 78.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dflow/refs/heads/main/screenshots/dflow-2026-07-25T211845.png
security:
- kind: authentication
  name: Dflow Authentication
  slug: dflow-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dflow Domain Security
  slug: dflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dflow
tags:
- Company
- Crypto Web3
- Solana
- Trading API
- DeFi
- DEX Aggregator
- Token Swap
- Blockchain
- MEV Protection
- Prediction Markets
- Agent Ready
website: https://dflow.net
---

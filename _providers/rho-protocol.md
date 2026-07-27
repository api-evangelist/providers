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
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 77.9
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Rho Protocol Agentic Access
  operation_count: 23
  slug: rho-protocol-agentic-access
  summary_line: 23 operations · 4 acting
api_count: 4
apis:
- description: The Market Data API from Rho Protocol — 7 operation(s) for market data.
  name: Rho Protocol Market Data API
  slug: rho-protocol-market-data-api
- description: The Stats API from Rho Protocol — 1 operation(s) for stats.
  name: Rho Protocol Stats API
  slug: rho-protocol-stats-api
- description: The Trading API from Rho Protocol — 3 operation(s) for trading.
  name: Rho Protocol Trading API
  slug: rho-protocol-trading-api
- description: The User Data API from Rho Protocol — 12 operation(s) for user data.
  name: Rho Protocol User Data API
  slug: rho-protocol-user-data-api
artifact_total: 10
asyncapis:
- description: Real-time streaming of market data, order updates, and account state for Rho X (Rho Exchange). Private channels require a WS session token (POST /auth-api/v1/ws-session).
  name: Rho X WebSocket API
  slug: rho-protocol-ws-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rho-protocol-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.rho.trading/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rho.trading/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.rho.trading/api-reference/rest-api-reference.md
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.rho.trading/getting-started/quick-start-first-trade.md
- group: auth
  title: ''
  type: Authentication
  url: authentication/rho-protocol-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://x.rho.trading/
- group: company
  title: ''
  type: Blog
  url: https://docs.rho.trading/
- group: operate
  title: ''
  type: Support
  url: https://docs.rho.trading/faq-and-support/contact-support.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RhoLabs
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/rho-protocol-openapi-original.json
- group: other
  title: ''
  type: Overlay
  url: overlays/rho-protocol-openapi-overlay.yaml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/rho-protocol-ws-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/rho-protocol-ws-asyncapi.yml
- group: build
  title: ''
  type: Packages
  url: packages/rho-protocol-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/rho-protocol-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rho-protocol-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rho-protocol-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rho-protocol-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rho-protocol-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rho-protocol-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/rho-protocol-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rho-protocol-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rho-protocol-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rho-protocol-rate-limits.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rho-protocol-agentic-access.yml
created: '2026-07-17'
description: Rho Protocol (Rho Labs) operates Rho X, a decentralized multi-asset trading and settlement layer for on-chain capital markets — interest-rate futures, perpetuals, and tokenized real-world assets tradable from a single cross-margined account. It offers off-exchange collateral custody (BitGo OES or self-custody), zero-gas settlement, and a private cross-chain RFQ swap service (Rho Relay) bridging Ethereum and Canton Network assets. Rho X exposes a REST API, a WebSocket streaming API, an npm SDK, and an official Model Context Protocol (MCP) server for programmatic trading, market data, and account management. Backed by Speedinvest.
image: https://github.com/RhoLabs.png
layout: provider
mcp_servers:
- description: ''
  name: rho-protocol-mcp.yml
  slug: rho-protocol-mcpyml
modified: '2026-07-21'
name: Rho Protocol
nav: Providers
network: true
overview: 'Rho Protocol publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Market Data API, Stats API, Trading API, and 1 more. Tagged areas include Company, Trading, DeFi, Derivatives, and Capital Markets.


  The Rho Protocol catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Rho Protocol''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, and 21 more developer resources.'
random_paper: 32
rate_limits:
- limit_count: 0
  name: Rho Protocol Rate Limits
  slug: rho-protocol-rate-limits
score:
  band: thin
  composite: 41.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 60.4
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 41.8
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Rho Protocol Authentication
  slug: rho-protocol-authentication
  summary_line: apiKey/http-bearer · 1 scheme
- kind: domain-security
  name: Rho Protocol Domain Security
  slug: rho-protocol-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rho-protocol
tags:
- Company
- Trading
- DeFi
- Derivatives
- Capital Markets
- Blockchain
- Market Data
- WebSocket
- MCP
website: https://x.rho.trading/
---

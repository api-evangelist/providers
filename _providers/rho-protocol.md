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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.2
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Rho Protocol Agentic Access
  operation_count: 23
  slug: rho-protocol-agentic-access
  summary_line: 23 operations · 4 acting
api_count: 1
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
artifact_total: 15
asyncapis:
- description: Real-time streaming of market data, order updates, and account state for Rho X (Rho Exchange). Private channels require a WS session token (POST /auth-api/v1/ws-session).
  name: Rho X WebSocket API
  slug: rho-protocol-ws-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rho Exchange Market Data API
  slug: open-rho-protocol-market-data-api
- collection_type: open
  name: Rho Exchange Market Data Stats API
  slug: open-rho-protocol-stats-api
- collection_type: open
  name: Rho Exchange Market Data Trading API
  slug: open-rho-protocol-trading-api
- collection_type: open
  name: Rho Exchange Market Data User Data API
  slug: open-rho-protocol-user-data-api
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
  url: openapi/_original/rho-protocol-openapi-original.json
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
  name: Rho Protocol MCP Server
  slug: rho-protocol-mcp-server
modified: '2026-07-21'
name: Rho Protocol
nav: Providers
network: true
overview: 'Rho Protocol publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Market Data API, Stats API, Trading API, and 1 more. Tagged areas include Company, Trading, DeFi, Derivatives, and Capital Markets.


  The Rho Protocol catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Rho Protocol''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, and 21 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 1
  name: Rho Protocol Rate Limits
  slug: rho-protocol-rate-limits
score:
  band: thin
  composite: 38.8
  coverage:
    artifact_dirs: 18
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 53.6
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 39.5
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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

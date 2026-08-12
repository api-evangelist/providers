---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.5
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 67
  human_in_the_loop: 4
  name: Orderly Network Agentic Access
  operation_count: 248
  slug: orderly-network-agentic-access
  summary_line: 248 operations · 67 acting · 4 human-in-the-loop
api_count: 4
apis:
- description: The admin API from Orderly Network — 1 operation(s) for admin.
  name: Orderly Network admin API
  slug: orderly-network-admin-api
- description: The client API from Orderly Network — 1 operation(s) for client.
  name: Orderly Network client API
  slug: orderly-network-client-api
- description: The private API from Orderly Network — 137 operation(s) for private.
  name: Orderly Network private API
  slug: orderly-network-private-api
- description: The public API from Orderly Network — 97 operation(s) for public.
  name: Orderly Network public API
  slug: orderly-network-public-api
artifact_total: 9
asyncapis:
- description: Real-time WebSocket streams for Orderly Network. Public streams carry market data (orderbook, trades, ticker, klines); private streams carry authenticated account, balance, position, and execution-rep
  name: Orderly Network WebSocket API
  slug: orderly-network-websocket-asyncapi
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/orderly-network-evm-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://orderly.network/docs/sdks/overview
- group: docs
  title: ''
  type: Documentation
  url: https://orderly.network/docs/introduction/getting-started/what-is-orderly
- group: docs
  title: ''
  type: APIReference
  url: https://orderly.network/docs/build-on-omnichain/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://orderly.network/docs/introduction/getting-started/builder-onboarding
- group: company
  title: ''
  type: Blog
  url: https://orderly.network/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OrderlyNetwork
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/OrderlyNetwork
- group: commercial
  title: ''
  type: TermsOfService
  url: https://orderly.network/docs/introduction/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://orderly.network/docs/introduction/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/orderly-network-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/orderly-network-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/orderly-network-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/orderly-network-cli.yml
- group: design
  title: ''
  type: Components
  url: components/orderly-network-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/orderly-network-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/orderly-network-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/orderly-network-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/orderly-network-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/orderly-network-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/orderly-network-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/orderly-network-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/orderly-network-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/orderly-network-sandbox.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/orderly-network-websocket-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/orderly-network-websocket-asyncapi.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/orderly-network-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orderly-network-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://orderly.network/
created: '2026-07-17'
description: Orderly Network is an omnichain, orderbook-based trading infrastructure that provides perpetual-futures liquidity for decentralized exchanges and builders. It exposes a full EVM REST API and WebSocket streams for order management, account and sub-account handling, cross-chain deposits/withdrawals, positions, settlement, and market data, plus a Strategy Vault API and a zero-auth Public Info API aimed at AI agents and analytics. Authentication uses ed25519 request signing with registered Orderly Keys. Builders integrate via React component and hooks SDKs, a devkit CLI, a Builders Marketplace plugin system, and an official MCP server. Markets use the PERP_<TOKEN>_USDC symbol format across a public mainnet and testnet.
image: https://raw.githubusercontent.com/OrderlyNetwork/documentation-public/main/logo/light.svg
layout: provider
mcp_servers:
- description: ''
  name: orderly-network-mcp.yml
  slug: orderly-network-mcpyml
modified: '2026-07-20'
name: Orderly Network
nav: Providers
network: true
overview: 'Orderly Network publishes 4 APIs on the [APIs.io](https://apis.io/) network, including admin API, client API, private API, and 1 more. Tagged areas include Company, Crypto, DeFi, Trading, and Perpetual Futures.


  The Orderly Network catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Orderly Network''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, CLI, authentication, and 23 more developer resources.'
random_paper: 84
score:
  band: developing
  composite: 47.1
  delta: -1.4
  facets:
    commercial_clarity: 21.1
    contract_quality: 56.6
    developer_ergonomics: 82.1
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 48.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
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
    score: 41.7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/orderly-network/refs/heads/main/screenshots/orderly-network-2026-08-07T190918.png
security:
- kind: authentication
  name: Orderly Network Authentication
  slug: orderly-network-authentication
  summary_line: signature · 1 scheme
- kind: domain-security
  name: Orderly Network Domain Security
  slug: orderly-network-domain-security
  summary_line: TLSv1.3 · DMARC
slug: orderly-network
tags:
- Company
- Crypto
- DeFi
- Trading
- Perpetual Futures
- Derivatives
- Orderbook
- Web3
- Blockchain
- Liquidity
website: https://orderly.network/
---

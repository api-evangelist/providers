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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-27'
api_count: 7
apis:
- description: The Assets API from Tristero — 1 operation(s) for assets.
  name: Tristero Assets API
  slug: tristero-assets-api
- description: Margin position management
  name: Tristero Margin API
  slug: tristero-margin-api
- description: Submit and manage orders
  name: Tristero Orders API
  slug: tristero-orders-api
- description: The Pricing API from Tristero — 1 operation(s) for pricing.
  name: Tristero Pricing API
  slug: tristero-pricing-api
- description: Request quotes for swaps and margin positions
  name: Tristero Quotes API
  slug: tristero-quotes-api
- description: The Trading API from Tristero — 2 operation(s) for trading.
  name: Tristero Trading API
  slug: tristero-trading-api
- description: Wallet and position queries
  name: Tristero Wallets API
  slug: tristero-wallets-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tristero-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tristero-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://tristero.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tristero.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tristero.com/docs/tristero
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tristero.com/docs/tristero/api/getQuote
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tristero.com/docs/feather/quickstart
- group: company
  title: ''
  type: Blog
  url: https://tristero.substack.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tristeroresearch
- group: start
  title: ''
  type: Login
  url: https://app.tristero.com
- group: operate
  title: ''
  type: Support
  url: mailto:outreach@tristero.com
- group: company
  title: ''
  type: Twitter
  url: https://x.com/0xtristero
- group: build
  title: ''
  type: Packages
  url: packages/tristero-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tristero-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tristero-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tristero-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tristero-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/tristero-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tristero-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tristero-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tristero-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tristero-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tristero-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Tristero is a trustless, cross-chain trading protocol backed by General Catalyst. On-chain traders use its API and Python/TypeScript SDKs to access deep liquidity across DEXs and CEXs for spot swaps of ERC-20 tokens across EVM chains (via Permit2 / EIP-712 signed orders), leveraged margin positions up to 10x, and cross-VM swaps into non-EVM assets like Bitcoin, Monero, and Litecoin through its Feather balance-sheet swap relay. Execution is non-custodial and MEV-protected, with real-time quote streaming over WebSocket, and the company's research roots are in on-chain dark pools and encrypted order matching.
image: https://docs.tristero.com/tristero.png
layout: provider
mcp_servers:
- description: ''
  name: tristero-mcp.yml
  slug: tristero-mcpyml
modified: '2026-07-21'
name: Tristero
nav: Providers
network: true
overview: 'Tristero publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Margin API, Orders API, and 4 more. Tagged areas include Company, Cryptocurrency, Trading, DeFi, and Cross-Chain.


  Tristero''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, support, sandbox, and 17 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 42.6
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 56.8
    developer_ergonomics: 80.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 42.6
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
  name: Tristero Authentication
  slug: tristero-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tristero Domain Security
  slug: tristero-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tristero
tags:
- Company
- Cryptocurrency
- Trading
- DeFi
- Cross-Chain
- Web3
- Margin Trading
- Dark Pools
website: https://tristero.com
---

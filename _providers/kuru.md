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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 61.5
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: The Generate Token API from Kuru — 1 operation(s) for generate token.
  name: Kuru Generate Token API
  slug: kuru-generate-token-api
- description: The Quote API from Kuru — 1 operation(s) for quote.
  name: Kuru Quote API
  slug: kuru-quote-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.kuru.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.kuru.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kuru.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kuru.io/api-reference/generate-jwt-token
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kuru.io/sdk/quickstart-sdk
- group: company
  title: ''
  type: Blog
  url: https://blog.kuru.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kuru-Labs
- group: operate
  title: ''
  type: StatusPage
  url: lifecycle/kuru-lifecycle.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.kuru.io/liquidity/how-fees-work
- group: start
  title: ''
  type: SignUp
  url: https://www.kuru.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.kuru.io/legal/tradingview
- group: build
  title: ''
  type: Packages
  url: packages/kuru-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kuru-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/kuru-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kuru-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kuru-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kuru-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kuru-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kuru-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kuru-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kuru-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kuru-data-model.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kuru-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kuru-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kuru-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kuru-domain-security.yml
created: '2026-07-17'
description: Kuru is a fully on-chain central limit order book (CLOB) decentralized exchange and smart routing aggregator built on Monad, operated by Kuru Labs. It combines an on-chain order book with AMM vault liquidity to deliver low-slippage, self-custody trading, and exposes the Kuru Flow API — a liquidity-aggregating routing engine that lets wallets, dApps and aggregators quote and build any-token-to-any-token swaps across every market on Monad, optionally appending their own referrer fee. Developers integrate through a TypeScript SDK, a Python CLOB SDK for market making, published and audited Solidity contracts, and a first-party agent skill for automated trading.
image: https://www.kuru.io/favicon-96x96.png
layout: provider
mcp_servers:
- description: ''
  name: kuru-mcp.yml
  slug: kuru-mcpyml
modified: '2026-07-19'
name: Kuru
nav: Providers
network: true
overview: 'Kuru publishes 2 APIs on the [APIs.io](https://apis.io/) network: Generate Token API and Quote API. Tagged areas include Company, DeFi, Decentralized Exchange, Order Book, and Trading.


  Kuru''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, CLI, and 20 more developer resources.'
random_paper: 47
rate_limits:
- limit_count: 1
  name: Kuru Rate Limits
  slug: kuru-rate-limits
score:
  band: developing
  composite: 51.4
  delta: -1.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 57.1
    developer_ergonomics: 82.6
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 52.4
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 45.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Kuru Authentication
  slug: kuru-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Kuru Domain Security
  slug: kuru-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: kuru
tags:
- Company
- DeFi
- Decentralized Exchange
- Order Book
- Trading
- Blockchain
- Monad
- Liquidity
- Swaps
- Web3
website: https://www.kuru.io/
---

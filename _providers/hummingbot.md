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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.6
  scored_at: '2026-08-11'
api_count: 17
apis:
- description: 'The Hummingbot API is a FastAPI backend service (default port 8000) that orchestrates multiple trading bots and exposes REST routers for accounts and exchange credentials, trading (orders, positions, '
  name: Hummingbot API
  slug: hummingbot-api
- description: Ethereum and EVM-based chain endpoints
  name: Hummingbot /chain/ethereum API
  slug: hummingbot-chain-ethereum-api
- description: Solana and SVM-based chain endpoints
  name: Hummingbot /chain/solana API
  slug: hummingbot-chain-solana-api
- description: System configuration endpoints
  name: Hummingbot /config API
  slug: hummingbot-config-api
- description: 0x connector endpoints
  name: Hummingbot /connector/0x API
  slug: hummingbot-connector-0x-api
- description: Jupiter connector endpoints
  name: Hummingbot /connector/jupiter API
  slug: hummingbot-connector-jupiter-api
- description: Meteora connector endpoints
  name: Hummingbot /connector/meteora API
  slug: hummingbot-connector-meteora-api
- description: Orca connector endpoints
  name: Hummingbot /connector/orca API
  slug: hummingbot-connector-orca-api
- description: PancakeSwap EVM connector endpoints
  name: Hummingbot /connector/pancakeswap API
  slug: hummingbot-connector-pancakeswap-api
- description: PancakeSwap Solana connector endpoints
  name: Hummingbot /connector/pancakeswap-sol API
  slug: hummingbot-connector-pancakeswap-sol-api
- description: Raydium connector endpoints
  name: Hummingbot /connector/raydium API
  slug: hummingbot-connector-raydium-api
- description: Uniswap connector endpoints
  name: Hummingbot /connector/uniswap API
  slug: hummingbot-connector-uniswap-api
- description: Pool management endpoints
  name: Hummingbot /pools API
  slug: hummingbot-pools-api
- description: Token management endpoints
  name: Hummingbot /tokens API
  slug: hummingbot-tokens-api
- description: Unified cross-chain CLMM (Concentrated Liquidity) endpoints
  name: Hummingbot /trading/clmm API
  slug: hummingbot-trading-clmm-api
- description: Unified cross-chain swap endpoints
  name: Hummingbot /trading/swap API
  slug: hummingbot-trading-swap-api
- description: Wallet management endpoints
  name: Hummingbot /wallet API
  slug: hummingbot-wallet-api
artifact_total: 21
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/hummingbot-gateway-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hummingbot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hummingbot.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hummingbot.org/
- group: docs
  title: ''
  type: Documentation
  url: https://hummingbot.org/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://hummingbot.org/hummingbot-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://hummingbot.org/installation/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hummingbot
- group: company
  title: ''
  type: Blog
  url: https://hummingbot.org/blog/
- group: operate
  title: ''
  type: Support
  url: https://hummingbot.org/community/
- group: commercial
  title: ''
  type: License
  url: https://github.com/hummingbot/hummingbot/blob/master/LICENSE
- group: operate
  title: ''
  type: ChangeLog
  url: https://hummingbot.org/release-notes/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hummingbot-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/hummingbot-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hummingbot-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hummingbot-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hummingbot-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/hummingbot-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hummingbot-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hummingbot-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hummingbot-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hummingbot-lifecycle.yml
- group: build
  title: ''
  type: CLI
  url: cli/hummingbot-cli.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hummingbot-conformance.yml
created: '2026-07-17'
description: 'Hummingbot is an open source Python framework, maintained by the Hummingbot Foundation, that lets traders build and run automated, high-frequency crypto trading strategies across both centralized (CEX) and decentralized (DEX) venues. The project ships several developer-facing components: the Hummingbot client (a CLI trading bot), Gateway (a TypeScript middleware that standardizes DEX/blockchain endpoints behind one REST API on port 15888, documented with a published OpenAPI spec), the Hummingbot API (a FastAPI REST server on port 8000 that orchestrates multiple bots, accounts, portfolios, and market data), an async Python API client, an official Model Context Protocol (MCP) server, and a set of open Agent Skills for AI trading agents. With 300+ exchange connectors and Apache-2.0 licensing, Hummingbot reports having facilitated tens of billions of dollars in trade volume across 100K+ deployed instances.'
image: https://github.com/hummingbot.png
layout: provider
mcp_servers:
- description: ''
  name: hummingbot-mcp.yml
  slug: hummingbot-mcpyml
modified: '2026-07-19'
name: Hummingbot
nav: Providers
network: true
overview: 'Hummingbot publishes 16 APIs on the [APIs.io](https://apis.io/) network, including /chain/ethereum API, /chain/solana API, /config API, and 13 more. Tagged areas include Company, Crypto, Trading, Blockchain, and DeFi.


  Hummingbot''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, authentication, and 18 more developer resources.'
random_paper: 38
rate_limits:
- limit_count: 1
  name: Hummingbot Rate Limits
  slug: hummingbot-rate-limits
score:
  band: thin
  composite: 38.2
  delta: -1.2
  facets:
    commercial_clarity: 0.0
    contract_quality: 39.1
    developer_ergonomics: 80.4
    discoverability: 72.2
    governance: 11.5
    operational_transparency: 42.1
  previous_composite: 39.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hummingbot/refs/heads/main/screenshots/hummingbot-2026-07-25T221727.png
security:
- kind: authentication
  name: Hummingbot Authentication
  slug: hummingbot-authentication
  summary_line: http-basic/passphrase/mtls-optional · 3 schemes
- kind: domain-security
  name: Hummingbot Domain Security
  slug: hummingbot-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hummingbot
tags:
- Company
- Crypto
- Trading
- Blockchain
- DeFi
- DEX
- Open Source
- Market Making
- Algorithmic Trading
- Bots
website: https://hummingbot.io/
---

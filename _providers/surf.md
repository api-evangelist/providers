---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-06'
api_count: 16
apis:
- description: OpenAI-style Chat/Research API. POST /responses with a surf-2.0 or surf-2.0-instant model and a natural-language crypto question; returns synthesized answers with inline citations drawn from live mark
  name: Surf Chat API
  slug: surf-chat-api
- description: The DEX API from Surf — 1 operation(s) for dex.
  name: Surf DEX API
  slug: surf-dex-api
- description: Access real-time trading data from major exchanges including Binance, OKX, Bybit, and more. Query live ticker prices, order book depth, OHLCV candlestick charts, and perpetual contract data such as fu
  name: Surf Exchange API
  slug: surf-exchange-api
- description: Explore crypto venture capital. Look up fund profiles with team info and social links, browse their full investment portfolio with round details, and rank funds by tier or portfolio size.
  name: Surf Fund API
  slug: surf-fund-api
- description: The Hyperliquid API from Surf — 9 operation(s) for hyperliquid.
  name: Surf Hyperliquid API
  slug: surf-hyperliquid-api
- description: Get a high-level view of the crypto market. Browse token rankings by market cap or volume, track derivatives across all exchanges, monitor spot ETF fund flows, view liquidation events, compute technic
  name: Surf Market API
  slug: surf-market-api
- description: Stay up to date with crypto news. Browse the latest articles from major crypto media outlets, read full article content, and search across all sources by keyword.
  name: Surf News API
  slug: surf-news-api
- description: Query blockchain data directly. Look up transaction details by hash, check gas prices, and run structured or raw SQL queries against indexed blockchain datasets spanning Ethereum, Base, Solana, and mo
  name: Surf Onchain API
  slug: surf-onchain-api
- description: Track prediction markets on Polymarket and Kalshi. Browse events and markets, view live prices and odds, analyze trading volume and open interest history, inspect individual trades, and discover top-r
  name: Surf Prediction Market API
  slug: surf-prediction-market-api
- description: Research crypto projects in depth. Retrieve aggregated project profiles covering overview, team, funding rounds, tokenomics, social links, and TGE status. Track DeFi protocol metrics like TVL, fees, r
  name: Surf Project API
  slug: surf-project-api
- description: Find anything across Surf's data universe. Search for crypto projects, X (Twitter) accounts and posts, news articles, wallet addresses, web pages, investment funds, airdrop opportunities, and predicti
  name: Surf Search API
  slug: surf-search-api
- description: Explore ranked project signal score snapshots, token-of-day/week highlights, and project-level signal cards with latest price, price-change, dimension scores, compact signals, and AI summaries.
  name: Surf Signal API
  slug: surf-signal-api
- description: Monitor crypto social activity on X (Twitter). Look up user profiles and their posts, track project sentiment scores and follower geography, discover smart followers, and analyze mindshare trends over
  name: Surf Social API
  slug: surf-social-api
- description: Analyze individual tokens on-chain. Look up top holders and their share of supply, track ERC-20/SPL token transfers, browse DEX swap history, and view upcoming token unlock schedules with allocation b
  name: Surf Token API
  slug: surf-token-api
- description: Inspect any wallet on Ethereum, Base, Solana, and other chains. View token balances, NFT holdings, entity labels, transfer history, full transaction logs, DeFi protocol positions (lending, staking, LP
  name: Surf Wallet API
  slug: surf-wallet-api
- description: Fetch and search web content. Retrieve any URL and convert it to clean, LLM-friendly markdown, or search the internet for crypto-related articles, reports, and resources.
  name: Surf Web API
  slug: surf-web-api
artifact_total: 19
common:
- group: company
  title: ''
  type: Website
  url: https://asksurf.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agents.asksurf.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://agents.asksurf.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://agents.asksurf.ai/docs/data-api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://agents.asksurf.ai/docs/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://agents.asksurf.ai/docs/pricing
- group: start
  title: ''
  type: SignUp
  url: https://agents.asksurf.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/asksurf-ai
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/surf-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/surf-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/surf-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/surf-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/surf-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/surf-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/surf-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/surf-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: CLI
  url: cli/surf-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/surf-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/surf-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/surf-domain-security.yml
created: '2026-07-17'
description: Surf (asksurf.ai) is a crypto-focused AI research and execution platform that exposes its intelligence as a developer API. The Surf Data API ("Hermod" gateway) provides 119 typed REST endpoints across 14 domains — exchange and market data, tokens, DeFi projects, wallets, on-chain SQL, social signals, news, funds, prediction markets (Polymarket/Kalshi), Hyperliquid perps, search, and web fetch — covering 40+ blockchains and 200+ data sources. A separate OpenAI-style Chat API (surf-2.0 / surf-2.0-instant models) answers natural-language crypto research questions with citations. Access is via a single Bearer API key with credit-based billing (30 free credits/day, no signup), and the platform ships a Go CLI, an MCP server, an Agent Skill, and a TypeScript SDK. Surf is backed by Pantera Capital.
image: https://asksurf.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: surf-mcp.yml
  slug: surf-mcpyml
modified: '2026-07-21'
name: Surf
nav: Providers
network: true
overview: 'Surf publishes 15 APIs on the [APIs.io](https://apis.io/) network, including DEX API, Exchange API, Fund API, and 12 more. Tagged areas include Company, Crypto, Blockchain, Market Data, and On-Chain Analytics.


  Surf''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, authentication, CLI, and 14 more developer resources.'
random_paper: 109
score:
  band: developing
  composite: 42.8
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 58.1
    developer_ergonomics: 73.9
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 42.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Surf Authentication
  slug: surf-authentication
  summary_line: http/apiKey · 3 schemes
- kind: domain-security
  name: Surf Domain Security
  slug: surf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: surf
tags:
- Company
- Crypto
- Blockchain
- Market Data
- On-Chain Analytics
- Wallet Intelligence
- AI
- DeFi
- Prediction Markets
- Developer API
website: https://asksurf.ai/
---

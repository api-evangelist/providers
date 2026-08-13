---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.3
  scored_at: '2026-08-12'
api_count: 3
apis:
- description: Programmatic control over a Mudrex futures trading account. Transfer funds between the spot and futures wallets (USDT and INR), list tradeable instruments and contract specifications, get and set leve
  name: Mudrex Futures Trading API
  slug: mudrex-futures-trading-api
- description: 'Public, unauthenticated market-data surface for Mudrex linear perpetual futures. Over REST it returns bulk historical OHLCV price klines (GET /price/kline, up to 25 assets and 1440 candles per asset) '
  name: Mudrex Market Data API
  slug: mudrex-market-data-api
- description: Mudrex's official hosted Model Context Protocol server, which exposes the Mudrex Futures Trading API to MCP-capable AI assistants as 20 tools across orders, positions, risk management (stop-loss/take-
  name: Mudrex MCP Server
  slug: mudrex-mcp-server
artifact_total: 9
asyncapis:
- description: ''
  name: Mudrex Market Data Streams
  slug: mudrex-market-data-streams
common:
- group: company
  title: ''
  type: Website
  url: https://mudrex.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mudrex.com/pro-trading
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trade.mudrex.com/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.trade.mudrex.com/docs/quick-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.trade.mudrex.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://mudrex.com/support
- group: company
  title: ''
  type: Blog
  url: https://mudrex.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mudrex
- group: commercial
  title: ''
  type: Pricing
  url: https://mudrex.com/fee-and-compliance
- group: start
  title: ''
  type: SignUp
  url: https://mudrex.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mudrex.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mudrex.com/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://mudrex.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/mudrex-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mudrex-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mudrex-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mudrex-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mudrex-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mudrex-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mudrex-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mudrex-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mudrex-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mudrex-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/mudrex-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mudrex-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mudrex-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/mudrex-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mudrex-llms.txt
created: '2026-08-04'
description: Mudrex is a US-headquartered, Bengaluru-based crypto investment and trading platform founded in 2018 and registered with India's Financial Intelligence Unit (FIU-IND). It serves retail and pro traders with spot trading, curated Coin Sets, and USDT- and INR-margined perpetual futures. Its developer surface is the Mudrex Futures API — a REST trading API under https://trade.mudrex.com/fapi/v1 covering wallet transfers, asset discovery, leverage and margin type, order create/amend/cancel, position management with stop-loss/take-profit, liquidation pricing and fee history — plus a public, unauthenticated market-data surface (historical price and mark-price klines over REST, live kline/mark-kline/ticker streams over WebSocket) and an officially hosted MCP server at https://mudrex.com/mcp that exposes 20 trading tools to AI agents. Authentication is a single X-Authentication API-key header issued after KYC and TOTP two-factor enrollment. An official Python SDK ships on PyPI as mudrex-sdk.
image: https://mudrex.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: mudrex-mcp.yml
  slug: mudrex-mcpyml
modified: '2026-08-04'
name: Mudrex
nav: Providers
network: true
overview: 'Mudrex publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Trading, Futures, and Financial Services.


  The Mudrex catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Mudrex''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
random_paper: 61
rate_limits:
- limit_count: 13
  name: Mudrex Rate Limits
  slug: mudrex-rate-limits
score:
  band: developing
  composite: 54.5
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.6
    developer_ergonomics: 69.0
    discoverability: 81.5
    governance: 12.5
    operational_transparency: 52.6
  previous_composite: 54.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 50.0
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mudrex/refs/heads/main/screenshots/mudrex-2026-08-07T184429.png
security:
- kind: authentication
  name: Mudrex Authentication
  slug: mudrex-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Mudrex Domain Security
  slug: mudrex-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Mudrex Trust Center
  slug: mudrex-trust-center
  summary_line: ISO 27001:2022, SOC 2 Type II
slug: mudrex
tags:
- Company
- Cryptocurrency
- Trading
- Futures
- Financial Services
- Fintech
- Market Data
- Exchange
- India
website: https://mudrex.com/
---

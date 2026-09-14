---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
api_count: 2
apis:
- baseURL: https://market-data.grvt.io
  baseurl_source: declared
  description: Public market-data API for GRVT — instruments, currencies, supported assets, margin rules, mini/full tickers, orderbook levels, trades, trade history, candlesticks, and funding rates. No authenticatio
  name: GRVT Market Data API
  slug: grvt-market-data-api
- description: Authenticated trading API for GRVT — create/cancel orders (single, bulk, TP/SL, trigger), open orders and order history, fills, positions and position history, margin management, sub-account and fundi
  name: GRVT Trading API
  slug: grvt-trading-api
artifact_total: 6
asyncapis:
- description: ''
  name: Blue Square Group Limited Streams
  slug: blue-square-group-limited-streams
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blue-square-group-limited-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://grvt.io
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.grvt.io/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.grvt.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gravity-technologies
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/blue-square-group-limited-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/blue-square-group-limited-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/blue-square-group-limited-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/blue-square-group-limited-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/blue-square-group-limited-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/blue-square-group-limited-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/blue-square-group-limited-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/blue-square-group-limited-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/blue-square-group-limited-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/blue-square-group-limited-streams.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/blue-square-group-limited-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/blue-square-group-limited-mcp.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/blue-square-group-limited-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/blue-square-group-limited-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/blue-square-group-limited-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/blue-square-group-limited-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://grvt.io/.well-known/security.txt
created: '2026-07-17'
description: Blue Square Group Limited is the corporate entity behind GRVT (pronounced "gravity"), a licensed hybrid crypto derivatives exchange headquartered in Singapore and engineered by Gravity Technologies. GRVT pairs a high-performance central limit order book with self-custody settlement on a zkSync-based Layer 2, and exposes a public Market Data API and an authenticated Trading API over both REST and WebSocket. The APIs cover perpetual futures and spot trading, order management (including bulk orders, TP/SL and trigger orders), positions and margin, sub-account and funding-account summaries, transfers, deposits and withdrawals, and on-chain vault investment and redemption. Authentication combines an API-key login with Ethereum-style ECDSA (secp256k1 / EIP-712) request signing and scoped session keys. First-party Python and JavaScript/TypeScript SDKs plus published agent skills round out the developer surface. Surfaced as a portfolio company of 500 Global and enriched into the API
  Evangelist network.
image: https://avatars.githubusercontent.com/u/112316440?v=4
layout: provider
modified: '2026-07-18'
name: Blue Square Group Limited
nav: Providers
network: true
overview: 'Blue Square Group Limited publishes 1 API on the [APIs.io](https://apis.io/) network: GRVT Market Data API. Tagged areas include Company, Cryptocurrency, Derivatives Exchange, Trading, and Perpetual Futures.


  The Blue Square Group Limited catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Blue Square Group Limited''s developer surface includes documentation, API reference, authentication, sandbox, and 19 more developer resources.'
random_paper: 18
screenshot: https://raw.githubusercontent.com/api-evangelist/blue-square-group-limited/refs/heads/main/screenshots/blue-square-group-limited-2026-07-25T203437.png
security:
- kind: authentication
  name: Blue Square Group Limited Authentication
  slug: blue-square-group-limited-authentication
  summary_line: apiKey/signature · 2 schemes
- kind: domain-security
  name: Blue Square Group Limited Domain Security
  slug: blue-square-group-limited-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Blue Square Group Limited Vulnerability Disclosure
  slug: blue-square-group-limited-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: blue-square-group-limited
tags:
- Company
- Cryptocurrency
- Derivatives Exchange
- Trading
- Perpetual Futures
- Market Data
- Blockchain
- WebSocket
- Financial-Services
website: https://grvt.io
---

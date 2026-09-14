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
api_count: 1
apis:
- baseURL: https://api.overlay.market
  baseurl_source: declared
  description: CoinGecko/CMC-style aggregator market-data feed.
  name: Overlay Aggregator API
  slug: overlay-aggregator-api
- baseURL: https://api.overlay.market
  baseurl_source: declared
  description: Price overview and OHLC chart data.
  name: Overlay Charts API
  slug: overlay-charts-api
- baseURL: https://api.overlay.market
  baseurl_source: declared
  description: Market catalog and metadata.
  name: Overlay Markets API
  slug: overlay-markets-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Overlay Market Data Aggregator API
  slug: open-overlay-aggregator-api
- collection_type: open
  name: Overlay Market Data Aggregator Charts API
  slug: open-overlay-charts-api
- collection_type: open
  name: Overlay Market Data Aggregator Markets API
  slug: open-overlay-markets-api
common:
- group: company
  title: ''
  type: Website
  url: https://overlay.market
- group: docs
  title: ''
  type: Documentation
  url: https://docs.overlay.market/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.overlay.market/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.overlay.market/api/aggregator-market-data
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/overlay-market
- group: operate
  title: ''
  type: Support
  url: https://redrct.overlay.market/discord
- group: other
  title: ''
  type: Whitepaper
  url: https://redrct.overlay.market/whitepaper
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/overlay-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/overlay-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/overlay-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/overlay-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/overlay-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/overlay-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/overlay-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/overlay-openapi-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/overlay-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/overlay-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/overlay-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/overlay-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/overlay-market.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/overlay-domain-security.yml
created: '2026-07-17'
description: Overlay is a decentralized perpetual-futures protocol on BNB Smart Chain (chain id 56) that lets anyone trade and permissionlessly create markets for emerging, pre-CEX, and narrative-driven assets against any verifiable data feed. Positions are synthetic — traders trade against a protocol-managed price feed with USDT/stablecoin collateral rather than an order book — with a dynamic risk engine managing thin markets and zero liquidity requirements. Overlay exposes a public, unauthenticated market-data API (aggregator contracts, contract specs, market catalog, charts price overview), a TypeScript SDK, a GraphQL subgraph, and a provider-published Agent Skill for automated trading. Backed by Polychain.
image: https://avatars.githubusercontent.com/u/70023182?v=4
layout: provider
modified: '2026-07-20'
name: Overlay
nav: Providers
network: true
overview: 'Overlay publishes 3 APIs on the [APIs.io](https://apis.io/) network: Aggregator API, Charts API, and Markets API. Tagged areas include Company, DeFi, Perpetual Futures, Derivatives, and Trading.


  Overlay''s developer surface includes documentation, API reference, support, authentication, and 17 more developer resources.'
random_paper: 14
screenshot: https://raw.githubusercontent.com/api-evangelist/overlay/refs/heads/main/screenshots/overlay-2026-08-07T191129.png
security:
- kind: authentication
  name: Overlay Authentication
  slug: overlay-authentication
  summary_line: none · 1 scheme
- kind: domain-security
  name: Overlay Domain Security
  slug: overlay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: overlay
tags:
- Company
- DeFi
- Perpetual Futures
- Derivatives
- Trading
- Market Data
- BNB Smart Chain
- Blockchain
- Web3
website: https://overlay.market
---

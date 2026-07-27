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
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 30.8
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: REST API for NFT data, market analytics, aggregated trading (GoTrading), machine-learning valuations (GoPricing), and webhook notifications (Notify). Authenticates with an X-API-KEY header and is mete
  name: NFTgo Developer API
  slug: nftgo-developer-api
artifact_total: 5
asyncapis:
- description: ''
  name: Nftgo Notify Webhooks
  slug: nftgo-notify-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://nftgo.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.nftgo.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nftgo.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.nftgo.io/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nftgo.io/reference/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://nftgo.io/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.nftgo.io/reference/compute-units
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.nftgo.io/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NFTGo
- group: build
  title: ''
  type: Packages
  url: packages/nftgo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nftgo-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nftgo-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nftgo-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/nftgo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nftgo-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nftgo-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nftgo-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/nftgo-notify-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nftgo-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nftgo-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nftgo-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nftgo-domain-security.yml
created: '2026-07-17'
description: 'NFTgo is an NFT data, analytics, and trading-aggregator platform that lets developers query NFT market data and execute transactions through a single REST API. The NFTgo Developer API spans several products: NFT Data (collection, token, owner, holder, rarity, and trait data across multiple chains), Charts & Market analytics (rankings, volume, market-cap, floor-price and holder charts), GoTrading (an aggregated order book plus create/fulfill/cancel listings and offers across OpenSea, Blur, LooksRare and X2Y2), GoPricing (machine-learning NFT valuations), and Notify (webhook-based real-time notifications). Requests authenticate with an X-API-KEY header against data-api.nftgo.io and are metered in Compute Units. NFTgo serves 3,000+ institutional customers and is backed by 500 Global.'
image: https://nftgo.io/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: nftgo-mcp.yml
  slug: nftgo-mcpyml
modified: '2026-07-20'
name: NFTgo
nav: Providers
network: true
overview: 'NFTgo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, NFT, Blockchain, Web3, and NFT Data.


  The NFTgo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  NFTgo''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, changelog, authentication, and 15 more developer resources.'
random_paper: 66
score:
  band: thin
  composite: 35.8
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 22.6
    developer_ergonomics: 60.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 35.8
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
  name: Nftgo Authentication
  slug: nftgo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nftgo Domain Security
  slug: nftgo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: nftgo
tags:
- Company
- NFT
- Blockchain
- Web3
- NFT Data
- NFT Analytics
- NFT Trading
- Market Data
- Cryptocurrency
- Ethereum
website: https://nftgo.io
---

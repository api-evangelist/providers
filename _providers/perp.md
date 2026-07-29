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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Public GraphQL subgraph indexing the Perpetual Protocol Curie (v2) perpetual futures protocol on Optimism (positions, markets, trades, liquidations, funding). Served via The Graph hosted service and S
  name: Perpetual Protocol Curie v2 Subgraph
  slug: perpetual-protocol-curie-v2-subgraph
- description: 'Signed, high-performance interface for connecting trading bots to the perp.com V1 matching engine: a private WebSocket trading channel, a public WebSocket market-data channel, and a secondary REST rea'
  name: Perp V1 Market Maker API
  slug: perp-v1-market-maker-api
artifact_total: 6
asyncapis:
- description: ''
  name: Perp Market Maker Webhooks
  slug: perp-market-maker-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://perp.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://perp.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://perp.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://perp.com/docs/market-maker-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/perpetual-protocol
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/perpdotcom
- group: other
  title: ''
  type: X
  url: https://x.com/perpdotcom
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/perpetual-protocol/sdk-curie
- group: build
  title: ''
  type: Packages
  url: packages/perp-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/perp-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/perp-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/perp-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/perp-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/perp-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/perp-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/perp-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/perp-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/perp-market-maker-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/perp-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/perp-lifecycle.yml
created: '2026-07-17'
description: Perp (Perpetual Protocol) is a decentralized derivatives protocol backed by Multicoin Capital. Its Curie (v2) generation ran on-chain perpetual futures on Optimism via audited smart contracts, a public GraphQL subgraph on The Graph, and an official TypeScript SDK (@perp/sdk-curie). The team has since pivoted to perp.com, a leveraged on-chain prediction-market platform ("perpetual futures for your predictions") offering up to 5x leverage on elections, macro, sports, and cultural outcomes with orderbook-driven, no-expiry positions and funding-rate rebalancing. The perp.com V1 Market Maker API is now documented in detail (a signed WebSocket + REST interface with HMAC-SHA256 auth, bulk order commands, a dead-man switch, private/public WebSocket streams, per-key rate limits, and a full MM_* error registry) though the api.perp.com host is not yet publicly reachable (V1 testnet). The other concrete developer surface is the Curie (v2) GraphQL subgraph, the TypeScript SDK, and the on-chain
  contract packages published to npm under the @perp scope.
image: https://user-images.githubusercontent.com/5022617/167766554-055c9785-00ec-4a5a-86ac-a4b3e1a42e76.png
layout: provider
modified: '2026-07-20'
name: Perp
nav: Providers
network: true
overview: 'Perp publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto Web3, DeFi, Derivatives, and Perpetual Futures.


  The Perp catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Perp''s developer surface includes documentation, API reference, support, authentication, sandbox, and 15 more developer resources.'
random_paper: 39
rate_limits:
- limit_count: 4
  name: Perp Rate Limits
  slug: perp-rate-limits
score:
  band: thin
  composite: 35.2
  delta: 4.8
  facets:
    commercial_clarity: 0.0
    contract_quality: 51.6
    developer_ergonomics: 52.2
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 30.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 20.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Perp Authentication
  slug: perp-authentication
  summary_line: apiKey/hmac · 3 schemes
- kind: domain-security
  name: Perp Domain Security
  slug: perp-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: perp
tags:
- Company
- Crypto Web3
- DeFi
- Derivatives
- Perpetual Futures
- Prediction Markets
- Optimism
- GraphQL
- Blockchain
- SDK
website: https://perp.com
---

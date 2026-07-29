---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Low-latency WebSocket feed (service-mango-fills) that parses Mango V4 Perp and Openbook event queues and emits individual fill events as they are processed by the validator. Supports getMarkets discov
  name: Mango v4 Fills Feed
  slug: fills-feed
- description: Low-latency WebSocket feed (service-mango-orderbook) that parses Mango V4 Perp and Openbook spot bookside accounts and emits L2 (price / quantity) and L3 (per-order) checkpoints and per-side delta upd
  name: Mango v4 Orderbook Feed
  slug: orderbook-feed
artifact_total: 4
asyncapis:
- description: 'AsyncAPI definition for the two public Mango Markets v4 WebSocket feed services operated by Blockworks Foundation: the Fills Feed (service-mango-fills) and the Orderbook Feed (service-mango-orderbook)'
  name: Mango Markets v4 Feeds API
  slug: mango-markets-feeds-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://mango.markets
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mango.markets
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blockworks-foundation
- group: build
  title: mango-feeds
  type: SourceCode
  url: https://github.com/blockworks-foundation/mango-feeds
created: '2026-05-30'
description: Mango Markets is a decentralized derivatives exchange and money market built on Solana, operated by the Blockworks Foundation. Mango v4 introduces unified margin accounts that combine spot trading, perpetual futures, and borrow/lend in a single risk engine, settled by the on-chain Mango v4 program. Beyond the on-chain program and the TypeScript client, the project exposes low-latency public market-data feeds through the mango-feeds geyser services - the Fills Feed (service-mango-fills, fills.mngo.cloud) and the Orderbook Feed (service-mango-orderbook, orderbook.mngo.cloud) - which stream fill events and L2/L3 orderbook state for Mango V4 Perp markets and Openbook spot markets over WebSocket.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mango-markets.png
layout: provider
modified: '2026-05-30'
name: Mango Markets
nav: Providers
network: true
overview: 'Mango Markets publishes 2 APIs on the [APIs.io](https://apis.io/) network: Mango v4 Fills Feed and Mango v4 Orderbook Feed. Tagged areas include Cryptocurrency, DeFi, Decentralized Exchange, Perpetual Futures, and Spot.


  The Mango Markets catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Mango Markets'' developer surface includes documentation and 3 more developer resources.'
random_paper: 25
rules:
- name: Mango Markets API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: mango-markets-asyncapi-spectral-rules
score:
  band: emerging
  composite: 22.2
  delta: 1.4
  facets:
    commercial_clarity: 0.0
    contract_quality: 44.4
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 47.9
    operational_transparency: 5.3
  previous_composite: 20.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 0.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
slug: mango-markets
tags:
- Cryptocurrency
- DeFi
- Decentralized Exchange
- Perpetual Futures
- Spot
- Margin
- Orderbook
- Fills
- Market Data
- WebSocket
- Solana
- Mango v4
website: https://mango.markets
---

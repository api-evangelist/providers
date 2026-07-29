---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
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
  score: 16.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Read-only REST/HTTP JSON and JSON-LD API for live Binance Spot market snapshots and single-market observations across nine USDT pairs. Keyless, cached to at most 30 seconds, fail-closed on stale data.
  name: BTC War Live Market Data API
  slug: btc-war-live-market-data-api
artifact_total: 1
created: '2026-07-18'
description: 'Public, read-only real-time crypto market-data API from btcwar.net, exposing live Binance Spot order-flow snapshots and single-market observations for nine USDT pairs as JSON and Schema.org JSON-LD. Ships a complete agent-native discovery stack: OpenAPI 3.1, Arazzo workflow, hosted MCP server, and llms.txt.'
layout: provider
modified: '2026-07-18'
name: BTC War Live Market Data API
nav: Providers
network: true
overview: 'BTC War Live Market Data API publishes 1 API on the [APIs.io](https://apis.io/) network: BTC War Live Market Data API. Tagged areas include finance, cryptocurrency, market-data, bitcoin, and crypto-price.'
random_paper: 61
score:
  band: minimal
  composite: 11.9
  delta: -5.5
  facets:
    commercial_clarity: 0.0
    contract_quality: 32.3
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 0.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
slug: btc-war-live-market-data-api
tags:
- finance
- cryptocurrency
- market-data
- bitcoin
- crypto-price
- binance-spot
- order-flow
- market-depth
- json-ld
- schema.org
- openapi
- mcp
- read-only
- no-authentication
---

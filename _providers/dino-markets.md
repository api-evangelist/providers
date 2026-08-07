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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-08-06'
api_count: 2
apis:
- description: Versioned REST API (/v2/) for matched cross-venue market catalog, priced arbitrage view, pair history, leagues, coverage, bad-arb reporting, and stream-ticket minting. Bearer API key auth (sk_live_).
  name: dino.markets REST API
  slug: dinomarkets-rest-api
- description: Native hosted Streamable HTTP MCP server exposing 7 tools (list_markets, find_arbitrage, get_market, list_leagues, get_coverage, report_bad_arb, watch_markets). Accepts the same sk_live_ API key. Free
  name: dino.markets MCP Server
  slug: dinomarkets-mcp-server
artifact_total: 2
created: '2026-07-08'
description: Real-time cross-venue sports prediction-market data. Matches the same game across Kalshi and Polymarket, computes live cross-venue arbitrage sized to fillable depth, and streams it via REST, WebSocket, and a native MCP server. Operated by Nusantara Ventures LLC. Not a broker; not financial advice.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dino-markets.png
layout: provider
modified: '2026-07-08'
name: dino.markets
nav: Providers
network: true
overview: 'dino.markets publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include prediction-markets, sports, arbitrage, kalshi, and polymarket.'
random_paper: 100
score:
  band: minimal
  composite: 12.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 32.3
    developer_ergonomics: 0.0
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.2
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 0.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
slug: dino-markets
tags:
- prediction-markets
- sports
- arbitrage
- kalshi
- polymarket
- trading
- real-time
- websocket
- mcp
- agent-native
---

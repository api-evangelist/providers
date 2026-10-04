---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 66.9
  scored_at: '2026-10-03'
api_count: 2
apis:
- description: Real-time subscriptions for supported Hyperliquid channels and historical replay for Hyperliquid and Lighter. Clients authenticate during the handshake with a bearer API key.
  name: 0xArchive WebSocket API
  slug: 0xarchive-websocket-api
- description: Read-only market-data discovery and retrieval for MCP clients. Hosted MCP uses client-managed OAuth and requires no 0xArchive API key.
  name: 0xArchive Hosted MCP
  slug: 0xarchive-hosted-mcp
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: 'Data quality monitoring: system status, coverage, incidents, latency, and SLA metrics.'
  name: 0xArchive Data Quality API
  phrasing_intents:
  - id: getDataQualityStatus
    intent: Check overall data system health
    question: Is any exchange or data type currently degraded?
  - id: getDataQualityCoverage
    intent: Summarize data coverage across venues
    question: How far back does archived data go for each venue family?
  - id: getExchangeCoverage
    intent: Get data coverage for one exchange
    question: What data coverage exists for a single exchange like Lighter?
  - id: getSymbolCoverage
    intent: Find data gaps for one symbol
    question: Are there missing periods in the archived data for a specific coin?
  - id: listIncidents
    intent: List data quality incidents
    question: Which data quality incidents have been reported recently?
  - id: getIncident
    intent: Get one data quality incident
    question: What happened in a specific data quality incident?
  - id: getLatencyMetrics
    intent: Get current latency metrics
    question: How much latency is there on WebSocket and REST data right now?
  - id: getSlaMetrics
    intent: Get monthly SLA compliance metrics
    question: Did uptime and completeness meet the SLA targets last month?
  phrasing_ops: 8
  slug: 0xarchive-data-quality-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: 'HIP-3 market breadth snapshots: percentage of eligible instruments trading above their current UTC-session VWAP.'
  name: 0xArchive HIP-3 Builder Perps - Breadth API
  phrasing_intents:
  - id: getHip3BreadthAboveVwapCurrent
    intent: Get current HIP-3 breadth above session VWAP
    question: What share of HIP-3 markets is trading above session VWAP right now?
  - id: getHip3BreadthAboveVwap
    intent: Get HIP-3 breadth above VWAP history
    question: How has HIP-3 market breadth above VWAP changed over the past week?
  phrasing_ops: 2
  slug: 0xarchive-hip-3-builder-perps-breadth-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: 'HIP-3 Builder Perps OHLCV candle data. Intervals: 1m, 5m, 15m, 30m, 1h, 4h, 1d, 1w. Coverage is symbol-specific; verify the selected market before choosing a time range.'
  name: 0xArchive HIP-3 Builder Perps - Candles API
  phrasing_intents:
  - id: getHip3Candles
    intent: Get OHLCV candles for a HIP-3 builder perp
    question: Can I get hourly candles for a HIP-3 market like km:US500?
  phrasing_ops: 1
  slug: 0xarchive-hip-3-builder-perps-candles-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: 'HIP-3 convenience endpoints: freshness, summary, and price history.'
  name: 0xArchive HIP-3 Builder Perps - Convenience API
  phrasing_intents:
  - id: getHip3Freshness
    intent: Check how fresh a HIP-3 coin's data is
    question: When was each data type last updated for a HIP-3 coin?
  - id: getHip3Summary
    intent: Get a one-call HIP-3 market summary
    question: Can I get a HIP-3 market's price, funding and open interest in one call?
  - id: getHip3PriceHistory
    intent: Get HIP-3 mark, oracle and mid price history
    question: Can I get only price fields over time for a HIP-3 coin?
  - id: getHip3Cvd
    intent: Get cumulative volume delta for a HIP-3 perp
    question: Is buying or selling pressure winning on a builder perp each hour?
  phrasing_ops: 4
  slug: 0xarchive-hip-3-builder-perps-convenience-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Full-depth aggregated L2 order book snapshots, checkpoint history, and diffs for HIP-3 builder perps derived from L4 data. Full-depth checkpoints and diffs where available.
  name: 0xArchive HIP-3 Builder Perps - Full-Depth L2 Order Book API
  phrasing_intents:
  - id: getHip3FullDepthL2Orderbook
    intent: Get a full-depth HIP-3 L2 book snapshot
    question: Can I see a HIP-3 book beyond the native 20 levels?
  - id: getHip3FullDepthL2History
    intent: Get full-depth HIP-3 L2 checkpoint history
    question: Can I page past full-depth L2 checkpoints for a builder perp?
  - id: getHip3FullDepthL2Diffs
    intent: Get tick-level full-depth HIP-3 L2 diffs
    question: How do I replay every tick change to a HIP-3 aggregated book?
  phrasing_ops: 3
  slug: 0xarchive-hip-3-builder-perps-full-depth-l2-order-book-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: HIP-3 Builder Perps funding rate history. Coverage is symbol-specific; inspect `/v1/symbols` `coverage_by_type.funding` before choosing a time range.
  name: 0xArchive HIP-3 Builder Perps - Funding API
  phrasing_intents:
  - id: getHip3FundingHistory
    intent: Get HIP-3 funding rate history
    question: What were a builder perp's historical funding rates?
  - id: getCurrentHip3Funding
    intent: Get the latest HIP-3 funding rate
    question: What is the funding rate on a HIP-3 market right now?
  phrasing_ops: 2
  slug: 0xarchive-hip-3-builder-perps-funding-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: HIP-3 Builder Perps instrument discovery. Use this route with `/v1/symbols` `coverage_by_type` to resolve the current inventory and schema-specific dates.
  name: 0xArchive HIP-3 Builder Perps - Instruments API
  phrasing_intents:
  - id: listHip3Instruments
    intent: List available HIP-3 builder perps
    question: Which builder-deployed perpetuals are live on Hyperliquid?
  - id: getHip3Instrument
    intent: Get one HIP-3 instrument
    question: What are the latest details of a single HIP-3 market?
  phrasing_ops: 2
  slug: 0xarchive-hip-3-builder-perps-instruments-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Individual order-level (L4) orderbook data for HIP-3 builder perps.
  name: 0xArchive HIP-3 Builder Perps - L4 Order Book API
  phrasing_intents:
  - id: getHip3L4Orderbook
    intent: Get an order-level L4 book for a HIP-3 perp
    question: Can I see individual resting orders with IDs on a HIP-3 book?
  - id: getHip3L4Diffs
    intent: Get per-order HIP-3 L4 diff events
    question: How do I see each order placement, fill and cancel on a builder perp book?
  - id: getHip3L4History
    intent: List HIP-3 L4 checkpoints for replay
    question: Which full L4 snapshots can I replay from on a HIP-3 market?
  phrasing_ops: 3
  slug: 0xarchive-hip-3-builder-perps-l4-order-book-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: HIP-3 Builder Perps liquidation-related fills. Coverage is symbol-specific; verify the selected market before choosing a time range.
  name: 0xArchive HIP-3 Builder Perps - Liquidations API
  phrasing_intents:
  - id: getHip3Liquidations
    intent: Get liquidation fills for a HIP-3 perp
    question: Which liquidations hit a builder perp since a given time?
  - id: getHip3LiquidationVolume
    intent: Get bucketed HIP-3 liquidation volume
    question: How much liquidation volume hit a builder perp per hour?
  phrasing_ops: 2
  slug: 0xarchive-hip-3-builder-perps-liquidations-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: HIP-3 Builder Perps historical open interest data. Coverage is symbol-specific; inspect `/v1/symbols` `coverage_by_type.oi` before choosing a time range.
  name: 0xArchive HIP-3 Builder Perps - Open Interest API
  phrasing_intents:
  - id: getHip3OpenInterest
    intent: Get HIP-3 open interest history
    question: How has open interest in a builder perp changed over time?
  - id: getCurrentHip3OpenInterest
    intent: Get current HIP-3 open interest
    question: What is the open interest on a HIP-3 market right now?
  phrasing_ops: 2
  slug: 0xarchive-hip-3-builder-perps-open-interest-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: The HIP-3 Builder Perps - Oracle API from 0xArchive — 2 operation(s) for hip-3 builder perps - oracle.
  name: 0xArchive HIP-3 Builder Perps - Oracle API
  phrasing_intents:
  - id: getHip3OracleExternalPrice
    intent: Get a HIP-3 deployer's external reference price
    question: What external reference price has the deployer pushed for a HIP-3 market?
  - id: getHip3OracleDiscoveryBounds
    intent: Get HIP-3 price discovery bounds
    question: What price range can a HIP-3 market trade within right now?
  phrasing_ops: 2
  slug: 0xarchive-hip-3-builder-perps-oracle-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: HIP-3 Builder Perps venue-native L2 order book snapshots. Native Hyperliquid source snapshots are capped at 20 levels per side; use the full-depth L2 routes for full-depth aggregated L2.
  name: 0xArchive HIP-3 Builder Perps - Order Book API
  phrasing_intents:
  - id: getHip3Orderbook
    intent: Get the native 20-level HIP-3 L2 book
    question: Can I get the top 20 price levels of a HIP-3 book at a past moment?
  - id: getHip3OrderbookHistory
    intent: Get native 20-level HIP-3 L2 book history
    question: Can I pull a series of native HIP-3 book snapshots over a range?
  phrasing_ops: 2
  slug: 0xarchive-hip-3-builder-perps-order-book-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Order lifecycle events for HIP-3 builder perps.
  name: 0xArchive HIP-3 Builder Perps - Orders API
  phrasing_intents:
  - id: getHip3OrderHistory
    intent: Get order lifecycle events for a HIP-3 perp
    question: Can I see every placement, fill and cancel on a builder perp?
  - id: getHip3OrderFlow
    intent: Get per-minute order flow for a HIP-3 perp
    question: How fast are orders being placed and cancelled on a builder perp?
  - id: getHip3Tpsl
    intent: Get HIP-3 take-profit and stop-loss events
    question: When were TP/SL orders placed or triggered on a builder perp?
  phrasing_ops: 3
  slug: 0xarchive-hip-3-builder-perps-orders-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: HIP-3 Builder Perps historical trade/fill data. Coverage is symbol-specific; inspect `/v1/symbols` `coverage_by_type.trades` before choosing a time range.
  name: 0xArchive HIP-3 Builder Perps - Trades API
  phrasing_intents:
  - id: getHip3Trades
    intent: Get historical HIP-3 trades
    question: Can I get every fill for a builder perp over a time range?
  - id: getHip3RecentTrades
    intent: Get the latest HIP-3 trades
    question: What were the last trades on a HIP-3 market?
  phrasing_ops: 2
  slug: 0xarchive-hip-3-builder-perps-trades-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: The HIP-3 Builder Perps - Wallets API from 0xArchive — 1 operation(s) for hip-3 builder perps - wallets.
  name: 0xArchive HIP-3 Builder Perps - Wallets API
  phrasing_intents:
  - id: classifyHip3Wallets
    intent: Classify active HIP-3 wallets by behavior
    question: Which wallets trade the most volume on HIP-3 builder perps each day?
  phrasing_ops: 1
  slug: 0xarchive-hip-3-builder-perps-wallets-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: The HIP-3 - Liquidations API from 0xArchive — 2 operation(s) for hip-3 - liquidations.
  name: 0xArchive HIP-3 - Liquidations API
  phrasing_intents:
  - id: getHip3LiquidationLevels
    intent: See projected HIP-3 liquidation levels
    question: At what prices would HIP-3 positions get force-liquidated?
  - id: getHip3LiquidationLevelsHistory
    intent: Get past HIP-3 liquidation level snapshots
    question: How have projected HIP-3 liquidation clusters shifted over time?
  phrasing_ops: 2
  slug: 0xarchive-hip-3-liquidations-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: The HIP-3 - Orders API from 0xArchive — 2 operation(s) for hip-3 - orders.
  name: 0xArchive HIP-3 - Orders API
  phrasing_intents:
  - id: getHip3TriggerLevels
    intent: See pending HIP-3 stop and take-profit levels
    question: Where are pending stop-losses clustered on a HIP-3 market?
  - id: getHip3TriggerLevelsHistory
    intent: Get past HIP-3 trigger level snapshots
    question: How have pending HIP-3 stop and take-profit clusters moved over time?
  phrasing_ops: 2
  slug: 0xarchive-hip-3-orders-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: OHLCV candles for HIP-4 outcome sides. Prices are implied probabilities (0..1); quote_volume in USDH.
  name: 0xArchive HIP-4 Outcomes - Candles API
  phrasing_intents:
  - id: getHip4Candles
    intent: Get OHLCV candles for a HIP-4 outcome side
    question: Can I chart implied probability candles for a HIP-4 outcome?
  phrasing_ops: 1
  slug: 0xarchive-hip-4-outcomes-candles-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: 'HIP-4 convenience endpoints: freshness, summary, and price history. `mark_price` for HIP-4 is an implied probability in [0,1], not a USD price.'
  name: 0xArchive HIP-4 Outcomes - Convenience API
  phrasing_intents:
  - id: getHip4Freshness
    intent: Check how fresh a HIP-4 outcome side's data is
    question: When was order book and trade data last updated for a HIP-4 side?
  - id: getHip4Summary
    intent: Get a one-call HIP-4 outcome side summary
    question: What is the implied probability and 24h volume for a HIP-4 outcome?
  - id: getHip4PriceHistory
    intent: Get HIP-4 outcome side price history
    question: How has an outcome's implied probability moved over time?
  phrasing_ops: 3
  slug: 0xarchive-hip-4-outcomes-convenience-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: 'HIP-4 per-side instrument discovery (one row per `#N` coin). Each outcome has two sides: side 0 (Yes) and side 1 (No). Coins are `#`-prefixed. Data from May 2026.'
  name: 0xArchive HIP-4 Outcomes - Instruments API
  phrasing_intents:
  - id: listHip4Instruments
    intent: List HIP-4 outcome side instruments
    question: Which HIP-4 outcome sides are listed?
  - id: getHip4Instrument
    intent: Get one HIP-4 outcome side instrument
    question: What are the details of a single HIP-4 side coin?
  phrasing_ops: 2
  slug: 0xarchive-hip-4-outcomes-instruments-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: HIP-4 outcome markets per-side open interest history. Display/paired/parity aggregates live on the `/outcomes/{outcome_id}` detail endpoint, not here. Data from May 2026.
  name: 0xArchive HIP-4 Outcomes - Open Interest API
  phrasing_intents:
  - id: getHip4OpenInterest
    intent: Get HIP-4 outcome side open interest history
    question: How has open interest on one side of a HIP-4 outcome changed?
  - id: getCurrentHip4OpenInterest
    intent: Get current HIP-4 outcome side open interest
    question: What is the open interest on a HIP-4 outcome side right now?
  phrasing_ops: 2
  slug: 0xarchive-hip-4-outcomes-open-interest-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: HIP-4 outcome markets L2 and L4 order book snapshots and diffs. Coins are referenced by numeric id (0, 1, 10, 11, ...); the `#`-prefixed form is also accepted. Data from May 2026.
  name: 0xArchive HIP-4 Outcomes - Order Book API
  phrasing_intents:
  - id: getHip4Orderbook
    intent: Get a HIP-4 outcome side L2 book snapshot
    question: What does the order book for a HIP-4 outcome side look like now?
  - id: getHip4OrderbookHistory
    intent: Get HIP-4 L2 book history
    question: Can I pull historical L2 book snapshots for a HIP-4 side?
  - id: getHip4L4Orderbook
    intent: Get an order-level L4 book for a HIP-4 side
    question: Can I see individual resting orders on a HIP-4 outcome book?
  - id: getHip4L4Diffs
    intent: Get per-order HIP-4 L4 diff events
    question: How do I replay each order placement and cancel on a HIP-4 book?
  - id: getHip4L4History
    intent: List HIP-4 L4 checkpoints for replay
    question: Which full L4 checkpoints can I replay from on a HIP-4 side?
  phrasing_ops: 5
  slug: 0xarchive-hip-4-outcomes-order-book-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: 'Order lifecycle events for HIP-4 outcome markets: placements, cancellations, fills, and TP/SL triggers.'
  name: 0xArchive HIP-4 Outcomes - Orders API
  phrasing_intents:
  - id: getHip4OrderHistory
    intent: Get order lifecycle events for a HIP-4 side
    question: Can I see every placement, fill and cancel on a HIP-4 outcome side?
  - id: getHip4OrderFlow
    intent: Get per-minute order flow for a HIP-4 side
    question: How quickly are orders placed and cancelled on a HIP-4 outcome?
  - id: getHip4Tpsl
    intent: Get HIP-4 take-profit and stop-loss events
    question: Are traders placing stop-losses on HIP-4 outcome sides?
  phrasing_ops: 3
  slug: 0xarchive-hip-4-outcomes-orders-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: HIP-4 outcome market discovery (one row per outcome, both sides combined). Use these to enumerate live and settled binary outcome markets. Data from May 2026.
  name: 0xArchive HIP-4 Outcomes - Outcomes API
  phrasing_intents:
  - id: listHip4Outcomes
    intent: List HIP-4 outcome markets
    question: Which HIP-4 prediction outcomes are live or settled?
  - id: getHip4Outcome
    intent: Get one HIP-4 outcome with aggregated open interest
    question: What is the combined open interest across both sides of an outcome?
  - id: getHip4OutcomeBySlug
    intent: Look up a HIP-4 outcome by slug
    question: Can I find a HIP-4 outcome from a readable slug like btc-above-78213-may-04-0600?
  phrasing_ops: 3
  slug: 0xarchive-hip-4-outcomes-outcomes-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: The HIP-4 Outcomes - Questions API from 0xArchive — 2 operation(s) for hip-4 outcomes - questions.
  name: 0xArchive HIP-4 Outcomes - Questions API
  phrasing_intents:
  - id: listHip4Questions
    intent: List HIP-4 question groupings
    question: Which HIP-4 questions group multiple outcome markets together?
  - id: getHip4Question
    intent: Get one HIP-4 question grouping
    question: Which outcome markets belong to a specific HIP-4 question?
  phrasing_ops: 2
  slug: 0xarchive-hip-4-outcomes-questions-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: HIP-4 outcome markets historical trade/fill data. Data from May 2026.
  name: 0xArchive HIP-4 Outcomes - Trades API
  phrasing_intents:
  - id: getHip4Trades
    intent: Get historical HIP-4 outcome trades
    question: Can I get every fill on a HIP-4 outcome side over a time range?
  - id: getHip4RecentTrades
    intent: Get the latest HIP-4 outcome trades
    question: What were the most recent trades on a HIP-4 outcome?
  phrasing_ops: 2
  slug: 0xarchive-hip-4-outcomes-trades-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: 'Hyperliquid OHLCV candle data. Intervals: 1m, 5m, 15m, 30m, 1h, 4h, 1d, 1w.'
  name: 0xArchive Hyperliquid - Candles API
  phrasing_intents:
  - id: getHyperliquidCandles
    intent: Get OHLCV candles for a Hyperliquid perp
    question: Can I get hourly OHLCV candles for BTC on Hyperliquid?
  phrasing_ops: 1
  slug: 0xarchive-hyperliquid-candles-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: 'Hyperliquid convenience endpoints: freshness, summary, and price history.'
  name: 0xArchive Hyperliquid - Convenience API
  phrasing_intents:
  - id: getHyperliquidLiquidationVolume
    intent: Get bucketed liquidation volume for a coin
    question: How much long versus short liquidation volume hit a coin each hour?
  - id: getHyperliquidFreshness
    intent: Check how fresh a coin's data is
    question: When was each data type last updated for a Hyperliquid coin?
  - id: getHyperliquidSummary
    intent: Get a one-call market summary for a coin
    question: Can I get price, funding, open interest, volume and liquidations in one call?
  - id: getHyperliquidPriceHistory
    intent: Get mark and oracle price history
    question: Is there a lightweight way to get only mark and oracle prices over time?
  - id: getHyperliquidCvd
    intent: Get cumulative volume delta for a core perp
    question: Is buying or selling pressure dominating a Hyperliquid coin by hour?
  phrasing_ops: 5
  slug: 0xarchive-hyperliquid-convenience-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Full-depth aggregated L2 order book snapshots, checkpoint history, and diffs for Hyperliquid perpetuals derived from L4 data. Full-depth checkpoints and diffs where available.
  name: 0xArchive Hyperliquid - Full-Depth L2 Order Book API
  phrasing_intents:
  - id: getHyperliquidFullDepthL2Orderbook
    intent: Get a full-depth L2 order book snapshot
    question: Can I see the whole Hyperliquid book beyond the 20-level native snapshot?
  - id: getHyperliquidFullDepthL2History
    intent: Get full-depth L2 checkpoint history
    question: Can I page through historical full-depth L2 checkpoints for a coin?
  - id: getHyperliquidFullDepthL2Diffs
    intent: Get tick-level full-depth L2 diffs
    question: How do I replay every change to the aggregated full-depth book tick by tick?
  phrasing_ops: 3
  slug: 0xarchive-hyperliquid-full-depth-l2-order-book-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Hyperliquid funding rate history. Data from May 2023.
  name: 0xArchive Hyperliquid - Funding API
  phrasing_intents:
  - id: getHyperliquidFundingHistory
    intent: Get Hyperliquid funding rate history
    question: What were a coin's historical funding rates on Hyperliquid?
  - id: getCurrentHyperliquidFunding
    intent: Get the latest Hyperliquid funding rate
    question: What is the funding rate on a Hyperliquid perp right now?
  phrasing_ops: 2
  slug: 0xarchive-hyperliquid-funding-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Hyperliquid available trading instruments and their specifications. Authenticated inventory contains 232 core perpetual rows.
  name: 0xArchive Hyperliquid - Instruments API
  phrasing_intents:
  - id: listHyperliquidInstruments
    intent: List all Hyperliquid trading instruments
    question: Which perp instruments can I trade on Hyperliquid?
  - id: getHyperliquidInstrument
    intent: Get specs for one Hyperliquid instrument
    question: What are the specifications of a single Hyperliquid instrument?
  phrasing_ops: 2
  slug: 0xarchive-hyperliquid-instruments-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Individual resting-order (L4) book state for Hyperliquid perpetuals, including price, size, order ID, wallet attribution, queue priority, diffs, and checkpoints.
  name: 0xArchive Hyperliquid - L4 Order Book API
  phrasing_intents:
  - id: getHyperliquidL4Orderbook
    intent: Get an order-level L4 book snapshot
    question: Can I see individual resting orders with order IDs on the book?
  - id: getHyperliquidL4Diffs
    intent: Get per-order L4 book diff events
    question: How do I see each order placement, modification, fill and cancel on the book?
  - id: getHyperliquidL4History
    intent: List L4 book checkpoints for replay
    question: Which full L4 snapshots can I use as a starting point for replay?
  phrasing_ops: 3
  slug: 0xarchive-hyperliquid-l4-order-book-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Hyperliquid liquidation events with user attribution. The observed global floor is July 27, 2025; exact starts vary by symbol.
  name: 0xArchive Hyperliquid - Liquidations API
  phrasing_intents:
  - id: getHyperliquidLiquidations
    intent: Get liquidation events for a coin
    question: Which liquidations happened on a Hyperliquid coin last week?
  - id: getHyperliquidLiquidationsByUser
    intent: Get liquidations for a wallet address
    question: Was a particular wallet ever liquidated on Hyperliquid?
  - id: getHyperliquidLiquidationLevels
    intent: See projected forced-liquidation levels
    question: At what prices would open positions get force-liquidated?
  - id: getHyperliquidLiquidationLevelsHistory
    intent: Get past projected liquidation level snapshots
    question: How have projected liquidation clusters shifted over time?
  phrasing_ops: 4
  slug: 0xarchive-hyperliquid-liquidations-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Hyperliquid historical open interest and market context data. Data from May 2023.
  name: 0xArchive Hyperliquid - Open Interest API
  phrasing_intents:
  - id: getHyperliquidOpenInterest
    intent: Get Hyperliquid open interest history
    question: How has open interest in a Hyperliquid coin changed over time?
  - id: getCurrentHyperliquidOpenInterest
    intent: Get current Hyperliquid open interest
    question: What is the open interest on a Hyperliquid perp right now?
  phrasing_ops: 2
  slug: 0xarchive-hyperliquid-open-interest-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Hyperliquid venue-native L2 order book snapshots. Native Hyperliquid source snapshots are capped at 20 levels per side; use the full-depth L2 routes for full-depth aggregated L2.
  name: 0xArchive Hyperliquid - Order Book API
  phrasing_intents:
  - id: getHyperliquidOrderbook
    intent: Get the native 20-level L2 book snapshot
    question: Can I get the top 20 price levels of a Hyperliquid book at a past moment?
  - id: getHyperliquidOrderbookHistory
    intent: Get native 20-level L2 book history
    question: Can I pull a series of native 20-level book snapshots over a time range?
  phrasing_ops: 2
  slug: 0xarchive-hyperliquid-order-book-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: 'Order lifecycle events for Hyperliquid perpetuals: placements, cancellations, fills, and TP/SL triggers.'
  name: 0xArchive Hyperliquid - Orders API
  phrasing_intents:
  - id: getHyperliquidOrderHistory
    intent: Get order lifecycle events for a coin
    question: Can I see every placement, fill and cancel for a coin's orders?
  - id: getHyperliquidOrderFlow
    intent: Get per-minute order flow for a coin
    question: How fast are orders being placed and cancelled on a coin?
  - id: getHyperliquidTpsl
    intent: Get take-profit and stop-loss order events
    question: When were TP/SL orders placed, triggered or cancelled on a coin?
  - id: getHyperliquidTriggerLevels
    intent: See pending stop and take-profit trigger levels
    question: Where are pending stop-losses and take-profits clustered near the price?
  - id: getHyperliquidTriggerLevelsHistory
    intent: Get past trigger level snapshots
    question: How have pending stop and take-profit clusters moved over time?
  phrasing_ops: 5
  slug: 0xarchive-hyperliquid-orders-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Hyperliquid Spot pair, order book, trade, reconstruction, TWAP, and freshness routes.
  name: 0xArchive Hyperliquid Spot API
  phrasing_intents:
  - id: getHyperliquidSpotPairs
    intent: List Hyperliquid Spot pairs
    question: Which Hyperliquid Spot pairs have archived data?
  - id: getHyperliquidSpotPair
    intent: Get metadata for one Spot pair
    question: What metadata is available for a single spot pair?
  - id: getHyperliquidSpotOrderbook
    intent: Get a Spot pair's L2 order book snapshot
    question: What does the spot order book for a pair look like right now?
  - id: getHyperliquidSpotTrades
    intent: Get historical trades for a Spot pair
    question: Can I pull spot fills for a pair over a bounded time range?
  - id: getSpotTradesRecent
    intent: Get the latest trades for a Spot pair
    question: What were the last few trades on a spot pair?
  - id: getHyperliquidSpotL4Orderbook
    intent: Get an order-level L4 book for a Spot pair
    question: Can I see individual resting orders on a spot pair's book?
  - id: getHyperliquidSpotL4Diffs
    intent: Get per-order L4 diffs for a Spot pair
    question: How do I replay every order change on a spot pair's L4 book?
  - id: getHyperliquidSpotL4History
    intent: Get Spot L4 book reconstruction history
    question: Which historical L4 reconstruction windows exist for a spot pair?
  phrasing_ops: 12
  slug: 0xarchive-hyperliquid-spot-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: OHLCV candles for spot pairs (1m base, rolled up on demand).
  name: 0xArchive Hyperliquid Spot - Candles API
  phrasing_intents:
  - id: getSpotCandles
    intent: Get OHLCV candles for a Spot pair
    question: Can I get hourly candles for HYPE-USDC on Hyperliquid Spot?
  phrasing_ops: 1
  slug: 0xarchive-hyperliquid-spot-candles-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: The Hyperliquid Spot - Order Book API from 0xArchive — 1 operation(s) for hyperliquid spot - order book.
  name: 0xArchive Hyperliquid Spot - Order Book API
  phrasing_intents:
  - id: getHyperliquidSpotOrderbookHistory
    intent: Get Spot L2 order book history
    question: Can I pull historical L2 book snapshots for a spot pair?
  phrasing_ops: 1
  slug: 0xarchive-hyperliquid-spot-order-book-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Hyperliquid historical trade/fill data with full execution details. Data from April 2023.
  name: 0xArchive Hyperliquid - Trades API
  phrasing_intents:
  - id: getHyperliquidTrades
    intent: Get historical Hyperliquid trades
    question: Can I get every fill for a Hyperliquid coin with fees and PnL?
  phrasing_ops: 1
  slug: 0xarchive-hyperliquid-trades-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: The Hyperliquid - Wallets API from 0xArchive — 1 operation(s) for hyperliquid - wallets.
  name: 0xArchive Hyperliquid - Wallets API
  phrasing_intents:
  - id: classifyHyperliquidWallets
    intent: Classify active Hyperliquid wallets by behavior
    question: Which Hyperliquid wallets trade the most volume each day?
  phrasing_ops: 1
  slug: 0xarchive-hyperliquid-wallets-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Deprecated endpoints that default to Hyperliquid. Use the exchange-specific endpoints (`/v1/hyperliquid/*`, `/v1/lighter/*`, `/v1/hyperliquid/hip3/*`) instead.
  name: 0xArchive Legacy API
  phrasing_intents:
  - id: getOrderbook
    intent: Get an order book via the deprecated route
    question: Does the old unprefixed order book endpoint still work?
  - id: getOrderbookHistory
    intent: Get order book history via the deprecated route
    question: Can I still pull order book history from the old /v1/orderbook route?
  - id: getTrades
    intent: Get trades via the deprecated route
    question: Is the old /v1/trades endpoint still available for fills?
  - id: getTradesCursor
    intent: Page trades via the deprecated cursor route
    question: Is there a legacy trades route that uses cursor pagination?
  - id: listInstruments
    intent: List instruments via the deprecated route
    question: Can I still list all instruments from the unprefixed /v1/instruments route?
  - id: getInstrument
    intent: Get one instrument via the deprecated route
    question: Does the legacy single-instrument lookup still return specs?
  - id: getOpenInterest
    intent: Get open interest history via the deprecated route
    question: Can I still pull open interest history from the old unprefixed route?
  - id: getCurrentOpenInterest
    intent: Get current open interest via the deprecated route
    question: Does the legacy current open interest endpoint still respond?
  phrasing_ops: 10
  slug: 0xarchive-legacy-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: 'Lighter OHLCV candle data. Intervals: 1m, 5m, 15m, 30m, 1h, 4h, 1d, 1w. Data from August 2025.'
  name: 0xArchive Lighter - Candles API
  phrasing_intents:
  - id: getLighterCandles
    intent: Get OHLCV candles for a Lighter market
    question: Can I get hourly candles for ETH on Lighter?
  phrasing_ops: 1
  slug: 0xarchive-lighter-candles-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: 'Lighter convenience endpoints: freshness, summary, and price history.'
  name: 0xArchive Lighter - Convenience API
  phrasing_intents:
  - id: getLighterFreshness
    intent: Check how fresh a Lighter coin's data is
    question: When was each data type last updated for a Lighter coin?
  - id: getLighterSummary
    intent: Get a one-call Lighter market summary
    question: Can I get a Lighter coin's price, funding and OI in one call?
  - id: getLighterPriceHistory
    intent: Get Lighter mark and oracle price history
    question: Can I get only mark and oracle prices over time on Lighter?
  phrasing_ops: 3
  slug: 0xarchive-lighter-convenience-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Lighter funding rate history. Data from August 2025.
  name: 0xArchive Lighter - Funding API
  phrasing_intents:
  - id: getLighterFundingHistory
    intent: Get Lighter funding rate history
    question: What were a coin's historical funding rates on Lighter?
  - id: getCurrentLighterFunding
    intent: Get the latest Lighter funding rate
    question: What is the funding rate on a Lighter market right now?
  phrasing_ops: 2
  slug: 0xarchive-lighter-funding-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Lighter available trading instruments and their specifications.
  name: 0xArchive Lighter - Instruments API
  phrasing_intents:
  - id: listLighterInstruments
    intent: List all Lighter trading instruments
    question: Which markets can I trade on Lighter?
  - id: getLighterInstrument
    intent: Get specs for one Lighter instrument
    question: What are the fees and minimum order amount for one Lighter market?
  phrasing_ops: 2
  slug: 0xarchive-lighter-instruments-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Individual order-level (L3) orderbook data for Lighter. Data from March 2026.
  name: 0xArchive Lighter - L3 Order Book API
  phrasing_intents:
  - id: getLighterL3Orderbook
    intent: Get a Lighter order-level L3 book snapshot
    question: Can I see individual resting orders and their owner accounts on Lighter?
  - id: getLighterL3OrderbookHistory
    intent: Get Lighter L3 order-level book history
    question: Can I pull historical order-level snapshots for a Lighter market?
  phrasing_ops: 2
  slug: 0xarchive-lighter-l3-order-book-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: The Lighter - Liquidations API from 0xArchive — 2 operation(s) for lighter - liquidations.
  name: 0xArchive Lighter - Liquidations API
  phrasing_intents:
  - id: getLighterLiquidations
    intent: Get Lighter liquidation events
    question: Which liquidations happened on a Lighter market recently?
  - id: getLighterLiquidationVolume
    intent: Get bucketed Lighter liquidation volume
    question: How much long and short liquidation volume hit a Lighter market per hour?
  phrasing_ops: 2
  slug: 0xarchive-lighter-liquidations-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Lighter historical open interest data. Data from August 2025.
  name: 0xArchive Lighter - Open Interest API
  phrasing_intents:
  - id: getLighterOpenInterest
    intent: Get Lighter open interest history
    question: How has open interest in a Lighter market changed over time?
  - id: getCurrentLighterOpenInterest
    intent: Get current Lighter open interest
    question: What is the open interest on a Lighter market right now?
  phrasing_ops: 2
  slug: 0xarchive-lighter-open-interest-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Lighter L2 order book snapshots with configurable granularity. Checkpoint history starts January 29, 2026; 30s/10s/1s start January 30, 2026; tick reconstruction available.
  name: 0xArchive Lighter - Order Book API
  phrasing_intents:
  - id: getLighterOrderbook
    intent: Get a Lighter L2 order book snapshot
    question: What does a Lighter market's order book look like now?
  - id: getLighterOrderbookHistory
    intent: Get Lighter L2 order book history
    question: Can I pull Lighter book snapshots at one-second resolution?
  phrasing_ops: 2
  slug: 0xarchive-lighter-order-book-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Lighter historical fill data across more than 200 markets. Served history begins August 27, 2025, with exact starts varying by market.
  name: 0xArchive Lighter - Trades API
  phrasing_intents:
  - id: getLighterTrades
    intent: Get historical Lighter trades
    question: Can I get every fill on a Lighter market over a time range?
  - id: getLighterRecentTrades
    intent: Get the latest Lighter trades
    question: What were the last trades on a Lighter market?
  phrasing_ops: 2
  slug: 0xarchive-lighter-trades-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Health checks and system status
  name: 0xArchive System API
  phrasing_intents:
  - id: healthCheck
    intent: Check whether the API is up
    question: Is the 0xArchive API up right now?
  - id: listSymbols
    intent: List every public market symbol
    question: Which market symbols can I get data for across all venues?
  - id: getPublicStats
    intent: Get public API usage statistics
    question: What headline statistics does the public stats endpoint report?
  - id: getPublicCoverageStatus
    intent: Get the public data coverage status
    question: Is there a public, no-auth view of data coverage across venues?
  phrasing_ops: 4
  slug: 0xarchive-system-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: SIWE authentication for existing wallet accounts and autonomous paid wallet access via x402. Standard Free accounts are created through the browser signup flow.
  name: 0xArchive Web3 Authentication API
  phrasing_intents:
  - id: web3Challenge
    intent: Request a Sign-In with Ethereum challenge
    question: How do I get a SIWE message for my wallet to sign?
  - id: web3Signup
    intent: Call the retired wallet-only free signup
    question: Can I still create a free account with just a wallet?
  - id: web3ListKeys
    intent: List the API keys owned by my wallet
    question: Which API keys belong to my wallet?
  - id: web3RevokeKey
    intent: Revoke a wallet API key
    question: How do I revoke an API key tied to my wallet?
  - id: web3Subscribe
    intent: Buy Build or Pro access with USDC
    question: Can I pay for Build or Pro access with USDC on Base?
  - id: web3Verify
    intent: Verify a signed wallet sign-in message
    question: How do I finish wallet sign-in after signing the SIWE message?
  phrasing_ops: 6
  slug: 0xarchive-web3-authentication-api
artifact_total: 64
asyncapis:
- description: ''
  name: 0Xarchive Websocket Channels
  slug: 0xarchive-websocket-channels
common:
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.0xarchive.io/mcp
- group: company
  title: ''
  type: Website
  url: https://0xarchive.io/
- group: start
  title: ''
  type: Portal
  url: https://docs.0xarchive.io/
- group: other
  title: ''
  type: APICatalog
  url: https://0xarchive.io/.well-known/api-catalog
- group: start
  title: ''
  type: APIOnboarding
  url: https://0xarchive.io/.well-known/api-onboarding
- group: design
  title: ''
  type: SpectralRules
  url: https://0xarchive.io/.well-known/spectral-ruleset.yaml
- group: other
  title: ''
  type: AICatalog
  url: https://0xarchive.io/.well-known/ai-catalog.json
- group: agent
  title: ''
  type: LLMSTxt
  url: https://0xarchive.io/llms.txt
- group: other
  title: ''
  type: x402Facilitator
  url: https://0xarchive.io/facilitator
- group: commercial
  title: ''
  type: Pricing
  url: https://0xarchive.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://0xarchive.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://0xarchive.io/privacy
- group: commercial
  title: ''
  type: DataLicense
  url: https://docs.0xarchive.io/data-rights
- group: auth
  title: ''
  type: Security
  url: https://0xarchive.io/.well-known/security.txt
- group: operate
  title: ''
  type: Status
  url: https://0xarchive.io/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://0xarchive.io/changelog
- group: operate
  title: ''
  type: Support
  url: mailto:support@0xarchive.io
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/0xarchive/refs/heads/main/security/0xarchive-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/0xarchive-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/0xarchive/refs/heads/main/security/0xarchive-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/0xarchive-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/0xarchive/refs/heads/main/authentication/0xarchive-authentication.yml
  title: ''
  type: Authentication
  url: authentication/0xarchive-authentication.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/0xarchive/refs/heads/main/openapi/_original/0xarchive-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/0xarchive-openapi.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/0xarchive/refs/heads/main/overlays/0xarchive-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/0xarchive-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/0xarchive/refs/heads/main/llms/0xarchive-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/0xarchive-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/0xarchive/refs/heads/main/well-known/0xarchive-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/0xarchive-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/0xarchive/refs/heads/main/well-known/0xarchive-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/0xarchive-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/0xarchive/refs/heads/main/a2a/0xarchive-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/0xarchive-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/0xarchive/refs/heads/main/mcp/0xarchive-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/0xarchive-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/0xarchive/refs/heads/main/mcp/0xarchive-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/0xarchive-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/0xarchive/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/0xarchive/refs/heads/main/packages/0xarchive-packages.yml
  title: ''
  type: Packages
  url: packages/0xarchive-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/0xarchive/refs/heads/main/packages/0xarchive-packages.yml
  title: ''
  type: SDKs
  url: packages/0xarchive-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/0xarchive/refs/heads/main/cli/0xarchive-cli.yml
  title: ''
  type: CLI
  url: cli/0xarchive-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/0xarchive/refs/heads/main/conformance/0xarchive-conformance.yml
  title: ''
  type: Conformance
  url: conformance/0xarchive-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/0xarchive/refs/heads/main/errors/0xarchive-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/0xarchive-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/0xarchive/refs/heads/main/lifecycle/0xarchive-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/0xarchive-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://0xarchive.io/status
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/0xarchive/refs/heads/main/scopes/0xarchive-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/0xarchive-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/0xarchive/refs/heads/main/security/0xarchive-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/0xarchive-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/0xarchive/refs/heads/main/conventions/0xarchive-conventions.yml
  title: ''
  type: Conventions
  url: conventions/0xarchive-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/0xarchive/refs/heads/main/sandbox/0xarchive-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/0xarchive-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/0xarchive/refs/heads/main/data-model/0xarchive-data-model.yml
  title: ''
  type: DataModel
  url: data-model/0xarchive-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/0xarchive/refs/heads/main/plans/0xarchive-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/0xarchive-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/0xarchive/refs/heads/main/rate-limits/0xarchive-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/0xarchive-rate-limits.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/0xarchive/refs/heads/main/changelog/0xarchive-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/0xarchive-changelog.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.0xarchive.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.0xarchive.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.0xarchive.io/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.0xarchive.io/quickstart
- group: operate
  title: ''
  type: Support
  url: https://0xarchive.io/contact
- group: company
  title: ''
  type: Blog
  url: https://0xarchive.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/0xArchiveIO
- group: start
  title: ''
  type: SignUp
  url: https://0xarchive.io/signup
- group: start
  title: ''
  type: Login
  url: https://0xarchive.io/login
- group: build
  title: ''
  type: Examples
  url: https://github.com/0xArchiveIO/examples
created: '2026-08-30'
description: '0xArchive is a replayable market-data archive for two decentralised perpetuals venues, Hyperliquid and Lighter, delivered as one REST API, one WebSocket API that carries both live subscriptions and historical replay on a single connection, bulk Parquet export, and a hosted MCP server. Hyperliquid coverage is split into four route families - core perpetuals, Spot, HIP-3 builder perps and HIP-4 binary outcome markets - each with its own symbol format and its own set of available data types. Beyond order books, trades, candles, funding, open interest and liquidations, the archive reconstructs order-level depth that the venues do not serve directly: L4 for the Hyperliquid families and L3 for Lighter. Access is unusually flat - every plan including Free reaches every route family, schema and served depth, and plans gate capacity and Free''s rolling 30-day history window rather than route access. An agent can buy its own 30-day Build or Pro access with an x402 USDC payment on Base
  and receive an API key on settlement, with no human signup step.'
image: https://0xarchive.io/logo-mark.svg
layout: provider
mcp_servers:
- description: Read-only market-data discovery and retrieval for MCP clients across Hyperliquid (core perps, HIP-3 builder perps, HIP-4 outcome markets, Spot) and Lighter.
  name: 0xArchive MCP
  slug: 0xarchive-mcp
- description: ''
  name: 0xArchive MCP Server
  slug: 0xarchive-mcp-server
modified: '2026-09-16'
name: 0xArchive
nav: Providers
network: true
overview: '0xArchive publishes 55 APIs on the [APIs.io](https://apis.io/) network, including Data Quality API, HIP-3 Builder Perps - Breadth API, HIP-3 Builder Perps - Candles API, and 52 more. Tagged areas include Market Data, Historical Data, Crypto, DeFi, and Perpetuals.


  The 0xArchive catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  0xArchive''s developer surface includes developer portal, pricing, status page, changelog, support, authentication, CLI, and 47 more developer resources.'
plans:
- name: 0Xarchive Plans Pricing
  plan_count: 5
  slug: 0xarchive-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 6
  name: 0Xarchive Rate Limits
  slug: 0xarchive-rate-limits
scopes:
- name: 0Xarchive Scopes
  scope_count: 0
  slug: 0xarchive-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 71.6
  coverage:
    artifact_dirs: 26
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 63.7
    developer_ergonomics: 85.7
    discoverability: 91.7
    operational_transparency: 71.1
  previous_composite: 71.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 53
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 43.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/0xarchive/refs/heads/main/screenshots/0xarchive-2026-09-02T144104.png
security:
- kind: authentication
  name: 0Xarchive Authentication
  slug: 0xarchive-authentication
  summary_line: apiKey/oauth2/siwe · 4 schemes
- kind: domain-security
  name: 0Xarchive Domain Security
  slug: 0xarchive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: 0Xarchive Vulnerability Disclosure
  slug: 0xarchive-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: 0xarchive
tags:
- Market Data
- Historical Data
- Crypto
- DeFi
- Perpetuals
- Derivatives
- Order Book
- Hyperliquid
- Lighter
- HIP-3
- HIP-4
- Prediction Markets
- WebSocket
- Streaming
- historical-replay
- Parquet
- Bulk Data
- MCP
- Agent-Native
- x402
- OpenAPI
- REST
- A2A
website: https://0xarchive.io/
---

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
  scored_at: '2026-09-16'
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
  slug: 0xarchive-data-quality-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: 'HIP-3 market breadth snapshots: percentage of eligible instruments trading above their current UTC-session VWAP.'
  name: 0xArchive HIP-3 Builder Perps - Breadth API
  slug: 0xarchive-hip-3-builder-perps-breadth-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: 'HIP-3 Builder Perps OHLCV candle data. Intervals: 1m, 5m, 15m, 30m, 1h, 4h, 1d, 1w. Coverage is symbol-specific; verify the selected market before choosing a time range.'
  name: 0xArchive HIP-3 Builder Perps - Candles API
  slug: 0xarchive-hip-3-builder-perps-candles-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: 'HIP-3 convenience endpoints: freshness, summary, and price history.'
  name: 0xArchive HIP-3 Builder Perps - Convenience API
  slug: 0xarchive-hip-3-builder-perps-convenience-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Full-depth aggregated L2 order book snapshots, checkpoint history, and diffs for HIP-3 builder perps derived from L4 data. Full-depth checkpoints and diffs where available.
  name: 0xArchive HIP-3 Builder Perps - Full-Depth L2 Order Book API
  slug: 0xarchive-hip-3-builder-perps-full-depth-l2-order-book-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: HIP-3 Builder Perps funding rate history. Coverage is symbol-specific; inspect `/v1/symbols` `coverage_by_type.funding` before choosing a time range.
  name: 0xArchive HIP-3 Builder Perps - Funding API
  slug: 0xarchive-hip-3-builder-perps-funding-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: HIP-3 Builder Perps instrument discovery. Use this route with `/v1/symbols` `coverage_by_type` to resolve the current inventory and schema-specific dates.
  name: 0xArchive HIP-3 Builder Perps - Instruments API
  slug: 0xarchive-hip-3-builder-perps-instruments-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Individual order-level (L4) orderbook data for HIP-3 builder perps.
  name: 0xArchive HIP-3 Builder Perps - L4 Order Book API
  slug: 0xarchive-hip-3-builder-perps-l4-order-book-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: HIP-3 Builder Perps liquidation-related fills. Coverage is symbol-specific; verify the selected market before choosing a time range.
  name: 0xArchive HIP-3 Builder Perps - Liquidations API
  slug: 0xarchive-hip-3-builder-perps-liquidations-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: HIP-3 Builder Perps historical open interest data. Coverage is symbol-specific; inspect `/v1/symbols` `coverage_by_type.oi` before choosing a time range.
  name: 0xArchive HIP-3 Builder Perps - Open Interest API
  slug: 0xarchive-hip-3-builder-perps-open-interest-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: The HIP-3 Builder Perps - Oracle API from 0xArchive — 2 operation(s) for hip-3 builder perps - oracle.
  name: 0xArchive HIP-3 Builder Perps - Oracle API
  slug: 0xarchive-hip-3-builder-perps-oracle-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: HIP-3 Builder Perps venue-native L2 order book snapshots. Native Hyperliquid source snapshots are capped at 20 levels per side; use the full-depth L2 routes for full-depth aggregated L2.
  name: 0xArchive HIP-3 Builder Perps - Order Book API
  slug: 0xarchive-hip-3-builder-perps-order-book-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Order lifecycle events for HIP-3 builder perps.
  name: 0xArchive HIP-3 Builder Perps - Orders API
  slug: 0xarchive-hip-3-builder-perps-orders-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: HIP-3 Builder Perps historical trade/fill data. Coverage is symbol-specific; inspect `/v1/symbols` `coverage_by_type.trades` before choosing a time range.
  name: 0xArchive HIP-3 Builder Perps - Trades API
  slug: 0xarchive-hip-3-builder-perps-trades-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: The HIP-3 Builder Perps - Wallets API from 0xArchive — 1 operation(s) for hip-3 builder perps - wallets.
  name: 0xArchive HIP-3 Builder Perps - Wallets API
  slug: 0xarchive-hip-3-builder-perps-wallets-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: The HIP-3 - Liquidations API from 0xArchive — 2 operation(s) for hip-3 - liquidations.
  name: 0xArchive HIP-3 - Liquidations API
  slug: 0xarchive-hip-3-liquidations-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: The HIP-3 - Orders API from 0xArchive — 2 operation(s) for hip-3 - orders.
  name: 0xArchive HIP-3 - Orders API
  slug: 0xarchive-hip-3-orders-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: OHLCV candles for HIP-4 outcome sides. Prices are implied probabilities (0..1); quote_volume in USDH.
  name: 0xArchive HIP-4 Outcomes - Candles API
  slug: 0xarchive-hip-4-outcomes-candles-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: 'HIP-4 convenience endpoints: freshness, summary, and price history. `mark_price` for HIP-4 is an implied probability in [0,1], not a USD price.'
  name: 0xArchive HIP-4 Outcomes - Convenience API
  slug: 0xarchive-hip-4-outcomes-convenience-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: 'HIP-4 per-side instrument discovery (one row per `#N` coin). Each outcome has two sides: side 0 (Yes) and side 1 (No). Coins are `#`-prefixed. Data from May 2026.'
  name: 0xArchive HIP-4 Outcomes - Instruments API
  slug: 0xarchive-hip-4-outcomes-instruments-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: HIP-4 outcome markets per-side open interest history. Display/paired/parity aggregates live on the `/outcomes/{outcome_id}` detail endpoint, not here. Data from May 2026.
  name: 0xArchive HIP-4 Outcomes - Open Interest API
  slug: 0xarchive-hip-4-outcomes-open-interest-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: HIP-4 outcome markets L2 and L4 order book snapshots and diffs. Coins are referenced by numeric id (0, 1, 10, 11, ...); the `#`-prefixed form is also accepted. Data from May 2026.
  name: 0xArchive HIP-4 Outcomes - Order Book API
  slug: 0xarchive-hip-4-outcomes-order-book-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: 'Order lifecycle events for HIP-4 outcome markets: placements, cancellations, fills, and TP/SL triggers.'
  name: 0xArchive HIP-4 Outcomes - Orders API
  slug: 0xarchive-hip-4-outcomes-orders-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: HIP-4 outcome market discovery (one row per outcome, both sides combined). Use these to enumerate live and settled binary outcome markets. Data from May 2026.
  name: 0xArchive HIP-4 Outcomes - Outcomes API
  slug: 0xarchive-hip-4-outcomes-outcomes-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: The HIP-4 Outcomes - Questions API from 0xArchive — 2 operation(s) for hip-4 outcomes - questions.
  name: 0xArchive HIP-4 Outcomes - Questions API
  slug: 0xarchive-hip-4-outcomes-questions-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: HIP-4 outcome markets historical trade/fill data. Data from May 2026.
  name: 0xArchive HIP-4 Outcomes - Trades API
  slug: 0xarchive-hip-4-outcomes-trades-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: 'Hyperliquid OHLCV candle data. Intervals: 1m, 5m, 15m, 30m, 1h, 4h, 1d, 1w.'
  name: 0xArchive Hyperliquid - Candles API
  slug: 0xarchive-hyperliquid-candles-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: 'Hyperliquid convenience endpoints: freshness, summary, and price history.'
  name: 0xArchive Hyperliquid - Convenience API
  slug: 0xarchive-hyperliquid-convenience-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Full-depth aggregated L2 order book snapshots, checkpoint history, and diffs for Hyperliquid perpetuals derived from L4 data. Full-depth checkpoints and diffs where available.
  name: 0xArchive Hyperliquid - Full-Depth L2 Order Book API
  slug: 0xarchive-hyperliquid-full-depth-l2-order-book-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Hyperliquid funding rate history. Data from May 2023.
  name: 0xArchive Hyperliquid - Funding API
  slug: 0xarchive-hyperliquid-funding-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Hyperliquid available trading instruments and their specifications. Authenticated inventory contains 232 core perpetual rows.
  name: 0xArchive Hyperliquid - Instruments API
  slug: 0xarchive-hyperliquid-instruments-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Individual resting-order (L4) book state for Hyperliquid perpetuals, including price, size, order ID, wallet attribution, queue priority, diffs, and checkpoints.
  name: 0xArchive Hyperliquid - L4 Order Book API
  slug: 0xarchive-hyperliquid-l4-order-book-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Hyperliquid liquidation events with user attribution. The observed global floor is July 27, 2025; exact starts vary by symbol.
  name: 0xArchive Hyperliquid - Liquidations API
  slug: 0xarchive-hyperliquid-liquidations-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Hyperliquid historical open interest and market context data. Data from May 2023.
  name: 0xArchive Hyperliquid - Open Interest API
  slug: 0xarchive-hyperliquid-open-interest-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Hyperliquid venue-native L2 order book snapshots. Native Hyperliquid source snapshots are capped at 20 levels per side; use the full-depth L2 routes for full-depth aggregated L2.
  name: 0xArchive Hyperliquid - Order Book API
  slug: 0xarchive-hyperliquid-order-book-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: 'Order lifecycle events for Hyperliquid perpetuals: placements, cancellations, fills, and TP/SL triggers.'
  name: 0xArchive Hyperliquid - Orders API
  slug: 0xarchive-hyperliquid-orders-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Hyperliquid Spot pair, order book, trade, reconstruction, TWAP, and freshness routes.
  name: 0xArchive Hyperliquid Spot API
  slug: 0xarchive-hyperliquid-spot-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: OHLCV candles for spot pairs (1m base, rolled up on demand).
  name: 0xArchive Hyperliquid Spot - Candles API
  slug: 0xarchive-hyperliquid-spot-candles-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: The Hyperliquid Spot - Order Book API from 0xArchive — 1 operation(s) for hyperliquid spot - order book.
  name: 0xArchive Hyperliquid Spot - Order Book API
  slug: 0xarchive-hyperliquid-spot-order-book-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Hyperliquid historical trade/fill data with full execution details. Data from April 2023.
  name: 0xArchive Hyperliquid - Trades API
  slug: 0xarchive-hyperliquid-trades-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: The Hyperliquid - Wallets API from 0xArchive — 1 operation(s) for hyperliquid - wallets.
  name: 0xArchive Hyperliquid - Wallets API
  slug: 0xarchive-hyperliquid-wallets-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Deprecated endpoints that default to Hyperliquid. Use the exchange-specific endpoints (`/v1/hyperliquid/*`, `/v1/lighter/*`, `/v1/hyperliquid/hip3/*`) instead.
  name: 0xArchive Legacy API
  slug: 0xarchive-legacy-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: 'Lighter OHLCV candle data. Intervals: 1m, 5m, 15m, 30m, 1h, 4h, 1d, 1w. Data from August 2025.'
  name: 0xArchive Lighter - Candles API
  slug: 0xarchive-lighter-candles-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: 'Lighter convenience endpoints: freshness, summary, and price history.'
  name: 0xArchive Lighter - Convenience API
  slug: 0xarchive-lighter-convenience-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Lighter funding rate history. Data from August 2025.
  name: 0xArchive Lighter - Funding API
  slug: 0xarchive-lighter-funding-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Lighter available trading instruments and their specifications.
  name: 0xArchive Lighter - Instruments API
  slug: 0xarchive-lighter-instruments-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Individual order-level (L3) orderbook data for Lighter. Data from March 2026.
  name: 0xArchive Lighter - L3 Order Book API
  slug: 0xarchive-lighter-l3-order-book-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: The Lighter - Liquidations API from 0xArchive — 2 operation(s) for lighter - liquidations.
  name: 0xArchive Lighter - Liquidations API
  slug: 0xarchive-lighter-liquidations-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Lighter historical open interest data. Data from August 2025.
  name: 0xArchive Lighter - Open Interest API
  slug: 0xarchive-lighter-open-interest-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Lighter L2 order book snapshots with configurable granularity. Checkpoint history starts January 29, 2026; 30s/10s/1s start January 30, 2026; tick reconstruction available.
  name: 0xArchive Lighter - Order Book API
  slug: 0xarchive-lighter-order-book-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Lighter historical fill data across more than 200 markets. Served history begins August 27, 2025, with exact starts varying by market.
  name: 0xArchive Lighter - Trades API
  slug: 0xarchive-lighter-trades-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: Health checks and system status
  name: 0xArchive System API
  slug: 0xarchive-system-api
- baseURL: https://api.0xarchive.io
  baseurl_source: declared
  description: SIWE authentication for existing wallet accounts and autonomous paid wallet access via x402. Standard Free accounts are created through the browser signup flow.
  name: 0xArchive Web3 Authentication API
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
overview: '0xArchive publishes 53 APIs on the [APIs.io](https://apis.io/) network, including Data Quality API, HIP-3 Builder Perps - Breadth API, HIP-3 Builder Perps - Candles API, and 50 more. Tagged areas include Market Data, Historical Data, Crypto, DeFi, and Perpetuals.


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
  composite: 76.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.7
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 69.6
    developer_ergonomics: 85.7
    discoverability: 94.4
    operational_transparency: 71.1
  previous_composite: 72.7
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
    score: 78.3
  schema_version: 0.22.0
  scored_at: '2026-09-16'
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
- agent-native
- x402
- OpenAPI
- REST
website: https://0xarchive.io/
---

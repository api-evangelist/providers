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
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.9
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: 'REST API for prediction market data across Kalshi and Polymarket: full-text search over markets, events, and series; historical orderbook snapshots, top-of-book timeseries, trades, and OHLCV bars; wha'
  name: Oddpool API
  slug: oddpool-api
- baseURL: wss://feeds.oddpool.com/ws
  baseurl_source: declared
  description: Single-connection WebSocket streaming real-time, normalized cross-venue prediction market data (dist, book, trade, and snapshot channels) for macro economic events and crypto (BTC/ETH) markets enriche
  name: Oddpool WebSocket Feeds
  slug: oddpool-websocket-feeds
artifact_total: 5
asyncapis:
- description: Single-connection WebSocket streaming real-time, normalized cross-venue prediction market data from Kalshi and Polymarket. Data is addressed by what (event_key / outcome) not where (venue). Four chann
  name: Oddpool WebSocket Feeds
  slug: oddpool-feeds-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://www.oddpool.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.oddpool.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oddpool.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.oddpool.com/llms.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oddpool.com/index.md
- group: commercial
  title: ''
  type: Pricing
  url: https://oddpool.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://oddpool.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://oddpool.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://oddpool.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://cal.com/team/oddpool/30-minute-meeting
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/oddpool-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/oddpool-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/oddpool-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/oddpool-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/oddpool-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/oddpool-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/oddpool-lifecycle.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/oddpool-mcp.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/oddpool-feeds-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/oddpool-feeds-asyncapi.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oddpool-domain-security.yml
created: '2026-07-17'
description: Oddpool is an institutional-grade data platform for prediction markets, offering unified access to market data across Kalshi and Polymarket through a single REST API and WebSocket feed. It describes itself as "the search engine for prediction markets," normalizing hundreds of thousands of markets into a common model so quant funds, trading desks, and prosumer traders can search markets and events, pull tick-level historical orderbooks and OHLCV bars, track whale trades, detect cross-venue arbitrage, and stream real-time cross-venue probability distributions, orderbooks, and trades. Data is addressed by what (event and outcome keys) rather than by venue-specific tickers. A separate enterprise Reference Data API provides canonical cross-venue identifiers, fungibility classification, and a Wikidata cross-walk for institutional clients.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oddpool.png
layout: provider
modified: '2026-07-20'
name: Oddpool
nav: Providers
network: true
overview: 'Oddpool publishes 1 API on the [APIs.io](https://apis.io/) network: WebSocket Feeds. Tagged areas include Company, Prediction Markets, Market Data, Financial Data, and Trading.


  The Oddpool catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Oddpool''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, authentication, and 14 more developer resources.'
random_paper: 18
score:
  band: developing
  composite: 40.5
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 41.7
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 40.5
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oddpool/refs/heads/main/screenshots/oddpool-2026-08-07T185952.png
security:
- kind: authentication
  name: Oddpool Authentication
  slug: oddpool-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Oddpool Domain Security
  slug: oddpool-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oddpool
tags:
- Company
- Prediction Markets
- Market Data
- Financial Data
- Trading
- Fintech
- Data Aggregation
- WebSocket
- Historical Data
- Kalshi
- Polymarket
website: https://www.oddpool.com
---

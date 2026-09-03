---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 20.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Polymarket Agentic Access
  operation_count: 5
  slug: polymarket-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 1
apis:
- description: Central-limit order book REST API for Polymarket - place, cancel, and query orders, list markets and tokens, fetch order books and trades, and look up user positions. Used by traders and bots interact
  name: Polymarket CLOB API
  slug: clob-api
- description: Read-only metadata API for markets, events, tags, and categories - the surface that powers polymarket.com's listings and search. Useful for discovery and for stitching multiple binary markets into the
  name: Polymarket Gamma API
  slug: gamma-api
- description: Historical and analytical data API exposing trades, prices, volumes, holders, and time-series aggregates across Polymarket markets, intended for research, dashboards, and quantitative use.
  name: Polymarket Data API
  slug: data-api
- description: Real-time streaming feed for order book updates, trades, and market events on the Polymarket CLOB - used by trading clients to maintain a live view of the book without polling.
  name: Polymarket WebSocket
  slug: websocket
- description: Official Python SDK for the Polymarket CLOB API - wallet signing, EIP-712 order construction, place / cancel / query, and market data helpers.
  name: py-clob-client (Python SDK)
  slug: py-clob-client
- description: Official TypeScript / JavaScript SDK for the Polymarket CLOB API - typed clients, wallet integration (viem), order construction, and market data helpers.
  name: clob-client (TypeScript SDK)
  slug: clob-client-ts
- description: Official Rust SDK for the Polymarket CLOB API.
  name: clob-client (Rust SDK)
  slug: clob-client-rust
- baseURL: https://clob.polymarket.com
  baseurl_source: declared
  description: Public CLOB market data.
  name: Polymarket CLOB Market Data API
  slug: polymarket-clob-market-data-api
- baseURL: https://clob.polymarket.com
  baseurl_source: declared
  description: Order placement and management on the central-limit order book.
  name: Polymarket CLOB Trade API
  slug: polymarket-clob-trade-api
- baseURL: https://clob.polymarket.com
  baseurl_source: declared
  description: Read-only event metadata.
  name: Polymarket Gamma Events API
  slug: polymarket-gamma-events-api
- baseURL: https://clob.polymarket.com
  baseurl_source: declared
  description: Read-only market metadata.
  name: Polymarket Gamma Markets API
  slug: polymarket-gamma-markets-api
artifact_total: 25
asyncapis:
- description: 'Real-time streaming feed for Polymarket''s central-limit order book (CLOB). Two channels are exposed: a public market channel that streams order book snapshots, price level updates, tick size changes, '
  name: Polymarket CLOB WebSocket API
  slug: polymarket-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Polymarket APIs (CLOB and Gamma) CLOB Market Data API
  slug: open-polymarket-clob-market-data-api
- collection_type: open
  name: Polymarket APIs (CLOB and Gamma) CLOB Market Data CLOB Trade API
  slug: open-polymarket-clob-trade-api
- collection_type: open
  name: Polymarket APIs (CLOB and Gamma) CLOB Market Data Gamma Events API
  slug: open-polymarket-gamma-events-api
- collection_type: open
  name: Polymarket APIs (CLOB and Gamma) CLOB Market Data Gamma Markets API
  slug: open-polymarket-gamma-markets-api
- collection_type: open
  name: Polymarket APIs (CLOB and Gamma)
  slug: open-polymarket
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Polymarket/py-clob-client/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/Polymarket/py-clob-client/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/Polymarket/py-clob-client/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/Polymarket/py-clob-client/blob/main/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/Polymarket/py-clob-client/blob/main/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/Polymarket/py-clob-client/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/polymarket-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/polymarket-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/polymarket-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://polymarket.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.polymarket.com/
- group: docs
  title: ''
  type: US Documentation
  url: https://docs.polymarket.us/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Polymarket
- group: other
  title: ''
  type: Builders Program
  url: https://builders.polymarket.com/
- group: operate
  title: ''
  type: Support
  url: https://help.polymarket.com/
- group: operate
  title: ''
  type: Status
  url: https://status.polymarket.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/polymarket/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.polymarket.us/llms.txt
created: '2026-05-23'
description: Polymarket is a decentralized prediction-market platform built on Polygon where users buy and sell binary outcome shares in real-world events. Settlement is on-chain via the UMA optimistic oracle, while order matching runs through a hybrid central-limit order book (CLOB). Developer surface includes the CLOB API for order placement and market data, the Gamma API for market and event metadata, a Data API for historical and analytical reads, a WebSocket stream, and official CLOB client SDKs in TypeScript, Python, and Rust.
finops:
- name: Polymarket Finops
  service_category: API
  slug: polymarket-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/polymarket.png
layout: provider
modified: '2026-05-29'
name: Polymarket
nav: Providers
network: true
overview: 'Polymarket publishes 5 APIs on the [APIs.io](https://apis.io/) network, including WebSocket, CLOB Market Data API, CLOB Trade API, and 2 more. Tagged areas include Prediction Markets, DeFi, Polygon, Order Book, and Crypto.


  The Polymarket catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Polymarket''s developer surface includes authentication, documentation, GitHub presence, support, status page, and 13 more developer resources.'
plans:
- name: Polymarket Plans Pricing
  plan_count: 1
  slug: polymarket-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Polymarket Rate Limits
  slug: polymarket-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Polymarket API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: polymarket-asyncapi-spectral-rules
score:
  band: developing
  composite: 46.7
  coverage:
    artifact_dirs: 12
    catalog_gap: 55.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 11.4
    contract_quality: 59.4
    developer_ergonomics: 26.2
    discoverability: 75.9
    governance: 11.4
    operational_transparency: 52.6
  open_source:
    applies: true
    score: 100.0
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 30.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/polymarket/refs/heads/main/screenshots/polymarket-2026-06-20T191927.png
security:
- kind: authentication
  name: Polymarket Authentication
  slug: polymarket-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Polymarket Domain Security
  slug: polymarket-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: polymarket
tags:
- Prediction Markets
- DeFi
- Polygon
- Order Book
- Crypto
- Markets
website: https://polymarket.com/
---

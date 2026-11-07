---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: wss://streams.fast.onetrading.com
  baseurl_source: declared
  description: Real-time WebSocket API for market data (order book, price ticks, book ticker) and, after authenticating, private trading events (order lifecycle, trades, settlement, funding payments, balance adjustm
  name: One Trading WebSocket Streams API
  slug: one-trading-websocket-streams-api
- baseURL: https://api.onetrading.com/fast
  baseurl_source: declared
  description: Subaccount balance transfers
  name: One Trading Funding API
  slug: one-trading-funding-api
- baseURL: https://api.onetrading.com/fast
  baseurl_source: declared
  description: Futures positions, funding and portfolio endpoints
  name: One Trading Futures API
  slug: one-trading-futures-api
- baseURL: https://api.onetrading.com/fast
  baseurl_source: declared
  description: Public market-data endpoints (no authentication)
  name: One Trading Public API
  slug: one-trading-public-api
- baseURL: https://api.onetrading.com/fast
  baseurl_source: declared
  description: Account order and trade endpoints (Bearer token, TRADE/READ scope)
  name: One Trading API
  slug: one-trading-trading-api
artifact_total: 16
asyncapis:
- description: Real-time WebSocket (WSS) API for the One Trading exchange. Clients receive market data feeds (order book, price ticks, book ticker) and, after authenticating, private trading event streams (order lif
  name: One Trading WebSocket Streams API
  slug: one-trading-streams-asyncapi
collections:
- collection_type: open
  name: One Trading Fast Funding API
  slug: open-one-trading-funding-api
- collection_type: open
  name: One Trading Fast Funding Futures API
  slug: open-one-trading-futures-api
- collection_type: open
  name: One Trading Fast Funding Public API
  slug: open-one-trading-public-api
- collection_type: open
  name: One Fast Funding Trading API
  slug: open-one-trading-trading-api
common:
- group: other
  href: https://artifacts.apis.io/one-trading/overlays/one-trading-fast-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/one-trading-fast-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/one-trading/security/one-trading-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/one-trading-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://onetrading.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.onetrading.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.onetrading.com/rest/public/currencies
- group: start
  title: ''
  type: GettingStarted
  url: https://support.onetrading.com/hc/en-gb/articles/16357722538129-What-should-I-know-about-One-Trading-API
- group: operate
  title: ''
  type: Support
  url: https://support.onetrading.com/hc/en-gb
- group: company
  title: ''
  type: Blog
  url: https://onetrading.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/one-trading
- group: commercial
  title: ''
  type: Pricing
  url: https://onetrading.com/fees
- group: start
  title: ''
  type: Login
  url: https://account.onetrading.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://onetrading.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://onetrading.com/privacy-policy
- group: agent
  href: https://artifacts.apis.io/one-trading/llms/one-trading-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/one-trading-llms.txt
- group: auth
  href: https://artifacts.apis.io/one-trading/authentication/one-trading-authentication.yml
  title: ''
  type: Authentication
  url: authentication/one-trading-authentication.yml
- group: design
  href: https://artifacts.apis.io/one-trading/conventions/one-trading-conventions.yml
  title: ''
  type: Conventions
  url: conventions/one-trading-conventions.yml
- group: design
  href: https://artifacts.apis.io/one-trading/conventions/one-trading-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/one-trading-conventions.yml
- group: design
  href: https://artifacts.apis.io/one-trading/errors/one-trading-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/one-trading-problem-types.yml
- group: design
  href: https://artifacts.apis.io/one-trading/lifecycle/one-trading-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/one-trading-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/one-trading/data-model/one-trading-data-model.yml
  title: ''
  type: DataModel
  url: data-model/one-trading-data-model.yml
- group: design
  href: https://artifacts.apis.io/one-trading/conformance/one-trading-conformance.yml
  title: ''
  type: Conformance
  url: conformance/one-trading-conformance.yml
- group: build
  href: https://artifacts.apis.io/one-trading/packages/one-trading-packages.yml
  title: ''
  type: Packages
  url: packages/one-trading-packages.yml
- group: agent
  href: https://artifacts.apis.io/one-trading/mcp/one-trading-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/one-trading-mcp.yml
- group: agent
  href: https://artifacts.apis.io/one-trading/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  href: https://artifacts.apis.io/one-trading/asyncapi/one-trading-streams-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/one-trading-streams-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/one-trading/asyncapi/one-trading-streams-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/one-trading-streams-asyncapi.yml
created: '2026-07-17'
description: One Trading (One Trading Exchange B.V.) is an EU-regulated cryptocurrency and derivatives exchange for retail and institutional traders, positioning itself as "the world's fastest exchange." It offers spot crypto plus crypto futures (up to 10x leverage), index futures and 24/7 equity futures. Its public "Fast API" provides REST market-data and trading endpoints (currencies, instruments, order book, candlesticks, ticker, fees, funding rates, orders, trades, futures positions and subaccount transfers) at https://api.onetrading.com/fast, plus a real-time WebSocket streams API at wss://streams.fast.onetrading.com. Formerly operated as Bitpanda Pro. This profile was surfaced as a Speedinvest portfolio company and enriched by the API Evangelist pipeline from the provider's public documentation and live endpoints.
image: https://framerusercontent.com/images/m2JxgHpA4PAHjVJIacTjS6wnvRY.png
layout: provider
modified: '2026-09-16'
name: One Trading
nav: Providers
network: true
overview: 'One Trading publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including WebSocket Streams API, Funding API, Futures API, and 2 more. Tagged areas include Company, Cryptocurrency, Cryptocurrency Exchange, Trading, and Derivatives.


  The One Trading catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  One Trading''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 19 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: One Trading API Rules
  rule_count: 54
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 1
  slug: one-trading-rules
score:
  band: thin
  composite: 34.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 23.9
    developer_ergonomics: 49.4
    discoverability: 73.2
    operational_transparency: 10.5
  previous_composite: 34.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 23.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/one-trading/one-trading-2026-08-07T190256.png
security:
- kind: authentication
  name: One Trading Authentication
  slug: one-trading-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: One Trading Domain Security
  slug: one-trading-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Monitor and manage a futures portfolio
  slug: one-trading-manage-futures
- name: Place and manage a limit order
  slug: one-trading-place-limit-order
- name: Stream real-time market data
  slug: one-trading-stream-market-data
slug: one-trading
tags:
- Company
- Cryptocurrency
- Cryptocurrency Exchange
- Trading
- Derivatives
- Futures
- Financial Services
- Market Data
- WebSocket
- Fintech
- Real-Time
website: https://onetrading.com
---

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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: na
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Siftingio Agentic Access
  operation_count: 37
  slug: siftingio-agentic-access
  summary_line: 37 operations
api_count: 1
apis:
- baseURL: wss://stream.sifting.io/ws/v1
  baseurl_source: declared
  description: WebSocket streaming API for live market data, described by an AsyncAPI 3.0 contract. Also offers a documented FIX API.
  name: SiftingIO Live Stream
  slug: siftingio-live-stream
- description: LOCALLY-RUN MCP server, not a hosted endpoint. The client launches it (`npx -y siftingio-mcp`, or the Python package) and it runs on the user's own machine, reading the key from SIFTING_API_KEY. 36 to
  name: SiftingIO MCP Server
  slug: siftingio-mcp-server
- baseURL: https://api.sifting.io
  baseurl_source: declared
  description: Historical OHLC bars for commodities (metals, energy, industrials).
  name: SiftingIO Commodities API
  slug: siftingio-commodities-api
- baseURL: https://api.sifting.io
  baseurl_source: declared
  description: Live currency and token conversion across forex and crypto.
  name: SiftingIO Convert API
  slug: siftingio-convert-api
- baseURL: https://api.sifting.io
  baseurl_source: declared
  description: Historical OHLCV bars for crypto symbols.
  name: SiftingIO Crypto API
  slug: siftingio-crypto-api
- baseURL: https://api.sifting.io
  baseurl_source: declared
  description: On-chain wallet portfolios and historical DEX bars.
  name: SiftingIO DEX API
  slug: siftingio-dex-api
- baseURL: https://api.sifting.io
  baseurl_source: declared
  description: US macro economic events.
  name: SiftingIO Economic Calendar API
  slug: siftingio-economiccalendar-api
- baseURL: https://api.sifting.io
  baseurl_source: declared
  description: 13F institutional holdings.
  name: SiftingIO Filers API
  slug: siftingio-filers-api
- baseURL: https://api.sifting.io
  baseurl_source: declared
  description: Historical OHLC bars for FX pairs.
  name: SiftingIO Forex API
  slug: siftingio-forex-api
- baseURL: https://api.sifting.io
  baseurl_source: declared
  description: Live market data read from the engine's latest snapshot.
  name: SiftingIO Live API
  slug: siftingio-live-api
- baseURL: https://api.sifting.io
  baseurl_source: declared
  description: Market catalog, status, hours, and holiday calendars.
  name: SiftingIO Markets API
  slug: siftingio-markets-api
- baseURL: https://api.sifting.io
  baseurl_source: declared
  description: Technical-analysis signals (live and historical) across stocks, forex, crypto, and commodities.
  name: SiftingIO Signals API
  slug: siftingio-signals-api
- baseURL: https://api.sifting.io
  baseurl_source: declared
  description: US-equity fundamentals (SEC) and historical bars.
  name: SiftingIO Stocks API
  slug: siftingio-stocks-api
artifact_total: 21
asyncapis:
- description: WebSocket API for live market data. Connect to `wss://stream.sifting.io/ws/v1?key=sft_...` — the API key is passed as the `key` query parameter (the only WebSocket auth method). After connecting, send
  name: SiftingIO Live Stream
  slug: siftingio-asyncapi
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/SiftingIO/siftingio-mcp/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/siftingio-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/siftingio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/siftingio-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/siftingio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/siftingio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: https://sifting.io/sdks
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/siftingio-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/siftingio-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/siftingio-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/siftingio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/siftingio-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/siftingio-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/siftingio-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/siftingio-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://siftingio.instatus.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://sifting.io/docs/quickstart
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/siftingio-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://sifting.io/changelog
- group: commercial
  title: ''
  type: Plans
  url: plans/siftingio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/siftingio-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/siftingio-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/siftingio-components.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/siftingio-commodities-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/siftingio-convert-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/siftingio-crypto-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/siftingio-dex-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/siftingio-economiccalendar-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/siftingio-filers-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/siftingio-forex-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/siftingio-live-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/siftingio-markets-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/siftingio-signals-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/siftingio-stocks-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://sifting.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sifting.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://sifting.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://sifting.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://sifting.io/docs/quickstart
- group: docs
  title: ''
  type: OpenAPI
  url: https://sifting.io/openapi.yaml
- group: docs
  title: ''
  type: AsyncAPI
  url: https://sifting.io/asyncapi.yaml
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/siftingio/siftingio-market-data-api
- group: operate
  title: ''
  type: Support
  url: https://sifting.io/contact
- group: operate
  title: ''
  type: Community
  url: https://sifting.io/community/slack
- group: company
  title: ''
  type: Blog
  url: https://sifting.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SiftingIO
- group: commercial
  title: ''
  type: Pricing
  url: https://sifting.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://sifting.io/register
- group: start
  title: ''
  type: Login
  url: https://sifting.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sifting.io/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sifting.io/legal/privacy-policy
created: '2026-08-17'
description: Cross-asset market data APIs covering US equities, forex, cryptocurrency, DeFi/on-chain, commodities, and SEC/EDGAR fundamentals, aggregated across venues and normalized into one JSON schema so every asset class shares the same fields, auth model and integration flow. Delivered over REST (37 operations under a public OpenAPI 3.1 contract), a WebSocket stream described by a public AsyncAPI 3.0 contract, and a documented FIX 4.4 market-data feed. Fundamentals cover filings, filing-text extraction and risk-factor diffs, XBRL financials, ratios, insiders, ownership and 13F holdings; reference data covers market status, hours and holiday calendars; derived data covers technical signals and on-chain TVL. Official Go, Python and JavaScript SDKs, an open-source (locally-run) MCP server with 36 tools, and a provider-published agent ruleset. Operated by SaltingIO LLC, a Wyoming company; explicitly not a broker, exchange or trading venue.
image: https://sifting.io/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: SiftingIO MCP Server
  slug: siftingio-mcp-server
- description: 'SiftingIO market data: live crypto/forex/metals prices, OHLCV bars, SEC fundamentals, 13F data. Returns the same normalized shapes as the REST API, with structuredContent alongside the text on the sna'
  name: SiftingIO MCP Server
  slug: siftingio-mcp-server-2
modified: '2026-08-17'
name: SiftingIO
nav: Providers
network: true
overview: 'SiftingIO publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Live Stream, Commodities API, Convert API, and 9 more. Tagged areas include Financial market data, Stocks/equities, Forex, Cryptocurrency, and DeFi/on-chain.


  The SiftingIO catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SiftingIO''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, support, and 45 more developer resources.'
plans:
- name: Siftingio Plans Pricing
  plan_count: 5
  slug: siftingio-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 9
  name: Siftingio Rate Limits
  slug: siftingio-rate-limits
score:
  band: strong
  composite: 63.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 56.0
    catalog_earned_first_party: 24.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 59.0
    developer_ergonomics: 83.3
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 57.9
  previous_composite: 63.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/siftingio/refs/heads/main/screenshots/siftingio-2026-09-02T155422.png
security:
- kind: authentication
  name: Siftingio Authentication
  slug: siftingio-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Siftingio Domain Security
  slug: siftingio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: siftingio
tags:
- Financial market data
- Stocks/equities
- Forex
- Cryptocurrency
- DeFi/on-chain
- Commodities
- SEC Filings
- XBRL
- Fundamentals
- Fintech
- Quant/trading infrastructure
- Real-Time Streaming
- WebSocket
- FIX
- Financial Data
- Market Data
- Stocks
- DeFi
- Real-Time
- REST API
- MCP Server
- agent-native
website: https://sifting.io
---

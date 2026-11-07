---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.2
  scored_at: '2026-11-06'
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
- baseURL: wss://stream.sifting.io/ws/v1
  baseurl_source: declared
  description: US macro economic events.
  name: SiftingIO Economic Calendar API
  slug: siftingio-economic-calendar-api
artifact_total: 28
asyncapis:
- description: WebSocket API for live market data. Connect to `wss://stream.sifting.io/ws/v1?key=sft_...` — the API key is passed as the `key` query parameter (the only WebSocket auth method). After connecting, send
  name: SiftingIO Live Stream
  slug: siftingio-asyncapi
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://sifting.io/blog/feed.xml
- group: commercial
  title: ''
  type: License
  url: https://github.com/SiftingIO/siftingio-mcp/blob/main/LICENSE
- group: agent
  href: https://artifacts.apis.io/siftingio/agentic-access/siftingio-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/siftingio-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/siftingio/security/siftingio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/siftingio-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/siftingio/authentication/siftingio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/siftingio-authentication.yml
- group: build
  href: https://artifacts.apis.io/siftingio/packages/siftingio-packages.yml
  title: ''
  type: Packages
  url: packages/siftingio-packages.yml
- group: build
  href: https://artifacts.apis.io/siftingio/packages/siftingio-packages.yml
  title: ''
  type: SDKs
  url: packages/siftingio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: https://sifting.io/sdks
- group: agent
  href: https://artifacts.apis.io/siftingio/llms/siftingio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/siftingio-llms.txt
- group: agent
  href: https://artifacts.apis.io/siftingio/mcp/siftingio-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/siftingio-mcp.yml
- group: build
  href: https://artifacts.apis.io/siftingio/mcp/siftingio-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/siftingio-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/siftingio/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/siftingio/conventions/siftingio-conventions.yml
  title: ''
  type: Conventions
  url: conventions/siftingio-conventions.yml
- group: design
  href: https://artifacts.apis.io/siftingio/errors/siftingio-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/siftingio-problem-types.yml
- group: design
  href: https://artifacts.apis.io/siftingio/conformance/siftingio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/siftingio-conformance.yml
- group: design
  href: https://artifacts.apis.io/siftingio/data-model/siftingio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/siftingio-data-model.yml
- group: design
  href: https://artifacts.apis.io/siftingio/lifecycle/siftingio-lifecycle.yml
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
  href: https://artifacts.apis.io/siftingio/changelog/siftingio-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/siftingio-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://sifting.io/changelog
- group: commercial
  href: https://artifacts.apis.io/siftingio/plans/siftingio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/siftingio-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/siftingio/rate-limits/siftingio-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/siftingio-rate-limits.yml
- group: start
  href: https://artifacts.apis.io/siftingio/sandbox/siftingio-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/siftingio-sandbox.yml
- group: design
  href: https://artifacts.apis.io/siftingio/components/siftingio-components.yml
  title: ''
  type: Components
  url: components/siftingio-components.yml
- group: other
  href: https://artifacts.apis.io/siftingio/overlays/siftingio-commodities-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/siftingio-commodities-overlay.yaml
- group: other
  href: https://artifacts.apis.io/siftingio/overlays/siftingio-convert-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/siftingio-convert-overlay.yaml
- group: other
  href: https://artifacts.apis.io/siftingio/overlays/siftingio-crypto-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/siftingio-crypto-overlay.yaml
- group: other
  href: https://artifacts.apis.io/siftingio/overlays/siftingio-dex-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/siftingio-dex-overlay.yaml
- group: other
  href: https://artifacts.apis.io/siftingio/overlays/siftingio-economiccalendar-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/siftingio-economiccalendar-overlay.yaml
- group: other
  href: https://artifacts.apis.io/siftingio/overlays/siftingio-filers-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/siftingio-filers-overlay.yaml
- group: other
  href: https://artifacts.apis.io/siftingio/overlays/siftingio-forex-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/siftingio-forex-overlay.yaml
- group: other
  href: https://artifacts.apis.io/siftingio/overlays/siftingio-live-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/siftingio-live-overlay.yaml
- group: other
  href: https://artifacts.apis.io/siftingio/overlays/siftingio-markets-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/siftingio-markets-overlay.yaml
- group: other
  href: https://artifacts.apis.io/siftingio/overlays/siftingio-signals-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/siftingio-signals-overlay.yaml
- group: other
  href: https://artifacts.apis.io/siftingio/overlays/siftingio-stocks-overlay.yaml
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
finops:
- has_sources: true
  method: derived
  name: Siftingio Finops
  primary_unit: market
  service_category: ''
  slug: siftingio-finops
  template: false
image: https://sifting.io/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: SiftingIO MCP Server
  slug: mcp
- description: 'SiftingIO market data: live crypto/forex/metals prices, OHLCV bars, SEC fundamentals, 13F data. Returns the same normalized shapes as the REST API, with structuredContent alongside the text on the sna'
  name: SiftingIO MCP Server
  slug: io-sifting-mcp
modified: '2026-10-06'
name: SiftingIO
nav: Providers
network: true
overview: 'SiftingIO publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Live Stream, Commodities API, Convert API, and 10 more. Tagged areas include Financial market data, Stocks/equities, Foreign Exchange, Cryptocurrency, and DeFi/on-chain.


  The SiftingIO catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  SiftingIO''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, support, and 46 more developer resources.'
plans:
- name: Siftingio Plans Pricing
  plan_count: 12
  slug: siftingio-plans-pricing
- name: Siftingio Price Estimates
  plan_count: 0
  slug: siftingio-price-estimates
random_paper: 12
rate_limits:
- limit_count: 9
  name: Siftingio Rate Limits
  slug: siftingio-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: SiftingIO API Rules
  rule_count: 63
  severity_counts:
    error: 56
    hint: 0
    info: 1
    warn: 6
  slug: siftingio-rules
score:
  band: strong
  composite: 65.5
  coverage:
    artifact_dirs: 30
    catalog_earned: 63.5
    catalog_earned_first_party: 24.0
    catalog_gap: 51.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 59.0
    developer_ergonomics: 83.3
    discoverability: 63.3
    operational_transparency: 57.9
  previous_composite: 64.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 11
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/siftingio/siftingio-2026-09-02T155422.png
security:
- kind: authentication
  name: Siftingio Authentication
  slug: siftingio-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Siftingio Domain Security
  slug: siftingio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: Research a US company's fundamentals from SEC filings
  slug: siftingio-company-fundamentals-research
- name: Pull live prices and historical OHLCV bars across asset classes
  slug: siftingio-cross-asset-prices-and-bars
- name: Check whether a market is open and read its calendar
  slug: siftingio-market-hours-and-calendars
- name: Read technical signals and on-chain positions
  slug: siftingio-technical-signals-and-onchain
slug: siftingio
tags:
- Financial market data
- Stocks/equities
- Foreign Exchange
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
- Agent-Native
website: https://sifting.io
---

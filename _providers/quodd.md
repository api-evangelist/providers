---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Quodd Agentic Access
  operation_count: 8
  slug: quodd-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 10
apis:
- description: Single-ticker real-time or delayed pricing snapshot (Snap). Returns the current quote and trade fields - last price, bid/ask, volume, and related market data - for one instrument across QUODD's global
  name: QUODD Snap API
  slug: quodd-snap-api
- description: Batch snapshot retrieval for many tickers in a single request, via GET (query list) or POST (ticker array). Returns real-time or delayed pricing for each requested instrument. Documented in QUODD's RE
  name: QUODD Batch Snaps API
  slug: quodd-batch-snaps-api
- description: Real-time or delayed options pricing snapshots for single contracts (Options Snap) and for many contracts at once (Batch Options Snaps, GET and POST). Documented in the QUODD REST API reference.
  name: QUODD Options Snaps API
  slug: quodd-options-snaps-api
- description: Token generation for trial and firm users. Exchanges username and password credentials for an access token that is appended to REST requests as the _token query parameter. Tokens expire after 24 hours
  name: QUODD Authentication Token API
  slug: quodd-authentication-token-api
- description: Ticker and symbol lookup for discovering securities across asset classes and identifiers (Cloud Search). Listed as Beta Access on the QUODD Developer Platform; endpoint paths are modeled.
  name: QUODD Ticker Search API
  slug: quodd-ticker-search-api
- description: End-of-day and historical market data across 80-plus global exchanges - US equities and ETFs from 1994, global markets from 2000 - as OHLCV time series or point-in-time snapshots, with adjusted and un
  name: QUODD Historical Prices API
  slug: quodd-historical-prices-api
- description: Global reference data and security master (Global Master) - intra-day global equity descriptive data, funds, corporate actions, dividends, and fixed income terms and conditions. Described in QUODD pro
  name: QUODD Reference Data & Security Master API
  slug: quodd-reference-data-security-master-api
- description: Company fundamentals, metrics, ratios, and analyst estimates on global securities for fundamental analysis. Described in QUODD product documentation; concrete endpoints are modeled, not published.
  name: QUODD Fundamentals & Estimates API
  slug: quodd-fundamentals-estimates-api
- description: gRPC delivery of pricing snapshots (Snap) and ticker information (Ticker Info) for high-performance, low-overhead integrations. Documented on the QUODD Developer Platform alongside the REST API.
  name: QUODD Snap gRPC API
  slug: quodd-snap-grpc-api
- description: Cloud Streaming pushes changing quote and trade fields continuously rather than requiring repeated REST polling, for live market data in servers, web, and mobile apps. QUODD's own developer platform d
  name: QUODD Cloud Streaming API
  slug: quodd-cloud-streaming-api
artifact_total: 17
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quodd-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/quodd-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/quodd-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quodd-financial-information-services
- group: company
  title: ''
  type: Website
  url: https://www.quodd.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.quodd.com
- group: commercial
  title: ''
  type: Plans
  url: plans/quodd-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/quodd-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/quodd-finops.yml
- group: build
  title: ''
  type: Packages
  url: packages/quodd-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/quodd-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/quodd-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/quodd-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/quodd-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/quodd-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/quodd-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/quodd-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.quodd.com
- group: operate
  title: ''
  type: Support
  url: https://www.quodd.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.quodd.com/insights
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.quodd.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.quodd.com/privacy-policy
created: '2026-07-11'
description: QUODD is a cloud-native market data provider delivering real-time, delayed, historical, end-of-day, and point-in-time pricing, plus reference data, a security master, fundamentals, estimates, corporate actions, ESG, and news across global equities, ETFs, options, fixed income, FX, funds, and indices. The QUODD Developer Platform (developer.quodd.com) exposes market data through REST and gRPC snapshot APIs, token-based authentication, and cloud delivery options - Cloud APIs, Cloud Streaming, Cloud Alerts, Cloud Search, and Cloud Files. QUODD advertises more than 250 billion data points across 150-plus global exchanges. Developer documentation is public, but production access is gated behind trial or firm credentials and enterprise contact-sales agreements; exact REST base URLs and full endpoint paths are not published openly.
finops:
- name: Quodd Finops
  service_category: Market Data and Financial Information
  slug: quodd-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quodd.png
layout: provider
mcp_servers:
- description: ''
  name: quodd-mcp.yml
  slug: quodd-mcpyml
modified: '2026-07-22'
name: QUODD
nav: Providers
network: true
overview: 'QUODD publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Snap API, Batch Snaps API, Options Snaps API, and 1 more. Tagged areas include Market Data, Real-Time Data, Financial Data, Streaming, and Historical Data.


  QUODD''s developer surface includes authentication, documentation, support, engineering blog, and 19 more developer resources.'
plans:
- name: Quodd Plans Pricing
  plan_count: 2
  slug: quodd-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Quodd Rate Limits
  slug: quodd-rate-limits
score:
  band: developing
  composite: 48.1
  delta: -1.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 60.2
    developer_ergonomics: 38.6
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 31.6
  previous_composite: 49.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quodd/refs/heads/main/screenshots/quodd-2026-07-22T202600.png
security:
- kind: authentication
  name: Quodd Authentication
  slug: quodd-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Quodd Domain Security
  slug: quodd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: quodd
tags:
- Market Data
- Real-Time Data
- Financial Data
- Streaming
- Historical Data
- Reference Data
- Quotes
- Fintech
website: https://www.quodd.com
---

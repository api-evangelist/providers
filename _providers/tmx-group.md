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
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.0
  scored_at: '2026-08-24'
api_count: 11
apis:
- description: End-of-day equity analytics for Canadian and US markets - basic, daily, and advanced daily stats plus liquidity analytics and liquidity summaries - via POST endpoints such as /v1/ca/dailystats, /v1/us
  name: TMX Essential Analytics for Equities API
  slug: tmx-equity-analytics-api
- description: One-minute and one-second trade and quote bars for Canadian and US equities via /v1/ca/tradebar1min, /v1/ca/tradebar1sec, /v1/ca/quotesbar1min, /v1/ca/quotesbar1sec and US equivalents.
  name: TMX Equity Intraday Trades and Quotes API
  slug: tmx-equity-intraday-api
- description: Historical trade-and-quote tick data with national best bid and offer for Canadian and US listings via /v1/ca/taqnbbo and /v1/us/taqnbbo.
  name: TMX Trades and Quotes Tick Data (TAQ NBBO) API
  slug: tmx-taq-nbbo-api
- description: Broker-level trading activity for Canadian markets - broker daily stats, broker liquidity, and broker summaries - via /v1/ca/brokerdailystats, /v1/ca/brokerliquidity, and /v1/ca/brokersummary, with GE
  name: TMX Broker Analytics API
  slug: tmx-broker-analytics-api
- description: Issuer profiles, global symbol directories and deltas, and global corporate actions via /v1/ca/issuers, /v1/globalsymbols, and /v1/globalsymbolsdelta, with V2 additions covering TSX reference data (CR
  name: TMX Corporate Actions and Reference Data API
  slug: tmx-reference-data-api
- description: Montreal Exchange derivatives analytics - MX daily stats for options and futures via /v1/ca/mxdailystats, with instrument, order book, and trade datasets documented alongside.
  name: TMX Options and Futures Analytics API
  slug: tmx-options-futures-analytics-api
- description: Short interest analytics for Canadian listings including days to cover (/v1/daystocover) and percent of float (/v1/percentfloat).
  name: TMX Short Interest Analytics API
  slug: tmx-short-interest-api
- description: North American share buyback activity via /v1/northamericanbuybacks.
  name: TMX Buybacks API
  slug: tmx-buybacks-api
- description: Price adjustment curves for historical price series via /v1/pac, /v1/pacexplain, /v1/original, and /v1/smoothened.
  name: TMX Price Adjustment Curve API
  slug: tmx-price-adjustment-curve-api
- description: Market-on-close imbalance analytics for the Toronto Stock Exchange closing auction via /v1/ca/moci.
  name: TMX MOC Imbalance Analytics API
  slug: tmx-moc-imbalance-api
- description: 'Second-generation GET-based REST surface on insightapi.tmxanalytics.com/v2 covering broker analytics, issuers, global symbols, TSX reference data (CRV bulletins, entitlements, FITC, SMF), and S&P/TSX '
  name: TMX Data Science API V2 (Insight API)
  slug: tmx-insight-api-v2
artifact_total: 15
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tmx-group-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tmx-group-plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tmx-group-rate-limits.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tmx-group-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tmx-group-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tmx-group-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tmx-group-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.tmxanalytics.com/#api-versioning
- group: auth
  title: ''
  type: Authentication
  url: authentication/tmx-group-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tmx-group-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tmx-group-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/tmx-group-components.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tmxanalytics.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tmxanalytics.com/#steps-to-access-apis
- group: company
  title: ''
  type: Website
  url: https://www.tmx.com
- group: start
  title: ''
  type: Portal
  url: https://hub.tmxanalytics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tmxanalytics.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TMXGroup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tmx-group
- group: company
  title: ''
  type: Blog
  url: https://www.tmx.com/newsroom
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tmxinfoservices.com/market-data/pricing-and-contract-documents
- group: start
  title: ''
  type: SignUp
  url: https://hub.tmxanalytics.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tmx.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tmx.com/en/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://docs.tmxanalytics.com/#tmx-api-support
created: '2026-07-21'
description: TMX Group operates Canadian capital-markets infrastructure - Toronto Stock Exchange, TSX Venture Exchange, TSX Alpha, and the Montreal Exchange - and sells market data through its TMX Datalinx arm. Alongside sales-gated real-time broadcast feeds (TL1/TL2, QuantumFeed, MX Order Book Feed) it offers a self-serve TMX Analytics platform (hub.tmxanalytics.com) whose REST Data Science APIs deliver Canadian and US equity daily stats, intraday trade/quote bars, TAQ NBBO tick data, broker analytics, short interest, buybacks, corporate actions and reference data, and Montreal Exchange options and futures analytics, plus cloud/S3 flat-file and notebook delivery.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tmx-group.png
layout: provider
modified: '2026-07-22'
name: TMX Group
nav: Providers
network: true
overview: 'TMX Group publishes 11 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Financial, Market Data, Stocks, Exchange, and Derivatives.


  TMX Group''s developer surface includes authentication, API reference, getting-started guide, developer portal, documentation, engineering blog, pricing, and 18 more developer resources.'
plans:
- name: Tmx Group Plans
  plan_count: 10
  slug: tmx-group-plans
random_paper: 2
rate_limits:
- limit_count: 11
  name: Tmx Group Rate Limits
  slug: tmx-group-rate-limits
score:
  band: developing
  composite: 42.7
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 42.1
  previous_composite: 42.7
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 65.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tmx-group/refs/heads/main/screenshots/tmx-group-2026-07-22T202645.png
security:
- kind: authentication
  name: Tmx Group Authentication
  slug: tmx-group-authentication
  summary_line: apiKey/http-bearer · 2 schemes
- kind: domain-security
  name: Tmx Group Domain Security
  slug: tmx-group-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: tmx-group
tags:
- Financial
- Market Data
- Stocks
- Exchange
- Derivatives
- Analytics
- Reference Data
- Canada
website: https://www.tmx.com
---

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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-05'
api_count: 4
apis:
- description: Cloud-based request/response REST API delivering real-time and delayed Level 1/Level 2 quotes, trades, historical OHLCV and tick data, full option chains with Greeks, fundamentals, earnings, news from
  name: QuoteMedia OnDemand (QMOD) Data API
  slug: quotemedia-ondemand-api
- description: Enterprise tick-by-tick streaming feed for real-time or delayed Level 1 and Level 2 market data, normalized across exchanges and delivered through a WebSocket API plus Java and .NET client APIs. The c
  name: QuoteMedia Streaming Data Feed API
  slug: quotemedia-streaming-data-feed-api
- description: 'Bulk data delivery via SFTP flat files for systematic import of price data, financials, corporate actions, and fund data, alongside historical time-series downloads in CSV, XML, and JSON. Sales-gated '
  name: QuoteMedia File Services
  slug: quotemedia-file-services
- description: Self-service package for non-professional developers building personal applications, combining tick-by-tick streaming data with request APIs, developer kits with documentation and example code, 90 day
  name: Quotestream Connect for Developers
  slug: quotestream-connect-for-developers
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quotemedia-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/quotemedia-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/quotemedia-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/quotemedia-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/quotemedia-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/quotemedia-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/quotemedia-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/quotemedia-authentication.yml
- group: design
  title: ''
  type: Components
  url: components/quotemedia-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/quotemedia-conventions.yml
- group: company
  title: ''
  type: Website
  url: https://quotemedia.com/
- group: start
  title: ''
  type: Portal
  url: https://www.quotemedia.com/apifeeds
- group: docs
  title: ''
  type: Documentation
  url: https://quotemediasupport.freshdesk.com/support/home
- group: operate
  title: ''
  type: Support
  url: https://quotemediasupport.freshdesk.com/support/home
- group: operate
  title: ''
  type: StatusPage
  url: https://status.quotemedia.com
- group: company
  title: ''
  type: Blog
  url: https://quotemedia.com/company/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quotemedia
- group: commercial
  title: ''
  type: TermsOfService
  url: https://quotemedia.com/legal/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://quotemedia.com/legal/privacy-policy
created: '2026-07-21'
description: QuoteMedia, Inc. is an independent, publicly traded (OTC QMCI) financial market data and financial technology company headquartered in Fountain Hills, Arizona, founded in 1999. It licenses real-time, delayed, and historical market data - equities, options, futures, commodities, currencies, mutual funds, ETFs, and indices - plus fundamentals, news, SEC/SEDAR filings, corporate actions, earnings, fund research, and ESG data to brokerages, banks, media, and investor relations customers. Data is delivered through the QuoteMedia OnDemand (QMOD) cloud REST API in JSON, XML, and CSV, an enterprise tick-by-tick Streaming Data Feed with WebSocket, Java, and .NET APIs, and bulk file services over SFTP. Access is entitlement-managed via webmaster IDs provisioned through sales, with a Quotestream Connect self-service package for individual developers; detailed API reference documentation lives behind a login on the company's Freshdesk knowledge base.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quotemedia.png
layout: provider
modified: '2026-07-22'
name: QuoteMedia
nav: Providers
network: true
overview: 'QuoteMedia publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Financial, Market Data, Stocks, Options, and Real-Time.


  QuoteMedia''s developer surface includes authentication, developer portal, documentation, support, engineering blog, and 14 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 44.0
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 22.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 33.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quotemedia/refs/heads/main/screenshots/quotemedia-2026-07-22T202611.png
security:
- kind: authentication
  name: Quotemedia Authentication
  slug: quotemedia-authentication
  summary_line: entitlement-id/session-token/credentials · 3 schemes
- kind: domain-security
  name: Quotemedia Domain Security
  slug: quotemedia-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: quotemedia
tags:
- Financial
- Market Data
- Stocks
- Options
- Real-Time
- Streaming
- News
- Fundamentals
- Reference Data
website: https://quotemedia.com/
---

---
access_model:
  confidence: medium
  label: Self-serve subscription with free playground
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://developer.exchange-data.com/p/api-faq
  - https://developer.exchange-data.com/p/developers-and-startups
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 21.2
  scored_at: '2026-07-23'
api_count: 24
apis:
- description: Worldwide end-of-day equity pricing (open, high, low, close, bid, ask, last trade, volume) queried by MIC, LocalCode, or ISIN via the GetLatestEODPrices endpoint, returned as JSON or pipe-separated va
  name: EDI End of Day Pricing Data API
  slug: end-of-day-pricing-api
- description: Adjustment factors used to back-adjust end-of-day per-share price series for corporate actions so historical prices can be graphed consistently, via the GetLatestAdjustmentFactors endpoint.
  name: EDI Adjustment Factors Data API
  slug: adjustment-factors-api
- description: Equity analytics measures for worldwide listed securities via the GetLatestEquityAnalytics endpoint on EDI's shared REST base.
  name: EDI Worldwide Equity Analytics API
  slug: worldwide-equity-analytics-api
- description: Daily over-the-counter bond pricing, including independent zero-coupon and swap-implied yield curves for valuations, via the GetBondLatestPricing endpoint.
  name: EDI OTC Data API
  slug: otc-data-api
- description: Listed derivatives security master reference data via the GetOptionSecurityMaster endpoint, covering exchange-traded options contract specifications.
  name: EDI Derivatives Reference Data API
  slug: derivatives-reference-data-api
- description: End-of-day pricing for listed derivatives via the GetDerivativesPricing endpoint.
  name: EDI Derivatives End of Day Pricing API
  slug: derivatives-eod-pricing-api
- description: Worldwide equity corporate actions with 200+ output fields (security identifiers, issuer, event details, dates, payment information) queried by OperationalMic, LocalCode, ISIN, or event code via GetLa
  name: EDI Worldwide Corporate Actions API
  slug: worldwide-corporate-actions-api
- description: Exchange traded notes data via the GetLatestExchangeTradedNotes endpoint.
  name: EDI Exchange Traded Notes API
  slug: exchange-traded-notes-api
- description: Fixed income security master and corporate actions coverage for bonds via the GetBondSecurityMaster endpoint.
  name: EDI Worldwide Fixed Income Corporate Actions API
  slug: worldwide-fixed-income-corporate-actions-api
- description: Consolidated securities reference file (SRF) data for worldwide listed instruments via the GetConsolidatedSRF endpoint.
  name: EDI Securities Reference Data API
  slug: securities-reference-data-api
- description: Holiday observances and market timings for worldwide exchanges via the GetGlobalMarketHolidays endpoint; the service is divided into five products covering holidays and trading hours.
  name: EDI Global Market Holidays and Timings API
  slug: global-market-holidays-api
- description: Shares outstanding figures for worldwide listed equities via the GetLatestSharesOutstanding endpoint.
  name: EDI Worldwide Shares Outstanding API
  slug: worldwide-shares-outstanding-api
- description: Detailed exchange adjustment notices for listed derivatives in a standardized machine-readable format, queried by underlying MIC, ISIN, or symbol via GetLatestDerivActions.
  name: EDI DerivActions API
  slug: derivactions-api
- description: Global economic indicator releases via the GetLatestEconomicIndicator endpoint.
  name: EDI Global Economic Indicators API
  slug: global-economic-indicators-api
- description: Forward-looking economic calendar events via the GetLatestEconomicCalendar endpoint.
  name: EDI Economic Calendar API
  slug: economic-calendar-api
- description: Central bank meeting and announcement calendar via the GetLatestCentralBankCalendar endpoint.
  name: EDI Central Bank Calendar API
  slug: central-bank-calendar-api
- description: United States economic data series via the GetUsEconomicData endpoint (documented on the developer portal with an http:// scheme against the same api3 host).
  name: EDI US Economic Data API
  slug: us-economic-data-api
- description: Worldwide initial public offering data via the GetLatestInitialPublicOfferings endpoint.
  name: EDI Initial Public Offerings API
  slug: initial-public-offerings-api
- description: Corporate bond evaluations via the GetLatestCorporateEvaluations endpoint, documented in the catalogue as the Corporate Bonds Data Dictionary product.
  name: EDI Corporate Bonds Data API
  slug: corporate-bonds-evaluated-pricing-api
- description: Options analytics including Greeks via the GetLatestOptionsGreeks endpoint.
  name: EDI Option Analytics Service API
  slug: option-analytics-api
- description: Fund corporate actions coverage; the documented endpoint GetLatestSouthAfricanFundDistributions returns South African fund distribution events.
  name: EDI Worldwide Funds Corporate Actions API
  slug: worldwide-funds-corporate-actions-api
- description: Investment fund net asset values via the GetLatestNetAssetValue endpoint.
  name: EDI Net Asset Value API
  slug: net-asset-value-api
- description: Index constituent reference data via the GetReferenceNameForIndexConstituents endpoint.
  name: EDI Index Constitution API
  slug: index-constitution-api
- description: Foreign exchange rates via the GetLatestFXRates endpoint.
  name: EDI Foreign Exchange Rates API
  slug: foreign-exchange-rates-api
artifact_total: 26
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/exchange-data-international-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/exchange-data-international-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/exchange-data-international-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/exchange-data-international-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/exchange-data-international-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/exchange-data-international-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/exchange-data-international-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/exchange-data-international-llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://developer.exchange-data.com/api-documentation/
- group: company
  title: ''
  type: Website
  url: https://www.exchange-data.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.exchange-data.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.exchange-data.com/api-documentation/
- group: start
  title: ''
  type: SignUp
  url: https://developer.exchange-data.com/register
- group: company
  title: ''
  type: Blog
  url: https://www.exchange-data.com/insights-edi/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/exchange-data-international/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.exchange-data.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.exchange-data.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://developer.exchange-data.com/contact
created: '2026-07-21'
description: 'Exchange Data International (EDI) is an independent, privately held financial data vendor founded in 1994 by Jonathan Bloch and headquartered in London, with operations in the USA, India, and Morocco serving 450+ institutional clients. EDI sells securities reference data, worldwide equity and fixed income corporate actions, end-of-day pricing, adjustment factors, shares outstanding, derivatives reference and pricing, economic indicators and calendars, fund NAVs, and FX rates. Data is delivered as SFTP flat-file feeds and through a self-serve REST API: the EDI Developer portal (developer.exchange-data.com) documents 24 API products on a shared base at api3.exchange-data.com, with account registration, an API Playground, per-product subscriptions, and JSON or pipe-separated responses. No public OpenAPI or AsyncAPI specification is published.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/exchange-data-international.png
layout: provider
modified: '2026-07-22'
name: Exchange Data International
nav: Providers
network: true
overview: 'Exchange Data International publishes 24 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Financial, Market Data, Corporate Actions, Reference Data, and End of Day Pricing.


  Exchange Data International''s developer surface includes authentication, sandbox, API reference, developer portal, documentation, signup flow, engineering blog, and 11 more developer resources.'
random_paper: 32
score:
  band: thin
  composite: 30.6
  delta: 4.2
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 47.8
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 26.4
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 54.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/exchange-data-international/refs/heads/main/screenshots/exchange-data-international-2026-07-22T202401.png
security:
- kind: authentication
  name: Exchange Data International Authentication
  slug: exchange-data-international-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Exchange Data International Domain Security
  slug: exchange-data-international-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: exchange-data-international
tags:
- Financial
- Market Data
- Corporate Actions
- Reference Data
- End of Day Pricing
- Fixed Income
- Derivatives
- Economic Data
- Stocks
- Exchange
website: https://www.exchange-data.com/
---

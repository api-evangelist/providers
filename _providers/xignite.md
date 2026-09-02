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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Xignite Agentic Access
  operation_count: 354
  slug: xignite-agentic-access
  summary_line: 354 operations
api_count: 22
apis:
- description: Delayed stock quotes for equities across global exchanges, served as REST operations (GetGlobalDelayedQuote, symbol changes, chart bars) in JSON, XML, or CSV from the globalquotes.xignite.com service.
  name: Xignite Global Quotes API
  slug: xignite-global-quotes-api
- description: Real-time stock quote data for global equities via REST request/response operations on the globalrealtime.xignite.com service.
  name: Xignite Global Real-Time API
  slug: xignite-global-real-time-api
- description: End-of-day and historical equity prices including historical quote ranges, chart bars, adjustment factors, and cash dividend history from the globalhistorical.xignite.com service.
  name: Xignite Global Historical API
  slug: xignite-global-historical-api
- description: Real-time, historical, and average foreign exchange rates - one of Xignite's longest-running and most widely used APIs - served from the globalcurrencies.xignite.com service.
  name: Xignite Global Currencies API
  slug: xignite-global-currencies-api
- description: Spot prices, bars, and historical rates for precious metals such as gold, silver, platinum, and palladium from the globalmetals.xignite.com service.
  name: Xignite Global Metals API
  slug: xignite-global-metals-api
- description: Cryptocurrency market data including quotes, chart bars, and historical prices for digital assets from the crypto.xignite.com service.
  name: Xignite Crypto API
  slug: xignite-crypto-api
- description: Stock market index and benchmark values with chart bars and index metadata from the globalindices.xignite.com service.
  name: Xignite Global Indices API
  slug: xignite-global-indices-api
- description: Option price data including quotes and chains for listed equity options from the globaloptions.xignite.com service.
  name: Xignite Global Options API
  slug: xignite-global-options-api
- description: Futures contract prices and metadata across commodity, index, and financial futures from the globalfutures.xignite.com service.
  name: Xignite Global Futures API
  slug: xignite-global-futures-api
- description: Bond price data for fixed income securities from the bonds.xignite.com service.
  name: Xignite Bonds API
  slug: xignite-bonds-api
- description: Money market, treasury, swap, and interbank rate data from the moneymarkets.xignite.com service.
  name: Xignite Money Markets API
  slug: xignite-money-markets-api
- description: Global security master and reference data - symbology, listings, identifiers, and instrument metadata - from the globalmaster.xignite.com service.
  name: Xignite Global Master API
  slug: xignite-global-master-api
- description: Corporate action events such as dividends, splits, mergers, and symbol changes from the globalcorporateactions.xignite.com service.
  name: Xignite Global Corporate Actions API
  slug: xignite-global-corporate-actions-api
- description: Company financial news headlines, market summaries, and press release data from the globalnews.xignite.com service.
  name: Xignite Global News API
  slug: xignite-global-news-api
- description: Company earnings announcement dates and earnings calendar data from the earningscalendar.xignite.com service.
  name: Xignite Earnings Calendar API
  slug: xignite-earnings-calendar-api
- description: Mutual fund net asset values (NAVs), adjustment factors, and fund pricing history from the navs.xignite.com service.
  name: Xignite NAVs API
  slug: xignite-navs-api
- description: Fund fundamental data - holdings, performance, and profile details for mutual funds and ETFs - from the globalfundfundamentals.xignite.com service.
  name: Xignite Global Fund Fundamentals API
  slug: xignite-global-fund-fundamentals-api
- description: Company fundamentals and financial statement data sourced from FactSet, served from the factsetfundamentals.xignite.com service.
  name: Xignite FactSet Fundamentals API
  slug: xignite-factset-fundamentals-api
- description: Environmental, social, and governance (ESG) data for companies from the globalesg.xignite.com service.
  name: Xignite Global ESG API
  slug: xignite-global-esg-api
- description: Exchange trading hours, market holidays, and calendar data for global exchanges from the globalholidays.xignite.com service.
  name: Xignite Global Holidays API
  slug: xignite-global-holidays-api
- description: Market event alerting - create and manage alerts on market data conditions - from the alerts.xignite.com service.
  name: Xignite CloudAlerts API
  slug: xignite-cloud-alerts-api
- description: Streaming product for pushing real-time quotes directly to applications. The product page is live but transport details (protocol, endpoints) are only documented behind registration; no public spec wa
  name: Xignite CloudStreaming API
  slug: xignite-cloud-streaming-api
- description: Bulk file delivery service behind Xignite's file products (historical equity prices, bonds, options, currencies, and corporate actions files), served from the cloudfiles.xignite.com service.
  name: Xignite CloudFiles API
  slug: xignite-cloud-files-api
artifact_total: 50
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: XigniteBonds CloudAlerts API
  slug: open-xignite-cloudalerts-api
- collection_type: open
  name: CloudAlerts XigniteBonds API
  slug: open-xignite-xignitebonds-api
- collection_type: open
  name: XigniteBonds CloudAlerts XigniteCloudFiles API
  slug: open-xignite-xignitecloudfiles-api
- collection_type: open
  name: XigniteBonds CloudAlerts XigniteCrypto API
  slug: open-xignite-xignitecrypto-api
- collection_type: open
  name: XigniteBonds CloudAlerts XigniteEarningsCalendar API
  slug: open-xignite-xigniteearningscalendar-api
- collection_type: open
  name: XigniteBonds CloudAlerts XigniteFactSetFundamentals API
  slug: open-xignite-xignitefactsetfundamentals-api
- collection_type: open
  name: XigniteBonds CloudAlerts XigniteGlobalCorporateActions API
  slug: open-xignite-xigniteglobalcorporateactions-api
- collection_type: open
  name: XigniteBonds CloudAlerts XigniteGlobalCurrencies API
  slug: open-xignite-xigniteglobalcurrencies-api
- collection_type: open
  name: XigniteBonds CloudAlerts XigniteGlobalESG API
  slug: open-xignite-xigniteglobalesg-api
- collection_type: open
  name: XigniteBonds CloudAlerts XigniteGlobalFundFundamentals API
  slug: open-xignite-xigniteglobalfundfundamentals-api
- collection_type: open
  name: XigniteBonds CloudAlerts XigniteGlobalFutures API
  slug: open-xignite-xigniteglobalfutures-api
- collection_type: open
  name: XigniteBonds CloudAlerts XigniteGlobalHistorical API
  slug: open-xignite-xigniteglobalhistorical-api
- collection_type: open
  name: XigniteBonds CloudAlerts XigniteGlobalHolidays API
  slug: open-xignite-xigniteglobalholidays-api
- collection_type: open
  name: XigniteBonds CloudAlerts XigniteGlobalIndices API
  slug: open-xignite-xigniteglobalindices-api
- collection_type: open
  name: XigniteBonds CloudAlerts XigniteGlobalMaster API
  slug: open-xignite-xigniteglobalmaster-api
- collection_type: open
  name: XigniteBonds CloudAlerts XigniteGlobalMetals API
  slug: open-xignite-xigniteglobalmetals-api
- collection_type: open
  name: XigniteBonds CloudAlerts XigniteGlobalNews API
  slug: open-xignite-xigniteglobalnews-api
- collection_type: open
  name: XigniteBonds CloudAlerts XigniteGlobalOptions API
  slug: open-xignite-xigniteglobaloptions-api
- collection_type: open
  name: XigniteBonds CloudAlerts XigniteGlobalQuotes API
  slug: open-xignite-xigniteglobalquotes-api
- collection_type: open
  name: XigniteBonds CloudAlerts XigniteGlobalRealTime API
  slug: open-xignite-xigniteglobalrealtime-api
- collection_type: open
  name: XigniteBonds CloudAlerts XigniteMoneyMarkets API
  slug: open-xignite-xignitemoneymarkets-api
- collection_type: open
  name: XigniteBonds CloudAlerts XigniteNAVs API
  slug: open-xignite-xignitenavs-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xignite-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/xignite-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/xignite-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.quodd.com/
- group: start
  title: ''
  type: Portal
  url: https://www.xignite.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://developer.quodd.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Xignite
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quodd
- group: company
  title: ''
  type: Blog
  url: https://quodd.com/insights
- group: start
  title: ''
  type: SignUp
  url: https://www.xignite.com/xignite-trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://quodd.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://quodd.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://quodd.com/support
- group: docs
  title: ''
  type: APIReference
  url: https://www.xignite.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://www.xignite.com/Support/GettingStarted.aspx
- group: build
  title: ''
  type: Packages
  url: packages/xignite-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/xignite-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/xignite-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/xignite-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/xignite-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/xignite-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/xignite-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/xignite-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/xignite-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/xignite-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-21'
description: Xignite pioneered cloud-based financial market data APIs, offering a catalog of 40+ REST web services covering equities, forex, crypto, indices, options, futures, fixed income, mutual funds, corporate actions, news, ESG, and reference data. Each API lives on its own subdomain (for example globalquotes.xignite.com) and returns JSON, XML, or CSV, with bulk datasets delivered as files via CloudFiles and streaming quotes via its CloudStreaming product. Founded in 2000, Xignite was acquired by QUODD (a NewSpring Holdings company) in February 2023; the xignite.com developer catalog remains live while corporate pages redirect to quodd.com, and QUODD runs a newer developer platform at developer.quodd.com.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/xignite.png
layout: provider
mcp_servers:
- description: ''
  name: Xignite MCP Server
  slug: xignite-mcp-server
modified: '2026-07-22'
name: Xignite
nav: Providers
network: true
overview: 'Xignite publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Global Quotes API, Global Real-Time API, Global Historical API, and 19 more. Tagged areas include Financial, Market Data, Stocks, Real-Time, and Forex.


  Xignite''s developer surface includes authentication, developer portal, documentation, engineering blog, signup flow, support, API reference, and 19 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 19
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 39.3
    developer_ergonomics: 66.1
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/xignite/refs/heads/main/screenshots/xignite-2026-07-22T202705.png
security:
- kind: authentication
  name: Xignite Authentication
  slug: xignite-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Xignite Domain Security
  slug: xignite-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: xignite
tags:
- Financial
- Market Data
- Stocks
- Real-Time
- Forex
- Cryptocurrency
- Options
- Futures
- Fixed Income
- Reference Data
- Corporate Actions
- Mutual Funds
- ESG
- News
website: https://www.quodd.com/
---

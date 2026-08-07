---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.3
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Barchart Agentic Access
  operation_count: 95
  slug: barchart-agentic-access
  summary_line: 95 operations
api_count: 12
apis:
- description: Grain bids, commodity statistics, fuel, and crop data.
  name: Barchart Commodities & Agriculture API
  slug: barchart-commodities-agriculture-api
- description: Splits, dividends, earnings, and calendars.
  name: Barchart Corporate Actions & Earnings API
  slug: barchart-corporate-actions-earnings-api
- description: Spot crypto quotes and history.
  name: Barchart Cryptocurrency API
  slug: barchart-cryptocurrency-api
- description: Company profiles and financial statements.
  name: Barchart Fundamentals API
  slug: barchart-fundamentals-api
- description: Futures and options market data and analytics.
  name: Barchart Futures & Options API
  slug: barchart-futures-options-api
- description: Historical tick, minute, and end-of-day time series.
  name: Barchart History API
  slug: barchart-history-api
- description: Financial news and SEC filings.
  name: Barchart News & Filings API
  slug: barchart-news-filings-api
- description: Real-time, delayed, and end-of-day price quotes.
  name: Barchart Quotes API
  slug: barchart-quotes-api
- description: Instrument metadata and bulk equities by exchange.
  name: Barchart Reference & Equities API
  slug: barchart-reference-equities-api
- description: Technical studies, signals, and chart images.
  name: Barchart Technicals & Charts API
  slug: barchart-technicals-charts-api
- description: Current conditions and forecasts.
  name: Barchart Weather API
  slug: barchart-weather-api
- description: Barchart OnDemand APIs from Barchart — 71 path(s) described in OpenAPI.
  name: Barchart OnDemand APIs
  slug: barchart-ondemand-official-openapi
artifact_total: 31
collections:
- collection_type: postman
  name: Barchart OnDemand Commodities & Agriculture API
  slug: postman-barchart-commodities-agriculture-api
- collection_type: postman
  name: Barchart OnDemand Commodities & Agriculture Corporate Actions & Earnings API
  slug: postman-barchart-corporate-actions-earnings-api
- collection_type: postman
  name: Barchart OnDemand Commodities & Agriculture Cryptocurrency API
  slug: postman-barchart-cryptocurrency-api
- collection_type: postman
  name: Barchart OnDemand Commodities & Agriculture Fundamentals API
  slug: postman-barchart-fundamentals-api
- collection_type: postman
  name: Barchart OnDemand Commodities & Agriculture Futures & Options API
  slug: postman-barchart-futures-options-api
- collection_type: postman
  name: Barchart OnDemand Commodities & Agriculture History API
  slug: postman-barchart-history-api
- collection_type: postman
  name: Barchart OnDemand Commodities & Agriculture News & Filings API
  slug: postman-barchart-news-filings-api
- collection_type: postman
  name: Barchart OnDemand Commodities & Agriculture Quotes API
  slug: postman-barchart-quotes-api
- collection_type: postman
  name: Barchart OnDemand Commodities & Agriculture Reference & Equities API
  slug: postman-barchart-reference-equities-api
- collection_type: postman
  name: Barchart OnDemand Commodities & Agriculture Technicals & Charts API
  slug: postman-barchart-technicals-charts-api
- collection_type: postman
  name: Barchart OnDemand Commodities & Agriculture Weather API
  slug: postman-barchart-weather-api
- collection_type: open
  name: Barchart OnDemand API
  slug: open-barchart
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/barchart/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/barchart-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/barchart-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/barchart-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/barchart-com
- group: company
  title: ''
  type: Website
  url: https://www.barchart.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.barchart.com/ondemand/api
- group: start
  title: ''
  type: SignUp
  url: https://www.barchart.com/solutions/services/ondemand
- group: commercial
  title: ''
  type: Plans
  url: plans/barchart-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/barchart-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/barchart-finops.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/barchart-ondemand-official-openapi.yml
- group: build
  title: ''
  type: Packages
  url: packages/barchart-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/barchart-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/barchart-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/barchart-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/barchart-ondemand-official-overlay.yaml
- group: other
  title: ''
  type: Protobuf
  url: grpc/barchart-openfeed.proto
- group: design
  title: ''
  type: Conformance
  url: conformance/barchart-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/barchart-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/barchart-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.barchart.com
- group: design
  title: ''
  type: Conventions
  url: conventions/barchart-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/barchart-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/barchart-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/barchart-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/barchart
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.barchart.com/ondemand
- group: start
  title: ''
  type: GettingStarted
  url: https://www.barchart.com/ondemand/free-market-data-api
- group: operate
  title: ''
  type: Support
  url: https://help.barchart.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.barchart.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.barchart.com/terms#privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.barchart.com/solutions/services/ondemand
- group: company
  title: ''
  type: Blog
  url: https://www.barchart.com/news
created: '2026-07-11'
description: Barchart is a leading provider of market data and commodity data, delivering real-time, delayed, and historical financial and reference data across equities, futures, options, forex, cryptocurrencies, ETFs, mutual funds, indexes, and physical commodities. The Barchart OnDemand API is a commercially licensed REST/JSON (also XML and CSV) service hosted at ondemand.websol.barchart.com, authenticated with an apikey and packaged into subscription and enterprise plans. It exposes a broad documented endpoint catalog - getQuote, getHistory, getEquitiesByExchange, getFuturesOptions, getProfile, getCrypto, getGrainBids, getNews, and dozens more - covering quotes, historical time series, fundamentals, corporate actions, options analytics, agricultural and energy commodity data, technicals, and news.
finops:
- name: Barchart Finops
  service_category: Market Data and Financial Data
  slug: barchart-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/barchart.png
layout: provider
mcp_servers:
- description: ''
  name: barchart-mcp.yml
  slug: barchart-mcpyml
modified: '2026-07-22'
name: Barchart
nav: Providers
network: true
overview: 'Barchart publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Commodities & Agriculture API, Corporate Actions & Earnings API, Cryptocurrency API, and 9 more. Tagged areas include Market Data, Financial Data, Commodities, Futures, and Options.


  Barchart''s developer surface includes authentication, documentation, signup flow, getting-started guide, support, pricing, engineering blog, and 28 more developer resources.'
plans:
- name: Barchart Plans Pricing
  plan_count: 3
  slug: barchart-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 4
  name: Barchart Rate Limits
  slug: barchart-rate-limits
score:
  band: strong
  composite: 60.4
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 62.4
    developer_ergonomics: 60.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 52.6
  previous_composite: 60.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Barchart Authentication
  slug: barchart-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Barchart Domain Security
  slug: barchart-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: barchart
tags:
- Market Data
- Financial Data
- Commodities
- Futures
- Options
- Reference Data
- Equities
- Historical Data
- Cryptocurrency
- Agriculture
website: https://www.barchart.com
---

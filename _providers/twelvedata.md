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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 55.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Twelvedata Agentic Access
  operation_count: 26
  slug: twelvedata-agentic-access
  summary_line: 26 operations
api_count: 6
apis:
- description: 'Real-time price streaming over a persistent, bidirectional WebSocket at wss://ws.twelvedata.com/v1/quotes/price. Clients authenticate with an apikey query parameter, send JSON subscribe / unsubscribe '
  name: Twelve Data WebSocket Streaming API
  slug: twelvedata-websocket-streaming-api
- description: Real-time quotes, latest prices, and end-of-day data.
  name: Twelve Data Core Data API
  slug: twelvedata-core-data-api
- description: Company profiles, statements, dividends, earnings, and analysis.
  name: Twelve Data Fundamentals API
  slug: twelvedata-fundamentals-api
- description: Catalogs of instruments, exchanges, and supporting metadata.
  name: Twelve Data Reference Data API
  slug: twelvedata-reference-data-api
- description: 100+ technical analysis indicators computed over time series.
  name: Twelve Data Technical Indicators API
  slug: twelvedata-technical-indicators-api
- description: Historical and real-time OHLCV time series.
  name: Twelve Data Time Series API
  slug: twelvedata-time-series-api
artifact_total: 23
asyncapis:
- description: AsyncAPI 2.6 description of Twelve Data's **real-time price WebSocket**. Unlike a one-way HTTP Server-Sent Events stream, this is a genuine, bidirectional WebSocket (`wss://`) surface. The client open
  name: Twelve Data Real-Time Price WebSocket
  slug: twelvedata-asyncapi
collections:
- collection_type: postman
  name: Twelve Data REST Core Data API
  slug: postman-twelvedata-core-data-api
- collection_type: postman
  name: Twelve Data REST Core Data Fundamentals API
  slug: postman-twelvedata-fundamentals-api
- collection_type: postman
  name: Twelve Data API
  slug: postman-twelvedata-openapi-original
- collection_type: postman
  name: Twelve Data REST Core Data Reference Data API
  slug: postman-twelvedata-reference-data-api
- collection_type: postman
  name: Twelve Data REST Core Data Technical Indicators API
  slug: postman-twelvedata-technical-indicators-api
- collection_type: postman
  name: Twelve Data REST Core Data Time Series API
  slug: postman-twelvedata-time-series-api
- collection_type: open
  name: Twelve Data REST API
  slug: open-twelvedata
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/twelve-data/overview
- group: auth
  title: ''
  type: TrustCenter
  url: security/twelvedata-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/twelvedata-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/twelvedata-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/twelvedata-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/twelve-data
- group: company
  title: ''
  type: Website
  url: https://twelvedata.com
- group: docs
  title: ''
  type: Documentation
  url: https://twelvedata.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/twelvedata-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/twelvedata-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/twelvedata-finops.yml
- group: operate
  title: ''
  type: Support
  url: https://support.twelvedata.com
- group: company
  title: ''
  type: Blog
  url: https://twelvedata.com/blog
- group: build
  title: ''
  type: Packages
  url: packages/twelvedata-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/twelvedata-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/twelvedata-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/twelvedata-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/twelvedata-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/twelvedata-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/twelvedata-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/twelvedata-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.twelvedata.com/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/twelvedata-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/twelvedata-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://twelvedata.isitup.cloud
- group: operate
  title: ''
  type: Roadmap
  url: https://roadmap.twelvedata.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/twelvedata-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/twelvedata-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/twelvedata-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/twelvedata-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/twelvedata-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://twelvedata.com/account
- group: docs
  title: ''
  type: APIReference
  url: https://twelvedata.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://twelvedata.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://twelvedata.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://twelvedata.com/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://twelvedata.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://twelvedata.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/twelvedata
created: '2026-07-11'
description: Twelve Data is a financial market data provider offering real-time and historical data for stocks, forex, cryptocurrencies, ETFs, indices, commodities, and funds through a single REST API and a real-time WebSocket. Coverage spans time series (OHLCV), quotes and prices, 100-plus technical indicators, reference and catalog data, and company fundamentals. Every request is authenticated with an apikey and metered as API credits; a free Basic plan grants 800 API credits per day. Real-time price streaming is delivered over a WebSocket at wss://ws.twelvedata.com/v1/quotes/price.
finops:
- name: Twelvedata Finops
  service_category: Financial Market Data
  slug: twelvedata-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/twelvedata.png
layout: provider
mcp_servers:
- description: ''
  name: twelvedata-mcp.yml
  slug: twelvedata-mcpyml
modified: '2026-07-22'
name: Twelve Data
nav: Providers
network: true
overview: 'Twelve Data publishes 6 APIs on the [APIs.io](https://apis.io/) network, including WebSocket Streaming API, Core Data API, Fundamentals API, and 3 more. Tagged areas include Market Data, Financial Data, Stocks, Forex, and Crypto.


  The Twelve Data catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Twelve Data''s developer surface includes authentication, documentation, support, engineering blog, CLI, changelog, sandbox, and 33 more developer resources.'
plans:
- name: Twelvedata Plans Pricing
  plan_count: 5
  slug: twelvedata-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Twelvedata Rate Limits
  slug: twelvedata-rate-limits
rules:
- name: Twelve Data API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: twelvedata-asyncapi-spectral-rules
score:
  band: exemplar
  composite: 75.6
  delta: -1.7
  facets:
    commercial_clarity: 100.0
    contract_quality: 63.3
    developer_ergonomics: 86.4
    discoverability: 92.6
    governance: 53.1
    operational_transparency: 73.7
  previous_composite: 77.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 83.3
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 60.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/twelvedata/refs/heads/main/screenshots/twelvedata-2026-07-22T202655.png
security:
- kind: authentication
  name: Twelvedata Authentication
  slug: twelvedata-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Twelvedata Domain Security
  slug: twelvedata-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Twelvedata Trust Center
  slug: twelvedata-trust-center
  summary_line: SOC 2, GDPR
slug: twelvedata
tags:
- Market Data
- Financial Data
- Stocks
- Forex
- Crypto
- Real-Time Data
- Technical Indicators
- Fundamentals
website: https://twelvedata.com
---

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
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 56.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Alpha Vantage Agentic Access
  operation_count: 1
  slug: alpha-vantage-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Intraday, daily, weekly, and monthly stock price and volume data
  name: Alpha Vantage Stock Time Series API
  slug: alpha-vantage-stock-time-series-api
artifact_total: 39
collections:
- collection_type: postman
  name: Alpha Vantage API
  slug: postman-alpha-vantage-plugin-openapi
- collection_type: postman
  name: Alpha Vantage Stock Time Series API
  slug: postman-alpha-vantage-stock-time-series-api
- collection_type: open
  name: Alpha Vantage API
  slug: open-alpha-vantage
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/alpha-vantage/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/alpha-vantage-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alpha-vantage-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/alpha-vantage-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/alpha-vantage-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/alpha-vantage-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/alpha-vantage-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/alpha-vantage-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alpha-vantage-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/alpha-vantage-stock-time-series-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/alpha-vantage-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/alpha-vantage-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alpha-vantage-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/alpha-vantage-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/alpha-vantage-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/alpha-vantage-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/alpha-vantage-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/alpha-vantage-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/alpha-vantage-vocabulary.yaml
- group: build
  title: ''
  type: Postman
  url: collections/alpha-vantage.postman_collection.json
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alpha-vantage-inc
- group: start
  title: ''
  type: Portal
  url: https://www.alphavantage.co/
- group: docs
  title: ''
  type: Documentation
  url: https://www.alphavantage.co/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://www.alphavantage.co/documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.alphavantage.co/support/
- group: operate
  title: ''
  type: Support
  url: https://www.alphavantage.co/support/#support
- group: start
  title: ''
  type: SignUp
  url: https://www.alphavantage.co/support/#api-key
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alphavantage.co/terms_of_service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alphavantage.co/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.alphavantage.co/premium/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alphavantage
- group: build
  title: ''
  type: GitHub
  url: https://github.com/RomelTorres/alpha_vantage
- group: commercial
  title: ''
  type: Plans
  url: plans/alpha-vantage-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/alpha-vantage-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/alpha-vantage-finops.yml
created: '2026-05-08'
description: Alpha Vantage provides a single REST market-data API at https://www.alphavantage.co/query exposing 100+ functions across stocks (intraday/daily/weekly/monthly time series, global quote), fundamentals (income statement, balance sheet, cash flow, earnings), forex, crypto, commodities, economic indicators, technical indicators (50+ TA functions), Alpha Intelligence (news, sentiment, insider transactions, top gainers/losers), and options data. Authentication is by apikey query parameter; output is JSON or CSV.
examples:
- key_count: 1
  name: Alpha Vantage Api_Response Example
  slug: alpha-vantage-api_response-example
- key_count: 13
  name: Alpha Vantage Company_Overview Example
  slug: alpha-vantage-company_overview-example
- key_count: 2
  name: Alpha Vantage Economic_Data_Point Example
  slug: alpha-vantage-economic_data_point-example
- key_count: 3
  name: Alpha Vantage Error_Response Example
  slug: alpha-vantage-error_response-example
- key_count: 9
  name: Alpha Vantage Exchange_Rate Example
  slug: alpha-vantage-exchange_rate-example
- key_count: 10
  name: Alpha Vantage Global_Quote Example
  slug: alpha-vantage-global_quote-example
- key_count: 5
  name: Alpha Vantage News_Article Example
  slug: alpha-vantage-news_article-example
- key_count: 5
  name: Alpha Vantage Time_Series_Data Example
  slug: alpha-vantage-time_series_data-example
finops:
- name: Alpha Vantage Finops
  service_category: Fintech
  slug: alpha-vantage-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alpha-vantage.png
json_schemas:
- name: ApiResponse
  property_count: 1
  slug: alpha-vantage-api_response
- name: CompanyOverview
  property_count: 13
  slug: alpha-vantage-company_overview
- name: EconomicDataPoint
  property_count: 2
  slug: alpha-vantage-economic_data_point
- name: ErrorResponse
  property_count: 3
  slug: alpha-vantage-error_response
- name: ExchangeRate
  property_count: 9
  slug: alpha-vantage-exchange_rate
- name: GlobalQuote
  property_count: 10
  slug: alpha-vantage-global_quote
- name: NewsArticle
  property_count: 5
  slug: alpha-vantage-news_article
- name: TimeSeriesData
  property_count: 5
  slug: alpha-vantage-time_series_data
json_structures:
- name: Alpha Vantage Api_Response Structure
  property_count: 1
  slug: alpha-vantage-api_response-structure
- name: Alpha Vantage Company_Overview Structure
  property_count: 13
  slug: alpha-vantage-company_overview-structure
- name: Alpha Vantage Economic_Data_Point Structure
  property_count: 2
  slug: alpha-vantage-economic_data_point-structure
- name: Alpha Vantage Error_Response Structure
  property_count: 3
  slug: alpha-vantage-error_response-structure
- name: Alpha Vantage Exchange_Rate Structure
  property_count: 9
  slug: alpha-vantage-exchange_rate-structure
- name: Alpha Vantage Global_Quote Structure
  property_count: 10
  slug: alpha-vantage-global_quote-structure
- name: Alpha Vantage News_Article Structure
  property_count: 5
  slug: alpha-vantage-news_article-structure
- name: Alpha Vantage Time_Series_Data Structure
  property_count: 5
  slug: alpha-vantage-time_series_data-structure
jsonld:
- class_count: 0
  name: Alpha Vantage Context
  property_count: 35
  slug: alpha-vantage-context
layout: provider
mcp_servers:
- description: ''
  name: alpha-vantage-mcp.yml
  slug: alpha-vantage-mcpyml
modified: '2026-07-22'
name: Alpha Vantage
nav: Providers
network: true
overview: 'Alpha Vantage publishes 1 API on the [APIs.io](https://apis.io/) network: Stock Time Series API. Tagged areas include Fintech, Market Data, Stocks, FX, and Crypto.


  The Alpha Vantage catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Alpha Vantage''s developer surface includes authentication, sandbox, developer portal, documentation, API reference, getting-started guide, support, and 29 more developer resources.'
plans:
- name: Alpha Vantage Plans Pricing
  plan_count: 7
  slug: alpha-vantage-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 7
  name: Alpha Vantage Rate Limits
  slug: alpha-vantage-rate-limits
rules:
- name: Alpha Vantage API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: alpha-vantage-jsonschema-spectral-rules
- name: Alpha Vantage API Rules
  rule_count: 20
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 11
  slug: alpha-vantage-spectral-rules
scopes:
- name: Alpha Vantage Scopes
  scope_count: 1
  slug: alpha-vantage-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: exemplar
  composite: 70.6
  delta: -4.6
  facets:
    commercial_clarity: 84.2
    contract_quality: 61.9
    developer_ergonomics: 77.7
    discoverability: 87.0
    governance: 80.2
    operational_transparency: 36.8
  previous_composite: 75.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 50.0
      derived: 1
      marker_coverage: 50.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 68.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alpha-vantage/refs/heads/main/screenshots/alpha-vantage-2026-06-20T171545.png
security:
- kind: authentication
  name: Alpha Vantage Authentication
  slug: alpha-vantage-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Alpha Vantage Domain Security
  slug: alpha-vantage-domain-security
  summary_line: TLSv1.3
slug: alpha-vantage
tags:
- Fintech
- Market Data
- Stocks
- FX
- Crypto
- Commodities
- Economic Indicators
- Technical Indicators
- Fundamentals
- News
- Sentiment
- Free
website: https://www.alphavantage.co/
---

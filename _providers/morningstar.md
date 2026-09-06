---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 56.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 75
  human_in_the_loop: 0
  name: Morningstar Agentic Access
  operation_count: 724
  slug: morningstar-agentic-access
  summary_line: 724 operations · 75 acting
api_count: 41
apis:
- description: On-demand access to Morningstar's financial market data over HTTP in XML and JSON - real-time, delayed, and end-of-day pricing, price and quote, time and sales, price history, OHLCV, corporate actions
  name: Morningstar Market Data Web Services API
  slug: morningstar-market-data-web-services-api
- baseURL: https://www.us-api.morningstar.com
  baseurl_source: declared
  description: OAuth 2.0 token issuance for all Morningstar APIs - POST /token/oauth with Basic credentials returns a bearer token valid for 60 minutes, usable against the regional Americas, EMEA, and APAC API bases
  name: Morningstar Authentication API
  slug: morningstar-authentication-api
- baseURL: https://www.us-api.morningstar.com
  baseurl_source: declared
  description: Direct Web Services time series data - historical prices, cumulative return, growth, dividend, and other calculated series for securities and managed investments, offered in synchronous and asynchrono
  name: Morningstar Time Series API
  slug: morningstar-time-series-api
- baseURL: https://www.us-api.morningstar.com
  baseurl_source: declared
  description: Screen global equities and managed investments (funds, ETFs) against Morningstar data points, ratings, and classifications, returning display-ready result sets for advisor and investor applications.
  name: Morningstar Screener APIs
  slug: morningstar-screener-api
- baseURL: https://www.us-api.morningstar.com
  baseurl_source: declared
  description: 'Deep security-level data for equities and managed investments - profiles, ratings, performance, holdings, fees, and hundreds of Morningstar data points - in synchronous and asynchronous variants with '
  name: Morningstar Investment Details APIs
  slug: morningstar-investment-details-api
- baseURL: https://www.us-api.morningstar.com
  baseurl_source: declared
  description: Retrieve curated and client-defined investment lists with associated Morningstar data points for rendering list-driven experiences.
  name: Morningstar Investment List API
  slug: morningstar-investment-list-api
- baseURL: https://www.us-api.morningstar.com
  baseurl_source: declared
  description: 'Portfolio calculation engines as APIs - X-Ray decomposition, performance, hypothetical performance, optimizer, and the Morningstar Portfolio Risk Score - across Direct Web Services and the US Dynamic '
  name: Morningstar Portfolio Analysis APIs
  slug: morningstar-portfolio-analysis-api
- baseURL: https://www.us-api.morningstar.com
  baseurl_source: declared
  description: Asynchronous generative summaries and insights over Morningstar data and research, available in Americas and APAC/EMEA regions.
  name: Morningstar AI Insights API
  slug: morningstar-ai-insights-api
- baseURL: https://www.us-api.morningstar.com
  baseurl_source: declared
  description: Stress-test portfolios against historical and hypothetical market scenarios using Morningstar risk engines.
  name: Morningstar Scenario Analysis API
  slug: morningstar-scenario-analysis-api
- baseURL: https://www.us-api.morningstar.com/risk-profiler
  baseurl_source: declared
  description: Investor risk-tolerance profiling built on the FinaMetrica psychometric methodology, returning risk scores and profiles for suitability workflows.
  name: Morningstar Risk Profiler API
  slug: morningstar-risk-profiler-api
- baseURL: https://www.us-api.morningstar.com
  baseurl_source: declared
  description: Utility API for resolving the investment universes and identifiers available to an account across Direct Web Services.
  name: Morningstar Universe API
  slug: morningstar-universe-api
- baseURL: https://www.us-api.morningstar.com
  baseurl_source: declared
  description: US financial-planning building blocks from the Dynamic Services APIs family - households, household members, portfolios, retirement plan lookup and benchmark fees, statement OCR, and report retrieval/
  name: Morningstar Financial Planning APIs
  slug: morningstar-financial-planning-apis
- baseURL: https://www.us-api.morningstar.com/ec/v1
  baseurl_source: declared
  description: Dynamic Services investment-analysis endpoints - securities data (US and global ecint), screening, autocomplete, editorial research, Investor Pulse, risk analytics, risk models, and enterprise-compone
  name: Morningstar Investment Analysis APIs
  slug: morningstar-investment-analysis-apis
- baseURL: https://www.byallaccounts.net/api/v1
  baseurl_source: declared
  description: REST account-aggregation API from Morningstar's ByAllAccounts business, aggregating held-away investment account data for wealth platforms, also reachable through the us-api.morningstar.com aggapi gat
  name: Morningstar ByAllAccounts API
  slug: morningstar-byallaccounts-api
- description: APIs backing Morningstar's embeddable enterprise components - editorial and news search, security details and comparison, investment screener and find-similar, time series (price, dividend, growth, cu
  name: Morningstar Enterprise Component APIs
  slug: morningstar-enterprise-component-apis
- description: WebSocket-based real-time market data streaming with Level 1 quote and Level 2 market-by-price subscriptions, documented publicly through Morningstar's official .NET streaming client library; endpoint
  name: Morningstar Streaming API
  slug: morningstar-streaming-api
- description: On-demand Level 1 market data snapshots over HTTPS with OAuth 2.0, documented publicly through Morningstar's official .NET snapshot client library; endpoints are account-specific and provided during o
  name: Morningstar Snapshot API
  slug: morningstar-snapshot-api
- baseURL: https://agents.morningstar.com
  baseurl_source: declared
  description: Morningstar's AI integration surface - the Morningstar Agent API at agents.morningstar.com plus an MCP server exposing datapoint lookup and editorial research tools to AI agents, with a published agen
  name: Morningstar Agent API
  slug: morningstar-agent-api
artifact_total: 142
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Authorization Tokens Accounts API
  slug: open-morningstar-accounts-api
- collection_type: open
  name: Authorization Tokens Accounts Activities API
  slug: open-morningstar-activities-api
- collection_type: open
  name: Authorization Tokens Accounts Aggregates Financials API
  slug: open-morningstar-aggregates-financials-api
- collection_type: open
  name: Authorization Tokens Accounts Aggregates Market Capitalization and Enterprise Value API
  slug: open-morningstar-aggregates-market-capitalization-and-enterprise-value-api
- collection_type: open
  name: Authorization Tokens Accounts Aggregates Residual Risk and Return Sensitivity API
  slug: open-morningstar-aggregates-residual-risk-and-return-sensitivity-api
- collection_type: open
  name: Authorization Tokens Accounts Aggregates Returns API
  slug: open-morningstar-aggregates-returns-api
- collection_type: open
  name: Authorization Tokens Accounts Analyst Highlights API
  slug: open-morningstar-analyst-highlights-api
- collection_type: open
  name: Authorization Tokens Accounts Analyst Normalized Financials API
  slug: open-morningstar-analyst-normalized-financials-api
- collection_type: open
  name: Authorization Tokens Accounts attribution API
  slug: open-morningstar-attribution-api
- collection_type: open
  name: Authorization Tokens Accounts autocomplete API
  slug: open-morningstar-autocomplete-api
- collection_type: open
  name: Authorization Tokens Accounts Basic Details API
  slug: open-morningstar-basic-details-api
- collection_type: open
  name: Authorization Tokens Accounts Basic Reference API
  slug: open-morningstar-basic-reference-api
- collection_type: open
  name: Authorization Tokens Accounts BenchmarkFees API
  slug: open-morningstar-benchmarkfees-api
- collection_type: open
  name: Authorization Tokens Accounts buckets API
  slug: open-morningstar-buckets-api
- collection_type: open
  name: Authorization Tokens Accounts Clients API
  slug: open-morningstar-clients-api
- collection_type: open
  name: Authorization Tokens Accounts company entitlements API
  slug: open-morningstar-company-entitlements-api
- collection_type: open
  name: Authorization Tokens Accounts Compensation API
  slug: open-morningstar-compensation-api
- collection_type: open
  name: Authorization Tokens Accounts Consensus Estimates API
  slug: open-morningstar-consensus-estimates-api
- collection_type: open
  name: Authorization Tokens Accounts Consensus Recommendations API
  slug: open-morningstar-consensus-recommendations-api
- collection_type: open
  name: Authorization Tokens Accounts Corporate Actions API
  slug: open-morningstar-corporate-actions-api
- collection_type: open
  name: Authorization Tokens Accounts Corporate Actions Price Mergers and Acquisitions API
  slug: open-morningstar-corporate-actions-price-mergers-and-acquisitions-api
- collection_type: open
  name: Authorization Tokens Accounts Credentials API
  slug: open-morningstar-credentials-api
- collection_type: open
  name: Authorization Tokens Accounts CUSIP API
  slug: open-morningstar-cusip-api
- collection_type: open
  name: Authorization Tokens Accounts CUSIP Change API
  slug: open-morningstar-cusip-change-api
- collection_type: open
  name: Authorization Tokens Accounts custodians API
  slug: open-morningstar-custodians-api
- collection_type: open
  name: Authorization Tokens Accounts Data Points API
  slug: open-morningstar-data-points-api
- collection_type: open
  name: Authorization Tokens Accounts decomposition API
  slug: open-morningstar-decomposition-api
- collection_type: open
  name: Authorization Tokens Accounts Earnings Summaries API
  slug: open-morningstar-earnings-summaries-api
- collection_type: open
  name: Authorization Tokens Accounts equity - company research API
  slug: open-morningstar-equity-company-research-api
- collection_type: open
  name: Authorization Tokens Accounts equity - moat framework API
  slug: open-morningstar-equity-moat-framework-api
- collection_type: open
  name: Authorization Tokens Accounts equity reports - quant and enhanced quant API
  slug: open-morningstar-equity-reports-quant-and-enhanced-quant-api
- collection_type: open
  name: Authorization Tokens Accounts equity - rps document API
  slug: open-morningstar-equity-rps-document-api
- collection_type: open
  name: Authorization Tokens Accounts esg API
  slug: open-morningstar-esg-api
- collection_type: open
  name: Authorization Tokens Accounts exposures API
  slug: open-morningstar-exposures-api
- collection_type: open
  name: Authorization Tokens Accounts Fees & Expenses API
  slug: open-morningstar-fees-expenses-api
- collection_type: open
  name: Authorization Tokens Accounts Financials API
  slug: open-morningstar-financials-api
- collection_type: open
  name: Authorization Tokens Accounts flow attribution API
  slug: open-morningstar-flow-attribution-api
- collection_type: open
  name: Authorization Tokens Accounts Fund-Level Sustainability Ratings, Research, and Analytics API
  slug: open-morningstar-fund-level-sustainability-ratings-research-and-analytics-api
- collection_type: open
  name: Authorization Tokens Accounts fund reports - carbon report API
  slug: open-morningstar-fund-reports-carbon-report-api
- collection_type: open
  name: Authorization Tokens Accounts fund reports - esg API
  slug: open-morningstar-fund-reports-esg-api
- collection_type: open
  name: Authorization Tokens Accounts fund reports - managed investment report API
  slug: open-morningstar-fund-reports-managed-investment-report-api
- collection_type: open
  name: Authorization Tokens Accounts fund reports - target date series API
  slug: open-morningstar-fund-reports-target-date-series-api
- collection_type: open
  name: Authorization Tokens Accounts Fund Research, Ratings and Analytics API
  slug: open-morningstar-fund-research-ratings-and-analytics-api
- collection_type: open
  name: Authorization Tokens Accounts Governance API
  slug: open-morningstar-governance-api
- collection_type: open
  name: Authorization Tokens Accounts holdings API
  slug: open-morningstar-holdings-api
- collection_type: open
  name: Authorization Tokens Accounts households API
  slug: open-morningstar-households-api
- collection_type: open
  name: Authorization Tokens Accounts hypo API
  slug: open-morningstar-hypo-api
- collection_type: open
  name: Authorization Tokens Accounts Hypothetical Performance API
  slug: open-morningstar-hypothetical-performance-api
- collection_type: open
  name: Authorization Tokens Accounts IDR (Investment Details Report) API
  slug: open-morningstar-idr-investment-details-report-api
- collection_type: open
  name: Authorization Tokens Accounts Industry Classification API
  slug: open-morningstar-industry-classification-api
- collection_type: open
  name: Authorization Tokens Accounts Industry-Specific Metrics API
  slug: open-morningstar-industry-specific-metrics-api
- collection_type: open
  name: Authorization Tokens Accounts Investment Details API
  slug: open-morningstar-investment-details-api
- collection_type: open
  name: Authorization Tokens Accounts Investment List API
  slug: open-morningstar-investment-list-api
- collection_type: open
  name: Authorization Tokens Accounts Investment Profiles API
  slug: open-morningstar-investment-profiles-api
- collection_type: open
  name: Authorization Tokens Accounts Investments Universe API
  slug: open-morningstar-investments-universe-api
- collection_type: open
  name: Authorization Tokens Accounts Key Events API
  slug: open-morningstar-key-events-api
- collection_type: open
  name: Authorization Tokens Accounts macro shock scenarios API
  slug: open-morningstar-macro-shock-scenarios-api
- collection_type: open
  name: Authorization Tokens Accounts Market Capitalization and Enterprise Value API
  slug: open-morningstar-market-capitalization-and-enterprise-value-api
- collection_type: open
  name: Authorization Tokens Accounts market shock scenarios API
  slug: open-morningstar-market-shock-scenarios-api
- collection_type: open
  name: Authorization Tokens Accounts models API
  slug: open-morningstar-models-api
- collection_type: open
  name: Authorization Tokens Accounts Morningstar Agent API
  slug: open-morningstar-morningstar-agent-api
- collection_type: open
  name: Authorization Tokens Accounts oauth API
  slug: open-morningstar-oauth-api
- collection_type: open
  name: Authorization Tokens Accounts Office Client API
  slug: open-morningstar-office-client-api
- collection_type: open
  name: Authorization Tokens Accounts Office Institution Client API
  slug: open-morningstar-office-institution-client-api
- collection_type: open
  name: Authorization Tokens Accounts Office Members API
  slug: open-morningstar-office-members-api
- collection_type: open
  name: Authorization Tokens Accounts Ownership - Asset Managers API
  slug: open-morningstar-ownership-asset-managers-api
- collection_type: open
  name: Authorization Tokens Accounts Ownership - Insiders API
  slug: open-morningstar-ownership-insiders-api
- collection_type: open
  name: Authorization Tokens Accounts Ownership - Managed Investments API
  slug: open-morningstar-ownership-managed-investments-api
- collection_type: open
  name: Authorization Tokens Accounts Ownership - Regulatory Reporting API
  slug: open-morningstar-ownership-regulatory-reporting-api
- collection_type: open
  name: Authorization Tokens Accounts Ownership - Summary API
  slug: open-morningstar-ownership-summary-api
- collection_type: open
  name: Authorization Tokens Accounts Performance API
  slug: open-morningstar-performance-api
- collection_type: open
  name: Authorization Tokens Accounts Persons API
  slug: open-morningstar-persons-api
- collection_type: open
  name: Authorization Tokens Accounts PJM (Professional Judgement Matrix) API
  slug: open-morningstar-pjm-professional-judgement-matrix-api
- collection_type: open
  name: Authorization Tokens Accounts Plan API
  slug: open-morningstar-plan-api
- collection_type: open
  name: Authorization Tokens Accounts PlanNames API
  slug: open-morningstar-plannames-api
- collection_type: open
  name: Authorization Tokens Accounts Portfolio Analytics API
  slug: open-morningstar-portfolio-analytics-api
- collection_type: open
  name: Authorization Tokens Accounts Portfolio Holdings API
  slug: open-morningstar-portfolio-holdings-api
- collection_type: open
  name: Authorization Tokens Accounts Portfolio Holdings Dates API
  slug: open-morningstar-portfolio-holdings-dates-api
- collection_type: open
  name: Authorization Tokens Accounts Portfolio Risk Score API
  slug: open-morningstar-portfolio-risk-score-api
- collection_type: open
  name: Authorization Tokens Accounts PortfolioOptimizer API
  slug: open-morningstar-portfoliooptimizer-api
- collection_type: open
  name: Authorization Tokens Accounts Portfolios API
  slug: open-morningstar-portfolios-api
- collection_type: open
  name: Authorization Tokens Accounts Positions API
  slug: open-morningstar-positions-api
- collection_type: open
  name: Authorization Tokens Accounts professional judgement matrices API
  slug: open-morningstar-professional-judgement-matrices-api
- collection_type: open
  name: Authorization Tokens Accounts profiles API
  slug: open-morningstar-profiles-api
- collection_type: open
  name: Authorization Tokens Accounts Quantitative Comparables API
  slug: open-morningstar-quantitative-comparables-api
- collection_type: open
  name: Authorization Tokens Accounts Quantitative Equity Rating Analysis API
  slug: open-morningstar-quantitative-equity-rating-analysis-api
- collection_type: open
  name: Authorization Tokens Accounts Quantitative Equity Research Ratings API
  slug: open-morningstar-quantitative-equity-research-ratings-api
- collection_type: open
  name: Authorization Tokens Accounts Questionnaires API
  slug: open-morningstar-questionnaires-api
- collection_type: open
  name: Authorization Tokens Accounts Reference API
  slug: open-morningstar-reference-api
- collection_type: open
  name: Authorization Tokens Accounts Reference Change API
  slug: open-morningstar-reference-change-api
- collection_type: open
  name: Authorization Tokens Accounts report files API
  slug: open-morningstar-report-files-api
- collection_type: open
  name: Authorization Tokens Accounts Reports API
  slug: open-morningstar-reports-api
- collection_type: open
  name: Authorization Tokens Accounts Research Ratings Most Recent and Historical API
  slug: open-morningstar-research-ratings-most-recent-and-historical-api
- collection_type: open
  name: Authorization Tokens Accounts Research Ratings Most Recent API
  slug: open-morningstar-research-ratings-most-recent-api
- collection_type: open
  name: Authorization Tokens Accounts Residual Risk and Return Sensitivity API
  slug: open-morningstar-residual-risk-and-return-sensitivity-api
- collection_type: open
  name: Authorization Tokens Accounts Returns API
  slug: open-morningstar-returns-api
- collection_type: open
  name: Authorization Tokens Accounts risk scores API
  slug: open-morningstar-risk-scores-api
- collection_type: open
  name: Authorization Tokens Accounts Scenario Analysis API
  slug: open-morningstar-scenario-analysis-api
- collection_type: open
  name: Authorization Tokens Accounts Screener API
  slug: open-morningstar-screener-api
- collection_type: open
  name: Authorization Tokens Accounts securities API
  slug: open-morningstar-securities-api
- collection_type: open
  name: Authorization Tokens Accounts SEDOL API
  slug: open-morningstar-sedol-api
- collection_type: open
  name: Authorization Tokens Accounts SEDOL Change API
  slug: open-morningstar-sedol-change-api
- collection_type: open
  name: Authorization Tokens Accounts sensitivity analysis API
  slug: open-morningstar-sensitivity-analysis-api
- collection_type: open
  name: Authorization Tokens Accounts Shareholder Stewardship API
  slug: open-morningstar-shareholder-stewardship-api
- collection_type: open
  name: Authorization Tokens Accounts Short Interest API
  slug: open-morningstar-short-interest-api
- collection_type: open
  name: Authorization Tokens Accounts Solutions API
  slug: open-morningstar-solutions-api
- collection_type: open
  name: Authorization Tokens Accounts statement details API
  slug: open-morningstar-statement-details-api
- collection_type: open
  name: Authorization Tokens Accounts statistics API
  slug: open-morningstar-statistics-api
- collection_type: open
  name: Authorization Tokens Accounts Style Box API
  slug: open-morningstar-style-box-api
- collection_type: open
  name: Authorization Tokens Accounts Time Series API
  slug: open-morningstar-time-series-api
- collection_type: open
  name: Authorization Tokens Accounts timeseries API
  slug: open-morningstar-timeseries-api
- collection_type: open
  name: Authorization Tokens Accounts Token API
  slug: open-morningstar-token-api
- collection_type: open
  name: Authorization Tokens Accounts Total Shares Outstanding API
  slug: open-morningstar-total-shares-outstanding-api
- collection_type: open
  name: Authorization Tokens Accounts Transcripts API
  slug: open-morningstar-transcripts-api
- collection_type: open
  name: Authorization Tokens Accounts Views API
  slug: open-morningstar-views-api
- collection_type: open
  name: Authorization Tokens Accounts X-Ray API
  slug: open-morningstar-x-ray-api
- collection_type: open
  name: Authorization Tokens Accounts x-rays API
  slug: open-morningstar-x-rays-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/morningstar-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/morningstar-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/morningstar-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.morningstar.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.morningstar.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.morningstar.com/direct-web-services
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Morningstar
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/morningstar
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.morningstar.com/user-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.morningstar.com/company/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.morningstar.com/
- group: operate
  title: ''
  type: Support
  url: https://www.morningstar.com/business/products/direct-web-services/contact
- group: build
  title: ''
  type: Packages
  url: packages/morningstar-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/morningstar-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/morningstar-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/morningstar-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/morningstar-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/morningstar-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/morningstar-agent-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/morningstar-securities-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/morningstar-screener-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/morningstar-x-ray-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/morningstar-token-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/morningstar-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/morningstar-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/morningstar-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/morningstar-scopes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/morningstar-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/morningstar-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/morningstar-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/morningstar-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/morningstar-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.morningstar.com/company/vulnerability-disclosure
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/dynamic-services-morningstar-com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.morningstar.com/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.morningstar.com/content/documentation/documentation/get-started/authentication/get-started-authentication.md
- group: company
  title: ''
  type: Blog
  url: https://newsroom.morningstar.com/
created: '2026-07-21'
description: Morningstar, Inc. (Nasdaq MORN) is a Chicago-based investment research and financial market data company selling fund and equity data, analyst research, ratings, indexes, and portfolio analytics to advisors, asset managers, and fintechs. Its developer portal at developer.morningstar.com documents two large API families - Direct Web Services and Dynamic Services APIs - delivered as regional REST bases (us/emea/apac-api.morningstar.com) secured with OAuth 2.0 tokens, plus a Market Data Web Services API for real-time, delayed, and end-of-day pricing, a WebSocket Streaming API for Level 1/Level 2 market data, ByAllAccounts account aggregation, and an emerging MCP/agent surface. Documentation and OpenAPI 3.x specs are fully public, but credentials are sales-gated through Morningstar onboarding - there is no self-serve signup. Morningstar remains an independent public company and owns PitchBook, DBRS (credit ratings), and ByAllAccounts.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/morningstar.png
layout: provider
mcp_servers:
- description: ''
  name: Morningstar MCP Server
  slug: morningstar-mcp-server
modified: '2026-07-22'
name: Morningstar
nav: Providers
network: true
overview: 'Morningstar publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Time Series API, Screener APIs, and 11 more. Tagged areas include Financial, Market Data, Investing, Stocks, and Funds.


  Morningstar''s developer surface includes authentication, developer portal, documentation, support, sandbox, API reference, getting-started guide, and 31 more developer resources.'
random_paper: 7
scopes:
- name: Morningstar Scopes
  scope_count: 4
  slug: morningstar-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 45.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 56.6
    developer_ergonomics: 73.8
    discoverability: 64.8
    governance: 4.5
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 45.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 117
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 61.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/morningstar/refs/heads/main/screenshots/morningstar-2026-07-22T202515.png
security:
- kind: authentication
  name: Morningstar Authentication
  slug: morningstar-authentication
  summary_line: http-basic (token issuance)/bearer (API calls)/oauth2 (MCP server) · 1 scheme
- kind: domain-security
  name: Morningstar Domain Security
  slug: morningstar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Morningstar Vulnerability Disclosure
  slug: morningstar-vulnerability-disclosure
  summary_line: Bugcrowd · contact published
slug: morningstar
tags:
- Financial
- Market Data
- Investing
- Stocks
- Funds
- Real-Time
- Reference Data
- Portfolio Analytics
- Research
- Indexes
website: https://www.morningstar.com/
---

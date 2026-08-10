---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 56.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 75
  human_in_the_loop: 0
  name: Morningstar Agentic Access
  operation_count: 724
  slug: morningstar-agentic-access
  summary_line: 724 operations · 75 acting
api_count: 18
apis:
- description: On-demand access to Morningstar's financial market data over HTTP in XML and JSON - real-time, delayed, and end-of-day pricing, price and quote, time and sales, price history, OHLCV, corporate actions
  name: Morningstar Market Data Web Services API
  slug: morningstar-market-data-web-services-api
- description: OAuth 2.0 token issuance for all Morningstar APIs - POST /token/oauth with Basic credentials returns a bearer token valid for 60 minutes, usable against the regional Americas, EMEA, and APAC API bases
  name: Morningstar Authentication API
  slug: morningstar-authentication-api
- description: Direct Web Services time series data - historical prices, cumulative return, growth, dividend, and other calculated series for securities and managed investments, offered in synchronous and asynchrono
  name: Morningstar Time Series API
  slug: morningstar-time-series-api
- description: Screen global equities and managed investments (funds, ETFs) against Morningstar data points, ratings, and classifications, returning display-ready result sets for advisor and investor applications.
  name: Morningstar Screener APIs
  slug: morningstar-screener-api
- description: 'Deep security-level data for equities and managed investments - profiles, ratings, performance, holdings, fees, and hundreds of Morningstar data points - in synchronous and asynchronous variants with '
  name: Morningstar Investment Details APIs
  slug: morningstar-investment-details-api
- description: Retrieve curated and client-defined investment lists with associated Morningstar data points for rendering list-driven experiences.
  name: Morningstar Investment List API
  slug: morningstar-investment-list-api
- description: 'Portfolio calculation engines as APIs - X-Ray decomposition, performance, hypothetical performance, optimizer, and the Morningstar Portfolio Risk Score - across Direct Web Services and the US Dynamic '
  name: Morningstar Portfolio Analysis APIs
  slug: morningstar-portfolio-analysis-api
- description: Asynchronous generative summaries and insights over Morningstar data and research, available in Americas and APAC/EMEA regions.
  name: Morningstar AI Insights API
  slug: morningstar-ai-insights-api
- description: Stress-test portfolios against historical and hypothetical market scenarios using Morningstar risk engines.
  name: Morningstar Scenario Analysis API
  slug: morningstar-scenario-analysis-api
- description: Investor risk-tolerance profiling built on the FinaMetrica psychometric methodology, returning risk scores and profiles for suitability workflows.
  name: Morningstar Risk Profiler API
  slug: morningstar-risk-profiler-api
- description: Utility API for resolving the investment universes and identifiers available to an account across Direct Web Services.
  name: Morningstar Universe API
  slug: morningstar-universe-api
- description: US financial-planning building blocks from the Dynamic Services APIs family - households, household members, portfolios, retirement plan lookup and benchmark fees, statement OCR, and report retrieval/
  name: Morningstar Financial Planning APIs
  slug: morningstar-financial-planning-apis
- description: Dynamic Services investment-analysis endpoints - securities data (US and global ecint), screening, autocomplete, editorial research, Investor Pulse, risk analytics, risk models, and enterprise-compone
  name: Morningstar Investment Analysis APIs
  slug: morningstar-investment-analysis-apis
- description: REST account-aggregation API from Morningstar's ByAllAccounts business, aggregating held-away investment account data for wealth platforms, also reachable through the us-api.morningstar.com aggapi gat
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
- description: Morningstar's AI integration surface - the Morningstar Agent API at agents.morningstar.com plus an MCP server exposing datapoint lookup and editorial research tools to AI agents, with a published agen
  name: Morningstar Agent API
  slug: morningstar-agent-api
artifact_total: 24
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
  name: morningstar-mcp.yml
  slug: morningstar-mcpyml
modified: '2026-07-22'
name: Morningstar
nav: Providers
network: true
overview: 'Morningstar publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Time Series API, Screener APIs, and 11 more. Tagged areas include Financial, Market Data, Investing, Stocks, and Funds.


  Morningstar''s developer surface includes authentication, developer portal, documentation, support, sandbox, API reference, getting-started guide, and 31 more developer resources.'
random_paper: 44
scopes:
- name: Morningstar Scopes
  scope_count: 4
  slug: morningstar-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 52.5
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 58.8
    developer_ergonomics: 84.8
    discoverability: 83.3
    governance: 11.5
    operational_transparency: 31.6
  previous_composite: 52.5
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
    score: 68.3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
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

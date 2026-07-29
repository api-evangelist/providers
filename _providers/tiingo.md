---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Tiingo Agentic Access
  operation_count: 37
  slug: tiingo-agentic-access
  summary_line: 37 operations
api_count: 6
apis:
- description: Daily OHLCV history for 100,000+ US equities and ETFs back to 1962, with split and dividend adjustments.
  name: Tiingo End-of-Day API
  slug: end-of-day-api
- description: IEX-sourced intraday quotes and trades over REST and WebSocket - real-time during US market hours.
  name: Tiingo IEX Intraday API
  slug: iex-intraday-api
- description: Crypto top-of-book and trade data aggregated from major exchanges over REST and WebSocket.
  name: Tiingo Crypto API
  slug: crypto-api
- description: Real-time and historical FX rates for major and emerging-market currency pairs.
  name: Tiingo Forex API
  slug: forex-api
- description: Income statement, balance sheet, cash flow, and corporate event data sourced from SEC filings.
  name: Tiingo Fundamentals API
  slug: fundamentals-api
- description: Tagged equity news from 1,000+ publishers with ticker, topic, and source filters.
  name: Tiingo News API
  slug: news-api
artifact_total: 15
asyncapis:
- description: Tiingo's WebSocket streaming interface for real-time market data. Clients subscribe and unsubscribe to data feeds by sending a JSON request containing eventName, an authorization API token, and eventD
  name: Tiingo WebSocket API
  slug: tiingo-websockets-asyncapi
collections:
- collection_type: postman
  name: Tiingo API
  slug: postman-tiingo
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/tiingo/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tiingo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tiingo-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tiingo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tiingo
- group: start
  title: ''
  type: Portal
  url: https://www.tiingo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tiingo.com/documentation/general/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tiingo.com/about/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/tiingo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tiingo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tiingo-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.tiingo.com/blog/feed/
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/tiingo-websockets-asyncapi.yml
- group: build
  title: ''
  type: Packages
  url: packages/tiingo-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tiingo-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tiingo-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/tiingo-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/tiingo-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tiingo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tiingo-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tiingo.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tiingo-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tiingo-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tiingo-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tiingo-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tiingo-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: APIReference
  url: https://www.tiingo.com/documentation/general/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://www.tiingo.com/documentation/general/connecting
- group: operate
  title: ''
  type: Support
  url: https://www.tiingo.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tiingo.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tiingo.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://www.tiingo.com/
created: '2026-05-08'
description: Tiingo provides high-quality financial market data APIs across US equities, crypto, FX, fundamentals, and news, popular among quantitative researchers. APIs include End-of-Day prices, IEX intraday data, Crypto, Forex, Fundamentals, and News, with REST and WebSocket access at api.tiingo.com.
finops:
- name: Tiingo Finops
  service_category: Fintech
  slug: tiingo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tiingo.png
layout: provider
mcp_servers:
- description: ''
  name: tiingo-mcp.yml
  slug: tiingo-mcpyml
modified: '2026-07-22'
name: Tiingo
nav: Providers
network: true
overview: 'Tiingo publishes 6 APIs on the [APIs.io](https://apis.io/) network, including End-of-Day API, IEX Intraday API, Crypto API, and 3 more. Tagged areas include Fintech, Market Data, Stocks, Crypto, and FX.


  The Tiingo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tiingo''s developer surface includes developer portal, documentation, pricing, engineering blog, changelog, authentication, sandbox, and 26 more developer resources.'
plans:
- name: Tiingo Plans Pricing
  plan_count: 4
  slug: tiingo-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 4
  name: Tiingo Rate Limits
  slug: tiingo-rate-limits
score:
  band: strong
  composite: 62.3
  delta: -0.6
  facets:
    commercial_clarity: 84.2
    contract_quality: 57.6
    developer_ergonomics: 66.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 68.4
  previous_composite: 62.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
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
screenshot: https://raw.githubusercontent.com/api-evangelist/tiingo/refs/heads/main/screenshots/tiingo-2026-06-20T195345.png
security:
- kind: authentication
  name: Tiingo Authentication
  slug: tiingo-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Tiingo Domain Security
  slug: tiingo-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: tiingo
tags:
- Fintech
- Market Data
- Stocks
- Crypto
- FX
- News
- Fundamentals
- WebSockets
website: https://www.tiingo.com/
---

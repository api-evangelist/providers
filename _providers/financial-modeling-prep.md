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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 81.7
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Financial Modeling Prep Agentic Access
  operation_count: 10
  slug: financial-modeling-prep-agentic-access
  summary_line: 10 operations
api_count: 10
apis:
- description: The Balance Sheet Statement API from Financial Modeling Prep — 1 operation(s) for balance sheet statement.
  name: Financial Modeling Prep Balance Sheet Statement API
  slug: financial-modeling-prep-balance-sheet-statement-api
- description: The Cash Flow Statement API from Financial Modeling Prep — 1 operation(s) for cash flow statement.
  name: Financial Modeling Prep Cash Flow Statement API
  slug: financial-modeling-prep-cash-flow-statement-api
- description: The Historical Price Full API from Financial Modeling Prep — 1 operation(s) for historical price full.
  name: Financial Modeling Prep Historical Price Full API
  slug: financial-modeling-prep-historical-price-full-api
- description: The Income Statement API from Financial Modeling Prep — 1 operation(s) for income statement.
  name: Financial Modeling Prep Income Statement API
  slug: financial-modeling-prep-income-statement-api
- description: The Insider Trading API from Financial Modeling Prep — 1 operation(s) for insider trading.
  name: Financial Modeling Prep Insider Trading API
  slug: financial-modeling-prep-insider-trading-api
- description: The Profile API from Financial Modeling Prep — 1 operation(s) for profile.
  name: Financial Modeling Prep Profile API
  slug: financial-modeling-prep-profile-api
- description: The Quote API from Financial Modeling Prep — 1 operation(s) for quote.
  name: Financial Modeling Prep Quote API
  slug: financial-modeling-prep-quote-api
- description: The Ratios API from Financial Modeling Prep — 1 operation(s) for ratios.
  name: Financial Modeling Prep Ratios API
  slug: financial-modeling-prep-ratios-api
- description: The Search API from Financial Modeling Prep — 1 operation(s) for search.
  name: Financial Modeling Prep Search API
  slug: financial-modeling-prep-search-api
- description: The Stock API from Financial Modeling Prep — 1 operation(s) for stock.
  name: Financial Modeling Prep Stock API
  slug: financial-modeling-prep-stock-api
artifact_total: 19
asyncapis:
- description: Real-time market data streaming from Financial Modeling Prep. Authenticate with a login event carrying your API key, then subscribe to tickers or predefined market streams. Derived from the Websockets
  name: Financial Modeling Prep WebSocket API
  slug: financial-modeling-prep-websocket-asyncapi
collections:
- collection_type: open
  name: Financial Modeling Prep API
  slug: open-financial-modeling-prep
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/financial-modeling-prep-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/financial-modeling-prep-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/financial-modeling-prep-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/financial-modeling-prep-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FinancialModelingPrep
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/financial-modeling-prep
- group: company
  title: ''
  type: Website
  url: https://site.financialmodelingprep.com/
- group: docs
  title: ''
  type: Documentation
  url: https://site.financialmodelingprep.com/developer/docs
- group: start
  title: ''
  type: Signup
  url: https://site.financialmodelingprep.com/register
- group: commercial
  title: ''
  type: Pricing
  url: https://site.financialmodelingprep.com/developer/docs/pricing
- group: company
  title: ''
  type: Blog
  url: https://site.financialmodelingprep.com/market-news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://site.financialmodelingprep.com/developer
- group: docs
  title: ''
  type: APIReference
  url: https://site.financialmodelingprep.com/developer/docs
- group: operate
  title: ''
  type: Support
  url: https://site.financialmodelingprep.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://site.financialmodelingprep.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://site.financialmodelingprep.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.financialmodelingprep.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/financial-modeling-prep-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/financial-modeling-prep-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/financial-modeling-prep-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/financial-modeling-prep-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/financial-modeling-prep-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/financial-modeling-prep-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://site.financialmodelingprep.com/trust
- group: agent
  title: ''
  type: WellKnown
  url: well-known/financial-modeling-prep-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/financial-modeling-prep-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/financial-modeling-prep-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/financial-modeling-prep-mcp.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/financial-modeling-prep-websocket-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/financial-modeling-prep-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/financial-modeling-prep-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/financial-modeling-prep-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/financial-modeling-prep-finops.yml
- group: build
  title: ''
  type: Postman
  url: collections/financial-modeling-prep.postman_collection.json
created: '2025-02-24'
description: Financial Modeling Prep (FMP) provides financial market data via REST APIs, including real-time and historical stock quotes, company fundamentals, income statements, balance sheets, cash flow statements, financial ratios, insider transactions, earnings, dividends, ETF and mutual fund data, and economic indicators - with up to 30 years of historical coverage.
finops:
- name: Financial Modeling Prep Finops
  service_category: API
  slug: financial-modeling-prep-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/financial-modeling-prep.png
layout: provider
modified: '2026-07-22'
name: Financial Modeling Prep
nav: Providers
network: true
overview: 'Financial Modeling Prep publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Balance Sheet Statement API, Cash Flow Statement API, Historical Price Full API, and 7 more. Tagged areas include Financial Data, Market Data, Stocks, Quotes, and Fundamentals.


  The Financial Modeling Prep catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Financial Modeling Prep''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, API reference, support, and 28 more developer resources.'
plans:
- name: Financial Modeling Prep Plans Pricing
  plan_count: 4
  slug: financial-modeling-prep-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 4
  name: Financial Modeling Prep Rate Limits
  slug: financial-modeling-prep-rate-limits
score:
  band: strong
  composite: 64.8
  delta: 21.4
  facets:
    commercial_clarity: 86.8
    contract_quality: 74.3
    developer_ergonomics: 60.9
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 76.3
  previous_composite: 43.4
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 65.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: rising
security:
- kind: authentication
  name: Financial Modeling Prep Authentication
  slug: financial-modeling-prep-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Financial Modeling Prep Domain Security
  slug: financial-modeling-prep-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Financial Modeling Prep Trust Center
  slug: financial-modeling-prep-trust-center
  summary_line: SOC 2
slug: financial-modeling-prep
tags:
- Financial Data
- Market Data
- Stocks
- Quotes
- Fundamentals
- Financial Statements
- Historical
website: https://site.financialmodelingprep.com/
---

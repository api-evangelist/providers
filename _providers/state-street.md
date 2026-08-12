---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: State Street Agentic Access
  operation_count: 13
  slug: state-street-agentic-access
  summary_line: 13 operations · 2 acting
api_count: 11
apis:
- description: 'The State Street Investment Accounting API provides institutional clients with access to portfolio accounting data including net asset value (NAV) calculations, position valuations, corporate actions '
  name: Investment Accounting API
  slug: investment-accounting-api
- description: The State Street Performance Analytics API (TrueView) provides institutional investors and asset managers with access to investment risk analytics, performance attribution, scenario analysis, and repo
  name: Performance Analytics API
  slug: performance-analytics-api
- description: The State Street Sample Transactions API is a reference and onboarding API provided in the developer portal to help new integration teams understand the authentication flow, request structure, and res
  name: Sample Transactions API
  slug: sample-transactions-api
- description: ETF portfolio composition basket operations
  name: State Street Baskets API
  slug: state-street-baskets-api
- description: ETF fund information operations
  name: State Street Funds API
  slug: state-street-funds-api
- description: ETF creation and redemption order operations
  name: State Street Orders API
  slug: state-street-orders-api
- description: Performance measurement and attribution operations
  name: State Street Performance API
  slug: state-street-performance-api
- description: Portfolio and account management operations
  name: State Street Portfolios API
  slug: state-street-portfolios-api
- description: Portfolio position and holdings operations
  name: State Street Positions API
  slug: state-street-positions-api
- description: Risk analytics and exposure operations
  name: State Street Risk API
  slug: state-street-risk-api
- description: Transaction history and settlement operations
  name: State Street Transactions API
  slug: state-street-transactions-api
artifact_total: 41
collections:
- collection_type: open
  name: State Street Alpha Data Platform API
  slug: open-state-street-alpha-data-platform
- collection_type: open
  name: State Street Fund Connect API
  slug: open-state-street-fund-connect
common:
- group: company
  title: ''
  type: Blog
  url: https://www.statestreet.com/content/statestreet/us/en/insights
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/state-street-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/state-street-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/state-street-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/state-street-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/statestreet
- group: company
  title: ''
  type: Website
  url: https://www.statestreet.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.statestreet.com
- group: other
  title: ''
  type: API Catalog
  url: https://developer.statestreet.com/apis-list
- group: other
  title: ''
  type: API Overview
  url: https://developer.statestreet.com/api-overview
- group: docs
  title: ''
  type: Documentation
  url: https://developer.statestreet.com/documentation-usage
- group: other
  title: ''
  type: API Standards
  url: https://developer.statestreet.com/api-platform-standards
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.statestreet.com/get-started-browser
- group: operate
  title: ''
  type: Support
  url: mailto:api-support@statestreet.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/state-street-corporation
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/StateStreet
- group: other
  title: ''
  type: Alpha Platform
  url: https://www.statestreet.com/alpha
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.statestreet.com/us/en/individual-investor/tools-and-resources/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.statestreet.com/us/en/individual-investor/tools-and-resources/terms-and-conditions
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/state-street-alpha-data-platform-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/state-street-fund-connect-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/state-street-portfolio-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/state-street-position-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/state-street-portfolio-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/state-street-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/state-street-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/state-street-rules.yml
description: State Street Corporation is one of the world's largest financial services companies, headquartered in Boston, Massachusetts. Founded in 1792, State Street provides investment servicing, investment management, investment research, and trading services to institutional investors including mutual funds, collective investment funds, corporate and public retirement plans, insurance companies, foundations, and endowments. State Street manages approximately $4.7 trillion in assets under management through State Street Global Advisors and services nearly $40 trillion in assets under custody. The company operates the State Street Alpha front-to-back investment management platform, Fund Connect for ETF creation and redemption, and Charles River Development for investment management technology. State Street's developer portal at developer.statestreet.com provides OAuth 2.0-secured APIs enabling institutional clients to programmatically access portfolio data, transaction history, NAV calculations,
  analytics, and ETF order management. APIs follow REST conventions with OpenAPI 3.0 specifications, JSON data format, and JSON Schema documentation.
examples:
- key_count: 2
  name: State Street List Portfolio Positions Example
  slug: state-street-list-portfolio-positions-example
finops:
- name: State Street Finops
  service_category: Financial Services / Asset Servicing
  slug: state-street-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/state-street.png
json_schemas:
- name: BasketResponse
  property_count: 4
  slug: state-street-basketresponse
- name: Error
  property_count: 3
  slug: state-street-error
- name: Fund
  property_count: 9
  slug: state-street-fund
- name: FundListResponse
  property_count: 3
  slug: state-street-fundlistresponse
- name: Order
  property_count: 9
  slug: state-street-order
- name: OrderListResponse
  property_count: 3
  slug: state-street-orderlistresponse
- name: OrderRequest
  property_count: 5
  slug: state-street-orderrequest
- name: PerformanceResponse
  property_count: 8
  slug: state-street-performanceresponse
- name: Portfolio
  property_count: 8
  slug: state-street-portfolio
- name: PortfolioListResponse
  property_count: 3
  slug: state-street-portfoliolistresponse
- name: Position
  property_count: 11
  slug: state-street-position
- name: PositionListResponse
  property_count: 5
  slug: state-street-positionlistresponse
- name: RiskResponse
  property_count: 8
  slug: state-street-riskresponse
- name: Transaction
  property_count: 11
  slug: state-street-transaction
- name: TransactionListResponse
  property_count: 6
  slug: state-street-transactionlistresponse
json_structures:
- name: State Street Portfolio Structure
  property_count: 0
  slug: state-street-portfolio-structure
- name: State Street Structure
  property_count: 0
  slug: state-street-structure
jsonld:
- class_count: 15
  name: State Street Context
  property_count: 20
  slug: state-street-context
layout: provider
modified: '2026-05-19'
name: State Street
nav: Providers
network: true
overview: 'State Street publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Baskets API, Funds API, Orders API, and 5 more. Tagged areas include Fortune 500.


  The State Street catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  State Street''s developer surface includes engineering blog, authentication, documentation, getting-started guide, support, and 22 more developer resources.'
plans:
- name: State Street Plans Pricing
  plan_count: 1
  slug: state-street-plans-pricing
press:
- date: '2026-05-25'
  title: State Street to unveil AI agents for client services this summer
  url: https://www.bizjournals.com/boston/news/2026/04/17/state-street-ai-tools-launching-summer-2026.html
- date: '2026-05-25'
  title: Annual Report 2024
  url: https://www.statestreet.com/content/dam/stt/web/about/our-story/annual-report/documents/ssc-annual-report-2024.pdf
- date: '2026-05-25'
  title: State Street and UC Investments Forge Strategic Alliance ...
  url: https://www.stocktitan.net/news/STT/state-street-and-uc-investments-forge-strategic-alliance-to-expand-741wudclkkig.html
- date: '2026-05-25'
  title: Hemant Rao - Vice President, Automation and Artificial ...
  url: https://www.linkedin.com/in/hemantrao0825
- date: '2026-05-25'
  title: State Street (STT) Q1 2026 Earnings Call Transcript
  url: https://fortune.com/company/state-street-corp/earnings/q1-2026/
random_paper: 93
rate_limits:
- limit_count: 1
  name: State Street Rate Limits
  slug: state-street-rate-limits
rules:
- name: State Street API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: state-street-jsonschema-spectral-rules
- name: State Street API Rules
  rule_count: 16
  severity_counts:
    error: 10
    hint: 0
    info: 0
    warn: 6
  slug: state-street-rules
scopes:
- name: State Street Scopes
  scope_count: 8
  slug: state-street-scopes
  summary_line: 8 scopes · clientCredentials
score:
  band: developing
  composite: 48.9
  delta: -5.4
  facets:
    commercial_clarity: 34.2
    contract_quality: 69.4
    developer_ergonomics: 45.7
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 10.5
  previous_composite: 54.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/state-street/refs/heads/main/screenshots/state-street-2026-06-20T194521.png
security:
- kind: authentication
  name: State Street Authentication
  slug: state-street-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: State Street Domain Security
  slug: state-street-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: state-street
tags:
- Fortune 500
website: https://www.statestreet.com
---

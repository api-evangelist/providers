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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Murex Agentic Access
  operation_count: 49
  slug: murex-agentic-access
  summary_line: 49 operations · 6 acting
api_count: 24
apis:
- description: Comprehensive capital markets platform providing trading, risk management, and post-trade operations across all asset classes.
  name: Murex MX.3 Platform
  slug: murex-mx3-platform
- description: Accounting entries and journal operations
  name: Murex Accounting API
  slug: murex-accounting-api
- description: Cash flow projections and management
  name: Murex Cash Flows API
  slug: murex-cash-flows-api
- description: Collateral management and margin operations
  name: Murex Collateral API
  slug: murex-collateral-api
- description: Trade confirmation generation and matching
  name: Murex Confirmations API
  slug: murex-confirmations-api
- description: Yield curves and forward curves
  name: Murex Curves API
  slug: murex-curves-api
- description: Foreign exchange rates and crosses
  name: Murex FX Rates API
  slug: murex-fx-rates-api
- description: Financial instrument reference data
  name: Murex Instruments API
  slug: murex-instruments-api
- description: Risk limit monitoring and management
  name: Murex Limits API
  slug: murex-limits-api
- description: Order creation, modification, and lifecycle management
  name: Murex Orders API
  slug: murex-orders-api
- description: Profit and loss calculations and reporting
  name: Murex P&L API
  slug: murex-p-l-api
- description: Trading portfolio and book management
  name: Murex Portfolios API
  slug: murex-portfolios-api
- description: Portfolio position retrieval and management
  name: Murex Positions API
  slug: murex-positions-api
- description: Real-time and historical price quotes
  name: Murex Quotes API
  slug: murex-quotes-api
- description: Position and cash reconciliation operations
  name: Murex Reconciliations API
  slug: murex-reconciliations-api
- description: Market reference and static data
  name: Murex Reference Data API
  slug: murex-reference-data-api
- description: Regulatory capital and compliance metrics
  name: Murex Regulatory API
  slug: murex-regulatory-api
- description: Regulatory trade and transaction reporting
  name: Murex Regulatory Reporting API
  slug: murex-regulatory-reporting-api
- description: Greek and sensitivity calculations
  name: Murex Sensitivities API
  slug: murex-sensitivities-api
- description: Settlement instruction management and processing
  name: Murex Settlements API
  slug: murex-settlements-api
- description: Stress testing and scenario analysis
  name: Murex Stress Testing API
  slug: murex-stress-testing-api
- description: Trade execution and trade blotter operations
  name: Murex Trades API
  slug: murex-trades-api
- description: Value at Risk calculations and reports
  name: Murex VaR API
  slug: murex-var-api
- description: Volatility surfaces and skew data
  name: Murex Volatility API
  slug: murex-volatility-api
artifact_total: 39
collections:
- collection_type: open
  name: Murex MX.3 Market Data API
  slug: open-murex-market-data
- collection_type: open
  name: Murex MX.3 Position API
  slug: open-murex-position
- collection_type: open
  name: Murex MX.3 Post-Trade API
  slug: open-murex-post-trade
- collection_type: open
  name: Murex MX.3 Risk API
  slug: open-murex-risk
- collection_type: open
  name: Murex MX.3 Trading API
  slug: open-murex-trading
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/murex-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/murex-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/murex-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/murex
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/murex
- group: company
  title: ''
  type: Website
  url: https://www.murex.com
- group: operate
  title: ''
  type: Support
  url: https://www.murex.com/en/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.murex.com/en/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.murex.com/en/legal/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.murex.com/en/news
created: '2024-01-01'
description: Murex is a global fintech leader in trading, treasury, risk management and post-trade operations software. Their MX.3 platform provides comprehensive solutions for capital markets across asset classes.
finops:
- name: Murex Finops
  service_category: API
  slug: murex-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/murex.png
json_schemas:
- name: Murex Position
  property_count: 23
  slug: murex-position
- name: Murex Trade
  property_count: 27
  slug: murex-trade
jsonld:
- class_count: 0
  name: Murex Context
  property_count: 11
  slug: murex-context
layout: provider
modified: '2026-05-19'
name: Murex
nav: Providers
network: true
overview: 'Murex publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Accounting API, Cash Flows API, Collateral API, and 20 more. Tagged areas include Capital Markets, Enterprise Software, Financial Services, Fintech, and Risk Management.


  The Murex catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Murex''s developer surface includes authentication, support, engineering blog, and 7 more developer resources.'
plans:
- name: Murex Plans Pricing
  plan_count: 3
  slug: murex-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Murex Rate Limits
  slug: murex-rate-limits
rules:
- name: Murex API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: murex-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.1
  delta: 0.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 67.7
    developer_ergonomics: 17.4
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 36.8
  previous_composite: 52.9
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 54.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/murex/refs/heads/main/screenshots/murex-2026-06-20T185859.png
security:
- kind: authentication
  name: Murex Authentication
  slug: murex-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Murex Domain Security
  slug: murex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: murex
tags:
- Capital Markets
- Enterprise Software
- Financial Services
- Fintech
- Risk Management
- Trading
website: https://www.murex.com
---

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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Degiro Agentic Access
  operation_count: 17
  slug: degiro-agentic-access
  summary_line: 17 operations · 4 acting
api_count: 11
apis:
- description: Endpoint suite for discovering tradable financial instruments on the DEGIRO platform. Supports full-text search across stocks, ETFs, bonds, options, futures, warrants, leveraged products, and investme
  name: DEGIRO Product Search API
  slug: degiro-product-search-api
- description: Real-time market data streaming service providing live ticker subscriptions for price, volume, bid/ask, and OHLC metrics across tradable instruments. Supports chart data retrieval with multiple time r
  name: DEGIRO Quotecast API
  slug: degiro-quotecast-api
- description: Account reporting endpoint providing downloadable financial statements and transaction records in multiple formats including CSV, HTML, PDF, and XLS. Supports account reports, transaction history expo
  name: DEGIRO Reporting API
  slug: degiro-reporting-api
- description: Company intelligence endpoints providing news feeds, company profiles, financial ratios, income statements, balance sheets, analyst estimates, and corporate event agendas (earnings, dividends, IPOs, s
  name: DEGIRO News and Company Intelligence API
  slug: degiro-news-and-company-intelligence-api
- description: The config API from DEGIRO — 1 operation(s) for config.
  name: DEGIRO config API
  slug: degiro-config-api
- description: The login API from DEGIRO — 1 operation(s) for login.
  name: DEGIRO login API
  slug: degiro-login-api
- description: The pa API from DEGIRO — 3 operation(s) for pa.
  name: DEGIRO pa API
  slug: degiro-pa-api
- description: The product-search API from DEGIRO — 1 operation(s) for product-search.
  name: DEGIRO product-search API
  slug: degiro-product-search-api
- description: The reporting API from DEGIRO — 2 operation(s) for reporting.
  name: DEGIRO reporting API
  slug: degiro-reporting-api
- description: The settings API from DEGIRO — 4 operation(s) for settings.
  name: DEGIRO settings API
  slug: degiro-settings-api
- description: The trading API from DEGIRO — 4 operation(s) for trading.
  name: DEGIRO trading API
  slug: degiro-trading-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Unofficial Degiro config API
  slug: open-degiro-config-api
- collection_type: open
  name: Unofficial Degiro config login API
  slug: open-degiro-login-api
- collection_type: open
  name: Unofficial Degiro config pa API
  slug: open-degiro-pa-api
- collection_type: open
  name: Unofficial Degiro config product-search API
  slug: open-degiro-product-search-api
- collection_type: open
  name: Unofficial Degiro config reporting API
  slug: open-degiro-reporting-api
- collection_type: open
  name: Unofficial Degiro config settings API
  slug: open-degiro-settings-api
- collection_type: open
  name: Unofficial Degiro config trading API
  slug: open-degiro-trading-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/degiro-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/degiro-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/degiro-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/degiro
- group: company
  title: ''
  type: Website
  url: https://www.degiro.eu
- group: operate
  title: ''
  type: Support
  url: https://www.degiro.eu/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.degiro.eu/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.degiro.eu/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://trader.degiro.nl/login
- group: company
  title: ''
  type: Blog
  url: https://www.degiro.eu/investor-updates
- group: operate
  title: ''
  type: Status
  url: https://www.degiro.eu/service-status
- group: operate
  title: ''
  type: FAQ
  url: https://www.degiro.eu/helpdesk
created: '2026-06-13'
description: DEGIRO is a European discount brokerage platform providing low-cost trading across stocks, ETFs, bonds, options, futures, warrants, and investment funds. While DEGIRO does not publish an official public API, their trading platform exposes REST-style HTTP endpoints used by the web and mobile trading applications. These unofficial endpoints support session-based authentication, portfolio management, order execution, real-time and historical market data, product search, account reporting, and company intelligence. The platform serves retail investors across Europe with among the lowest trading commissions on the continent.
examples:
- key_count: 5
  name: Degiro Login Example
  slug: degiro-login-example
- key_count: 5
  name: Degiro Place Order Example
  slug: degiro-place-order-example
- key_count: 5
  name: Degiro Portfolio Example
  slug: degiro-portfolio-example
- key_count: 5
  name: Degiro Product Search Example
  slug: degiro-product-search-example
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/degiro.png
json_schemas:
- name: DEGIRO Login
  property_count: 5
  slug: degiro-login
- name: DEGIRO Order
  property_count: 7
  slug: degiro-order
- name: DEGIRO Portfolio Position
  property_count: 9
  slug: degiro-portfolio
- name: DEGIRO Product
  property_count: 12
  slug: degiro-product
- name: DEGIRO Session
  property_count: 6
  slug: degiro-session
jsonld:
- class_count: 0
  name: Degiro Context
  property_count: 6
  slug: degiro-context
layout: provider
modified: '2026-06-13'
name: DEGIRO
nav: Providers
network: true
overview: 'DEGIRO publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Product Search API, Reporting API, config API, and 6 more. Tagged areas include Trading, Brokerage, Stocks, ETFs, and Portfolio.


  The DEGIRO catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DEGIRO''s developer surface includes authentication, support, engineering blog, status page, FAQ, and 7 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 4
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: DEGIRO API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: degiro-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.2
  delta: -13.1
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 9.8
    contract_quality: 53.4
    developer_ergonomics: 16.7
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 2.6
  previous_composite: 46.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/degiro/refs/heads/main/screenshots/degiro-2026-08-17T080852.png
security:
- kind: authentication
  name: Degiro Authentication
  slug: degiro-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Degiro Domain Security
  slug: degiro-domain-security
  summary_line: TLSv1.3 · DMARC
slug: degiro
tags:
- Trading
- Brokerage
- Stocks
- ETFs
- Portfolio
- Market Data
- Finance
website: https://www.degiro.eu
---

---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 16.5
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: REST API for financial and market data covering equities, ETFs, crypto, forex, derivatives, fundamentals, financial statements, news, economic indicators, and more. Responses in JSON/CSV; API-key auth
  name: FinancialData.Net REST API
  slug: financialdatanet-rest-api
- description: Hosted MCP server mapping the entire REST API documentation into callable MCP tools (e.g., getStockSymbols, getIncomeStatements). Advertised for ChatGPT, Claude, Cursor, and custom agents; authenticat
  name: FinancialData.Net MCP Server
  slug: financialdatanet-mcp-server
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/financialdata-net-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/financialdata-net-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/financialdata-net-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/financialdata-net-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/financialdata-net-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/financialdata-net-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/financialdata-net-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/financialdata-net-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/financialdata-net-response-examples.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/financialdata-net-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/financialdata-net-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/financialdata-net-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://financialdata.instatus.com
- group: commercial
  title: ''
  type: Plans
  url: plans/financialdata-net-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/financialdata-net-rate-limits.yml
- group: design
  title: ''
  type: Components
  url: components/financialdata-net-components.yml
- group: company
  title: ''
  type: Website
  url: https://financialdata.net
- group: start
  title: ''
  type: DeveloperPortal
  url: https://financialdata.net
- group: commercial
  title: ''
  type: Pricing
  url: https://financialdata.net/pricing
- group: start
  title: ''
  type: SignUp
  url: https://financialdata.net/sign-up
- group: start
  title: ''
  type: Login
  url: https://financialdata.net/sign-in
- group: operate
  title: ''
  type: Support
  url: https://financialdata.net/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://financialdata.net/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://financialdata.net/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://financialdata.net/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/financialdatanet
created: '2026-08-22'
description: A financial-data provider offering a single REST API (with JSON/CSV responses) covering stock, ETF, crypto, forex, and derivatives market data, company fundamentals, financial statements, news, economic indicators, insider/institutional trading, and ESG data sourced from public regulators (SEC, FINRA). Also offers a hosted MCP server, an official Python SDK, and an Excel add-in.
image: https://financialdata.net/static/images/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: FinancialData.Net MCP Server
  slug: financialdatanet-mcp-server
modified: '2026-08-22'
name: FinancialData.Net
nav: Providers
network: true
overview: 'FinancialData.Net publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include finance, financial-data, stock-market-api, market-data, and equities.


  FinancialData.Net''s developer surface includes authentication, code examples, changelog, pricing, signup flow, support, and 20 more developer resources.'
plans:
- name: Financialdata Net Plans Pricing
  plan_count: 5
  slug: financialdata-net-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Financialdata Net Rate Limits
  slug: financialdata-net-rate-limits
score:
  band: developing
  composite: 41.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 1.4
    developer_ergonomics: 33.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 50.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
security:
- kind: authentication
  name: Financialdata Net Authentication
  slug: financialdata-net-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Financialdata Net Domain Security
  slug: financialdata-net-domain-security
  summary_line: TLSv1.3 · DMARC
slug: financialdata-net
tags:
- finance
- financial-data
- stock-market-api
- market-data
- equities
- etf
- crypto
- forex
- derivatives-options
- fundamentals
- insider-trading
- institutional-13f
- esg
- economic-data
- mcp
- investing
- trading
website: https://financialdata.net
---

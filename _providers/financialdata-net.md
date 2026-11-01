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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.6
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: REST API for financial and market data covering equities, ETFs, crypto, forex, derivatives, fundamentals, financial statements, news, economic indicators, and more. Responses in JSON/CSV; API-key auth
  name: FinancialData.Net REST API
  slug: financialdatanet-rest-api
- description: Hosted MCP server mapping the entire REST API documentation into callable MCP tools (e.g., getStockSymbols, getIncomeStatements). Advertised for ChatGPT, Claude, Cursor, and custom agents; authenticat
  name: FinancialData.Net MCP Server
  slug: financialdatanet-mcp-server
artifact_total: 9
common:
- group: auth
  href: https://artifacts.apis.io/financialdata-net/security/financialdata-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/financialdata-net-domain-security.yml
- group: build
  href: https://artifacts.apis.io/financialdata-net/packages/financialdata-net-packages.yml
  title: ''
  type: Packages
  url: packages/financialdata-net-packages.yml
- group: build
  href: https://artifacts.apis.io/financialdata-net/packages/financialdata-net-packages.yml
  title: ''
  type: SDKs
  url: packages/financialdata-net-packages.yml
- group: agent
  href: https://artifacts.apis.io/financialdata-net/llms/financialdata-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/financialdata-net-llms.txt
- group: auth
  href: https://artifacts.apis.io/financialdata-net/authentication/financialdata-net-authentication.yml
  title: ''
  type: Authentication
  url: authentication/financialdata-net-authentication.yml
- group: design
  href: https://artifacts.apis.io/financialdata-net/conventions/financialdata-net-conventions.yml
  title: ''
  type: Conventions
  url: conventions/financialdata-net-conventions.yml
- group: design
  href: https://artifacts.apis.io/financialdata-net/errors/financialdata-net-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/financialdata-net-problem-types.yml
- group: design
  href: https://artifacts.apis.io/financialdata-net/data-model/financialdata-net-data-model.yml
  title: ''
  type: DataModel
  url: data-model/financialdata-net-data-model.yml
- group: build
  href: https://artifacts.apis.io/financialdata-net/examples/financialdata-net-response-examples.yml
  title: ''
  type: Examples
  url: examples/financialdata-net-response-examples.yml
- group: design
  href: https://artifacts.apis.io/financialdata-net/conformance/financialdata-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/financialdata-net-conformance.yml
- group: design
  href: https://artifacts.apis.io/financialdata-net/lifecycle/financialdata-net-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/financialdata-net-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/financialdata-net/changelog/financialdata-net-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/financialdata-net-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://financialdata.instatus.com
- group: commercial
  href: https://artifacts.apis.io/financialdata-net/plans/financialdata-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/financialdata-net-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/financialdata-net/rate-limits/financialdata-net-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/financialdata-net-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/financialdata-net/components/financialdata-net-components.yml
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
finops:
- has_sources: true
  method: derived
  name: Financialdata Net Finops
  primary_unit: subscription
  service_category: ''
  slug: financialdata-net-finops
  template: false
image: https://financialdata.net/static/images/favicon.ico
layout: provider
mcp_servers:
- description: Remote MCP server at financialdata.net over streamable HTTP requiring an API key; 86 tools listed.
  name: FinancialData.Net MCP Server
  slug: financialdata-net
modified: '2026-08-22'
name: FinancialData.Net
nav: Providers
network: true
overview: 'FinancialData.Net is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Financial Data, stock-market-api, Market Data, and Stocks.


  FinancialData.Net''s developer surface includes authentication, code examples, changelog, pricing, signup flow, support, and 20 more developer resources.'
plans:
- name: Financialdata Net Plans Pricing
  plan_count: 10
  slug: financialdata-net-plans-pricing
- name: Financialdata Net Price Estimates
  plan_count: 0
  slug: financialdata-net-price-estimates
random_paper: 11
rate_limits:
- limit_count: 5
  name: Financialdata Net Rate Limits
  slug: financialdata-net-rate-limits
score:
  band: developing
  composite: 45.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 6.5
    developer_ergonomics: 50.0
    discoverability: 65.0
    operational_transparency: 68.4
  previous_composite: 44.0
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/financialdata-net/financialdata-net-2026-09-02T145508.png
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
- Finance
- Financial Data
- stock-market-api
- Market Data
- Stocks
- ETFs
- Cryptocurrency
- Foreign Exchange
- derivatives-options
- Fundamentals
- Insider Trading
- institutional-13f
- ESG
- Economic Data
- MCP
- Investing
- Trading
website: https://financialdata.net
---

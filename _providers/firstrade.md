---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Firstrade Agentic Access
  operation_count: 24
  slug: firstrade-agentic-access
  summary_line: 24 operations · 11 acting
api_count: 6
apis:
- description: 'Access to Firstrade account data is available through the Plaid financial data aggregation platform. Plaid supports four product categories for Firstrade: Assets (consolidated balance summaries and as'
  name: Firstrade Account Data API (via Plaid)
  slug: firstrade-account-data-api-via-plaid
- description: Account list, balances, positions, and history
  name: Firstrade Account API
  slug: firstrade-account-api
- description: Session login and MFA flows
  name: Firstrade Authentication API
  slug: firstrade-authentication-api
- description: Stock quotes, OHLC chart data, and option chains
  name: Firstrade Market Data API
  slug: firstrade-market-data-api
- description: Equity and option order placement, listing, and cancellation
  name: Firstrade Orders API
  slug: firstrade-orders-api
- description: Watchlist CRUD operations
  name: Firstrade Watchlist API
  slug: firstrade-watchlist-api
artifact_total: 12
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/firstrade-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/firstrade-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/firstrade-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.firstrade.com/
- group: other
  title: ''
  type: Trading
  url: https://www.firstrade.com/trading
- group: commercial
  title: ''
  type: Pricing
  url: https://www.firstrade.com/trading/pricing
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.firstrade.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.firstrade.com/content/en-us/aboutus/privacypolicy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.firstrade.com/content/en-us/aboutus/termsofuse
- group: company
  title: ''
  type: PressCenter
  url: https://www.firstrade.com/press
- group: other
  title: ''
  type: MobileApp
  url: https://apps.apple.com/us/app/firstrade-invest-trade/id405325225
- group: other
  title: ''
  type: OpenBankingTracker
  url: https://www.openbankingtracker.com/provider/firstrade
- group: build
  title: ''
  type: PlaidIntegration
  url: https://plaid.com/institutions/firstrade/
created: '2026-06-13'
description: Firstrade Securities is a commission-free online brokerage offering trading in stocks, ETFs, options, mutual funds, and fixed income securities with no account minimums and no inactivity fees. Firstrade does not publish an official public REST API; programmatic account access is available through the Plaid financial data aggregator, which supports account balance retrieval, transaction history, investment holdings, and asset reports for Firstrade accounts. Community-developed unofficial Python SDKs also exist for session- based automation but are not affiliated with or endorsed by Firstrade.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/firstrade.png
layout: provider
modified: '2026-06-13'
name: Firstrade
nav: Providers
network: true
overview: 'Firstrade publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Account API, Authentication API, Market Data API, and 2 more. Tagged areas include Brokerage, Commission-Free Trading, Stocks, ETFs, and Options.


  Firstrade''s developer surface includes authentication, pricing, and 11 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 4
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 35.2
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 57.8
    developer_ergonomics: 15.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 35.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 25.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/firstrade/refs/heads/main/screenshots/firstrade-2026-06-20T181243.png
security:
- kind: authentication
  name: Firstrade Authentication
  slug: firstrade-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Firstrade Domain Security
  slug: firstrade-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: firstrade
tags:
- Brokerage
- Commission-Free Trading
- Stocks
- ETFs
- Options
- Mutual Funds
- Fixed Income
- Retirement
- IRA
- Investing
- Finance
- Open Banking
website: https://www.firstrade.com/
---

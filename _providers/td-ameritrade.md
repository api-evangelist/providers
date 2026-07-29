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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Td Ameritrade Agentic Access
  operation_count: 36
  slug: td-ameritrade-agentic-access
  summary_line: 36 operations · 12 acting
api_count: 15
apis:
- description: Provides REST endpoints for accessing real-time and historical market data. Includes current quotes for single and multiple symbols, historical price history for equities and ETFs, options chains with
  name: TD Ameritrade Market Data API
  slug: td-ameritrade-market-data-api
- description: Provides REST endpoints for searching and retrieving instrument details by symbol or CUSIP. Supports searching by symbol or description and retrieving fundamental data including financial ratios, earn
  name: TD Ameritrade Instruments API
  slug: td-ameritrade-instruments-api
- description: Implements OAuth 2.0 token-based authentication as described in RFC6749 section 1.3.1. Applications registered on the TD Ameritrade Developer Portal receive a Consumer Key (client_id). Access tokens a
  name: TD Ameritrade Authentication API
  slug: td-ameritrade-authentication-api
- description: Provides a WebSocket-based streaming API that delivers up-to-the-second market data including real-time Level 1 and Level 2 quotes, time and sales data for equities, options, and futures, as well as o
  name: TD Ameritrade Streaming Market Data API
  slug: td-ameritrade-streaming-market-data-api
- description: The Accounts and Trading API from TD Ameritrade — 7 operation(s) for accounts and trading.
  name: TD Ameritrade Accounts and Trading API
  slug: td-ameritrade-accounts-and-trading-api
- description: The Authentication API from TD Ameritrade — 1 operation(s) for authentication.
  name: TD Ameritrade Authentication API
  slug: td-ameritrade-authentication-api
- description: The Instruments API from TD Ameritrade — 2 operation(s) for instruments.
  name: TD Ameritrade Instruments API
  slug: td-ameritrade-instruments-api
- description: The Market Hours API from TD Ameritrade — 2 operation(s) for market hours.
  name: TD Ameritrade Market Hours API
  slug: td-ameritrade-market-hours-api
- description: The Movers API from TD Ameritrade — 1 operation(s) for movers.
  name: TD Ameritrade Movers API
  slug: td-ameritrade-movers-api
- description: The Option Chains API from TD Ameritrade — 1 operation(s) for option chains.
  name: TD Ameritrade Option Chains API
  slug: td-ameritrade-option-chains-api
- description: The Price History API from TD Ameritrade — 1 operation(s) for price history.
  name: TD Ameritrade Price History API
  slug: td-ameritrade-price-history-api
- description: The Quotes API from TD Ameritrade — 2 operation(s) for quotes.
  name: TD Ameritrade Quotes API
  slug: td-ameritrade-quotes-api
- description: The Transaction History API from TD Ameritrade — 2 operation(s) for transaction history.
  name: TD Ameritrade Transaction History API
  slug: td-ameritrade-transaction-history-api
- description: The User Info & Preferences API from TD Ameritrade — 3 operation(s) for user info & preferences.
  name: TD Ameritrade User Info & Preferences API
  slug: td-ameritrade-user-info-preferences-api
- description: The Watchlist API from TD Ameritrade — 3 operation(s) for watchlist.
  name: TD Ameritrade Watchlist API
  slug: td-ameritrade-watchlist-api
artifact_total: 26
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/td-ameritrade-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/td-ameritrade-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/td-ameritrade-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.tdameritrade.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.tdameritrade.com/content/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developer.tdameritrade.com/apis
- group: auth
  title: ''
  type: Authentication
  url: https://developer.tdameritrade.com/authentication/apis
- group: auth
  title: ''
  type: AuthenticationFAQ
  url: https://developer.tdameritrade.com/content/authentication-faq
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/td-ameritrade/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/td-ameritrade/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/td-ameritrade/refs/heads/main/finops/finops.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.tdameritrade.com/content/td-ameritrade-api-terms-use
- group: operate
  title: ''
  type: StatusPage
  url: https://developer.tdameritrade.com/content/getting-started
- group: operate
  title: ''
  type: DeprecationNotice
  url: https://blog.pickmytrade.trade/td-ameritrade-have-api-2025/
- group: docs
  title: ''
  type: MigrationGuide
  url: https://developer.schwab.com/
created: '2024-01-01'
description: TD Ameritrade was a US retail brokerage that provided REST APIs for trading equities and options, accessing streaming market data, managing brokerage accounts, and retrieving historical and real-time market data. Following the Charles Schwab acquisition, the TD Ameritrade API was shut down on May 10, 2024. Schwab has ported much of the original functionality into the Schwab Trader API.
examples:
- key_count: 1
  name: Td Ameritrade Examples
  slug: td-ameritrade-examples
finops:
- name: Finops
  service_category: ''
  slug: finops
graphqls:
- description: TD Ameritrade was a major US retail brokerage that provided REST APIs for trading equities and options, accessing streaming market data, managing brokerage accounts, and retrieving historical and real
  name: TD Ameritrade GraphQL Schema
  slug: td-ameritrade-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/td-ameritrade.png
json_schemas:
- name: TD Ameritrade API Schemas
  property_count: 0
  slug: td-ameritrade
jsonld:
- class_count: 0
  name: Td Ameritrade Context
  property_count: 0
  slug: td-ameritrade
layout: provider
modified: '2026-06-13'
name: TD Ameritrade
nav: Providers
network: true
overview: 'TD Ameritrade publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Instruments API, Authentication API, Accounts and Trading API, and 10 more. Tagged areas include Brokerage, Trading, Finance, Equities, and Options.


  The TD Ameritrade catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TD Ameritrade''s developer surface includes authentication, developer portal, getting-started guide, documentation, and 11 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 6
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: TD Ameritrade API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: td-ameritrade-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.6
  delta: -3.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.5
    developer_ergonomics: 39.1
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 15.8
  previous_composite: 51.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 45.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Td Ameritrade Authentication
  slug: td-ameritrade-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Td Ameritrade Domain Security
  slug: td-ameritrade-domain-security
  summary_line: DMARC
slug: td-ameritrade
tags:
- Brokerage
- Trading
- Finance
- Equities
- Options
- Market Data
- Streaming
website: https://developer.tdameritrade.com/
---

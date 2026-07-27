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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Td Ameritrade Holding Agentic Access
  operation_count: 34
  slug: td-ameritrade-holding-agentic-access
  summary_line: 34 operations · 11 acting
api_count: 9
apis:
- description: Account information, balances, and positions
  name: TD Ameritrade Holding Accounts API
  slug: td-ameritrade-holding-accounts-api
- description: Security and instrument search
  name: TD Ameritrade Holding Instruments API
  slug: td-ameritrade-holding-instruments-api
- description: Quotes, price history, and market hours
  name: TD Ameritrade Holding Market Data API
  slug: td-ameritrade-holding-market-data-api
- description: Options chains and derivatives
  name: TD Ameritrade Holding Options API
  slug: td-ameritrade-holding-options-api
- description: Order placement, management, and retrieval
  name: TD Ameritrade Holding Orders API
  slug: td-ameritrade-holding-orders-api
- description: Saved order management
  name: TD Ameritrade Holding Saved Orders API
  slug: td-ameritrade-holding-saved-orders-api
- description: Account transaction history
  name: TD Ameritrade Holding Transactions API
  slug: td-ameritrade-holding-transactions-api
- description: User preferences and principal data
  name: TD Ameritrade Holding User Management API
  slug: td-ameritrade-holding-user-management-api
- description: Watchlist creation and management
  name: TD Ameritrade Holding Watchlists API
  slug: td-ameritrade-holding-watchlists-api
artifact_total: 24
collections:
- collection_type: open
  name: TD Ameritrade Accounts and Trading API
  slug: open-td-ameritrade-accounts-trading
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/td-ameritrade-holding-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/td-ameritrade-holding-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/td-ameritrade-holding-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/td-ameritrade-holding-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/td-ameritrade
- group: company
  title: ''
  type: Website
  url: https://www.tdameritrade.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.tdameritrade.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.schwab.com
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/td-ameritrade-holding/refs/heads/main/openapi/td-ameritrade-accounts-trading-openapi.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/td-ameritrade-holding/refs/heads/main/vocabulary/td-ameritrade-vocabulary.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/td-ameritrade-holding/refs/heads/main/json-schema/td-ameritrade-order-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/td-ameritrade-holding/refs/heads/main/json-ld/td-ameritrade-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/td-ameritrade-holding/refs/heads/main/rules/td-ameritrade-rules.yml
- group: auth
  title: ''
  type: Authentication
  url: https://api.tdameritrade.com/v1/oauth2/token
created: '2026-03-24'
description: TD Ameritrade Holding Corporation was a brokerage firm that provided online brokerage and related services for individual investors. The company was acquired by Charles Schwab in 2020 and the TD Ameritrade platform was fully migrated to Charles Schwab in May 2024. TD Ameritrade offered a developer API for programmatic access to trading, account management, market data, and order management capabilities. The successor API is now the Charles Schwab Trader API at developer.schwab.com.
examples:
- key_count: 2
  name: Td Ameritrade Get Quotes Example
  slug: td-ameritrade-get-quotes-example
- key_count: 2
  name: Td Ameritrade Place Order Example
  slug: td-ameritrade-place-order-example
finops:
- name: Td Ameritrade Holding Finops
  service_category: API
  slug: td-ameritrade-holding-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/td-ameritrade-holding.png
json_schemas:
- name: TD Ameritrade Trade Order
  property_count: 13
  slug: td-ameritrade-order
json_structures:
- name: Td Ameritrade Order Structure
  property_count: 0
  slug: td-ameritrade-order-structure
jsonld:
- class_count: 35
  name: Td Ameritrade Context
  property_count: 0
  slug: td-ameritrade-context
layout: provider
modified: '2026-05-19'
name: TD Ameritrade Holding
nav: Providers
network: true
overview: 'TD Ameritrade Holding publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Instruments API, Market Data API, and 6 more. Tagged areas include Finance, Brokerage, Trading, Market Data, and Investment.


  The TD Ameritrade Holding catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  TD Ameritrade Holding''s developer surface includes authentication, documentation, and 12 more developer resources.'
plans:
- name: Td Ameritrade Holding Plans Pricing
  plan_count: 3
  slug: td-ameritrade-holding-plans-pricing
press:
- date: '2026-05-25'
  title: Broadridge to Acquire TD Ameritrade Retirement Plan ...
  url: https://www.broadridge.com/press-release/2019/broadridge-acquires-td-ameritrade-retirement-plan-custody-trust-assets
- date: '2026-05-25'
  title: Charles Schwab Corp. is planning to use artificial ...
  url: https://www.facebook.com/bloombergbusiness/posts/charles-schwab-corp-is-planning-to-use-artificial-intelligence-to-extend-benefit/1397432698909486/
- date: '2026-05-25'
  title: TD Ameritrade Invests in ErisX, a New Regulated ...
  url: https://www.lifehealth.com/td-ameritrade-invests-erisx-new-regulated-cryptocurrency-exchange-spot-futures-trading/
- date: '2026-05-25'
  title: TD Ameritrade Launches AI-Driven Educational Platform
  url: https://www.investopedia.com/news/td-ameritrade-launches-aidriven-educational-platform/
- date: '2026-05-25'
  title: TD Bank Financial Group - Media Room - Media Releases
  url: https://td.mediaroom.com/index.php?s=19518&%3Bitem=35847&o=965
random_paper: 61
rate_limits:
- limit_count: 5
  name: Td Ameritrade Holding Rate Limits
  slug: td-ameritrade-holding-rate-limits
rules:
- name: TD Ameritrade Holding API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: td-ameritrade-holding-jsonschema-spectral-rules
- name: TD Ameritrade Holding API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 7
  slug: td-ameritrade-rules
scopes:
- name: Td Ameritrade Holding Scopes
  scope_count: 3
  slug: td-ameritrade-holding-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 54.0
  delta: 2.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 67.5
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 31.6
  previous_composite: 51.3
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 58.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/td-ameritrade-holding/refs/heads/main/screenshots/td-ameritrade-holding-2026-06-20T194947.png
security:
- kind: authentication
  name: Td Ameritrade Holding Authentication
  slug: td-ameritrade-holding-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Td Ameritrade Holding Domain Security
  slug: td-ameritrade-holding-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: td-ameritrade-holding
tags:
- Finance
- Brokerage
- Trading
- Market Data
- Investment
- Charles Schwab
- Deprecated
- Fortune 1000
website: https://www.tdameritrade.com
---

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
  - '{''url'': ''https://www.tdameritrade.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.schwab.com/welcome-to-schwab — a different registrable domain (tdameritrade.com -> schwab.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Td Ameritrade Holding Agentic Access
  operation_count: 34
  slug: td-ameritrade-holding-agentic-access
  summary_line: 34 operations · 11 acting
api_count: 1
apis:
- baseURL: https://api.tdameritrade.com/v1
  baseurl_source: declared
  description: Account information, balances, and positions
  name: TD Ameritrade Holding Accounts API
  slug: td-ameritrade-holding-accounts-api
- baseURL: https://api.tdameritrade.com/v1
  baseurl_source: declared
  description: Security and instrument search
  name: TD Ameritrade Holding Instruments API
  slug: td-ameritrade-holding-instruments-api
- baseURL: https://api.tdameritrade.com/v1
  baseurl_source: declared
  description: Quotes, price history, and market hours
  name: TD Ameritrade Holding Market Data API
  slug: td-ameritrade-holding-market-data-api
- baseURL: https://api.tdameritrade.com/v1
  baseurl_source: declared
  description: Options chains and derivatives
  name: TD Ameritrade Holding Options API
  slug: td-ameritrade-holding-options-api
- baseURL: https://api.tdameritrade.com/v1
  baseurl_source: declared
  description: Order placement, management, and retrieval
  name: TD Ameritrade Holding Orders API
  slug: td-ameritrade-holding-orders-api
- baseURL: https://api.tdameritrade.com/v1
  baseurl_source: declared
  description: Saved order management
  name: TD Ameritrade Holding Saved Orders API
  slug: td-ameritrade-holding-saved-orders-api
- baseURL: https://api.tdameritrade.com/v1
  baseurl_source: declared
  description: Account transaction history
  name: TD Ameritrade Holding Transactions API
  slug: td-ameritrade-holding-transactions-api
- baseURL: https://api.tdameritrade.com/v1
  baseurl_source: declared
  description: User preferences and principal data
  name: TD Ameritrade Holding User Management API
  slug: td-ameritrade-holding-user-management-api
- baseURL: https://api.tdameritrade.com/v1
  baseurl_source: declared
  description: Watchlist creation and management
  name: TD Ameritrade Holding Watchlists API
  slug: td-ameritrade-holding-watchlists-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TD Ameritrade Accounts and Trading API
  slug: open-td-ameritrade-accounts-trading
- collection_type: open
  name: TD Ameritrade and Trading Accounts API
  slug: open-td-ameritrade-holding-accounts-api
- collection_type: open
  name: TD Ameritrade and Trading Accounts Instruments API
  slug: open-td-ameritrade-holding-instruments-api
- collection_type: open
  name: TD Ameritrade and Trading Accounts Market Data API
  slug: open-td-ameritrade-holding-market-data-api
- collection_type: open
  name: TD Ameritrade and Trading Accounts Options API
  slug: open-td-ameritrade-holding-options-api
- collection_type: open
  name: TD Ameritrade and Trading Accounts Orders API
  slug: open-td-ameritrade-holding-orders-api
- collection_type: open
  name: TD Ameritrade and Trading Accounts Saved Orders API
  slug: open-td-ameritrade-holding-saved-orders-api
- collection_type: open
  name: TD Ameritrade and Trading Accounts Transactions API
  slug: open-td-ameritrade-holding-transactions-api
- collection_type: open
  name: TD Ameritrade and Trading Accounts User Management API
  slug: open-td-ameritrade-holding-user-management-api
- collection_type: open
  name: TD Ameritrade and Trading Accounts Watchlists API
  slug: open-td-ameritrade-holding-watchlists-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/charles-schwab/
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


  TD Ameritrade Holding''s developer surface includes authentication, documentation, and 13 more developer resources.'
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
random_paper: 1
rate_limits:
- limit_count: 5
  name: Td Ameritrade Holding Rate Limits
  slug: td-ameritrade-holding-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: TD Ameritrade Holding API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: td-ameritrade-holding-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: TD Ameritrade Holding API Rules
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
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 19
    catalog_gap: 51.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 58.3
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 35.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 55.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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

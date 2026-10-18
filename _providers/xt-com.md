---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 31
  human_in_the_loop: 8
  name: Xt Com Agentic Access
  operation_count: 137
  slug: xt-com-agentic-access
  summary_line: 137 operations · 31 acting · 8 human-in-the-loop
api_count: 4
apis:
- description: XT.COM spot trading REST API (v4) for market data, orders, balances, deposits and withdrawals. Documented at doc.xt.com/spot; no machine-readable contract is published for it.
  name: XT.COM Spot API
  slug: spot-api
- description: Local stdio MCP server and agent skills published by XT.COM for market research and spot/futures trading from AI assistants.
  name: XT TradeKit MCP Server
  slug: tradekit-mcp
- baseURL: https://fapi.xt.com/future/market
  baseurl_source: declared
  description: Basic Error Controller
  name: XT.COM Basic Error Controller API
  slug: xt-com-basic-error-controller-api
- baseURL: https://fapi.xt.com/future/market
  baseurl_source: declared
  description: Contract Info Controller
  name: XT.COM 合约信息 API
  slug: xt-com-default-api
- baseURL: https://fapi.xt.com/future/market
  baseurl_source: declared
  description: Listen Key Controller
  name: XT.COM Listen Key API
  slug: xt-com-listenkey-api
- baseURL: https://fapi.xt.com/future/market
  baseurl_source: declared
  description: Smart Money Order Controller
  name: XT.COM 合约聪明钱 Order API
  slug: xt-com-order-api
- baseURL: https://fapi.xt.com/future/market
  baseurl_source: declared
  description: Symbol Controller
  name: XT.COM Symbol Controller API
  slug: xt-com-symbol-controller-api
- baseURL: https://fapi.xt.com/future/market
  baseurl_source: declared
  description: Symbol V 2 Controller
  name: XT.COM 获取交易对配置信息(v2) API
  slug: xt-com-v2-api
- baseURL: https://fapi.xt.com/future/market
  baseurl_source: declared
  description: Symbol V 3 Controller
  name: XT.COM 获取交易对配置信息(v3) API
  slug: xt-com-v3-api
artifact_total: 28
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/xt-com/refs/heads/main/rate-limits/xt-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/xt-com-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/xt-com/refs/heads/main/authentication/xt-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/xt-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xt-com/refs/heads/main/errors/xt-com-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/xt-com-error-codes.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/xt-com/refs/heads/main/overlays/xt-com-futures-market-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/xt-com-futures-market-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/xt-com/refs/heads/main/agentic-access/xt-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/xt-com-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xt-com/refs/heads/main/rules/xt-com-rules.yml
  title: ''
  type: Spectral
  url: rules/xt-com-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xt-com/refs/heads/main/json-ld/xt-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/xt-com-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xt-com/refs/heads/main/vocabulary/xt-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/xt-com-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xt-com/refs/heads/main/data-model/xt-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/xt-com-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xt-com/refs/heads/main/errors/xt-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/xt-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xt-com/refs/heads/main/conformance/xt-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/xt-com-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/xt-com/refs/heads/main/well-known/xt-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/xt-com-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/xt-com/refs/heads/main/hosts/xt-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/xt-com-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/xt-com/refs/heads/main/vendors/xt-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/xt-com-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/xt-com/refs/heads/main/packages/xt-com-packages.yml
  title: ''
  type: SDKs
  url: packages/xt-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/xt-com/refs/heads/main/packages/xt-com-packages.yml
  title: ''
  type: Packages
  url: packages/xt-com-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/xt-com/refs/heads/main/security/xt-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/xt-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.xt.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://doc.xt.com
- group: docs
  title: ''
  type: Documentation
  url: https://doc.xt.com
- group: start
  title: ''
  type: GettingStarted
  url: https://doc.xt.com/index/quick-start
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/XtApis
- group: company
  title: ''
  type: Blog
  url: https://www.xt.com/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.xt.com/en/price
- group: start
  title: ''
  type: SignUp
  url: https://www.xt.com/en/accounts/register
- group: start
  title: ''
  type: Login
  url: https://www.xt.com/en/accounts/login
- group: operate
  title: ''
  type: Support
  url: https://support.xt.com/hc/zh-cn
created: '2026-10-13'
description: XT.COM is a centralized cryptocurrency exchange offering spot, margin, USDT-M and coin-M futures, copy trading, earn and loan products. Its developer program at doc.xt.com documents REST and WebSocket APIs on sapi.xt.com (spot) and fapi.xt.com (futures), publishes OpenAPI 3.0 contracts for the futures market-data and user APIs in github.com/XtApis/xt-api, an official Python connector (pyxt), and a local MCP server with agent skills (XT TradeKit).
image: https://a.static-global.com/home_seo/en.jpg
json_schemas:
- name: CommonResponse«List«EventFutureConfigVO»»
  property_count: 4
  slug: xt-com-common-response-list-event-future-config-vo
- name: CommonResponse«List«SatisfactionFeedbackTypeDTO»»
  property_count: 4
  slug: xt-com-common-response-list-satisfaction-feedback-type-dto
- name: CommonResponse«List«SymbolBracketCacheDTO»»
  property_count: 4
  slug: xt-com-common-response-list-symbol-bracket-cache-dto
- name: CommonResponse«MongoPageResult«AutoDeleverageHistoryVO»»
  property_count: 4
  slug: xt-com-common-response-mongo-page-result-auto-deleverage-history-vo
- name: CommonResponse«MongoPageResult«DepositCouponDetailVO»»
  property_count: 4
  slug: xt-com-common-response-mongo-page-result-deposit-coupon-detail-vo
- name: CommonResponse«MongoPageResult«FundRateRecordDetailVO»»
  property_count: 4
  slug: xt-com-common-response-mongo-page-result-fund-rate-record-detail-vo
- name: CommonResponse«MongoPageResult«FundRateRecordVO»»
  property_count: 4
  slug: xt-com-common-response-mongo-page-result-fund-rate-record-vo
- name: CommonResponse«MongoPageResult«RiskBalanceVO»»
  property_count: 4
  slug: xt-com-common-response-mongo-page-result-risk-balance-vo
- name: ContractVO
  property_count: 25
  slug: xt-com-contract-vo
- name: OrderBookVO
  property_count: 4
  slug: xt-com-order-book-vo
- name: UserCollectionDTO
  property_count: 1
  slug: xt-com-user-collection-dto
- name: UserStepApplyDTO
  property_count: 4
  slug: xt-com-user-step-apply-dto
jsonld:
- class_count: 120
  name: Xt Com Context
  property_count: 232
  slug: xt-com-context
layout: provider
mcp_servers:
- description: 'XT.COM publishes XT TradeKit (github.com/XtApis/AItradekit, the XtApis org linked from doc.xt.com), a local Python MCP server run over stdio plus seven agent skills. No hosted/remote MCP endpoint was '
  name: XT.COM MCP Server
  slug: xt-com-mcp-yml
modified: '2026-10-13'
name: XT.COM
nav: Providers
network: true
overview: 'XT.COM publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Basic Error Controller API, 合约信息 API, Listen Key API, and 6 more. Tagged areas include Company, Cryptocurrency, Exchange, Trading, and Futures.


  The XT.COM catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  XT.COM''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, signup flow, support, and 20 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 2
  name: Xt Com Rate Limits
  slug: xt-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: XT.COM API Rules
  rule_count: 16
  severity_counts:
    error: 13
    hint: 0
    info: 2
    warn: 1
  slug: xt-com-rules
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 73.8
    catalog_earned_first_party: 8.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 22.0
    contract_quality: 54.4
    developer_ergonomics: 57.1
    discoverability: 70.0
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 15.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Xt Com Authentication
  slug: xt-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Xt Com Domain Security
  slug: xt-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: xt-com
tags:
- Company
- Cryptocurrency
- Exchange
- Trading
- Futures
- Market Data
- Blockchain
website: https://www.xt.com
---

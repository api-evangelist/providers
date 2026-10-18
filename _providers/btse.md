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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.6
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 44
  human_in_the_loop: 1
  name: Btse Agentic Access
  operation_count: 95
  slug: btse-agentic-access
  summary_line: 95 operations · 44 acting · 1 human-in-the-loop
api_count: 16
apis:
- baseURL: https://api.btse.com
  baseurl_source: declared
  description: Requires API key with Read permission
  name: BTSE Account API
  slug: btse-account-api
- baseURL: https://api.btse.com
  baseurl_source: declared
  description: Investment product endpoints
  name: BTSE Earn API
  slug: btse-earn-api
- baseURL: https://api.btse.com
  baseurl_source: declared
  description: Public market data shared by spot and futures markets
  name: BTSE Markets API
  slug: btse-markets-api
- baseURL: https://api.btse.com
  baseurl_source: declared
  description: OTC trading endpoints
  name: BTSE OTC API
  slug: btse-otc-api
- baseURL: https://api.btse.com
  baseurl_source: declared
  description: Requires API key with Trading permission
  name: BTSE Trade API
  slug: btse-trade-api
- baseURL: https://api.btse.com
  baseurl_source: declared
  description: The Trade V3 API from BTSE — 11 operation(s) for trade v3.
  name: BTSE Trade V3 API
  slug: btse-trade-v3-api
- baseURL: https://api.btse.com
  baseurl_source: declared
  description: The Trade V4 API from BTSE — 7 operation(s) for trade v4.
  name: BTSE Trade V4 API
  slug: btse-trade-v4-api
- baseURL: https://api.btse.com
  baseurl_source: declared
  description: Requires API key with Read or Transfer permission
  name: BTSE Wallet API
  slug: btse-wallet-api
artifact_total: 58
asyncapis:
- description: Futures WebSocket streams for real-time market data and private user events. **OSS Endpoint (Orderbook):** `wss://ws.btse.com/ws/oss/futures` **Main Endpoint:** `wss://ws.btse.com/ws/futures` **Testne
  name: Futures WebSocket API
  slug: btse-futures-websocket-asyncapi
- description: OTC WebSocket stream for real-time OTC quote data. **Production Endpoint:** `wss://ws.btse.com/ws/otc` **Testnet Endpoint:** `wss://testws.btse.io/ws/otc` **Authentication:** Private topics require se
  name: OTC WebSocket API
  slug: btse-otc-websocket-asyncapi
- description: 'Spot WebSocket streams for real-time market data and private user events. **OSS Endpoint (Orderbook):** `wss://ws.btse.com/ws/oss/spot` **Main Endpoint:** `wss://ws.btse.com/ws/spot` **Testnet OSS:** '
  name: Spot WebSocket API
  slug: btse-spot-websocket-asyncapi
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/btse/refs/heads/main/agentic-access/btse-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/btse-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/btse/refs/heads/main/rate-limits/btse-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/btse-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/btse/refs/heads/main/rules/btse-rules.yml
  title: ''
  type: Spectral
  url: rules/btse-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/btse/refs/heads/main/json-ld/btse-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/btse-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/btse/refs/heads/main/vocabulary/btse-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/btse-vocabulary.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/btse/refs/heads/main/asyncapi/btse-spot-websocket-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/btse-spot-websocket-asyncapi.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/btse/refs/heads/main/asyncapi/btse-otc-websocket-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/btse-otc-websocket-asyncapi.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/btse/refs/heads/main/asyncapi/btse-futures-websocket-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/btse-futures-websocket-asyncapi.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/btse/refs/heads/main/data-model/btse-data-model.yml
  title: ''
  type: DataModel
  url: data-model/btse-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/btse/refs/heads/main/changelog/btse-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/btse-changelog.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/btse/refs/heads/main/sandbox/btse-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/btse-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/btse/refs/heads/main/errors/btse-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/btse-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/btse/refs/heads/main/conformance/btse-conformance.yml
  title: ''
  type: Conformance
  url: conformance/btse-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/btse/refs/heads/main/llms/btse-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/btse-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/btse/refs/heads/main/hosts/btse-hosts.yml
  title: ''
  type: Hosts
  url: hosts/btse-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/btse/refs/heads/main/vendors/btse-vendors.yml
  title: ''
  type: Vendors
  url: vendors/btse-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.btse.com`
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/btse/refs/heads/main/authentication/btse-authentication.yml
  title: ''
  type: Authentication
  url: authentication/btse-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/btse/refs/heads/main/security/btse-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/btse-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.btse.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.btse.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.btse.com/quickstart/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.btse.com/api-explorer/markets/markets-api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/btsecom
- group: operate
  title: ''
  type: Support
  url: https://support.btse.com
- group: start
  title: ''
  type: Login
  url: https://www.btse.com/en/login
- group: start
  title: ''
  type: SignUp
  url: https://www.btse.com/en/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.btse.com/en/termsandconditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.btse.com/en/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.btse.com/spot/changelog
created: '2026-10-13'
description: BTSE is a global cryptocurrency exchange offering spot, perpetual futures, OTC, earn and wallet services. Its developer program at docs.btse.com publishes OpenAPI 3 contracts for the Markets, Spot, Futures, Wallet, Earn and OTC REST APIs, AsyncAPI contracts for its WebSocket streams, a FIX protocol interface, HMAC-SHA384 request signing, and a testnet at testapi.btse.io.
image: https://docs.btse.com/img/logo.svg
json_schemas:
- name: AccountFee
  property_count: 3
  slug: btse-account-fee
- name: AmendOrderRequest
  property_count: 8
  slug: btse-amend-order-request
- name: AmendOrderResp
  property_count: 24
  slug: btse-amend-order-resp
- name: AssetExchangeRateResponse
  property_count: 1
  slug: btse-asset-exchange-rate-response
- name: ClosePositionResp
  property_count: 20
  slug: btse-close-position-resp
- name: Conditional
  property_count: 0
  slug: btse-conditional
- name: ConvertRequest
  property_count: 3
  slug: btse-convert-request
- name: CreateAddressRequest
  property_count: 3
  slug: btse-create-address-request
- name: CreateOrderRequest
  property_count: 15
  slug: btse-create-order-request
- name: DefaultResponse
  property_count: 1
  slug: btse-default-response
- name: DepositInvestmentRequest
  property_count: 4
  slug: btse-deposit-investment-request
- name: ExchangeInfoResponse
  property_count: 0
  slug: btse-exchange-info-response
- name: FundingRateHistoryResponse
  property_count: 0
  slug: btse-funding-rate-history-response
- name: FuturesOrderResponse
  property_count: 24
  slug: btse-futures-order-response
- name: FuturesUserTrade
  property_count: 21
  slug: btse-futures-user-trade
- name: InvestmentHistoryResponse
  property_count: 4
  slug: btse-investment-history-response
- name: InvestmentOrder
  property_count: 16
  slug: btse-investment-order
- name: InvestmentProduct
  property_count: 12
  slug: btse-investment-product
- name: MarketRiskLimitArrayResponse
  property_count: 0
  slug: btse-market-risk-limit-array-response
- name: MarketsResponse
  property_count: 0
  slug: btse-markets-response
- name: OHLCVResponse
  property_count: 0
  slug: btse-ohlcvresponse
- name: OpenOrderResponse
  property_count: 26
  slug: btse-open-order-response
- name: OrderResp
  property_count: 45
  slug: btse-order-resp
- name: OrderResponse
  property_count: 29
  slug: btse-order-response
- name: OTCAcceptQuoteRequest
  property_count: 3
  slug: btse-otcaccept-quote-request
- name: OTCMarketResponse
  property_count: 0
  slug: btse-otcmarket-response
- name: OTCQuoteResponse
  property_count: 0
  slug: btse-otcquote-response
- name: OTCRequestQuoteRequest
  property_count: 6
  slug: btse-otcrequest-quote-request
- name: PlaceOrderResp
  property_count: 23
  slug: btse-place-order-resp
- name: PositionResp
  property_count: 21
  slug: btse-position-resp
- name: Position
  property_count: 21
  slug: btse-position
- name: QueryOrderResp
  property_count: 40
  slug: btse-query-order-resp
- name: QueryOrderResponse
  property_count: 27
  slug: btse-query-order-response
- name: RedeemInvestmentRequest
  property_count: 2
  slug: btse-redeem-investment-request
- name: RenewInvestmentRequest
  property_count: 2
  slug: btse-renew-investment-request
- name: Ticker24HrFullArrayResponse
  property_count: 0
  slug: btse-ticker24-hr-full-array-response
- name: TradeHistoryResp
  property_count: 17
  slug: btse-trade-history-resp
- name: TransferRequest
  property_count: 4
  slug: btse-transfer-request
- name: Twap
  property_count: 0
  slug: btse-twap
- name: UserTrade
  property_count: 10
  slug: btse-user-trade
- name: WithdrawRequest
  property_count: 7
  slug: btse-withdraw-request
jsonld:
- class_count: 120
  name: Btse Context
  property_count: 279
  slug: btse-context
layout: provider
modified: '2026-10-13'
name: BTSE
nav: Providers
network: true
overview: 'BTSE publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Earn API, Markets API, and 5 more. Tagged areas include Company, Cryptocurrency, Exchange, Trading, and Digital Assets.


  The BTSE catalog on APIs.io includes 3 event-driven AsyncAPI specifications, 1 JSON-LD context, and 1 Spectral governance ruleset.


  BTSE''s developer surface includes changelog, sandbox, authentication, documentation, getting-started guide, API reference, support, and 23 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 4
  name: Btse Rate Limits
  slug: btse-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: BTSE API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 2
  slug: btse-rules
score:
  band: strong
  composite: 55.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 77.3
    developer_ergonomics: 61.9
    discoverability: 78.6
    operational_transparency: 52.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 23.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Btse Authentication
  slug: btse-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Btse Domain Security
  slug: btse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: btse
tags:
- Company
- Cryptocurrency
- Exchange
- Trading
- Digital Assets
- Futures
- WebSocket
website: https://www.btse.com
---

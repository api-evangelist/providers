---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.0
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Bigone Agentic Access
  operation_count: 50
  slug: bigone-agentic-access
  summary_line: 50 operations · 13 acting
api_count: 10
apis:
- description: Real-time spot market data and private order/account streams at wss://api.big.one/ws/v2 (JSON or protobuf messages, defined in the published websocket.proto), plus contract streams at wss://api.big.on
  name: BigONE WebSocket API
  slug: bigone-websocket-api
- baseURL: https://api.big.one/api/v3
  baseurl_source: declared
  description: Account Balance
  name: BigONE Account API
  slug: bigone-account-api
- baseURL: https://api.big.one/api/v3
  baseurl_source: declared
  description: Wallet Assets
  name: BigONE Asset API
  slug: bigone-asset-api
- baseURL: https://api.big.one/api/v3
  baseurl_source: declared
  description: Asset information
  name: BigONE Assets API
  slug: bigone-assets-api
- baseURL: https://api.big.one/api/v3
  baseurl_source: declared
  description: Wallet Deposits
  name: BigONE Deposit API
  slug: bigone-deposit-api
- baseURL: https://api.big.one/api/v3
  baseurl_source: declared
  description: Funding Account Balances
  name: BigONE Funding Account API
  slug: bigone-funding-account-api
- baseURL: https://api.big.one/api/v3
  baseurl_source: declared
  description: Public Market Data
  name: BigONE Market Data API
  slug: bigone-market-data-api
- baseURL: https://api.big.one/api/v3
  baseurl_source: declared
  description: Order Management
  name: BigONE Order API
  slug: bigone-order-api
- baseURL: https://api.big.one/api/v3
  baseurl_source: declared
  description: The Ping API from BigONE — 1 operation(s) for ping.
  name: BigONE Ping API
  slug: bigone-ping-api
- baseURL: https://api.big.one/api/v3
  baseurl_source: declared
  description: Position Management
  name: BigONE Position API
  slug: bigone-position-api
- baseURL: https://api.big.one/api/v3
  baseurl_source: declared
  description: Get quotes for conversion
  name: BigONE Quote API
  slug: bigone-quote-api
- baseURL: https://api.big.one/api/v3
  baseurl_source: declared
  description: Trading range limits
  name: BigONE Ranges API
  slug: bigone-ranges-api
- baseURL: https://api.big.one/api/v3
  baseurl_source: declared
  description: Trade History
  name: BigONE Trade API
  slug: bigone-trade-api
- baseURL: https://api.big.one/api/v3
  baseurl_source: declared
  description: Execute and manage trades
  name: BigONE Trades API
  slug: bigone-trades-api
- baseURL: https://api.big.one/api/v3
  baseurl_source: declared
  description: Wallet Transfers
  name: BigONE Transfer API
  slug: bigone-transfer-api
- baseURL: https://api.big.one/api/v3
  baseurl_source: declared
  description: Wallet Withdrawals
  name: BigONE Withdrawal API
  slug: bigone-withdrawal-api
artifact_total: 44
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bigone/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bigone/refs/heads/main/overlays/bigone-contract-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bigone-contract-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bigone/refs/heads/main/agentic-access/bigone-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bigone-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bigone/refs/heads/main/rate-limits/bigone-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bigone-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bigone/refs/heads/main/rules/bigone-rules.yml
  title: ''
  type: Spectral
  url: rules/bigone-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bigone/refs/heads/main/json-ld/bigone-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bigone-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bigone/refs/heads/main/vocabulary/bigone-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bigone-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bigone/refs/heads/main/data-model/bigone-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bigone-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bigone/refs/heads/main/changelog/bigone-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bigone-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bigone/refs/heads/main/conventions/bigone-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/bigone-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bigone/refs/heads/main/conventions/bigone-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bigone-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bigone/refs/heads/main/errors/bigone-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/bigone-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bigone/refs/heads/main/errors/bigone-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bigone-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bigone/refs/heads/main/conformance/bigone-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bigone-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bigone/refs/heads/main/hosts/bigone-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bigone-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bigone/refs/heads/main/vendors/bigone-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bigone-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bigone/refs/heads/main/packages/bigone-packages.yml
  title: ''
  type: SDKs
  url: packages/bigone-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bigone/refs/heads/main/packages/bigone-packages.yml
  title: ''
  type: Packages
  url: packages/bigone-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bigone/refs/heads/main/authentication/bigone-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bigone-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bigone/refs/heads/main/security/bigone-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bigone-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://big.one
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.big.one/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://open.big.one/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://open.big.one/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://open.big.one/docs/authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://open.big.one/docs/general-info
- group: design
  title: ''
  type: ErrorCodes
  url: https://open.big.one/docs/error-codes
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bigone-eng
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/bigone-eng/openapi-specs
- group: operate
  title: ''
  type: Support
  url: https://t.me/bigapi
- group: other
  title: ''
  type: X
  url: https://x.com/BigONEexchange
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@BigONEExchange
created: '2026-10-13'
description: BigONE is a cryptocurrency exchange (big.one) offering spot trading, contract (perpetual futures) trading, instant convert (flash swap) and wallet services. Its developer program at open.big.one documents four REST APIs on api.big.one (Spot v3, Wallet v3, Convert sapi v1 and Contract v2), JWT (HS256) authentication, and WebSocket streams, and publishes the OpenAPI definitions in the bigone-eng/openapi-specs GitHub repository and the WebSocket protobuf in bigone-eng/websocket-proto.
image: https://b.peatio.com/logos/favicon.ico
json_schemas:
- name: Account
  property_count: 2
  slug: bigone-account
- name: AssetPair
  property_count: 8
  slug: bigone-asset-pair
- name: Asset
  property_count: 8
  slug: bigone-asset
- name: Candle
  property_count: 6
  slug: bigone-candle
- name: ConvertAsset
  property_count: 2
  slug: bigone-convert-asset
- name: ConvertQuote
  property_count: 10
  slug: bigone-convert-quote
- name: ConvertRange
  property_count: 4
  slug: bigone-convert-range
- name: ConvertTrade
  property_count: 10
  slug: bigone-convert-trade
- name: CreateOrderBody
  property_count: 10
  slug: bigone-create-order-body
- name: CreateTradeRequest
  property_count: 2
  slug: bigone-create-trade-request
- name: CreateTransferBody
  property_count: 7
  slug: bigone-create-transfer-body
- name: CreateWithdrawalBody
  property_count: 7
  slug: bigone-create-withdrawal-body
- name: Deposit
  property_count: 12
  slug: bigone-deposit
- name: Instrument
  property_count: 18
  slug: bigone-instrument
- name: Order
  property_count: 16
  slug: bigone-order
- name: PlaceOrderRequest
  property_count: 6
  slug: bigone-place-order-request
- name: Position
  property_count: 30
  slug: bigone-position
- name: Ticker
  property_count: 9
  slug: bigone-ticker
- name: Trade
  property_count: 13
  slug: bigone-trade
- name: TransferInfo
  property_count: 6
  slug: bigone-transfer-info
- name: UserTrade
  property_count: 12
  slug: bigone-user-trade
- name: Withdrawal
  property_count: 14
  slug: bigone-withdrawal
jsonld:
- class_count: 41
  name: Bigone Context
  property_count: 161
  slug: bigone-context
layout: provider
modified: '2026-10-13'
name: BigONE
nav: Providers
network: true
overview: 'BigONE publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Asset API, Assets API, and 13 more. Tagged areas include Company, Cryptocurrency, Exchange, Trading, and Derivatives.


  The BigONE catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BigONE''s developer surface includes changelog, authentication, documentation, getting-started guide, support, YouTube channel, and 26 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 2
  name: Bigone Rate Limits
  slug: bigone-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: BigONE API Rules
  rule_count: 12
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 2
  slug: bigone-rules
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 73.8
    catalog_earned_first_party: 8.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 62.2
    developer_ergonomics: 56.5
    discoverability: 71.4
    operational_transparency: 42.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
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
  name: Bigone Authentication
  slug: bigone-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bigone Domain Security
  slug: bigone-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bigone
tags:
- Company
- Cryptocurrency
- Exchange
- Trading
- Derivatives
- Wallets
- Market Data
website: https://big.one
---

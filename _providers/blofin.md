---
agent_readiness:
  band: agent-ready
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
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.7
  scored_at: '2026-10-17'
api_count: 11
apis:
- description: OAuth-based broker API at oauth.blofin.com for brokers to obtain tokens and user info, create API keys on a user's behalf and query deposit addresses and status. Its operations are in the generated Bl
  name: BloFin Broker API
  slug: blofin-broker-api
- description: Public and private WebSocket channels for futures (wss://openapi.blofin.com/ws/public, /ws/private), spot (/ws/spot/public, /ws/spot/private) and copy trading (/ws/copytrading/private); demo equivalen
  name: BloFin WebSocket API
  slug: blofin-websocket-api
- baseURL: https://openapi.blofin.com
  baseurl_source: declared
  description: The Account API from BloFin — 12 operation(s) for account.
  name: BloFin Account API
  slug: blofin-account-api
- baseURL: https://openapi.blofin.com
  baseurl_source: declared
  description: The Affiliate API from BloFin — 6 operation(s) for affiliate.
  name: BloFin Affiliate API
  slug: blofin-affiliate-api
- baseURL: https://openapi.blofin.com
  baseurl_source: declared
  description: The Asset API from BloFin — 9 operation(s) for asset.
  name: BloFin Asset API
  slug: blofin-asset-api
- baseURL: https://openapi.blofin.com
  baseurl_source: declared
  description: The Copytrading API from BloFin — 23 operation(s) for copytrading.
  name: BloFin Copytrading API
  slug: blofin-copytrading-api
- baseURL: https://openapi.blofin.com
  baseurl_source: declared
  description: The Market API from BloFin — 12 operation(s) for market.
  name: BloFin Market API
  slug: blofin-market-api
- baseURL: https://openapi.blofin.com
  baseurl_source: declared
  description: The Oauth API from BloFin — 6 operation(s) for oauth.
  name: BloFin OAuth API
  slug: blofin-oauth-api
- baseURL: https://openapi.blofin.com
  baseurl_source: declared
  description: The Spot API from BloFin — 18 operation(s) for spot.
  name: BloFin Spot API
  slug: blofin-spot-api
- baseURL: https://openapi.blofin.com
  baseurl_source: declared
  description: The Trade API from BloFin — 23 operation(s) for trade.
  name: BloFin Trade API
  slug: blofin-trade-api
- baseURL: https://openapi.blofin.com
  baseurl_source: declared
  description: The User API from BloFin — 1 operation(s) for user.
  name: BloFin User API
  slug: blofin-user-api
artifact_total: 24
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/blofin/refs/heads/main/rate-limits/blofin-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/blofin-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blofin/refs/heads/main/rules/blofin-rules.yml
  title: ''
  type: Spectral
  url: rules/blofin-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blofin/refs/heads/main/json-ld/blofin-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/blofin-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blofin/refs/heads/main/vocabulary/blofin-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/blofin-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blofin/refs/heads/main/data-model/blofin-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blofin-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/blofin/refs/heads/main/cli/blofin-cli.yml
  title: ''
  type: CLI
  url: cli/blofin-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/blofin/refs/heads/main/changelog/blofin-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/blofin-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blofin/refs/heads/main/conventions/blofin-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/blofin-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blofin/refs/heads/main/conventions/blofin-conventions.yml
  title: ''
  type: Conventions
  url: conventions/blofin-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/blofin/refs/heads/main/sandbox/blofin-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/blofin-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blofin/refs/heads/main/authentication/blofin-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blofin-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blofin/refs/heads/main/lifecycle/blofin-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/blofin-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blofin/refs/heads/main/errors/blofin-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/blofin-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blofin/refs/heads/main/conformance/blofin-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blofin-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blofin/refs/heads/main/llms/blofin-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blofin-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blofin/refs/heads/main/mcp/blofin-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/blofin-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blofin/refs/heads/main/well-known/blofin-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blofin-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blofin/refs/heads/main/hosts/blofin-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blofin-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blofin/refs/heads/main/vendors/blofin-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blofin-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/blofin/refs/heads/main/packages/blofin-packages.yml
  title: ''
  type: SDKs
  url: packages/blofin-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/blofin/refs/heads/main/packages/blofin-packages.yml
  title: ''
  type: Packages
  url: packages/blofin-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blofin/refs/heads/main/security/blofin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blofin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blofin.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blofin.com/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.blofin.com/index.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.blofin.com/changelog.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blofin
- group: operate
  title: ''
  type: Support
  url: https://support.blofin.com/hc/en-us
created: '2026-10-13'
description: 'BloFin is a cryptocurrency exchange offering spot, perpetual futures and copy trading. Its public Open API (base https://openapi.blofin.com, demo https://demo-trading-openapi.blofin.com) exposes REST endpoints for public market data, account, trading, asset management, affiliate and copy trading, plus public and private WebSocket channels, authenticated with ACCESS-KEY / ACCESS-SIGN HMAC-signed headers; a separate OAuth broker API runs at oauth.blofin.com. BloFin also publishes an official MCP server (blofin-mcp), an agent-first CLI (blofin-cli), a Python SDK and an agent skills hub on GitHub. Surfaced via the API Evangelist harvest backlog (source: market-gap:crypto-exchanges).'
image: https://s2.blofin.com/icons/blofin/favicon-v2.ico
json_schemas:
- name: GetApiV1AffiliateInviteesResponse
  property_count: 21
  slug: blofin-get-api-v1-affiliate-invitees-response
- name: GetApiV1CopytradingTradeOrdersPendingResponse
  property_count: 21
  slug: blofin-get-api-v1-copytrading-trade-orders-pending-response
- name: GetApiV1TradeOrdersHistoryResponse
  property_count: 31
  slug: blofin-get-api-v1-trade-orders-history-response
- name: PostApiV1TradeBatchOrdersRequest
  property_count: 17
  slug: blofin-post-api-v1-trade-batch-orders-request
- name: PostApiV1TradeOrderRequest
  property_count: 16
  slug: blofin-post-api-v1-trade-order-request
- name: PostApiV1TradeOrderTpslRequest
  property_count: 15
  slug: blofin-post-api-v1-trade-order-tpsl-request
jsonld:
- class_count: 120
  name: Blofin Context
  property_count: 244
  slug: blofin-context
layout: provider
mcp_servers:
- description: Official MCP server for the BloFin exchange API (market data, account, trading, asset management), documented at https://docs.blofin.com/index.html#mcp-server.
  name: BloFin MCP Server
  slug: blofin-mcp-server
modified: '2026-10-13'
name: BloFin
nav: Providers
network: true
overview: 'BloFin is listed with 11 APIs on the [APIs.io](https://apis.io/) network, including Account API, Affiliate API, Asset API, and 8 more. Tagged areas include Company, Cryptocurrency, Cryptocurrency Exchange, Trading, and Futures.


  The BloFin catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BloFin''s developer surface includes CLI, changelog, sandbox, authentication, documentation, API reference, support, and 21 more developer resources.'
plans:
- name: Blofin Plans Pricing
  plan_count: 0
  slug: blofin-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 4
  name: Blofin Rate Limits
  slug: blofin-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: BloFin API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 3
  slug: blofin-rules
score:
  band: thin
  composite: 34.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 25.9
    developer_ergonomics: 54.8
    discoverability: 76.7
    operational_transparency: 52.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 10
      marker_coverage: 100.0
      total: 10
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 21.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Blofin Authentication
  slug: blofin-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Blofin Domain Security
  slug: blofin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blofin
tags:
- Company
- Cryptocurrency
- Cryptocurrency Exchange
- Trading
- Futures
- Spot Trading
- Copy Trading
- WebSocket
website: https://blofin.com
---

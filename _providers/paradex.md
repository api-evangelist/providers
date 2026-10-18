---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: platform
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 51
  human_in_the_loop: 3
  name: Paradex Agentic Access
  operation_count: 133
  slug: paradex-agentic-access
  summary_line: 133 operations · 51 acting · 3 human-in-the-loop
api_count: 2
apis:
- baseURL: wss://ws.api.prod.paradex.trade/v1
  baseurl_source: declared
  description: JSON-RPC over WebSocket channels for real-time market data, order book, trades, fills, orders, positions and account updates.
  name: Paradex WebSocket API
  slug: paradex-websocket-api
- description: Paradex-hosted public remote MCP server exposing market and vault data tools to AI clients; also distributed as the mcp-paradex Python package.
  name: Paradex MCP Server
  slug: paradex-mcp-server
- baseURL: https://api.prod.paradex.trade/v1
  baseurl_source: declared
  description: The Account API from Paradex — 25 operation(s) for account.
  name: Paradex Account API
  slug: paradex-account-api
- baseURL: https://api.prod.paradex.trade/v1
  baseurl_source: declared
  description: The Algos API from Paradex — 3 operation(s) for algos.
  name: Paradex Algos API
  slug: paradex-algos-api
- baseURL: https://api.prod.paradex.trade/v1
  baseurl_source: declared
  description: The Authentication API from Paradex — 5 operation(s) for authentication.
  name: Paradex Authentication API
  slug: paradex-authentication-api
- baseURL: https://api.prod.paradex.trade/v1
  baseurl_source: declared
  description: The BlockTrades API from Paradex — 6 operation(s) for blocktrades.
  name: Paradex Block Trades API
  slug: paradex-blocktrades-api
- baseURL: https://api.prod.paradex.trade/v1
  baseurl_source: declared
  description: The Insurance API from Paradex — 1 operation(s) for insurance.
  name: Paradex Insurance API
  slug: paradex-insurance-api
- baseURL: https://api.prod.paradex.trade/v1
  baseurl_source: declared
  description: The Liquidations API from Paradex — 1 operation(s) for liquidations.
  name: Paradex Liquidations API
  slug: paradex-liquidations-api
- baseURL: https://api.prod.paradex.trade/v1
  baseurl_source: declared
  description: The MarketMakerProtection API from Paradex — 3 operation(s) for marketmakerprotection.
  name: Paradex Market Maker Protection API
  slug: paradex-marketmakerprotection-api
- baseURL: https://api.prod.paradex.trade/v1
  baseurl_source: declared
  description: The Markets API from Paradex — 11 operation(s) for markets.
  name: Paradex Markets API
  slug: paradex-markets-api
- baseURL: https://api.prod.paradex.trade/v1
  baseurl_source: declared
  description: The Orders API from Paradex — 5 operation(s) for orders.
  name: Paradex Orders API
  slug: paradex-orders-api
- baseURL: https://api.prod.paradex.trade/v1
  baseurl_source: declared
  description: The Referrals API from Paradex — 2 operation(s) for referrals.
  name: Paradex Referrals API
  slug: paradex-referrals-api
- baseURL: https://api.prod.paradex.trade/v1
  baseurl_source: declared
  description: The Rfqs API from Paradex — 9 operation(s) for rfqs.
  name: Paradex Rfqs API
  slug: paradex-rfqs-api
- baseURL: https://api.prod.paradex.trade/v1
  baseurl_source: declared
  description: The Staking API from Paradex — 5 operation(s) for staking.
  name: Paradex Staking API
  slug: paradex-staking-api
- baseURL: https://api.prod.paradex.trade/v1
  baseurl_source: declared
  description: The Subkey API from Paradex — 5 operation(s) for subkey.
  name: Paradex Subkey API
  slug: paradex-subkey-api
- baseURL: https://api.prod.paradex.trade/v1
  baseurl_source: declared
  description: The System API from Paradex — 7 operation(s) for system.
  name: Paradex System API
  slug: paradex-system-api
- baseURL: https://api.prod.paradex.trade/v1
  baseurl_source: declared
  description: The Token API from Paradex — 4 operation(s) for token.
  name: Paradex Token API
  slug: paradex-token-api
- baseURL: https://api.prod.paradex.trade/v1
  baseurl_source: declared
  description: The Trades API from Paradex — 1 operation(s) for trades.
  name: Paradex Trades API
  slug: paradex-trades-api
- baseURL: https://api.prod.paradex.trade/v1
  baseurl_source: declared
  description: The Transfers API from Paradex — 1 operation(s) for transfers.
  name: Paradex Transfers API
  slug: paradex-transfers-api
- baseURL: https://api.prod.paradex.trade/v1
  baseurl_source: declared
  description: The Vaults API from Paradex — 10 operation(s) for vaults.
  name: Paradex Vaults API
  slug: paradex-vaults-api
- baseURL: https://api.prod.paradex.trade/v1
  baseurl_source: declared
  description: The XPTransfersV2 API from Paradex — 6 operation(s) for xptransfersv2.
  name: Paradex XP Transfers V2 API
  slug: paradex-xptransfersv2-api
artifact_total: 35
asyncapis:
- description: 'Channels for real-time updates. Public market data channels are delivered as SBE binary frames. Negotiate the encoding with the sbeSchemaId and sbeSchemaVersion query parameters: wss://ws.api.prod.par'
  name: WebSocket channels
  slug: paradex-websocket-asyncapi
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/paradex/refs/heads/main/agentic-access/paradex-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/paradex-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/paradex/refs/heads/main/rate-limits/paradex-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/paradex-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paradex/refs/heads/main/rules/paradex-rules.yml
  title: ''
  type: Spectral
  url: rules/paradex-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paradex/refs/heads/main/json-ld/paradex-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/paradex-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paradex/refs/heads/main/vocabulary/paradex-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/paradex-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paradex/refs/heads/main/data-model/paradex-data-model.yml
  title: ''
  type: DataModel
  url: data-model/paradex-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paradex/refs/heads/main/errors/paradex-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/paradex-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paradex/refs/heads/main/conformance/paradex-conformance.yml
  title: ''
  type: Conformance
  url: conformance/paradex-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/paradex/refs/heads/main/llms/paradex-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/paradex-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/paradex/refs/heads/main/mcp/paradex-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/paradex-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/paradex/refs/heads/main/mcp/paradex-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/paradex-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/paradex/refs/heads/main/well-known/paradex-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/paradex-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/paradex/refs/heads/main/hosts/paradex-hosts.yml
  title: ''
  type: Hosts
  url: hosts/paradex-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/paradex/refs/heads/main/vendors/paradex-vendors.yml
  title: ''
  type: Vendors
  url: vendors/paradex-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/paradex/refs/heads/main/packages/paradex-packages.yml
  title: ''
  type: SDKs
  url: packages/paradex-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/paradex/refs/heads/main/packages/paradex-packages.yml
  title: ''
  type: Packages
  url: packages/paradex-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/paradex/refs/heads/main/authentication/paradex-authentication.yml
  title: ''
  type: Authentication
  url: authentication/paradex-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/paradex/refs/heads/main/security/paradex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/paradex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.paradex.trade
- group: docs
  title: ''
  type: Documentation
  url: https://docs.paradex.trade/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.paradex.trade/docs/getting-started/what-is-paradex
- group: docs
  title: ''
  type: APIReference
  url: https://docs.paradex.trade/api/general-information/api-quick-start
- group: company
  title: ''
  type: Blog
  url: https://www.paradex.trade/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.paradex.trade/releases/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tradeparadex
- group: start
  title: ''
  type: Login
  url: https://app.paradex.trade/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.paradex.trade/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.paradex.trade/terms-of-service
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.paradex.trade/trading/trading-fees
- group: operate
  title: ''
  type: StatusPage
  url: https://status.paradex.trade
created: '2026-10-13'
description: Paradex is a perpetual futures decentralized exchange (perp DEX) built on its own Starknet appchain, offering zero-fee trading of crypto, equities, FX and commodity perpetuals and options. It exposes a public REST API, a WebSocket API described in AsyncAPI, official Python and TypeScript SDKs, and hosted MCP servers for AI agents.
image: https://cdn.prod.website-files.com/632b1650d518e93de132751a/67dc06a9c7c21f316cefbf02_og%20--%20home-prdx%20-%20new.webp
json_schemas:
- name: responses.MarketResp
  property_count: 34
  slug: paradex-responses-market-resp
- name: responses.MarketSummaryResp
  property_count: 26
  slug: paradex-responses-market-summary-resp
- name: responses.OrderResp
  property_count: 23
  slug: paradex-responses-order-resp
- name: responses.SystemConfigResponse
  property_count: 25
  slug: paradex-responses-system-config-response
- name: responses.TransferResult
  property_count: 20
  slug: paradex-responses-transfer-result
- name: responses.VaultSummaryResp
  property_count: 27
  slug: paradex-responses-vault-summary-resp
jsonld:
- class_count: 120
  name: Paradex Context
  property_count: 366
  slug: paradex-context
layout: provider
mcp_servers:
- description: Paradex hosts a public remote MCP server at https://mcp.paradex.trade/mcp (no API key, market and vault data). The same server is published as the open-source Python package mcp-paradex for local stdi
  name: Paradex MCP Server
  slug: paradex-mcp-server
modified: '2026-10-13'
name: Paradex
nav: Providers
network: true
overview: 'Paradex publishes 21 API contracts indexed on the [APIs.io](https://apis.io/) network, including WebSocket API, Account API, Algos API, and 18 more. Tagged areas include Company, Cryptocurrency, Exchange, Derivatives, and Trading.


  The Paradex catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Paradex''s developer surface includes authentication, documentation, getting-started guide, API reference, engineering blog, changelog, pricing, and 23 more developer resources.'
random_paper: 15
rate_limits:
- limit_count: 5
  name: Paradex Rate Limits
  slug: paradex-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Paradex API Rules
  rule_count: 13
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 6
  slug: paradex-rules
score:
  band: strong
  composite: 56.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 64.5
    developer_ergonomics: 50.0
    discoverability: 75.0
    operational_transparency: 68.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 23.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 22.2
security:
- kind: authentication
  name: Paradex Authentication
  slug: paradex-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Paradex Domain Security
  slug: paradex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: paradex
tags:
- Company
- Cryptocurrency
- Exchange
- Derivatives
- Trading
- Perpetual Futures
- DeFi
- WebSocket
- MCP
website: https://www.paradex.trade
---

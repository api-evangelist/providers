---
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.4
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Blockchain.Com Agentic Access
  operation_count: 35
  slug: blockchain.com-agentic-access
  summary_line: 35 operations · 5 acting
api_count: 3
apis:
- description: Real-time WebSocket gateway for the Blockchain.com Exchange. Anonymous channels stream heartbeat, L2/L3 order books, prices, symbols, ticker and trades; authenticated channels cover auth, balances and
  name: Blockchain.com Exchange WebSocket API
  slug: blockchaincom-exchange-websocket-api
- description: Free JSON API over the Blockchain.com Explorer data set — single blocks, transactions, addresses, unspent outputs, block height and latest block queries for Bitcoin.
  name: Blockchain Data API
  slug: blockchain-data-api
- description: Plain-text query API returning single values for blockchain statistics such as block count, difficulty, hash rate, total bitcoins in circulation, market cap and address balances.
  name: Blockchain.com Simple Query API
  slug: blockchaincom-simple-query-api
- description: Ticker and currency-conversion API returning bitcoin exchange rates across major fiat currencies, aggregated from the major exchanges.
  name: Blockchain.com Exchange Rates API
  slug: blockchaincom-exchange-rates-api
- description: JSON/CSV feed behind the Blockchain.com charts and stats pages — per-chart time series, network statistics, and mining pool distribution.
  name: Blockchain.com Charts and Statistics API
  slug: blockchaincom-charts-and-statistics-api
- description: Low-latency streaming socket channel providing notifications on new bitcoin blocks, unconfirmed transactions and watched addresses via the unconfirmed_sub, blocks_sub and addr_sub subscription operati
  name: Blockchain.com Explorer WebSocket API
  slug: blockchaincom-explorer-websocket-api
- description: Public backend service for NFT market data, returning NFT assets owned by an address and individual asset lookups by network, contract address and token id. Publishes a Swagger 2.0 definition at its d
  name: Blockchain.com NFT Market API
  slug: blockchaincom-nft-market-api
- description: OAuth 2.0 resource gateway that lets a third-party app read a consenting user's Blockchain.com custodial wallet data. Two endpoints are documented — transaction history (scope read_transactions, up to
  name: Blockchain.com OAuth Resources API
  slug: blockchaincom-oauth-resources-api
- description: Open-source Wallet API service (service-my-wallet-v3) that runs locally and exposes HTTP endpoints for creating wallets, sending payments, and checking balances against Blockchain.com wallets, plus th
  name: Blockchain.com Wallet API
  slug: blockchaincom-wallet-api
- description: Available currencies, regions, and payment methods for the partner account.
  name: Blockchain.com Eligibility API
  slug: blockchain.com-eligibility-api
- description: The nft API from Blockchain.com — 1 operation(s) for nft.
  name: Blockchain.com Nft API
  slug: blockchain.com-nft-api
- description: The nft_v2 API from Blockchain.com — 2 operation(s) for nft_v2.
  name: Blockchain.com Nft V2 API
  slug: blockchain.com-nft-v2-api
- description: Order listing and lookup.
  name: Blockchain.com Orders API
  slug: blockchain.com-orders-api
- description: Get account status and initiate deposits and withdrawals
  name: Blockchain.com Payments API
  slug: blockchain.com-payments-api
- description: The Public API from Blockchain.com — 3 operation(s) for public.
  name: Blockchain.com Public API
  slug: blockchain.com-public-api
- description: Real-time buy quotes.
  name: Blockchain.com Quote API
  slug: blockchain.com-quote-api
- description: Post orders and get information about historical trades
  name: Blockchain.com Trading API
  slug: blockchain.com-trading-api
- description: Retrieve current prices and markets
  name: Blockchain.com Unauthenticated API
  slug: blockchain.com-unauthenticated-api
artifact_total: 37
asyncapis:
- description: ''
  name: Blockchain.Com Event Surface
  slug: blockchain.com-event-surface
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Blockchain.com Pay Partner Eligibility API
  slug: open-blockchain
- collection_type: open
  name: Market Nft API
  slug: open-blockchain
- collection_type: open
  name: NFT Market Nft V2 API
  slug: open-blockchain
- collection_type: open
  name: Blockchain.com Pay Partner Orders API
  slug: open-blockchain
- collection_type: open
  name: Blockchain.com Exchange REST Payments API
  slug: open-blockchain
- collection_type: open
  name: NFT Market Public API
  slug: open-blockchain
- collection_type: open
  name: Blockchain.com Pay Partner Quote API
  slug: open-blockchain
- collection_type: open
  name: Blockchain.com Exchange REST Trading API
  slug: open-blockchain
- collection_type: open
  name: Blockchain.com Exchange REST Unauthenticated API
  slug: open-blockchain
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/blockchain.com-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/blockchain.com-exchange-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/blockchain.com-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/blockchain.com-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/blockchain.com-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/blockchain.com-security.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/blockchain.com-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/blockchain.com-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/blockchain.com-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.blockchain.com/legal/licenses
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/blockchain.com-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/blockchain.com-data-model.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/blockchain.com-scopes.yml
- group: design
  title: ''
  type: Components
  url: components/blockchain.com-components.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/blockchain.com-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/blockchain.com-event-surface.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/blockchain.com-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/blockchain.com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blockchain.com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/blockchain.com-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.blockchain.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.blockchain.com/explorer/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blockchain.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.blockchain.com/v3/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.blockchain.com/pay/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.blockchain.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blockchain
- group: commercial
  title: ''
  type: Pricing
  url: https://www.blockchain.com/prices
- group: start
  title: ''
  type: SignUp
  url: https://login.blockchain.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blockchain.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blockchain.com/legal/privacy
- group: operate
  title: ''
  type: Support
  url: https://support.blockchain.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.blockchain.com/
- group: auth
  title: ''
  type: Security
  url: https://www.blockchain.com/.well-known/security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/blockchain.com-llms.txt
created: '2026-08-02'
description: Blockchain.com is a cryptocurrency financial services company that operates the Blockchain.com Explorer (one of the longest-running Bitcoin block explorers), a self-custody and custodial wallet, an institutional spot exchange, and Blockchain.com Pay, an embeddable fiat-to-crypto on-ramp and off-ramp for partners. Its public API surface spans the Exchange REST API (market data, trading, deposits and withdrawals, authenticated with an X-API-Token header), a FIX-named WebSocket trading and market-data gateway, the Pay Partner API (eligibility, quotes and orders, authenticated with public and private API key headers plus order webhooks), the free Blockchain Data, Simple Query, Exchange Rates and Charts & Statistics APIs on blockchain.info, a real-time blockchain WebSocket notification stream, an NFT Market API, and the open-source Wallet API service (service-my-wallet-v3) with first-party client libraries for Python, Node.js, Ruby, PHP and Java.
image: https://www.blockchain.com/static/apple-touch-icon.png
json_schemas:
- name: Blockchain.Com Pay Webhook Event
  property_count: 0
  slug: blockchain.com-pay-webhook-event
layout: provider
mcp_servers:
- description: ''
  name: Blockchain.com MCP Server
  slug: blockchaincom-mcp-server
modified: '2026-08-02'
name: Blockchain.com
nav: Providers
network: true
overview: 'Blockchain.com publishes 10 APIs on the [APIs.io](https://apis.io/) network, including NFT Market API, Eligibility API, Nft API, and 7 more. Tagged areas include cryptocurrency, bitcoin, Blockchain, exchange, and Trading.


  The Blockchain.com catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Blockchain.com''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 29 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 2
  name: Blockchain.Com Rate Limits
  slug: blockchain.com-rate-limits
scopes:
- name: Blockchain.Com Scopes
  scope_count: 2
  slug: blockchain.com-scopes
  summary_line: 2 scopes
score:
  band: strong
  composite: 57.2
  coverage:
    artifact_dirs: 23
    catalog_gap: 61.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 4.5
    contract_quality: 58.4
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 52.6
  previous_composite: 57.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 71.9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blockchain.com/refs/heads/main/screenshots/blockchain.com-2026-08-07T162627.png
security:
- kind: authentication
  name: Blockchain.Com Authentication
  slug: blockchain.com-authentication
  summary_line: apiKey/oauth2 · 5 schemes
- kind: domain-security
  name: Blockchain.Com Domain Security
  slug: blockchain.com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Blockchain.Com Vulnerability Disclosure
  slug: blockchain.com-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: blockchain.com
tags:
- cryptocurrency
- bitcoin
- Blockchain
- exchange
- Trading
- Market Data
- Payments
- on-ramp
- Wallets
- block-explorer
- Fintech
- Webhook
website: https://www.blockchain.com/
---

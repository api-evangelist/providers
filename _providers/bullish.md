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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 29
  human_in_the_loop: 3
  name: Bullish Agentic Access
  operation_count: 94
  slug: bullish-agentic-access
  summary_line: 94 operations · 29 acting · 3 human-in-the-loop
api_count: 1
apis:
- description: A separately published OpenAPI document carrying the 15 operations Bullish has deprecated or decommissioned — the v1 order create/cancel/get surface, v1 AMM instructions, v1 spot account reads and the
  name: Bullish Deprecated Features and APIs
  slug: deprecated-api
- description: AsyncAPI 3.0.0 document for simultaneous subscriptions to multiple L1 and L2 order books across different Bullish markets over WebSocket.
  name: Bullish WebSocket Multi-Order Book API
  slug: ws-orderbook
- description: AsyncAPI 3.0.0 document for batched anonymous trade subscriptions across multiple Bullish markets over WebSocket.
  name: Bullish WebSocket Anonymous Trades API
  slug: ws-trades
- description: AsyncAPI 3.0.0 document for simultaneous tick subscriptions across multiple Bullish markets over WebSocket.
  name: Bullish WebSocket Anonymous Ticks API
  slug: ws-ticks
- description: AsyncAPI 3.0.0 document for the real-time auction feed, delivering phase and order-imbalance data for Bullish markets with auctions enabled.
  name: Bullish WebSocket Auction Feed API
  slug: ws-auction
- description: AsyncAPI 3.0.0 document for streaming Bullish index prices, with the subscribed asset set controlled by subscription-message parameters.
  name: Bullish WebSocket Index Data API
  slug: ws-index-data
- description: AsyncAPI 3.0.0 document for the authenticated private stream — real-time orders, trades, asset accounts, trading accounts, derivatives positions, AMM instructions and market-maker-protection triggers.
  name: Bullish WebSocket Private Data API
  slug: ws-private-data
- description: The Bullish FIX order-entry, drop-copy, reference-data and trading-status surface for institutional and high-frequency clients, with session management and component definitions documented. Rejections
  name: Bullish FIX API
  slug: fix-api
- description: A small non-authenticated REST surface publishing aggregated public market data — tickers with 24-hour rolling statistics, order books, and the last 100 trades, each optionally filtered by market type
  name: Bullish Aggregator API
  slug: aggregator-api
- description: Authenticated APIs for reading account data
  name: Bullish Account Assets API
  slug: bullish-account-assets-api
- description: Authenticated APIs that allow users to Create, View and Terminate AMM instructions. Please refer to the [AMM instruction Overview Doc](https://github.com/bullish-exchange/api-docs/wiki/Automated-Marke
  name: Bullish Amm Instructions API
  slug: bullish-amm-instructions-api
- description: Non-authenticated APIs for accessing general asset data information
  name: Bullish Asset Data API
  slug: bullish-asset-data-api
- description: The auction-public API from Bullish — 2 operation(s) for auction-public.
  name: Bullish Auction Public API
  slug: bullish-auction-public-api
- description: Authenticated API for submitting commands into the exchange.
  name: Bullish command entry API
  slug: bullish-command-entry-api
- description: Authenticated APIs for custody, [Custody Basic Examples](https://github.com/bullish-exchange/api-examples/blob/master/bullish/rest/custody_basics.py) Custody APIs have a limit of 40 requests per IP, p
  name: Bullish Custody API
  slug: bullish-custody-api
- description: List of deprecated APIs that will be removed towards the end of Q3 2024.
  name: Bullish deprecated - q3 2024 API
  slug: bullish-deprecated-q3-2024-api
- description: The derivatives API from Bullish — 1 operation(s) for derivatives.
  name: Bullish Derivatives API
  slug: bullish-derivatives-api
- description: The derivatives-public API from Bullish — 3 operation(s) for derivatives-public.
  name: Bullish Derivatives Public API
  slug: bullish-derivatives-public-api
- description: The general API from Bullish — 2 operation(s) for general.
  name: Bullish General API
  slug: bullish-general-api
- description: The history API from Bullish — 5 operation(s) for history.
  name: Bullish History API
  slug: bullish-history-api
- description: The Inter-dealer Broker (IDB) API is available to authorized inter-dealer brokers to book OTC trades on Bullish on behalf of their respective end customers.
  name: Bullish Idb API
  slug: bullish-idb-api
- description: The index-price-data API from Bullish — 2 operation(s) for index-price-data.
  name: Bullish Index Price Data API
  slug: bullish-index-price-data-api
- description: Non-authenticated APIs for accessing general market data information
  name: Bullish Market Data API
  slug: bullish-market-data-api
- description: The market-history-data API from Bullish — 4 operation(s) for market-history-data.
  name: Bullish Market History Data API
  slug: bullish-market-history-data-api
- description: The market-maker-protection API from Bullish — 1 operation(s) for market-maker-protection.
  name: Bullish Market Maker Protection API
  slug: bullish-market-maker-protection-api
- description: Authenticated APIs for interacting with orders
  name: Bullish Orders API
  slug: bullish-orders-api
- description: The OTC Clearing Facility API (OTC API) is available to customers to book trades negotiated outside of the Bullish Exchange order book to Bullish's clearing and settlement platform. Customers may agre
  name: Bullish Otc API
  slug: bullish-otc-api
- description: The portfolio-margin-simulator API from Bullish — 2 operation(s) for portfolio-margin-simulator.
  name: Bullish Portfolio Margin Simulator API
  slug: bullish-portfolio-margin-simulator-api
- description: The session-management API from Bullish — 3 operation(s) for session-management.
  name: Bullish Session Management API
  slug: bullish-session-management-api
- description: Authenticated APIs for reading trade data
  name: Bullish Trades API
  slug: bullish-trades-api
- description: The trading-accounts API from Bullish — 2 operation(s) for trading-accounts.
  name: Bullish Trading Accounts API
  slug: bullish-trading-accounts-api
- description: Authenticated API for initiating asset transfers between trading accounts.
  name: Bullish Transfer API
  slug: bullish-transfer-api
artifact_total: 70
asyncapis:
- description: 'The Auction Feed provides real-time auction data for markets with auctions enabled. Two topics are available: - `noii` - Net Order Imbalance Indicator (NOII) updates. Available during the Lockdown pha'
  name: Auction Feed
  slug: bullish-ws-auction-asyncapi
- description: The index price of different assets to be subscribed are controlled by the parameters in the subscription message listed below. ``` /trading-api/v1/index-data ```
  name: Index Data
  slug: bullish-ws-index-data-asyncapi
- description: This allows simultaneous subscriptions to multiple L1 and L2 order books of different markets. The order books of different markets to be subscribed are controlled by the parameters in the subscriptio
  name: Multi-Order Book
  slug: bullish-ws-orderbook-asyncapi
- description: All private data updates are realtime. Multiple topics and multiple accounts can be subscribed to within a single connection. A default subscribed trading account can be pre-specified by using this en
  name: Private Data
  slug: bullish-ws-private-data-asyncapi
- description: 'This allows simultaneous tick subscriptions to multiple markets. Upon subscribing to a market, the client will first receive a snapshot of latest ticker, followed by updates. See the data model: [Get '
  name: Anonymous Ticks
  slug: bullish-ws-ticks-asyncapi
- description: This allows simultaneous trade subscriptions to multiple markets. Additionally, instead of sending trades one by one, trades are sent in batches. Upon subscribing to a market, the client will first re
  name: Anonymous Trades
  slug: bullish-ws-trades-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bullish Trading Account Assets API
  slug: open-bullish-account-assets-api
- collection_type: open
  name: Bullish Trading Amm Instructions API
  slug: open-bullish-amm-instructions-api
- collection_type: open
  name: Bullish Trading Asset Data API
  slug: open-bullish-asset-data-api
- collection_type: open
  name: Bullish Trading Auction Public API
  slug: open-bullish-auction-public-api
- collection_type: open
  name: Bullish Trading command entry API
  slug: open-bullish-command-entry-api
- collection_type: open
  name: Bullish Trading Custody API
  slug: open-bullish-custody-api
- collection_type: open
  name: Bullish Features Deprecated API
  slug: open-bullish-deprecated-api
- collection_type: open
  name: Bullish Deprecated Features deprecated - q3 2024 API
  slug: open-bullish-deprecated-q3-2024-api
- collection_type: open
  name: Bullish Trading Derivatives API
  slug: open-bullish-derivatives-api
- collection_type: open
  name: Bullish Trading Derivatives Public API
  slug: open-bullish-derivatives-public-api
- collection_type: open
  name: Bullish Trading General API
  slug: open-bullish-general-api
- collection_type: open
  name: Bullish Trading History API
  slug: open-bullish-history-api
- collection_type: open
  name: Bullish Trading Idb API
  slug: open-bullish-idb-api
- collection_type: open
  name: Bullish Trading Index Price Data API
  slug: open-bullish-index-price-data-api
- collection_type: open
  name: Bullish Trading Market Data API
  slug: open-bullish-market-data-api
- collection_type: open
  name: Bullish Trading Market History Data API
  slug: open-bullish-market-history-data-api
- collection_type: open
  name: Bullish Trading Market Maker Protection API
  slug: open-bullish-market-maker-protection-api
- collection_type: open
  name: Bullish Trading Orders API
  slug: open-bullish-orders-api
- collection_type: open
  name: Bullish Trading Otc API
  slug: open-bullish-otc-api
- collection_type: open
  name: Bullish Trading Portfolio Margin Simulator API
  slug: open-bullish-portfolio-margin-simulator-api
- collection_type: open
  name: Bullish Trading Session Management API
  slug: open-bullish-session-management-api
- collection_type: open
  name: Bullish Trading Trades API
  slug: open-bullish-trades-api
- collection_type: open
  name: Bullish Trading Trading Accounts API
  slug: open-bullish-trading-accounts-api
- collection_type: open
  name: Bullish Trading Transfer API
  slug: open-bullish-transfer-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/bullish-capability-edges.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bullish-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bullish-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bullish-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bullish.com/us/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.exchange.bullish.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.exchange.bullish.com/rest/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.exchange.bullish.com/rest/api/get-markets
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.exchange.bullish.com/rest/introduction
- group: auth
  title: ''
  type: Authentication
  url: authentication/bullish-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/bullish-trading-api-openapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/bullish-ws-private-data-asyncapi.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bullish-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bullish-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bullish.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.exchange.bullish.com/rest/deprecated/bullish-deprecated-features-apis
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bullish-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bullish-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bullish-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/bullish-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bullish-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bullish-exchange
- group: operate
  title: ''
  type: Support
  url: https://support.exchange.bullish.com/servicedesk/customer/portals
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.bullish.com
- group: commercial
  title: ''
  type: Pricing
  url: https://support.exchange.bullish.com/servicedesk/customer/portal/1/article/9373547
- group: start
  title: ''
  type: SignUp
  url: https://exchange.bullish.com/register/sign-up
- group: start
  title: ''
  type: Login
  url: https://exchange.bullish.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bullish.com/us/site-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bullish.com/us/legal-us
- group: company
  title: ''
  type: Blog
  url: https://www.bullish.com/us/news-insights
- group: auth
  title: ''
  type: Security
  url: https://www.bullish.com/us/bug-bounty-program
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.bullish.com/us/trust
- group: auth
  title: ''
  type: Compliance
  url: https://www.bullish.com/us/trust
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bullish-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bullish-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bullish-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bullish-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bullish-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/bullish-trading-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-08'
description: 'Bullish is an institutional digital-asset exchange and custodian operating a regulated spot, perpetual, dated-futures and options venue with an integrated automated market maker, deterministic central limit order book matching, and qualified custody. It publishes a genuinely machine-readable API estate: a 79-operation OpenAPI 3.0.3 Trading API covering markets, orders, trades, AMM instructions, derivatives positions, portfolio-margin simulation, OTC and inter-dealer-broker booking, custody deposits and withdrawals, and history; six AsyncAPI 3.0.0 WebSocket documents for order book, trades, ticks, auction, index and private account data; and a FIX 4.2/5.0 order-entry and drop-copy surface. Authentication is JWT bearer minted from a client-signed ECDSA R1 or HMAC login rather than OAuth. Bullish is licensed or registered with the Gibraltar Financial Services Commission, BaFin (MiCA CASP and qualified crypto custodian), the Hong Kong SFC, FinCEN and NYDFS, and lists on the NYSE
  as BLSH.'
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Bullish MCP Server
  slug: bullish-mcp-server
modified: '2026-08-08'
name: Bullish
nav: Providers
network: true
overview: 'Bullish publishes 30 APIs on the [APIs.io](https://apis.io/) network, including Deprecated Features and APIs, WebSocket Multi-Order Book API, WebSocket Anonymous Trades API, and 27 more. Tagged areas include Digital Assets, Cryptocurrency, Exchange, Trading, and Derivatives.


  The Bullish catalog on APIs.io includes 6 event-driven AsyncAPI specifications.


  Bullish''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, pricing, and 33 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 5
  name: Bullish Rate Limits
  slug: bullish-rate-limits
score:
  band: strong
  composite: 66.0
  coverage:
    artifact_dirs: 23
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 63.2
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 84.2
  previous_composite: 66.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 73.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bullish/refs/heads/main/screenshots/bullish-2026-08-17T080736.png
security:
- kind: authentication
  name: Bullish Authentication
  slug: bullish-authentication
  summary_line: http/custom-signed-login · 1 scheme
- kind: domain-security
  name: Bullish Domain Security
  slug: bullish-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bullish Vulnerability Disclosure
  slug: bullish-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Bullish Trust Center
  slug: bullish-trust-center
  summary_line: SOC 1 Type 1, SOC 2 Type 1
slug: bullish
tags:
- Digital Assets
- Cryptocurrency
- Exchange
- Trading
- Derivatives
- Custody
- Market Data
- Financial-Services
- Institutional
- FIX
website: https://www.bullish.com/us/
---

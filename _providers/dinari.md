---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.7
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Dinari Agentic Access
  operation_count: 61
  slug: dinari-agentic-access
  summary_line: 61 operations · 21 acting
api_count: 10
apis:
- description: '**`Accounts` represent the financial accounts of an `Entity`.** `Orders`, dividends, and other transactions are associated with an `Account`.'
  name: Dinari Accounts API
  slug: dinari-accounts-api
- description: '**Corporate actions are events that affect the ownership of a `Stock`.** Corporate actions include dividends and stock splits.'
  name: Dinari Corporate Actions API
  slug: dinari-corporate-actions-api
- description: '**`Entities` represent a business or organization that uses the API, and their customers.** Dinari Partners are represented as an organization `Entity` in the API, with their own accounts. Individual '
  name: Dinari Entities API
  slug: dinari-entities-api
- description: '**KYC (Know Your Customer) is a process of verifying the identity of customer `Entities`.** KYC is required for all customer `Entities` that transact on Dinari''s platform. Dinari provides a managed KY'
  name: Dinari KYC API
  slug: dinari-kyc-api
- description: '**Managed `Orders` represent the buying and selling of assets using a Dinari-managed `Wallet`.** Similar to Proxied `Orders`, placing a managed `Order` creates an `OrderRequest` which is then submitte'
  name: Dinari Managed Orders API
  slug: dinari-managed-orders-api
- description: '**Dinari provides basic market data for `Stocks` and `Alloys` that are available to transact on.** This data is provided on a best-effort basis and we recommend using a dedicated provider for more int'
  name: Dinari Market Data API
  slug: dinari-market-data-api
- description: '**`Order Requests` represent requests for Dinari to create `Orders` on behalf of an `Account`.** `Order Requests` are created when placing **proxied orders** or **managed orders**. See their respectiv'
  name: Dinari Order Requests API
  slug: dinari-order-requests-api
- description: '**`Orders` represent the buying and selling of assets under an `Account`.** For `Accounts` using self-custodied `Wallets`, `Orders` are created and fulfilled by making calls to Dinari''s smart contract'
  name: Dinari Orders API
  slug: dinari-orders-api
- description: '**`Wallets` represent the blockchain wallet that holds the assets of an `Account`.** An `Account` may be connected to a single `Wallet`. Individual `Entities` can connect their self-custodied `Wallets'
  name: Dinari Wallets API
  slug: dinari-wallets-api
- description: '**`Withdrawals` represent the transfer of stablecoins from an `Account` connected to a managed `Wallet` to another `Account` that is owned by the `Entity`.** Since the `Account` is backed by a managed'
  name: Dinari Withdrawals API
  slug: dinari-withdrawals-api
arazzos:
- description: Fetch a wallet-connection nonce, connect the wallet, fund the account via the sandbox faucet, and read the portfolio.
  name: Connect a wallet and fund an account
  slug: dinari-connect-wallet-and-fund
- description: Create an entity, run KYC, open an account, find a stock, and place a managed market buy.
  name: Onboard a customer and place a dShare order
  slug: dinari-onboard-and-trade
artifact_total: 39
asyncapis:
- description: Real-time market data and order updates over WebSocket. Clients authenticate with their API key + secret, then subscribe to market data (Level 2 order book, DFN quotes) and/or order data for their cus
  name: Dinari Streaming (WebSocket) API
  slug: dinari-streaming-asyncapi
collections:
- collection_type: postman
  name: Dinari Enterprise Accounts API
  slug: postman-dinari-accounts-api
- collection_type: postman
  name: Dinari Enterprise Accounts Corporate Actions API
  slug: postman-dinari-corporate-actions-api
- collection_type: postman
  name: Dinari Enterprise Accounts Entities API
  slug: postman-dinari-entities-api
- collection_type: postman
  name: Dinari Enterprise Accounts KYC API
  slug: postman-dinari-kyc-api
- collection_type: postman
  name: Dinari Enterprise Accounts Managed Orders API
  slug: postman-dinari-managed-orders-api
- collection_type: postman
  name: Dinari Enterprise Accounts Market Data API
  slug: postman-dinari-market-data-api
- collection_type: postman
  name: Dinari Enterprise Accounts Order Requests API
  slug: postman-dinari-order-requests-api
- collection_type: postman
  name: Dinari Enterprise Accounts Orders API
  slug: postman-dinari-orders-api
- collection_type: postman
  name: Dinari Enterprise Accounts Wallets API
  slug: postman-dinari-wallets-api
- collection_type: postman
  name: Dinari Enterprise Accounts Withdrawals API
  slug: postman-dinari-withdrawals-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dinari Enterprise Accounts API
  slug: open-dinari-accounts-api
- collection_type: open
  name: Dinari Enterprise Accounts Corporate Actions API
  slug: open-dinari-corporate-actions-api
- collection_type: open
  name: Dinari Enterprise Accounts Entities API
  slug: open-dinari-entities-api
- collection_type: open
  name: Dinari Enterprise Accounts KYC API
  slug: open-dinari-kyc-api
- collection_type: open
  name: Dinari Enterprise Accounts Managed Orders API
  slug: open-dinari-managed-orders-api
- collection_type: open
  name: Dinari Enterprise Accounts Market Data API
  slug: open-dinari-market-data-api
- collection_type: open
  name: Dinari Enterprise Accounts Order Requests API
  slug: open-dinari-order-requests-api
- collection_type: open
  name: Dinari Enterprise Accounts Orders API
  slug: open-dinari-orders-api
- collection_type: open
  name: Dinari Enterprise Accounts Wallets API
  slug: open-dinari-wallets-api
- collection_type: open
  name: Dinari Enterprise Accounts Withdrawals API
  slug: open-dinari-withdrawals-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/dinari/overview
- group: company
  title: ''
  type: Website
  url: https://dinari.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://partners.dinari.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dinari.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dinari.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dinari.com/docs/quickstart
- group: company
  title: ''
  type: Blog
  url: https://dinari.com/blog
- group: operate
  title: ''
  type: Support
  url: https://dinari.com/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dinaricrypto
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.dinari.com/docs/fees
- group: start
  title: ''
  type: SignUp
  url: https://partners.dinari.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dinari.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dinari.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dinari.com
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.dinari.com/docs/deprecations
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.dinari.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dinari-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/dinari-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dinari-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dinari-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dinari-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/dinari-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/dinari-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dinari-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dinari-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dinari-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dinari-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/dinari-sandbox.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/dinari-streaming-asyncapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dinari-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dinari-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dinari-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.dinari.com/docs/security
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dinari-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dinari-onboard-and-trade.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dinari-connect-wallet-and-fund.yml
created: '2026-07-17'
description: Dinari provides tokenized US stocks and ETFs (dShares) backed 1:1 by real securities, giving businesses an API to offer global customers regulated access to over a hundred equities and index tokens across 85+ jurisdictions. The Dinari Enterprise API covers entity onboarding and KYC/KYB, brokerage account management, market data (prices, quotes, splits, dividends, news), managed and on-chain (EIP-155 permit) order requests, order fulfillment, blockchain wallet connection, token transfers, withdrawals, and a USD+ stablecoin for dividend payments. dShares settle on-chain across Arbitrum One, HyperEVM, and Avalanche C-Chain. Surfaced as a portfolio company of 500 Global and Version One Ventures and enriched into the API Evangelist network.
image: https://cdn.prod.website-files.com/656fd13bce08f2dc3bc50573/6a2b7f71ca32dba392e2c452_dinari-og-2026.jpg
layout: provider
mcp_servers:
- description: ''
  name: Dinari MCP Server
  slug: dinari-mcp-server
modified: '2026-07-18'
name: Dinari
nav: Providers
network: true
overview: 'Dinari publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Corporate Actions API, Entities API, and 7 more. Tagged areas include Company, Tokenized Securities, Stocks, ETFs, and Brokerage.


  The Dinari catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Dinari''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 30 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 49.9
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 16.7
    contract_quality: 67.3
    developer_ergonomics: 54.2
    discoverability: 74.1
    governance: 16.7
    operational_transparency: 39.5
  previous_composite: 49.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dinari/refs/heads/main/screenshots/dinari-2026-07-25T212044.png
security:
- kind: authentication
  name: Dinari Authentication
  slug: dinari-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Dinari Domain Security
  slug: dinari-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dinari Vulnerability Disclosure
  slug: dinari-vulnerability-disclosure
  summary_line: contact published
slug: dinari
tags:
- Company
- Tokenized Securities
- Stocks
- ETFs
- Brokerage
- Market Data
- Blockchain
- Stablecoins
- Fintech
- KYC
- Order
- Wallets
website: https://dinari.com
---

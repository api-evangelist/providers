---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Dinari Agentic Access
  operation_count: 61
  slug: dinari-agentic-access
  summary_line: 61 operations · 21 acting
api_count: 1
apis:
- baseURL: https://api-enterprise.sbt.dinari.com/api/v2
  baseurl_source: declared
  description: '**`Accounts` represent the financial accounts of an `Entity`.** `Orders`, dividends, and other transactions are associated with an `Account`.'
  name: Dinari Accounts API
  slug: dinari-accounts-api
- baseURL: https://api-enterprise.sbt.dinari.com/api/v2
  baseurl_source: declared
  description: '**Corporate actions are events that affect the ownership of a `Stock`.** Corporate actions include dividends and stock splits.'
  name: Dinari Corporate Actions API
  slug: dinari-corporate-actions-api
- baseURL: https://api-enterprise.sbt.dinari.com/api/v2
  baseurl_source: declared
  description: '**`Entities` represent a business or organization that uses the API, and their customers.** Dinari Partners are represented as an organization `Entity` in the API, with their own accounts. Individual '
  name: Dinari Entities API
  slug: dinari-entities-api
- baseURL: https://api-enterprise.sbt.dinari.com/api/v2
  baseurl_source: declared
  description: '**KYC (Know Your Customer) is a process of verifying the identity of customer `Entities`.** KYC is required for all customer `Entities` that transact on Dinari''s platform. Dinari provides a managed KY'
  name: Dinari KYC API
  slug: dinari-kyc-api
- baseURL: https://api-enterprise.sbt.dinari.com/api/v2
  baseurl_source: declared
  description: '**Managed `Orders` represent the buying and selling of assets using a Dinari-managed `Wallet`.** Similar to Proxied `Orders`, placing a managed `Order` creates an `OrderRequest` which is then submitte'
  name: Dinari Managed Orders API
  slug: dinari-managed-orders-api
- baseURL: https://api-enterprise.sbt.dinari.com/api/v2
  baseurl_source: declared
  description: '**Dinari provides basic market data for `Stocks` and `Alloys` that are available to transact on.** This data is provided on a best-effort basis and we recommend using a dedicated provider for more int'
  name: Dinari Market Data API
  slug: dinari-market-data-api
- baseURL: https://api-enterprise.sbt.dinari.com/api/v2
  baseurl_source: declared
  description: '**`Order Requests` represent requests for Dinari to create `Orders` on behalf of an `Account`.** `Order Requests` are created when placing **proxied orders** or **managed orders**. See their respectiv'
  name: Dinari Order Requests API
  slug: dinari-order-requests-api
- baseURL: https://api-enterprise.sbt.dinari.com/api/v2
  baseurl_source: declared
  description: '**`Orders` represent the buying and selling of assets under an `Account`.** For `Accounts` using self-custodied `Wallets`, `Orders` are created and fulfilled by making calls to Dinari''s smart contract'
  name: Dinari Orders API
  slug: dinari-orders-api
- baseURL: https://api-enterprise.sbt.dinari.com/api/v2
  baseurl_source: declared
  description: '**`Wallets` represent the blockchain wallet that holds the assets of an `Account`.** An `Account` may be connected to a single `Wallet`. Individual `Entities` can connect their self-custodied `Wallets'
  name: Dinari Wallets API
  slug: dinari-wallets-api
- baseURL: https://api-enterprise.sbt.dinari.com/api/v2
  baseurl_source: declared
  description: '**`Withdrawals` represent the transfer of stablecoins from an `Account` connected to a managed `Wallet` to another `Account` that is owned by the `Entity`.** Since the `Account` is backed by a managed'
  name: Dinari Withdrawals API
  slug: dinari-withdrawals-api
arazzos:
- description: Fetch a wallet-connection nonce, connect the wallet, fund the account via the sandbox faucet, and read the portfolio.
  name: Connect a wallet and fund an account
  slug: dinari-connect-wallet-and-fund
- description: Create an entity, run KYC, open an account, find a stock, and place a managed market buy.
  name: Onboard a customer and place a dShare order
  slug: dinari-onboard-and-trade
artifact_total: 44
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
- group: commercial
  href: https://artifacts.apis.io/dinari/plans/dinari-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dinari-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/dinari/capabilities/dinari-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/dinari-capability-edges.yml
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
  href: https://artifacts.apis.io/dinari/changelog/dinari-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dinari-changelog.yml
- group: build
  href: https://artifacts.apis.io/dinari/packages/dinari-packages.yml
  title: ''
  type: Packages
  url: packages/dinari-packages.yml
- group: build
  href: https://artifacts.apis.io/dinari/packages/dinari-packages.yml
  title: ''
  type: SDKs
  url: packages/dinari-packages.yml
- group: agent
  href: https://artifacts.apis.io/dinari/mcp/dinari-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/dinari-mcp.yml
- group: agent
  href: https://artifacts.apis.io/dinari/llms/dinari-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dinari-llms.txt
- group: other
  href: https://artifacts.apis.io/dinari/overlays/dinari-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dinari-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/dinari/conformance/dinari-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dinari-conformance.yml
- group: design
  href: https://artifacts.apis.io/dinari/errors/dinari-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/dinari-error-codes.yml
- group: design
  href: https://artifacts.apis.io/dinari/lifecycle/dinari-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dinari-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/dinari/conventions/dinari-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dinari-conventions.yml
- group: design
  href: https://artifacts.apis.io/dinari/data-model/dinari-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dinari-data-model.yml
- group: start
  href: https://artifacts.apis.io/dinari/sandbox/dinari-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/dinari-sandbox.yml
- group: docs
  href: https://artifacts.apis.io/dinari/asyncapi/dinari-streaming-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/dinari-streaming-asyncapi.yml
- group: auth
  href: https://artifacts.apis.io/dinari/authentication/dinari-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dinari-authentication.yml
- group: auth
  href: https://artifacts.apis.io/dinari/security/dinari-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dinari-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/dinari/security/dinari-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dinari-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.dinari.com/docs/security
- group: agent
  href: https://artifacts.apis.io/dinari/agentic-access/dinari-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dinari-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/dinari/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dinari/arazzo/dinari-onboard-and-trade.yml
  title: ''
  type: Arazzo
  url: arazzo/dinari-onboard-and-trade.yml
- group: design
  href: https://artifacts.apis.io/dinari/arazzo/dinari-connect-wallet-and-fund.yml
  title: ''
  type: Arazzo
  url: arazzo/dinari-connect-wallet-and-fund.yml
created: '2026-07-17'
description: Dinari provides tokenized US stocks and ETFs (dShares) backed 1:1 by real securities, giving businesses an API to offer global customers regulated access to over a hundred equities and index tokens across 85+ jurisdictions. The Dinari Enterprise API covers entity onboarding and KYC/KYB, brokerage account management, market data (prices, quotes, splits, dividends, news), managed and on-chain (EIP-155 permit) order requests, order fulfillment, blockchain wallet connection, token transfers, withdrawals, and a USD+ stablecoin for dividend payments. dShares settle on-chain across Arbitrum One, HyperEVM, and Avalanche C-Chain. Surfaced as a portfolio company of 500 Global and Version One Ventures and enriched into the API Evangelist network.
finops:
- has_sources: true
  method: derived
  name: Dinari Finops
  primary_unit: api access
  service_category: ''
  slug: dinari-finops
  template: false
image: https://cdn.prod.website-files.com/656fd13bce08f2dc3bc50573/6a2b7f71ca32dba392e2c452_dinari-og-2026.jpg
layout: provider
modified: '2026-07-18'
name: Dinari
nav: Providers
network: true
overview: 'Dinari publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Corporate Actions API, Entities API, and 7 more. Tagged areas include Company, Tokenized Securities, Stocks, ETFs, and Brokerage.


  The Dinari catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Dinari''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 32 more developer resources.'
plans:
- name: Dinari Plans Pricing
  plan_count: 5
  slug: dinari-plans-pricing
- name: Dinari Price Estimates
  plan_count: 0
  slug: dinari-price-estimates
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: Dinari API Rules
  rule_count: 66
  severity_counts:
    error: 59
    hint: 0
    info: 1
    warn: 6
  slug: dinari-rules
score:
  band: strong
  composite: 64.6
  coverage:
    artifact_dirs: 31
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 10.2
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 60.6
    developer_ergonomics: 74.4
    discoverability: 73.2
    operational_transparency: 52.6
  previous_composite: 54.4
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
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/dinari/dinari-2026-07-25T212044.png
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
skill_count: 3
skills:
- name: Connect a wallet and fund a Dinari account
  slug: dinari-connect-wallet-and-fund
- name: Onboard a Dinari entity (KYC) and open an account
  slug: dinari-onboard-entity
- name: Place a managed dShare order
  slug: dinari-place-managed-order
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
- Real-Time
- Financial Services
website: https://dinari.com
---

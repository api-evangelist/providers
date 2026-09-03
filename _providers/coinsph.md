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
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 63
  human_in_the_loop: 0
  name: Coinsph Agentic Access
  operation_count: 113
  slug: coinsph-agentic-access
  summary_line: 113 operations · 63 acting
api_count: 11
apis:
- baseURL: https://api.pro.coins.ph
  baseurl_source: declared
  description: Account management APIs.
  name: Coins.ph Account API
  slug: coinsph-account-api
- baseURL: https://api.pro.coins.ph
  baseurl_source: declared
  description: The Account Validation API from Coins.ph — 2 operation(s) for account validation.
  name: Coins.ph Account Validation API
  slug: coinsph-account-validation-api
- baseURL: https://api.pro.coins.ph
  baseurl_source: declared
  description: Checkout creation and management
  name: Coins.ph Checkout API
  slug: coinsph-checkout-api
- baseURL: https://api.pro.coins.ph
  baseurl_source: declared
  description: Checkout refund operations
  name: Coins.ph Checkout Refund API
  slug: coinsph-checkout-refund-api
- baseURL: https://api.pro.coins.ph
  baseurl_source: declared
  description: Crypto deposit address
  name: Coins.ph Collections - Crypto API
  slug: coinsph-collections-crypto-api
- baseURL: https://api.pro.coins.ph
  baseurl_source: declared
  description: QRPH code generation and management
  name: Coins.ph Collections - QRPH API
  slug: coinsph-collections-qrph-api
- baseURL: https://api.pro.coins.ph
  baseurl_source: declared
  description: Convert quote and acceptance operations.
  name: Coins.ph Convert API
  slug: coinsph-convert-api
- baseURL: https://api.pro.coins.ph
  baseurl_source: declared
  description: Cash-out and disbursement operations
  name: Coins.ph Disbursements API
  slug: coinsph-disbursements-api
- baseURL: https://api.pro.coins.ph
  baseurl_source: declared
  description: General endpoints for connectivity, server time, system status, and user IP.
  name: Coins.ph General API
  slug: coinsph-general-api
- baseURL: https://api.pro.coins.ph
  baseurl_source: declared
  description: Manage user data stream listenKeys for WebSocket connections. A listenKey is required to establish a private WebSocket connection for receiving real-time account updates (orders, balances, positions).
  name: Coins.ph Listens API
  slug: coinsph-listens-api
- baseURL: https://api.pro.coins.ph
  baseurl_source: declared
  description: Market data APIs.
  name: Coins.ph Markets API
  slug: coinsph-markets-api
- baseURL: https://api.pro.coins.ph
  baseurl_source: declared
  description: Fiat-to-crypto and crypto-to-fiat ramp operations
  name: Coins.ph ON/OFF Ramp API
  slug: coinsph-on-off-ramp-api
- baseURL: https://api.pro.coins.ph
  baseurl_source: declared
  description: Order history and details
  name: Coins.ph Order History API
  slug: coinsph-order-history-api
- baseURL: https://api.pro.coins.ph
  baseurl_source: declared
  description: Webhook callbacks sent to the merchant's configured callback URL when order status changes
  name: Coins.ph Ramp Callback API
  slug: coinsph-ramp-callback-api
- baseURL: https://api.pro.coins.ph
  baseurl_source: declared
  description: Reconciliation report
  name: Coins.ph Reconciliation API
  slug: coinsph-reconciliation-api
- baseURL: https://api.pro.coins.ph
  baseurl_source: declared
  description: Refund operations
  name: Coins.ph Refund API
  slug: coinsph-refund-api
- baseURL: https://api.pro.coins.ph
  baseurl_source: declared
  description: QR code scan-to-pay payment operations
  name: Coins.ph Scan to Pay API
  slug: coinsph-scan-to-pay-api
- baseURL: https://api.pro.coins.ph
  baseurl_source: declared
  description: Spot trading operations including order placement, querying, cancellation, and trade history.
  name: Coins.ph Spot API
  slug: coinsph-spot-api
- baseURL: https://api.pro.coins.ph
  baseurl_source: declared
  description: Sub Account deposit, withdrawal, and transfer operations.
  name: Coins.ph Sub Account API
  slug: coinsph-sub-account-api
- baseURL: https://api.pro.coins.ph
  baseurl_source: declared
  description: Password-free (auto-debit) checkout
  name: Coins.ph Tokenized Checkout API
  slug: coinsph-tokenized-checkout-api
- baseURL: https://api.pro.coins.ph
  baseurl_source: declared
  description: Convert trading operations
  name: Coins.ph Trading - Convert API
  slug: coinsph-trading-convert-api
- baseURL: https://api.pro.coins.ph
  baseurl_source: declared
  description: OTC trading for Business Account
  name: Coins.ph Trading - OTC API
  slug: coinsph-trading-otc-api
- baseURL: https://api.pro.coins.ph
  baseurl_source: declared
  description: The Transfers API from Coins.ph — 2 operation(s) for transfers.
  name: Coins.ph Transfers API
  slug: coinsph-transfers-api
- baseURL: https://api.pro.coins.ph
  baseurl_source: declared
  description: Account balance, transfers, and utility endpoints
  name: Coins.ph Utility API
  slug: coinsph-utility-api
- baseURL: https://api.pro.coins.ph
  baseurl_source: declared
  description: Virtual account creation and management
  name: Coins.ph Virtual Account API
  slug: coinsph-virtual-account-api
- baseURL: https://api.pro.coins.ph
  baseurl_source: declared
  description: Convert, Deposit, Withdraw, Transfers, and Sub Account Transfer operations.
  name: Coins.ph Wallet API
  slug: coinsph-wallet-api
artifact_total: 59
asyncapis:
- description: ''
  name: Coinsph Webhooks
  slug: coinsph-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TRADING Account API
  slug: open-coinsph-account-api
- collection_type: open
  name: TRADING Account Account Validation API
  slug: open-coinsph-account-validation-api
- collection_type: open
  name: TRADING Account Checkout API
  slug: open-coinsph-checkout-api
- collection_type: open
  name: TRADING Account Checkout Refund API
  slug: open-coinsph-checkout-refund-api
- collection_type: open
  name: TRADING Account Collections - Crypto API
  slug: open-coinsph-collections-crypto-api
- collection_type: open
  name: TRADING Account Collections - QRPH API
  slug: open-coinsph-collections-qrph-api
- collection_type: open
  name: TRADING Account Convert API
  slug: open-coinsph-convert-api
- collection_type: open
  name: TRADING Account Disbursements API
  slug: open-coinsph-disbursements-api
- collection_type: open
  name: TRADING Account General API
  slug: open-coinsph-general-api
- collection_type: open
  name: TRADING Account Listens API
  slug: open-coinsph-listens-api
- collection_type: open
  name: TRADING Account Markets API
  slug: open-coinsph-markets-api
- collection_type: open
  name: TRADING Account ON/OFF Ramp API
  slug: open-coinsph-on-off-ramp-api
- collection_type: open
  name: TRADING Account Order History API
  slug: open-coinsph-order-history-api
- collection_type: open
  name: TRADING Account Ramp Callback API
  slug: open-coinsph-ramp-callback-api
- collection_type: open
  name: TRADING Account Reconciliation API
  slug: open-coinsph-reconciliation-api
- collection_type: open
  name: TRADING Account Refund API
  slug: open-coinsph-refund-api
- collection_type: open
  name: TRADING Account Scan to Pay API
  slug: open-coinsph-scan-to-pay-api
- collection_type: open
  name: TRADING Account Spot API
  slug: open-coinsph-spot-api
- collection_type: open
  name: TRADING Account Sub Account API
  slug: open-coinsph-sub-account-api
- collection_type: open
  name: TRADING Account Tokenized Checkout API
  slug: open-coinsph-tokenized-checkout-api
- collection_type: open
  name: TRADING Account Trading - Convert API
  slug: open-coinsph-trading-convert-api
- collection_type: open
  name: TRADING Account Trading - OTC API
  slug: open-coinsph-trading-otc-api
- collection_type: open
  name: TRADING Account Transfers API
  slug: open-coinsph-transfers-api
- collection_type: open
  name: TRADING Account Utility API
  slug: open-coinsph-utility-api
- collection_type: open
  name: TRADING Account Virtual Account API
  slug: open-coinsph-virtual-account-api
- collection_type: open
  name: TRADING Account Wallet API
  slug: open-coinsph-wallet-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.docs.coins.ph
- group: docs
  title: ''
  type: Documentation
  url: https://api.docs.coins.ph
- group: docs
  title: ''
  type: APIReference
  url: https://api.docs.coins.ph
- group: start
  title: ''
  type: GettingStarted
  url: https://api.docs.coins.ph
- group: operate
  title: ''
  type: ChangeLog
  url: https://api.docs.coins.ph/changelog
- group: operate
  title: ''
  type: Support
  url: https://support.coins.ph/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://coins.ph/en-ph/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coinsph
- group: commercial
  title: ''
  type: Pricing
  url: https://coins.ph/en-ph/fees
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coins.ph/en-ph/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coins.ph/en-ph/legal#privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coins.ph
- group: auth
  title: ''
  type: Security
  url: https://coins.ph/en-ph/bug-bounty
- group: company
  title: ''
  type: Website
  url: https://coins.ph/
- group: auth
  title: ''
  type: Authentication
  url: authentication/coinsph-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coinsph-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/coinsph-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/coinsph-packages.yml
- group: design
  title: ''
  type: Components
  url: components/coinsph-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/coinsph-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/coinsph-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/coinsph-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/coinsph-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/coinsph-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/coinsph-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/coinsph-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/coinsph-mcp.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/coinsph-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coinsph-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/coinsph-webhooks.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/coinsph-payment-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coinsph-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Coins.ph is a BSP-regulated Philippine fintech super app combining a licensed crypto exchange (Coins Pro), an e-wallet for pesos and 170+ cryptocurrencies, and a merchant/partner payments platform. Its public developer platform exposes a Partner Integration / Payment API (QRPH collections, checkout, disbursements, refunds, virtual accounts, reconciliation) and the Coins Pro exchange API (spot trading, wallets, market data, convert, sub-accounts, and a WebSocket user-data stream), plus an on/off ramp API. All requests are authenticated with an API key and HMAC-SHA256 request signing (X-COINS-APIKEY, Timestamp, Signature). Backed by Pantera Capital and Ribbit Capital.
image: https://coins.ph/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Coins.ph MCP Server
  slug: coinsph-mcp-server
modified: '2026-07-18'
name: Coins.ph
nav: Providers
network: true
overview: 'Coins.ph publishes 26 APIs on the [APIs.io](https://apis.io/) network, including Account API, Account Validation API, Checkout API, and 23 more. Tagged areas include Company, Crypto, Cryptocurrency Exchange, Payments, and Fintech.


  The Coins.ph catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Coins.ph''s developer surface includes documentation, API reference, getting-started guide, changelog, support, engineering blog, pricing, and 26 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 49.5
  coverage:
    artifact_dirs: 21
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 62.0
    developer_ergonomics: 54.2
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 44.7
  previous_composite: 49.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 26
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coinsph/refs/heads/main/screenshots/coinsph-2026-07-25T210033.png
security:
- kind: authentication
  name: Coinsph Authentication
  slug: coinsph-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Coinsph Domain Security
  slug: coinsph-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Coinsph Vulnerability Disclosure
  slug: coinsph-vulnerability-disclosure
  summary_line: contact published
slug: coinsph
tags:
- Company
- Crypto
- Cryptocurrency Exchange
- Payments
- Fintech
- Wallets
- Philippines
- Trading
website: https://coins.ph/
---

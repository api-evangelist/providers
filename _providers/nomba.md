---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.9
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 20
  human_in_the_loop: 1
  name: Nomba Agentic Access
  operation_count: 32
  slug: nomba-agentic-access
  summary_line: 32 operations · 20 acting · 1 human-in-the-loop
api_count: 14
apis:
- description: The Nomba Checkout SDK provides pre-built plugins and client libraries for integrating Nomba payment acceptance into websites and mobile applications. It includes an iOS SDK and e-commerce plugins suc
  name: Nomba Checkout SDK
  slug: checkout-sdk
- description: Endpoints for managing Nomba business accounts, retrieving account details, balances, and terminal assignments.
  name: Nomba Accounts API
  slug: nomba-accounts-api
- description: Endpoints for obtaining, refreshing, and revoking OAuth2 access tokens used to authenticate requests to all Nomba APIs.
  name: Nomba Authentication API
  slug: nomba-authentication-api
- description: Endpoints for submitting card details, processing OTP verification, and managing the card payment flow.
  name: Nomba Card Charge API
  slug: nomba-card-charge-api
- description: Endpoints for creating and managing online checkout orders that support multiple payment channels.
  name: Nomba Checkout Orders API
  slug: nomba-checkout-orders-api
- description: Endpoints for listing supported payout corridors and their configurations.
  name: Nomba Corridors API
  slug: nomba-corridors-api
- description: Endpoints for fetching and locking live exchange rates for cross-border payouts.
  name: Nomba Exchange Rates API
  slug: nomba-exchange-rates-api
- description: Endpoints for retrieving order details and managing checkout transactions.
  name: Nomba Order Management API
  slug: nomba-order-management-api
- description: Endpoints for initiating and tracking cross-border payout transactions.
  name: Nomba Payouts API
  slug: nomba-payouts-api
- description: Endpoints for retrieving and managing customer saved cards.
  name: Nomba Saved Cards API
  slug: nomba-saved-cards-api
- description: Endpoints for managing and charging tokenized card data for returning customers.
  name: Nomba Tokenized Cards API
  slug: nomba-tokenized-cards-api
- description: Endpoints for retrieving transaction history, filtering transactions, and querying transaction details for reconciliation and reporting.
  name: Nomba Transactions API
  slug: nomba-transactions-api
- description: Endpoints for bank lookups, account verification, and initiating domestic fund transfers to bank accounts and between wallets.
  name: Nomba Transfers API
  slug: nomba-transfers-api
- description: Endpoints for creating, fetching, filtering, updating, and expiring virtual bank accounts used for payment collection.
  name: Nomba Virtual Accounts API
  slug: nomba-virtual-accounts-api
artifact_total: 82
asyncapis:
- description: The Nomba Webhooks system delivers real-time event notifications via HTTP POST callbacks when activities occur within a customer account. Events include payment successes and failures, payout completi
  name: Nomba Webhook Events
  slug: nomba-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nomba Accounts API
  slug: open-nomba-accounts-api
- collection_type: open
  name: Nomba Accounts API
  slug: open-nomba-accounts
- collection_type: open
  name: Nomba Accounts Authentication API
  slug: open-nomba-authentication-api
- collection_type: open
  name: Nomba Authentication API
  slug: open-nomba-authentication
- collection_type: open
  name: Nomba Accounts Card Charge API
  slug: open-nomba-card-charge-api
- collection_type: open
  name: Nomba Charge API
  slug: open-nomba-charge
- collection_type: open
  name: Nomba Accounts Checkout Orders API
  slug: open-nomba-checkout-orders-api
- collection_type: open
  name: Nomba Accounts Corridors API
  slug: open-nomba-corridors-api
- collection_type: open
  name: Nomba Accounts Exchange Rates API
  slug: open-nomba-exchange-rates-api
- collection_type: open
  name: Nomba Global Payout API
  slug: open-nomba-global-payout
- collection_type: open
  name: Nomba Online Checkout API
  slug: open-nomba-online-checkout
- collection_type: open
  name: Nomba Accounts Order Management API
  slug: open-nomba-order-management-api
- collection_type: open
  name: Nomba Accounts Payouts API
  slug: open-nomba-payouts-api
- collection_type: open
  name: Nomba Accounts Saved Cards API
  slug: open-nomba-saved-cards-api
- collection_type: open
  name: Nomba Accounts Tokenized Cards API
  slug: open-nomba-tokenized-cards-api
- collection_type: open
  name: Nomba Accounts Transactions API
  slug: open-nomba-transactions-api
- collection_type: open
  name: Nomba Transactions API
  slug: open-nomba-transactions
- collection_type: open
  name: Nomba Accounts Transfers API
  slug: open-nomba-transfers-api
- collection_type: open
  name: Nomba Transfers API
  slug: open-nomba-transfers
- collection_type: open
  name: Nomba Accounts Virtual Accounts API
  slug: open-nomba-virtual-accounts-api
- collection_type: open
  name: Nomba Virtual Accounts API
  slug: open-nomba-virtual-accounts
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nomba-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nomba-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nomba-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nombahq
- group: company
  title: ''
  type: Website
  url: https://nomba.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.nomba.com
- group: company
  title: ''
  type: Blog
  url: https://nomba-developers.hashnode.dev
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/nomba-webhooks-asyncapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/nomba-webhook-event-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/nomba-virtual-account-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/nomba-transaction-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/nomba-checkout-order-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/nomba-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.nomba.com/llms.txt
created: '2026-03-24'
description: Nomba is a Nigerian fintech platform that provides payment infrastructure for businesses, offering APIs for payment acceptance, transfers, virtual accounts, and cross-border payouts. Their developer platform enables merchants and platforms to integrate card payments, bank transfers, USSD, and QR code payments into applications.
finops:
- name: Nomba Finops
  service_category: Payments
  slug: nomba-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nomba.png
json_schemas:
- name: Account
  property_count: 6
  slug: nomba-account
- name: AccountBalanceResponse
  property_count: 3
  slug: nomba-accountbalanceresponse
- name: AccountDetailsResponse
  property_count: 3
  slug: nomba-accountdetailsresponse
- name: Bank
  property_count: 2
  slug: nomba-bank
- name: BankAccountLookupResponse
  property_count: 3
  slug: nomba-bankaccountlookupresponse
- name: BankListResponse
  property_count: 3
  slug: nomba-banklistresponse
- name: CardChargeResponse
  property_count: 3
  slug: nomba-cardchargeresponse
- name: ChargeResponse
  property_count: 3
  slug: nomba-chargeresponse
- name: Nomba Checkout Order
  property_count: 9
  slug: nomba-checkout-order
- name: CheckoutOrderResponse
  property_count: 3
  slug: nomba-checkoutorderresponse
- name: Corridor
  property_count: 6
  slug: nomba-corridor
- name: CorridorListResponse
  property_count: 3
  slug: nomba-corridorlistresponse
- name: ErrorResponse
  property_count: 3
  slug: nomba-errorresponse
- name: ExchangeRate
  property_count: 4
  slug: nomba-exchangerate
- name: ExchangeRateListResponse
  property_count: 3
  slug: nomba-exchangeratelistresponse
- name: OrderDetailsResponse
  property_count: 3
  slug: nomba-orderdetailsresponse
- name: PayoutRecipient
  property_count: 8
  slug: nomba-payoutrecipient
- name: PayoutResponse
  property_count: 3
  slug: nomba-payoutresponse
- name: RateLockResponse
  property_count: 3
  slug: nomba-ratelockresponse
- name: SavedCard
  property_count: 6
  slug: nomba-savedcard
- name: SavedCardsResponse
  property_count: 3
  slug: nomba-savedcardsresponse
- name: SuccessResponse
  property_count: 2
  slug: nomba-successresponse
- name: Terminal
  property_count: 4
  slug: nomba-terminal
- name: TerminalsResponse
  property_count: 3
  slug: nomba-terminalsresponse
- name: TokenizedCard
  property_count: 6
  slug: nomba-tokenizedcard
- name: TokenizedCardListResponse
  property_count: 3
  slug: nomba-tokenizedcardlistresponse
- name: TokenResponse
  property_count: 3
  slug: nomba-tokenresponse
- name: Nomba Transaction
  property_count: 15
  slug: nomba-transaction
- name: TransactionListResponse
  property_count: 3
  slug: nomba-transactionlistresponse
- name: TransferResponse
  property_count: 3
  slug: nomba-transferresponse
- name: Nomba Virtual Account
  property_count: 9
  slug: nomba-virtual-account
- name: VirtualAccount
  property_count: 7
  slug: nomba-virtualaccount
- name: VirtualAccountListResponse
  property_count: 3
  slug: nomba-virtualaccountlistresponse
- name: VirtualAccountResponse
  property_count: 3
  slug: nomba-virtualaccountresponse
- name: Nomba Webhook Event
  property_count: 3
  slug: nomba-webhook-event
json_structures:
- name: Nomba Structure
  property_count: 0
  slug: nomba-structure
jsonld:
- class_count: 0
  name: Nomba Context
  property_count: 9
  slug: nomba-context
layout: provider
modified: '2026-05-19'
name: Nomba
nav: Providers
network: true
overview: 'Nomba publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Authentication API, Card Charge API, and 10 more. Tagged areas include Payments, Fintech, Banking, Transfers, and Virtual Accounts.


  The Nomba catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Nomba''s developer surface includes authentication, engineering blog, and 12 more developer resources.'
plans:
- name: Nomba Plans Pricing
  plan_count: 1
  slug: nomba-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Nomba Rate Limits
  slug: nomba-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Nomba API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: nomba-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Nomba API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: nomba-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.0
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 13.6
    contract_quality: 72.2
    developer_ergonomics: 23.8
    discoverability: 81.5
    governance: 13.6
    operational_transparency: 5.3
  previous_composite: 36.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 32.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nomba/refs/heads/main/screenshots/nomba-2026-06-20T190355.png
security:
- kind: authentication
  name: Nomba Authentication
  slug: nomba-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nomba Domain Security
  slug: nomba-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nomba
tags:
- Payments
- Fintech
- Banking
- Transfers
- Virtual Accounts
- Checkout
- Cross-Border Payments
- Cards
website: https://nomba.com
---

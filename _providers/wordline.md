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
  - scopes
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 419
  human_in_the_loop: 29
  name: Wordline Agentic Access
  operation_count: 695
  slug: wordline-agentic-access
  summary_line: 695 operations · 419 acting · 29 human-in-the-loop
api_count: 9
apis:
- description: Enterprise online payment processing API enabling merchants to accept payments globally through hosted checkout, hosted tokenization, and server-to-server integration. Supports payments, refunds, disp
  name: Worldline Connect (Global Collect) API
  slug: worldline-connect-global-collect-api
- description: 'Online payment API for SMBs providing access to 40+ alternative payment methods, 20+ local acquirers, and comprehensive payment operations including cancellations, captures, refunds, and Card on File '
  name: Worldline Direct (Global Online Pay) API
  slug: worldline-direct-global-online-pay-api
- description: 'Platform-independent REST API for PSPs, NSPs, and Payment Facilitators to process merchant transactions. Supports card-based transactions, Card-on-File operations, Strong Customer Authentication, and '
  name: Worldline Acquiring API
  slug: worldline-acquiring-api
- description: Modular card management solution providing full-scope issuing services for card issuers including card lifecycle management, authentication, and value-added services.
  name: Worldline Financial Services Issuing API
  slug: worldline-financial-services-issuing-api
- description: Smart acquiring processing for all channels and ATM management. Includes merchant management, accept transactions, interchange fees, merchant analysis, statements, and transaction APIs.
  name: Worldline Financial Services Acquiring API
  slug: worldline-financial-services-acquiring-api
- description: Connectivity to more than 3,500 European banks in 21 countries supporting PSD2 open banking. Provides payment initiation, account information, verification of payee, iDEAL 2.0, WERO, and account-to-ac
  name: Worldline Open Banking API
  slug: worldline-open-banking-api
- description: API for building and deploying applications on Worldline SmartPOS Android payment terminals. Supports in-person payment acceptance, tap-to-pay, value-added services, and app lifecycle management throu
  name: Worldline SmartPOS API
  slug: worldline-smartpos-api
- description: Security APIs for authenticating sensitive financial transactions including FIDO-based two-factor authentication, WebProtector 3D Secure, risk-based authentication scoring, OAuth2 token management, an
  name: Worldline Identity and Authentication API
  slug: worldline-identity-and-authentication-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Account State Controller
  name: Worldline Account - AccountState API
  slug: wordline-account-accountstate-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Account Api Controller
  name: Worldline Account API
  slug: wordline-account-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Account Authorization Controller
  name: Worldline Account - Authorization API
  slug: wordline-account-authorization-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Account Authorization Restriction Controller
  name: Worldline Account - Authorization Restriction API
  slug: wordline-account-authorization-restriction-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Account Cvv2 Try Counter Controller
  name: Worldline Account - Cvv2 Try Counter API
  slug: wordline-account-cvv2-try-counter-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Account Future Updates Api Controller
  name: Worldline Account - Future Update API
  slug: wordline-account-future-update-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Account Insurance Contract Api Controller
  name: Worldline Account - Insurance Contract API
  slug: wordline-account-insurance-contract-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Account Offline Reservation Api Controller
  name: Worldline Account - Offline Reservation API
  slug: wordline-account-offline-reservation-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Account Operation Api Controller
  name: Worldline Account - Operation API
  slug: wordline-account-operation-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Account Statement Api Controller
  name: Worldline Account - Statement API
  slug: wordline-account-statement-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Account Temporary Credit Limit Api Controller
  name: Worldline Account - Temporary Credit Limit API
  slug: wordline-account-temporary-credit-limit-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Account Velocity Limit Controller
  name: Worldline Account - Velocity Limit API
  slug: wordline-account-velocity-limit-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Api Meta Info Api Controller
  name: Worldline Api Meta Info API
  slug: wordline-api-meta-info-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: The Authentication Resource API from Worldline — 1 operation(s) for authentication resource.
  name: Worldline Authentication Resource API
  slug: wordline-authentication-resource-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: The Authorization API from Worldline — 1 operation(s) for authorization.
  name: Worldline Authorization API
  slug: wordline-authorization-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: The Bulk Payment Initiation Service (Extended service) API from Worldline — 10 operation(s) for bulk payment initiation service (extended service).
  name: Worldline Bulk Payment Initiation Service (Extended service) API
  slug: wordline-bulk-payment-initiation-service-extended-service-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Card Api Controller
  name: Worldline Card API
  slug: wordline-card-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Card Pin State
  name: Worldline Card - CardPinState API
  slug: wordline-card-cardpinstate-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Card Contract Api Controller
  name: Worldline Card Contract API
  slug: wordline-card-contract-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Card CVV Api Controller
  name: Worldline Card - CVV API
  slug: wordline-card-cvv-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Card EMV Controller
  name: Worldline Card - EMV API
  slug: wordline-card-emv-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Card Letter API Controller
  name: Worldline Card - Letter API
  slug: wordline-card-letter-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Card Linked Account State Controller
  name: Worldline Card - LinkedAccountState API
  slug: wordline-card-linkedaccountstate-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Card Order Api Controller
  name: Worldline Card - Order API
  slug: wordline-card-order-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Card Pin Api Controller
  name: Worldline Card - Pin API
  slug: wordline-card-pin-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Card Pin Try Counter Api Controller
  name: Worldline Card - Pin Try Counter API
  slug: wordline-card-pin-try-counter-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Company Address Api Controller
  name: Worldline Company - Address API
  slug: wordline-company-address-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Company Api Controller
  name: Worldline Company API
  slug: wordline-company-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Company Related Api Controller
  name: Worldline Company - Related API
  slug: wordline-company-related-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Contract Api Controller
  name: Worldline Contract API
  slug: wordline-contract-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Contract Global Search API Controller
  name: Worldline Contract - Global Search API
  slug: wordline-contract-global-search-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Corporate Contract API Controller
  name: Worldline Corporate Contract API
  slug: wordline-corporate-contract-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Corporate Contract Global Search API Controller
  name: Worldline Corporate Contract - Global Search API
  slug: wordline-corporate-contract-global-search-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Credit Transfer Api Controller
  name: Worldline Credit Transfer API
  slug: wordline-credit-transfer-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: The Currency Conversion (Extended services) API from Worldline — 1 operation(s) for currency conversion (extended services).
  name: Worldline Currency Conversion (Extended services) API
  slug: wordline-currency-conversion-extended-services-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Customer Address Api Controller
  name: Worldline Customer - Address API
  slug: wordline-customer-address-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Customer Api Controller
  name: Worldline Customer API
  slug: wordline-customer-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Customer Related Api Controller
  name: Worldline Customer - Related API
  slug: wordline-customer-related-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: The Debtor Preference Retrieval API from Worldline — 1 operation(s) for debtor preference retrieval.
  name: Worldline Debtor Preference Retrieval API
  slug: wordline-debtor-preference-retrieval-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Direct Debit Api Controller
  name: Worldline Direct Debit API
  slug: wordline-direct-debit-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Dispute Api Controller
  name: Worldline Dispute API
  slug: wordline-dispute-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Event Store Controller
  name: Worldline Event Store API
  slug: wordline-event-store-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: The Holding API from Worldline — 3 operation(s) for holding.
  name: Worldline Holding API
  slug: wordline-holding-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: The Interchange fee API from Worldline — 7 operation(s) for interchange fee.
  name: Worldline Interchange fee API
  slug: wordline-interchange-fee-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Issuer Api Controller
  name: Worldline Issuer API
  slug: wordline-issuer-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Issuer Velocity Limit Controller
  name: Worldline Issuer - Velocity Limit API
  slug: wordline-issuer-velocity-limit-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: The Merchant API from Worldline — 4 operation(s) for merchant.
  name: Worldline Merchant API
  slug: wordline-merchant-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Message Subscription Api Controller
  name: Worldline Message - Subscription API
  slug: wordline-message-subscription-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Message Subscription Event Api Controller
  name: Worldline Message - Subscription Event API
  slug: wordline-message-subscription-event-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Message Subscription Service Api Controller
  name: Worldline Message - Subscription Service API
  slug: wordline-message-subscription-service-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Apple Pay Controller
  name: Worldline Mobile Payment Operations API
  slug: wordline-mobile-payment-operations-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Operation Global Search API Controller
  name: Worldline Operation - Global Search API
  slug: wordline-operation-global-search-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: The Payment API from Worldline — 5 operation(s) for payment.
  name: Worldline Payment API
  slug: wordline-payment-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: The Payment Initiation Service API from Worldline — 11 operation(s) for payment initiation service.
  name: Worldline Payment Initiation Service API
  slug: wordline-payment-initiation-service-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: The Periodic Payment Initiation Service (Extended service) API from Worldline — 10 operation(s) for periodic payment initiation service (extended service).
  name: Worldline Periodic Payment Initiation Service (Extended service) API
  slug: wordline-periodic-payment-initiation-service-extended-service-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Product Override API Controller
  name: Worldline Product Override API
  slug: wordline-product-override-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: The Refund Initiation Service V3 (Extended services) API from Worldline — 6 operation(s) for refund initiation service v3 (extended services).
  name: Worldline Refund Initiation Service V3 (Extended services) API
  slug: wordline-refund-initiation-service-v3-extended-services-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: The Registration Resource API from Worldline — 1 operation(s) for registration resource.
  name: Worldline Registration Resource API
  slug: wordline-registration-resource-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: The Relying Party Resource API from Worldline — 2 operation(s) for relying party resource.
  name: Worldline Relying Party Resource API
  slug: wordline-relying-party-resource-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: The Retrieve transaction totals API from Worldline — 2 operation(s) for retrieve transaction totals.
  name: Worldline Retrieve transaction totals API
  slug: wordline-retrieve-transaction-totals-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: The Retrieve transaction totals per brand API from Worldline — 2 operation(s) for retrieve transaction totals per brand.
  name: Worldline Retrieve transaction totals per brand API
  slug: wordline-retrieve-transaction-totals-per-brand-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: The Scheduled Payment Initiation Service (Extended service) API from Worldline — 10 operation(s) for scheduled payment initiation service (extended service).
  name: Worldline Scheduled Payment Initiation Service (Extended service) API
  slug: wordline-scheduled-payment-initiation-service-extended-service-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: The Site API from Worldline — 8 operation(s) for site.
  name: Worldline Site API
  slug: wordline-site-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: The Statement API from Worldline — 4 operation(s) for statement.
  name: Worldline Statement API
  slug: wordline-statement-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: The Terminal API from Worldline — 10 operation(s) for terminal.
  name: Worldline Terminal API
  slug: wordline-terminal-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: The Token Resource API from Worldline — 1 operation(s) for token resource.
  name: Worldline Token Resource API
  slug: wordline-token-resource-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Transaction API Controller
  name: Worldline Transaction API
  slug: wordline-transaction-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: Transaction Global Search API Controller
  name: Worldline Transaction - Global Search API
  slug: wordline-transaction-global-search-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: The Transaction Lifecycle API from Worldline — 1 operation(s) for transaction lifecycle.
  name: Worldline Transaction Lifecycle API
  slug: wordline-transaction-lifecycle-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: The User Resource API from Worldline — 2 operation(s) for user resource.
  name: Worldline User Resource API
  slug: wordline-user-resource-api
- baseURL: https://api.connect.worldline-solutions.com
  baseurl_source: declared
  description: The Health Check API from Worldline — 1 operation(s) for health check.
  name: Worldline Health Check API
  slug: wordline-health-check-api
artifact_total: 333
asyncapis:
- description: ''
  name: Wordline Webhooks
  slug: wordline-webhooks
collections:
- collection_type: open
  name: Worldline Card Issuing Account - AccountState API
  slug: open-wordline-account-accountstate-api
- collection_type: open
  name: Worldline Card Issuing - AccountState Account API
  slug: open-wordline-account-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Account - Authorization API
  slug: open-wordline-account-authorization-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Account - Authorization Restriction API
  slug: open-wordline-account-authorization-restriction-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Account - Cvv2 Try Counter API
  slug: open-wordline-account-cvv2-try-counter-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Account - Future Update API
  slug: open-wordline-account-future-update-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Account - Insurance Contract API
  slug: open-wordline-account-insurance-contract-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Account - Offline Reservation API
  slug: open-wordline-account-offline-reservation-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Account - Operation API
  slug: open-wordline-account-operation-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Account - Statement API
  slug: open-wordline-account-statement-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Account - Temporary Credit Limit API
  slug: open-wordline-account-temporary-credit-limit-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Account - Velocity Limit API
  slug: open-wordline-account-velocity-limit-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Api Meta Info API
  slug: open-wordline-api-meta-info-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Authentication Resource API
  slug: open-wordline-authentication-resource-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Authorization API
  slug: open-wordline-authorization-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Bulk Payment Initiation Service (Extended service) API
  slug: open-wordline-bulk-payment-initiation-service-extended-service-api
- collection_type: open
  name: Worldline Issuing Account - AccountState Card API
  slug: open-wordline-card-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Card - CardPinState API
  slug: open-wordline-card-cardpinstate-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Card Contract API
  slug: open-wordline-card-contract-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Card - CVV API
  slug: open-wordline-card-cvv-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Card - EMV API
  slug: open-wordline-card-emv-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Card - Letter API
  slug: open-wordline-card-letter-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Card - LinkedAccountState API
  slug: open-wordline-card-linkedaccountstate-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Card - Order API
  slug: open-wordline-card-order-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Card - Pin API
  slug: open-wordline-card-pin-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Card - Pin Try Counter API
  slug: open-wordline-card-pin-try-counter-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Company - Address API
  slug: open-wordline-company-address-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Company API
  slug: open-wordline-company-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Company - Related API
  slug: open-wordline-company-related-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Contract API
  slug: open-wordline-contract-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Contract - Global Search API
  slug: open-wordline-contract-global-search-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Corporate Contract API
  slug: open-wordline-corporate-contract-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Corporate Contract - Global Search API
  slug: open-wordline-corporate-contract-global-search-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Credit Transfer API
  slug: open-wordline-credit-transfer-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Currency Conversion (Extended services) API
  slug: open-wordline-currency-conversion-extended-services-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Customer - Address API
  slug: open-wordline-customer-address-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Customer API
  slug: open-wordline-customer-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Customer - Related API
  slug: open-wordline-customer-related-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Debtor Preference Retrieval API
  slug: open-wordline-debtor-preference-retrieval-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Direct Debit API
  slug: open-wordline-direct-debit-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Dispute API
  slug: open-wordline-dispute-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Event Store API
  slug: open-wordline-event-store-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState HealthCheck API
  slug: open-wordline-healthcheck-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Holding API
  slug: open-wordline-holding-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Interchange fee API
  slug: open-wordline-interchange-fee-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Issuer API
  slug: open-wordline-issuer-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Issuer - Velocity Limit API
  slug: open-wordline-issuer-velocity-limit-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Merchant API
  slug: open-wordline-merchant-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Message - Subscription API
  slug: open-wordline-message-subscription-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Message - Subscription Event API
  slug: open-wordline-message-subscription-event-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Message - Subscription Service API
  slug: open-wordline-message-subscription-service-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Mobile Payment Operations API
  slug: open-wordline-mobile-payment-operations-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Operation - Global Search API
  slug: open-wordline-operation-global-search-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Payment API
  slug: open-wordline-payment-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Payment Initiation Service API
  slug: open-wordline-payment-initiation-service-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Periodic Payment Initiation Service (Extended service) API
  slug: open-wordline-periodic-payment-initiation-service-extended-service-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Product Override API
  slug: open-wordline-product-override-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Refund Initiation Service V3 (Extended services) API
  slug: open-wordline-refund-initiation-service-v3-extended-services-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Registration Resource API
  slug: open-wordline-registration-resource-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Relying Party Resource API
  slug: open-wordline-relying-party-resource-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Retrieve transaction totals API
  slug: open-wordline-retrieve-transaction-totals-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Retrieve transaction totals per brand API
  slug: open-wordline-retrieve-transaction-totals-per-brand-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Scheduled Payment Initiation Service (Extended service) API
  slug: open-wordline-scheduled-payment-initiation-service-extended-service-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Site API
  slug: open-wordline-site-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Statement API
  slug: open-wordline-statement-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Terminal API
  slug: open-wordline-terminal-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Token Resource API
  slug: open-wordline-token-resource-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Transaction API
  slug: open-wordline-transaction-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Transaction - Global Search API
  slug: open-wordline-transaction-global-search-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState Transaction Lifecycle API
  slug: open-wordline-transaction-lifecycle-api
- collection_type: open
  name: Worldline Card Issuing Account - AccountState User Resource API
  slug: open-wordline-user-resource-api
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://worldline.com/en/compliancy/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://worldline.com/en/compliancy/privacy
- group: design
  href: https://artifacts.apis.io/wordline/rules/wordline-rules.yml
  title: ''
  type: Spectral
  url: rules/wordline-rules.yml
- group: design
  href: https://artifacts.apis.io/wordline/json-ld/wordline-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/wordline-context.jsonld
- group: design
  href: https://artifacts.apis.io/wordline/vocabulary/wordline-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/wordline-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/wordline/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/wordline/asyncapi/wordline-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/wordline-webhooks.yml
- group: design
  href: https://artifacts.apis.io/wordline/data-model/wordline-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wordline-data-model.yml
- group: design
  href: https://artifacts.apis.io/wordline/conventions/wordline-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/wordline-conventions.yml
- group: design
  href: https://artifacts.apis.io/wordline/conventions/wordline-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wordline-conventions.yml
- group: operate
  href: https://artifacts.apis.io/wordline/lifecycle/wordline-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/wordline-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/wordline/lifecycle/wordline-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/wordline-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/wordline/errors/wordline-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/wordline-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/wordline/errors/wordline-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wordline-problem-types.yml
- group: design
  href: https://artifacts.apis.io/wordline/conformance/wordline-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wordline-conformance.yml
- group: other
  href: https://artifacts.apis.io/wordline/hosts/wordline-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wordline-hosts.yml
- group: other
  href: https://artifacts.apis.io/wordline/vendors/wordline-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wordline-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.connect.worldline-solutions.com/getting-started/index
- group: docs
  title: ''
  type: Documentation
  url: https://developer.worldline.com/
- group: other
  href: https://artifacts.apis.io/wordline/capabilities/wordline-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/wordline-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/wordline/agentic-access/wordline-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/wordline-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/wordline/security/wordline-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wordline-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/wordline/authentication/wordline-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wordline-authentication.yml
- group: auth
  href: https://artifacts.apis.io/wordline/scopes/wordline-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/wordline-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.worldline.com/en/home
- group: start
  title: ''
  type: FinancialServicesPortal
  url: https://financial-services.developer.worldline.com/home
- group: company
  title: ''
  type: Website
  url: https://worldline.com/
- group: operate
  title: ''
  type: Support
  url: https://developer.worldline.com/en/home/contact
- group: start
  title: ''
  type: Signup
  url: https://financial-services.developer.worldline.com/user/register
- group: start
  title: ''
  type: Login
  url: https://financial-services.developer.worldline.com/user/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/worldline
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/worldline-global-collect
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wl-online-payments-direct
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/wordline/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/wordline/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/wordline/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: European payment and digital services company providing REST APIs for payment processing, acquiring, digital banking services, open banking, identity and authentication, and merchant account management.
finops:
- has_sources: false
  method: generated
  name: Finops
  primary_unit: ''
  service_category: ''
  slug: finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wordline.png
json_schemas:
- name: AddCardsAccountsRequest
  property_count: 7
  slug: wordline-add-cards-accounts-request
- name: AddCorporateContractEntityRequest
  property_count: 3
  slug: wordline-add-corporate-contract-entity-request
- name: AddCorporateEmployeeCardsAndAccountsRequest
  property_count: 2
  slug: wordline-add-corporate-employee-cards-and-accounts-request
- name: AddCorporateVcaServiceCardsAndAccountsRequest
  property_count: 2
  slug: wordline-add-corporate-vca-service-cards-and-accounts-request
- name: ApiResponseEntityAddressVersions
  property_count: 2
  slug: wordline-api-response-entity-address-versions
- name: ApiResponseEntityCancelAccountDelinquencyResponse
  property_count: 2
  slug: wordline-api-response-entity-cancel-account-delinquency-response
- name: ApiResponseEntityCancelAccountFutureUpdateResponse
  property_count: 2
  slug: wordline-api-response-entity-cancel-account-future-update-response
- name: ApiResponseEntityCancelCloseCardContractResponse
  property_count: 2
  slug: wordline-api-response-entity-cancel-close-card-contract-response
- name: ApiResponseEntityCancelCreditTransferResponse
  property_count: 2
  slug: wordline-api-response-entity-cancel-credit-transfer-response
- name: ApiResponseEntityCancelDirectDebitResponse
  property_count: 2
  slug: wordline-api-response-entity-cancel-direct-debit-response
- name: ApiResponseEntityCancelOfflineReservationResponse
  property_count: 2
  slug: wordline-api-response-entity-cancel-offline-reservation-response
- name: ApiResponseEntityCardPinStateList
  property_count: 2
  slug: wordline-api-response-entity-card-pin-state-list
- name: ApiResponseEntityCardPinState
  property_count: 2
  slug: wordline-api-response-entity-card-pin-state
- name: ApiResponseEntityCloseCardContractResponse
  property_count: 2
  slug: wordline-api-response-entity-close-card-contract-response
- name: ApiResponseEntityCloseInsuranceContractResponse
  property_count: 2
  slug: wordline-api-response-entity-close-insurance-contract-response
- name: ApiResponseEntityCreateAccountFutureUpdateResponse
  property_count: 2
  slug: wordline-api-response-entity-create-account-future-update-response
- name: ApiResponseEntityCreateAddressAndSubscriptionResponse
  property_count: 2
  slug: wordline-api-response-entity-create-address-and-subscription-response
- name: ApiResponseEntityCreateAddressUsageResponse
  property_count: 2
  slug: wordline-api-response-entity-create-address-usage-response
- name: ApiResponseEntityCreateAuthorizationRestrictionOverride
  property_count: 2
  slug: wordline-api-response-entity-create-authorization-restriction-override
- name: ApiResponseEntityCreateContactResponse
  property_count: 2
  slug: wordline-api-response-entity-create-contact-response
- name: ApiResponseEntityCreateCreditTransferResponse
  property_count: 2
  slug: wordline-api-response-entity-create-credit-transfer-response
- name: ApiResponseEntityCreateCustomerResponse
  property_count: 2
  slug: wordline-api-response-entity-create-customer-response
- name: ApiResponseEntityCreateDirectDebitResponse
  property_count: 2
  slug: wordline-api-response-entity-create-direct-debit-response
- name: ApiResponseEntityCreateInsuranceContractResponse
  property_count: 2
  slug: wordline-api-response-entity-create-insurance-contract-response
- name: ApiResponseEntityCreateInsuranceEventResponse
  property_count: 2
  slug: wordline-api-response-entity-create-insurance-event-response
- name: ApiResponseEntityCreateOfflineReservationResponse
  property_count: 2
  slug: wordline-api-response-entity-create-offline-reservation-response
- name: ApiResponseEntityCreateTemporaryCreditLimitResponse
  property_count: 2
  slug: wordline-api-response-entity-create-temporary-credit-limit-response
- name: ApiResponseEntityCreateVelocityLimitOverride
  property_count: 2
  slug: wordline-api-response-entity-create-velocity-limit-override
- name: ApiResponseEntityCreditTransfer
  property_count: 2
  slug: wordline-api-response-entity-credit-transfer
- name: ApiResponseEntityDeactivateAddressResponse
  property_count: 2
  slug: wordline-api-response-entity-deactivate-address-response
- name: ApiResponseEntityDeleteAddressUsageResponse
  property_count: 2
  slug: wordline-api-response-entity-delete-address-usage-response
- name: ApiResponseEntityDeleteAuthorizationRestrictionOverride
  property_count: 2
  slug: wordline-api-response-entity-delete-authorization-restriction-override
- name: ApiResponseEntityDeleteCardLetterResponse
  property_count: 2
  slug: wordline-api-response-entity-delete-card-letter-response
- name: ApiResponseEntityDeleteTemporaryCreditLimitResponse
  property_count: 2
  slug: wordline-api-response-entity-delete-temporary-credit-limit-response
- name: ApiResponseEntityDeleteVelocityLimitOverride
  property_count: 2
  slug: wordline-api-response-entity-delete-velocity-limit-override
- name: ApiResponseEntityDirectDebit
  property_count: 2
  slug: wordline-api-response-entity-direct-debit
- name: ApiResponseEntityEmptyEntity
  property_count: 2
  slug: wordline-api-response-entity-empty-entity
- name: ApiResponseEntityEMVCommands
  property_count: 2
  slug: wordline-api-response-entity-emvcommands
- name: ApiResponseEntityEnquireVelocityChecks
  property_count: 2
  slug: wordline-api-response-entity-enquire-velocity-checks
- name: ApiResponseEntityEventStoreList
  property_count: 2
  slug: wordline-api-response-entity-event-store-list
- name: ApiResponseEntityGenerateCardLetterResponse
  property_count: 2
  slug: wordline-api-response-entity-generate-card-letter-response
- name: ApiResponseEntityGetAccountStates
  property_count: 2
  slug: wordline-api-response-entity-get-account-states
- name: ApiResponseEntityGetAuthorizationRestrictionOverrideHistory
  property_count: 2
  slug: wordline-api-response-entity-get-authorization-restriction-override-history
- name: ApiResponseEntityGetAuthorizationRestrictionOverrides
  property_count: 2
  slug: wordline-api-response-entity-get-authorization-restriction-overrides
- name: ApiResponseEntityGetAuthorization
  property_count: 2
  slug: wordline-api-response-entity-get-authorization
- name: ApiResponseEntityGetAuthorizations
  property_count: 2
  slug: wordline-api-response-entity-get-authorizations
- name: ApiResponseEntityGetBusinessCase
  property_count: 2
  slug: wordline-api-response-entity-get-business-case
- name: ApiResponseEntityGetBusinessCases
  property_count: 2
  slug: wordline-api-response-entity-get-business-cases
- name: ApiResponseEntityGetCvvResponse
  property_count: 2
  slug: wordline-api-response-entity-get-cvv-response
- name: ApiResponseEntityGetPinResponse
  property_count: 2
  slug: wordline-api-response-entity-get-pin-response
- name: ApiResponseEntityGetReserves
  property_count: 2
  slug: wordline-api-response-entity-get-reserves
- name: ApiResponseEntityGetVelocityLimitOverrideHistoryResponse
  property_count: 2
  slug: wordline-api-response-entity-get-velocity-limit-override-history-response
- name: ApiResponseEntityGlobalSearchContract
  property_count: 2
  slug: wordline-api-response-entity-global-search-contract
- name: ApiResponseEntityInfo
  property_count: 2
  slug: wordline-api-response-entity-info
- name: ApiResponseEntityListAccountFutureUpdate
  property_count: 2
  slug: wordline-api-response-entity-list-account-future-update
- name: ApiResponseEntityListAccount
  property_count: 2
  slug: wordline-api-response-entity-list-account
- name: ApiResponseEntityListCardContract
  property_count: 2
  slug: wordline-api-response-entity-list-card-contract
- name: ApiResponseEntityListContract
  property_count: 2
  slug: wordline-api-response-entity-list-contract
- name: ApiResponseEntityListCompany
  property_count: 2
  slug: wordline-api-response-entity-list-corporate-contracts
- name: ApiResponseEntityListInsuranceContract
  property_count: 2
  slug: wordline-api-response-entity-list-insurance-contract
- name: ApiResponseEntityListIssuer
  property_count: 2
  slug: wordline-api-response-entity-list-issuer
- name: ApiResponseEntityListOfflineReservationsResponse
  property_count: 2
  slug: wordline-api-response-entity-list-offline-reservations-response
- name: ApiResponseEntityListOperation
  property_count: 2
  slug: wordline-api-response-entity-list-operation
- name: ApiResponseEntityListStatement
  property_count: 2
  slug: wordline-api-response-entity-list-statement
- name: ApiResponseEntityListTemporaryCreditLimit
  property_count: 2
  slug: wordline-api-response-entity-list-temporary-credit-limit
- name: ApiResponseEntityModifyAccountFutureUpdateResponse
  property_count: 2
  slug: wordline-api-response-entity-modify-account-future-update-response
- name: ApiResponseEntityModifyCardContractResponse
  property_count: 2
  slug: wordline-api-response-entity-modify-card-contract-response
- name: ApiResponseEntityModifyContactResponse
  property_count: 2
  slug: wordline-api-response-entity-modify-contact-response
- name: ApiResponseEntityModifyCreditLimitResponse
  property_count: 2
  slug: wordline-api-response-entity-modify-credit-limit-response
- name: ApiResponseEntityModifyVelocityLimitOverride
  property_count: 2
  slug: wordline-api-response-entity-modify-velocity-limit-override
- name: ApiResponseEntityOrder
  property_count: 2
  slug: wordline-api-response-entity-order
- name: ApiResponseEntityPrefilledLetterTemplatesResponse
  property_count: 2
  slug: wordline-api-response-entity-prefilled-letter-templates-response
- name: ApiResponseEntityReleaseOrderResponse
  property_count: 2
  slug: wordline-api-response-entity-release-order-response
- name: ApiResponseEntityReprintStatementResponse
  property_count: 2
  slug: wordline-api-response-entity-reprint-statement-response
- name: ApiResponseEntityRetrieveLetterTemplates
  property_count: 2
  slug: wordline-api-response-entity-retrieve-letter-templates
- name: ApiResponseEntitySetPinResponse
  property_count: 2
  slug: wordline-api-response-entity-set-pin-response
- name: ApiResponseEntityStatement
  property_count: 2
  slug: wordline-api-response-entity-statement
- name: ApiResponseEntityValidateCardLetterResponse
  property_count: 2
  slug: wordline-api-response-entity-validate-card-letter-response
- name: ApiResponseEntityValidateCvvResponse
  property_count: 2
  slug: wordline-api-response-entity-validate-cvv-response
- name: AssertionResponse
  property_count: 2
  slug: wordline-assertion-response
- name: AuthOptionRequest
  property_count: 3
  slug: wordline-auth-option-request
- name: AuthOptionResponse
  property_count: 9
  slug: wordline-auth-option-response
- name: Authorization
  property_count: 32
  slug: wordline-authorization
- name: BlockAllCardsRequest
  property_count: 27
  slug: wordline-block-all-cards-request
- name: BlockCardRequest
  property_count: 25
  slug: wordline-block-card-request
- name: BulkPaymentInitiationRequest
  property_count: 5
  slug: wordline-bulk-payment-initiation-request
- name: BusinessCasesEnquiryRequest
  property_count: 4
  slug: wordline-business-cases-enquiry-request
- name: BusinessRefTypeValues
  property_count: 2
  slug: wordline-business-ref-type-values
- name: CancelCreditTransferRequest
  property_count: 1
  slug: wordline-cancel-credit-transfer-request
- name: CancelDirectDebitRequest
  property_count: 1
  slug: wordline-cancel-direct-debit-request
- name: CancelMandateRequest
  property_count: 4
  slug: wordline-cancel-mandate-request
- name: CancelOfflineReservationRequest
  property_count: 1
  slug: wordline-cancel-offline-reservation-request
- name: CloseCardContractRequest
  property_count: 4
  slug: wordline-close-card-contract-request
- name: CorrelationResponse
  property_count: 1
  slug: wordline-correlation-response
- name: CreateAccountFutureUpdateRequest
  property_count: 17
  slug: wordline-create-account-future-update-request
- name: CreateAddOnSubscriptionRequest
  property_count: 7
  slug: wordline-create-add-on-subscription-request
- name: CreateAddressAndSubscriptionRequest
  property_count: 3
  slug: wordline-create-address-and-subscription-request
- name: CreateAddressRequest
  property_count: 10
  slug: wordline-create-address-request
- name: CreateAddressUsageRequest
  property_count: 3
  slug: wordline-create-address-usage-request
- name: CreateAuthorizationRestrictionOverrideRequest
  property_count: 5
  slug: wordline-create-authorization-restriction-override-request
- name: CreateCompanyRequest
  property_count: 17
  slug: wordline-create-company-request
- name: CreateContactRequest
  property_count: 9
  slug: wordline-create-contact-request
- name: CreateCorporateContractRequest
  property_count: 6
  slug: wordline-create-corporate-contract-request
- name: CreateCreditTransferRequest
  property_count: 8
  slug: wordline-create-credit-transfer-request
- name: CreateCustomerRequest
  property_count: 36
  slug: wordline-create-customer-request
- name: CreateDirectDebitRequest
  property_count: 4
  slug: wordline-create-direct-debit-request
- name: CreateDisputeRequest
  property_count: 10
  slug: wordline-create-dispute-request
- name: CreateDocumentRequest
  property_count: 5
  slug: wordline-create-document-request
- name: CreateEventRequest
  property_count: 2
  slug: wordline-create-event-request
- name: CreateEventStoreEventRequest
  property_count: 7
  slug: wordline-create-event-store-event-request
- name: CreateEventStoreEventResponse
  property_count: 1
  slug: wordline-create-event-store-event-response
- name: CreateInsuranceContractRequest
  property_count: 2
  slug: wordline-create-insurance-contract-request
- name: CreateInsuranceEventRequest
  property_count: 3
  slug: wordline-create-insurance-event-request
- name: CreateMandateRequest
  property_count: 20
  slug: wordline-create-mandate-request
- name: CreateOfflineReservationRequest
  property_count: 3
  slug: wordline-create-offline-reservation-request
- name: CreateOperationBonusRequest
  property_count: 12
  slug: wordline-create-operation-bonus-request
- name: CreateOperationPaymentRequest
  property_count: 12
  slug: wordline-create-operation-payment-request
- name: CreateOperationReimbursementRequest
  property_count: 10
  slug: wordline-create-operation-reimbursement-request
- name: CreatePostingRequest
  property_count: 4
  slug: wordline-create-posting-request
- name: CreateSuperFolderRequest
  property_count: 2
  slug: wordline-create-super-folder-request
- name: CreateTemporaryCreditLimitRequest
  property_count: 4
  slug: wordline-create-temporary-credit-limit-request
- name: CreateVelocityLimitOverrideRequest
  property_count: 12
  slug: wordline-create-velocity-limit-override-request
- name: ExchangeRateRequest
  property_count: 3
  slug: wordline-exchange-rate-request
- name: ExchangeRateResponse
  property_count: 5
  slug: wordline-exchange-rate-response
- name: GenerateCardLetterRequest
  property_count: 3
  slug: wordline-generate-card-letter-request
- name: GenerateChargebackRequest
  property_count: 6
  slug: wordline-generate-chargeback-request
- name: GetCvvRequest
  property_count: 1
  slug: wordline-get-cvv-request
- name: GetLinkedAccountStatesRequest
  property_count: 1
  slug: wordline-get-linked-account-states-request
- name: GetPinByPanRequest
  property_count: 8
  slug: wordline-get-pin-by-pan-request
- name: GetPinRequest
  property_count: 2
  slug: wordline-get-pin-request
- name: GlobalSearchContractRequest
  property_count: 9
  slug: wordline-global-search-contract-request
- name: GlobalSearchCorporateContractRequest
  property_count: 5
  slug: wordline-global-search-corporate-contract-request
- name: HoldingAddressData
  property_count: 2
  slug: wordline-holding-address-data
- name: HoldingData
  property_count: 4
  slug: wordline-holding-data
- name: HoldingListData
  property_count: 6
  slug: wordline-holding-list-data
- name: InterchangeFee
  property_count: 17
  slug: wordline-interchange-fee
- name: MerchantListData
  property_count: 6
  slug: wordline-merchant-list-data
- name: ModifyAccountFutureUpdateRequest
  property_count: 23
  slug: wordline-modify-account-future-update-request
- name: ModifyAccountRequest
  property_count: 34
  slug: wordline-modify-account-request
- name: ModifyAddressRequest
  property_count: 8
  slug: wordline-modify-address-request
- name: ModifyAllCardsBlockingInformationRequest
  property_count: 13
  slug: wordline-modify-all-cards-blocking-information-request
- name: ModifyAuthorizationRestrictionOverrideRequest
  property_count: 5
  slug: wordline-modify-authorization-restriction-override-request
- name: ModifyCardBlockingInformationRequest
  property_count: 11
  slug: wordline-modify-card-blocking-information-request
- name: ModifyCardContractRequest
  property_count: 25
  slug: wordline-modify-card-contract-request
- name: ModifyCompanyRequest
  property_count: 15
  slug: wordline-modify-company-request
- name: ModifyContactRequest
  property_count: 9
  slug: wordline-modify-contact-request
- name: ModifyContractFeeRequest
  property_count: 5
  slug: wordline-modify-contract-fee-request
- name: ModifyContractRequest
  property_count: 12
  slug: wordline-modify-contract-request
- name: ModifyCorporateContractRequest
  property_count: 12
  slug: wordline-modify-corporate-contract-request
- name: ModifyCustomerRequest
  property_count: 36
  slug: wordline-modify-customer-request
- name: ModifyVelocityLimitOverrideRequest
  property_count: 12
  slug: wordline-modify-velocity-limit-override-request
- name: Operation
  property_count: 4
  slug: wordline-operation
- name: PaymentAuthorisationRequest
  property_count: 2
  slug: wordline-payment-authorisation-request
- name: PaymentAuthorisationUpdateRequest
  property_count: 4
  slug: wordline-payment-authorisation-update-request
- name: PaymentDetailedInformation
  property_count: 4
  slug: wordline-payment-detailed-information
- name: PaymentIdentificationResponse
  property_count: 2
  slug: wordline-payment-identification-response
- name: PaymentInitiationResponse
  property_count: 3
  slug: wordline-payment-initiation-response
- name: PostHoldingResponse
  property_count: 2
  slug: wordline-post-holding-response
- name: PsuBankPreferences
  property_count: 3
  slug: wordline-psu-bank-preferences
- name: RemindPINRequest
  property_count: 10
  slug: wordline-remind-pinrequest
- name: ReorderPINRequest
  property_count: 10
  slug: wordline-reorder-pinrequest
- name: RetrieveCardPinStateRequest
  property_count: 3
  slug: wordline-retrieve-card-pin-state-request
- name: ReverseOperationBalanceAdjustmentRequest
  property_count: 10
  slug: wordline-reverse-operation-balance-adjustment-request
- name: ReverseOperationPaymentRequest
  property_count: 9
  slug: wordline-reverse-operation-payment-request
- name: ReverseOperationReimbursementRequest
  property_count: 9
  slug: wordline-reverse-operation-reimbursement-request
- name: SetPinByPanRequest
  property_count: 8
  slug: wordline-set-pin-by-pan-request
- name: SetPinRequest
  property_count: 3
  slug: wordline-set-pin-request
- name: ValidateCvvRequest
  property_count: 3
  slug: wordline-validate-cvv-request
jsonld:
- class_count: 120
  name: Wordline Context
  property_count: 574
  slug: wordline-context
layout: provider
modified: '2026-06-13'
name: Worldline
nav: Providers
network: true
overview: 'Worldline publishes 79 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account - AccountState API, Account API, Account - Authorization API, and 76 more. Tagged areas include Payments, Payment Processing, Acquiring, Issuing, and Open Banking.


  The Worldline catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Worldline''s developer surface includes getting-started guide, documentation, authentication, developer portal, support, signup flow, and 30 more developer resources.'
plans:
- name: Plans
  plan_count: 5
  slug: plans
random_paper: 4
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Worldline API Rules
  rule_count: 16
  severity_counts:
    error: 6
    hint: 0
    info: 4
    warn: 6
  slug: wordline-rules
scopes:
- name: Wordline Scopes
  scope_count: 7
  slug: wordline-scopes
  summary_line: 7 scopes · clientCredentials
score:
  band: developing
  composite: 49.1
  coverage:
    artifact_dirs: 33
    catalog_earned: 68.8
    catalog_earned_first_party: 0.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 25.0
    contract_governance: 35.6
    contract_quality: 66.4
    developer_ergonomics: 57.7
    discoverability: 71.4
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 47.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 83.1
      derived: 0
      marker_coverage: 0.0
      total: 71
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 38.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/wordline/wordline-2026-10-11T194447.png
security:
- kind: authentication
  name: Wordline Authentication
  slug: wordline-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Wordline Domain Security
  slug: wordline-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 5
skills:
- name: wordline-create-and-retrieve-customer
  slug: wordline-create-and-retrieve-customer
- name: wordline-direct-debit-workflow
  slug: wordline-direct-debit-workflow
- name: wordline-get-account-full-info
  slug: wordline-get-account-full-info
- name: wordline-payment-initiation-flow
  slug: wordline-payment-initiation-flow
- name: wordline-transaction-dispute
  slug: wordline-transaction-dispute
slug: wordline
tags:
- Payments
- Payment Processing
- Acquiring
- Issuing
- Open Banking
- Digital Banking
- Fintech
- Europe
website: https://worldline.com/
---

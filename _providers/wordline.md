---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 429
  human_in_the_loop: 29
  name: Wordline Agentic Access
  operation_count: 695
  slug: wordline-agentic-access
  summary_line: 695 operations · 429 acting · 29 human-in-the-loop
api_count: 79
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
- description: Account State Controller
  name: Worldline Account - AccountState API
  slug: wordline-account-accountstate-api
- description: Account Api Controller
  name: Worldline Account API
  slug: wordline-account-api
- description: Account Authorization Controller
  name: Worldline Account - Authorization API
  slug: wordline-account-authorization-api
- description: Account Authorization Restriction Controller
  name: Worldline Account - Authorization Restriction API
  slug: wordline-account-authorization-restriction-api
- description: Account Cvv2 Try Counter Controller
  name: Worldline Account - Cvv2 Try Counter API
  slug: wordline-account-cvv2-try-counter-api
- description: Account Future Updates Api Controller
  name: Worldline Account - Future Update API
  slug: wordline-account-future-update-api
- description: Account Insurance Contract Api Controller
  name: Worldline Account - Insurance Contract API
  slug: wordline-account-insurance-contract-api
- description: Account Offline Reservation Api Controller
  name: Worldline Account - Offline Reservation API
  slug: wordline-account-offline-reservation-api
- description: Account Operation Api Controller
  name: Worldline Account - Operation API
  slug: wordline-account-operation-api
- description: Account Statement Api Controller
  name: Worldline Account - Statement API
  slug: wordline-account-statement-api
- description: Account Temporary Credit Limit Api Controller
  name: Worldline Account - Temporary Credit Limit API
  slug: wordline-account-temporary-credit-limit-api
- description: Account Velocity Limit Controller
  name: Worldline Account - Velocity Limit API
  slug: wordline-account-velocity-limit-api
- description: Api Meta Info Api Controller
  name: Worldline Api Meta Info API
  slug: wordline-api-meta-info-api
- description: The Authentication Resource API from Worldline — 1 operation(s) for authentication resource.
  name: Worldline Authentication Resource API
  slug: wordline-authentication-resource-api
- description: The Authorization API from Worldline — 1 operation(s) for authorization.
  name: Worldline Authorization API
  slug: wordline-authorization-api
- description: The Bulk Payment Initiation Service (Extended service) API from Worldline — 10 operation(s) for bulk payment initiation service (extended service).
  name: Worldline Bulk Payment Initiation Service (Extended service) API
  slug: wordline-bulk-payment-initiation-service-extended-service-api
- description: Card Api Controller
  name: Worldline Card API
  slug: wordline-card-api
- description: Card Pin State
  name: Worldline Card - CardPinState API
  slug: wordline-card-cardpinstate-api
- description: Card Contract Api Controller
  name: Worldline Card Contract API
  slug: wordline-card-contract-api
- description: Card CVV Api Controller
  name: Worldline Card - CVV API
  slug: wordline-card-cvv-api
- description: Card EMV Controller
  name: Worldline Card - EMV API
  slug: wordline-card-emv-api
- description: Card Letter API Controller
  name: Worldline Card - Letter API
  slug: wordline-card-letter-api
- description: Card Linked Account State Controller
  name: Worldline Card - LinkedAccountState API
  slug: wordline-card-linkedaccountstate-api
- description: Card Order Api Controller
  name: Worldline Card - Order API
  slug: wordline-card-order-api
- description: Card Pin Api Controller
  name: Worldline Card - Pin API
  slug: wordline-card-pin-api
- description: Card Pin Try Counter Api Controller
  name: Worldline Card - Pin Try Counter API
  slug: wordline-card-pin-try-counter-api
- description: Company Address Api Controller
  name: Worldline Company - Address API
  slug: wordline-company-address-api
- description: Company Api Controller
  name: Worldline Company API
  slug: wordline-company-api
- description: Company Related Api Controller
  name: Worldline Company - Related API
  slug: wordline-company-related-api
- description: Contract Api Controller
  name: Worldline Contract API
  slug: wordline-contract-api
- description: Contract Global Search API Controller
  name: Worldline Contract - Global Search API
  slug: wordline-contract-global-search-api
- description: Corporate Contract API Controller
  name: Worldline Corporate Contract API
  slug: wordline-corporate-contract-api
- description: Corporate Contract Global Search API Controller
  name: Worldline Corporate Contract - Global Search API
  slug: wordline-corporate-contract-global-search-api
- description: Credit Transfer Api Controller
  name: Worldline Credit Transfer API
  slug: wordline-credit-transfer-api
- description: The Currency Conversion (Extended services) API from Worldline — 1 operation(s) for currency conversion (extended services).
  name: Worldline Currency Conversion (Extended services) API
  slug: wordline-currency-conversion-extended-services-api
- description: Customer Address Api Controller
  name: Worldline Customer - Address API
  slug: wordline-customer-address-api
- description: Customer Api Controller
  name: Worldline Customer API
  slug: wordline-customer-api
- description: Customer Related Api Controller
  name: Worldline Customer - Related API
  slug: wordline-customer-related-api
- description: The Debtor Preference Retrieval API from Worldline — 1 operation(s) for debtor preference retrieval.
  name: Worldline Debtor Preference Retrieval API
  slug: wordline-debtor-preference-retrieval-api
- description: Direct Debit Api Controller
  name: Worldline Direct Debit API
  slug: wordline-direct-debit-api
- description: Dispute Api Controller
  name: Worldline Dispute API
  slug: wordline-dispute-api
- description: Event Store Controller
  name: Worldline Event Store API
  slug: wordline-event-store-api
- description: The HealthCheck API from Worldline — 1 operation(s) for healthcheck.
  name: Worldline HealthCheck API
  slug: wordline-healthcheck-api
- description: The Holding API from Worldline — 3 operation(s) for holding.
  name: Worldline Holding API
  slug: wordline-holding-api
- description: The Interchange fee API from Worldline — 7 operation(s) for interchange fee.
  name: Worldline Interchange fee API
  slug: wordline-interchange-fee-api
- description: Issuer Api Controller
  name: Worldline Issuer API
  slug: wordline-issuer-api
- description: Issuer Velocity Limit Controller
  name: Worldline Issuer - Velocity Limit API
  slug: wordline-issuer-velocity-limit-api
- description: The Merchant API from Worldline — 4 operation(s) for merchant.
  name: Worldline Merchant API
  slug: wordline-merchant-api
- description: Message Subscription Api Controller
  name: Worldline Message - Subscription API
  slug: wordline-message-subscription-api
- description: Message Subscription Event Api Controller
  name: Worldline Message - Subscription Event API
  slug: wordline-message-subscription-event-api
- description: Message Subscription Service Api Controller
  name: Worldline Message - Subscription Service API
  slug: wordline-message-subscription-service-api
- description: Apple Pay Controller
  name: Worldline Mobile Payment Operations API
  slug: wordline-mobile-payment-operations-api
- description: Operation Global Search API Controller
  name: Worldline Operation - Global Search API
  slug: wordline-operation-global-search-api
- description: The Payment API from Worldline — 5 operation(s) for payment.
  name: Worldline Payment API
  slug: wordline-payment-api
- description: The Payment Initiation Service API from Worldline — 11 operation(s) for payment initiation service.
  name: Worldline Payment Initiation Service API
  slug: wordline-payment-initiation-service-api
- description: The Periodic Payment Initiation Service (Extended service) API from Worldline — 10 operation(s) for periodic payment initiation service (extended service).
  name: Worldline Periodic Payment Initiation Service (Extended service) API
  slug: wordline-periodic-payment-initiation-service-extended-service-api
- description: Product Override API Controller
  name: Worldline Product Override API
  slug: wordline-product-override-api
- description: The Refund Initiation Service V3 (Extended services) API from Worldline — 6 operation(s) for refund initiation service v3 (extended services).
  name: Worldline Refund Initiation Service V3 (Extended services) API
  slug: wordline-refund-initiation-service-v3-extended-services-api
- description: The Registration Resource API from Worldline — 1 operation(s) for registration resource.
  name: Worldline Registration Resource API
  slug: wordline-registration-resource-api
- description: The Relying Party Resource API from Worldline — 2 operation(s) for relying party resource.
  name: Worldline Relying Party Resource API
  slug: wordline-relying-party-resource-api
- description: The Retrieve transaction totals API from Worldline — 2 operation(s) for retrieve transaction totals.
  name: Worldline Retrieve transaction totals API
  slug: wordline-retrieve-transaction-totals-api
- description: The Retrieve transaction totals per brand API from Worldline — 2 operation(s) for retrieve transaction totals per brand.
  name: Worldline Retrieve transaction totals per brand API
  slug: wordline-retrieve-transaction-totals-per-brand-api
- description: The Scheduled Payment Initiation Service (Extended service) API from Worldline — 10 operation(s) for scheduled payment initiation service (extended service).
  name: Worldline Scheduled Payment Initiation Service (Extended service) API
  slug: wordline-scheduled-payment-initiation-service-extended-service-api
- description: The Site API from Worldline — 8 operation(s) for site.
  name: Worldline Site API
  slug: wordline-site-api
- description: The Statement API from Worldline — 4 operation(s) for statement.
  name: Worldline Statement API
  slug: wordline-statement-api
- description: The Terminal API from Worldline — 10 operation(s) for terminal.
  name: Worldline Terminal API
  slug: wordline-terminal-api
- description: The Token Resource API from Worldline — 1 operation(s) for token resource.
  name: Worldline Token Resource API
  slug: wordline-token-resource-api
- description: Transaction API Controller
  name: Worldline Transaction API
  slug: wordline-transaction-api
- description: Transaction Global Search API Controller
  name: Worldline Transaction - Global Search API
  slug: wordline-transaction-global-search-api
- description: The Transaction Lifecycle API from Worldline — 1 operation(s) for transaction lifecycle.
  name: Worldline Transaction Lifecycle API
  slug: wordline-transaction-lifecycle-api
- description: The User Resource API from Worldline — 2 operation(s) for user resource.
  name: Worldline User Resource API
  slug: wordline-user-resource-api
artifact_total: 86
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wordline-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wordline-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wordline-authentication.yml
- group: auth
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
- group: company
  title: ''
  type: Blog
  url: https://worldline.com/en/home/knowledgehub/blog.html
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
- group: commercial
  title: ''
  type: TermsOfService
  url: https://worldline.com/en/home/legal-notices.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://worldline.com/en/home/privacy-statement.html
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
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wordline.png
layout: provider
modified: '2026-06-13'
name: Worldline
nav: Providers
network: true
overview: 'Worldline publishes 71 APIs on the [APIs.io](https://apis.io/) network, including Account - AccountState API, Account API, Account - Authorization API, and 68 more. Tagged areas include Payments, Payment Processing, Acquiring, Issuing, and Open Banking.


  Worldline''s developer surface includes authentication, developer portal, engineering blog, support, signup flow, and 14 more developer resources.'
plans:
- name: Plans
  plan_count: 5
  slug: plans
random_paper: 56
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
scopes:
- name: Wordline Scopes
  scope_count: 7
  slug: wordline-scopes
  summary_line: 7 scopes · clientCredentials
score:
  band: thin
  composite: 41.1
  delta: 0.0
  facets:
    commercial_clarity: 73.7
    contract_quality: 53.1
    developer_ergonomics: 26.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 41.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 71
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 53.1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Wordline Authentication
  slug: wordline-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Wordline Domain Security
  slug: wordline-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wordline
tags:
- Payments
- Payment Processing
- Acquiring
- Issuing
- Open Banking
- Digital Banking
- FinTech
- Europe
website: https://worldline.com/
---

---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 23
apis:
- description: Barclays Smartpay Web Payment API enables businesses to accept payments on their website with real-time processing, secure encryption, and fraud prevention.
  name: Barclays Smartpay Web Payment API
  slug: barclaycard-smartpay-web-payment-api
- description: Verify the availability of funds in a Barclays Bank Ireland account in real-time.
  name: Barclays Bank Ireland Confirmation of Funds API
  slug: barclays-bank-ireland-confirmation-of-funds-api
- description: Access and manage account information and transaction history through UK Open Banking standards.
  name: Barclays Account and Transactions API
  slug: account-and-transactions-api
- description: Securely access and retrieve account information from Barclays Bank Ireland accounts.
  name: Barclays Bank Ireland Account Information API
  slug: barclays-bank-ireland-account-information-api
- description: Initiate payments from Barclays Bank Ireland accounts via PSD2-compliant API.
  name: Barclays Bank Ireland Payment Initiation API
  slug: barclays-bank-ireland-payment-initiation-api
- description: Verify the availability of funds in a Barclays account in real-time.
  name: Barclays Confirmation of Funds API
  slug: confirmation-of-funds-api
- description: Manage customer consent for third-party access to Barclays account data.
  name: Barclays Consent API
  slug: consent-api
- description: Programmatically register TPP client applications with Barclays for Open Banking access.
  name: Barclays Dynamic Client Registration API
  slug: dynamic-client-registration-api
- description: Receive real-time webhook notifications for account and transaction events.
  name: Barclays Event Notification API
  slug: event-notification-api
- description: Securely initiate and authorize payments from Barclays accounts via Open Banking.
  name: Barclays Payment Initiation API
  slug: payment-initiation-api
- description: Find the nearest Barclays ATMs with details on available services and operating hours.
  name: Barclays ATM Locator API
  slug: atm-locator-api
- description: Find Barclays bank branches with addresses, phone numbers, and operating hours.
  name: Barclays Branch Locator API
  slug: branch-locator-api
- description: Access Barclays FCA-mandated service performance metrics data.
  name: Barclays FCA Service Metrics API
  slug: fca-service-metrics-api
- description: Access detailed information about Barclays banking products including rates, fees, and eligibility.
  name: Barclays Product Details API
  slug: product-details-api
- description: Access and manage Barclays account information via Open Banking standards.
  name: Barclays Accounts API
  slug: accounts-api
- description: Secure OAuth2 authentication for accessing Barclays Open Banking APIs.
  name: Barclays Authentication API
  slug: authentication-api
- description: Integrate credit card application functionality with real-time status updates.
  name: Barclays Card Application API
  slug: card-application-api
- description: Secure cryptographic key exchange for encrypted API communication with Barclays.
  name: Barclays Cryptography Key Exchange API
  slug: cryptography-key-exchange-api
- description: Integrate digital wallet functionality for mobile payments and account management.
  name: Barclays Digital Wallet API
  slug: digital-wallet-api
- description: Securely make and receive payments with fraud detection and real-time tracking.
  name: Barclays Payments API
  slug: payments-api
- description: Integrate loyalty programs and sync rewards data with Barclays customer accounts.
  name: Barclays Rewards Loyalty Sync API
  slug: rewards-loyalty-sync-api
- description: Enable customers to pay with Barclays Rewards points at merchant point-of-sale.
  name: Barclays Rewards Pay with Points API
  slug: rewards-pay-with-points-api
- description: Access detailed transaction history and spending analytics for Barclays accounts.
  name: Barclays Transactions API
  slug: transactions-api
artifact_total: 53
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/barclays-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/barclays-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://home.barclays/insights/barclays-insights/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Barclays
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/barclays-bank
- group: start
  title: ''
  type: Portal
  url: https://developer.barclays.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.barclays.com/catalogue
- group: operate
  title: ''
  type: Support
  url: https://developer.barclays.com/support/help-guides
- group: start
  title: ''
  type: Login
  url: https://developer.barclays.com/login
- group: start
  title: ''
  type: Signup
  url: https://drm.developer.barclays.com/s/registration
- group: other
  title: ''
  type: Knowledgebase
  url: https://developer.barclays.com/support/knowledge-base
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.barclays.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developer.barclays.com/privacy-policy
- group: design
  title: ''
  type: SpectralRules
  url: rules/barclays-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/barclays-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/barclays-context.jsonld
created: '2025-02-21'
description: Barclays is a multinational financial services company providing retail and commercial banking, investment banking, wealth management, and credit cards. The Barclays API Exchange (developer.barclays.com) offers 22+ APIs covering open banking account information, payment initiation, confirmation of funds, ATM/branch location, rewards, digital wallet, and more, compliant with UK Open Banking and EU PSD2 standards.
examples:
- key_count: 3
  name: Account Example
  slug: account-example
- key_count: 3
  name: Transaction Example
  slug: transaction-example
features:
- description: PSD2 and UK Open Banking compliant account balance and transaction access.
  name: Open Banking Account Information
- description: Secure third-party payment initiation from customer accounts.
  name: Payment Initiation
- description: Real-time verification of available funds for payment authorization.
  name: Confirmation of Funds
- description: Location services for Barclays ATMs and branches worldwide.
  name: ATM and Branch Locator
- description: Real-time webhook notifications for account and transaction events.
  name: Event Notifications
- description: Automated TPP registration for Open Banking API access.
  name: Dynamic Client Registration
- description: Loyalty program integration and pay-with-points capabilities.
  name: Rewards and Loyalty
- description: Mobile payment and digital wallet integration.
  name: Digital Wallet
- description: Credit card application submission and status tracking.
  name: Card Applications
- description: Mandated service performance metrics for regulatory reporting.
  name: FCA Compliance Metrics
finops:
- name: Barclays Finops
  service_category: API
  slug: barclays-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/barclays.png
json_schemas:
- name: Account
  property_count: 7
  slug: account
- name: PaymentRequest
  property_count: 5
  slug: payment
- name: Transaction
  property_count: 9
  slug: transaction
json_structures:
- name: Barclays Json Structure
  property_count: 0
  slug: barclays-json-structure
jsonld:
- class_count: 2
  name: Barclays Context
  property_count: 17
  slug: barclays-context
layout: provider
modified: '2026-04-21'
name: Barclays
nav: Providers
network: true
overview: 'Barclays publishes 23 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Credit Cards, Finance, Open Banking, and Payments.


  The Barclays catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Barclays'' developer surface includes engineering blog, developer portal, documentation, support, signup flow, and 11 more developer resources.'
plans:
- name: Barclays Plans Pricing
  plan_count: 3
  slug: barclays-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Barclays Rate Limits
  slug: barclays-rate-limits
rules:
- name: Barclays API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: barclays-jsonschema-spectral-rules
- name: Barclays API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: barclays-spectral-rules
score:
  band: thin
  composite: 40.7
  delta: -7.6
  facets:
    commercial_clarity: 73.7
    contract_quality: 12.9
    developer_ergonomics: 23.9
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 48.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/barclays/refs/heads/main/screenshots/barclays-2026-06-20T173004.png
security:
- kind: domain-security
  name: Barclays Domain Security
  slug: barclays-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Barclays Vulnerability Disclosure
  slug: barclays-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: barclays
tags:
- Banking
- Credit Cards
- Finance
- Open Banking
- Payments
- PSD2
- UK Banking
use_cases:
- description: Aggregate Barclays account data in budgeting and financial planning apps.
  name: Personal Finance Management
- description: Initiate payments directly from customer bank accounts via PSD2.
  name: Open Banking Payments
- description: Accept Barclays-branded payments via Smartpay Web Payment API.
  name: E-Commerce Checkout
- description: Embed ATM and branch location search in apps and websites.
  name: Branch and ATM Finder
- description: Integrate Barclays Rewards with merchant loyalty programs.
  name: Loyalty Integration
- description: Enable online credit card applications through partner platforms.
  name: Credit Card Origination
website: https://developer.barclays.com/
---

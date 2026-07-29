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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Airwallex Agentic Access
  operation_count: 18
  slug: airwallex-agentic-access
  summary_line: 18 operations · 10 acting
api_count: 14
apis:
- description: The Airwallex Payment Acceptance API enables businesses to accept online payments globally. Supports credit and debit cards, local payment methods, and 3D Secure. Available as hosted checkout or embed
  name: Airwallex Payment Acceptance API
  slug: payment-acceptance
- description: The Airwallex Global Accounts API enables businesses to create and manage multi-currency accounts. Supports account creation, balance management, account statements, and receiving funds in multiple cu
  name: Airwallex Global Accounts API
  slug: global-accounts
- description: The Airwallex Payouts API enables businesses to send cross-border payments to suppliers, contractors, and employees globally. Supports bank transfers to 150+ countries, bulk payouts, and beneficiary m
  name: Airwallex Payouts API
  slug: payouts
- description: The Airwallex FX API provides access to real-time foreign exchange rates and currency conversion. Supports spot conversions, rate quotes, and conversion history for 60+ currencies.
  name: Airwallex FX API
  slug: fx
- description: The Airwallex Issuing API enables businesses to create and manage virtual and physical corporate cards for employee spending. Supports card issuance, spend controls, transaction management, and expens
  name: Airwallex Issuing API
  slug: issuing
- description: The Airwallex Platform API enables businesses to embed financial services into their products. Supports merchant onboarding, sub-account management, platform payments, and split payouts for marketplac
  name: Airwallex Platform API
  slug: platform
- description: The Authentication API from Airwallex — 1 operation(s) for authentication.
  name: Airwallex Authentication API
  slug: airwallex-authentication-api
- description: The Balances API from Airwallex — 1 operation(s) for balances.
  name: Airwallex Balances API
  slug: airwallex-balances-api
- description: The Beneficiaries API from Airwallex — 3 operation(s) for beneficiaries.
  name: Airwallex Beneficiaries API
  slug: airwallex-beneficiaries-api
- description: The Customers API from Airwallex — 2 operation(s) for customers.
  name: Airwallex Customers API
  slug: airwallex-customers-api
- description: The Payment Intents API from Airwallex — 5 operation(s) for payment intents.
  name: Airwallex Payment Intents API
  slug: airwallex-payment-intents-api
- description: The Payouts API from Airwallex — 2 operation(s) for payouts.
  name: Airwallex Payouts API
  slug: airwallex-payouts-api
- description: The Refunds API from Airwallex — 2 operation(s) for refunds.
  name: Airwallex Refunds API
  slug: airwallex-refunds-api
- description: The Transfers API from Airwallex — 2 operation(s) for transfers.
  name: Airwallex Transfers API
  slug: airwallex-transfers-api
artifact_total: 62
collections:
- collection_type: postman
  name: Airwallex Open Authentication API
  slug: postman-airwallex-authentication-api
- collection_type: postman
  name: Airwallex Open Authentication Balances API
  slug: postman-airwallex-balances-api
- collection_type: postman
  name: Airwallex Open Authentication Beneficiaries API
  slug: postman-airwallex-beneficiaries-api
- collection_type: postman
  name: Airwallex Open Authentication Customers API
  slug: postman-airwallex-customers-api
- collection_type: postman
  name: Airwallex Open Authentication Payment Intents API
  slug: postman-airwallex-payment-intents-api
- collection_type: postman
  name: Airwallex Open Authentication Payouts API
  slug: postman-airwallex-payouts-api
- collection_type: postman
  name: Airwallex Open Authentication Refunds API
  slug: postman-airwallex-refunds-api
- collection_type: postman
  name: Airwallex Open Authentication Transfers API
  slug: postman-airwallex-transfers-api
- collection_type: open
  name: Airwallex Open API
  slug: open-airwallex
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/airwallex/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/airwallex-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/airwallex-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/airwallex-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airwallex-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/airwallex-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airwallex
- group: start
  title: ''
  type: Portal
  url: https://www.airwallex.com
- group: start
  title: ''
  type: GettingStarted
  url: https://www.airwallex.com/docs/api
- group: docs
  title: ''
  type: Documentation
  url: https://www.airwallex.com/docs/api#/Introduction
- group: auth
  title: ''
  type: Authentication
  url: https://www.airwallex.com/docs/api#/Payment_Acceptance/Authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://www.airwallex.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.airwallex.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.airwallex.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.airwallex.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/airwallex
- group: build
  title: Airwallex CLI
  type: CLI
  url: https://github.com/airwallex/airwallex-cli
- group: build
  title: Magento Plugin
  type: SDKs
  url: https://github.com/airwallex/paymentacceptance-plugin-magento
- group: build
  title: Salesforce Commerce Cloud
  type: SDKs
  url: https://github.com/airwallex/airwallex-salesforce-commerce-cloud-cartridge
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/airwallex/refs/heads/main/rules/airwallex-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/airwallex/refs/heads/main/vocabulary/airwallex-vocabulary.yaml
created: '2025-02-17'
description: Airwallex is a financial technology company that specializes in providing global payment solutions for businesses. Their platform enables companies to accept payments, manage multi-currency accounts, convert currencies at competitive rates, send cross-border payments, issue corporate cards, and embed financial services into their own products. Airwallex serves businesses in over 150 countries with APIs for payment acceptance, FX, accounts, transfers, and embedded finance.
examples:
- key_count: 7
  name: Airwallex Account Example
  slug: airwallex-account-example
- key_count: 8
  name: Airwallex Fx Quote Example
  slug: airwallex-fx-quote-example
- key_count: 13
  name: Airwallex Payment Intent Example
  slug: airwallex-payment-intent-example
- key_count: 12
  name: Airwallex Transfer Example
  slug: airwallex-transfer-example
features:
- description: Accept payments in 180+ currencies via cards and local payment methods.
  name: Global Payment Acceptance
- description: Hold, manage, and convert funds in 60+ currencies.
  name: Multi-Currency Accounts
- description: Send payments to 150+ countries with competitive FX rates.
  name: Cross-Border Payouts
- description: Real-time currency conversion at competitive exchange rates.
  name: FX Conversion
- description: Issue virtual and physical Visa cards for employee spending.
  name: Corporate Card Issuing
- description: Embed Airwallex financial services into your own platform.
  name: Embedded Finance
- description: iOS, Android, React Native, and Flutter SDKs for in-app payments.
  name: Mobile SDKs
- description: Real-time event notifications for payment status changes.
  name: Webhooks
- description: Built-in fraud detection and risk scoring via the Airwallex Risk SDK.
  name: Risk Management
finops:
- name: Airwallex Finops
  service_category: API
  slug: airwallex-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/airwallex.png
json_schemas:
- name: Account
  property_count: 7
  slug: airwallex-account
- name: FxQuote
  property_count: 8
  slug: airwallex-fx-quote
- name: PaymentIntent
  property_count: 13
  slug: airwallex-payment-intent
- name: Transfer
  property_count: 12
  slug: airwallex-transfer
json_structures:
- name: Airwallex Account Structure
  property_count: 7
  slug: airwallex-account-structure
- name: Airwallex Fx Quote Structure
  property_count: 8
  slug: airwallex-fx-quote-structure
- name: Airwallex Payment Intent Structure
  property_count: 13
  slug: airwallex-payment-intent-structure
- name: Airwallex Transfer Structure
  property_count: 12
  slug: airwallex-transfer-structure
jsonld:
- class_count: 6
  name: Airwallex Context
  property_count: 19
  slug: airwallex-context
layout: provider
modified: '2026-04-19'
name: Airwallex
nav: Providers
network: true
overview: 'Airwallex publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Balances API, Beneficiaries API, and 5 more. Tagged areas include Cross-Border Payments, FinTech, Foreign Exchange, Payments, and Global.


  The Airwallex catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Airwallex''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, engineering blog, CLI, and 14 more developer resources.'
plans:
- name: Airwallex Plans Pricing
  plan_count: 3
  slug: airwallex-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Airwallex Rate Limits
  slug: airwallex-rate-limits
rules:
- name: Airwallex API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: airwallex-jsonschema-spectral-rules
- name: Airwallex API Rules
  rule_count: 32
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 17
  slug: airwallex-spectral-rules
score:
  band: strong
  composite: 63.6
  delta: -5.3
  facets:
    commercial_clarity: 78.9
    contract_quality: 63.3
    developer_ergonomics: 58.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 68.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 62.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/airwallex/refs/heads/main/screenshots/airwallex-2026-06-20T171444.png
security:
- kind: authentication
  name: Airwallex Authentication
  slug: airwallex-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Airwallex Domain Security
  slug: airwallex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Airwallex Vulnerability Disclosure
  slug: airwallex-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Airwallex Trust Center
  slug: airwallex-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: airwallex
tags:
- Cross-Border Payments
- FinTech
- Foreign Exchange
- Payments
- Global
- Embedded Finance
- Multi-Currency
use_cases:
- description: Accept global payments on e-commerce stores and marketplaces.
  name: E-Commerce Checkout
- description: Pay international suppliers and contractors efficiently.
  name: Cross-Border B2B Payments
- description: Issue cards and track employee spending globally.
  name: Employee Expense Management
- description: Manage treasury operations across multiple currencies.
  name: Multi-Currency Treasury
- description: Collect and distribute payments to marketplace sellers.
  name: Marketplace Split Payments
- description: Embed payment processing into SaaS platforms.
  name: SaaS Platform Monetization
- description: Pay remote workers and freelancers in their local currencies.
  name: Freelancer Payouts
website: https://www.airwallex.com
---

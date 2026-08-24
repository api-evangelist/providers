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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Ravelin Agentic Access
  operation_count: 24
  slug: ravelin-agentic-access
  summary_line: 24 operations · 24 acting
api_count: 13
apis:
- description: A purpose-built API surface for Payment Service Providers (PSPs) embedding Ravelin's risk scoring and dispute capture into their own merchant-facing product. Exposes Score, Transaction, Dispute, and t
  name: Ravelin PSP API
  slug: ravelin-psp-api
- description: Outbound webhook callbacks delivered by Ravelin to merchant-configured endpoints when manual reviews, order decisions, or refund decisions are completed in the Ravelin dashboard. Used to keep order-ma
  name: Ravelin Callbacks API
  slug: ravelin-callbacks-api
- description: EMV 3DS 2.x authentication operations.
  name: Ravelin 3D Secure API
  slug: ravelin-3d-secure-api
- description: Login and registration events for account takeover scoring.
  name: Ravelin Authentication API
  slug: ravelin-authentication-api
- description: Pre-payment order risk scoring.
  name: Ravelin Checkout API
  slug: ravelin-checkout-api
- description: Cross-merchant identity and signal sharing.
  name: Ravelin Connect API
  slug: ravelin-connect-api
- description: Customer profile, identity, and label events.
  name: Ravelin Customer API
  slug: ravelin-customer-api
- description: Chargebacks, disputes, and reclaim events.
  name: Ravelin Disputes API
  slug: ravelin-disputes-api
- description: Outbound payouts to suppliers and recipients.
  name: Ravelin Payouts API
  slug: ravelin-payouts-api
- description: Refund requests and decisioning.
  name: Ravelin Refunds API
  slug: ravelin-refunds-api
- description: Supplier, driver, courier, and seller events for marketplace risk.
  name: Ravelin Supplier API
  slug: ravelin-supplier-api
- description: Payment attempts, captures, refunds, and authorizations.
  name: Ravelin Transactions API
  slug: ravelin-transactions-api
- description: Voucher, promo, and payment-method voucher events.
  name: Ravelin Vouchers API
  slug: ravelin-vouchers-api
artifact_total: 56
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ravelin Server 3D Secure API
  slug: open-ravelin-3d-secure-api
- collection_type: open
  name: Ravelin 3D Secure Server API
  slug: open-ravelin-3ds-server-api
- collection_type: open
  name: Ravelin Server 3D Secure Authentication API
  slug: open-ravelin-authentication-api
- collection_type: open
  name: Ravelin Server 3D Secure Callbacks API
  slug: open-ravelin-callbacks-api
- collection_type: open
  name: Ravelin Server 3D Secure Checkout API
  slug: open-ravelin-checkout-api
- collection_type: open
  name: Ravelin Server 3D Secure Connect API
  slug: open-ravelin-connect-api
- collection_type: open
  name: Ravelin Server 3D Secure Customer API
  slug: open-ravelin-customer-api
- collection_type: open
  name: Ravelin Server 3D Secure Disputes API
  slug: open-ravelin-disputes-api
- collection_type: open
  name: Ravelin Merchant API
  slug: open-ravelin-merchant-api
- collection_type: open
  name: Ravelin Server 3D Secure Payouts API
  slug: open-ravelin-payouts-api
- collection_type: open
  name: Ravelin Server 3D Secure Refunds API
  slug: open-ravelin-refunds-api
- collection_type: open
  name: Ravelin Server 3D Secure Supplier API
  slug: open-ravelin-supplier-api
- collection_type: open
  name: Ravelin Server 3D Secure Transactions API
  slug: open-ravelin-transactions-api
- collection_type: open
  name: Ravelin Server 3D Secure Vouchers API
  slug: open-ravelin-vouchers-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ravelin-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ravelin-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ravelin-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ravelin-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.ravelin.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.ravelin.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ravelin.com/merchant/
- group: start
  title: ''
  type: Signup
  url: https://www.ravelin.com/contact-us
- group: start
  title: ''
  type: Login
  url: https://dashboard.ravelin.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ravelin.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ravelin.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ravelin.com/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://support.ravelin.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.ravelin.com/
- group: company
  title: ''
  type: Blog
  url: https://www.ravelin.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://updates.ravelin.com/en
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://updates.ravelin.com/en
- group: company
  title: ''
  type: Careers
  url: https://www.ravelin.com/careers
- group: operate
  title: ''
  type: ContactUs
  url: https://www.ravelin.com/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unravelin
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ravelin/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ravelinhq
- group: build
  title: ''
  type: SDKs
  url: https://github.com/unravelin/ravelinjs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/unravelin/ravelin-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/unravelin/ravelin-core-ios-xcframework-distribution
- group: build
  title: ''
  type: SDKs
  url: https://github.com/unravelin/ravelin-encrypt-ios-xcframework-distribution
- group: build
  title: ''
  type: SDKs
  url: https://github.com/unravelin/ravelin-3ds-sdk-ios-xcframework-distribution
- group: build
  title: ''
  type: SDKs
  url: https://developer.ravelin.com/merchant/libraries-and-sdks/android/core-sdk/android/
- group: docs
  title: ''
  type: ReferenceImplementation
  url: https://github.com/unravelin/ravelin-3ds-demo
- group: auth
  title: ''
  type: Compliance
  url: https://www.ravelin.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.ravelin.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.ravelin.com/
created: '2026-05-25'
description: Ravelin is a London-based fraud detection and prevention platform offering AI-native, real-time decisioning APIs for online merchants. Their products cover payment fraud, chargeback recovery, account takeover (ATO) protection, refund and policy abuse, marketplace and supplier fraud, and a PSP-agnostic 3D Secure server. Ravelin combines per-merchant machine learning models, graph network analysis, and a consortium database of identity signals to score every customer interaction across checkout, login, registration, and post-transaction events.
features:
- description: Custom ML models trained and tuned to each merchant's traffic, products, and fraud patterns rather than a single global model.
  name: Per-Merchant Machine Learning
- description: Link analysis across customers, devices, payment instruments, and addresses to surface hidden fraud rings and shared-identity clusters.
  name: Graph Network Analysis
- description: A shared identity-signals consortium spanning 9+ billion identity elements used to enrich risk scoring across all merchants.
  name: Consortium Identity Database
- description: ALLOW / REVIEW / PREVENT decisions returned synchronously on every checkout, login, registration, voucher, and transaction event.
  name: Real-Time Decisioning
- description: A 3DS Server that works with any acquirer or PSP, supports dynamic exemption routing, and is bundled with native iOS and Android 3DS SDKs.
  name: PSP-Agnostic 3D Secure
- description: Built-in dashboard for human review of borderline cases with webhook callbacks to sync decisions back to the merchant's order management system.
  name: Manual Review Workflow
- description: Merchant-authored rules layered on top of ML scores, executed in active or passive mode so new rules can be safely shadow-tested before going live.
  name: Rules Engine
- description: A built-in 50 events-per-minute-per-customer guardrail that returns a PREVENT action with source RATE_LIMIT to defend against scripted abuse.
  name: Per-Customer Rate Limiting
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ravelin.png
integrations:
- description: Integrates with major PSPs and acquirers via the PSP API and the PSP-agnostic 3DS Server.
  name: Payment Service Providers
- description: Order, refund, and manual-review decisions are pushed to downstream OMS via webhook callbacks.
  name: Order Management Systems
- description: Native iOS Core, Encrypt, and 3DS SDKs distributed as XCFrameworks.
  name: iOS Applications
- description: Native Android Core and 3DS SDKs with bundled ProGuard rules.
  name: Android Applications
- description: RavelinJS browser SDK for device fingerprinting, encryption, and 3DS browser flows.
  name: Web Applications
layout: provider
modified: '2026-05-25'
name: Ravelin
nav: Providers
network: true
overview: 'Ravelin publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Callbacks API, 3D Secure API, Authentication API, and 9 more. Tagged areas include Fraud Prevention, Fraud Detection, Chargeback Prevention, Account Takeover, and 3D Secure.


  Ravelin''s developer surface includes authentication, developer portal, documentation, signup flow, pricing, support, engineering blog, and 25 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 37.7
  delta: 0.0
  facets:
    access_clarity: 25.0
    commercial_clarity: 25.0
    contract_governance: 0.0
    contract_quality: 57.8
    developer_ergonomics: 54.8
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 35.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ravelin/refs/heads/main/screenshots/ravelin-2026-06-20T192610.png
security:
- kind: authentication
  name: Ravelin Authentication
  slug: ravelin-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ravelin Domain Security
  slug: ravelin-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ravelin Vulnerability Disclosure
  slug: ravelin-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ravelin
solutions:
- description: End-to-end protection of the checkout and transaction surface for online merchants.
  name: Payment Fraud
- description: Login, registration, and credential-event scoring for ATO prevention.
  name: Account Security
- description: Detection of refund and return abuse across orders and channels.
  name: Refund Abuse
- description: Supplier, courier, and seller risk scoring for marketplaces and gig platforms.
  name: Marketplace Risk
- description: PSP-agnostic 3DS Server with exemption routing and native mobile SDKs.
  name: 3D Secure and Transaction Optimization
tags:
- Fraud Prevention
- Fraud Detection
- Chargeback Prevention
- Account Takeover
- 3D Secure
- Risk Scoring
- Payments
- Machine-Learning
use_cases:
- description: Scoring checkout and transaction events to block fraudulent orders before they ship and reduce card scheme chargebacks.
  name: Online Payment Fraud and Chargeback Prevention
- description: Risk-scoring login events to detect credential stuffing, breach reuse, and session hijacking attempts in real time.
  name: Account Takeover (ATO) Protection
- description: Detecting customers who systematically exploit refund, return, and goodwill policies across orders and channels.
  name: Refund and Policy Abuse
- description: Scoring voucher and promo redemption events to stop bonus stacking, multi-accounting, and referral fraud.
  name: Promo, Voucher, and Loyalty Abuse
- description: Risk-scoring suppliers, drivers, couriers, sellers, and other marketplace participants to detect collusion and onboarding fraud.
  name: Marketplace and Supplier Fraud
- description: Running EMV 3DS 2.x authentication through Ravelin's 3DS Server with dynamic exemption routing to maximize approval and shift liability where appropriate.
  name: 3D Secure and SCA Optimization
website: https://www.ravelin.com/
---

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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 9
apis:
- description: Enables integration of the Google Pay payment method into web applications, allowing merchants to accept payments from cards saved to Google Accounts. The API provides JavaScript client methods for im
  name: Google Pay API
  slug: google-pay-api
- description: Enables integration of Google Pay into Android applications, allowing users to pay with cards saved to their Google Account. The API provides methods to check payment readiness and load payment data f
  name: Google Pay API for Android
  slug: google-pay-api-for-android
- description: APIs for creating and managing digital passes for Google Wallet, including loyalty cards, event tickets, boarding passes, transit tickets, gift cards, offers, and generic passes. Issuers can define pa
  name: Google Wallet API
  slug: google-wallet-api
- description: Provides services hosted by Google for processing facilitated payment events as part of Google Standard Payments. Payment integrators use this API to report and manage transaction events within the Go
  name: Google Pay Facilitated Transaction Event API
  slug: google-pay-facilitated-transaction-event-api
- description: Enables payment integrators to enroll cards, retrieve virtual card numbers, manage transactions, and handle authentication challenges for virtual card payments. Used by issuers and payment service pro
  name: Google Pay Virtual Cards API
  slug: google-pay-virtual-cards-api
- description: Allows card issuers to provision payment cards directly into Google Pay and Google Wallet from their own applications. Issuers can set default payment tokens, manage token lifecycle, and enable push p
  name: Google Pay Push Provisioning API
  slug: google-pay-push-provisioning-api
- description: Enables Android applications to scan credit and debit cards using the device camera to extract card number and expiration date through on-device optical character recognition. Processing occurs entire
  name: Google Pay Payment Card Recognition API
  slug: google-pay-payment-card-recognition-api
- description: A toolkit for developers in India to integrate their Android, iOS, and web applications with Google Pay for accepting UPI and card-based payments. Supports merchant onboarding, payment initiation, and
  name: Google Pay India Merchant SDK
  slug: google-pay-india-merchant-sdk
- description: A standard for securely and efficiently exchanging commerce data between merchant and platform systems to enable checkout experiences directly on Google surfaces including Search and Gemini. Merchants
  name: Google Universal Commerce Protocol
  slug: google-universal-commerce-protocol
artifact_total: 14
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-pay-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-pay-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/google-pay
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/pay
- group: docs
  title: ''
  type: Brand Guidelines
  url: https://developers.google.com/pay/api/web/guides/brand-guidelines
- group: commercial
  title: ''
  type: TermsOfService
  url: https://payments.developers.google.com/terms/sellertos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/pay/api/web/guides/tutorial
- group: build
  title: ''
  type: SDKs
  url: https://developers.google.com/pay/api/web/guides/resources
- group: start
  title: ''
  type: Console
  url: https://pay.google.com/business/console/
- group: operate
  title: ''
  type: StatusPage
  url: https://developers.google.com/pay/api/status
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/pay/api/web/support
- group: company
  title: ''
  type: Blog
  url: https://developers.googleblog.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.google.com/pay/api/web/support/release-notes
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/google-pay
- group: operate
  title: ''
  type: FAQ
  url: https://developers.google.com/pay/api/web/support/faq
created: '2024-01-01'
description: Google Pay APIs enable payment processing and digital wallet functionality for apps and websites.
finops:
- name: Google Pay Finops
  service_category: API
  slug: google-pay-finops
image: https://developers.google.com/pay/api/images/brand-guidelines/google-pay-mark.png
layout: provider
modified: '2026-04-28'
name: Google Pay
nav: Providers
network: true
overview: 'Google Pay publishes 2 APIs on the [APIs.io](https://apis.io/) network, including Google Wallet API, and 1 more. Tagged areas include Contactless Payments, Digital Wallet, Mobile Payments, and Payments.


  Google Pay''s developer surface includes developer portal, getting-started guide, developer console, support, engineering blog, changelog, FAQ, and 9 more developer resources.'
plans:
- name: Google Pay Plans Pricing
  plan_count: 3
  slug: google-pay-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 5
  name: Google Pay Rate Limits
  slug: google-pay-rate-limits
score:
  band: thin
  composite: 41.4
  delta: -4.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 32.3
    developer_ergonomics: 39.1
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 68.4
  previous_composite: 45.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-pay/refs/heads/main/screenshots/google-pay-2026-06-20T182221.png
security:
- kind: domain-security
  name: Google Pay Domain Security
  slug: google-pay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Pay Vulnerability Disclosure
  slug: google-pay-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-pay
tags:
- Contactless Payments
- Digital Wallet
- Mobile Payments
- Payments
website: https://developers.google.com/pay
---

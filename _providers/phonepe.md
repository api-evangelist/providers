---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Phonepe Agentic Access
  operation_count: 4
  slug: phonepe-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 21
apis:
- description: Server-to-server REST API for creating PhonePe checkout orders, kicking off UPI / card / wallet / netbanking flows, and retrieving payment status. Issues redirect or intent URLs for the buyer to autho
  name: PhonePe Payment Gateway API
  slug: pg
- description: Initiates refunds against completed PhonePe transactions and retrieves refund status. Supports partial and full refunds.
  name: PhonePe Refunds API
  slug: refunds
- description: Polling endpoint to retrieve the current status of a payment order by merchant order ID. Used to reconcile in-store and online flows after buyer authorisation.
  name: PhonePe Check Payment Status API
  slug: status
- description: Server-to-server callback that PhonePe POSTs to a merchant-configured URL on terminal payment events. Payloads are signed (X-VERIFY) so the merchant can verify authenticity before acting on the result
  name: PhonePe S2S Callback / Webhook
  slug: webhook
- description: Generates per-order dynamic QR codes for in-store collection, with order-linked status retrieval and callbacks. Targeted at retail counters and quick-service merchants.
  name: PhonePe Dynamic QR Solution
  slug: dynamic-qr
- description: Onboards a merchant store with a static PhonePe QR code that maps collected funds to the merchant account. Lower-touch alternative to dynamic QR for fixed-price kiosks and stalls.
  name: PhonePe Integrated Static QR
  slug: static-qr
- description: 'Merchant-initiated UPI collect-request flow: the merchant raises a payment request to a customer''s UPI handle, the customer approves in their UPI app, and the merchant is notified on completion.'
  name: PhonePe Collect Call Solution
  slug: collect-call
- description: Integration with PhonePe's EDC (Electronic Data Capture / POS) terminals, allowing merchant systems to push order amounts to the terminal and receive completion events.
  name: PhonePe Integrated EDC Solution
  slug: edc
- description: Native Android SDK that embeds the PhonePe checkout experience inside a merchant app, supporting the full PG flow across UPI and other payment methods.
  name: PhonePe Android SDK
  slug: android-sdk
- description: Native iOS SDK that embeds the PhonePe checkout experience inside a merchant iOS app.
  name: PhonePe iOS SDK
  slug: ios-sdk
- description: Flutter plugin wrapping the PhonePe Android and iOS SDKs for cross-platform mobile checkout.
  name: PhonePe Flutter SDK
  slug: flutter-sdk
- description: React Native plugin wrapping the PhonePe Android and iOS SDKs for cross-platform mobile checkout.
  name: PhonePe React Native SDK
  slug: react-native-sdk
- description: Ionic plugin wrapping the PhonePe Android and iOS SDKs for hybrid mobile checkout.
  name: PhonePe Ionic SDK
  slug: ionic-sdk
- description: Server-side Java SDK that wraps the PhonePe PG REST API, handling X-VERIFY signing, request modelling, and response parsing.
  name: PhonePe Java Backend SDK
  slug: java-sdk
- description: Server-side Python SDK wrapping the PhonePe PG REST API.
  name: PhonePe Python Backend SDK
  slug: python-sdk
- description: Server-side Node.js SDK wrapping the PhonePe PG REST API.
  name: PhonePe Node.js Backend SDK
  slug: node-sdk
- description: Server-side PHP SDK wrapping the PhonePe PG REST API.
  name: PhonePe PHP Backend SDK
  slug: php-sdk
- description: PhonePe's Indus AppStore is an India-first native Android app marketplace with a developer console for app submission, listings, releases, and analytics, positioning itself as a local alternative to G
  name: Indus AppStore Developer Platform
  slug: indus-appstore
- description: Create payment orders.
  name: PhonePe Checkout API
  slug: phonepe-checkout-api
- description: Retrieve the status of a payment order.
  name: PhonePe Order Status API
  slug: phonepe-order-status-api
- description: Initiate and track refunds.
  name: PhonePe Refunds API
  slug: phonepe-refunds-api
artifact_total: 29
collections:
- collection_type: open
  name: PhonePe Payment Gateway API
  slug: open-phonepe
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/phonepe-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/phonepe-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/phonepe-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/phonepe-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.phonepe.com/business-solutions/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.phonepe.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/phonepe
- group: build
  title: ''
  type: GitHub
  url: https://github.com/PhonePe
- group: other
  title: ''
  type: AppStore
  url: https://www.indusappstore.com/
created: '2026-05-23'
description: PhonePe is India's largest UPI payments network, owned by Walmart. Its PhonePe Business / Developer platform exposes the PhonePe Payment Gateway (PG) APIs for collecting payments, refunds, and status checks across UPI, cards, netbanking, and wallets, alongside in-store solutions (Static QR, Dynamic QR, Collect Call, Integrated EDC). Backend integrations are wrapped in official Java, Python, Node.js, and PHP server SDKs, with mobile SDKs for Android, iOS, Flutter, React Native, and Ionic. PhonePe also operates the Indus AppStore, a developer platform for native app distribution in India.
finops:
- name: Phonepe Finops
  service_category: API
  slug: phonepe-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/phonepe.png
layout: provider
modified: '2026-05-23'
name: PhonePe
nav: Providers
network: true
overview: 'PhonePe publishes 3 APIs on the [APIs.io](https://apis.io/) network: Checkout API, Order Status API, and Refunds API. Tagged areas include Payments, Payment Gateway, UPI, QR, and EDC.


  PhonePe''s developer surface includes authentication, documentation, GitHub presence, and 6 more developer resources.'
plans:
- name: Phonepe Plans Pricing
  plan_count: 1
  slug: phonepe-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 2
  name: Phonepe Rate Limits
  slug: phonepe-rate-limits
score:
  band: thin
  composite: 34.8
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 64.1
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 34.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 28.1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/phonepe/refs/heads/main/screenshots/phonepe-2026-06-20T191650.png
security:
- kind: authentication
  name: Phonepe Authentication
  slug: phonepe-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Phonepe Domain Security
  slug: phonepe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Phonepe Vulnerability Disclosure
  slug: phonepe-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: phonepe
tags:
- Payments
- Payment Gateway
- UPI
- QR
- EDC
- App Store
- Fintech
- India
website: https://www.phonepe.com/business-solutions/
---

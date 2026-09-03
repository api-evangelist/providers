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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.0
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Paytm Agentic Access
  operation_count: 3
  slug: paytm-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 1
apis:
- description: Core server-to-server payment initiation and status APIs. Generates transaction tokens, processes payments across UPI, cards, netbanking, and wallet, and exposes transaction-status retrieval. Requests
  name: Paytm Payments API
  slug: payments
- description: Initiates full and partial refunds against settled or unsettled Paytm transactions and exposes refund status retrieval. Supports instant refund flows for eligible payment methods.
  name: Paytm Refunds API
  slug: refunds
- description: Returns settlement reports and merchant payout cycles for transactions collected through Paytm, including settlement IDs, UTRs, and per-order breakdowns for reconciliation.
  name: Paytm Settlement API
  slug: settlement
- description: Creates and manages recurring payment subscriptions and mandates across cards, UPI AutoPay, and netbanking e-mandates. Supports plan creation, subscription activation, renewal charging, and cancellati
  name: Paytm Subscriptions API
  slug: subscriptions
- description: Auto-debit mandate APIs for recurring collections, enabling merchants to register, authenticate, and debit customer accounts on a schedule under RBI's e-mandate framework.
  name: Paytm Auto-Debit API
  slug: auto-debit
- description: Authorize and later capture or release card holds. Used for travel, hospitality, and rental flows that need to block funds before final settlement.
  name: Paytm Pre-Auth API
  slug: pre-auth
- description: Generate shareable payment links for collection over email, SMS, WhatsApp, or social channels. Supports expiry, partial payments, and callback notifications on completion.
  name: Paytm Payment Links API
  slug: payment-links
- description: Card tokenization service compliant with RBI guidelines. Exchanges raw card PANs for network or issuer tokens that merchants can store and use for repeat charging and CVV-less flows.
  name: Paytm Token Gateway API
  slug: token-gateway
- description: Returns available bank offers, instant discounts, no-cost EMI plans, and EMI subvention metadata for the customer's card or netbanking option at checkout.
  name: Paytm Bank Offers / EMI API
  slug: bank-offers
- description: Lists, retrieves, and responds to chargebacks and disputes raised against merchant transactions, including evidence upload and status tracking.
  name: Paytm Disputes / Chargeback API
  slug: disputes
- description: Generates per-order dynamic UPI / Bharat QR codes for in-store and contactless collection, with order-linked status callbacks.
  name: Paytm Dynamic QR API
  slug: dynamic-qr
- description: Server-to-server notification posted to a merchant-configured URL when a transaction reaches a terminal state. Includes signed payload with transaction, refund, or subscription event details.
  name: Paytm Status Notification Webhook
  slug: webhook
- description: Native Android SDK that hosts the Paytm payment experience inside the merchant app, supporting UPI, cards, netbanking, wallet, and Paytm Postpaid in a single flow.
  name: Paytm All-in-One SDK (Android)
  slug: all-in-one-sdk-android
- description: Native iOS SDK that hosts the Paytm payment experience inside the merchant app across all supported payment methods.
  name: Paytm All-in-One SDK (iOS)
  slug: all-in-one-sdk-ios
- description: Browser JavaScript checkout that renders the Paytm payment page in two steps - server-side token creation followed by client-side invocation of the hosted checkout overlay.
  name: Paytm JS Checkout
  slug: js-checkout
- baseURL: https://securegw.paytm.in
  baseurl_source: declared
  description: The Payments API from Paytm — 2 operation(s) for payments.
  name: Paytm Payments API
  slug: paytm-payments-api
- baseURL: https://securegw.paytm.in
  baseurl_source: declared
  description: The Refunds API from Paytm — 1 operation(s) for refunds.
  name: Paytm Refunds API
  slug: paytm-refunds-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Paytm Payment Gateway Payments API
  slug: open-paytm-payments-api
- collection_type: open
  name: Paytm Payment Gateway Payments Refunds API
  slug: open-paytm-refunds-api
- collection_type: open
  name: Paytm Payment Gateway API
  slug: open-paytm
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/paytm-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paytm-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paytm-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://business.paytm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://business.paytm.com/docs/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/paytm
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Paytm-Payments
- group: agent
  title: ''
  type: LlmsText
  url: https://paytm.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://business.paytm.com/blog
created: '2026-05-23'
description: Paytm (One97 Communications) is India's leading digital payments and financial services company. Through Paytm for Business it operates a wide catalogue of payment APIs covering online payment gateway, UPI, payment links, subscriptions, auto-debit, pre-auth, refunds, settlement, payouts, token gateway, bank offers, EMI, disputes, and in-store retail solutions (Dynamic QR, EDC, Point-of-Sale). Backend integrations are exposed via REST APIs at the secure gateway (securegw.paytm.in), with first-party Android, iOS, Flutter, React Native, and Web JS / Custom Checkout / JS Elements SDKs, and server SDKs for S2S checksum-signed flows.
finops:
- name: Paytm Finops
  service_category: API
  slug: paytm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/paytm.png
layout: provider
modified: '2026-05-23'
name: Paytm
nav: Providers
network: true
overview: 'Paytm publishes 2 APIs on the [APIs.io](https://apis.io/) network: Payments API and Refunds API. Tagged areas include Payments, Payment Gateway, UPI, Payouts, and Subscription.


  Paytm''s developer surface includes authentication, documentation, GitHub presence, engineering blog, and 5 more developer resources.'
plans:
- name: Paytm Plans Pricing
  plan_count: 1
  slug: paytm-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Paytm Rate Limits
  slug: paytm-rate-limits
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 11
    catalog_gap: 62.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 23.8
    discoverability: 70.4
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 32.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paytm/refs/heads/main/screenshots/paytm-2026-06-20T191508.png
security:
- kind: authentication
  name: Paytm Authentication
  slug: paytm-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Paytm Domain Security
  slug: paytm-domain-security
  summary_line: TLSv1.3 · DMARC
slug: paytm
tags:
- Payments
- Payment Gateway
- UPI
- Payouts
- Subscription
- Refunds
- Settlement
- QR
- EDC
- Fintech
- India
website: https://business.paytm.com/
---

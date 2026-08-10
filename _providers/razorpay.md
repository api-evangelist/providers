---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Razorpay Agentic Access
  operation_count: 15
  slug: razorpay-agentic-access
  summary_line: 15 operations · 6 acting
api_count: 6
apis:
- description: RESTful API covering orders, payments, refunds, customers, tokens, invoices, payment links, virtual accounts, settlements, transfers, subscriptions, and webhooks. Authentication is HTTP Basic using th
  name: Razorpay Core REST API
  slug: core-api
- description: Subset of the core REST API focused on creating orders, capturing authorized payments, fetching payment details, issuing refunds, and retrieving transfers for split settlements between linked accounts
  name: Razorpay Payments API
  slug: payments-api
- description: Event-driven webhook surface that POSTs JSON payloads to a merchant-configured HTTPS endpoint when subscribed events occur across payments, orders, refunds, subscriptions, invoices, settlements, Smart
  name: Razorpay Webhooks
  slug: webhooks
- description: The Orders API from Razorpay — 3 operation(s) for orders.
  name: Razorpay Orders API
  slug: razorpay-orders-api
- description: The Payments API from Razorpay — 6 operation(s) for payments.
  name: Razorpay Payments API
  slug: razorpay-payments-api
- description: The Refunds API from Razorpay — 2 operation(s) for refunds.
  name: Razorpay Refunds API
  slug: razorpay-refunds-api
artifact_total: 15
asyncapis:
- description: AsyncAPI description of Razorpay's webhook surface. Razorpay POSTs JSON event payloads to a merchant-configured webhook URL whenever a subscribed event occurs (payments, orders, refunds, subscriptions
  name: Razorpay Webhooks
  slug: razorpay-webhooks-asyncapi
collections:
- collection_type: open
  name: Razorpay Core REST API
  slug: open-razorpay
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/razorpay-a2a.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/razorpay-agentic-access.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/razorpay-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/razorpay-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/razorpay-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/razorpay-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/razorpay-data-model.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/razorpay-decline-codes.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/razorpay-trust-center.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/razorpay-scopes.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/razorpay-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/razorpay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/razorpay-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/razorpay
- group: company
  title: ''
  type: Website
  url: https://razorpay.com
- group: docs
  title: ''
  type: Documentation
  url: https://razorpay.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://razorpay.com/docs/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://razorpay.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://dashboard.razorpay.com/signup
- group: other
  title: ''
  type: Dashboard
  url: https://dashboard.razorpay.com
- group: operate
  title: ''
  type: Support
  url: https://razorpay.com/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.razorpay.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/razorpay
- group: company
  title: ''
  type: Blog
  url: https://razorpay.com/blog/
created: '2026-05-11'
description: Razorpay is India's leading full-stack payments and business banking platform, enabling merchants to accept, process, and disburse payments across cards, UPI, netbanking, wallets, EMI, and BNPL through a single integration. Its developer platform exposes a fully RESTful API at https://api.razorpay.com/v1 (with select v2 resources) returning JSON, secured by HTTP Basic authentication using a key_id and key_secret pair. Beyond core payment processing, Razorpay offers payment links, hosted pages, subscriptions, smart routing, refunds, settlements, payouts via RazorpayX, and KYC-driven onboarding.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-05-30'
name: Razorpay
nav: Providers
network: true
overview: 'Razorpay publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Core REST API, Webhooks, Orders API, and 2 more. Tagged areas include Payments, Payment Gateway, Fintech, India, and UPI.


  The Razorpay catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Razorpay''s developer surface includes sandbox, changelog, authentication, documentation, API reference, pricing, signup flow, and 17 more developer resources.'
random_paper: 76
rules:
- name: Razorpay API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: razorpay-asyncapi-spectral-rules
scopes:
- name: Razorpay Scopes
  scope_count: 5
  slug: razorpay-scopes
  summary_line: 5 scopes
score:
  band: developing
  composite: 45.4
  delta: 0.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 66.2
    developer_ergonomics: 39.1
    discoverability: 64.8
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 45.4
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
    score: 51.6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/razorpay/refs/heads/main/screenshots/razorpay-2026-06-20T192629.png
security:
- kind: authentication
  name: Razorpay Authentication
  slug: razorpay-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Razorpay Domain Security
  slug: razorpay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Razorpay Vulnerability Disclosure
  slug: razorpay-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Razorpay Trust Center
  slug: razorpay-trust-center
  summary_line: PCI DSS, ISO 27001, SOC 2
slug: razorpay
tags:
- Payments
- Payment Gateway
- Fintech
- India
- UPI
- Subscriptions
- Payouts
- Checkout
website: https://razorpay.com
---

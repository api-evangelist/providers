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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Fastspring Agentic Access
  operation_count: 51
  slug: fastspring-agentic-access
  summary_line: 51 operations · 28 acting
api_count: 12
apis:
- description: The Accounts API from FastSpring — 3 operation(s) for accounts.
  name: FastSpring Accounts API
  slug: fastspring-accounts-api
- description: The Coupons API from FastSpring — 3 operation(s) for coupons.
  name: FastSpring Coupons API
  slug: fastspring-coupons-api
- description: The Data API from FastSpring — 4 operation(s) for data.
  name: FastSpring Data API
  slug: fastspring-data-api
- description: The Events API from FastSpring — 2 operation(s) for events.
  name: FastSpring Events API
  slug: fastspring-events-api
- description: The Invoices API from FastSpring — 2 operation(s) for invoices.
  name: FastSpring Invoices API
  slug: fastspring-invoices-api
- description: The Orders API from FastSpring — 2 operation(s) for orders.
  name: FastSpring Orders API
  slug: fastspring-orders-api
- description: The Products API from FastSpring — 3 operation(s) for products.
  name: FastSpring Products API
  slug: fastspring-products-api
- description: The Quotes API from FastSpring — 3 operation(s) for quotes.
  name: FastSpring Quotes API
  slug: fastspring-quotes-api
- description: The Returns API from FastSpring — 2 operation(s) for returns.
  name: FastSpring Returns API
  slug: fastspring-returns-api
- description: The Sessions API from FastSpring — 5 operation(s) for sessions.
  name: FastSpring Sessions API
  slug: fastspring-sessions-api
- description: The Subscriptions API from FastSpring — 7 operation(s) for subscriptions.
  name: FastSpring Subscriptions API
  slug: fastspring-subscriptions-api
- description: The Webhooks API from FastSpring — 1 operation(s) for webhooks.
  name: FastSpring Webhooks API
  slug: fastspring-webhooks-api
artifact_total: 19
asyncapis:
- description: AsyncAPI 2.6 description of FastSpring's outbound webhook surface. FastSpring delivers events to a seller-configured HTTPS endpoint as HTTP POSTs with a JSON envelope of one or more events. Each reque
  name: FastSpring Webhooks
  slug: fastspring-asyncapi
collections:
- collection_type: open
  name: FastSpring API
  slug: open-fastspring
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fastspring-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fastspring-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fastspring-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fastspring-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FastSpring
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fastspring
- group: company
  title: ''
  type: Website
  url: https://fastspring.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.fastspring.com
- group: commercial
  title: ''
  type: Pricing
  url: https://fastspring.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://fastspring.com/contact-sales
- group: other
  title: ''
  type: App Dashboard
  url: https://app.fastspring.com
- group: operate
  title: ''
  type: Support
  url: https://fastspring.com/support
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.fastspring.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://fastspring.com/blog/feed/
created: '2026-05-11'
description: FastSpring is a full-service ecommerce and merchant-of-record platform for SaaS, software, and digital product companies, handling global payments, tax compliance, subscription billing, checkout, and revenue management. The FastSpring API is a REST interface for managing orders, subscriptions, products, coupons, customers, and webhook events, secured via HTTP Basic Authentication using credentials issued from the FastSpring App Dashboard and with HMAC SHA-256 signing available for webhook payload verification.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fastspring.png
layout: provider
modified: '2026-05-30'
name: FastSpring
nav: Providers
network: true
overview: 'FastSpring publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Coupons API, Data API, and 9 more. Tagged areas include Ecommerce, Merchant of Record, Subscription Billing, Payments, and SaaS Billing.


  The FastSpring catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  FastSpring''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 8 more developer resources.'
random_paper: 36
rules:
- name: FastSpring API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: fastspring-asyncapi-spectral-rules
score:
  band: thin
  composite: 36.1
  delta: -4.7
  facets:
    commercial_clarity: 18.4
    contract_quality: 60.2
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 47.9
    operational_transparency: 5.3
  previous_composite: 40.8
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
    score: 26.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fastspring/refs/heads/main/screenshots/fastspring-2026-06-20T181053.png
security:
- kind: authentication
  name: Fastspring Authentication
  slug: fastspring-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fastspring Domain Security
  slug: fastspring-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Fastspring Trust Center
  slug: fastspring-trust-center
  summary_line: SOC 2, PCI DSS, GDPR
slug: fastspring
tags:
- Ecommerce
- Merchant of Record
- Subscription Billing
- Payments
- SaaS Billing
- Checkout
- Tax Compliance
website: https://fastspring.com
---

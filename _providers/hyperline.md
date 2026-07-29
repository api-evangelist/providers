---
access_model:
  confidence: high
  label: Paid (free trial) · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  trial: true
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
- acting_count: 27
  human_in_the_loop: 0
  name: Hyperline Agentic Access
  operation_count: 42
  slug: hyperline-agentic-access
  summary_line: 42 operations · 27 acting
api_count: 7
apis:
- description: The Billable Events API from Hyperline — 2 operation(s) for billable events.
  name: Hyperline Billable Events API
  slug: hyperline-billable-events-api
- description: The Customers API from Hyperline — 5 operation(s) for customers.
  name: Hyperline Customers API
  slug: hyperline-customers-api
- description: The Invoices API from Hyperline — 6 operation(s) for invoices.
  name: Hyperline Invoices API
  slug: hyperline-invoices-api
- description: The Payments API from Hyperline — 2 operation(s) for payments.
  name: Hyperline Payments API
  slug: hyperline-payments-api
- description: The Products API from Hyperline — 3 operation(s) for products.
  name: Hyperline Products API
  slug: hyperline-products-api
- description: The Subscriptions API from Hyperline — 6 operation(s) for subscriptions.
  name: Hyperline Subscriptions API
  slug: hyperline-subscriptions-api
- description: The Webhooks API from Hyperline — 3 operation(s) for webhooks.
  name: Hyperline Webhooks API
  slug: hyperline-webhooks-api
artifact_total: 15
collections:
- collection_type: open
  name: Hyperline API
  slug: open-hyperline
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hyperline-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/hyperline-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hyperline-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hyperline-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hyperline
- group: company
  title: ''
  type: Website
  url: https://www.hyperline.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hyperline.co
- group: commercial
  title: ''
  type: Plans
  url: plans/hyperline-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hyperline-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hyperline-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://hyperline.co/resources/blog
created: '2026-06-20'
description: Hyperline is a usage-based billing and subscription platform that helps B2B SaaS companies manage their entire quote-to-cash workflow. Its REST API covers customers, a product and plan catalog, subscriptions, real-time usage and event ingestion, invoicing, payments, credit notes, and webhooks for hybrid pricing models combining subscription and metered charges.
finops:
- name: Hyperline Finops
  service_category: Billing and Revenue Management
  slug: hyperline-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hyperline.png
layout: provider
modified: '2026-06-20'
name: Hyperline
nav: Providers
network: true
overview: 'Hyperline publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Billable Events API, Customers API, Invoices API, and 4 more. Tagged areas include Billing, Subscriptions, Usage-Based, Metering, and Payments.


  Hyperline''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Hyperline Plans Pricing
  plan_count: 3
  slug: hyperline-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 2
  name: Hyperline Rate Limits
  slug: hyperline-rate-limits
score:
  band: thin
  composite: 35.4
  delta: -3.3
  facets:
    commercial_clarity: 47.4
    contract_quality: 51.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hyperline/refs/heads/main/screenshots/hyperline-2026-06-20T183050.png
security:
- kind: authentication
  name: Hyperline Authentication
  slug: hyperline-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hyperline Domain Security
  slug: hyperline-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Hyperline Trust Center
  slug: hyperline-trust-center
  summary_line: ISO 27001, GDPR
slug: hyperline
tags:
- Billing
- Subscriptions
- Usage-Based
- Metering
- Payments
- Invoicing
- FinOps
website: https://www.hyperline.co
---

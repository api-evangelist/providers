---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Yoco Agentic Access
  operation_count: 10
  slug: yoco-agentic-access
  summary_line: 10 operations · 4 acting
api_count: 5
apis:
- description: Create and manage hosted checkout sessions.
  name: Yoco Checkout API
  slug: yoco-checkout-api
- description: Read shareable payment links (versioned Yoco API).
  name: Yoco Payment Links API
  slug: yoco-payment-links-api
- description: Read payment records (versioned Yoco API).
  name: Yoco Payments API
  slug: yoco-payments-api
- description: Refund completed checkouts and read refund records.
  name: Yoco Refunds API
  slug: yoco-refunds-api
- description: Register and manage webhook endpoints for event notifications.
  name: Yoco Webhooks API
  slug: yoco-webhooks-api
artifact_total: 12
collections:
- collection_type: open
  name: Yoco Online Payments API
  slug: open-yoco
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/yoco-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yoco-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/yoco-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/yoco
- group: company
  title: ''
  type: Website
  url: https://www.yoco.com/za/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.yoco.com
- group: commercial
  title: ''
  type: Plans
  url: plans/yoco-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/yoco-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/yoco-finops.yml
created: '2026-07-12'
description: Yoco is a South African fintech providing card acceptance and payments infrastructure for small and medium businesses - card machines, point of sale, and online payments. Its developer platform exposes REST APIs for accepting online card payments - the Checkout API (server-side hosted checkout at payments.yoco.com/api) for creating payment sessions and issuing refunds, plus a newer versioned Yoco API (api.yoco.com/v1) for reading payments, refunds, and payment links. Integrations authenticate with a secret key (Bearer) and receive asynchronous notifications via signed webhooks. Yoco operates primarily in South Africa and settles in ZAR.
finops:
- name: Yoco Finops
  service_category: Payments and Financial Infrastructure
  slug: yoco-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yoco.png
layout: provider
modified: '2026-07-12'
name: Yoco
nav: Providers
network: true
overview: 'Yoco publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Checkout API, Payment Links API, Payments API, and 2 more. Tagged areas include Payments, Fintech, Payment Gateway, Card Payments, and South Africa.


  Yoco''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Yoco Plans Pricing
  plan_count: 3
  slug: yoco-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 3
  name: Yoco Rate Limits
  slug: yoco-rate-limits
score:
  band: thin
  composite: 38.4
  delta: 2.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.4
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 35.6
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 26.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Yoco Authentication
  slug: yoco-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Yoco Domain Security
  slug: yoco-domain-security
  summary_line: HSTS · DMARC
slug: yoco
tags:
- Payments
- Fintech
- Payment Gateway
- Card Payments
- South Africa
- Online Payments
- Checkout
- Point of Sale
- SMB
- Financial Infrastructure
website: https://www.yoco.com/za/
---

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
- acting_count: 14
  human_in_the_loop: 0
  name: Moyasar Agentic Access
  operation_count: 27
  slug: moyasar-agentic-access
  summary_line: 27 operations · 14 acting
api_count: 5
apis:
- description: Hosted invoices with a Moyasar-hosted checkout URL.
  name: Moyasar Invoices API
  slug: moyasar-invoices-api
- description: Create and manage card and wallet payments.
  name: Moyasar Payments API
  slug: moyasar-payments-api
- description: Payout accounts and payouts / disbursements.
  name: Moyasar Payouts API
  slug: moyasar-payouts-api
- description: Client-side card tokenization using a publishable key.
  name: Moyasar Tokens API
  slug: moyasar-tokens-api
- description: Server-to-server event notifications over HTTP POST.
  name: Moyasar Webhooks API
  slug: moyasar-webhooks-api
artifact_total: 12
collections:
- collection_type: open
  name: Moyasar API
  slug: open-moyasar
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/moyasar-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moyasar-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/moyasar-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/moyasar
- group: company
  title: ''
  type: Website
  url: https://moyasar.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.moyasar.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/moyasar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/moyasar-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/moyasar-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://moyasar.com/en/blog/
created: '2026-07-12'
description: Moyasar is a Saudi Arabian payment gateway that lets businesses accept online payments across mada, Visa, Mastercard, American Express, Apple Pay, Samsung Pay, and STC Pay. Its REST API (base https://api.moyasar.com/v1) covers payments (create, fetch, list, refund, capture, void), hosted invoices, card tokenization, webhooks, and payouts / disbursements. Authentication is HTTP Basic with a publishable or secret API key as the username and an empty password, in separate test and live modes.
finops:
- name: Moyasar Finops
  service_category: Payments and Financial Services
  slug: moyasar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/moyasar.png
layout: provider
modified: '2026-07-12'
name: Moyasar
nav: Providers
network: true
overview: 'Moyasar publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Invoices API, Payments API, Payouts API, and 2 more. Tagged areas include Payments, Payment Gateway, Saudi Arabia, MENA, and mada.


  Moyasar''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Moyasar Plans Pricing
  plan_count: 2
  slug: moyasar-plans-pricing
random_paper: 86
rate_limits:
- limit_count: 3
  name: Moyasar Rate Limits
  slug: moyasar-rate-limits
score:
  band: thin
  composite: 34.7
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 63.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 34.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Moyasar Authentication
  slug: moyasar-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Moyasar Domain Security
  slug: moyasar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: moyasar
tags:
- Payments
- Payment Gateway
- Saudi Arabia
- MENA
- mada
- Cards
- Apple Pay
- STC Pay
- Invoices
- Fintech
website: https://moyasar.com/
---

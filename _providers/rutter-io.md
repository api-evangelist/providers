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
- acting_count: 6
  human_in_the_loop: 0
  name: Rutter Io Agentic Access
  operation_count: 24
  slug: rutter-io-agentic-access
  summary_line: 24 operations · 6 acting
api_count: 5
apis:
- description: Normalized accounting data - accounts, ledger accounts, journal entries, invoices, bills, payments, expenses, transactions.
  name: Rutter Accounting API
  slug: rutter-io-accounting-api
- description: Normalized commerce data - orders, products, customers, transactions.
  name: Rutter Commerce API
  slug: rutter-io-commerce-api
- description: Manage end-user connections created via Rutter Link.
  name: Rutter Connections API
  slug: rutter-io-connections-api
- description: Normalized payment-processor data - payments, payouts, balances, transactions.
  name: Rutter Payments API
  slug: rutter-io-payments-api
- description: Register and manage webhook endpoints for sync and data events.
  name: Rutter Webhooks API
  slug: rutter-io-webhooks-api
artifact_total: 12
collections:
- collection_type: open
  name: Rutter Unified API
  slug: open-rutter-io
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rutter-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rutter-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rutter-io-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rutter-api
- group: company
  title: ''
  type: Website
  url: https://www.rutter.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rutterapi.com/docs/introduction
- group: commercial
  title: ''
  type: Plans
  url: plans/rutter-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rutter-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/rutter-io-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.rutter.com/blog
created: '2026-07-01'
description: Rutter is a unified API for commerce, accounting, and payments. Developers integrate once and read and write normalized business data across QuickBooks, Xero, NetSuite, Sage Intacct, Shopify, Amazon, Stripe, and dozens of other platforms. Rutter authenticates with Basic auth (client_id:secret) and an X-Rutter-Version header, and scopes each request to an end-user's connection via an access_token.
finops:
- name: Rutter Io Finops
  service_category: Integration and API Management
  slug: rutter-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rutter-io.png
layout: provider
modified: '2026-07-01'
name: Rutter
nav: Providers
network: true
overview: 'Rutter publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounting API, Commerce API, Connections API, and 2 more. Tagged areas include Unified API, Accounting, Commerce, Payments, and Business Data.


  Rutter''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Rutter Io Plans Pricing
  plan_count: 3
  slug: rutter-io-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 4
  name: Rutter Io Rate Limits
  slug: rutter-io-rate-limits
score:
  band: thin
  composite: 34.2
  delta: -3.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 52.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.8
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
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Rutter Io Authentication
  slug: rutter-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rutter Io Domain Security
  slug: rutter-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: rutter-io
tags:
- Unified API
- Accounting
- Commerce
- Payments
- Business Data
- Integrations
website: https://www.rutter.com
---

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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Octobat Agentic Access
  operation_count: 48
  slug: octobat-agentic-access
  summary_line: 48 operations · 32 acting
api_count: 9
apis:
- description: Discount coupons for invoices and subscriptions.
  name: Octobat Coupons API
  slug: octobat-coupons-api
- description: Compliant credit notes issued against invoices.
  name: Octobat Credit Notes API
  slug: octobat-credit-notes-api
- description: Customers and their billing / tax details.
  name: Octobat Customers API
  slug: octobat-customers-api
- description: Compliant invoices, their items, and lifecycle actions.
  name: Octobat Invoices API
  slug: octobat-invoices-api
- description: Settlement payouts and their balance transactions.
  name: Octobat Payouts API
  slug: octobat-payouts-api
- description: Products and their tax categorization.
  name: Octobat Products API
  slug: octobat-products-api
- description: Recurring-billing subscriptions and metered usage.
  name: Octobat Subscriptions API
  slug: octobat-subscriptions-api
- description: Real-time tax determination for customers and carts / checkouts.
  name: Octobat Tax Evidence API
  slug: octobat-tax-evidence-api
- description: Payments registered against invoices for reconciliation and tax reporting.
  name: Octobat Transactions API
  slug: octobat-transactions-api
artifact_total: 16
collections:
- collection_type: open
  name: Octobat API
  slug: open-octobat
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/octobat-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/octobat-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/octobat-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/0ctobat
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/octobat
- group: company
  title: ''
  type: Website
  url: https://www.octobat.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.octobat.com
- group: commercial
  title: ''
  type: Plans
  url: plans/octobat-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/octobat-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/octobat-finops.yml
created: '2026-07-03'
description: Octobat is a billing, invoicing, and tax-compliance platform for online businesses. It automates the creation, delivery, and storage of legally compliant invoices, credit notes, self-billing invoices, and tax receipts for every online transaction, and provides a real-time tax (VAT / GST / sales tax) determination engine for tax-exclusive and tax-inclusive billing models. Octobat integrates with Stripe, GoCardless, and other payment providers, and exposes a Stripe-style REST API at base URL https://apiv2.octobat.com authenticated with HTTP Basic (secret key). Octobat also ships Beanie (a hosted checkout) and Plaza (marketplace / platform tax and invoicing for connected accounts). Operating status - Octobat was acquired by Mirakl in November 2021; the standalone marketing site (octobat.com) now redirects to mirakl.com, while the developer documentation at docs.octobat.com and the apiv2.octobat.com API remain available to existing integrators.
finops:
- name: Octobat Finops
  service_category: Billing and Tax Compliance
  slug: octobat-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/octobat.png
layout: provider
modified: '2026-07-03'
name: Octobat
nav: Providers
network: true
overview: 'Octobat publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Coupons API, Credit Notes API, Customers API, and 6 more. Tagged areas include Billing, Invoicing, Tax Compliance, VAT, and E-Commerce.


  Octobat''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Octobat Plans Pricing
  plan_count: 4
  slug: octobat-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Octobat Rate Limits
  slug: octobat-rate-limits
score:
  band: thin
  composite: 35.1
  delta: -3.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.7
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
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
  name: Octobat Authentication
  slug: octobat-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Octobat Domain Security
  slug: octobat-domain-security
  summary_line: TLSv1.3 · HSTS
slug: octobat
tags:
- Billing
- Invoicing
- Tax Compliance
- VAT
- E-Commerce
- Payments
- Fintech
website: https://www.octobat.com
---

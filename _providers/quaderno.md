---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
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
- acting_count: 28
  human_in_the_loop: 0
  name: Quaderno Agentic Access
  operation_count: 53
  slug: quaderno-agentic-access
  summary_line: 53 operations · 28 acting
api_count: 14
apis:
- description: Ping the API and inspect the authenticated account and rate-limit state.
  name: Quaderno Authentication API
  slug: quaderno-authentication-api
- description: Hosted checkout sessions for collecting tax-compliant payments.
  name: Quaderno Checkout API
  slug: quaderno-checkout-api
- description: Customers and vendors.
  name: Quaderno Contacts API
  slug: quaderno-contacts-api
- description: Credit notes issued against invoices.
  name: Quaderno Credits API
  slug: quaderno-credits-api
- description: Quotes and estimates issued to customers.
  name: Quaderno Estimates API
  slug: quaderno-estimates-api
- description: Location evidence records supporting tax determination for a transaction.
  name: Quaderno Evidences API
  slug: quaderno-evidences-api
- description: Purchases and vendor bills recorded against the account.
  name: Quaderno Expenses API
  slug: quaderno-expenses-api
- description: Sales invoices issued to customers.
  name: Quaderno Invoices API
  slug: quaderno-invoices-api
- description: Reusable products and services used as document line items.
  name: Quaderno Items API
  slug: quaderno-items-api
- description: Payments recorded against invoices, credits, and expenses.
  name: Quaderno Payments API
  slug: quaderno-payments-api
- description: Recurring document templates that auto-generate invoices.
  name: Quaderno Recurring API
  slug: quaderno-recurring-api
- description: Real-time tax rate calculation, jurisdictions, tax codes, and tax ID validation.
  name: Quaderno Taxes API
  slug: quaderno-taxes-api
- description: Unified sales transactions that both record a sale and calculate tax.
  name: Quaderno Transactions API
  slug: quaderno-transactions-api
- description: Subscriptions that deliver real-time event notifications to your app.
  name: Quaderno Webhooks API
  slug: quaderno-webhooks-api
artifact_total: 21
collections:
- collection_type: open
  name: Quaderno API
  slug: open-quaderno
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/quaderno-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quaderno-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/quaderno-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/quaderno
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quaderno
- group: company
  title: ''
  type: Website
  url: https://quaderno.io
- group: docs
  title: ''
  type: Documentation
  url: https://developers.quaderno.io
- group: commercial
  title: ''
  type: Plans
  url: plans/quaderno-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/quaderno-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/quaderno-finops.yml
created: '2026-07-03'
description: Quaderno is a tax compliance, invoicing, and sales-tax / VAT automation platform. Its REST API calculates the correct sales tax, VAT, and GST in real time for any jurisdiction, then issues tax-compliant invoices, credit notes, estimates, and receipts. The account-scoped API (https://ACCOUNT_NAME.quadernoapp.com/api) covers contacts, items, invoices, credits, estimates, expenses, recurring documents, payments, unified sales transactions, hosted Checkout sessions, and webhooks, plus a tax engine for rate calculation, jurisdictions, tax codes, and tax ID validation. Requests use HTTP Basic Auth with a private API key and return JSON; every endpoint path ends in .json.
finops:
- name: Quaderno Finops
  service_category: Tax Compliance and Billing
  slug: quaderno-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quaderno.png
layout: provider
modified: '2026-07-03'
name: Quaderno
nav: Providers
network: true
overview: 'Quaderno publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Checkout API, Contacts API, and 11 more. Tagged areas include Tax Compliance, Sales Tax, VAT, Invoicing, and Billing.


  Quaderno''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Quaderno Plans Pricing
  plan_count: 5
  slug: quaderno-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 3
  name: Quaderno Rate Limits
  slug: quaderno-rate-limits
score:
  band: thin
  composite: 38.1
  delta: -2.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.5
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Quaderno Authentication
  slug: quaderno-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Quaderno Domain Security
  slug: quaderno-domain-security
  summary_line: TLSv1.3 · DMARC
slug: quaderno
tags:
- Tax Compliance
- Sales Tax
- VAT
- Invoicing
- Billing
- FinTech
website: https://quaderno.io
---

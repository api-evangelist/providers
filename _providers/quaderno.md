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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Quaderno Agentic Access
  operation_count: 53
  slug: quaderno-agentic-access
  summary_line: 53 operations · 28 acting
api_count: 1
apis:
- baseURL: https://ACCOUNT_NAME.quadernoapp.com/api
  baseurl_source: declared
  description: Ping the API and inspect the authenticated account and rate-limit state.
  name: Quaderno Authentication API
  slug: quaderno-authentication-api
- baseURL: https://ACCOUNT_NAME.quadernoapp.com/api
  baseurl_source: declared
  description: Hosted checkout sessions for collecting tax-compliant payments.
  name: Quaderno Checkout API
  slug: quaderno-checkout-api
- baseURL: https://ACCOUNT_NAME.quadernoapp.com/api
  baseurl_source: declared
  description: Customers and vendors.
  name: Quaderno Contacts API
  slug: quaderno-contacts-api
- baseURL: https://ACCOUNT_NAME.quadernoapp.com/api
  baseurl_source: declared
  description: Credit notes issued against invoices.
  name: Quaderno Credits API
  slug: quaderno-credits-api
- baseURL: https://ACCOUNT_NAME.quadernoapp.com/api
  baseurl_source: declared
  description: Quotes and estimates issued to customers.
  name: Quaderno Estimates API
  slug: quaderno-estimates-api
- baseURL: https://ACCOUNT_NAME.quadernoapp.com/api
  baseurl_source: declared
  description: Location evidence records supporting tax determination for a transaction.
  name: Quaderno Evidences API
  slug: quaderno-evidences-api
- baseURL: https://ACCOUNT_NAME.quadernoapp.com/api
  baseurl_source: declared
  description: Purchases and vendor bills recorded against the account.
  name: Quaderno Expenses API
  slug: quaderno-expenses-api
- baseURL: https://ACCOUNT_NAME.quadernoapp.com/api
  baseurl_source: declared
  description: Sales invoices issued to customers.
  name: Quaderno Invoices API
  slug: quaderno-invoices-api
- baseURL: https://ACCOUNT_NAME.quadernoapp.com/api
  baseurl_source: declared
  description: Reusable products and services used as document line items.
  name: Quaderno Items API
  slug: quaderno-items-api
- baseURL: https://ACCOUNT_NAME.quadernoapp.com/api
  baseurl_source: declared
  description: Payments recorded against invoices, credits, and expenses.
  name: Quaderno Payments API
  slug: quaderno-payments-api
- baseURL: https://ACCOUNT_NAME.quadernoapp.com/api
  baseurl_source: declared
  description: Recurring document templates that auto-generate invoices.
  name: Quaderno Recurring API
  slug: quaderno-recurring-api
- baseURL: https://ACCOUNT_NAME.quadernoapp.com/api
  baseurl_source: declared
  description: Real-time tax rate calculation, jurisdictions, tax codes, and tax ID validation.
  name: Quaderno Taxes API
  slug: quaderno-taxes-api
- baseURL: https://ACCOUNT_NAME.quadernoapp.com/api
  baseurl_source: declared
  description: Unified sales transactions that both record a sale and calculate tax.
  name: Quaderno Transactions API
  slug: quaderno-transactions-api
- baseURL: https://ACCOUNT_NAME.quadernoapp.com/api
  baseurl_source: declared
  description: Subscriptions that deliver real-time event notifications to your app.
  name: Quaderno Webhooks API
  slug: quaderno-webhooks-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Quaderno Authentication API
  slug: open-quaderno-authentication-api
- collection_type: open
  name: Quaderno Authentication Checkout API
  slug: open-quaderno-checkout-api
- collection_type: open
  name: Quaderno Authentication Contacts API
  slug: open-quaderno-contacts-api
- collection_type: open
  name: Quaderno Authentication Credits API
  slug: open-quaderno-credits-api
- collection_type: open
  name: Quaderno Authentication Estimates API
  slug: open-quaderno-estimates-api
- collection_type: open
  name: Quaderno Authentication Evidences API
  slug: open-quaderno-evidences-api
- collection_type: open
  name: Quaderno Authentication Expenses API
  slug: open-quaderno-expenses-api
- collection_type: open
  name: Quaderno Authentication Invoices API
  slug: open-quaderno-invoices-api
- collection_type: open
  name: Quaderno Authentication Items API
  slug: open-quaderno-items-api
- collection_type: open
  name: Quaderno Authentication Payments API
  slug: open-quaderno-payments-api
- collection_type: open
  name: Quaderno Authentication Recurring API
  slug: open-quaderno-recurring-api
- collection_type: open
  name: Quaderno Authentication Taxes API
  slug: open-quaderno-taxes-api
- collection_type: open
  name: Quaderno Authentication Transactions API
  slug: open-quaderno-transactions-api
- collection_type: open
  name: Quaderno Authentication Webhooks API
  slug: open-quaderno-webhooks-api
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
random_paper: 2
rate_limits:
- limit_count: 3
  name: Quaderno Rate Limits
  slug: quaderno-rate-limits
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 56.7
    developer_ergonomics: 29.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quaderno/refs/heads/main/screenshots/quaderno-2026-09-02T152547.png
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
- Fintech
website: https://quaderno.io
---

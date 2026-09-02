---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Ordway Agentic Access
  operation_count: 65
  slug: ordway-agentic-access
  summary_line: 65 operations · 20 acting
api_count: 1
apis:
- description: Automated billing run management
  name: Ordway Billing Runs API
  slug: ordway-billing-runs-api
- description: Manage billing schedules
  name: Ordway Billing Schedules API
  slug: ordway-billing-schedules-api
- description: Manage general ledger chart of accounts
  name: Ordway Chart of Accounts API
  slug: ordway-chart-of-accounts-api
- description: Manage discount coupons
  name: Ordway Coupons API
  slug: ordway-coupons-api
- description: Manage customer credits
  name: Ordway Credits API
  slug: ordway-credits-api
- description: Manage billing customers and their contacts, notes, and payment methods
  name: Ordway Customers API
  slug: ordway-customers-api
- description: Manage debit memos
  name: Ordway Debit Memos API
  slug: ordway-debit-memos-api
- description: Manage invoices and billing
  name: Ordway Invoices API
  slug: ordway-invoices-api
- description: Manage accounting journal entries
  name: Ordway Journal Entries API
  slug: ordway-journal-entries-api
- description: Manage one-time orders
  name: Ordway Orders API
  slug: ordway-orders-api
- description: Automated payment run management
  name: Ordway Payment Runs API
  slug: ordway-payment-runs-api
- description: Manage payments and payment methods
  name: Ordway Payments API
  slug: ordway-payments-api
- description: Manage billing plans and charges
  name: Ordway Plans API
  slug: ordway-plans-api
- description: Manage products and plans
  name: Ordway Products API
  slug: ordway-products-api
- description: Manage payment refunds
  name: Ordway Refunds API
  slug: ordway-refunds-api
- description: Manage revenue recognition rules
  name: Ordway Revenue Rules API
  slug: ordway-revenue-rules-api
- description: Manage ASC 606 revenue recognition schedules
  name: Ordway Revenue Schedules API
  slug: ordway-revenue-schedules-api
- description: Customer account statements
  name: Ordway Statements API
  slug: ordway-statements-api
- description: Manage subscription lifecycle and charges
  name: Ordway Subscriptions API
  slug: ordway-subscriptions-api
- description: Manage usage-based billing records
  name: Ordway Usages API
  slug: ordway-usages-api
- description: Manage webhook configurations
  name: Ordway Webhooks API
  slug: ordway-webhooks-api
artifact_total: 60
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ordway REST Billing Runs API
  slug: open-ordway-billing-runs-api
- collection_type: open
  name: Ordway REST Billing Runs Billing Schedules API
  slug: open-ordway-billing-schedules-api
- collection_type: open
  name: Ordway REST Billing Runs Chart of Accounts API
  slug: open-ordway-chart-of-accounts-api
- collection_type: open
  name: Ordway REST Billing Runs Coupons API
  slug: open-ordway-coupons-api
- collection_type: open
  name: Ordway REST Billing Runs Credits API
  slug: open-ordway-credits-api
- collection_type: open
  name: Ordway REST Billing Runs Customers API
  slug: open-ordway-customers-api
- collection_type: open
  name: Ordway REST Billing Runs Debit Memos API
  slug: open-ordway-debit-memos-api
- collection_type: open
  name: Ordway REST Billing Runs Invoices API
  slug: open-ordway-invoices-api
- collection_type: open
  name: Ordway REST Billing Runs Journal Entries API
  slug: open-ordway-journal-entries-api
- collection_type: open
  name: Ordway REST Billing Runs Orders API
  slug: open-ordway-orders-api
- collection_type: open
  name: Ordway REST Billing Runs Payment Runs API
  slug: open-ordway-payment-runs-api
- collection_type: open
  name: Ordway REST Billing Runs Payments API
  slug: open-ordway-payments-api
- collection_type: open
  name: Ordway REST Billing Runs Plans API
  slug: open-ordway-plans-api
- collection_type: open
  name: Ordway REST Billing Runs Products API
  slug: open-ordway-products-api
- collection_type: open
  name: Ordway REST Billing Runs Refunds API
  slug: open-ordway-refunds-api
- collection_type: open
  name: Ordway REST Billing Runs Revenue Rules API
  slug: open-ordway-revenue-rules-api
- collection_type: open
  name: Ordway REST Billing Runs Revenue Schedules API
  slug: open-ordway-revenue-schedules-api
- collection_type: open
  name: Ordway REST Billing Runs Statements API
  slug: open-ordway-statements-api
- collection_type: open
  name: Ordway REST Billing Runs Subscriptions API
  slug: open-ordway-subscriptions-api
- collection_type: open
  name: Ordway REST Billing Runs Usages API
  slug: open-ordway-usages-api
- collection_type: open
  name: Ordway REST Billing Runs Webhooks API
  slug: open-ordway-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ordway-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ordway-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ordway-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://ordwaylabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ordwaylabs.stoplight.io/docs/ordway/ZG9jOjQ4OTgxNg-overview
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ordwaylabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ordway
- group: company
  title: ''
  type: Blog
  url: https://ordwaylabs.com/resources/blog/
- group: other
  title: ''
  type: X
  url: https://x.com/ordwaylabs
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ordwaylabs.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/ordway-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ordway-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ordway-finops.yml
created: 2026-06-13
description: Ordway is a billing and revenue automation platform providing REST APIs for managing subscriptions, invoicing, payments, revenue recognition, and financial reporting for SaaS companies. The platform supports usage-based billing, ASC 606 compliant revenue recognition, accounts receivable automation, and SaaS metrics reporting.
examples:
- key_count: 28
  name: Customer Example
  slug: customer-example
- key_count: 45
  name: Invoice Example
  slug: invoice-example
- key_count: 23
  name: Payment Example
  slug: payment-example
- key_count: 42
  name: Subscription Example
  slug: subscription-example
- key_count: 17
  name: Usage Example
  slug: usage-example
finops:
- name: Ordway Finops
  service_category: ''
  slug: ordway-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ordway.png
json_schemas:
- name: Customer
  property_count: 29
  slug: customer
- name: Invoice
  property_count: 37
  slug: invoice
- name: Subscription
  property_count: 38
  slug: subscription
- name: Usage
  property_count: 17
  slug: usage
jsonld:
- class_count: 0
  name: Ordway Context
  property_count: 164
  slug: ordway-context
layout: provider
modified: 2026-06-13
name: Ordway
nav: Providers
network: true
overview: 'Ordway publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Billing Runs API, Billing Schedules API, Chart of Accounts API, and 18 more. Tagged areas include Billing, Revenue Automation, Subscription, Invoicing, and Payments.


  The Ordway catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ordway''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Ordway Plans Pricing
  plan_count: 1
  slug: ordway-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Ordway Rate Limits
  slug: ordway-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Ordway API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: ordway-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.1
  coverage:
    artifact_dirs: 15
    catalog_gap: 55.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 58.8
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 21.1
  previous_composite: 35.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ordway/refs/heads/main/screenshots/ordway-2026-06-20T191205.png
security:
- kind: authentication
  name: Ordway Authentication
  slug: ordway-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Ordway Domain Security
  slug: ordway-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ordway
tags:
- Billing
- Revenue Automation
- Subscription
- Invoicing
- Payments
- Revenue Recognition
- SaaS Metrics
- Usage-Based Billing
- Financial Reporting
- Accounts Receivable
website: https://ordwaylabs.com/
---

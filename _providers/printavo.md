---
access_model:
  confidence: medium
  label: Freemium (free trial) · Requires approval
  onboarding: approval
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
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
  score: 19.4
  scored_at: '2026-07-28'
api_count: 9
apis:
- description: GraphQL surface for quotes - the pre-invoice document in Printavo. Query a single quote or a paginated quotes connection, and create, update, delete, or duplicate quotes via the quoteCreate, quoteUpda
  name: Printavo Quotes API
  slug: printavo-quotes-api
- description: GraphQL surface for invoices - a quote that has been converted into a billable order. Query a single invoice or an invoices connection, and update, delete, or duplicate invoices via the invoiceUpdate,
  name: Printavo Invoices API
  slug: printavo-invoices-api
- description: GraphQL surface for orders, where an order is the union of quotes and invoices. Query a single order or a paginated orders connection with filtering by production dates and statuses and sorting option
  name: Printavo Orders API
  slug: printavo-orders-api
- description: 'GraphQL surface for customers (companies) and their contacts. Query single or plural customers and contacts, and create, update, or delete them via the customerCreate, customerUpdate, customerDelete, '
  name: Printavo Customers and Contacts API
  slug: printavo-customers-api
- description: 'GraphQL surface for the products, garments, and decoration that make up an order. Query line items and line item groups, and create, update, or delete line items, line item groups, imprints, and fees '
  name: Printavo Line Items API
  slug: printavo-line-items-api
- description: 'GraphQL surface for the production statuses that track an order through the shop. Query a single status or a statuses connection, and move an order between stages with the statusUpdate mutation. Each '
  name: Printavo Statuses API
  slug: printavo-statuses-api
- description: GraphQL surface for tasks and approval requests attached to quotes, invoices, and orders. Query single or plural tasks with sorting, and create, update, or delete tasks via taskCreate, taskUpdate, and
  name: Printavo Tasks API
  slug: printavo-tasks-api
- description: GraphQL surface for payments and money movement. Query transactions, transaction details, and payment requests, and record, update, or delete payments via transactionPaymentCreate, transactionPaymentU
  name: Printavo Payments API
  slug: printavo-payments-api
- description: 'GraphQL surface for Printavo Merch online stores. Query merch orders and merch stores (a separately priced add-on) to pull group-store sales into the same order and production workflow as the rest of '
  name: Printavo Merch API
  slug: printavo-merch-api
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/printavo-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/printavo
- group: company
  title: ''
  type: Website
  url: https://www.printavo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.printavo.com/docs/api/v2
- group: commercial
  title: ''
  type: Plans
  url: plans/printavo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/printavo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/printavo-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.printavo.com/blog/
created: '2026-07-11'
description: Printavo is print shop management software for screen printers, embroiderers, and other decorated-apparel businesses, covering quotes, invoices, orders, customers, line items, production statuses, tasks, payments, and merch stores. Printavo exposes a public GraphQL API (API v2) at www.printavo.com/api/v2 that supersedes its legacy REST API. The GraphQL API is authenticated with an account email plus an API token and is gated to Printavo's Premium subscription tier; the API reference and GraphQL schema are publicly documented at www.printavo.com/docs/api/v2.
finops:
- name: Printavo Finops
  service_category: Business Application Software
  slug: printavo-finops
graphqls:
- description: Printavo API v2 is a **native GraphQL API** for print shop management - quotes,
  name: Printavo API v2 (GraphQL)
  slug: printavo-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/printavo.png
layout: provider
modified: '2026-07-11'
name: Printavo
nav: Providers
network: true
overview: 'Printavo publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Print Shop Management, Screen Printing, Embroidery, Quotes, and Invoices.


  Printavo''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Printavo Plans Pricing
  plan_count: 5
  slug: printavo-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 4
  name: Printavo Rate Limits
  slug: printavo-rate-limits
score:
  band: thin
  composite: 32.4
  delta: 8.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 43.2
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 24.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
security:
- kind: domain-security
  name: Printavo Domain Security
  slug: printavo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: printavo
tags:
- Print Shop Management
- Screen Printing
- Embroidery
- Quotes
- Invoices
- Orders
- GraphQL
- Decorated Apparel
website: https://www.printavo.com/
---

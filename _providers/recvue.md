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
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: Recvue Agentic Access
  operation_count: 21
  slug: recvue-agentic-access
  summary_line: 21 operations · 13 acting · 1 human-in-the-loop
api_count: 10
apis:
- description: OAuth2 client-credentials token issuance.
  name: RecVue Authentication API
  slug: recvue-authentication-api
- description: Bill runs and invoice generation.
  name: RecVue Billing API
  slug: recvue-billing-api
- description: Dated billing schedule records.
  name: RecVue Billing Schedules API
  slug: recvue-billing-schedules-api
- description: Customer accounts, sites, and contacts.
  name: RecVue Customers API
  slug: recvue-customers-api
- description: Invoices and adjustments (AR integration).
  name: RecVue Invoices API
  slug: recvue-invoices-api
- description: Order and order-line lifecycle (order-to-cash).
  name: RecVue Orders API
  slug: recvue-orders-api
- description: Price lists, tier pricing, and pricing rules.
  name: RecVue Pricing API
  slug: recvue-pricing-api
- description: Asynchronous concurrent programs (bill runs, revenue, exports).
  name: RecVue Programs API
  slug: recvue-programs-api
- description: ASC 606 / IFRS 15 revenue-contract configuration.
  name: RecVue Revenue Recognition API
  slug: recvue-revenue-recognition-api
- description: Usage/delivery ingestion for consumption billing.
  name: RecVue Usage API
  slug: recvue-usage-api
artifact_total: 16
collections:
- collection_type: open
  name: RecVue API
  slug: open-recvue
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/recvue-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/recvue-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/recvue
- group: company
  title: ''
  type: Website
  url: https://www.recvue.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.recvue.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/recvue-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/recvue-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/recvue-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.recvue.com/resources/
created: '2026-07-11'
description: RecVue is an enterprise revenue management platform (RevOS - the Revenue Operating System) that unifies complex billing, revenue recognition, order-to-cash, usage-based monetization, and partner settlements for the office of the CFO. It automates recurring, usage, milestone, and hybrid billing models and recognizes revenue in compliance with ASC 606 and IFRS 15, with performance-obligation tracking, allocation, deferral, and audit trails. RecVue is API-first and exposes a documented, RESTful developer API (JSON, OAuth2 client-credentials, a Bulk API for large data sets, and official Node, Ruby, JavaScript, and Python client libraries) covering orders, order lines, bill runs, billing schedules, pricing, usage/deliveries, customers, invoices/adjustments, and revenue contracts. The platform is enterprise/sales-gated for provisioning (production and sandbox tenants), but the API reference is public at developer.recvue.com.
finops:
- name: Recvue Finops
  service_category: Financial Applications and Revenue Management
  slug: recvue-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/recvue.png
layout: provider
modified: '2026-07-11'
name: RecVue
nav: Providers
network: true
overview: 'RecVue publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Billing API, Billing Schedules API, and 7 more. Tagged areas include Revenue Recognition, ASC 606, Billing, Order-to-Cash, and Revenue Management.


  RecVue''s developer surface includes authentication, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Recvue Plans Pricing
  plan_count: 1
  slug: recvue-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 4
  name: Recvue Rate Limits
  slug: recvue-rate-limits
score:
  band: thin
  composite: 35.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 55.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 35.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Recvue Authentication
  slug: recvue-authentication
  summary_line: oauth2 · 1 scheme
slug: recvue
tags:
- Revenue Recognition
- ASC 606
- Billing
- Order-to-Cash
- Revenue Management
- Usage-Based Billing
- Partner Settlements
- IFRS 15
- Subscription Billing
- Enterprise
website: https://www.recvue.com/
---

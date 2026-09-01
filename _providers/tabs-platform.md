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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Tabs Platform Agentic Access
  operation_count: 34
  slug: tabs-platform-agentic-access
  summary_line: 34 operations · 14 acting
api_count: 1
apis:
- description: Items (GL-mapped products/services) and revenue categories.
  name: Tabs Catalog API
  slug: tabs-platform-catalog-api
- description: Customer agreements defining dates, terms, obligations, and billing terms.
  name: Tabs Contracts API
  slug: tabs-platform-contracts-api
- description: The businesses you bill, with contacts, addresses, and external IDs.
  name: Tabs Customers API
  slug: tabs-platform-customers-api
- description: Itemized requests for payment derived from obligations, with actions and PDF export.
  name: Tabs Invoices API
  slug: tabs-platform-invoices-api
- description: Commitments linked to GL items that generate invoice line items.
  name: Tabs Obligations API
  slug: tabs-platform-obligations-api
- description: Receipts (often bank-imported) that settle invoices.
  name: Tabs Payments API
  slug: tabs-platform-payments-api
- description: ASC 606 performance obligations, recognized revenue, ARR and cash-forecast reporting.
  name: Tabs Revenue Recognition API
  slug: tabs-platform-revenue-recognition-api
- description: Consumption records that feed usage-based and metered billing.
  name: Tabs Usage Events API
  slug: tabs-platform-usage-events-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tabs Platform Catalog API
  slug: open-tabs-platform-catalog-api
- collection_type: open
  name: Tabs Platform Catalog Contracts API
  slug: open-tabs-platform-contracts-api
- collection_type: open
  name: Tabs Platform Catalog Customers API
  slug: open-tabs-platform-customers-api
- collection_type: open
  name: Tabs Platform Catalog Invoices API
  slug: open-tabs-platform-invoices-api
- collection_type: open
  name: Tabs Platform Catalog Obligations API
  slug: open-tabs-platform-obligations-api
- collection_type: open
  name: Tabs Platform Catalog Payments API
  slug: open-tabs-platform-payments-api
- collection_type: open
  name: Tabs Platform Catalog Revenue Recognition API
  slug: open-tabs-platform-revenue-recognition-api
- collection_type: open
  name: Tabs Platform Catalog Usage Events API
  slug: open-tabs-platform-usage-events-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tabs-platform-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tabs-platform-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/teamtabs
- group: company
  title: ''
  type: Website
  url: https://tabs.inc
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tabsplatform.com
- group: commercial
  title: ''
  type: Plans
  url: plans/tabs-platform-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tabs-platform-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tabs-platform-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.tabs.com/blog
created: '2026-07-11'
description: Tabs (tabs.inc) is an AI-native revenue automation platform for B2B companies that unifies billing, collections, ASC 606 revenue recognition, and reporting on top of a contract-driven data model. Tabs ingests executed contracts, uses AI to extract commercial terms, automatically generates invoices, schedules ASC 606-compliant revenue, drives collections, and produces real-time ARR, cash, and AR reporting. The public Tabs Platform REST API (https://api.tabsplatform.com, documented at docs.tabsplatform.com) exposes the core data model - customers, contracts, items, revenue categories, obligations, invoices, payments, usage events, and performance obligations - so contract, billing, and revenue data can flow into the rest of the finance stack (ERP, CRM, payment, and tax systems). Supports subscription, usage-based, metered, and hybrid billing models. Authenticated with an API key passed in the Authorization header.
finops:
- name: Tabs Platform Finops
  service_category: Financial Operations and Revenue Automation
  slug: tabs-platform-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tabs-platform.png
layout: provider
modified: '2026-07-11'
name: Tabs
nav: Providers
network: true
overview: 'Tabs publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Contracts API, Customers API, and 5 more. Tagged areas include Revenue Recognition, ASC 606, Billing, B2B Payments, and Accounts Receivable.


  Tabs'' developer surface includes authentication, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Tabs Platform Plans Pricing
  plan_count: 3
  slug: tabs-platform-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Tabs Platform Rate Limits
  slug: tabs-platform-rate-limits
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 8
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 51.6
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 33.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Tabs Platform Authentication
  slug: tabs-platform-authentication
  summary_line: apiKey · 1 scheme
slug: tabs-platform
tags:
- Revenue Recognition
- ASC 606
- Billing
- B2B Payments
- Accounts Receivable
- Invoicing
- Collection
- Usage-Based Billing
- Subscription
- Contracts
- Finance
- Revenue Automation
website: https://tabs.inc
---

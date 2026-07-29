---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 9
apis:
- description: 'Programmatically create, list, retrieve, and update bills and vendor invoices flowing through Airbase''s AP automation - including bill line items, approval state, payment status, and payment method - '
  name: Airbase Bills & AP Automation API
  slug: airbase-bills-ap-api
- description: Create and track guided purchase requests and purchase orders, including intake details, line items, vendor and GL coding, budget checks, and the approval milestones a request transitions through. Air
  name: Airbase Purchase Requests & Orders API
  slug: airbase-purchase-orders-api
- description: Manage the vendor/supplier master record - create, list, retrieve, and update vendors, their payment details, tax and onboarding information, and the relationships that bills, purchase orders, and pay
  name: Airbase Vendors API
  slug: airbase-vendors-api
- description: Access Airbase corporate and virtual card programs - list cards, card holders, spend limits and controls, and their associated policies - to reconcile card spend against budgets and the general ledger
  name: Airbase Corporate Cards API
  slug: airbase-cards-api
- description: Pull unified transaction and spend data across cards, bills, and reimbursements - amounts, merchants, dates, GL coding, and reconciliation status - for reporting, analytics, and closing the books. End
  name: Airbase Transactions API
  slug: airbase-transactions-api
- description: Create and track employee expense reimbursements and out-of-pocket claims - receipts, line items, approval state, and payout status - as part of Airbase's expense management workflows. Endpoints model
  name: Airbase Expense Reimbursements API
  slug: airbase-reimbursements-api
- description: Inspect and act on the multi-step approval workflows that gate purchase requests, bills, cards, and reimbursements - approvers, policy rules, current state, and milestone transitions. Approval milesto
  name: Airbase Approvals API
  slug: airbase-approvals-api
- description: Read and push general-ledger coding and accounting records so spend stays in sync with the ERP/GL. Airbase promotes a REST API specifically for building custom ERP/GL connections for systems not on it
  name: Airbase GL & Accounting Sync API
  slug: airbase-gl-accounting-sync-api
- description: 'Register and manage webhook subscriptions so external systems receive Airbase events - for example a purchase request being approved or a workflow transitioning through a milestone - as JSON payloads '
  name: Airbase Webhooks Management API
  slug: airbase-webhooks-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airbase-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airbase
- group: company
  title: ''
  type: Website
  url: https://www.airbase.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.airbase.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/airbase-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/airbase-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/airbase-finops.yml
created: '2026-07-03'
description: Airbase is a modern spend management platform for finance teams that combines accounts-payable (AP) automation and bill pay, guided procurement and purchase orders, corporate cards, and expense reimbursements on a single system with real-time general-ledger sync. Airbase Inc. was acquired by Paylocity in a ~$325M deal announced September 4, 2024 and completed October 1, 2024, and now operates as "Airbase by Paylocity," extending Paylocity's HCM suite into the office of the CFO. Airbase exposes a developer platform at developer.airbase.io (REST API reference, OpenAPI/Swagger, Postman and Insomnia collections, a webhooks management API, an OAuth playground, and a sandbox) used to build custom connections for systems not covered by the pre-built integrations. API access is account-gated - credentials are generated inside the customer's Airbase/Paylocity tenant rather than through open self-serve signup - so the logical APIs below are honestly modeled from the documented product
  surface and developer portal, and the exact endpoint paths and base URL are not publicly reproduced here (endpointsModeled).
finops:
- name: Airbase Finops
  service_category: Financial Management and Spend Management
  slug: airbase-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/airbase.png
layout: provider
modified: '2026-07-03'
name: Airbase
nav: Providers
network: true
overview: 'Airbase publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Spend Management, Accounts Payable, Bill Pay, Procurement, and Corporate Cards.


  Airbase''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Airbase Plans Pricing
  plan_count: 2
  slug: airbase-plans-pricing
random_paper: 79
rate_limits:
- limit_count: 2
  name: Airbase Rate Limits
  slug: airbase-rate-limits
score:
  band: emerging
  composite: 16.7
  delta: -2.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 19.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/airbase/refs/heads/main/screenshots/airbase-2026-07-25T195412.png
security:
- kind: domain-security
  name: Airbase Domain Security
  slug: airbase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: airbase
tags:
- Spend Management
- Accounts Payable
- Bill Pay
- Procurement
- Corporate Cards
- Expense Management
- FinTech
- Paylocity
- Gated API
website: https://www.airbase.com/
---

---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Bill Agentic Access
  operation_count: 40
  slug: bill-agentic-access
  summary_line: 40 operations · 26 acting
api_count: 11
apis:
- description: REST API providing full-breadth access to BILL's Accounts Payable, Accounts Receivable, and Spend & Expense capabilities including bills, invoices, vendors, customers, payments, approvals, and webhook
  name: BILL v3 API
  slug: v3-api
- description: Low-code, embeddable UI components that surface the BILL Accounts Payable workflow inside partner applications with minimal development effort.
  name: BILL Elements
  slug: elements
- description: The Authentication API from BILL — 5 operation(s) for authentication.
  name: BILL Authentication API
  slug: bill-authentication-api
- description: The Bills API from BILL — 4 operation(s) for bills.
  name: BILL Bills API
  slug: bill-bills-api
- description: The Customers API from BILL — 3 operation(s) for customers.
  name: BILL Customers API
  slug: bill-customers-api
- description: The Funding Accounts API from BILL — 2 operation(s) for funding accounts.
  name: BILL Funding Accounts API
  slug: bill-funding-accounts-api
- description: The Invoices API from BILL — 3 operation(s) for invoices.
  name: BILL Invoices API
  slug: bill-invoices-api
- description: The Organizations API from BILL — 2 operation(s) for organizations.
  name: BILL Organizations API
  slug: bill-organizations-api
- description: The Payments API from BILL — 5 operation(s) for payments.
  name: BILL Payments API
  slug: bill-payments-api
- description: The Vendors API from BILL — 3 operation(s) for vendors.
  name: BILL Vendors API
  slug: bill-vendors-api
- description: The Webhooks API from BILL — 2 operation(s) for webhooks.
  name: BILL Webhooks API
  slug: bill-webhooks-api
artifact_total: 17
asyncapis:
- description: Outbound webhook event notifications delivered by the BILL v3 API Platform to subscriber `notificationUrl` endpoints. Subscribers register through the BILL v3 webhook subscription endpoints; BILL POST
  name: BILL Webhooks
  slug: bill-webhooks-asyncapi
collections:
- collection_type: open
  name: BILL v3 API
  slug: open-bill
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bill-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bill-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bill-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.bill.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bill.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bill.com/docs/home
- group: docs
  title: ''
  type: APIReference
  url: https://developer.bill.com/reference
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bill.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.bill.com/Signup
- group: operate
  title: ''
  type: Support
  url: https://developersupport.bill.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bill-com
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.bill.com/llms.txt
created: '2026-05-11'
description: BILL (formerly Bill.com) is a cloud-based financial operations platform for small and midsize businesses that automates accounts payable, accounts receivable, and spend & expense management. The BILL API Platform exposes these workflows through the BILL v3 REST API and embeddable BILL Elements UI components, enabling partners and ERPs to integrate bill capture, approvals, payments, and real-time event notifications via webhooks. The API uses session-based authentication with API keys and developer keys against production and sandbox gateways.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bill.png
layout: provider
modified: '2026-05-30'
name: BILL
nav: Providers
network: true
overview: 'BILL publishes 10 APIs on the [APIs.io](https://apis.io/) network, including v3 API, Authentication API, Bills API, and 7 more. Tagged areas include Accounts Payable, Accounts Receivable, Spend Management, Expense Management, and Payments.


  The BILL catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  BILL''s developer surface includes authentication, documentation, API reference, pricing, signup flow, support, and 6 more developer resources.'
random_paper: 24
rules:
- name: BILL API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: bill-asyncapi-spectral-rules
score:
  band: thin
  composite: 35.2
  delta: -3.9
  facets:
    commercial_clarity: 10.5
    contract_quality: 63.6
    developer_ergonomics: 39.1
    discoverability: 64.8
    governance: 47.9
    operational_transparency: 0.0
  previous_composite: 39.1
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
screenshot: https://raw.githubusercontent.com/api-evangelist/bill/refs/heads/main/screenshots/bill-2026-06-20T173240.png
security:
- kind: authentication
  name: Bill Authentication
  slug: bill-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bill Domain Security
  slug: bill-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bill
tags:
- Accounts Payable
- Accounts Receivable
- Spend Management
- Expense Management
- Payments
- Bill Pay
- Financial Operations
- Fintech
website: https://www.bill.com
---

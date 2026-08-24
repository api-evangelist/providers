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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.4
  scored_at: '2026-08-24'
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
artifact_total: 27
asyncapis:
- description: Outbound webhook event notifications delivered by the BILL v3 API Platform to subscriber `notificationUrl` endpoints. Subscribers register through the BILL v3 webhook subscription endpoints; BILL POST
  name: BILL Webhooks
  slug: bill-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BILL v3 Authentication API
  slug: open-bill-authentication-api
- collection_type: open
  name: BILL v3 Authentication Bills API
  slug: open-bill-bills-api
- collection_type: open
  name: BILL v3 Authentication Customers API
  slug: open-bill-customers-api
- collection_type: open
  name: BILL v3 Authentication Funding Accounts API
  slug: open-bill-funding-accounts-api
- collection_type: open
  name: BILL v3 Authentication Invoices API
  slug: open-bill-invoices-api
- collection_type: open
  name: BILL v3 Authentication Organizations API
  slug: open-bill-organizations-api
- collection_type: open
  name: BILL v3 Authentication Payments API
  slug: open-bill-payments-api
- collection_type: open
  name: BILL v3 Authentication Vendors API
  slug: open-bill-vendors-api
- collection_type: open
  name: BILL v3 Authentication Webhooks API
  slug: open-bill-webhooks-api
- collection_type: open
  name: BILL v3 API
  slug: open-bill
common:
- group: company
  title: ''
  type: Blog
  url: https://www.bill.com/blog
- group: design
  title: ''
  type: Webhooks
  url: https://developer.bill.com/docs/webhooks
- group: start
  title: ''
  type: Sandbox
  url: https://developer.bill.com/docs/sandbox-bank-account-setup
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.bill.com/changelog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bill.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bill.com/legal/terms-of-service
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.bill.com/docs/get-started-in-production
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


  BILL''s developer surface includes engineering blog, sandbox, changelog, getting-started guide, authentication, documentation, API reference, and 12 more developer resources.'
random_paper: 20
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: BILL API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: bill-asyncapi-spectral-rules
score:
  band: developing
  composite: 42.1
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 13.6
    contract_quality: 58.6
    developer_ergonomics: 41.7
    discoverability: 72.2
    governance: 13.6
    operational_transparency: 11.8
  previous_composite: 42.1
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
    score: 31.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
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

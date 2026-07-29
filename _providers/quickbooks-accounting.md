---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API for managing QuickBooks Online accounting entities including Customer, Vendor, Employee, Item, Invoice, Bill, Payment, BillPayment, JournalEntry, Account, TaxCode, and Company information. Al
  name: QuickBooks Online Accounting API
  slug: accounting-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quickbooks-accounting-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/intuit
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/quickbooks
- group: company
  title: ''
  type: Website
  url: https://quickbooks.intuit.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.intuit.com/app/developer/qbo/docs/develop
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.intuit.com
- group: commercial
  title: ''
  type: Pricing
  url: https://quickbooks.intuit.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://developer.intuit.com/app/developer/homepage
- group: start
  title: ''
  type: Sandbox
  url: https://developer.intuit.com/app/developer/sandbox
- group: operate
  title: ''
  type: Support
  url: https://help.developer.intuit.com/
- group: build
  title: ''
  type: SDK Hub
  url: https://developer.intuit.com/app/developer/qbo/docs/develop/sdks-and-samples-collections
created: '2026-05-11'
description: The QuickBooks Online Accounting API is Intuit's REST API for reading and writing the core accounting entities of a QuickBooks Online company file, including customers, vendors, items, invoices, bills, payments, accounts, journal entries, and tax codes. Apps authenticate via OAuth 2.0 against the Intuit Developer platform and target a per-company realm using https://quickbooks.api.intuit.com/v3/company/{realmId} in production or the sandbox host for testing. It is the foundation API for accounting, bookkeeping, invoicing, and financial reporting integrations on QuickBooks Online.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quickbooks-accounting.png
layout: provider
modified: '2026-05-11'
name: QuickBooks Online Accounting API
nav: Providers
network: true
overview: 'QuickBooks Online Accounting API publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Accounting, Bookkeeping, Invoicing, Small Business, and QuickBooks.


  QuickBooks Online Accounting API''s developer surface includes documentation, pricing, signup flow, sandbox, support, and 6 more developer resources.'
random_paper: 35
score:
  band: emerging
  composite: 15.3
  delta: -2.4
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 28.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 17.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quickbooks-accounting/refs/heads/main/screenshots/quickbooks-accounting-2026-06-20T192431.png
security:
- kind: domain-security
  name: Quickbooks Accounting Domain Security
  slug: quickbooks-accounting-domain-security
  summary_line: TLSv1.3 · DMARC
slug: quickbooks-accounting
tags:
- Accounting
- Bookkeeping
- Invoicing
- Small Business
- QuickBooks
- Intuit
- Financial Data
- OAuth 2.0
website: https://quickbooks.intuit.com
---

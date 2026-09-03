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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
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
random_paper: 11
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 3
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 22.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
- Authentication
website: https://quickbooks.intuit.com
---

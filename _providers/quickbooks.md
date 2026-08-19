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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.8
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: 'REST API for the QuickBooks Online accounting platform, exposing accounting objects such as Invoice, Customer, Payment, Bill, Vendor, Account, Item, Estimate, JournalEntry, and TaxRate over JSON with '
  name: QuickBooks Online Accounting API
  slug: online-accounting
- description: REST API for processing credit card, ACH, and eCheck payments through Intuit's payments platform, with support for charges, refunds, tokens, and payment methods.
  name: QuickBooks Payments API
  slug: payments
- description: REST API for managing payroll, employees, paychecks, and payroll tax information within QuickBooks Online Payroll.
  name: QuickBooks Payroll API
  slug: payroll
artifact_total: 7
asyncapis:
- description: AsyncAPI 2.6 description of the QuickBooks Online (QBO) Data Services webhook surface. QuickBooks Online delivers asynchronous notifications of data-change events on the configured Intuit App by issui
  name: QuickBooks Online Webhooks
  slug: quickbooks-online-webhooks-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quickbooks-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/quickbooks
- group: company
  title: ''
  type: Website
  url: https://quickbooks.intuit.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.intuit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.intuit.com/app/developer/qbo/docs/develop
- group: docs
  title: ''
  type: APIReference
  url: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/most-commonly-used/account
- group: start
  title: ''
  type: Signup
  url: https://developer.intuit.com/app/developer/homepage
- group: commercial
  title: ''
  type: Pricing
  url: https://quickbooks.intuit.com/pricing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/intuit
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/intuit/quickbooks-online-mcp-server
created: '2026-05-11'
description: QuickBooks is Intuit's accounting software platform for small businesses, self-employed, and accountants, available as QuickBooks Online (cloud) and QuickBooks Desktop. The QuickBooks Online Accounting REST API provides programmatic access to a company's financial data, allowing developers to read, create, update, and delete accounting objects including invoices, customers, payments, bills, vendors, items, and tax data using OAuth 2.0 and JSON over HTTPS.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quickbooks.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-30'
name: QuickBooks
nav: Providers
network: true
overview: 'QuickBooks publishes 1 API on the [APIs.io](https://apis.io/) network: Online Accounting API. Tagged areas include Accounting, Bookkeeping, Small Business, Financials, and Invoicing.


  The QuickBooks catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  QuickBooks'' developer surface includes documentation, API reference, signup flow, pricing, and 6 more developer resources.'
random_paper: 40
rules:
- effective_rule_count: 30
  extends:
  - spectral:asyncapi
  name: QuickBooks API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 1
  slug: quickbooks-asyncapi-spectral-rules
score:
  band: thin
  composite: 30.8
  delta: -4.5
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 13.6
    contract_quality: 45.6
    developer_ergonomics: 26.2
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 2.6
  previous_composite: 35.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quickbooks/refs/heads/main/screenshots/quickbooks-2026-06-20T192434.png
security:
- kind: domain-security
  name: Quickbooks Domain Security
  slug: quickbooks-domain-security
  summary_line: TLSv1.3 · DMARC
slug: quickbooks
tags:
- Accounting
- Bookkeeping
- Small Business
- Financials
- Invoicing
- Payroll
- Tax
website: https://quickbooks.intuit.com/
---

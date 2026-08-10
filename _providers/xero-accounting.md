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
  band: agent-ready
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
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Xero Accounting Agentic Access
  operation_count: 17
  slug: xero-accounting-agentic-access
  summary_line: 17 operations · 8 acting
api_count: 7
apis:
- description: OAuth 2.0 connections endpoint for listing the Xero tenants authorized under an access token.
  name: Xero Connections API
  slug: connections
- description: The Accounts API from Xero Accounting — 3 operation(s) for accounts.
  name: Xero Accounting Accounts API
  slug: xero-accounting-accounts-api
- description: The BankTransactions API from Xero Accounting — 2 operation(s) for banktransactions.
  name: Xero Accounting BankTransactions API
  slug: xero-accounting-banktransactions-api
- description: The BankTransfers API from Xero Accounting — 1 operation(s) for banktransfers.
  name: Xero Accounting BankTransfers API
  slug: xero-accounting-banktransfers-api
- description: The BatchPayments API from Xero Accounting — 1 operation(s) for batchpayments.
  name: Xero Accounting BatchPayments API
  slug: xero-accounting-batchpayments-api
- description: The Contacts API from Xero Accounting — 1 operation(s) for contacts.
  name: Xero Accounting Contacts API
  slug: xero-accounting-contacts-api
- description: The Invoices API from Xero Accounting — 1 operation(s) for invoices.
  name: Xero Accounting Invoices API
  slug: xero-accounting-invoices-api
artifact_total: 13
collections:
- collection_type: open
  name: Xero Accounting API
  slug: open-xero-accounting
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/xero-accounting-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xero-accounting-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/xero-accounting-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/xero-accounting-scopes.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.xero.com/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/xero
- group: company
  title: ''
  type: Website
  url: https://www.xero.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.xero.com/documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://www.xero.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://developer.xero.com/app/manage
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/XeroAPI
- group: docs
  title: ''
  type: OpenAPI Specifications
  url: https://github.com/XeroAPI/Xero-OpenAPI
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/XeroAPI/xero-mcp-server
created: '2026-05-11'
description: Xero is a cloud accounting platform for small businesses, accountants, and bookkeepers that provides invoicing, bank reconciliation, payroll, expense management, and financial reporting. The Xero Accounting API exposes full-featured REST endpoints for invoices, contacts, bank transactions, accounts, items, journals, reports, and more. All Xero APIs share a single OAuth 2.0 authorization layer, require the Xero-Tenant-Id header to scope requests to an organization, and are served from api.xero.com.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/xero-accounting.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Xero Accounting
nav: Providers
network: true
overview: 'Xero Accounting publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, BankTransactions API, BankTransfers API, and 3 more. Tagged areas include Accounting, Small Business, Invoicing, Bookkeeping, and Financial Reporting.


  Xero Accounting''s developer surface includes authentication, engineering blog, documentation, pricing, signup flow, and 8 more developer resources.'
random_paper: 50
scopes:
- name: Xero Accounting Scopes
  scope_count: 6
  slug: xero-accounting-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: thin
  composite: 30.6
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 57.4
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 30.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/xero-accounting/refs/heads/main/screenshots/xero-accounting-2026-06-20T201700.png
security:
- kind: authentication
  name: Xero Accounting Authentication
  slug: xero-accounting-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Xero Accounting Domain Security
  slug: xero-accounting-domain-security
  summary_line: TLSv1.3 · DMARC
slug: xero-accounting
tags:
- Accounting
- Small Business
- Invoicing
- Bookkeeping
- Financial Reporting
- SaaS
website: https://www.xero.com
---

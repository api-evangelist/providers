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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Quickbooks Online Agentic Access
  operation_count: 8
  slug: quickbooks-online-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 2
apis:
- description: REST API for processing card and bank payments, tokenizing payment methods, creating charges and refunds, and managing eChecks tied to a QuickBooks Online merchant account. Authentication uses OAuth 2
  name: QuickBooks Payments API
  slug: payments-api
- description: The Company API from QuickBooks Online — 8 operation(s) for company.
  name: QuickBooks Online Company API
  slug: quickbooks-online-company-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: QuickBooks Online Accounting Company API
  slug: open-quickbooks-online-company-api
- collection_type: open
  name: QuickBooks Online Accounting API
  slug: open-quickbooks-online
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/quickbooks-online-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quickbooks-online-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/quickbooks-online-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/quickbooks-online-scopes.yml
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
  url: https://quickbooks.intuit.com/online/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.intuit.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.intuit.com/app/developer/qbo/docs/develop
- group: commercial
  title: ''
  type: Pricing
  url: https://quickbooks.intuit.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://quickbooks.intuit.com/online/signup/
- group: start
  title: ''
  type: Developer Sign Up
  url: https://developer.intuit.com/app/developer/myapps
- group: build
  title: ''
  type: SDKs
  url: https://developer.intuit.com/app/developer/qbo/docs/develop/sdks-and-samples-collections
- group: operate
  title: ''
  type: Support
  url: https://help.developer.intuit.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.developer.intuit.com
created: '2026-05-11'
description: QuickBooks Online is Intuit's cloud accounting platform for small and mid-sized businesses, providing invoicing, expense tracking, payroll, reporting, sales tax, and bookkeeping. The QuickBooks Online Accounting API (v3) gives developers REST access to customers, invoices, payments, items, vendors, journal entries, and the full chart of accounts. The API uses OAuth 2.0 with the Intuit OAuth platform and is sandbox-enabled for development and testing.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quickbooks-online.png
layout: provider
modified: '2026-05-11'
name: QuickBooks Online
nav: Providers
network: true
overview: 'QuickBooks Online publishes 1 API on the [APIs.io](https://apis.io/) network: Company API. Tagged areas include Accounting, Bookkeeping, Invoicing, Small Business, and Finance.


  QuickBooks Online''s developer surface includes authentication, documentation, pricing, signup flow, support, and 10 more developer resources.'
random_paper: 9
scopes:
- name: Quickbooks Online Scopes
  scope_count: 5
  slug: quickbooks-online-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: thin
  composite: 35.1
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 42.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 35.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 34.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quickbooks-online/refs/heads/main/screenshots/quickbooks-online-2026-06-20T192431.png
security:
- kind: authentication
  name: Quickbooks Online Authentication
  slug: quickbooks-online-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Quickbooks Online Domain Security
  slug: quickbooks-online-domain-security
  summary_line: TLSv1.3 · DMARC
slug: quickbooks-online
tags:
- Accounting
- Bookkeeping
- Invoicing
- Small Business
- Finance
- Payments
- Payroll
website: https://quickbooks.intuit.com/online/
---

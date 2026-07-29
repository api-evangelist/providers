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
    asyncapi_events: false
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
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Freeagent Agentic Access
  operation_count: 23
  slug: freeagent-agentic-access
  summary_line: 23 operations · 15 acting
api_count: 4
apis:
- description: RESTful API for the FreeAgent cloud accounting platform. Provides full access to invoices, estimates, contacts, bills, expenses, projects, timeslips, bank accounts, transactions, and accountancy-pract
  name: FreeAgent REST API
  slug: rest-api
- description: The BankAccounts API from FreeAgent — 2 operation(s) for bankaccounts.
  name: FreeAgent BankAccounts API
  slug: freeagent-bankaccounts-api
- description: The Contacts API from FreeAgent — 2 operation(s) for contacts.
  name: FreeAgent Contacts API
  slug: freeagent-contacts-api
- description: The Invoices API from FreeAgent — 10 operation(s) for invoices.
  name: FreeAgent Invoices API
  slug: freeagent-invoices-api
artifact_total: 10
collections:
- collection_type: open
  name: FreeAgent API
  slug: open-freeagent
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/freeagent-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/freeagent-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freeagent-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/freeagent-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/freeagent-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/freeagent
- group: company
  title: ''
  type: Website
  url: https://www.freeagent.com
- group: docs
  title: ''
  type: Documentation
  url: https://dev.freeagent.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.freeagent.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.freeagent.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://signup.freeagent.com/
- group: operate
  title: ''
  type: Support
  url: https://support.freeagent.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.freeagent.com
- group: company
  title: ''
  type: Blog
  url: https://www.freeagent.com/feed.rss
created: '2026-05-11'
description: FreeAgent is UK-focused cloud accounting software for small businesses, freelancers, and accountants, providing invoicing, expense tracking, time tracking, project management, banking, payroll, and Self Assessment / VAT filing through HMRC's Making Tax Digital. The FreeAgent API is a RESTful service that exposes contacts, invoices, estimates, expenses, bills, timeslips, projects, bank accounts, bank transactions, transaction explanations, and tax timeline events for company accounts and accountancy practices. Authentication uses OAuth 2.0 (authorization code flow) and responses are available in JSON or XML.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/freeagent.png
layout: provider
modified: '2026-05-11'
name: FreeAgent
nav: Providers
network: true
overview: 'FreeAgent publishes 4 APIs on the [APIs.io](https://apis.io/) network, including REST API, BankAccounts API, Contacts API, and 1 more. Tagged areas include Accounting, Small Business, Invoicing, Bookkeeping, and Expenses.


  FreeAgent''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 8 more developer resources.'
random_paper: 65
scopes:
- name: Freeagent Scopes
  scope_count: 0
  slug: freeagent-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.9
  delta: -2.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 53.4
    developer_ergonomics: 34.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 33.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/freeagent/refs/heads/main/screenshots/freeagent-2026-06-20T181523.png
security:
- kind: authentication
  name: Freeagent Authentication
  slug: freeagent-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Freeagent Domain Security
  slug: freeagent-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Freeagent Vulnerability Disclosure
  slug: freeagent-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: freeagent
tags:
- Accounting
- Small Business
- Invoicing
- Bookkeeping
- Expenses
- Payroll
- VAT
- HMRC
- Making Tax Digital
website: https://www.freeagent.com
---

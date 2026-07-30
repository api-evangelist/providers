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
- acting_count: 13
  human_in_the_loop: 0
  name: Freshbooks Agentic Access
  operation_count: 27
  slug: freshbooks-agentic-access
  summary_line: 27 operations · 13 acting
api_count: 13
apis:
- description: REST API for FreshBooks providing CRUD access to clients, invoices, estimates, expenses, projects, time entries, tasks, payments, items, taxes, and accounting reports. Uses OAuth 2.0 Bearer tokens and
  name: FreshBooks REST API
  slug: freshbooks-api
- description: Event delivery surface for the FreshBooks Callbacks API. Subscribers register an HTTPS endpoint, complete a verifier handshake, and then receive HMAC-SHA256 signed POSTs (application/x-www-form-urlenc
  name: FreshBooks Webhooks (Callbacks API)
  slug: freshbooks-webhooks
- description: The Auth API from FreshBooks — 1 operation(s) for auth.
  name: FreshBooks Auth API
  slug: freshbooks-auth-api
- description: The Clients API from FreshBooks — 2 operation(s) for clients.
  name: FreshBooks Clients API
  slug: freshbooks-clients-api
- description: The Estimates API from FreshBooks — 1 operation(s) for estimates.
  name: FreshBooks Estimates API
  slug: freshbooks-estimates-api
- description: The Expenses API from FreshBooks — 2 operation(s) for expenses.
  name: FreshBooks Expenses API
  slug: freshbooks-expenses-api
- description: The Invoices API from FreshBooks — 2 operation(s) for invoices.
  name: FreshBooks Invoices API
  slug: freshbooks-invoices-api
- description: The Items API from FreshBooks — 1 operation(s) for items.
  name: FreshBooks Items API
  slug: freshbooks-items-api
- description: The Payments API from FreshBooks — 1 operation(s) for payments.
  name: FreshBooks Payments API
  slug: freshbooks-payments-api
- description: The Projects API from FreshBooks — 1 operation(s) for projects.
  name: FreshBooks Projects API
  slug: freshbooks-projects-api
- description: The Tasks API from FreshBooks — 1 operation(s) for tasks.
  name: FreshBooks Tasks API
  slug: freshbooks-tasks-api
- description: The Taxes API from FreshBooks — 1 operation(s) for taxes.
  name: FreshBooks Taxes API
  slug: freshbooks-taxes-api
- description: The TimeEntries API from FreshBooks — 1 operation(s) for timeentries.
  name: FreshBooks TimeEntries API
  slug: freshbooks-timeentries-api
artifact_total: 19
asyncapis:
- description: Best-effort AsyncAPI 2.6 description of the FreshBooks Webhooks (Callbacks API) surface. FreshBooks delivers webhook notifications as HTTP POST requests with an `application/x-www-form-urlencoded` bod
  name: FreshBooks Webhooks (Callbacks API)
  slug: freshbooks-webhooks-asyncapi
collections:
- collection_type: open
  name: FreshBooks REST API
  slug: open-freshbooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/freshbooks-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freshbooks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/freshbooks-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/freshbooks
- group: company
  title: ''
  type: Website
  url: https://www.freshbooks.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.freshbooks.com/api/start
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.freshbooks.com/developers
- group: start
  title: ''
  type: Signup
  url: https://www.freshbooks.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.freshbooks.com/pricing
- group: start
  title: ''
  type: Login
  url: https://my.freshbooks.com/
- group: operate
  title: ''
  type: Support
  url: https://support.freshbooks.com/
- group: company
  title: ''
  type: Blog
  url: https://www.freshbooks.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/freshbooks
created: '2026-05-11'
description: FreshBooks is a cloud-based accounting and small business management platform offering invoicing, expense tracking, time tracking, project management, payments, estimates, and financial reporting for freelancers, self-employed professionals, and small businesses. The FreshBooks REST API provides access to clients, invoices, expenses, estimates, projects, time entries, payments, and reports using OAuth 2.0 Bearer token authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/freshbooks.png
layout: provider
modified: '2026-05-30'
name: FreshBooks
nav: Providers
network: true
overview: 'FreshBooks publishes 13 APIs on the [APIs.io](https://apis.io/) network, including REST API, Webhooks (Callbacks API), Auth API, and 10 more. Tagged areas include Accounting, Invoicing, Expense Tracking, Time Tracking, and Small Business.


  The FreshBooks catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  FreshBooks'' developer surface includes authentication, documentation, signup flow, pricing, support, engineering blog, and 7 more developer resources.'
random_paper: 12
rules:
- name: FreshBooks API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: freshbooks-asyncapi-spectral-rules
score:
  band: thin
  composite: 39.5
  delta: -3.5
  facets:
    commercial_clarity: 23.7
    contract_quality: 58.9
    developer_ergonomics: 34.8
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 5.3
  previous_composite: 43.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/freshbooks/refs/heads/main/screenshots/freshbooks-2026-06-20T181538.png
security:
- kind: authentication
  name: Freshbooks Authentication
  slug: freshbooks-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Freshbooks Domain Security
  slug: freshbooks-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: freshbooks
tags:
- Accounting
- Invoicing
- Expense Tracking
- Time Tracking
- Small Business
- Bookkeeping
website: https://www.freshbooks.com
---

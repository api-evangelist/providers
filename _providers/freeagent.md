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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Freeagent Agentic Access
  operation_count: 23
  slug: freeagent-agentic-access
  summary_line: 23 operations · 15 acting
api_count: 1
apis:
- description: RESTful API for the FreeAgent cloud accounting platform. Provides full access to invoices, estimates, contacts, bills, expenses, projects, timeslips, bank accounts, transactions, and accountancy-pract
  name: FreeAgent REST API
  slug: rest-api
- baseURL: https://api.freeagent.com/v2
  baseurl_source: declared
  description: The BankAccounts API from FreeAgent — 2 operation(s) for bankaccounts.
  name: FreeAgent BankAccounts API
  slug: freeagent-bankaccounts-api
- baseURL: https://api.freeagent.com/v2
  baseurl_source: declared
  description: The Contacts API from FreeAgent — 2 operation(s) for contacts.
  name: FreeAgent Contacts API
  slug: freeagent-contacts-api
- baseURL: https://api.freeagent.com/v2
  baseurl_source: declared
  description: The Invoices API from FreeAgent — 10 operation(s) for invoices.
  name: FreeAgent Invoices API
  slug: freeagent-invoices-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FreeAgent BankAccounts API
  slug: open-freeagent-bankaccounts-api
- collection_type: open
  name: FreeAgent BankAccounts Contacts API
  slug: open-freeagent-contacts-api
- collection_type: open
  name: FreeAgent BankAccounts Invoices API
  slug: open-freeagent-invoices-api
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
random_paper: 0
scopes:
- name: Freeagent Scopes
  scope_count: 0
  slug: freeagent-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 51.0
    developer_ergonomics: 61.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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

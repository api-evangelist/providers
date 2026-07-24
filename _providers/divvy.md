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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 29.8
  scored_at: '2026-07-23'
api_count: 0
artifact_total: 4
asyncapis:
- description: ''
  name: Divvy Spend Expense Webhooks
  slug: divvy-spend-expense-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://getdivvy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bill.com/docs/home
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bill.com/docs/spend-expense-api
- group: docs
  title: ''
  type: APIReference
  url: https://developer.bill.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.bill.com/docs/bill-v3-api-get-started
- group: operate
  title: ''
  type: Support
  url: https://help.bill.com/direct/s/
- group: company
  title: ''
  type: Blog
  url: https://www.bill.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bill.com/product/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.bill.com/signup
- group: start
  title: ''
  type: Login
  url: https://login.us.bill.com/neo/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bill.com/legal/spend-expense-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bill.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://developer.bill.com/docs/bill-v3-api-postman-collection
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.bill.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/divvy-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/divvy-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/divvy-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/divvy-spend-expense-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/divvy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/divvy-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/divvy-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/divvy-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/divvy-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/divvy-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/divvy-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/divvy-domain-security.yml
created: '2026-07-17'
description: Divvy is a corporate card and spend-management platform (free software plus business credit cards) that was acquired by BILL and now operates as BILL Spend & Expense; getdivvy.com redirects to bill.com. Its API for budgets, users, virtual cards, transactions, and reimbursements is delivered through the BILL developer platform (developer.bill.com) as part of the BILL v3 API, authenticated with a Spend & Expense API token, with a documented webhook event surface, dated changelog, sandbox environment, and per-token rate limits. This profile was surfaced as an Insight Partners portfolio company and has been enriched from BILL's public developer surface.
image: https://www.bill.com/product/spend-and-expense
layout: provider
modified: '2026-07-18'
name: Divvy
nav: Providers
network: true
overview: 'Divvy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Spend Management, Corporate Cards, and Expense Management.


  The Divvy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Divvy''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 19 more developer resources.'
random_paper: 1
rate_limits:
- limit_count: 5
  name: Divvy Rate Limits
  slug: divvy-rate-limits
score:
  band: thin
  composite: 42.4
  delta: 0.2
  facets:
    commercial_clarity: 44.7
    contract_quality: 22.6
    developer_ergonomics: 63.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 63.2
  previous_composite: 42.2
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 43.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Divvy Authentication
  slug: divvy-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Divvy Domain Security
  slug: divvy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: divvy
tags:
- Company
- Payments
- Spend Management
- Corporate Cards
- Expense Management
- Fintech
- BILL
website: https://getdivvy.com/
---

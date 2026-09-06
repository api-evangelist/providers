---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  - '{''url'': ''https://getdivvy.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.bill.com/product/spend-and-expense — a different registrable domain (getdivvy.com -> bill.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 4
asyncapis:
- description: ''
  name: Divvy Spend Expense Webhooks
  slug: divvy-spend-expense-webhooks
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/bill/
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


  Divvy''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 20 more developer resources.'
random_paper: 16
rate_limits:
- limit_count: 5
  name: Divvy Rate Limits
  slug: divvy-rate-limits
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 45.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 55.3
  previous_composite: 41.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/divvy/refs/heads/main/screenshots/divvy-2026-07-25T212135.png
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
- Bill
website: https://getdivvy.com/
---

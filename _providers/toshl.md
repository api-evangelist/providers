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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: REST JSON API for the Toshl personal finance platform. Manage accounts, entries (expenses and incomes with repeats per RFC 5545, transactions, images, locations), budgets, categories, tags, currencies
  name: Toshl API
  slug: toshl-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/toshl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://toshl.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.toshl.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.toshl.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.toshl.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.toshl.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://toshl.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://toshl.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://toshl.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://toshl.com/signup
- group: start
  title: ''
  type: Login
  url: https://toshl.com/login
- group: company
  title: ''
  type: Blog
  url: https://toshl.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.toshl.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/toshl
- group: operate
  title: ''
  type: StatusPage
  url: https://status.toshl.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/toshl-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/toshl-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/toshl-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/toshl-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/toshl-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/toshl-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/toshl-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/toshl-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/toshl-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/toshl-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/toshl-rate-limits.yml
created: '2026-07-17'
description: Toshl Finance is a personal finance and budgeting platform (a 500 Global portfolio company, founded in Slovenia) that helps people track expenses, organize bills, and budget across mobile and web apps, with bank account connections or manual entry. Its Toshl API at api.toshl.com exposes the user's complete personal-finance graph - accounts, entries (expenses and incomes), budgets, categories, tags, locations, images, currencies, exports, planning, and bank institutions/connections/imports - as a REST JSON API with OAuth 2.0 (per-resource read/read-write scopes) or long-lived personal tokens.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/toshl.png
layout: provider
modified: '2026-07-21'
name: Toshl
nav: Providers
network: true
overview: 'Toshl publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Personal Finance, Budgeting, Expense Tracking, Fintech, and Banking.


  Toshl''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, support, and 19 more developer resources.'
random_paper: 8
rate_limits:
- limit_count: 0
  name: Toshl Rate Limits
  slug: toshl-rate-limits
scopes:
- name: Toshl Scopes
  scope_count: 16
  slug: toshl-scopes
  summary_line: 16 scopes · authorizationCode/implicit
score:
  band: thin
  composite: 35.5
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 35.5
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 53.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/toshl/refs/heads/main/screenshots/toshl-2026-09-02T163937.png
security:
- kind: authentication
  name: Toshl Authentication
  slug: toshl-authentication
  summary_line: oauth2/http-basic · 2 schemes
- kind: domain-security
  name: Toshl Domain Security
  slug: toshl-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: toshl
tags:
- Personal Finance
- Budgeting
- Expense Tracking
- Fintech
- Banking
- Consumer Apps
- Company
website: https://toshl.com
---

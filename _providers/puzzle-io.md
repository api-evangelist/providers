---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Puzzle Io Agentic Access
  operation_count: 10
  slug: puzzle-io-agentic-access
  summary_line: 10 operations
api_count: 8
apis:
- description: Ledger accounts and chart of accounts.
  name: Puzzle Accounts API
  slug: puzzle-io-accounts-api
- description: Categories, classes, departments, and projects for classification.
  name: Puzzle Categories API
  slug: puzzle-io-categories-api
- description: Companies connected to a Puzzle partner account.
  name: Puzzle Companies API
  slug: puzzle-io-companies-api
- description: Upstream data connections that feed the ledger.
  name: Puzzle Integrations API
  slug: puzzle-io-integrations-api
- description: Double-entry journal entries against the general ledger.
  name: Puzzle Journal Entries API
  slug: puzzle-io-journal-entries-api
- description: Startup finance metrics derived from the ledger.
  name: Puzzle Metrics API
  slug: puzzle-io-metrics-api
- description: Real-time financial statements.
  name: Puzzle Reports API
  slug: puzzle-io-reports-api
- description: Normalized, categorized transaction feed from connected sources.
  name: Puzzle Transactions API
  slug: puzzle-io-transactions-api
artifact_total: 16
collections:
- collection_type: open
  name: Puzzle Accounting API
  slug: open-puzzle-io
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/puzzle-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/puzzle-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/puzzle-io-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/puzzle-io-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/puzzlefin
- group: company
  title: ''
  type: Website
  url: https://puzzle.io
- group: docs
  title: ''
  type: Documentation
  url: https://puzzle-api.readme.io/docs/welcome
- group: start
  title: ''
  type: SignUp
  url: https://puzzle.io/partners
- group: commercial
  title: ''
  type: Pricing
  url: https://puzzle.io/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/puzzle-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/puzzle-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/puzzle-io-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://puzzle.io/blog
created: '2026-07-01'
description: Puzzle is real-time, AI-native accounting software for startups and accounting firms. It builds a continuously reconciled general ledger on top of connected Stripe, bank, card, and payroll data and surfaces financial statements plus startup metrics like burn, runway, and margin. The Puzzle API exposes that same real-time financial data hub and general ledger over a RESTful, OAuth 2.0-secured JSON interface. As of this catalog entry the API is in an active-development, partner-gated rollout, available to platform partners building embedded accounting and to large accounting or advisory firms; individual companies join a waitlist.
finops:
- name: Puzzle Io Finops
  service_category: Accounting and Financial Management
  slug: puzzle-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/puzzle-io.png
layout: provider
modified: '2026-07-01'
name: Puzzle
nav: Providers
network: true
overview: 'Puzzle publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Categories API, Companies API, and 5 more. Tagged areas include Accounting, Fintech, General Ledger, Financial Reporting, and Bookkeeping.


  Puzzle''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Puzzle Io Plans Pricing
  plan_count: 4
  slug: puzzle-io-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 3
  name: Puzzle Io Rate Limits
  slug: puzzle-io-rate-limits
scopes:
- name: Puzzle Io Scopes
  scope_count: 4
  slug: puzzle-io-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: developing
  composite: 43.5
  delta: -2.2
  facets:
    commercial_clarity: 63.2
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 45.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Puzzle Io Authentication
  slug: puzzle-io-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Puzzle Io Domain Security
  slug: puzzle-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: puzzle-io
tags:
- Accounting
- Fintech
- General Ledger
- Financial Reporting
- Bookkeeping
- Startups
- Embedded Accounting
- Metrics
website: https://puzzle.io
---

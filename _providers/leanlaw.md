---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.1
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: LeanLaw operates a remote Model Context Protocol server at https://api.leanlaw.io/mcp that lets an AI assistant work with a firm's clients, matters, time entries, expenses, fixed fees and invoices. It
  name: LeanLaw MCP Server
  slug: leanlaw-mcp
- baseURL: https://api.leanlaw.io
  baseurl_source: declared
  description: The Client API from LeanLaw — 3 operation(s) for client.
  name: LeanLaw Client API
  slug: leanlaw-client-api
- baseURL: https://api.leanlaw.io
  baseurl_source: declared
  description: The Codes API from LeanLaw — 1 operation(s) for codes.
  name: LeanLaw Codes API
  slug: leanlaw-codes-api
- baseURL: https://api.leanlaw.io
  baseurl_source: declared
  description: The CustomField API from LeanLaw — 1 operation(s) for customfield.
  name: LeanLaw Custom Field API
  slug: leanlaw-customfield-api
- baseURL: https://api.leanlaw.io
  baseurl_source: declared
  description: The Expense API from LeanLaw — 2 operation(s) for expense.
  name: LeanLaw Expense API
  slug: leanlaw-expense-api
- baseURL: https://api.leanlaw.io
  baseurl_source: declared
  description: The FixedFee API from LeanLaw — 2 operation(s) for fixedfee.
  name: LeanLaw Fixed Fee API
  slug: leanlaw-fixedfee-api
- baseURL: https://api.leanlaw.io
  baseurl_source: declared
  description: The Invoice API from LeanLaw — 1 operation(s) for invoice.
  name: LeanLaw Invoice API
  slug: leanlaw-invoice-api
- baseURL: https://api.leanlaw.io
  baseurl_source: declared
  description: The Matter API from LeanLaw — 2 operation(s) for matter.
  name: LeanLaw Matter API
  slug: leanlaw-matter-api
- baseURL: https://api.leanlaw.io
  baseurl_source: declared
  description: The PracticeArea API from LeanLaw — 2 operation(s) for practicearea.
  name: LeanLaw Practice Area API
  slug: leanlaw-practicearea-api
- baseURL: https://api.leanlaw.io
  baseurl_source: declared
  description: The TimeEntry API from LeanLaw — 2 operation(s) for timeentry.
  name: LeanLaw Time Entry API
  slug: leanlaw-timeentry-api
- baseURL: https://api.leanlaw.io
  baseurl_source: declared
  description: The User API from LeanLaw — 2 operation(s) for user.
  name: LeanLaw User API
  slug: leanlaw-user-api
artifact_total: 16
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/leanlaw-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/leanlaw-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.leanlaw.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.leanlaw.io/start
- group: docs
  title: ''
  type: Documentation
  url: https://platform.leanlaw.io/start
- group: docs
  title: ''
  type: APIReference
  url: https://platform.leanlaw.io/api
- group: start
  title: ''
  type: GettingStarted
  url: https://platform.leanlaw.io/start
- group: operate
  title: ''
  type: Support
  url: https://support.leanlaw.co/
- group: company
  title: ''
  type: Blog
  url: https://www.leanlaw.co/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/leanlaw
- group: commercial
  title: ''
  type: Pricing
  url: https://www.leanlaw.co/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.leanlaw.co/leanlaw-trial/
- group: start
  title: ''
  type: Login
  url: https://next.myleanlaw.co/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.leanlaw.co/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.leanlaw.co/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://leanlaw.statuspage.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://platform.leanlaw.io/changelog
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/leanlaw-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/leanlaw-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/leanlaw-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/leanlaw-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/leanlaw-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/leanlaw-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/leanlaw-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leanlaw-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/leanlaw-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/leanlaw-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-25'
description: LeanLaw is legal billing and revenue-operations software for small and mid-sized law firms, built natively on QuickBooks Online. It runs the full law-firm revenue lifecycle — time and expense tracking, matter management, trust/IOLTA accounting, flat-fee and contingency billing, invoicing, e-payments, LEDES output and compensation reporting — and keeps a real-time two-way sync with QuickBooks Online so invoices, payments, trust deposits and expenses post automatically. LeanLaw publishes a public REST API (v2) at api.leanlaw.io covering clients, matters, time entries, expenses, fixed fees, invoices, practice areas, custom fields, users and LEDES billing codes, with an OpenAPI 3.0.4 specification, a Zudoku-powered developer portal at platform.leanlaw.io, and a remote MCP server for AI assistants that is currently in private beta.
image: https://www.leanlaw.co/images/og-default.png
layout: provider
modified: '2026-08-25'
name: LeanLaw
nav: Providers
network: true
overview: 'LeanLaw publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Client API, Codes API, Custom Field API, and 7 more. Tagged areas include Legal, Legal Billing, Law Firms, Time Tracking, and Billing.


  LeanLaw''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
plans:
- name: Leanlaw Plans Pricing
  plan_count: 4
  slug: leanlaw-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Leanlaw Rate Limits
  slug: leanlaw-rate-limits
scopes:
- name: Leanlaw Scopes
  scope_count: 0
  slug: leanlaw-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 57.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 52.3
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 57.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leanlaw/refs/heads/main/screenshots/leanlaw-2026-09-02T150231.png
security:
- kind: authentication
  name: Leanlaw Authentication
  slug: leanlaw-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Leanlaw Domain Security
  slug: leanlaw-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: leanlaw
tags:
- Legal
- Legal Billing
- Law Firms
- Time Tracking
- Billing
- Invoicing
- Accounting
- Trust Accounting
- Practice Management
- QuickBooks
- Payments
- Legal Tech
- Software-as-a-Service
website: https://www.leanlaw.co/
---

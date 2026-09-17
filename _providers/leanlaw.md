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
  band_gated_from: agent-native
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.3
  scored_at: '2026-09-16'
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
  description: The User API from LeanLaw — 2 operation(s) for user.
  name: LeanLaw User API
  slug: leanlaw-user-api
- baseURL: https://api.leanlaw.io/mcp
  baseurl_source: declared
  description: The Custom Field API from LeanLaw — 1 operation(s) for custom field.
  name: LeanLaw Custom Field API
  slug: leanlaw-custom-field-api
- baseURL: https://api.leanlaw.io/mcp
  baseurl_source: declared
  description: The Time entry API from LeanLaw — 2 operation(s) for time entry.
  name: LeanLaw Time entry API
  slug: leanlaw-time-entry-api
artifact_total: 16
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/leanlaw/refs/heads/main/capabilities/leanlaw-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/leanlaw-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/leanlaw/refs/heads/main/overlays/leanlaw-api-overlay.yaml
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
  href: https://raw.githubusercontent.com/api-evangelist/leanlaw/refs/heads/main/lifecycle/leanlaw-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/leanlaw-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/leanlaw/refs/heads/main/plans/leanlaw-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/leanlaw-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/leanlaw/refs/heads/main/rate-limits/leanlaw-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/leanlaw-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/leanlaw/refs/heads/main/authentication/leanlaw-authentication.yml
  title: ''
  type: Authentication
  url: authentication/leanlaw-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/leanlaw/refs/heads/main/scopes/leanlaw-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/leanlaw-scopes.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/leanlaw/refs/heads/main/well-known/leanlaw-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/leanlaw-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/leanlaw/refs/heads/main/conformance/leanlaw-conformance.yml
  title: ''
  type: Conformance
  url: conformance/leanlaw-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/leanlaw/refs/heads/main/security/leanlaw-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/leanlaw-domain-security.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/leanlaw/refs/heads/main/packages/leanlaw-packages.yml
  title: ''
  type: Packages
  url: packages/leanlaw-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/leanlaw/refs/heads/main/llms/leanlaw-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/leanlaw-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/leanlaw/refs/heads/main/skills/_index.yml
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
overview: 'LeanLaw publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Client API, Codes API, Expense API, and 7 more. Tagged areas include Legal, Legal Billing, Law Firms, Time Tracking, and Billing.


  LeanLaw''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
plans:
- name: Leanlaw Plans Pricing
  plan_count: 4
  slug: leanlaw-plans-pricing
random_paper: 14
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
  composite: 57.0
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
    contract_governance: 18.2
    contract_quality: 52.3
    developer_ergonomics: 58.9
    discoverability: 75.9
    operational_transparency: 34.2
  previous_composite: 57.0
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
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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

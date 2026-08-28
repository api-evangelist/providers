---
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
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: 'The LeanLaw REST API (v2) provides programmatic access to a LeanLaw law-firm account — clients, matters, time entries, expenses, fixed fees, invoices, practice areas, custom field definitions, users, '
  name: LeanLaw API
  slug: leanlaw-api
- description: LeanLaw operates a remote Model Context Protocol server at https://api.leanlaw.io/mcp that lets an AI assistant work with a firm's clients, matters, time entries, expenses, fixed fees and invoices. It
  name: LeanLaw MCP Server
  slug: leanlaw-mcp
artifact_total: 8
common:
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
mcp_servers:
- description: LeanLaw operates a first-party remote MCP server that lets an AI assistant work with a law firm's clients, matters, time entries, expenses, fixed fees and invoices. Per the provider's own documentatio
  name: LeanLaw MCP Server
  slug: leanlaw-mcp-server
modified: '2026-08-25'
name: LeanLaw
nav: Providers
network: true
overview: 'LeanLaw publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Legal, Legal Billing, Law Firms, Time Tracking, and Billing.


  LeanLaw''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 19 more developer resources.'
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
  composite: 58.5
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 30.3
    contract_quality: 48.3
    developer_ergonomics: 58.9
    discoverability: 79.6
    governance: 30.3
    operational_transparency: 34.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
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
- LegalTech
- SaaS
website: https://www.leanlaw.co/
---

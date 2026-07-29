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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 5
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bonsai-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bonsai-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bonsai-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bonsai-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bonsai-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hellobonsai.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bonsai-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.hellobonsai.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hellobonsai.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hellobonsai.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.hellobonsai.com/users/sign_up
- group: start
  title: ''
  type: Login
  url: https://app.hellobonsai.com/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hellobonsai.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hellobonsai.com/legal/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.hellobonsai.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.hellobonsai.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.hellobonsai.com/en/
- group: company
  title: ''
  type: Website
  url: https://hellobonsai.com
created: '2026-07-17'
description: Bonsai (hellobonsai.com) is an all-in-one business management platform for service businesses -- freelancers, agencies, and firms -- consolidating client management (CRM, pipeline, proposals, contracts, forms, client portal), project management (tasks, Gantt, time tracking, timesheets, resource planning), and financial management (invoicing, payments, expenses, bookkeeping, rate cards, budgeting and profitability) into one system. Used by 500,000+ small businesses globally. Bonsai exposes its programmatic surface through an official hosted MCP (Model Context Protocol) server at mcp.hellobonsai.com so AI clients (Claude, ChatGPT, Gemini, Cursor, Codex) can act on tasks, projects, deals, contacts, time entries and invoices; a public REST API is documented as forthcoming. Backed by Matrix Partners.
image: https://cdn.prod.website-files.com/635ac9564cc3682ce1536786/673f6d94d320621186b12534_Social%20Meta%20Image%20(1).png
layout: provider
mcp_servers:
- description: ''
  name: bonsai-mcp.yml
  slug: bonsai-mcpyml
modified: '2026-07-18'
name: Bonsai
nav: Providers
network: true
overview: 'Bonsai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, B2B, Business Management, Freelancing, and Agencies.


  Bonsai''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, support, and 12 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 1
  name: Bonsai Rate Limits
  slug: bonsai-rate-limits
score:
  band: emerging
  composite: 27.3
  delta: -1.7
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 29.0
  provenance:
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bonsai/refs/heads/main/screenshots/bonsai-2026-07-25T203600.png
security:
- kind: authentication
  name: Bonsai Authentication
  slug: bonsai-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Bonsai Domain Security
  slug: bonsai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bonsai Trust Center
  slug: bonsai-trust-center
  summary_line: trust center published
slug: bonsai
tags:
- Company
- B2B
- Business Management
- Freelancing
- Agencies
- CRM
- Project Management
- Time Tracking
- Invoicing
- Proposals
- Contracts
- Accounting
- MCP
website: https://hellobonsai.com
---

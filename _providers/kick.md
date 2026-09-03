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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Kick's programmatic surface — a hosted MCP server and CLI executing against the Kick REST API under the same auth, workspace, permission, and audit checks as the web app. No public OpenAPI is publishe
  name: Kick MCP & REST API
  slug: kick-mcp-rest-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.kick.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.kick.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kick.co/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kick.co/ai/developer-tools/mcp/tool-reference.md
- group: start
  title: ''
  type: Quickstart
  url: https://docs.kick.co/ai/mcp/mcp-quickstart.md
- group: company
  title: ''
  type: Blog
  url: https://www.kick.co/resources
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kick.co/pricing
- group: start
  title: ''
  type: SignUp
  url: https://use.kick.co/register
- group: start
  title: ''
  type: Login
  url: https://use.kick.co/login
- group: operate
  title: ''
  type: Support
  url: https://docs.kick.co/troubleshooting/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kick.co/legal#terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kick.co/legal#privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kick.co/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.kick.co/changelog
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kick-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/kick-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/kick-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kick-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kick-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kick-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kick-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kick-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kick-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kick-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kick-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kick-domain-security.yml
created: '2026-07-17'
description: Kick is a self-driving, agentic bookkeeping platform for business owners and accounting firms — "an agentic ledger that does your books with you." It auto-categorizes bank and card transactions in real time (via Plaid), surfaces commonly missed deductions, supports customizable categorization rules, classes, multi-entity journal entries, reconciliation, and tax-ready financials (P&L, balance sheet, cash flow, tax package). Kick exposes a hosted, OAuth-secured Model Context Protocol (MCP) server at use.kick.co/mcp and a first-party CLI (@kickfinance/cli), letting AI agents in Claude, ChatGPT, and Gemini query and safely write to the books with preview-first confirmation. Backed by Felicis and General Catalyst.
image: https://use.kick.co/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: Kick
  slug: kick
modified: '2026-07-19'
name: Kick
nav: Providers
network: true
overview: 'Kick publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Bookkeeping, Accounting, Finance, and Fintech.


  Kick''s developer surface includes documentation, API reference, quickstart, engineering blog, pricing, signup flow, support, and 19 more developer resources.'
random_paper: 19
scopes:
- name: Kick Scopes
  scope_count: 2
  slug: kick-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 34.4
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kick/refs/heads/main/screenshots/kick-2026-07-25T223718.png
security:
- kind: authentication
  name: Kick Authentication
  slug: kick-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Kick Domain Security
  slug: kick-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kick
tags:
- Company
- Bookkeeping
- Accounting
- Finance
- Fintech
- MCP
- AI Agents
- Small Business
website: https://www.kick.co
---

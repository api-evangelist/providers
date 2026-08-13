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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://ambrook.com
- group: commercial
  title: ''
  type: Pricing
  url: https://ambrook.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://ambrook.com/overview/get-started
- group: start
  title: ''
  type: Login
  url: https://ambrook.com/login
- group: company
  title: ''
  type: Blog
  url: https://ambrook.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.ambrook.com/en/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ambrook.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ambrook.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ambrook
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ambrook-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ambrook-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ambrook-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ambrook-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ambrook-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ambrook-domain-security.yml
created: '2026-07-17'
description: Ambrook is financial management software for farms, ranches, and the trades — construction, trucking, manufacturing, and the interconnected businesses that produce, build, and move physical goods. Founded in 2020 and based in New York, it combines bookkeeping, invoicing, payments, and inventory in one platform, with Schedule F/C tax alignment, enterprise tagging for tracking profitability by business line, and cost-per-head livestock tracking. Positioned as a QuickBooks alternative for agriculture and margin-sensitive industries, Ambrook pairs a full-featured mobile app with U.S.-based, ag-centric support. It also operates an OAuth-gated Model Context Protocol (MCP) server that lets AI agents connect to a business's Ambrook data via a read-only GraphQL surface. Ambrook raised a $26.1M Series A and is backed by investors including Homebrew.
image: https://ambrook.com/img/share/default-og.png
layout: provider
mcp_servers:
- description: ''
  name: ambrook-mcp.yml
  slug: ambrook-mcpyml
modified: '2026-07-17'
name: Ambrook
nav: Providers
network: true
overview: 'Ambrook is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Agriculture, Accounting, and Bookkeeping.


  Ambrook''s developer surface includes pricing, signup flow, engineering blog, support, authentication, and 10 more developer resources.'
random_paper: 27
scopes:
- name: Ambrook Scopes
  scope_count: 5
  slug: ambrook-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: emerging
  composite: 24.5
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 24.5
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ambrook/refs/heads/main/screenshots/ambrook-2026-07-25T200036.png
security:
- kind: authentication
  name: Ambrook Authentication
  slug: ambrook-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Ambrook Domain Security
  slug: ambrook-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ambrook
tags:
- Company
- Fintech
- Agriculture
- Accounting
- Bookkeeping
- Payments
- Farm Management
- MCP
website: https://ambrook.com
---

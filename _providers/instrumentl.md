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
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 21.4
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Instrumentl's authenticated remote Model Context Protocol (MCP) server, exposing the grant-management platform to AI agents. Access is gated by OAuth 2.0 (authorization code + PKCE, dynamic client reg
  name: Instrumentl MCP Server
  slug: instrumentl-mcp-server
artifact_total: 6
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/instrumentl-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/instrumentl-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/instrumentl-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/instrumentl-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/instrumentl-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/instrumentl-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/instrumentl-security.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/instrumentl-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.instrumentl.com
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/instrumentl-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://instrumentl.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/instrumentl-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://help.instrumentl.com
- group: company
  title: ''
  type: Blog
  url: https://www.instrumentl.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/instrumentl
- group: commercial
  title: ''
  type: Pricing
  url: https://www.instrumentl.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.instrumentl.com/signup
- group: start
  title: ''
  type: Login
  url: https://www.instrumentl.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.instrumentl.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.instrumentl.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://instrumentl.com
created: '2026-07-17'
description: Instrumentl is the all-in-one grant management platform for nonprofits and grant-writing consultants, helping 5,500+ organizations discover, apply for, and manage grants across the full funding lifecycle. Its Discover capability uses AI-powered matching across 35,000+ active grant opportunities; Apply provides AI-assisted proposal drafting trained on an organization's own winning proposals and funder insights; and Manage handles post-award administration, spend-down tracking, compliance monitoring, and deadline management. Instrumentl maintains a grants database and a 450,000+ funder Foundation Directory built from IRS Form 990 filings, and exposes an authenticated remote MCP server (mcp.instrumentl.com) for agent access.
image: https://static-assets.instrumentl.com/assets/open-graph-image-7aeb77fce8b2e99a998345583d30006a4f24546304a720cb2a2c7c97372f6212.png
layout: provider
mcp_servers:
- description: ''
  name: Instrumentl MCP Server
  slug: instrumentl-mcp-server
modified: '2026-07-19'
name: Instrumentl
nav: Providers
network: true
overview: 'Instrumentl publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Grants, Non-Profit, Fundraising, and Grant Management.


  Instrumentl''s developer surface includes authentication, support, engineering blog, pricing, signup flow, and 16 more developer resources.'
random_paper: 3
scopes:
- name: Instrumentl Scopes
  scope_count: 2
  slug: instrumentl-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: emerging
  composite: 22.5
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 22.5
  provenance:
    mcp: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/instrumentl/refs/heads/main/screenshots/instrumentl-2026-07-25T222622.png
security:
- kind: authentication
  name: Instrumentl Authentication
  slug: instrumentl-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Instrumentl Domain Security
  slug: instrumentl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Instrumentl Vulnerability Disclosure
  slug: instrumentl-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: instrumentl
tags:
- Company
- Grants
- Non-Profit
- Fundraising
- Grant Management
- Foundation Data
- Philanthropy
- MCP
website: https://instrumentl.com
---

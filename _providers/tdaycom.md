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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Hosted Model Context Protocol (MCP) server for tday, exposed at https://tday.com/api/mcp and secured with OAuth 2.1 (authorization_code + PKCE, dynamic client registration, single "tday" scope). It is
  name: tday MCP Server
  slug: tday-mcp-server
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tdaycom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tday.com
- group: start
  title: ''
  type: Login
  url: https://tday.com/login
- group: operate
  title: ''
  type: Support
  url: https://tday.com/book
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tday.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tday.com/terms
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tdaycom-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tdaycom-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tdaycom-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tdaycom-scopes.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tdaycom-llms.txt
created: '2026-07-17'
description: tday (tday.com) is a Y Combinator-backed (Spring 2026) AI platform that turns a software product into on-brand marketing content. It connects to a company's GitHub repository or live website, and on every release automatically produces a launch package — an end-to-end demo video generated from real product flows, feature showcases, and on-brand social graphics and ads — then publishes that creative to social and ad channels and measures how it performs, closing the loop from what a team ships to what it posts. tday operates through the browser like a user, with no SDK embedded in the customer's product, using isolated per-run workspaces, scoped repository access, secure credential storage, and secret redaction. tday exposes a hosted Model Context Protocol (MCP) server at https://tday.com/api/mcp secured with OAuth 2.1 (PKCE, dynamic client registration, RFC 8414 / RFC 9728 discovery), making it the agent-facing surface of the platform.
image: https://tday.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: tdaycom-mcp.yml
  slug: tdaycom-mcpyml
modified: '2026-07-21'
name: Tdaycom
nav: Providers
network: true
overview: 'Tdaycom publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Artificial Intelligence, Content Generation, and Video.


  Tdaycom''s developer surface includes support, authentication, and 9 more developer resources.'
random_paper: 60
scopes:
- name: Tdaycom Scopes
  scope_count: 1
  slug: tdaycom-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 20.3
  delta: -0.6
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 20.9
  provenance:
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Tdaycom Authentication
  slug: tdaycom-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Tdaycom Domain Security
  slug: tdaycom-domain-security
  summary_line: TLSv1.3 · HSTS
slug: tdaycom
tags:
- Company
- Marketing
- Artificial Intelligence
- Content Generation
- Video
- Social Media
- Developer Tools
- MCP
- Agents
- Y Combinator
website: https://tday.com
---

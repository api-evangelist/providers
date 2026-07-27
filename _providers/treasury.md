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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 25.0
  scored_at: '2026-07-27'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://treasury.app/
- group: start
  title: ''
  type: Login
  url: https://treasury.app/login
- group: agent
  title: ''
  type: MCPServer
  url: mcp/treasury-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/treasury-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/treasury-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/treasury-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/treasury-domain-security.yml
created: '2026-07-17'
description: 'Treasury (treasury.app) is a consumer investing and personal-finance education platform that bills itself as "the first investing platform built for learning as a community" and a "non-judgmental investing community." It pairs creator-led learning communities (workshops, coaching, and discussion forums), commission-free brokerage investing accounts with fractional and recurring investments, and self-guided courses on investing, personal finance, and retirement. Backed by Bloomberg Beta and other investors, Treasury has introduced tens of thousands of new investors to the market. It has no traditional public REST/OpenAPI developer platform, but it does expose an agent-native surface: a hosted Model Context Protocol (MCP) server at treasury.app/mcp guarded by an OAuth 2.1 authorization server (authorization code + PKCE, dynamic client registration, scope mcp:connect).'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/treasury.png
layout: provider
mcp_servers:
- description: ''
  name: Treasury MCP Server
  slug: treasury-mcp-server
modified: '2026-07-21'
name: Treasury
nav: Providers
network: true
overview: 'Treasury is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Investing, Personal Finance, Fintech, and Brokerage.


  Treasury''s developer surface includes authentication and 6 more developer resources.'
random_paper: 11
scopes:
- name: Treasury Scopes
  scope_count: 1
  slug: treasury-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 18.5
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.5
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 47.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Treasury Authentication
  slug: treasury-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Treasury Domain Security
  slug: treasury-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: treasury
tags:
- Company
- Investing
- Personal Finance
- Fintech
- Brokerage
- Financial Education
- MCP
- Agent
website: https://treasury.app/
---

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
- description: OAuth-protected Model Context Protocol server exposing Nowlun freight-forwarding capabilities to agents. Requires an access token holding the "mcp" scope.
  name: Nowlun MCP Server
  slug: nowlun-mcp-server
artifact_total: 5
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nowlun-holding-corp-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nowlun-holding-corp-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nowlun-holding-corp-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nowlun-holding-corp-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nowlun-holding-corp-domain-security.yml
- group: start
  title: ''
  type: SignUp
  url: https://nowlun.com/en/users/register/sign_up
- group: start
  title: ''
  type: Login
  url: https://nowlun.com/en/users/login
- group: company
  title: ''
  type: Blog
  url: https://nowlun.com/en/resources
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nowlun.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://wa.me/201014176458
- group: company
  title: ''
  type: Website
  url: https://nowlun.com
created: '2026-07-17'
description: Nowlun is a digital freight-forwarding platform serving the Middle East and North Africa that lets businesses compare instant ocean-freight quotes from 30+ shipping lines, book FCL and bulk sea shipments, arrange inland trucking to and from ports, track cargo through transit, and handle customs clearance. Beyond its shipper-facing web application, Nowlun operates a live, OAuth-protected Model Context Protocol (MCP) server at https://nowlun.com/mcp, secured with RFC 8414 authorization-server and RFC 9728 protected-resource discovery (Authorization Code + PKCE, "mcp" scope). Surfaced as a 500 Global portfolio company and enriched into the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nowlun-holding-corp.png
layout: provider
mcp_servers:
- description: ''
  name: nowlun-holding-corp-mcp.yml
  slug: nowlun-holding-corp-mcpyml
modified: '2026-07-20'
name: Nowlun Holding Corp.
nav: Providers
network: true
overview: 'Nowlun Holding Corp. publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Freight Forwarding, Shipping, and Supply Chain.


  Nowlun Holding Corp.''s developer surface includes authentication, signup flow, engineering blog, support, and 7 more developer resources.'
random_paper: 46
scopes:
- name: Nowlun Holding Corp Scopes
  scope_count: 3
  slug: nowlun-holding-corp-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: emerging
  composite: 17.9
  delta: -1.3
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 79.6
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 19.2
  provenance:
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Nowlun Holding Corp Authentication
  slug: nowlun-holding-corp-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Nowlun Holding Corp Domain Security
  slug: nowlun-holding-corp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nowlun-holding-corp
tags:
- Company
- Logistics
- Freight Forwarding
- Shipping
- Supply Chain
- Sea Freight
- Customs
- MENA
- MCP
website: https://nowlun.com
---

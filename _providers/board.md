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
    agent_skills: true
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
  score: 29.8
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: 'Board''s storefront agent-commerce API, provided natively by Shopify via the Universal Commerce Protocol (UCP 2026-04-08). Exposes an MCP endpoint for AI agents to search the catalog, build carts, and '
  name: Board Agent Commerce (UCP)
  slug: board-agent-commerce-ucp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://board.fun
- group: agent
  title: ''
  type: MCPServer
  url: mcp/board-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/board-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/board-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/board-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/board-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/board-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/board-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/board-domain-security.yml
- group: start
  title: ''
  type: Login
  url: https://account.board.fun
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://board.fun/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://board.fun/policies/terms-of-service
created: '2026-07-17'
description: 'Board (board.fun) is a maker of turn-based strategy board games sold direct-to-consumer through a Shopify storefront - its debut title, Thrasos, is a game in which players compete as Greek gods for control of ancient Greece by blessing and cursing cities to build influence. Board was surfaced as a portfolio company of Union Square Ventures and added to the API Evangelist network. Although Board ships no bespoke developer API, its store exposes a full, live agent-commerce surface via Shopify''s Universal Commerce Protocol (UCP): a hosted MCP endpoint, OpenID Connect customer accounts, published /llms.txt and /agents.md agent instructions, and Shop Pay / card payment handlers - enabling AI shopping agents to discover, cart, and (with human approval) purchase products.'
image: https://board.fun/cdn/shop/files/flipbook_001.png
layout: provider
mcp_servers:
- description: ''
  name: board-mcp.yml
  slug: board-mcpyml
modified: '2026-07-18'
name: Board
nav: Providers
network: true
overview: 'Board publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Commerce, E-Commerce, Board Games, and Agent Commerce.


  Board''s developer surface includes authentication and 12 more developer resources.'
random_paper: 10
scopes:
- name: Board Scopes
  scope_count: 4
  slug: board-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 21.3
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 21.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Board Authentication
  slug: board-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Board Domain Security
  slug: board-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: board
tags:
- Company
- Commerce
- E-Commerce
- Board Games
- Agent Commerce
- Universal Commerce Protocol
- Shopify
- MCP
website: https://board.fun
---

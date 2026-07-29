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
    agent_skills: true
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
  score: 27.9
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Hosted Model Context Protocol server that lets business partners find hourly workers and book shifts on Instawork using natural language via an AI assistant. Secured with OAuth 2.1 (PKCE + dynamic cli
  name: Instawork Partner MCP Server
  slug: instawork-partner-mcp-server
artifact_total: 5
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/instawork-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/instawork-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/instawork-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/instawork-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/instawork-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/instawork-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/instawork/skills
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/instawork
- group: operate
  title: ''
  type: Support
  url: https://help.instawork.com
- group: company
  title: ''
  type: Blog
  url: https://engineering.instawork.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.instawork.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.instawork.com/business
- group: start
  title: ''
  type: Login
  url: https://www.instawork.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.instawork.com/legal/instawork-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.instawork.com/legal/instawork-privacy-policy
- group: company
  title: ''
  type: Website
  url: https://instawork.com
created: '2026-07-17'
description: 'Instawork is a flexible-staffing marketplace that connects businesses in hospitality, warehouse, events, retail, and food service with vetted hourly workers ("Pros") for short-term shifts across the USA and Canada. Businesses post or rebook shifts and Instawork''s ML-driven "Smart assign" matching fills them, often within hours. Instawork''s developer surface is agent-native: rather than a public REST API it ships a hosted Partner MCP server (finch.instawork.com/mcp/partner) secured with OAuth 2.1, plus a published Agent Skill (github.com/instawork/skills) that lets AI assistants such as Claude and Cursor search locations and positions, price shifts, and create bookings on a business partner''s behalf. Backed by Craft Ventures, Greylock, GV, and Y Combinator.'
image: https://cdn.prod.website-files.com/63fd26f2fd0da53e0276079c/649a16c8f69460000a219a25_Instawork-OG-Image-blue.png
layout: provider
mcp_servers:
- description: ''
  name: instawork-mcp.yml
  slug: instawork-mcpyml
modified: '2026-07-19'
name: Instawork
nav: Providers
network: true
overview: 'Instawork publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Staffing, Gig Economy, and Hospitality.


  Instawork''s developer surface includes authentication, documentation, support, engineering blog, pricing, signup flow, and 11 more developer resources.'
random_paper: 70
scopes:
- name: Instawork Scopes
  scope_count: 2
  slug: instawork-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: emerging
  composite: 27.3
  delta: 0.2
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 79.6
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 27.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/instawork/refs/heads/main/screenshots/instawork-2026-07-25T222614.png
security:
- kind: authentication
  name: Instawork Authentication
  slug: instawork-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Instawork Domain Security
  slug: instawork-domain-security
  summary_line: TLSv1.3 · DMARC
slug: instawork
tags:
- Company
- Marketplace
- Staffing
- Gig Economy
- Hospitality
- Workforce
- Labor
- MCP
- Agent
website: https://instawork.com
---

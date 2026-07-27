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
  url: https://www.mutinyhq.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.mutinyhq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.mutinyhq.com/
- group: company
  title: ''
  type: Blog
  url: https://www.mutinyhq.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mutinyhq.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.mutinyhq.com/register
- group: start
  title: ''
  type: Login
  url: https://app.mutinyhq.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mutinyhq.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mutinyhq.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MutinyHQ
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mutiny-hq-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mutiny-hq-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mutiny-hq-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mutiny-hq-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mutiny-hq-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.mutinyhq.com/dpa
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mutiny-hq-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mutiny-hq-llms.txt
created: '2026-07-17'
description: Mutiny is a GTM (go-to-market) assistant built for customer-facing work — a vertical AI platform for B2B revenue teams (used by Snowflake, Uber, Rippling, GitLab, and Figma). It generates on-brand customer-facing assets such as deal rooms, pitch decks, business cases, ABM campaigns, comparison pages, and meeting recaps, and automates repetitive sales and marketing workflows through an agent, skill, and routine framework. Mutiny integrates with common CRM and GTM systems (Salesforce, HubSpot, Marketo, 6sense, Segment) and exposes a hosted Model Context Protocol (MCP) server so agents like Claude and ChatGPT can create, browse, and publish assets in conversation. Mutiny is backed by Insight Partners. It does not publish a general-purpose REST API; its programmatic entry point is the OAuth-protected MCP server.
image: https://framerusercontent.com/assets/Ec1hAhKLtluxlMfLydNP0NTrIA.png
layout: provider
mcp_servers:
- description: ''
  name: mutiny-hq-mcp.yml
  slug: mutiny-hq-mcpyml
modified: '2026-07-20'
name: Mutiny HQ
nav: Providers
network: true
overview: 'Mutiny HQ is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, GTM, Sales Enablement, Marketing, and Website Personalization.


  Mutiny HQ''s developer surface includes documentation, engineering blog, pricing, signup flow, authentication, and 13 more developer resources.'
random_paper: 56
scopes:
- name: Mutiny Hq Scopes
  scope_count: 5
  slug: mutiny-hq-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: emerging
  composite: 24.9
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 24.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Mutiny Hq Authentication
  slug: mutiny-hq-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Mutiny Hq Domain Security
  slug: mutiny-hq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mutiny-hq
tags:
- Company
- GTM
- Sales Enablement
- Marketing
- Website Personalization
- AI
- Agents
- MCP
- ABM
- Content Generation
website: https://www.mutinyhq.com/
---

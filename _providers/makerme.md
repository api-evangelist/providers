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
  scored_at: '2026-07-23'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://maker.co
- group: auth
  title: ''
  type: DomainSecurity
  url: security/makerme-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/makerme-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/makerme-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/makerme-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/makerme-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/makerme-scopes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/makerme-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.maker.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.maker.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.maker.co
- group: start
  title: ''
  type: Quickstart
  url: https://docs.maker.co/introduction/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.maker.co/community/support-and-contact
- group: commercial
  title: ''
  type: Pricing
  url: https://maker.co/pricing
- group: company
  title: ''
  type: Blog
  url: https://stories.maker.co
- group: design
  title: ''
  type: Conformance
  url: conformance/makerme-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/makerme-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/makerme-components.yml
created: '2026-07-17'
description: Maker (maker.co) provides AI code, content, and design agents for your website. Describe what you want in plain language and Maker designs it, codes it, and serves it live on your existing site — landing pages, product pages, A+ product content, personalized and location-based experiences, A/B variants, and Figma imports — with no developers, agencies, or rebuild required. Maker exposes a hosted, OAuth-secured MCP (Model Context Protocol) server at ai.maker.co/mcp so AI assistants such as Claude, ChatGPT, Claude Code, and Codex can create, edit, publish, and analyze Maker projects directly. Surfaced as a 500 Global portfolio company and enriched into the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/makerme.png
layout: provider
mcp_servers:
- description: ''
  name: makerme-mcp.yml
  slug: makerme-mcpyml
modified: '2026-07-20'
name: Maker.me
nav: Providers
network: true
overview: 'Maker.me is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Website Builder, No-Code, and Content Generation.


  Maker.me''s developer surface includes authentication, documentation, quickstart, support, pricing, engineering blog, and 12 more developer resources.'
random_paper: 24
scopes:
- name: Makerme Scopes
  scope_count: 0
  slug: makerme-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.3
  delta: 0.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 0.0
    developer_ergonomics: 54.3
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 23.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Makerme Authentication
  slug: makerme-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Makerme Domain Security
  slug: makerme-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: makerme
tags:
- Company
- AI
- Website Builder
- No-Code
- Content Generation
- Design
- Ecommerce
- MCP
- Agents
website: https://maker.co
---

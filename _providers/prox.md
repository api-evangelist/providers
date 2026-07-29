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
- description: Hosted MCP server that lets AI assistants query a manufacturer's Prox workspace (products, knowledge trees, wiki nodes) grounded in their manuals and make attributed, version-controlled edits. OAuth 2
  name: Prox MCP Connector
  slug: prox-mcp-connector
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://useprox.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://useprox.com/docs/mcp
- group: docs
  title: ''
  type: Documentation
  url: https://useprox.com/docs/mcp
- group: agent
  title: ''
  type: MCPServer
  url: mcp/prox-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/prox-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/prox-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/prox-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prox-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/prox-trust-center.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/prox-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prox-llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://useprox.com/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://signin.useprox.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://useprox.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://useprox.com/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:info@useprox.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/prox-inc/
created: '2026-07-17'
description: Prox is the AI product specialist for manufacturers of complex physical products. It grounds answers in a company's own manuals and catalogs, cites them to the page, and deploys everywhere customers, dealers, and field technicians already work, including a hosted Model Context Protocol (MCP) connector for ChatGPT, Claude, Copilot, and Gemini. Prox indexes internal technical knowledge and generates visual answers such as troubleshooters, product selectors, sizing calculators, and step-by-step guides. Backed by Y Combinator (F25), Bloomberg Beta, and investors from OpenAI and Microsoft, and based in San Francisco.
image: https://useprox.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: prox-mcp.yml
  slug: prox-mcpyml
modified: '2026-07-20'
name: Prox
nav: Providers
network: true
overview: 'Prox publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, MCP, Model Context Protocol, and Manufacturing.


  Prox''s developer surface includes documentation, authentication, pricing, signup flow, support, and 12 more developer resources.'
random_paper: 57
scopes:
- name: Prox Scopes
  scope_count: 4
  slug: prox-scopes
  summary_line: 4 scopes · authorizationCode/deviceCode
score:
  band: emerging
  composite: 27.5
  delta: -0.5
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 28.0
  provenance:
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Prox Authentication
  slug: prox-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Prox Domain Security
  slug: prox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Prox Trust Center
  slug: prox-trust-center
  summary_line: trust center published
slug: prox
tags:
- Company
- Artificial Intelligence
- MCP
- Model Context Protocol
- Manufacturing
- Product Support
- Knowledge Base
- Documentation
- Agents
website: https://useprox.com/
---

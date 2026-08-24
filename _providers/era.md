---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 28.8
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: 'Era''s remote Model Context Protocol server. Connect bank accounts to any MCP-compatible AI agent and manage money through natural conversation: spending analysis, cash-flow forecasting, transaction au'
  name: Era Context MCP Server
  slug: era-context-mcp-server
artifact_total: 8
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/era-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/era-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/era-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/era-api-catalog.json
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/era-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/era-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/era-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/era-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/era-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/era-plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/era-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://era.app/context/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/era-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/era-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://era.app/context/finance-mcp
- group: docs
  title: ''
  type: Documentation
  url: https://era.app/help/mcp-server-era-context
- group: docs
  title: ''
  type: APIReference
  url: https://era.app/.well-known/mcp/server-card.json
- group: start
  title: ''
  type: GettingStarted
  url: https://era.app/help/mcp-server-era-context
- group: company
  title: ''
  type: Blog
  url: https://era.app/articles
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/era-app
- group: commercial
  title: ''
  type: Pricing
  url: https://era.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://era.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://era.app/privacy
- group: company
  title: ''
  type: Website
  url: https://era.app
created: '2026-07-17'
description: Era is an AI-native personal finance platform that connects a user's bank accounts to any MCP-compatible AI assistant — Claude, ChatGPT, Gemini, Cursor, and others — so people can analyze spending, forecast cash flow, automate transaction categorization, and manage money through natural conversation. Every capability is exposed through the Era Context remote MCP server (65 tools over Streamable HTTP, OAuth 2.1) rather than a traditional REST API, with a portable cross-agent memory layer, scoped consent, and hard safety boundaries. Founded in 2023 by Stripe alumni and backed by Northzone, Era is a registered investment adviser targeting the mass-affluent market across the US, UK, and Canada.
image: https://era.app/social-card.png
layout: provider
mcp_servers:
- description: AI-native personal finance management. Connect bank accounts, analyze spending, forecast cash flow, automate transactions, and manage your money through natural conversation via MCP.
  name: Era Context
  slug: era-context
modified: '2026-07-19'
name: Era
nav: Providers
network: true
overview: 'Era publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Artificial Intelligence, Personal Finance, and Wealth Management.


  Era''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Era Plans
  plan_count: 4
  slug: era-plans
random_paper: 18
rate_limits:
- limit_count: 4
  name: Era Rate Limits
  slug: era-rate-limits
scopes:
- name: Era Scopes
  scope_count: 10
  slug: era-scopes
  summary_line: 10 scopes · authorizationCode
score:
  band: developing
  composite: 44.6
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.2
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 44.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 60.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/era/refs/heads/main/screenshots/era-2026-07-25T213555.png
security:
- kind: authentication
  name: Era Authentication
  slug: era-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Era Domain Security
  slug: era-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Era Vulnerability Disclosure
  slug: era-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: era
tags:
- Company
- Fintech
- Artificial Intelligence
- Personal Finance
- Wealth Management
- MCP
- agent-native
- Open Banking
- Authentication
website: https://era.app
---

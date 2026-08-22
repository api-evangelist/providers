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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
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
  score: 19.9
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'Hosted MCP server (https://mcp.rindler.ai) that exposes mapped websites as deterministic, typed agent tools over HTTP with OAuth 2.0 PKCE. Core tools: start_session, dispatch_action, extract_content, '
  name: Rindler MCP Server
  slug: rindler-mcp-server
artifact_total: 5
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://rindler.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://rindler.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://rindler.ai/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://rindler.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://chat.rindler.ai/?from=rindler-site
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rindler.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rindler.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://rindler.ai/faq
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rindler-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rindler-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rindler-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/rindler-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rindler-conventions.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rindler-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rindler-domain-security.yml
created: '2026-07-17'
description: Rindler is a Y Combinator (Summer 2026) company that operates a hosted Model Context Protocol (MCP) server turning any pre-onboarded website — including sites that have no API — into a deterministic, typed set of tools that AI agents can reliably use. Agents open a session against a mapped site, dispatch a semantic action (search, add to cart, submit a form, move a candidate, pull a statement), and receive structured JSON records instead of raw HTML, accessibility trees, or DOM selectors. Rindler handles authentication, 2FA, pop-ups, bot defenses, navigation, retries, and error recovery server-side, and re-verifies each site mapping against the real site before shipping it. It targets legacy portals, private SaaS dashboards, government registries, healthcare/insurance portals, ATS systems, and bank/brokerage sites.
image: https://rindler.ai/logo.png
layout: provider
mcp_servers:
- description: ''
  name: rindler-mcp.yml
  slug: rindler-mcpyml
modified: '2026-07-21'
name: Rindler
nav: Providers
network: true
overview: 'Rindler publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MCP, Model Context Protocol, AI Agents, and Web Automation.


  Rindler''s developer surface includes documentation, getting-started guide, pricing, signup flow, support, authentication, and 10 more developer resources.'
random_paper: 17
scopes:
- name: Rindler Scopes
  scope_count: 3
  slug: rindler-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 27.5
  delta: -0.9
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 49.4
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 28.4
  provenance:
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Rindler Authentication
  slug: rindler-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Rindler Domain Security
  slug: rindler-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: rindler
tags:
- Company
- MCP
- Model Context Protocol
- AI Agents
- Web Automation
- Browser Automation
- Structured Data
- Website to API
- Agent Tools
- Y Combinator
website: https://rindler.ai/docs
---

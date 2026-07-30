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
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://getduckbill.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://getduckbill.com/platform
- group: docs
  title: ''
  type: Documentation
  url: https://getduckbill.com/platform
- group: agent
  title: ''
  type: MCPServer
  url: mcp/duckbill-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/duckbill-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/duckbill-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/duckbill-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/duckbill-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/duckbill-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://research.getduckbill.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://getduckbill.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.getduckbill.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.getduckbill.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getduckbill.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getduckbill.com/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:support@getduckbill.com
created: '2026-07-17'
description: 'Duckbill is an AI-plus-human task-completion service that executes the real-world errands people avoid: fighting refunds, disputes and billing errors, cancelling services, researching vendors and getting quotes, and booking appointments and reservations. It pairs AI planning with background-checked human "doers" who make the phone calls and handle the red tape, accepting requests by text, email, forwarded message, or app. Duckbill exposes this execution layer to AI agents through a hosted MCP (Model Context Protocol) server — "Connect to Claude" — plus platform API and CLI access, so developers can plug real human follow-through into any AI workflow. Backed by Forerunner Ventures, General Catalyst, and Uncork Capital.'
image: https://getduckbill.com/preview.png
layout: provider
mcp_servers:
- description: ''
  name: duckbill-mcp.yml
  slug: duckbill-mcpyml
modified: '2026-07-18'
name: Duckbill
nav: Providers
network: true
overview: 'Duckbill is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, AI Assistant, Personal Assistant, and Task Automation.


  Duckbill''s developer surface includes documentation, authentication, engineering blog, pricing, signup flow, support, and 10 more developer resources.'
random_paper: 22
scopes:
- name: Duckbill Scopes
  scope_count: 6
  slug: duckbill-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: emerging
  composite: 24.5
  delta: 0.1
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 43.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 24.4
  provenance:
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/duckbill/refs/heads/main/screenshots/duckbill-2026-07-25T212450.png
security:
- kind: authentication
  name: Duckbill Authentication
  slug: duckbill-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Duckbill Domain Security
  slug: duckbill-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: duckbill
tags:
- Company
- Consumer
- AI Assistant
- Personal Assistant
- Task Automation
- Agents
- MCP
- Concierge
website: https://getduckbill.com
---

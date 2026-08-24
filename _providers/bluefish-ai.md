---
access_model:
  confidence: medium
  label: Customer-only
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - https://www.bluefishai.com/contact/sales
  - https://platform.bluefishai.com/connected-apps/authorize
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.6
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: A live, first-party remote Model Context Protocol server that makes the Bluefish AI platform callable by agents over Streamable HTTP. It is protected by OAuth 2.1 and requires the mcp:connect scope; a
  name: Bluefish AI MCP Server
  slug: bluefish-ai-mcp
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.bluefishai.com/
- group: company
  title: ''
  type: Blog
  url: https://www.bluefishai.com/blog
- group: start
  title: ''
  type: Login
  url: https://platform.bluefishai.com/login
- group: operate
  title: ''
  type: Support
  url: https://www.bluefishai.com/contact/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bluefishai.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bluefishai.com/legal/privacy-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bluefish-ai-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bluefish-ai-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bluefish-ai-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bluefish-ai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bluefish-ai-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bluefish-ai-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bluefish-ai-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bluefish-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bluefish-ai-rate-limits.yml
created: '2026-07-17'
description: Bluefish AI is an enterprise AI marketing platform built for Fortune 500 brands to gain visibility and control over how they are represented across AI channels. The platform spans AI monitoring of brand reputation in AI-native experiences, generative engine optimization (GEO) to improve performance across AI search, GEO measurement frameworks, AI brand safety and accuracy verification, and agentic commerce tooling for AI-driven buying journeys. It serves search, content, brand, and PR teams. Founded by martech veterans whose prior advertising technologies are now owned by Microsoft and Meta, and backed by enterprise and AI investors including Bloomberg Beta and Threshold Ventures, with a $43M Series B in 2026. Bluefish publishes no developer documentation, OpenAPI definition, or SDKs, but it does operate a live first-party remote MCP server at platform.bluefishai.com/mcp, protected by OAuth 2.1 with full RFC 9728 and RFC 8414 discovery and offered to customers as a connected
  app.
image: https://framerusercontent.com/images/HAib9zYaCuHpzLWP2A6EcUxHGM.png
layout: provider
mcp_servers:
- description: ''
  name: Bluefish AI MCP Server
  slug: bluefish-ai-mcp-server
modified: '2026-08-13'
name: Bluefish AI
nav: Providers
network: true
overview: 'Bluefish AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Artificial Intelligence, Generative Engine Optimization, and Brand Safety.


  Bluefish AI''s developer surface includes engineering blog, support, authentication, and 12 more developer resources.'
plans:
- name: Bluefish Ai Plans Pricing
  plan_count: 0
  slug: bluefish-ai-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Bluefish Ai Rate Limits
  slug: bluefish-ai-rate-limits
scopes:
- name: Bluefish Ai Scopes
  scope_count: 7
  slug: bluefish-ai-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: emerging
  composite: 20.2
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 20.2
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bluefish-ai/refs/heads/main/screenshots/bluefish-ai-2026-07-25T203448.png
security:
- kind: authentication
  name: Bluefish Ai Authentication
  slug: bluefish-ai-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Bluefish Ai Domain Security
  slug: bluefish-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bluefish-ai
tags:
- Company
- Marketing
- Artificial Intelligence
- Generative Engine Optimization
- Brand Safety
- Agentic Commerce
- Analytics
- MCP
- Agents
website: https://www.bluefishai.com/
---

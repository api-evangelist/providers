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
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.aninebing.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/anine-bing-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/anine-bing-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/anine-bing-agents.md
- group: agent
  title: ''
  type: WellKnown
  url: well-known/anine-bing-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/anine-bing-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/anine-bing-openid-configuration.json
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/anine-bing-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anine-bing-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aninebing.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aninebing.com/policies/terms-of-service
- group: company
  title: ''
  type: Blog
  url: https://www.aninebing.com/blogs/journal
- group: operate
  title: ''
  type: Support
  url: https://www.aninebing.com/pages/contact
created: '2026-07-17'
description: 'Anine Bing is a Los Angeles-based contemporary womenswear and fashion brand selling apparel, denim, footwear, and accessories direct to consumers through its online store at aninebing.com. The storefront runs on Shopify and exposes a modern agent-commerce surface: a published /llms.txt and /agents.md, a Universal Commerce Protocol (ucp.dev) merchant profile at /.well-known/ucp, and a live UCP shopping MCP endpoint for agent-driven catalog search, cart, and buyer-approved checkout. Customer authentication is provided by Shopify''s Customer Account API over OpenID Connect. Originally added to the API Evangelist network as a portfolio lead of Index Ventures, this profile has been enriched from the brand''s real public agent, auth, and discovery surfaces.'
image: https://www.aninebing.com/cdn/shop/files/Screen_Shot_2019-11-20_at_9.53.49_AM.png?v=1614725796
layout: provider
mcp_servers:
- description: ''
  name: Anine Bing UCP shopping MCP
  slug: anine-bing-ucp-shopping-mcp
modified: '2026-07-17'
name: Anine Bing
nav: Providers
network: true
overview: 'Anine Bing is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Fashion, Apparel, and Ecommerce.


  Anine Bing''s developer surface includes authentication, engineering blog, support, and 10 more developer resources.'
random_paper: 36
scopes:
- name: Anine Bing Scopes
  scope_count: 4
  slug: anine-bing-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 17.6
  delta: 0.1
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.5
  provenance:
    mcp: first-party
    skills: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Anine Bing Authentication
  slug: anine-bing-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Anine Bing Domain Security
  slug: anine-bing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: anine-bing
tags:
- Company
- Retail
- Fashion
- Apparel
- Ecommerce
- Shopify
- Agent Commerce
- MCP
website: https://www.aninebing.com
---

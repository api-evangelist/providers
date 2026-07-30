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
  score: 24.5
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: The Universal Commerce Protocol (UCP) agent-commerce surface for the LINSY HOME storefront (www.linsyhome.com, Shopify shop linsy-home.myshopify.com). Agents discover the merchant profile at /.well-kn
  name: LINSY HOME UCP Commerce API (MCP)
  slug: linsy-home-ucp
- description: The Universal Commerce Protocol (UCP) agent-commerce surface for the Linsy official storefront (linsy.com, Shopify shop linsyofficial.myshopify.com). Same UCP shopping service and capability set as th
  name: Linsy Official Store UCP Commerce API (MCP)
  slug: linsy-official-ucp
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linsy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.linsyhome.com/
- group: start
  title: ''
  type: Portal
  url: https://www.linsyhome.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.linsyhome.com/account/register
- group: start
  title: ''
  type: Login
  url: https://www.linsyhome.com/account/login
- group: operate
  title: ''
  type: Support
  url: https://www.linsyhome.com/pages/user-support
- group: operate
  title: ''
  type: Contact
  url: https://www.linsyhome.com/pages/contact
- group: company
  title: ''
  type: Blog
  url: https://www.linsyhome.com/blogs/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.linsyhome.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.linsyhome.com/policies/privacy-policy
- group: company
  title: ''
  type: About
  url: https://www.linsyhome.com/pages/about-us
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/linsy-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/linsy-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/linsy-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/linsy-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/linsy-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/linsy-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/linsy-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/linsy-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Linsy (LINSY HOME) is a direct-to-consumer modular furniture brand founded in 2007, selling True Modular sofas, sectionals, reclining couches, modular storage cabinets, replacement covers and accessories to households in the United States and other markets from U.S. warehouse fulfillment. Linsy operates two Shopify storefronts — www.linsyhome.com and linsy.com — and both expose a machine-readable agent surface: a published llms.txt/agents.md, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, an MCP endpoint for agent-driven catalog search, cart, checkout and fulfillment, and OpenID Connect discovery for Shopify customer accounts. Linsy was surfaced as a portfolio company of Hongshan.'
image: https://www.linsyhome.com/cdn/shop/files/LINSY_HOME_LOGO.png
layout: provider
mcp_servers:
- description: ''
  name: linsy-mcp.yml
  slug: linsy-mcpyml
modified: '2026-07-19'
name: Linsy
nav: Providers
network: true
overview: 'Linsy publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Retail, E-Commerce, and Furniture.


  Linsy''s developer surface includes developer portal, signup flow, support, engineering blog, authentication, and 15 more developer resources.'
random_paper: 67
scopes:
- name: Linsy Scopes
  scope_count: 0
  slug: linsy-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.2
  delta: -1.1
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 36.4
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 24.3
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Linsy Authentication
  slug: linsy-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Linsy Domain Security
  slug: linsy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: linsy
tags:
- Company
- Consumer
- Retail
- E-Commerce
- Furniture
- Home Goods
- Direct To Consumer
- Agentic Commerce
- Shopify
- MCP
website: https://www.linsyhome.com/
---

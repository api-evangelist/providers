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
  score: 23.1
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Agent-driven commerce surface for The Folklore's Shopify storefront, implementing the Universal Commerce Protocol over an MCP endpoint with buyer-approved checkout, plus read-only storefront JSON endp
  name: The Folklore Commerce (UCP)
  slug: the-folklore-commerce-ucp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://thefolklore.com/
- group: docs
  title: ''
  type: Documentation
  url: https://thefolklore.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://thefolklore.com/pages/faqs
- group: company
  title: ''
  type: Blog
  url: https://thefolklore.com/blogs/my-folklore
- group: commercial
  title: ''
  type: Pricing
  url: https://thefolklore.com/pages/pricing
- group: start
  title: ''
  type: SignUp
  url: https://thefolklore.com/pages/join-us
- group: start
  title: ''
  type: Login
  url: https://thefolklore.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thefolklore.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thefolklore.com/policies/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/the-folklore-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/the-folklore-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/the-folklore-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-folklore-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/the-folklore-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/the-folklore-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/the-folklore-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-folklore-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'The Folklore is a commerce platform and B2B wholesale marketplace that helps emerging and diverse consumer brands sell and market globally, connecting them with retail buyers and shoppers through dropship, shipping, and commerce technology. Its storefront runs on Shopify and exposes a modern agent-commerce surface: a Universal Commerce Protocol (UCP) MCP endpoint for agent-driven search, cart, checkout, and fulfillment, Shopify Customer Account OpenID Connect authentication, and published /llms.txt and /agents.md instructions so AI shopping agents can transact with buyer approval.'
image: https://thefolklore.com/cdn/shop/files/TheFolklore_Logo_Marketplace_B1__digital_430x_cbbbe0ff-35cb-4e95-b54c-dd5a61ad01d2.webp?v=1733852909
layout: provider
mcp_servers:
- description: ''
  name: the-folklore-mcp.yml
  slug: the-folklore-mcpyml
modified: '2026-07-21'
name: The Folklore
nav: Providers
network: true
overview: 'The Folklore publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Commerce, Wholesale, Marketplace, and Retail.


  The Folklore''s developer surface includes documentation, support, engineering blog, pricing, signup flow, authentication, and 12 more developer resources.'
random_paper: 36
scopes:
- name: The Folklore Scopes
  scope_count: 4
  slug: the-folklore-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 25.9
  delta: -0.4
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 26.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: The Folklore Authentication
  slug: the-folklore-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: The Folklore Domain Security
  slug: the-folklore-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: the-folklore
tags:
- Company
- Commerce
- Wholesale
- Marketplace
- Retail
- E-commerce
- Fashion
- Agentic Commerce
- Shopify
website: https://thefolklore.com/
---

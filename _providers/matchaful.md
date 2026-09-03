---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The store's Shopify-provided Universal Commerce Protocol agent-commerce surface — a live MCP shopping endpoint (search_catalog, create_cart, create_checkout, update_checkout, complete_checkout) docume
  name: Matchaful Agent Commerce (UCP)
  slug: matchaful-agent-commerce-ucp
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://matchaful.com/
- group: company
  title: ''
  type: Blog
  url: https://www.matchaful.com/blogs/the-matchaful-blog
- group: start
  title: ''
  type: SignUp
  url: https://www.matchaful.com/account/register
- group: operate
  title: ''
  type: Support
  url: https://www.matchaful.com/pages/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.matchaful.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.matchaful.com/policies/privacy-policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/matchaful-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/matchaful-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/matchaful-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Matchaful is a premium Japanese matcha brand selling single-origin, organically-grown ceremonial matcha from Shizuoka, Japan — ground to order, pesticide-free, and third-party tested under its Farm-to-Whisk program. It sells direct-to-consumer through a Shopify storefront and runs physical cafes, and is a Techstars portfolio company. Matchaful publishes no traditional developer REST API or OpenAPI, but its Shopify storefront exposes a live agent-commerce surface: an /llms.txt and /agents.md agent instruction set, a Universal Commerce Protocol (UCP, ucp.dev) merchant profile at /.well-known/ucp, a first-party MCP shopping endpoint at /api/ucp/mcp, and Shopify Customer Account OIDC/OAuth discovery documents served under the store domain.'
image: https://www.matchaful.com/cdn/shop/files/matchaful-organic-matcha-website-hero.jpg?v=1780489902
layout: provider
mcp_servers:
- description: ''
  name: Matchaful MCP Server
  slug: matchaful-mcp-server
modified: '2026-07-20'
name: Matchaful
nav: Providers
network: true
overview: 'Matchaful publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Matcha, Tea, Food and Beverage, and CPG.


  Matchaful''s developer surface includes engineering blog, signup flow, support, and 7 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.3
  provenance:
    mcp: first-party
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/matchaful/refs/heads/main/screenshots/matchaful-2026-08-07T172128.png
slug: matchaful
tags:
- Company
- Matcha
- Tea
- Food and Beverage
- CPG
- E-Commerce
- Direct to Consumer
- Shopify
- Agent Commerce
- UCP
- MCP
website: https://matchaful.com/
---

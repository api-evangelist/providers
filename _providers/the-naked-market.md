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
    agentic_commerce: platform
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.9
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://thenakedmarket.com
- group: operate
  title: ''
  type: Support
  url: https://www.thenakedmarket.com/pages/contact
- group: company
  title: ''
  type: Blog
  url: https://www.thenakedmarket.com/blogs/news
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-naked-market-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/the-naked-market-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/the-naked-market-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/the-naked-market-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-naked-market-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/the-naked-market-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/the-naked-market-conformance.yml
created: '2026-07-17'
description: 'The Naked Market is a San Francisco-based consumer packaged goods (CPG) company and brand incubator founded in 2019 by Harrison Fugman, Alex Kost, and Tim Marbach. It uses a "fast fail" end-to-end infrastructure to take a food or beverage product from idea to market in roughly three months, launching and acquiring socially conscious direct-to-consumer brands across snacks, drinks, and better-for-you categories. Its portfolio has included Project Breakfast, Flock crispy chicken chips, Avocrazy avocado puffs, Beach House Bowls, Rob''s Backstage Popcorn, and the low-alcohol aperitif brand Haus. The company raised $27.5 million in Series A funding in 2021 and is backed by HV Capital. It operates as a consumer brand holding company and does not publish a traditional developer API program, but its Shopify-hosted storefront exposes an agent-commerce surface: llms.txt agent instructions, a Universal Commerce Protocol (UCP) merchant profile, OpenID Connect discovery, and a live MCP
  endpoint for catalog search, cart, and buyer-approved checkout.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/the-naked-market.png
layout: provider
mcp_servers:
- description: ''
  name: The Naked Market Storefront MCP (Universal Commerce Protocol)
  slug: the-naked-market-storefront-mcp-universal-commerce-protocol
modified: '2026-07-21'
name: The Naked Market
nav: Providers
network: true
overview: 'The Naked Market is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Consumer Packaged Goods, Food and Beverage, and Direct to Consumer.


  The Naked Market''s developer surface includes support, engineering blog, authentication, and 7 more developer resources.'
random_paper: 16
scopes:
- name: The Naked Market Scopes
  scope_count: 4
  slug: the-naked-market-scopes
  summary_line: 4 scopes
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 11.7
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: The Naked Market Authentication
  slug: the-naked-market-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: The Naked Market Domain Security
  slug: the-naked-market-domain-security
  summary_line: TLSv1.3 · HSTS
slug: the-naked-market
tags:
- Company
- Consumer
- Consumer Packaged Goods
- Food and Beverage
- Direct to Consumer
- Snacks
- Brand Incubator
- E-Commerce
website: https://thenakedmarket.com
---

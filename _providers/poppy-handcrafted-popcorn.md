---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 28.3
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The agent-facing commerce surface for the Poppy Hand-Crafted Popcorn storefront, implementing the Universal Commerce Protocol (UCP) 2026-04-08 over MCP. Thirteen tools cover catalog search and lookup,
  name: Poppy Hand-Crafted Popcorn UCP Commerce API
  slug: poppy-hand-crafted-popcorn-ucp-commerce-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/poppy-handcrafted-popcorn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://poppyhandcraftedpopcorn.com/
- group: docs
  title: ''
  type: Documentation
  url: https://poppyhandcraftedpopcorn.com/agents.md
- group: docs
  title: ''
  type: APIReference
  url: https://poppyhandcraftedpopcorn.com/llms.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://poppyhandcraftedpopcorn.com/llms.txt
- group: operate
  title: ''
  type: Support
  url: https://poppyhandcraftedpopcorn.com/pages/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://poppyhandcraftedpopcorn.com/pages/faq
- group: company
  title: ''
  type: Blog
  url: https://poppyhandcraftedpopcorn.com/blogs/news
- group: commercial
  title: ''
  type: Pricing
  url: https://poppyhandcraftedpopcorn.com/collections/all
- group: start
  title: ''
  type: SignUp
  url: https://poppyhandcraftedpopcorn.com/account/register
- group: start
  title: ''
  type: Login
  url: https://poppyhandcraftedpopcorn.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://poppyhandcraftedpopcorn.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://poppyhandcraftedpopcorn.com/policies/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/poppy-handcrafted-popcorn-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/poppy-handcrafted-popcorn-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/poppy-handcrafted-popcorn-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/poppy-handcrafted-popcorn-plans-pricing.yml
created: '2026-08-26'
description: 'Poppy Hand-Crafted Popcorn is a woman-owned gourmet snack maker founded in 2014 by Ginger Frank in Asheville, North Carolina, producing small-batch sweet and savory popcorn from non-GMO corn and simple natural ingredients. It sells direct-to-consumer, through wholesale and corporate gifting, and via retailers across North America. Its public machine surface is not a developer API program but an agent-commerce one: the Shopify-hosted storefront publishes a first-party /llms.txt and /agents.md, a /.well-known/ucp Universal Commerce Protocol merchant profile, and an unauthenticated UCP MCP endpoint at /api/ucp/mcp exposing thirteen catalog, cart, checkout and order tools with full JSON Schema inputs.'
image: https://cdn.shopify.com/s/files/1/0424/8387/6008/files/New_Bags_Collections_-_web_banner.jpg?v=1704995950
layout: provider
mcp_servers:
- description: ''
  name: Poppy Hand-Crafted Popcorn UCP Commerce MCP Server
  slug: poppy-hand-crafted-popcorn-ucp-commerce-mcp-server
modified: '2026-08-26'
name: Poppy Handcrafted Popcorn
nav: Providers
network: true
overview: 'Poppy Handcrafted Popcorn publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food and Beverage, Consumer Packaged Goods, Retail, and E-Commerce.


  Poppy Handcrafted Popcorn''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 11 more developer resources.'
plans:
- name: Poppy Handcrafted Popcorn Plans Pricing
  plan_count: 0
  slug: poppy-handcrafted-popcorn-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Poppy Handcrafted Popcorn Rate Limits
  slug: poppy-handcrafted-popcorn-rate-limits
scopes:
- name: Poppy Handcrafted Popcorn Scopes
  scope_count: 0
  slug: poppy-handcrafted-popcorn-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 28.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/poppy-handcrafted-popcorn/refs/heads/main/screenshots/poppy-handcrafted-popcorn-2026-09-02T151753.png
security:
- kind: authentication
  name: Poppy Handcrafted Popcorn Authentication
  slug: poppy-handcrafted-popcorn-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Poppy Handcrafted Popcorn Domain Security
  slug: poppy-handcrafted-popcorn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: poppy-handcrafted-popcorn
tags:
- Company
- Food and Beverage
- Consumer Packaged Goods
- Retail
- E-Commerce
- Agent Commerce
- Universal Commerce Protocol
- MCP
- Shopify
- Snacks
website: https://poppyhandcraftedpopcorn.com/
---

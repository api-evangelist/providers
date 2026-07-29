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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cuyana-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cuyana.com/
- group: operate
  title: ''
  type: Support
  url: https://support.cuyana.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://cuyana.com/blogs/news
- group: start
  title: ''
  type: Login
  url: https://account.cuyana.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cuyana.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cuyana.com/policies/privacy-policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cuyana-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cuyana-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cuyana-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cuyana-scopes.yml
created: '2026-07-17'
description: 'Cuyana is a San Francisco-based direct-to-consumer women''s fashion brand founded in 2011 by Karla Gallardo and Shilpa Shah, built on a "Fewer, Better Things" philosophy of timeless, high-quality essentials — leather totes and handbags, small leather goods, and apparel — crafted from sustainable, Leather Working Group (LWG) certified materials through ethical manufacturing partnerships. The brand runs an omnichannel direct-to-consumer business across its e-commerce store and a growing fleet of retail locations. Cuyana''s storefront runs on Shopify, which exposes agent-facing surfaces on the cuyana.com domain: a live hosted Storefront MCP server at /api/mcp for AI shopping agents (search_catalog, get_cart, update_cart, get_product_details, search_shop_policies_and_faqs), and Shopify Customer Account OAuth/OIDC discovery documents under /.well-known/. Cuyana is backed by Canaan Partners.'
image: https://cdn.shopify.com/s/files/1/0712/5054/2907/files/BagsPLP_3.webp?v=1715724617
layout: provider
mcp_servers:
- description: ''
  name: cuyana-mcp.yml
  slug: cuyana-mcpyml
modified: '2026-07-18'
name: Cuyana
nav: Providers
network: true
overview: 'Cuyana is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fashion, Retail, E-commerce, and Direct-to-Consumer.


  Cuyana''s developer surface includes support, engineering blog, authentication, and 8 more developer resources.'
random_paper: 9
scopes:
- name: Cuyana Scopes
  scope_count: 4
  slug: cuyana-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 18.2
  delta: -0.6
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.8
  provenance:
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Cuyana Authentication
  slug: cuyana-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Cuyana Domain Security
  slug: cuyana-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cuyana
tags:
- Company
- Fashion
- Retail
- E-commerce
- Direct-to-Consumer
- Apparel
- Leather Goods
- Sustainable Fashion
- Shopify
website: https://www.cuyana.com/
---

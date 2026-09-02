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
    agentic_commerce: false
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
  score: 19.4
  scored_at: '2026-09-01'
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
  name: Cuyana MCP Server
  slug: cuyana-mcp-server
modified: '2026-07-18'
name: Cuyana
nav: Providers
network: true
overview: 'Cuyana is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fashion, Retail, E-Commerce, and Direct to Consumer.


  Cuyana''s developer surface includes support, engineering blog, authentication, and 8 more developer resources.'
random_paper: 11
scopes:
- name: Cuyana Scopes
  scope_count: 4
  slug: cuyana-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.3
  provenance:
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cuyana/refs/heads/main/screenshots/cuyana-2026-08-07T164003.png
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
- E-Commerce
- Direct to Consumer
- Apparel
- Leather Goods
- Sustainable Fashion
- Shopify
website: https://www.cuyana.com/
---

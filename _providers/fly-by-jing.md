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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'The live machine surface on the flybyjing.com domain: a Shopify Storefront MCP server for agentic product search and cart/checkout, plus a Shopify Customer Account API secured with OAuth 2.0 / OpenID '
  name: Fly By Jing Storefront (Shopify)
  slug: fly-by-jing-storefront-shopify
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://flybyjing.com/
- group: company
  title: ''
  type: About
  url: https://flybyjing.com/pages/about
- group: company
  title: ''
  type: Blog
  url: https://flybyjing.com/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://flybyjing.com/pages/faq
- group: operate
  title: ''
  type: Contact
  url: https://flybyjing.com/pages/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://flybyjing.com/collections/shop
- group: start
  title: ''
  type: Login
  url: https://account.flybyjing.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flybyjing.com/pages/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flybyjing.com/pages/privacy-policy
- group: company
  title: ''
  type: Instagram
  url: https://instagram.com/flybyjing
- group: other
  title: ''
  type: TikTok
  url: https://www.tiktok.com/@flybyjing
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fly-by-jing-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fly-by-jing-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fly-by-jing-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fly-by-jing-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fly-by-jing-domain-security.yml
created: '2026-07-17'
description: 'Fly By Jing is a premium Chinese food brand founded by James Beard Award-winning chef and entrepreneur Jing Gao in 2018, best known for its small-batch Sichuan Chili Crisp made in Chengdu without preservatives or added sugar. The company sells its signature sauces, noodles, gift sets, and pantry staples direct-to-consumer through a Shopify-powered storefront at flybyjing.com. From an API Evangelist perspective, the storefront exposes a real, live machine surface: a Shopify Storefront MCP server at /api/mcp (search_catalog, get_cart, update_cart, get_product_details, search_shop_policies_and_faqs) and a Shopify Customer Account API secured with OAuth 2.0 / OpenID Connect, discoverable via the domain''s /.well-known/openid-configuration document. Surfaced originally as a Techstars portfolio lead and enriched here from live discovery probes of the store domain.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fly-by-jing.png
layout: provider
mcp_servers:
- description: ''
  name: Fly By Jing MCP Server
  slug: fly-by-jing-mcp-server
modified: '2026-07-19'
name: Fly By Jing
nav: Providers
network: true
overview: 'Fly By Jing publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food and Beverage, Consumer Packaged Goods, E-Commerce, and Shopify.


  Fly By Jing''s developer surface includes engineering blog, support, pricing, authentication, and 12 more developer resources.'
random_paper: 14
scopes:
- name: Fly By Jing Scopes
  scope_count: 0
  slug: fly-by-jing-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.3
  provenance:
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fly-by-jing/refs/heads/main/screenshots/fly-by-jing-2026-08-07T165356.png
security:
- kind: authentication
  name: Fly By Jing Authentication
  slug: fly-by-jing-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Fly By Jing Domain Security
  slug: fly-by-jing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fly-by-jing
tags:
- Company
- Food and Beverage
- Consumer Packaged Goods
- E-Commerce
- Shopify
- Direct to Consumer
- MCP
- Agentic Commerce
website: https://flybyjing.com/
---

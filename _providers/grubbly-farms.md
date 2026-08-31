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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: 'The machine-consumable surface of the Grubbly Farms Shopify storefront: a hosted Storefront MCP server for agentic product discovery and cart/checkout, plus a Customer Account OpenID Connect / OAuth 2'
  name: Grubbly Farms Storefront (Shopify MCP & Customer Account)
  slug: grubbly-farms-storefront-shopify-mcp-customer-account
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://grubblyfarms.com/
- group: operate
  title: ''
  type: Support
  url: https://help.grubblyfarms.com/en-US
- group: company
  title: ''
  type: Blog
  url: https://grubblyfarms.com/blogs/the-flyer
- group: start
  title: ''
  type: SignUp
  url: https://account.grubblyfarms.com/
- group: start
  title: ''
  type: Login
  url: https://account.grubblyfarms.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://grubblyfarms.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://grubblyfarms.com/policies/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/grubbly-farms-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/grubbly-farms-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/grubbly-farms-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/grubbly-farms-openid-configuration.json
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/grubbly-farms-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/grubbly-farms-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/grubbly-farms-domain-security.yml
created: '2026-07-17'
description: 'Grubbly Farms is a direct-to-consumer backyard-poultry brand that sells chicken and duck feed, treats, supplements, and coop supplies made with dried black soldier fly grubs raised on upcycled food surplus as a sustainable protein source. The storefront runs on Shopify and, like other Shopify merchants, exposes a real machine-consumable surface: a hosted Storefront MCP server at /api/mcp (product catalog search, cart management, product detail lookup, and shop-policy/FAQ retrieval) and a Shopify Customer Account identity surface published through OpenID Connect / OAuth 2.0 discovery documents (authorization-code with PKCE), including Shopify''s customer-account-api and customer-account-mcp-api scopes. This profile captures that discoverable agent and identity surface rather than a traditional developer-published REST API.'
image: https://cdn.shopify.com/s/files/1/1407/3744/files/MicrosoftTeams-image_5.png?v=1743713875
layout: provider
mcp_servers:
- description: ''
  name: Grubbly Farms MCP Server
  slug: grubbly-farms-mcp-server
modified: '2026-07-19'
name: Grubbly Farms
nav: Providers
network: true
overview: 'Grubbly Farms publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Consumer Packaged Goods, and Pet & Animal.


  Grubbly Farms'' developer surface includes support, engineering blog, signup flow, authentication, and 10 more developer resources.'
random_paper: 18
scopes:
- name: Grubbly Farms Scopes
  scope_count: 4
  slug: grubbly-farms-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 19.7
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/grubbly-farms/refs/heads/main/screenshots/grubbly-farms-2026-08-07T165848.png
security:
- kind: authentication
  name: Grubbly Farms Authentication
  slug: grubbly-farms-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Grubbly Farms Domain Security
  slug: grubbly-farms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: grubbly-farms
tags:
- Company
- E-Commerce
- Retail
- Consumer Packaged Goods
- Pet & Animal
- Poultry
- Sustainability
- Shopify
- MCP
- Agentic Commerce
website: https://grubblyfarms.com/
---

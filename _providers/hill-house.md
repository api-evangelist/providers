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
  url: security/hill-house-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hill-house-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hill-house-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hill-house-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hill-house-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://hillhousehome.com
- group: start
  title: ''
  type: Login
  url: https://hillhousehome.com/account/login
- group: operate
  title: ''
  type: Support
  url: https://hillhousehome.com/pages/contact
- group: company
  title: ''
  type: Blog
  url: https://hillhousehome.com/blogs/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hillhousehome.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hillhousehome.com/policies/terms-of-service
created: '2026-07-17'
description: Hill House Home is a digital-first lifestyle brand that brings beauty and joy to everyday rituals. Since launching with bedding in 2016 it has extended its collections to bath, baby, accessories and apparel, including the widely beloved Nap Dress. The direct-to-consumer storefront at hillhousehome.com runs on Shopify and exposes a live, public Storefront MCP server (catalog search, cart, and store-policy tools) at /api/mcp, plus Shopify Customer Account OAuth 2.0 / OpenID Connect discovery for customer-scoped access. Surfaced as an 8vc portfolio company and enriched from its public commerce surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hill-house.png
layout: provider
mcp_servers:
- description: ''
  name: Hill House Home Storefront MCP
  slug: hill-house-home-storefront-mcp
modified: '2026-07-19'
name: Hill House
nav: Providers
network: true
overview: 'Hill House is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Home Goods, and Apparel.


  Hill House''s developer surface includes authentication, support, engineering blog, and 8 more developer resources.'
random_paper: 10
scopes:
- name: Hill House Scopes
  scope_count: 4
  slug: hill-house-scopes
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
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hill-house/refs/heads/main/screenshots/hill-house-2026-08-07T170218.png
security:
- kind: authentication
  name: Hill House Authentication
  slug: hill-house-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Hill House Domain Security
  slug: hill-house-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hill-house
tags:
- Company
- E-Commerce
- Retail
- Home Goods
- Apparel
- Direct to Consumer
- Consumer Brand
- Shopify
- MCP
website: https://hillhousehome.com
---

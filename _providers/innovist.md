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
  score: 20.3
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://innovist.com/
- group: company
  title: ''
  type: Blog
  url: https://innovist.com/blogs/all
- group: operate
  title: ''
  type: Support
  url: https://innovist.com/pages/contact-us
- group: start
  title: ''
  type: Login
  url: https://innovist.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://innovist.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://innovist.com/policies/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/innovist-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/innovist-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/innovist-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/innovist-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/innovist-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/innovist-domain-security.yml
created: '2026-07-17'
description: 'Innovist is an Accel-backed, science-backed direct-to-consumer personal care house based in India, building and operating a portfolio of skincare, haircare and suncare brands including Chemist At Play, Bare Anatomy and Sunscoop. It sells direct to consumers through a Shopify-powered online store at innovist.com, offering free delivery and category-wide discounts across skin, hair and sun care. While Innovist does not publish a traditional developer API program, its storefront natively implements agent-facing commerce surfaces: a customer-account OpenID Connect identity layer, a published llms.txt / agents.md for AI shopping assistants, and a Universal Commerce Protocol (UCP) MCP endpoint that lets approved agents search the catalog, build carts and complete buyer-approved checkouts.'
image: https://innovist.com/cdn/shop/files/1200_628.png?v=1724222722
layout: provider
mcp_servers:
- description: ''
  name: Innovist MCP Server
  slug: innovist-mcp-server
modified: '2026-07-19'
name: Innovist
nav: Providers
network: true
overview: 'Innovist is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Personal Care, Skincare, and Hair Care.


  Innovist''s developer surface includes engineering blog, support, authentication, and 9 more developer resources.'
random_paper: 8
scopes:
- name: Innovist Scopes
  scope_count: 4
  slug: innovist-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 15.1
  coverage:
    artifact_dirs: 8
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.1
  provenance:
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/innovist/refs/heads/main/screenshots/innovist-2026-08-07T170712.png
security:
- kind: authentication
  name: Innovist Authentication
  slug: innovist-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Innovist Domain Security
  slug: innovist-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: innovist
tags:
- Company
- Consumer
- Personal Care
- Skincare
- Hair Care
- Suncare
- Direct to Consumer
- E-Commerce
- Shopify
- Agentic Commerce
website: https://innovist.com/
---

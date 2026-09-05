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
  scored_at: '2026-09-04'
api_count: 3
apis:
- description: Universal Commerce Protocol (UCP) merchant surface for the Skullcandy Shopify storefront. Agents discover capabilities at /.well-known/ucp and transact against a hosted MCP endpoint (catalog search, c
  name: Skullcandy Agentic Commerce (UCP)
  slug: skullcandy-agentic-commerce-ucp
- description: 'Shopify Customer Account API for the Skullcandy store, secured with OpenID Connect / OAuth 2.0 (authorization code + PKCE). Scopes include customer-account-api:full and customer-account-mcp-api:full. '
  name: Skullcandy Customer Account API (Shopify)
  slug: skullcandy-customer-account-api-shopify
- description: 'Unauthenticated read-only storefront endpoints for browsing catalog data: product JSON (/products/{handle}.json), collection JSON (/collections/{handle}/products.json), search, and sitemap.xml.'
  name: Skullcandy Storefront Data (read-only)
  slug: skullcandy-storefront-data-read-only
artifact_total: 7
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/skullcandy-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/skullcandy-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/skullcandy-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/skullcandy-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/skullcandy-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/skullcandy-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skullcandy-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://shopify.dev
- group: docs
  title: ''
  type: Documentation
  url: https://ucp.dev/2026-04-08/specification/overview/
- group: operate
  title: ''
  type: Support
  url: https://support.skullcandy.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/skullcandy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.skullcandy.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.skullcandy.com/policies/terms-of-service
created: '2026-07-17'
description: 'Skullcandy is a US consumer-audio brand that designs and sells headphones, wireless earbuds, gaming headsets, and Bluetooth speakers. Its e-commerce storefront at skullcandy.com runs on Shopify, and rather than a traditional developer program the brand exposes a modern agentic-commerce surface: an agent-facing llms.txt / agents.md, a Universal Commerce Protocol (UCP) merchant profile with a hosted Model Context Protocol (MCP) endpoint for catalog search, cart, checkout and fulfillment, a Shopify Customer Account API secured with OpenID Connect / OAuth 2.0 (including a customer-account MCP scope), and read-only storefront JSON endpoints for products and collections. This profile captures that agent- and API-facing surface as discovered on the live site.'
image: https://www.skullcandy.com/cdn/shop/files/new-social.jpg?v=1726116747
layout: provider
mcp_servers:
- description: Hosted Universal Commerce Protocol (UCP) shopping MCP server for the Skullcandy Shopify storefront. Agents call the MCP endpoint to search the catalog, build a cart, and drive a buyer-approved checkou
  name: Skullcandy MCP Server
  slug: skullcandy-mcp-server
modified: '2026-07-21'
name: Skullcandy
nav: Providers
network: true
overview: 'Skullcandy publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Electronics, Audio, Headphones, and E-Commerce.


  Skullcandy''s developer surface includes authentication, documentation, support, and 10 more developer resources.'
random_paper: 11
scopes:
- name: Skullcandy Scopes
  scope_count: 4
  slug: skullcandy-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 18.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 18.9
  provenance:
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/skullcandy/refs/heads/main/screenshots/skullcandy-2026-09-02T155747.png
security:
- kind: authentication
  name: Skullcandy Authentication
  slug: skullcandy-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Skullcandy Domain Security
  slug: skullcandy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: skullcandy
tags:
- Company
- Consumer Electronics
- Audio
- Headphones
- E-Commerce
- Retail
- Shopify
- Agentic Commerce
- MCP
- Universal Commerce Protocol
website: https://shopify.dev
---

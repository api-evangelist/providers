---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.9
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Cometeer's Universal Commerce Protocol shopping service, exposed over MCP (JSON-RPC 2.0 via HTTP POST) at /api/ucp/mcp and advertised from /.well-known/ucp. Thirteen tools cover catalog search and loo
  name: Cometeer UCP Commerce (MCP)
  slug: ucp-commerce
- description: Collection (category) browsing
  name: Cometeer Collections API
  slug: cometeer-collections-api
- description: Product catalog browsing
  name: Cometeer Products API
  slug: cometeer-products-api
- description: Storefront search
  name: Cometeer Search API
  slug: cometeer-search-api
artifact_total: 9
collections:
- collection_type: open
  name: Cometeer Storefront (read-only agent surface)
  slug: open-cometeer-storefront
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cometeer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cometeer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cometeer.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cometeer-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://help.cometeer.com/
- group: company
  title: ''
  type: Blog
  url: https://cometeer.com/blogs/tasting-notes
- group: commercial
  title: ''
  type: Pricing
  url: https://cometeer.com/pages/shop-all-coffee
- group: start
  title: ''
  type: SignUp
  url: https://account.cometeer.com/account
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cometeer.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cometeer.com/policies/privacy-policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cometeer-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cometeer-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cometeer-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cometeer-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cometeer-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cometeer-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cometeer-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cometeer-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-01'
description: 'Cometeer is a Gloucester, Massachusetts coffee company, founded in 2015 by Matthew Roberts and Douglas Hoon, that brews specialty coffee at high extraction and then flash-freezes it with liquid nitrogen into single-serve capsules shipped direct to consumers by subscription. Coffees are roasted by third-wave partners including Counter Culture, Intelligentsia, Onyx, Square Mile, Equator and George Howell. Cometeer publishes no developer API, but its Shopify-hosted storefront exposes a substantial machine-readable agent surface: an /llms.txt agent instruction set, OpenID Connect and RFC 8414 authorization-server metadata on its own apex host, and a live Universal Commerce Protocol (UCP) merchant profile advertising an MCP endpoint for agent-driven cart, checkout and order flows.'
image: https://cometeer.com/cdn/shop/files/Cometeer01528.png?crop=center&height=480&v=1759521644&width=480
layout: provider
mcp_servers:
- description: ''
  name: Cometeer MCP Server
  slug: cometeer-mcp-server
modified: '2026-08-01'
name: Cometeer
nav: Providers
network: true
overview: 'Cometeer publishes 3 APIs on the [APIs.io](https://apis.io/) network: Collections API, Products API, and Search API. Tagged areas include Company, Coffee, Food and Beverage, E-Commerce, and Direct to Consumer.


  Cometeer''s developer surface includes documentation, support, engineering blog, pricing, signup flow, authentication, and 13 more developer resources.'
random_paper: 12
scopes:
- name: Cometeer Scopes
  scope_count: 4
  slug: cometeer-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 13.1
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 28.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cometeer/refs/heads/main/screenshots/cometeer-2026-08-07T163704.png
security:
- kind: authentication
  name: Cometeer Authentication
  slug: cometeer-authentication
  summary_line: none/openIdConnect/oauth2 · 3 schemes
- kind: domain-security
  name: Cometeer Domain Security
  slug: cometeer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cometeer
tags:
- Company
- Coffee
- Food and Beverage
- E-Commerce
- Direct to Consumer
- Retail
- Subscription
- Agentic Commerce
- Shopify
- MCP
website: https://cometeer.com/
---

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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: 'Agent-driven commerce surface for the TO THE MARKET store, implementing the Universal Commerce Protocol over a hosted MCP endpoint. Agents can search the catalog, create carts, and run buyer-approved '
  name: TO THE MARKET Agent Commerce (UCP / MCP)
  slug: to-the-market-agent-commerce-ucp-mcp
artifact_total: 5
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/to-the-market-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/to-the-market-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/to-the-market-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/to-the-market-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/to-the-market-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/to-the-market-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/to-the-market-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/to-the-market-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tothemarket.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tothemarket.com/policies/terms-of-service
- group: start
  title: ''
  type: SignUp
  url: https://tothemarket.com/pages/wholesale-account-sign-up
- group: start
  title: ''
  type: Login
  url: https://tothemarket.com/account/login
- group: operate
  title: ''
  type: Support
  url: https://tothemarket.com/pages/contact-us
- group: company
  title: ''
  type: Website
  url: https://tothemarket.com/
created: '2026-07-17'
description: 'TO THE MARKET is a mission-driven commerce company that combines TRACERA supply-chain software with a curated catalog of "Global Good" sustainable, ethically sourced products, delivering verified impact, compliance, and transparency to buyers and enterprise sourcing teams. Its Shopify-powered storefront at tothemarket.com exposes a native agent-commerce surface: a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp and a hosted Model Context Protocol (MCP) endpoint, letting AI shopping agents discover the catalog, build carts, and run buyer-approved checkout. Buyer and customer actions authenticate through the Shopify Customer Account API over OAuth2/OpenID Connect.'
image: https://tothemarket.com/cdn/shop/files/logo.png
layout: provider
mcp_servers:
- description: ''
  name: TO THE MARKET MCP Server
  slug: to-the-market-mcp-server
modified: '2026-07-21'
name: TO THE MARKET
nav: Providers
network: true
overview: 'TO THE MARKET publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Commerce, E-Commerce, Sustainability, and Supply Chain.


  TO THE MARKET''s developer surface includes authentication, signup flow, support, and 11 more developer resources.'
random_paper: 1
scopes:
- name: To The Market Scopes
  scope_count: 4
  slug: to-the-market-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 20.0
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/to-the-market/refs/heads/main/screenshots/to-the-market-2026-09-02T163835.png
security:
- kind: authentication
  name: To The Market Authentication
  slug: to-the-market-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: To The Market Domain Security
  slug: to-the-market-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: to-the-market
tags:
- Company
- Commerce
- E-Commerce
- Sustainability
- Supply Chain
- Agent Commerce
- Shopify
- MCP
website: https://tothemarket.com/
---

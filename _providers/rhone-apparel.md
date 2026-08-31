---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: self
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
  score: 33.7
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Rhone's agent-facing commerce surface, implementing the Universal Commerce Protocol over MCP (JSON-RPC 2.0). Thirteen tools cover catalog search and lookup, product detail, cart create / update / canc
  name: Rhone UCP Commerce (MCP)
  slug: rhone-ucp-commerce-mcp
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rhone-apparel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rhone.com/
- group: docs
  title: ''
  type: Documentation
  url: https://rhone.myshopify.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rhone-apparel-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rhone-apparel-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rhone-apparel-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/rhone-apparel-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://www.rhone.com/blogs/pursuit
- group: operate
  title: ''
  type: Support
  url: https://www.rhone.com/pages/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rhone.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rhone.com/policies/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://www.rhone.com/account/login
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://www.hiive.com/securities/rhone-apparel-stock
created: '2026-08-26'
description: 'Rhone Apparel, Inc. is a direct-to-consumer men''s premium performance apparel and activewear brand founded in 2014 by brothers Nate and Ben Checketts and headquartered in Stamford, Connecticut. It sells through its own storefront, wholesale partners including Nordstrom and Bloomingdale''s, and its own retail locations. Rhone runs no developer program and publishes no OpenAPI, SDK or API documentation. It does, however, operate a real and reachable agent-commerce surface: its Shopify storefront serves a store-specific llms.txt and agents.md, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, an anonymous MCP endpoint exposing 13 catalog, cart, checkout and order tools with full JSON Schema inputSchemas, and Shopify Customer Accounts OIDC discovery branded on account.rhone.com. The company is profiled here as an agent-commerce participant rather than an API producer.'
image: https://rhone.myshopify.com/cdn/shop/files/Discount_auto_applied_1200x.png?v=1733928390
layout: provider
mcp_servers:
- description: ''
  name: Rhone Apparel MCP Server
  slug: rhone-apparel-mcp-server
modified: '2026-08-26'
name: Rhone Apparel
nav: Providers
network: true
overview: 'Rhone Apparel publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Apparel, Retail, E-Commerce, Direct to Consumer, and Agent Commerce.


  Rhone Apparel''s developer surface includes documentation, engineering blog, support, signup flow, and 10 more developer resources.'
plans:
- name: Rhone Apparel Plans Pricing
  plan_count: 0
  slug: rhone-apparel-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Rhone Apparel Rate Limits
  slug: rhone-apparel-rate-limits
scopes:
- name: Rhone Apparel Scopes
  scope_count: 0
  slug: rhone-apparel-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 19.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Rhone Apparel Authentication
  slug: rhone-apparel-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Rhone Apparel Domain Security
  slug: rhone-apparel-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: rhone-apparel
tags:
- Apparel
- Retail
- E-Commerce
- Direct to Consumer
- Agent Commerce
- Universal Commerce Protocol
- MCP
- Shopify
- Activewear
- Company
website: https://www.rhone.com/
---

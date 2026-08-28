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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
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
  score: 12.1
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: 'Agent-facing commerce surface for the Soylent storefront implementing the Universal Commerce Protocol over MCP: catalog search, cart, checkout, and fulfillment with a buyer-approval invariant on payme'
  name: Soylent Agent Commerce (UCP / MCP)
  slug: soylent-agent-commerce-ucp-mcp
artifact_total: 5
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/soylent-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/soylent-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/soylent-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/soylent-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/soylent-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/soylent-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/soylent-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/soylent-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://ucp.dev/2026-04-08/specification/overview/
- group: company
  title: ''
  type: Blog
  url: https://soylent.com/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://soylent.com/pages/contact
- group: start
  title: ''
  type: SignUp
  url: https://soylent.com/account/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://soylent.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://soylent.com/policies/terms-of-service
- group: company
  title: ''
  type: Website
  url: https://soylent.com
created: '2026-07-17'
description: 'Soylent is a nutrition company known for its plant-based, complete-nutrition meal-replacement drinks, powders, and bars, sold direct-to-consumer through its Shopify-powered online store at soylent.com. It reached the API Evangelist network as a portfolio company of a16z and GV. Soylent publishes no traditional developer program, but its storefront is agent-native: it implements the Universal Commerce Protocol (UCP) with a live MCP endpoint for agent-driven catalog search, cart, and buyer-approved checkout; publishes /llms.txt and /agents.md agent instructions; and exposes Shopify Customer Account OAuth 2.0 / OpenID Connect authentication with a discoverable authorization server. This profile captures that agent-commerce and authentication surface.'
image: https://soylent.com/cdn/shop/files/soylent_logo-01.png
layout: provider
mcp_servers:
- description: ''
  name: Soylent MCP Server
  slug: soylent-mcp-server
modified: '2026-07-21'
name: Soylent
nav: Providers
network: true
overview: 'Soylent publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Nutrition, Food and Beverage, and Meal Replacement.


  Soylent''s developer surface includes authentication, documentation, engineering blog, support, signup flow, and 10 more developer resources.'
random_paper: 5
scopes:
- name: Soylent Scopes
  scope_count: 4
  slug: soylent-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 22.3
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 22.3
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Soylent Authentication
  slug: soylent-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Soylent Domain Security
  slug: soylent-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: soylent
tags:
- Company
- Consumer
- Nutrition
- Food and Beverage
- Meal Replacement
- E-Commerce
- Retail
- Direct to Consumer
- Agent Commerce
- Universal Commerce Protocol
- Shopify
- MCP
website: https://soylent.com
---

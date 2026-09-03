---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The Universal Commerce Protocol (UCP) shopping service that Super Coffee's storefront implements over MCP transport. An anonymous tools/list returns 13 tools covering catalog search and lookup, produc
  name: Super Coffee UCP Commerce MCP
  slug: super-coffee-ucp-mcp
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/super-coffee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.drinksupercoffee.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.drinksupercoffee.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://help.drinksupercoffee.com/
- group: company
  title: ''
  type: Blog
  url: https://www.drinksupercoffee.com/blogs/news
- group: commercial
  title: ''
  type: Pricing
  url: https://www.drinksupercoffee.com/collections/all
- group: start
  title: ''
  type: SignUp
  url: https://www.drinksupercoffee.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.drinksupercoffee.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.drinksupercoffee.com/policies/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/super-coffee-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/super-coffee-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/super-coffee-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/super-coffee-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/super-coffee-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/super-coffee-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/super-coffee-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/super-coffee-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/super-coffee-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-05'
description: 'Super Coffee is the ready-to-drink coffee brand operated by Kitu Life, Inc., founded in 2015 by brothers Jordan, Jake and Jim DeCicco and distributed across tens of thousands of US retail locations alongside a direct-to-consumer online store at drinksupercoffee.com. The company is not a software vendor and publishes no developer program, but its Shopify-hosted storefront exposes a real, anonymous, machine-readable agent commerce surface: an /llms.txt and /agents.md agent instruction set, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, a live MCP endpoint at /api/ucp/mcp serving 13 catalog, cart, checkout and order tools with full JSON Schema inputs, and OAuth 2.0 / OpenID Connect discovery documents for Shopify customer accounts. Checkout is explicitly gated on contemporaneous human approval.'
image: https://www.drinksupercoffee.com/cdn/shop/files/super_coffee_logo_49f6a156-94a1-46e2-9440-f09c07a4bf74.jpg?v=1623443564&width=2048
layout: provider
mcp_servers:
- description: ''
  name: Super Coffee MCP Server
  slug: super-coffee-mcp-server
modified: '2026-08-05'
name: Super Coffee
nav: Providers
network: true
overview: 'Super Coffee publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food and Beverage, Consumer Packaged Goods, Retail, and E-Commerce.


  Super Coffee''s developer surface includes documentation, support, engineering blog, pricing, signup flow, authentication, and 13 more developer resources.'
random_paper: 2
scopes:
- name: Super Coffee Scopes
  scope_count: 4
  slug: super-coffee-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 23.8
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 25.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 23.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/super-coffee/refs/heads/main/screenshots/super-coffee-2026-09-02T161200.png
security:
- kind: authentication
  name: Super Coffee Authentication
  slug: super-coffee-authentication
  summary_line: oauth2/openIdConnect/none · 3 schemes
- kind: domain-security
  name: Super Coffee Domain Security
  slug: super-coffee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: super-coffee
tags:
- Company
- Food and Beverage
- Consumer Packaged Goods
- Retail
- E-Commerce
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- Shopify
website: https://www.drinksupercoffee.com/
---

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
  - rate-limits
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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.7
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: The Universal Commerce Protocol (UCP) shopping service for the M.Gemi store, exposed over Model Context Protocol at https://mgemi.com/api/ucp/mcp. An anonymous tools/list returns 13 tools with full JS
  name: M.Gemi UCP Commerce MCP API
  slug: mgemi-ucp-commerce-mcp-api
- description: 'The read-only Shopify storefront JSON surface for the M.Gemi catalog, documented by the store''s own /llms.txt for agents that only need to read store data without transacting: /products.json, /product'
  name: M.Gemi Storefront Product JSON
  slug: mgemi-storefront-product-json
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://mgemi.com
- group: docs
  title: ''
  type: Documentation
  url: https://mgemi.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/m-gemi-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/m-gemi-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/m-gemi-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/m-gemi-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/m-gemi-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/m-gemi-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/m-gemi-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/m-gemi-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/m-gemi-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/m-gemi-problem-types.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/m-gemi-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/m-gemi-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/m-gemi-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://mgemi.com/pages/faq
- group: company
  title: ''
  type: Blog
  url: https://mgemi.com/blogs/news
- group: start
  title: ''
  type: SignUp
  url: https://mgemi.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mgemi.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mgemi.com/policies/privacy-policy
created: '2026-08-25'
description: 'M.Gemi is a Boston-based direct-to-consumer footwear and leather-goods brand founded in 2015 by Maria Gangemi and Cheryl Kaplan, selling handcrafted Italian shoes and handbags made in small batches by family-owned workshops across Italy and released weekly. Its public API surface is not a developer program but an agent-commerce surface: the mgemi.com storefront publishes an /llms.txt and /agents.md agent instruction document, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, and a live, unauthenticated Model Context Protocol endpoint at /api/ucp/mcp exposing 13 tools for catalog search, cart, checkout and order retrieval, alongside the read-only Shopify storefront product JSON endpoints its own agent instructions document. Customer identity is served by a Shopify Customer Account OpenID Connect discovery document on the store host.'
image: https://cdn.shopify.com/s/files/1/0136/6648/4283/files/logomark2_d8d577da-e62c-4ca0-85a8-03466eb5c403.png?v=1632354360
layout: provider
mcp_servers:
- description: The Universal Commerce Protocol (UCP) shopping service for the M.Gemi store, exposed over Model Context Protocol. Advertised by the store's own /llms.txt and /agents.md and registered in the UCP merch
  name: M.Gemi UCP Commerce MCP Server
  slug: mgemi-ucp-commerce-mcp-server
modified: '2026-08-25'
name: M.Gemi
nav: Providers
network: true
overview: 'M.Gemi publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Fashion, and Footwear.


  M.Gemi''s developer surface includes documentation, authentication, support, engineering blog, signup flow, and 16 more developer resources.'
plans:
- name: M Gemi Plans Pricing
  plan_count: 0
  slug: m-gemi-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: M Gemi Rate Limits
  slug: m-gemi-rate-limits
scopes:
- name: M Gemi Scopes
  scope_count: 0
  slug: m-gemi-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 26.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/m-gemi/refs/heads/main/screenshots/m-gemi-2026-09-02T150434.png
security:
- kind: authentication
  name: M Gemi Authentication
  slug: m-gemi-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: M Gemi Domain Security
  slug: m-gemi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: m-gemi
tags:
- Company
- Retail
- E-Commerce
- Fashion
- Footwear
- Direct to Consumer
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- Shopify
- Catalog
- Checkout
website: https://mgemi.com
---

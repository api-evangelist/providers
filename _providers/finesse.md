---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 29.5
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: 'Agent-facing commerce endpoint implementing the Universal Commerce Protocol (version 2026-04-08, with 2026-01-23 also supported) over MCP/JSON-RPC 2.0. Thirteen tools cover catalog search and lookup, '
  name: FINESSE UCP Commerce MCP API
  slug: finesse-ucp-commerce-mcp-api
- description: 'Unauthenticated read-only product endpoints that FINESSE documents for agents in its own agents.md: a paged product feed at /products.json, per-product and per-collection JSON, product search, and a s'
  name: FINESSE Storefront JSON (read-only)
  slug: finesse-storefront-json-read-only
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/finesse-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://finesse.us/
- group: docs
  title: ''
  type: Documentation
  url: https://finesse.us/agents.md
- group: docs
  title: ''
  type: APIReference
  url: https://finesse.us/agents.md
- group: start
  title: ''
  type: GettingStarted
  url: https://finesse.us/agents.md
- group: operate
  title: ''
  type: Support
  url: https://finesse.us/pages/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://finesse.us/pages/faq
- group: company
  title: ''
  type: Blog
  url: https://finesse.us/blogs/news
- group: start
  title: ''
  type: SignUp
  url: https://finesse.us/account/register
- group: start
  title: ''
  type: Login
  url: https://finesse.us/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://finesse.us/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://finesse.us/policies/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/finesse-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/finesse-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/finesse-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/finesse-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/finesse-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/finesse-openid-configuration.json
- group: design
  title: ''
  type: Conventions
  url: conventions/finesse-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/finesse-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/finesse-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/finesse-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/finesse-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/finesse-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/finesse-plans-pricing.yml
created: '2026-08-12'
description: 'FINESSE is a Los Angeles direct-to-consumer womenswear brand, founded in 2018, that positions itself as an AI-driven fashion house: proprietary demand-prediction models combined with weekly community votes decide which styles get produced and in what quantity, which the company frames as an answer to overproduction and fashion waste. It sells dresses, tops, bottoms, jumpsuits, outerwear, footwear and accessories in sizes XS-3X. FINESSE publishes no developer API program, but its storefront at finesse.us ships a genuine agent surface: a live Universal Commerce Protocol merchant profile at /.well-known/ucp, an unauthenticated MCP endpoint at /api/ucp/mcp exposing 13 catalog, cart, checkout and order tools with full JSON Schema inputs, an /agents.md instruction document advertised through a dedicated agentic-discovery sitemap, a mirroring /llms.txt, and OAuth 2.0 / OpenID Connect metadata for shopper accounts on account.finesse.us.'
image: https://finesse.us/cdn/shop/files/opt-1.jpg?v=1745528244
layout: provider
mcp_servers:
- description: ''
  name: finesse-mcp.yml
  slug: finesse-mcpyml
- description: ''
  name: mcp
  slug: mcp
modified: '2026-08-12'
name: FINESSE
nav: Providers
network: true
overview: 'FINESSE publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, retail, ecommerce, fashion, and apparel.


  FINESSE''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 19 more developer resources.'
plans:
- name: Finesse Plans Pricing
  plan_count: 0
  slug: finesse-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Finesse Rate Limits
  slug: finesse-rate-limits
scopes:
- name: Finesse Scopes
  scope_count: 0
  slug: finesse-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.7
  delta: -0.1
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 28.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Finesse Authentication
  slug: finesse-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Finesse Domain Security
  slug: finesse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: finesse
tags:
- Company
- retail
- ecommerce
- fashion
- apparel
- direct-to-consumer
- agentic-commerce
- ucp
- mcp
- agent-native
- shopify
- consumer
website: https://finesse.us/
---

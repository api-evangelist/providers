---
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
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: Anonymous JSON-RPC 2.0 / Model Context Protocol endpoint implementing the Universal Commerce Protocol shopping service (version 2026-04-08). A tools/list call returns 13 tools with JSON Schema input c
  name: Flying Embers Commerce API (UCP over MCP)
  slug: flying-embers-commerce-mcp
- description: 'Unauthenticated read-only storefront JSON the merchant documents for agents that only need to read store data: product and collection JSON, product search, and the sitemap. Documented in the merchant'''
  name: Flying Embers Storefront Product JSON
  slug: flying-embers-storefront-json
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flying-embers-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.flyingembers.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.flyingembers.com/agents.md
- group: company
  title: ''
  type: Blog
  url: https://www.flyingembers.com/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://www.flyingembers.com/pages/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.flyingembers.com/pages/faq
- group: start
  title: ''
  type: Login
  url: https://www.flyingembers.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flyingembers.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flyingembers.com/policies/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/flying-embers-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flying-embers-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/flying-embers-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flying-embers-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/flying-embers-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/flying-embers-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/flying-embers-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/flying-embers-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/flying-embers-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flying-embers-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/flying-embers-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/flying-embers-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/flying-embers-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/flying-embers-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/flying-embers_stock/
created: '2026-08-16'
description: 'Flying Embers is a Ventura, California beverage company founded in 2017 by Bill Moses (co-founder of KeVita) that brews USDA-organic hard kombucha, canned cocktails and hard seltzers, sold in retail across the United States and direct-to-consumer from flyingembers.com. It is not a software vendor and runs no developer program, but its Shopify-hosted storefront serves a real, live agent surface from its own domain: a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, an anonymous Model Context Protocol endpoint at /api/ucp/mcp exposing 13 catalog, cart, checkout and order tools with full JSON Schema input contracts, a published /llms.txt and /agents.md carrying agent operating instructions, and OIDC/OAuth 2.0 discovery documents for customer accounts. Payment completion is explicitly gated on contemporaneous human approval and on an idempotency key.'
image: https://www.flyingembers.com/cdn/shop/files/fe-social-logo.png?v=1692298714
layout: provider
mcp_servers:
- description: Flying Embers serves a live, unauthenticated Model Context Protocol endpoint on its own domain as part of the Universal Commerce Protocol (UCP) shopping service. A tools/list call returns 13 real tool
  name: Flying Embers Commerce MCP (UCP)
  slug: flying-embers-commerce-mcp-ucp
modified: '2026-08-16'
name: Flying Embers
nav: Providers
network: true
overview: 'Flying Embers publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Commerce, E-Commerce, Retail, and Beverages.


  Flying Embers'' developer surface includes documentation, engineering blog, support, authentication, and 21 more developer resources.'
plans:
- name: Flying Embers Plans Pricing
  plan_count: 0
  slug: flying-embers-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Flying Embers Rate Limits
  slug: flying-embers-rate-limits
scopes:
- name: Flying Embers Scopes
  scope_count: 4
  slug: flying-embers-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 24.1
  coverage:
    artifact_dirs: 16
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 24.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Flying Embers Authentication
  slug: flying-embers-authentication
  summary_line: none/oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Flying Embers Domain Security
  slug: flying-embers-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flying-embers
tags:
- Company
- Commerce
- E-Commerce
- Retail
- Beverages
- Consumer Packaged Goods
- Agentic Commerce
- MCP
- Shopify
- Direct to Consumer
website: https://www.flyingembers.com/
---

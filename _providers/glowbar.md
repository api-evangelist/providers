---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.8
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Glowbar Agentic Access
  operation_count: 13
  slug: glowbar-agentic-access
  summary_line: 13 operations
api_count: 1
apis:
- description: The agent-facing commerce interface for the Glowbar online store. A Model Context Protocol (MCP) endpoint implementing the Universal Commerce Protocol (UCP) dev.ucp.shopping service, version 2026-04-0
  name: Glowbar UCP Commerce MCP API
  slug: glowbar-ucp-commerce-mcp-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://glowbar.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/glowbar-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/glowbar-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/glowbar-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/glowbar-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/glowbar-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/glowbar-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/glowbar-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://glowbar.com/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://glowbar.com/pages/faqs
- group: commercial
  title: ''
  type: Pricing
  url: https://glowbar.com/pages/membership
- group: start
  title: ''
  type: SignUp
  url: https://glowbar.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://glowbar.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://glowbar.com/policies/privacy-policy
created: '2026-08-22'
description: 'Glowbar is a New York-founded skincare studio chain offering expert 30-minute customized facials delivered by licensed estheticians across roughly 25 studios, sold through a monthly membership ($65/month for one facial, $120/month for two) alongside an $85 non-member walk-in price and a direct-to-consumer retail storefront of professional skincare products. Glowbar is not a software vendor and publishes no developer program, but its glowbar.com storefront runs on Shopify and therefore exposes a genuine, callable, unauthenticated agent surface: an agents.md / llms.txt agent instruction document, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, and a live MCP endpoint at /api/ucp/mcp that answers tools/list anonymously with 13 catalog, cart, checkout and order tools carrying full JSON Schema 2020-12 input schemas. Appointment booking itself runs on a third-party platform (Boulevard) at bookings.glowbar.com and publishes no contract.'
image: https://glowbar.com/cdn/shop/files/Face_your_skin._2.png?v=1681760540
layout: provider
mcp_servers:
- description: ''
  name: Glowbar UCP Commerce MCP
  slug: glowbar-ucp-commerce-mcp
modified: '2026-08-22'
name: Glowbar
nav: Providers
network: true
overview: 'Glowbar publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Skincare, Beauty, Retail, and Commerce.


  Glowbar''s developer surface includes engineering blog, support, pricing, signup flow, and 11 more developer resources.'
plans:
- name: Glowbar Plans Pricing
  plan_count: 0
  slug: glowbar-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Glowbar Rate Limits
  slug: glowbar-rate-limits
scopes:
- name: Glowbar Scopes
  scope_count: 0
  slug: glowbar-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.7
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 0.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
security:
- kind: authentication
  name: Glowbar Authentication
  slug: glowbar-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Glowbar Domain Security
  slug: glowbar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: glowbar
tags:
- Company
- Skincare
- Beauty
- Retail
- Commerce
- Ecommerce
- Consumer Services
- Shopify
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- Memberships
website: https://glowbar.com/
---

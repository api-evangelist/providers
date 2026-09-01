---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 16.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: A live, OAuth-protected Model Context Protocol endpoint served by CoolerX from its own apex host and discovered through the RFC 9728 protected-resource metadata document at https://coolerx.com/.well-k
  name: CoolerX Website MCP Server
  slug: coolerx-website-mcp-server
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cooler-screens-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cooler-screens-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.coolerx.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coolerx.com/privacy-policy/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cooler-screens-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cooler-screens-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cooler-screens-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cooler-screens-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cooler-screens-problem-types.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cooler-screens-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cooler-screens-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cooler-screens-mcp.yml
- group: operate
  title: ''
  type: Support
  url: https://coolerx.com/contact/
created: '2026-08-09'
description: CoolerX — formerly Cooler Screens — is an in-store retail media and merchandising technology company that turns cooler doors, endcaps, checkout coolers and pharmacy fixtures into IoT-connected digital screens. The platform pairs an AI "Intent Engine" for contextual targeting and conversion-funnel optimization with a Dynamic Content Engine for creative optimization, alongside campaign management, real-time measurement, and a data integration hub for product, price, promotion and context data. It is deployed with retailers including Kroger, Walgreens, Giant Eagle's GetGo, Chevron and Western Union, and is built on Microsoft Azure with NVIDIA, BOE, LG, Samsung and Foxconn as hardware and infrastructure partners. CoolerX sells to retailers and brands through a demo and sales motion; as of this profile it publishes no public developer program, API reference, SDK, or machine-readable specification.
image: https://www.coolerx.com/wp-content/uploads/2025/01/white-on-black-coolerX-logo.png
layout: provider
mcp_servers:
- description: CoolerX serves live Model Context Protocol endpoints from its own apex host, coolerx.com. They are published by the WordPress MCP Adapter plugin running on the CoolerX marketing site (WordPress 6.x on
  name: CoolerX Website MCP Server
  slug: coolerx-website-mcp-server
modified: '2026-08-12'
name: CoolerX
nav: Providers
network: true
overview: 'CoolerX publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Retail Media, Advertising, and Digital Signage.


  CoolerX''s developer surface includes authentication, support, and 11 more developer resources.'
plans:
- name: Cooler Screens Plans Pricing
  plan_count: 0
  slug: cooler-screens-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Cooler Screens Rate Limits
  slug: cooler-screens-rate-limits
scopes:
- name: Cooler Screens Scopes
  scope_count: 0
  slug: cooler-screens-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 14.0
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Cooler Screens Authentication
  slug: cooler-screens-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Cooler Screens Domain Security
  slug: cooler-screens-domain-security
  summary_line: TLSv1.3
slug: cooler-screens
tags:
- Company
- Retail
- Retail Media
- Advertising
- Digital Signage
- In-Store Media
- Merchandising
- Artificial Intelligence
- Internet of Things
website: https://www.coolerx.com/
---

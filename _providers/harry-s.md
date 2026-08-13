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
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: 'Anonymous Model Context Protocol server exposed by the Harry''s storefront at /api/mcp. Five tools — search_catalog, get_product_details, get_cart, update_cart and search_shop_policies_and_faqs — each '
  name: Harry's Storefront MCP Server
  slug: harrys-storefront-mcp-server
- description: Anonymous Model Context Protocol server exposed by the Flamingo storefront at /api/mcp, with the same five-tool surface as Harry's. Flamingo additionally publishes an llms.txt and an agents.md describ
  name: Flamingo Storefront MCP Server
  slug: flamingo-storefront-mcp-server
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/harry-s-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mammothbrands.com/
- group: company
  title: ''
  type: Blog
  url: https://www.mammothbrands.com/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mammothbrands.com/termsofuse
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mammothbrands.com/privacypolicy
- group: operate
  title: ''
  type: Support
  url: https://www.shopflamingo.com/pages/faq
- group: agent
  title: ''
  type: MCPServer
  url: mcp/harry-s-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/harry-s-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/harry-s-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/harry-s-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/harry-s-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/harry-s-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/harry-s-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/harry-s-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/harry-s-problem-types.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/harry-s-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-31'
description: Mammoth Brands is the consumer packaged goods company formerly known as Harry's Inc., renamed in April 2025 to reflect a portfolio that now spans Harry's (men's shaving and grooming), Flamingo (women's hair removal and body care), Lume and Mando (whole-body deodorant) and Coterie (modern baby care). Founded in 2013 by Jeff Raider and Andy Katz-Mayfield and still privately held, it reported $835M in 2024 revenue. It runs no developer programme and publishes no OpenAPI, but two of its brands operate on Shopify and therefore expose a live, anonymous Model Context Protocol server plus a Universal Commerce Protocol merchant profile on their own domains — a real agentic-commerce surface with no documentation portal behind it.
image: https://cdn.sanity.io/images/xo0k3v4q/production/c4a04b0d2919757ff10fdc3d96d577a136c6fa2d-256x256.png?w=256&h=256
layout: provider
mcp_servers:
- description: ''
  name: harry-s-mcp.yml
  slug: harry-s-mcpyml
modified: '2026-07-31'
name: Mammoth Brands
nav: Providers
network: true
overview: 'Mammoth Brands publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Packaged Goods, Retail, E-Commerce, and Personal Care.


  Mammoth Brands'' developer surface includes engineering blog, support, authentication, and 14 more developer resources.'
random_paper: 110
scopes:
- name: Harry S Scopes
  scope_count: 4
  slug: harry-s-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 20.9
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 20.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/harry-s/refs/heads/main/screenshots/harry-s-2026-08-07T170002.png
security:
- kind: authentication
  name: Harry S Authentication
  slug: harry-s-authentication
  summary_line: oauth2/openIdConnect/none · 4 schemes
- kind: domain-security
  name: Harry S Domain Security
  slug: harry-s-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: harry-s
tags:
- Company
- Consumer Packaged Goods
- Retail
- E-Commerce
- Personal Care
- Agentic Commerce
- Model Context Protocol
- Shopify
website: https://www.mammothbrands.com/
---

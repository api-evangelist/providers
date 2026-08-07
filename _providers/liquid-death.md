---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 57.4
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Liquid Death Agentic Access
  operation_count: 7
  slug: liquid-death-agentic-access
  summary_line: 7 operations
api_count: 3
apis:
- description: The anonymous, read-only product and collection JSON surface Liquid Death documents for AI agents in its agents.md, covering product records, collection listings, storefront search and the store-level
  name: Liquid Death Storefront Read-Only JSON API
  slug: liquid-death-storefront-read-only-json-api
- description: 'Liquid Death''s hosted Model Context Protocol server implementing the Universal Commerce Protocol dev.ucp.shopping service — catalog search and lookup, cart, checkout, fulfillment, discount and order. '
  name: Liquid Death UCP Shopping MCP
  slug: liquid-death-ucp-shopping-mcp
- description: The OpenID Connect and OAuth 2.0 authorization server for the Liquid Death customer account, hosted at account.liquiddeath.com and discoverable from both /.well-known/openid-configuration and /.well-k
  name: Liquid Death Customer Account OAuth
  slug: liquid-death-customer-account-oauth
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://liquiddeath.com/
- group: docs
  title: ''
  type: Documentation
  url: https://liquiddeath.com/agents.md
- group: start
  title: ''
  type: GettingStarted
  url: https://liquiddeath.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/liquid-death-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/liquid-death-well-known.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/liquid-death-storefront-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/liquid-death-storefront-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/liquid-death-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/liquid-death-tool-crosswalk.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/liquid-death-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/liquid-death-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/liquid-death-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/liquid-death-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/liquid-death-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/liquid-death-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/liquid-death-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/liquid-death-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/liquid-death-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/liquid-death-domain-security.yml
- group: operate
  title: ''
  type: FAQ
  url: https://liquiddeath.com/pages/faq
- group: operate
  title: ''
  type: Support
  url: https://liquiddeath.com/pages/summon-us
- group: company
  title: ''
  type: Blog
  url: https://liquiddeath.com/blogs/news
- group: other
  title: ''
  type: Shop
  url: https://liquiddeath.com/collections/all
- group: other
  title: ''
  type: WhereToBuy
  url: https://liquiddeath.com/pages/where-to-buy
- group: company
  title: ''
  type: Careers
  url: https://liquiddeath.com/pages/careers
- group: company
  title: ''
  type: About
  url: https://liquiddeath.com/pages/manifesto
- group: commercial
  title: ''
  type: TermsOfService
  url: https://liquiddeath.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://liquiddeath.com/policies/privacy-policy
- group: other
  title: ''
  type: RefundPolicy
  url: https://liquiddeath.com/policies/refund-policy
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/liquiddeath/
- group: other
  title: ''
  type: TikTok
  url: https://www.tiktok.com/@liquiddeath
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/liquid-death_stock/
created: '2026-08-01'
description: 'Liquid Death is a Los Angeles beverage company founded in 2014 by Mike Cessario, Pat Cook and JonRyan Riggins, selling still and sparkling mountain water, iced tea, flavored sparkling water, the Death Dust electrolyte powder and a Sparkling Energy line, all in recyclable aluminum tallboys and marketed through a deliberately horror-comedy brand voice. It has raised roughly $264M and was valued at $1.4B in its 2024 Series F. Liquid Death publishes no conventional developer portal, yet it is one of the more agent-forward direct-to-consumer storefronts in the catalog: liquiddeath.com serves a first-party agents.md (mirrored at /llms.txt), a dedicated agentic-discovery sitemap, an agent policy block inside robots.txt, a Universal Commerce Protocol merchant profile at /.well-known/ucp, a live UCP shopping MCP endpoint, and both OpenID Connect and RFC 8414 OAuth discovery documents for its customer account. The storefront exposes an anonymous read-only product and collection JSON
  surface, while every cart, checkout and order capability is confined to the identity-gated, idempotency-keyed MCP transport that requires contemporaneous human approval before payment.'
image: https://liquiddeath.com/cdn/shop/files/Liquid-Death-Preview-Image_7033558e-a84d-4880-8a70-87e84739f262.jpg?v=1681949476
layout: provider
mcp_servers:
- description: ''
  name: liquid-death-mcp.yml
  slug: liquid-death-mcpyml
modified: '2026-08-01'
name: Liquid Death
nav: Providers
network: true
overview: 'Liquid Death publishes 1 API on the [APIs.io](https://apis.io/) network: Storefront Read-Only JSON API. Tagged areas include Company, Beverages, Consumer Packaged Goods, Direct to Consumer, and Ecommerce.


  Liquid Death''s developer surface includes documentation, getting-started guide, authentication, FAQ, support, engineering blog, and 27 more developer resources.'
random_paper: 81
scopes:
- name: Liquid Death Scopes
  scope_count: 4
  slug: liquid-death-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 38.8
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 57.9
    developer_ergonomics: 47.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Liquid Death Authentication
  slug: liquid-death-authentication
  summary_line: none/openIdConnect/oauth2/agentProfile · 4 schemes
- kind: domain-security
  name: Liquid Death Domain Security
  slug: liquid-death-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: liquid-death
tags:
- Company
- Beverages
- Consumer Packaged Goods
- Direct to Consumer
- Ecommerce
- Retail
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- Shopify
website: https://liquiddeath.com/
---

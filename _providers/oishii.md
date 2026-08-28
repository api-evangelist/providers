---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 30.4
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: Anonymous, live Model Context Protocol server for the Oishii storefront, served from oishii.com and provided by the Shopify storefront-renderer platform. A tools/list call returns five tools with full
  name: Oishii Storefront MCP Server
  slug: oishii-storefront-mcp-server
- description: 'Universal Commerce Protocol (UCP) endpoint for agent-driven purchasing from the Oishii store, advertised in the merchant profile at https://oishii.com/.well-known/ucp with supported protocol versions '
  name: Oishii UCP Agentic Commerce Endpoint
  slug: oishii-ucp-agentic-commerce-endpoint
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oishii-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://oishii.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/oishii_stock/
- group: docs
  title: ''
  type: Documentation
  url: https://oishii.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://oishii.com/pages/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://oishii.com/pages/faq
- group: company
  title: ''
  type: Blog
  url: https://oishii.com/blogs/news
- group: start
  title: ''
  type: SignUp
  url: https://oishii.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://oishii.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://oishii.com/policies/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/oishii-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/oishii-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/oishii-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oishii-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/oishii-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/oishii-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/oishii-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/oishii-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/oishii-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/oishii-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-04'
description: 'Oishii is a US vertical-farming company founded in 2016 and headquartered in Jersey City, New Jersey, that grows pesticide-free Japanese strawberry varieties — the Omakase Berry and Koyo Berry — plus the Rubi Tomato inside robot-assisted, bee-pollinated indoor "Smart Farms" in New Jersey, and sells them direct-to-consumer and through grocery retail across the United States and Canada. Oishii publishes no traditional developer program, but its direct-to-consumer storefront at oishii.com runs on Shopify and therefore exposes a real, anonymous, machine-readable agent-commerce surface: an /agents.md and /llms.txt agent instruction document, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, OAuth 2.0 and OpenID Connect discovery documents, a live storefront MCP server at /api/mcp exposing catalog search, cart, product-detail and policy-lookup tools, and a UCP checkout MCP endpoint at /api/ucp/mcp that is gated behind an agent profile URI.'
image: https://oishii.com/cdn/shop/files/OishiiOGImage_24043e78-29c0-4975-8026-ea0399740ae4.jpg?v=1655908654
layout: provider
mcp_servers:
- description: ''
  name: Oishii MCP Server
  slug: oishii-mcp-server
modified: '2026-08-04'
name: Oishii
nav: Providers
network: true
overview: 'Oishii publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, Vertical Farming, Food and Beverage, and Consumer Products.


  Oishii''s developer surface includes documentation, support, engineering blog, signup flow, authentication, and 16 more developer resources.'
random_paper: 15
scopes:
- name: Oishii Scopes
  scope_count: 4
  slug: oishii-scopes
  summary_line: 4 scopes · authorizationCode/refreshToken/urn:ietf:params:oauth:grant-type:jwt-bearer
score:
  band: emerging
  composite: 24.9
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 24.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oishii/refs/heads/main/screenshots/oishii-2026-08-07T190044.png
security:
- kind: authentication
  name: Oishii Authentication
  slug: oishii-authentication
  summary_line: none/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Oishii Domain Security
  slug: oishii-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: oishii
tags:
- Company
- Agriculture
- Vertical Farming
- Food and Beverage
- Consumer Products
- E-Commerce
- Retail
- Agent Commerce
- Shopify
- MCP
- Universal Commerce Protocol
website: https://oishii.com/
---

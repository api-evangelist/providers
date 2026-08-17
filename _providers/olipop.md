---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Olipop Agentic Access
  operation_count: 13
  slug: olipop-agentic-access
  summary_line: 13 operations · 8 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: Agent-facing commerce surface for the OLIPOP storefront, implementing the Universal Commerce Protocol (UCP) shopping service over MCP JSON-RPC. The merchant profile at /.well-known/ucp declares protoc
  name: OLIPOP Agent Commerce API (UCP over MCP)
  slug: olipop-agent-commerce-api-ucp-over-mcp
- description: Shopify Storefront GraphQL API served on the OLIPOP domain, exposing 35 root query fields and 41 mutations across products, collections, search, blogs, pages, menus, metaobjects, localization, cart an
  name: OLIPOP Storefront GraphQL API
  slug: olipop-storefront-graphql-api
- description: Unauthenticated read-only JSON endpoints the store's own agent instructions publish for agents that only need to read catalog data - all products, a single product by handle, and the products in a col
  name: OLIPOP Storefront Product JSON
  slug: olipop-storefront-product-json
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://drinkolipop.com/
- group: docs
  title: ''
  type: Documentation
  url: https://drinkolipop.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://drinkolipop.com/pages/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://drinkolipop.com/pages/faq
- group: company
  title: ''
  type: Blog
  url: https://drinkolipop.com/blogs/digest
- group: start
  title: ''
  type: SignUp
  url: https://drinkolipop.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://drinkolipop.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://drinkolipop.com/policies/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/olipop-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/olipop-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/olipop-tool-crosswalk.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/olipop-storefront.graphql
- group: agent
  title: ''
  type: WellKnown
  url: well-known/olipop-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/olipop-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/olipop-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/olipop-openid-configuration.json
- group: design
  title: ''
  type: Conventions
  url: conventions/olipop-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/olipop-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/olipop-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/olipop-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/olipop-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/olipop-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/olipop-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/olipop-domain-security.yml
created: '2026-07-31'
description: 'OLIPOP PBC is an Oakland, California prebiotic soda maker founded in 2018 by Ben Goodwin and David Lester, built around its trademarked OLISMART blend of plant fibers, prebiotics and botanicals, sold across tens of thousands of US retail locations and direct to consumers at drinkolipop.com. It has no traditional developer program, but its Shopify-hosted storefront is a genuinely agent-native commerce surface: the domain publishes a first-party llms.txt and agents.md describing how AI agents may interact with the store, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, a live UCP/MCP JSON-RPC endpoint at /api/ucp/mcp for catalog search, cart, checkout and order tools, an anonymously introspectable Shopify Storefront GraphQL API, unauthenticated product/collection JSON endpoints, and OpenID Connect discovery for customer accounts. Checkout is explicitly gated on contemporaneous human buyer approval.'
image: https://cdn.shopify.com/s/files/1/0034/6610/0806/files/Website_-_Social_-_Share_-_V1.png?v=1639521624
layout: provider
mcp_servers:
- description: ''
  name: olipop-mcp.yml
  slug: olipop-mcpyml
modified: '2026-07-31'
name: Olipop
nav: Providers
network: true
overview: 'Olipop publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include beverage, consumer-packaged-goods, direct-to-consumer, ecommerce, and retail.


  Olipop''s developer surface includes documentation, support, engineering blog, signup flow, authentication, and 20 more developer resources.'
random_paper: 63
scopes:
- name: Olipop Scopes
  scope_count: 4
  slug: olipop-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 35.8
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 48.1
    developer_ergonomics: 36.4
    discoverability: 81.5
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 35.8
  provenance:
    agentic_access: first-party
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/olipop/refs/heads/main/screenshots/olipop-2026-08-07T190120.png
security:
- kind: authentication
  name: Olipop Authentication
  slug: olipop-authentication
  summary_line: none/apiKey/oauth2/openIdConnect/agent-profile · 5 schemes
- kind: domain-security
  name: Olipop Domain Security
  slug: olipop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: olipop
tags:
- beverage
- consumer-packaged-goods
- direct-to-consumer
- ecommerce
- retail
- agent-commerce
- universal-commerce-protocol
- mcp
- graphql
- shopify
- prebiotic-soda
- functional-beverage
website: https://drinkolipop.com/
---

---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.5
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: Therabody's agent-facing commerce server, implementing the Universal Commerce Protocol (UCP) shopping service over MCP on the Therabody storefront host. Anonymous tools/list returns 13 tools with full
  name: Therabody UCP Commerce MCP
  slug: therabody-ucp-commerce-mcp
- description: The Shopify Storefront GraphQL API served from the Therabody US storefront host. Anonymous introspection is open and returns 416 types across 35 query root fields covering products, collections, carts
  name: Therabody Storefront GraphQL API
  slug: therabody-storefront-graphql
- description: 'Therabody''s customer-account MCP server on account.therabody.com, exposing four post-purchase tools: most-recent order status, order status by order number, store credit balances, and return requests.'
  name: Therabody Customer Account MCP
  slug: therabody-customer-account-mcp
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.therabody.com/
- group: company
  title: ''
  type: Blog
  url: https://www.therabody.com/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://www.therabody.com/pages/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.therabody.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.therabody.com/policies/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://account.therabody.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/therabody-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/therabody-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/therabody-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/therabody-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/therabody-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/therabody-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/therabody-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/therabody-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/therabody-domain-security.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/therabody-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/therabody-decline-codes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/therabody-mcp.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/therabody-storefront.graphql
created: '2026-08-05'
description: 'Therabody is a Los Angeles-based wellness technology company founded in 2016 by Dr. Jason Wersland, best known for inventing the Theragun percussive therapy device. Its product ecosystem spans percussive therapy (Theragun), pneumatic compression (RecoveryAir), electrical stimulation (PowerDot), vibration therapy (Wave) and the Therabody companion app. Therabody publishes no traditional developer program, but its direct-to-consumer storefront at therabody.com runs on Shopify and exposes a substantial machine-readable commerce surface: an open Storefront GraphQL API, a Universal Commerce Protocol (UCP) MCP server for agent-driven catalog search, cart and checkout, a customer-account MCP server for order status and returns, OAuth 2.0 / OpenID Connect discovery, and published agent instructions at /llms.txt and /agents.md.'
image: https://www.therabody.com/cdn/shop/files/theragun-social-media.jpg?v=1742212493
layout: provider
mcp_servers:
- description: ''
  name: therabody-mcp.yml
  slug: therabody-mcpyml
modified: '2026-08-05'
name: Therabody
nav: Providers
network: true
overview: 'Therabody publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wellness, Health, Consumer Products, and E-Commerce.


  Therabody''s developer surface includes engineering blog, support, signup flow, authentication, and 16 more developer resources.'
random_paper: 17
scopes:
- name: Therabody Scopes
  scope_count: 4
  slug: therabody-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 35.6
  delta: -0.2
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 38.9
    developer_ergonomics: 20.8
    discoverability: 92.6
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 35.8
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Therabody Authentication
  slug: therabody-authentication
  summary_line: oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Therabody Domain Security
  slug: therabody-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: therabody
tags:
- Company
- Wellness
- Health
- Consumer Products
- E-Commerce
- Retail
- Shopify
- Agentic Commerce
- Model Context Protocol
- GraphQL
- Universal Commerce Protocol
website: https://www.therabody.com/
---

---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: true
    agentic_commerce: platform
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: 100 Thieves Agentic Access
  operation_count: 13
  slug: 100-thieves-agentic-access
  summary_line: 13 operations · 7 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: An anonymous Model Context Protocol endpoint implementing the Universal Commerce Protocol (UCP) shopping service for the 100 Thieves online store. Exposes thirteen tools covering catalog search and lo
  name: 100 Thieves UCP Commerce MCP API
  slug: 100-thieves-ucp-commerce-mcp
- description: The Shopify Storefront GraphQL API as deployed on the 100 Thieves domain, version 2024-04. Schema introspection is open to anonymous callers and returns 414 types, 35 query root fields and 41 mutation
  name: 100 Thieves Storefront GraphQL API
  slug: 100-thieves-storefront-graphql
- description: The read-only JSON surface the store documents for agents that only need to browse catalog data without transacting - product JSON by handle, collection product listings, and product search. No authen
  name: 100 Thieves Storefront JSON Endpoints
  slug: 100-thieves-storefront-json
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/100-thieves-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://100thieves.com/
- group: docs
  title: ''
  type: Documentation
  url: https://100thieves.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/100-thieves-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/100-thieves-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/100-thieves-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/100-thieves-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/100-thieves-openid-configuration.json
- group: design
  title: ''
  type: Conventions
  url: conventions/100-thieves-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/100-thieves-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/100-thieves-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/100-thieves-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/100-thieves-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/100-thieves-agentic-access.yml
- group: company
  title: ''
  type: Blog
  url: https://100thieves.com/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://100thieves.com/pages/contact
- group: start
  title: ''
  type: SignUp
  url: https://100thieves.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://100thieves.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://100thieves.com/policies/privacy-policy
created: '2026-08-05'
description: '100 Thieves is an American lifestyle brand and gaming organization founded in 2017 by Call of Duty World Champion Matthew "Nadeshot" Haag, headquartered in Los Angeles, California. The company operates championship esports franchises in League of Legends, VALORANT and Call of Duty, a roster of content creators, and a premium streetwear apparel line sold through its own direct-to-consumer online store. Its public machine-readable surface is that storefront: a Shopify-hosted commerce platform that publishes agent-facing instructions at /agents.md and /llms.txt, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, an anonymous Model Context Protocol endpoint exposing thirteen catalog, cart, checkout and order tools, and a Storefront GraphQL API whose schema is openly introspectable. 100 Thieves publishes no developer portal, API reference, or SDKs of its own.'
image: https://100thieves.com/cdn/shop/files/100-Thieves-arcade.jpg?v=1710263463
layout: provider
mcp_servers:
- description: ''
  name: 100 Thieves MCP Server
  slug: 100-thieves-mcp-server
modified: '2026-08-05'
name: 100 Thieves
nav: Providers
network: true
overview: '100 Thieves publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Esports, Gaming, Apparel, and Retail.


  100 Thieves'' developer surface includes documentation, authentication, engineering blog, support, signup flow, and 15 more developer resources.'
random_paper: 5
scopes:
- name: 100 Thieves Scopes
  scope_count: 4
  slug: 100-thieves-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 33.6
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 41.5
    developer_ergonomics: 30.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 33.6
  provenance:
    agentic_access: first-party
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/100-thieves/refs/heads/main/screenshots/100-thieves-2026-08-07T160646.png
security:
- kind: authentication
  name: 100 Thieves Authentication
  slug: 100-thieves-authentication
  summary_line: none/oauth2/openIdConnect · 6 schemes
- kind: domain-security
  name: 100 Thieves Domain Security
  slug: 100-thieves-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 100-thieves
tags:
- Company
- Esports
- Gaming
- Apparel
- Retail
- E-Commerce
- Entertainment
- Media
- Direct to Consumer
- Agentic Commerce
website: https://100thieves.com/
---

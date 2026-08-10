---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: Cerebelly's Universal Commerce Protocol (UCP) MCP endpoint, served anonymously from the storefront host. A tools/list call returns 13 tools with full JSON Schema draft 2020-12 input schemas covering c
  name: Cerebelly UCP Commerce MCP
  slug: cerebelly-ucp-commerce-mcp
- description: 'The Shopify Storefront GraphQL API as served from cerebelly.com. Answers unauthenticated introspection: 416 types, 35 root queries and 41 mutations covering products, collections, blog articles, pages'
  name: Cerebelly Storefront GraphQL API
  slug: cerebelly-storefront-graphql
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cerebelly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cerebelly.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cerebelly.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cerebelly-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cerebelly-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cerebelly-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cerebelly-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cerebelly-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/cerebelly-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cerebelly-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cerebelly-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cerebelly-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cerebelly-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Blog
  url: https://cerebelly.com/blogs/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://cerebelly.com/blogs/news.atom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cerebelly
- group: operate
  title: ''
  type: Support
  url: https://cerebelly.com/pages/contact
- group: start
  title: ''
  type: SignUp
  url: https://cerebelly.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cerebelly.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cerebelly.com/policies/privacy-policy
- group: other
  title: ''
  type: RefundPolicy
  url: https://cerebelly.com/policies/refund-policy
- group: other
  title: ''
  type: ShippingPolicy
  url: https://cerebelly.com/policies/shipping-policy
- group: other
  title: ''
  type: WhereToBuy
  url: https://cerebelly.com/pages/where-to-buy
created: '2026-08-09'
description: 'Cerebelly is an organic baby and toddler food company founded by a practicing neurosurgeon with a PhD in developmental neurobiology from Stanford, making veggie-first purees, bone-broth protein purees, dairy-free smoothie pouches, Smart Bars and Clever Bars formulated around 16 brain-supporting nutrients. Its direct-to-consumer storefront at cerebelly.com runs on Shopify, and that storefront is its API surface: an anonymous Universal Commerce Protocol (UCP) MCP endpoint exposing 13 catalog, cart and checkout tools, a public Shopify Storefront GraphQL API answering unauthenticated introspection, an OpenID Connect customer-account authorization server, and a published llms.txt / agents.md pair that tells AI shopping agents how to transact. Cerebelly ships no developer program of its own — every machine-readable surface here is the Shopify commerce platform as deployed on Cerebelly''s own hosts.'
image: https://cdn.shopify.com/s/files/1/0745/9091/2725/files/Cerebelly_Pantry_01_6a49ec81-265a-437a-ba3d-b5b94590be47.png?v=1759935945
json_schemas:
- name: Cerebelly UCP Commerce MCP — tool input schemas
  property_count: 0
  slug: cerebelly-ucp-tool-schemas
layout: provider
mcp_servers:
- description: ''
  name: cerebelly-mcp.yml
  slug: cerebelly-mcpyml
modified: '2026-08-09'
name: Cerebelly
nav: Providers
network: true
overview: 'Cerebelly publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Baby Food, Consumer Packaged Goods, Food and Beverage, and eCommerce.


  Cerebelly''s developer surface includes documentation, authentication, engineering blog, support, signup flow, and 19 more developer resources.'
random_paper: 23
scopes:
- name: Cerebelly Scopes
  scope_count: 0
  slug: cerebelly-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.1
  facets:
    commercial_clarity: 34.2
    contract_quality: 55.6
    developer_ergonomics: 32.6
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 5.3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
security:
- kind: authentication
  name: Cerebelly Authentication
  slug: cerebelly-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Cerebelly Domain Security
  slug: cerebelly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cerebelly
tags:
- Company
- Baby Food
- Consumer Packaged Goods
- Food and Beverage
- eCommerce
- Retail
- Direct to Consumer
- Shopify
- Agentic Commerce
- Universal Commerce Protocol
- Nutrition
website: https://cerebelly.com/
---

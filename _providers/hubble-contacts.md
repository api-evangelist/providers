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
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.8
  scored_at: '2026-08-17'
api_count: 3
apis:
- description: 'Agent-facing commerce surface for the Hubble Contacts online store, implementing the Universal Commerce Protocol (UCP) over MCP/JSON-RPC. Hubble''s own /agents.md documents the flow: discover capabilit'
  name: Hubble Contacts UCP Commerce (MCP)
  slug: hubble-contacts-ucp-commerce
- description: 'Unauthenticated read-only JSON over the Hubble Contacts storefront catalog, documented in Hubble''s own /agents.md for agents that only need to read store data without transacting: /products.json for t'
  name: Hubble Contacts Storefront Product JSON
  slug: hubble-contacts-storefront-json
- description: 'The Shopify Storefront GraphQL API as served on Hubble Contacts'' own host at /api/{version}/graphql.json. It answers unauthenticated: full introspection and real data queries both return 200 with no s'
  name: Hubble Contacts Storefront GraphQL API
  slug: hubble-contacts-storefront-graphql
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hubble-contacts-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hubblecontacts.com/
- group: start
  title: ''
  type: SignUp
  url: https://account.hubblecontacts.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hubblecontacts.com/contact-lenses/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tos.hubblecontacts.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.hubblecontacts.com/
- group: operate
  title: ''
  type: Support
  url: https://www.hubblecontacts.com/contact-us/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.hubblecontacts.com/faq/
- group: company
  title: ''
  type: Blog
  url: https://www.hubblecontacts.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hubblecontacts
- group: other
  title: ''
  type: Accessibility
  url: https://www.hubblecontacts.com/accessibility-statement/
- group: docs
  title: ''
  type: Documentation
  url: https://account.hubblecontacts.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hubble-contacts-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hubble-contacts-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hubble-contacts-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/hubble-contacts-tool-crosswalk.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hubble-contacts-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hubble-contacts-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hubble-contacts-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hubble-contacts-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hubble-contacts-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hubble-contacts-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hubble-contacts-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/hubble-contacts-storefront.graphql
- group: build
  title: ''
  type: Postman
  url: collections/hubble-contacts-doctor-ecp.postman_collection.json
- group: build
  title: ''
  type: PostmanCollection
  url: collections/hubble-contacts-collections.yml
created: '2026-08-04'
description: 'Hubble Contacts is a New York-based direct-to-consumer vision care brand that sells prescription contact lenses, eyeglasses, sunglasses and eye care accessories on a personalized subscription model, shipping daily, weekly and monthly lenses — its own Classic, Hydro and SkyHy lines alongside third-party brands such as Acuvue, Bausch + Lomb, Biotrue and DAILIES — direct to customers at prices it advertises as up to 30% below comparable retail. Its public machine-readable surface is not a developer API but an agent-commerce one: the storefront at account.hubblecontacts.com publishes /llms.txt and /agents.md, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, an MCP endpoint at /api/ucp/mcp for agent-driven catalog search, cart, checkout and order flows, OAuth 2.0 / OpenID Connect customer account discovery documents, and unauthenticated read-only product and collection JSON endpoints. Undocumented but wide open beside them sits the full Shopify Storefront
  GraphQL API on the same host — 416 types, anonymous, introspectable, and the only place the company''s subscription selling plans are modelled.'
image: https://hubblecontacts.com/static/Hubble-Contacts-Homepage-Inset-Image-mobile.webp
layout: provider
mcp_servers:
- description: ''
  name: hubble-contacts-mcp.yml
  slug: hubble-contacts-mcpyml
modified: '2026-08-04'
name: Hubble Contacts
nav: Providers
network: true
overview: 'Hubble Contacts publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Health, and Vision Care.


  Hubble Contacts'' developer surface includes signup flow, pricing, support, engineering blog, documentation, authentication, and 21 more developer resources.'
random_paper: 44
scopes:
- name: Hubble Contacts Scopes
  scope_count: 4
  slug: hubble-contacts-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 41.3
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 43.2
    developer_ergonomics: 40.8
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 41.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hubble-contacts/refs/heads/main/screenshots/hubble-contacts-2026-08-07T170351.png
security:
- kind: authentication
  name: Hubble Contacts Authentication
  slug: hubble-contacts-authentication
  summary_line: oauth2/openIdConnect/http/none · 2 schemes
- kind: domain-security
  name: Hubble Contacts Domain Security
  slug: hubble-contacts-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hubble-contacts
tags:
- Company
- E-Commerce
- Retail
- Health
- Vision Care
- Contact Lenses
- Subscriptions
- Agentic Commerce
- Model Context Protocol
- Shopify
- GraphQL
website: https://www.hubblecontacts.com/
---

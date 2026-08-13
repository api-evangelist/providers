---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 25.0
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: Anonymous, publicly callable MCP server on binske's direct-to-consumer storefront host implementing the Universal Commerce Protocol shopping service. A live JSON-RPC 2.0 tools/list returned 13 tools w
  name: binske Storefront Commerce API (UCP / MCP)
  slug: binske-storefront-commerce-api-ucp-mcp
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/binske-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://binske.com/
- group: docs
  title: ''
  type: Documentation
  url: https://shopbinske.com/agents.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/binske-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/binske-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/binske-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/binske-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/binske-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/binske-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/binske-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/binske-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/binske-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/binske-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Blog
  url: https://binske.com/explore/
- group: company
  title: ''
  type: BlogRSS
  url: https://binske.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://binske.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://binske.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://binske.com/privacy-policy/
- group: other
  title: ''
  type: Store
  url: https://shopbinske.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/binske_stock/
created: '2026-08-07'
description: binske is a Colorado-born premium cannabis brand founded in 2015, producing flower and pre-rolls, live resin and live hash rosin concentrates, vape carts and all-in-ones, and edibles including chocolate bars and fruit gummies, sold through licensed dispensaries as a multi-state brand across Colorado, Florida, Michigan, New Jersey, New York and Washington. The company develops proprietary genetics with ONI Seed Co. and built its chocolate line around rare white cacao sourced in Peru, with packaging art by UK artist Martin O'Neill. binske operates no developer program and publishes no API of its own; its only machine-callable surface is the Shopify-native Universal Commerce Protocol MCP endpoint served from its direct-to-consumer storefront at shopbinske.com, which exposes catalog search, cart and checkout to agents and requires explicit human approval before payment.
image: https://binske.com/wp-content/uploads/2026/01/favicon-300x300.png
layout: provider
mcp_servers:
- description: ''
  name: binske-mcp.yml
  slug: binske-mcpyml
- description: ''
  name: binske-mcp-tools.json
  slug: binske-mcp-toolsjson
modified: '2026-08-07'
name: Binske
nav: Providers
network: true
overview: 'Binske publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include cannabis, consumer-packaged-goods, direct-to-consumer, ecommerce, and retail.


  Binske''s developer surface includes documentation, authentication, engineering blog, support, and 17 more developer resources.'
random_paper: 36
scopes:
- name: Binske Scopes
  scope_count: 0
  slug: binske-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.7
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 36.4
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 21.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/binske/refs/heads/main/screenshots/binske-2026-08-07T162438.png
security:
- kind: authentication
  name: Binske Authentication
  slug: binske-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Binske Domain Security
  slug: binske-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: binske
tags:
- cannabis
- consumer-packaged-goods
- direct-to-consumer
- ecommerce
- retail
- shopify
- agent-commerce
- ucp
- mcp
- storefront
website: https://binske.com/
---

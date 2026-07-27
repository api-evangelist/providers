---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 60.6
  scored_at: '2026-07-27'
api_count: 5
apis:
- description: Obtain and test API keys
  name: ShopGo Authentication API
  slug: shopgo-authentication-api
- description: Order, payment and shipment management
  name: ShopGo Orders API
  slug: shopgo-orders-api
- description: Store availability, legal and webhook settings
  name: ShopGo Store API
  slug: shopgo-store-api
- description: The Tenants API from ShopGo — 2 operation(s) for tenants.
  name: ShopGo Tenants API
  slug: shopgo-tenants-api
- description: Dashboard user and tenant information
  name: ShopGo Users API
  slug: shopgo-users-api
artifact_total: 9
asyncapis:
- description: ''
  name: Shopgo Webhooks
  slug: shopgo-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://shopgo.me
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.shopgo.me
- group: docs
  title: ''
  type: Documentation
  url: https://docs.shopgo.me
- group: docs
  title: ''
  type: APIReference
  url: https://docs.shopgo.me/management-api/orders
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shopgo
- group: auth
  title: ''
  type: Authentication
  url: authentication/shopgo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shopgo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/shopgo-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/shopgo-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/shopgo-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shopgo-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/shopgo-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/shopgo-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shopgo-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/shopgo-well-known.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/shopgo-management-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shopgo-domain-security.yml
created: '2026-07-17'
description: 'ShopGo (now branded Makane) is a MENA-focused eCommerce SaaS platform based in Amman, Jordan and founded in 2012, backed by 500 Global. It lets merchants build and run online stores with integrated payment and shipment options across the Middle East and North Africa. For developers, ShopGo publishes a GitBook developer portal (docs.shopgo.me) documenting two REST APIs served from api.shopgo.me: a Management API for store, order, payment and shipment administration, and an internal Platform API for SaaS tenant control. Both use API-key authentication and a JSON result/payload envelope, and the platform supports configurable checkout webhooks (custom shipping rates, order confirmation).'
image: https://github.com/shopgo.png
layout: provider
mcp_servers:
- description: ''
  name: shopgo-mcp.yml
  slug: shopgo-mcpyml
modified: '2026-07-21'
name: ShopGo
nav: Providers
network: true
overview: 'ShopGo publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Orders API, Store API, and 2 more. Tagged areas include Company, eCommerce, Online Stores, Payments, and Shipping.


  The ShopGo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ShopGo''s developer surface includes documentation, API reference, authentication, and 15 more developer resources.'
random_paper: 44
score:
  band: thin
  composite: 38.1
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 66.5
    developer_ergonomics: 50.0
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 38.1
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Shopgo Authentication
  slug: shopgo-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Shopgo Domain Security
  slug: shopgo-domain-security
  summary_line: TLSv1.3
slug: shopgo
tags:
- Company
- eCommerce
- Online Stores
- Payments
- Shipping
- SaaS
- MENA
- Orders
website: https://shopgo.me
---

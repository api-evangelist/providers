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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-08-12'
api_count: 7
apis:
- description: Once you followed above steps from [Getting started](#section/Getting-Started) and that you have your signed JWT token, you can request the access token.
  name: Delivery Hero Authentication API
  slug: delivery-hero-authentication-api
- description: '**▶️ READ THIS FIRST ◀️** * Those are NOT actual endpoints. They are callback from ODR to your endpoint * This is used to represent the payload ODR will sent * This is an optional feature and it requi'
  name: Delivery Hero Callback API
  slug: delivery-hero-callback-api
- description: The OrdersEstimation API from Delivery Hero — 2 operation(s) for ordersestimation.
  name: Delivery Hero OrdersEstimation API
  slug: delivery-hero-ordersestimation-api
- description: The following sections provide a complete summary of all available endpoints and features connected with the Orders API. Please review the documentation carefully. When selecting an endpoint, note the
  name: Delivery Hero OrdersManagement API
  slug: delivery-hero-ordersmanagement-api
- description: The Outlets API from Delivery Hero — 2 operation(s) for outlets.
  name: Delivery Hero Outlets API
  slug: delivery-hero-outlets-api
- description: The Proofs API from Delivery Hero — 3 operation(s) for proofs.
  name: Delivery Hero Proofs API
  slug: delivery-hero-proofs-api
- description: The RiderPosition API from Delivery Hero — 1 operation(s) for riderposition.
  name: Delivery Hero RiderPosition API
  slug: delivery-hero-riderposition-api
artifact_total: 12
asyncapis:
- description: ''
  name: Delivery Hero On Demand Rider Webhooks
  slug: delivery-hero-on-demand-rider-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/delivery-hero-on-demand-rider-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://deliveryhero.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.deliveryhero.com/
- group: docs
  title: ''
  type: Documentation
  url: https://on-demand-rider-docs.deliveryhero.io/
- group: docs
  title: ''
  type: APIReference
  url: https://on-demand-rider-docs.deliveryhero.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://on-demand-rider-docs.deliveryhero.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deliveryhero
- group: company
  title: ''
  type: Blog
  url: https://www.deliveryhero.com/newsroom/
- group: operate
  title: ''
  type: Support
  url: https://developers.deliveryhero.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/delivery-hero-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/delivery-hero-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/delivery-hero-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/delivery-hero-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/delivery-hero-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/delivery-hero-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/delivery-hero-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/delivery-hero-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/delivery-hero-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/delivery-hero-on-demand-rider-webhooks.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/delivery-hero-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/delivery-hero-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/delivery-hero-create-and-track-order.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/delivery-hero-cancel-and-proof.md
created: '2026-07-17'
description: Delivery Hero SE is a Berlin-based multinational online food-delivery and quick-commerce company operating in 70+ markets through local brands including foodpanda, Talabat, Glovo, PedidosYa, Yemeksepeti, Hungerstation and Pandamart. Its public developer surface exposes logistics and partner-integration APIs. The flagship On Demand Rider (ODR) API lets merchants request on-demand courier delivery across brands such as Glovo and pandago — registering outlets, estimating delivery fees and times, creating and tracking orders, retrieving proof of pickup/delivery/return, and receiving order-status, courier-location and refund webhooks. Additional Q-Commerce and Restaurant (POS) integration APIs handle order transmission and grocery assortment/promotion sync for restaurant and quick-commerce partners.
image: images/delivery-hero-on-demand-rider-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: delivery-hero-mcp.yml
  slug: delivery-hero-mcpyml
modified: '2026-07-18'
name: Delivery Hero
nav: Providers
network: true
overview: 'Delivery Hero publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Callback API, OrdersEstimation API, and 4 more. Tagged areas include Company, Technology, Food Delivery, Logistics, and Quick Commerce.


  The Delivery Hero catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Delivery Hero''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 16 more developer resources.'
random_paper: 23
scopes:
- name: Delivery Hero Scopes
  scope_count: 1
  slug: delivery-hero-scopes
  summary_line: 1 scope
score:
  band: thin
  composite: 38.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 59.7
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 13.2
  previous_composite: 38.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/delivery-hero/refs/heads/main/screenshots/delivery-hero-2026-07-25T211652.png
security:
- kind: authentication
  name: Delivery Hero Authentication
  slug: delivery-hero-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Delivery Hero Domain Security
  slug: delivery-hero-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: delivery-hero
tags:
- Company
- Technology
- Food Delivery
- Logistics
- Quick Commerce
- Last Mile Delivery
- On Demand
- Orders
website: https://deliveryhero.com
---

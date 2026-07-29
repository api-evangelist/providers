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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-07-28'
api_count: 20
apis:
- description: The Account API from OTO Global — 4 operation(s) for account.
  name: OTO Global Account API
  slug: oto-global-account-api
- description: 'You need your refresh_token for authorization. You can obtain your token from the UI by following these steps: Go to Settings → API Integrations . Click the Connect button to activate your Refresh Tok'
  name: OTO Global Authorization API
  slug: oto-global-authorization-api
- description: The Brands API from OTO Global — 2 operation(s) for brands.
  name: OTO Global Brands API
  slug: oto-global-brands-api
- description: The Carrier Integrations API from OTO Global — 10 operation(s) for carrier integrations.
  name: OTO Global Carrier Integrations API
  slug: oto-global-carrier-integrations-api
- description: The Customer Notifications API from OTO Global — 1 operation(s) for customer notifications.
  name: OTO Global Customer Notifications API
  slug: oto-global-customer-notifications-api
- description: The Marketplace API from OTO Global — 2 operation(s) for marketplace.
  name: OTO Global Marketplace API
  slug: oto-global-marketplace-api
- description: The National Address API from OTO Global — 1 operation(s) for national address.
  name: OTO Global National Address API
  slug: oto-global-national-address-api
- description: The Orders API from OTO Global — 9 operation(s) for orders.
  name: OTO Global Orders API
  slug: oto-global-orders-api
- description: The OTO FLEX API from OTO Global — 2 operation(s) for oto flex.
  name: OTO Global OTO FLEX API
  slug: oto-global-oto-flex-api
- description: The Pickup Locations API from OTO Global — 3 operation(s) for pickup locations.
  name: OTO Global Pickup Locations API
  slug: oto-global-pickup-locations-api
- description: The Products API from OTO Global — 5 operation(s) for products.
  name: OTO Global Products API
  slug: oto-global-products-api
- description: The Return Shipments API from OTO Global — 4 operation(s) for return shipments.
  name: OTO Global Return Shipments API
  slug: oto-global-return-shipments-api
- description: The Sales Channels API from OTO Global — 3 operation(s) for sales channels.
  name: OTO Global Sales Channels API
  slug: oto-global-sales-channels-api
- description: The Shipments API from OTO Global — 2 operation(s) for shipments.
  name: OTO Global Shipments API
  slug: oto-global-shipments-api
- description: The Shipping Label(AWB) API from OTO Global — 1 operation(s) for shipping label(awb).
  name: OTO Global Shipping Label(AWB) API
  slug: oto-global-shipping-label-awb-api
- description: The Shipping Prices API from OTO Global — 4 operation(s) for shipping prices.
  name: OTO Global Shipping Prices API
  slug: oto-global-shipping-prices-api
- description: The Stock Management API from OTO Global — 8 operation(s) for stock management.
  name: OTO Global Stock Management API
  slug: oto-global-stock-management-api
- description: The Tracking API from OTO Global — 3 operation(s) for tracking.
  name: OTO Global Tracking API
  slug: oto-global-tracking-api
- description: The Transactions API from OTO Global — 3 operation(s) for transactions.
  name: OTO Global Transactions API
  slug: oto-global-transactions-api
- description: 'WEBHOOK for ORDER There are 3 types of webhook for now, newOrders, orderStatus , shipmentError and walletTransaction. OTO will push updates to the registered webhook endpoint for the orderStatus type '
  name: OTO Global Webhook API
  slug: oto-global-webhook-api
artifact_total: 24
asyncapis:
- description: ''
  name: Oto Global Webhooks
  slug: oto-global-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oto-global-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tryoto.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apis.tryoto.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apis.tryoto.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apis.tryoto.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.tryoto.com/api-integration
- group: operate
  title: ''
  type: Support
  url: https://help.tryoto.com/en/support/home
- group: company
  title: ''
  type: Blog
  url: https://www.tryoto.com/otopedia/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tryoto.com/plans-ksa
- group: start
  title: ''
  type: SignUp
  url: https://app.tryoto.com/register/en_US
- group: start
  title: ''
  type: Login
  url: https://app.tryoto.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tryoto.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tryoto.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tryoto.com
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/oto-global-openapi.yml
- group: build
  title: ''
  type: Postman
  url: postman/oto-global-postman.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/oto-global-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/oto-global-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/oto-global-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/oto-global-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/oto-global-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/oto-global-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/oto-global-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/oto-global-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/oto-global-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/oto-global-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/oto-global-openapi-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/oto-global-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: OTO is a multi-carrier shipping and fulfillment platform for e-commerce businesses, headquartered in Saudi Arabia and serving 10,000+ merchants. It connects a single integration to 450+ shipping carriers and provides order management, warehouse and picking/packing automation, real-time tracking with customer notifications, returns management, address validation, and omnichannel order synchronization. The OTO REST API V2 (base https://api.tryoto.com/rest/v2, staging at staging-api.tryoto.com) exposes 74 operations across orders, shipments, returns, tracking, shipping rates, carrier integrations, pickup locations, products, stock management, sales channels, and webhooks. Authentication is a bearer access_token minted from a dashboard refresh_token.
image: https://www.tryoto.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: oto-global-mcp.yml
  slug: oto-global-mcpyml
modified: '2026-07-20'
name: OTO Global
nav: Providers
network: true
overview: 'OTO Global publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Account API, Authorization API, Brands API, and 17 more. Tagged areas include Company, Shipping, Logistics, Fulfillment, and E-commerce.


  The OTO Global catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  OTO Global''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
random_paper: 36
score:
  band: developing
  composite: 53.8
  delta: -1.3
  facets:
    commercial_clarity: 44.7
    contract_quality: 71.0
    developer_ergonomics: 66.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 23.7
  previous_composite: 55.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Oto Global Authentication
  slug: oto-global-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Oto Global Domain Security
  slug: oto-global-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: oto-global
tags:
- Company
- Shipping
- Logistics
- Fulfillment
- E-commerce
- Delivery
- Carriers
- Returns
- Saudi Arabia
website: https://tryoto.com
---

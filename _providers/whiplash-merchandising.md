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
  scored_at: '2026-07-23'
api_count: 21
apis:
- description: Bundle Items are components that make up a bundle, defining the quantity and relationship of items within product bundles.
  name: Whiplash Merchandising bundle_items API
  slug: whiplash-merchandising-bundle-items-api
- description: A ConsumerReturn represents goods coming back from an end consumer. It is a special form of Shipnotice, and is processed in much the same way.
  name: Whiplash Merchandising consumer_returns API
  slug: whiplash-merchandising-consumer-returns-api
- description: Customers are Whiplash clients, not the End Consumer. Most Whiplash resources are owned by a Customer (or belong to resources that are).
  name: Whiplash Merchandising customers API
  slug: whiplash-merchandising-customers-api
- description: Documents are imported files and exported reports. We store a record in your account of every file you import, as well as every report you've run, so they're easy to search and access.
  name: Whiplash Merchandising documents API
  slug: whiplash-merchandising-documents-api
- description: Items are probably the most fundamental entity in the Whiplash system. An item is simply a 'shippable unit'. So, it's not a Whiplash T-Shirt; it's a Small Whiplash T-Shirt, for instance. Most commerce
  name: Whiplash Merchandising items API
  slug: whiplash-merchandising-items-api
- description: The load_scacs API from Whiplash Merchandising — 2 operation(s) for load_scacs.
  name: Whiplash Merchandising load_scacs API
  slug: whiplash-merchandising-load-scacs-api
- description: System event definitions for notifications.
  name: Whiplash Merchandising notification_events API
  slug: whiplash-merchandising-notification-events-api
- description: User notification preferences and subscriptions.
  name: Whiplash Merchandising notification_subscriptions API
  slug: whiplash-merchandising-notification-subscriptions-api
- description: Order-related documentation and paperwork.
  name: Whiplash Merchandising order_documents API
  slug: whiplash-merchandising-order-documents-api
- description: An OrderItem represents an Item with a quantity in an Order.
  name: Whiplash Merchandising order_items API
  slug: whiplash-merchandising-order-items-api
- description: Order picking container management.
  name: Whiplash Merchandising order_totes API
  slug: whiplash-merchandising-order-totes-api
- description: Orders are end consumer requests for Items. An Order is comprised of OrderItems. Orders represent outgoing stock.
  name: Whiplash Merchandising orders API
  slug: whiplash-merchandising-orders-api
- description: Originators are e-commerce, API, or ERP representations of an Item, Order, OrderItem, ConsumerReturn, Shipnotice, or ShipnoticeItem. They contain your system's ID and, optionally, details. You can use
  name: Whiplash Merchandising originators API
  slug: whiplash-merchandising-originators-api
- description: Shipment package details and tracking.
  name: Whiplash Merchandising packages API
  slug: whiplash-merchandising-packages-api
- description: Project management and organization.
  name: Whiplash Merchandising projects API
  slug: whiplash-merchandising-projects-api
- description: Barcode management and processing.
  name: Whiplash Merchandising scancodes API
  slug: whiplash-merchandising-scancodes-api
- description: Similar to an OrderItem, ShipnoticeItem represents an Item with a quantity in a Shipnotice. quantity refers to the quantity expected to arrive, and the quantity actually received is quantity_good.
  name: Whiplash Merchandising shipnotice_items API
  slug: whiplash-merchandising-shipnotice-items-api
- description: A Shipnotice is the opposite of an order, and are notifications by the client of inventory that is expected to arrive at a warehouse. Shipnotices represent incoming stock.
  name: Whiplash Merchandising shipnotices API
  slug: whiplash-merchandising-shipnotices-api
- description: (Sandbox Only) Simulate Order and Ship Notice processing, since these are staff-only operations.
  name: Whiplash Merchandising simulate API
  slug: whiplash-merchandising-simulate-api
- description: Templates allow you to customize packing slips, email confirmations, order inserts, etc.
  name: Whiplash Merchandising templates API
  slug: whiplash-merchandising-templates-api
- description: The wholesale_items API from Whiplash Merchandising — 2 operation(s) for wholesale_items.
  name: Whiplash Merchandising wholesale_items API
  slug: whiplash-merchandising-wholesale-items-api
artifact_total: 25
asyncapis:
- description: ''
  name: Whiplash Merchandising Notifications Webhooks
  slug: whiplash-merchandising-notifications-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/whiplash-merchandising-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://whiplash.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.getwhiplash.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.getwhiplash.com
- group: docs
  title: ''
  type: APIReference
  url: https://developers.getwhiplash.com
- group: operate
  title: ''
  type: Support
  url: https://help.whiplash.com/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getwhiplash.com
- group: start
  title: ''
  type: Login
  url: https://www.getwhiplash.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://whiplash.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ryder.com/en-us/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/whiplashmerch
- group: auth
  title: ''
  type: Authentication
  url: authentication/whiplash-merchandising-authentication.yml
- group: auth
  title: ''
  type: OAuthAuthorizationServer
  url: well-known/whiplash-merchandising-oauth-authorization-server.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/whiplash-merchandising-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/whiplash-merchandising-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/whiplash-merchandising-packages.yml
- group: design
  title: ''
  type: Components
  url: components/whiplash-merchandising-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/whiplash-merchandising-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/whiplash-merchandising-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/whiplash-merchandising-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/whiplash-merchandising-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/whiplash-merchandising-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/whiplash-merchandising-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/whiplash-merchandising-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/whiplash-merchandising-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/whiplash-merchandising-notifications-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Whiplash (now Ryder E-commerce by Whiplash) is an order-fulfillment and third-party logistics (3PL) platform for direct-to-consumer and ecommerce brands. It runs a network of fulfillment centers offering pick-pack-ship, warehousing, inventory management, kitting, omnichannel order routing, and returns processing. The company exposes the Rydership V2 REST API (formerly the Whiplash API) so merchants and platforms can programmatically manage items, orders, order items, shipments (ship notices), consumer returns, customers, documents, and webhook notification subscriptions across the fulfillment lifecycle. Whiplash was founded in 2011, backed by 500 Global, and acquired by Ryder System in 2021.
image: https://wl-s3-assets.s3.amazonaws.com/rydership/RyderShip-horizontal-safe-padding.svg
layout: provider
mcp_servers:
- description: ''
  name: whiplash-merchandising-mcp.yml
  slug: whiplash-merchandising-mcpyml
modified: '2026-07-21'
name: Whiplash Merchandising
nav: Providers
network: true
overview: 'Whiplash Merchandising publishes 21 APIs on the [APIs.io](https://apis.io/) network, including bundle_items API, consumer_returns API, customers API, and 18 more. Tagged areas include Company, Fulfillment, Logistics, Ecommerce, and Shipping.


  The Whiplash Merchandising catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Whiplash Merchandising''s developer surface includes documentation, API reference, support, pricing, authentication, and 22 more developer resources.'
random_paper: 37
score:
  band: developing
  composite: 49.4
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 66.6
    developer_ergonomics: 60.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 49.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Whiplash Merchandising Authentication
  slug: whiplash-merchandising-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Whiplash Merchandising Domain Security
  slug: whiplash-merchandising-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: whiplash-merchandising
tags:
- Company
- Fulfillment
- Logistics
- Ecommerce
- Shipping
- Warehousing
- Inventory
- 3PL
- Order Management
- Returns
- Supply Chain
website: https://whiplash.com
---

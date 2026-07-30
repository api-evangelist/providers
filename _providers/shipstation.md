---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Shipstation Agentic Access
  operation_count: 36
  slug: shipstation-agentic-access
  summary_line: 36 operations · 19 acting
api_count: 11
apis:
- description: The ShipStation V2 API is the next-generation shipping and inventory API built on ShipEngine technology. It provides improved endpoints for creating orders, managing customers, querying order and ship
  name: ShipStation V2 API
  slug: shipstation-v2-api
- description: Manage ShipStation account settings
  name: ShipStation Accounts API
  slug: shipstation-accounts-api
- description: Query carriers and services
  name: ShipStation Carriers API
  slug: shipstation-carriers-api
- description: Manage customer records
  name: ShipStation Customers API
  slug: shipstation-customers-api
- description: Manage third-party fulfillments
  name: ShipStation Fulfillments API
  slug: shipstation-fulfillments-api
- description: Manage customer orders
  name: ShipStation Orders API
  slug: shipstation-orders-api
- description: Manage product records
  name: ShipStation Products API
  slug: shipstation-products-api
- description: Create and manage shipments
  name: ShipStation Shipments API
  slug: shipstation-shipments-api
- description: Manage marketplace store connections
  name: ShipStation Stores API
  slug: shipstation-stores-api
- description: Manage warehouse locations
  name: ShipStation Warehouses API
  slug: shipstation-warehouses-api
- description: Manage webhook subscriptions
  name: ShipStation Webhooks API
  slug: shipstation-webhooks-api
artifact_total: 82
asyncapis:
- description: AsyncAPI description of the ShipStation V1 outbound webhook surface. ShipStation delivers event notifications by issuing HTTP POST requests with a JSON body to a `target_url` that the customer registe
  name: ShipStation Webhooks
  slug: shipstation-webhooks-asyncapi
collections:
- collection_type: postman
  name: ShipStation V1 Accounts API
  slug: postman-shipstation-accounts-api
- collection_type: postman
  name: ShipStation V1 Accounts Carriers API
  slug: postman-shipstation-carriers-api
- collection_type: postman
  name: ShipStation V1 Accounts Customers API
  slug: postman-shipstation-customers-api
- collection_type: postman
  name: ShipStation V1 Accounts Fulfillments API
  slug: postman-shipstation-fulfillments-api
- collection_type: postman
  name: ShipStation V1 Accounts Orders API
  slug: postman-shipstation-orders-api
- collection_type: postman
  name: ShipStation V1 Accounts Products API
  slug: postman-shipstation-products-api
- collection_type: postman
  name: ShipStation V1 Accounts Shipments API
  slug: postman-shipstation-shipments-api
- collection_type: postman
  name: ShipStation V1 Accounts Stores API
  slug: postman-shipstation-stores-api
- collection_type: postman
  name: ShipStation V1 Accounts Warehouses API
  slug: postman-shipstation-warehouses-api
- collection_type: postman
  name: ShipStation V1 Accounts Webhooks API
  slug: postman-shipstation-webhooks-api
- collection_type: open
  name: ShipStation V1 API
  slug: open-shipstation-v1
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/shipstation/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shipstation-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shipstation-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shipstation-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shipstation
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shipstation
- group: docs
  title: ''
  type: Documentation
  url: https://www.shipstation.com/docs/api/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.shipstation.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.shipstation.com/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://www.shipstation.com/docs/api/requirements/
- group: docs
  title: ''
  type: OpenAPI
  url: https://docs.shipstation.com/openapi/downloads
- group: operate
  title: ''
  type: Support
  url: https://help.shipstation.com/hc/en-us/articles/360025856212-ShipStation-API
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shipstation.com/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shipstation.com/legal/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://www.shipstation.com
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.shipstation.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.shipstation.com/feed/
created: '2025-03-01'
description: ShipStation is a leading shipping platform for ecommerce businesses providing APIs to integrate shipping workflows into applications. The ShipStation API enables developers to automate order management, create shipments, generate labels, track packages, manage warehouses, and connect to multiple carriers. ShipStation offers both V1 (ssapi.shipstation.com) and V2 (ShipEngine-powered) API versions.
examples:
- key_count: 4
  name: Shipstation Create Label Example
  slug: shipstation-create-label-example
- key_count: 4
  name: Shipstation Create Order Example
  slug: shipstation-create-order-example
features:
- 'Starter $14.99/mo: 50 shipments, 3 users'
- 'Standard $29.99/mo: 50 shipments, 10 users, API access'
- 'Premium $349.99/mo: advanced inventory + warehouse'
- Unlimited store connections (Shopify, WooCommerce, BigCommerce, Amazon, eBay, Etsy, etc.)
- Automated rate shopping across carriers
- Bring your own carrier accounts
- Return labels and exchanges
- Shipping API v1 and v2
- Default 40 req/min/account
- Webhooks for order/shipment events
- API key + secret auth
- Auto-Routing (Premium)
- Cubiscan integration (Premium)
- Open Database Connectivity (ODBC) on Premium
- Mobile app for label printing
- Owned by Auctane (parent company)
finops:
- name: Shipstation Finops
  service_category: Shipping / Order Management
  slug: shipstation-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the ShipStation multi-carrier shipping platform. ShipStation exposes a REST API (V1 at `ssapi.shipstation.com` and V2 at `docs.shipstation.com`)
  name: ShipStation GraphQL Schema
  slug: shipstation-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shipstation.png
json_schemas:
- name: Address
  property_count: 11
  slug: shipstation-address
- name: Carrier
  property_count: 8
  slug: shipstation-carrier
- name: CarrierService
  property_count: 6
  slug: shipstation-carrierservice
- name: Customer
  property_count: 14
  slug: shipstation-customer
- name: CustomerPaginatedList
  property_count: 4
  slug: shipstation-customerpaginatedlist
- name: Dimensions
  property_count: 4
  slug: shipstation-dimensions
- name: Fulfillment
  property_count: 11
  slug: shipstation-fulfillment
- name: FulfillmentPaginatedList
  property_count: 4
  slug: shipstation-fulfillmentpaginatedlist
- name: Label
  property_count: 11
  slug: shipstation-label
- name: LabelCreateRequest
  property_count: 12
  slug: shipstation-labelcreaterequest
- name: ShipStation Order
  property_count: 27
  slug: shipstation-order
- name: OrderCreateRequest
  property_count: 29
  slug: shipstation-ordercreaterequest
- name: OrderItem
  property_count: 15
  slug: shipstation-orderitem
- name: OrderPaginatedList
  property_count: 4
  slug: shipstation-orderpaginatedlist
- name: Package
  property_count: 5
  slug: shipstation-package
- name: Product
  property_count: 31
  slug: shipstation-product
- name: ProductPaginatedList
  property_count: 4
  slug: shipstation-productpaginatedlist
- name: Rate
  property_count: 4
  slug: shipstation-rate
- name: RateRequest
  property_count: 12
  slug: shipstation-raterequest
- name: ShipStation Shipment
  property_count: 22
  slug: shipstation-shipment
- name: ShipmentPaginatedList
  property_count: 4
  slug: shipstation-shipmentpaginatedlist
- name: Store
  property_count: 14
  slug: shipstation-store
- name: Tag
  property_count: 3
  slug: shipstation-tag
- name: Warehouse
  property_count: 6
  slug: shipstation-warehouse
- name: WarehouseCreateRequest
  property_count: 4
  slug: shipstation-warehousecreaterequest
- name: Webhook
  property_count: 14
  slug: shipstation-webhook
- name: WebhookCreateRequest
  property_count: 4
  slug: shipstation-webhookcreaterequest
- name: Weight
  property_count: 3
  slug: shipstation-weight
json_structures:
- name: Shipstation Order Structure
  property_count: 0
  slug: shipstation-order-structure
- name: Shipstation Structure
  property_count: 0
  slug: shipstation-structure
jsonld:
- class_count: 43
  name: Shipstation Context
  property_count: 20
  slug: shipstation-context
layout: provider
modified: '2026-05-30'
name: ShipStation
nav: Providers
network: true
overview: 'ShipStation publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Carriers API, Customers API, and 7 more. Tagged areas include Ecommerce, Labels, Logistics, Order Management, and Shipping.


  The ShipStation catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  ShipStation''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, and 11 more developer resources.'
plans:
- name: Shipstation Plans Pricing
  plan_count: 3
  slug: shipstation-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 2
  name: Shipstation Rate Limits
  slug: shipstation-rate-limits
rules:
- name: ShipStation API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: shipstation-asyncapi-spectral-rules
- name: ShipStation API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: shipstation-jsonschema-spectral-rules
- name: ShipStation API Rules
  rule_count: 13
  severity_counts:
    error: 5
    hint: 0
    info: 3
    warn: 5
  slug: shipstation-rules
score:
  band: strong
  composite: 58.6
  delta: -2.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 88.3
    developer_ergonomics: 47.8
    discoverability: 64.8
    governance: 41.7
    operational_transparency: 26.3
  previous_composite: 60.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shipstation/refs/heads/main/screenshots/shipstation-2026-06-20T193826.png
security:
- kind: authentication
  name: Shipstation Authentication
  slug: shipstation-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Shipstation Domain Security
  slug: shipstation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shipstation
tags:
- Ecommerce
- Labels
- Logistics
- Order Management
- Shipping
- Warehousing
website: https://www.shipstation.com
---

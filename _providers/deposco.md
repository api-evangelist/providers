---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: Import and query customer (sales) orders for fulfillment. Modeled from Deposco integration references - PUT /import/{businessUnit}/customerOrder/{orderNumber} to create or update an order, and GET /se
  name: Deposco Customer Orders API
  slug: deposco-customer-orders-api
- description: Create and search purchase orders for inbound inventory. Modeled from Deposco integration references - PUT /orders/Purchase Order/{orderNumber}, POST /orders, and GET /search/Order?otherReferenceNumbe
  name: Deposco Purchase Orders API
  slug: deposco-purchase-orders-api
- description: Create and update item (SKU) master data. Modeled from Deposco integration references - PUT /items/{itemNumber} for a single item and POST /items for bulk item imports. Endpoints are modeled from publ
  name: Deposco Items API
  slug: deposco-items-api
- description: Retrieve real-time inventory by facility and location. Modeled from Deposco integration references - GET /inventory/facility/{facilityNumber}/location/{locationNumber} and GET /inventory/{businessUnit
  name: Deposco Inventory API
  slug: deposco-inventory-api
- description: Search outbound shipments produced by fulfillment. Modeled from Deposco integration references - GET /search/shipment?orderHeaders.customerOrderNumber={orderNumber} to retrieve shipment and tracking d
  name: Deposco Shipments API
  slug: deposco-shipments-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deposco-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deposco
- group: company
  title: ''
  type: Website
  url: https://deposco.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.deposco.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/deposco-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.deposco.com/
created: '2026-07-04'
description: Deposco is a cloud supply chain execution platform combining order management (OMS) and warehouse management (WMS) for retailers, brands, 3PLs, and DTC ecommerce sellers. Its Bright Suite gives real-time visibility into inventory, orders, and shipments across the fulfillment lifecycle - receiving, putaway, picking, packing, and shipping. Deposco integrates through a REST API exposed on its Developer Portal (developer.deposco.com) using resource paths under /integration/{code}/, secured with OAuth 2.0 / per-merchant API credentials and scoped by tenant code and business unit. API access is provisioned per customer through a Deposco account manager rather than through open self-service signup, and Deposco also ships 150+ pre-built connectors and EDI integrations.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deposco.png
layout: provider
modified: '2026-07-04'
name: Deposco
nav: Providers
network: true
overview: 'Deposco publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Supply Chain, Warehouse Management, WMS, Order Management, and OMS.


  Deposco''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Deposco Plans Pricing
  plan_count: 1
  slug: deposco-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 13.8
  delta: -2.6
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/deposco/refs/heads/main/screenshots/deposco-2026-07-25T211736.png
security:
- kind: domain-security
  name: Deposco Domain Security
  slug: deposco-domain-security
  summary_line: TLSv1.2 · DMARC
slug: deposco
tags:
- Supply Chain
- Warehouse Management
- WMS
- Order Management
- OMS
- Fulfillment
- Inventory
- Logistics
- Ecommerce
- 3PL
website: https://deposco.com/
---

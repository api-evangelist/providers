---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-12'
api_count: 9
apis:
- description: Create new orders and update, cancel, or get information about existing outbound B2C orders. Includes shipment details such as shipping box dimensions, contents, and tracking information.
  name: Shipwire Order API
  slug: shipwire-order-api
- description: Track inventory levels and stock across Shipwire fulfillment centers in real time.
  name: Shipwire Stock API
  slug: shipwire-stock-api
- description: Manage inbound inventory arrivals and create Advanced Shipping Notices (ASNs) to suppliers to streamline warehouse receiving operations.
  name: Shipwire Receiving API
  slug: shipwire-receiving-api
- description: Generate return labels, postage, and return tracking information by notifying the Shipwire Platform when an order is being returned by a customer.
  name: Shipwire Returns API
  slug: shipwire-returns-api
- description: Compare real-time shipping quotes across carriers and service levels, or by warehouse, to select the optimal carrier for each shipment.
  name: Shipwire Rate API
  slug: shipwire-rate-api
- description: Manage product catalogs, marketing inserts, and product kits within the Shipwire fulfillment platform.
  name: Shipwire Product API
  slug: shipwire-product-api
- description: Create, edit, and cancel purchase orders in the Shipwire system for B2B fulfillment workflows. POs can be approved to generate fulfillment orders.
  name: Shipwire Purchase Order API
  slug: shipwire-purchase-order-api
- description: Subscribe to real-time push notifications for various fulfillment events to trigger workflows in external systems when order, shipment, or inventory events occur.
  name: Shipwire Webhooks API
  slug: shipwire-webhooks-api
- description: Validate shipping addresses before submitting orders to reduce failed deliveries and improve fulfillment accuracy.
  name: Shipwire Address Validation API
  slug: shipwire-address-validation-api
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shipwire-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.shipwire.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.shipwire.com/developers/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.shipwire.com/developers/getting-started/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/shipwire
- group: company
  title: ''
  type: Blog
  url: https://www.shipwire.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.shipwire.com/support/policy-fees-minimum-balance-and-ancillary-charges/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.shipwire.com
- group: other
  title: ''
  type: X
  url: https://x.com/shipwire
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shipwire-inc-
- group: commercial
  title: ''
  type: Plans
  url: plans/shipwire-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shipwire-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/shipwire-finops.yml
- group: build
  title: ''
  type: ClientLibraries
  url: https://www.shipwire.com/developers/client-libraries/
- group: start
  title: ''
  type: Sandbox
  url: https://api.beta.shipwire.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.shipwire.com/platform/empower-developers/
- group: docs
  title: ''
  type: GraphQL
  url: graphql/shipwire-graphql.md
created: '2026-06-13'
description: Shipwire is a global fulfillment and third-party logistics (3PL) platform providing a REST API for managing orders, inventory, warehousing, shipments, returns, and carrier selection across a worldwide network of fulfillment centers. The platform serves eCommerce brands with nine distinct RESTful APIs covering order management, stock tracking, receiving, returns, rate shopping, product catalogs, purchase orders, webhooks, and address validation, enabling fully automated fulfillment workflows.
finops:
- name: Shipwire Finops
  service_category: ''
  slug: shipwire-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Shipwire 3PL fulfillment platform. Shipwire exposes nine distinct REST APIs covering order management, stock tracking, receiving, returns, r
  name: Shipwire GraphQL Schema
  slug: shipwire-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shipwire.png
layout: provider
modified: '2026-06-13'
name: Shipwire
nav: Providers
network: true
overview: 'Shipwire publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fulfillment, Logistics, 3PL, eCommerce, and Shipping.


  Shipwire''s developer surface includes documentation, getting-started guide, engineering blog, pricing, sandbox, and 12 more developer resources.'
plans:
- name: Shipwire Plans Pricing
  plan_count: 1
  slug: shipwire-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 3
  name: Shipwire Rate Limits
  slug: shipwire-rate-limits
score:
  band: thin
  composite: 36.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 48.1
    developer_ergonomics: 37.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 36.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shipwire/refs/heads/main/screenshots/shipwire-2026-06-20T193825.png
security:
- kind: domain-security
  name: Shipwire Domain Security
  slug: shipwire-domain-security
  summary_line: TLSv1.3 · DMARC
slug: shipwire
tags:
- Fulfillment
- Logistics
- 3PL
- eCommerce
- Shipping
- Warehousing
- Inventory
- Orders
- Returns
- Carriers
website: https://www.shipwire.com/
---

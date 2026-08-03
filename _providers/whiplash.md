---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 30
  human_in_the_loop: 0
  name: Whiplash Agentic Access
  operation_count: 86
  slug: whiplash-agentic-access
  summary_line: 86 operations · 30 acting
api_count: 10
apis:
- description: Components defining quantity and relationships within product bundles — retrieve, update quantity, and destroy
  name: Whiplash Bundle Items API
  slug: whiplash-bundle-items-api
- description: Goods returning from end consumers — list, create (single/bulk), count, retrieve, update, destroy, and meta fields
  name: Whiplash Consumer Returns API
  slug: whiplash-consumer-returns-api
- description: Customer management — list, count, retrieve, update, and available actions
  name: Whiplash Customers API
  slug: whiplash-customers-api
- description: Document handling — list, create, retrieve, destroy, and actions
  name: Whiplash Documents API
  slug: whiplash-documents-api
- description: Inventory item management — list, create, count, retrieve, update, archive, bundles, actions, locations, meta fields, originators, scancodes, history, and stock by warehouse
  name: Whiplash Items API
  slug: whiplash-items-api
- description: Event tracking — list and retrieve
  name: Whiplash Notification Events API
  slug: whiplash-notification-events-api
- description: Webhook subscription management — list, create, count, retrieve, update, delete, and test
  name: Whiplash Notification Subscriptions API
  slug: whiplash-notification-subscriptions-api
- description: Order processing — full CRUD, bulk creation, actions, customs info, history, documents, items, serial numbers, shipping details, and wholesale
  name: Whiplash Orders API
  slug: whiplash-orders-api
- description: Incoming inventory shipments — list, create, bulk operations, count, retrieve, update, destroy, items, and meta fields
  name: Whiplash Shipnotices API
  slug: whiplash-shipnotices-api
- description: Simulation endpoints for testing order, consumer return, and shipnotice processing in sandbox environments
  name: Whiplash Simulate API
  slug: whiplash-simulate-api
artifact_total: 28
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/whiplash-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/whiplash-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/whiplash-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.getwhiplash.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.whiplash.com/hc/en-us/categories/13378954544411-Whiplash-Application-Developers
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/whiplashmerch
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/whiplash-merchandising-logistics
- group: company
  title: ''
  type: Blog
  url: https://www.getwhiplash.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getwhiplash.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getwhiplash.com
- group: other
  title: ''
  type: X
  url: https://x.com/getwhiplash
- group: commercial
  title: ''
  type: Plans
  url: plans/whiplash-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/whiplash-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/whiplash-finops.yml
created: '2026-06-13'
description: Whiplash is a multichannel order fulfillment and third-party logistics (3PL) platform providing a REST API for managing orders, SKUs, inventory levels, shipments, and returns across warehouse locations. Now operating as RyderShip under Ryder System, the platform offers pre-built integrations with leading ecommerce platforms including Shopify, and supports omnichannel fulfillment for DTC, retail, and wholesale brands.
examples:
- key_count: 4
  name: Whiplash Create Order Example
  slug: whiplash-create-order-example
- key_count: 4
  name: Whiplash Create Shipnotice Example
  slug: whiplash-create-shipnotice-example
- key_count: 4
  name: Whiplash Webhook Subscription Example
  slug: whiplash-webhook-subscription-example
finops:
- name: Whiplash Finops
  service_category: ''
  slug: whiplash-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/whiplash.png
json_schemas:
- name: Customer
  property_count: 15
  slug: whiplash-customer
- name: Fulfillment
  property_count: 23
  slug: whiplash-fulfillment
- name: Inventory
  property_count: 6
  slug: whiplash-inventory
- name: Order
  property_count: 31
  slug: whiplash-order
- name: Product Variant
  property_count: 24
  slug: whiplash-product-variant
- name: Product
  property_count: 16
  slug: whiplash-product
- name: Return
  property_count: 35
  slug: whiplash-return
jsonld:
- class_count: 39
  name: Whiplash Context
  property_count: 2
  slug: whiplash-context
layout: provider
modified: '2026-06-13'
name: Whiplash
nav: Providers
network: true
overview: 'Whiplash publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Bundle Items API, Consumer Returns API, Customers API, and 7 more. Tagged areas include Fulfillment, 3PL, Logistics, Ecommerce, and Orders.


  The Whiplash catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Whiplash''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Whiplash Plans Pricing
  plan_count: 1
  slug: whiplash-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Whiplash Rate Limits
  slug: whiplash-rate-limits
rules:
- name: Whiplash API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: whiplash-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 65.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 48.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/whiplash/refs/heads/main/screenshots/whiplash-2026-06-20T201434.png
security:
- kind: authentication
  name: Whiplash Authentication
  slug: whiplash-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Whiplash Domain Security
  slug: whiplash-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: whiplash
tags:
- Fulfillment
- 3PL
- Logistics
- Ecommerce
- Orders
- Inventory
- Shipments
- Returns
- Warehousing
website: https://www.getwhiplash.com
---

---
access_model:
  confidence: medium
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Orderdesk Agentic Access
  operation_count: 26
  slug: orderdesk-agentic-access
  summary_line: 26 operations · 16 acting
api_count: 1
apis:
- baseURL: https://app.orderdesk.me/api/v2
  baseurl_source: declared
  description: Maintain the store's inventory catalog.
  name: Order Desk Inventory Items API
  slug: orderdesk-inventory-items-api
- baseURL: https://app.orderdesk.me/api/v2
  baseurl_source: declared
  description: Manage line items within an order.
  name: Order Desk Order Items API
  slug: orderdesk-order-items-api
- baseURL: https://app.orderdesk.me/api/v2
  baseurl_source: declared
  description: Create, retrieve, search, update, and delete orders.
  name: Order Desk Orders API
  slug: orderdesk-orders-api
- baseURL: https://app.orderdesk.me/api/v2
  baseurl_source: declared
  description: Record and manage shipments and tracking against an order.
  name: Order Desk Shipments API
  slug: orderdesk-shipments-api
- baseURL: https://app.orderdesk.me/api/v2
  baseurl_source: declared
  description: Store settings, folder structure, and connectivity test.
  name: Order Desk Store API
  slug: orderdesk-store-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Order Desk Inventory Items API
  slug: open-orderdesk-inventory-items-api
- collection_type: open
  name: Order Desk Inventory Items Order Items API
  slug: open-orderdesk-order-items-api
- collection_type: open
  name: Order Desk Inventory Items Orders API
  slug: open-orderdesk-orders-api
- collection_type: open
  name: Order Desk Inventory Items Shipments API
  slug: open-orderdesk-shipments-api
- collection_type: open
  name: Order Desk Inventory Items Store API
  slug: open-orderdesk-store-api
- collection_type: open
  name: Order Desk API
  slug: open-orderdesk
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/orderdesk-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/orderdesk-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orderdesk-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/orderdesk-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/order-desk
- group: company
  title: ''
  type: Website
  url: https://www.orderdesk.com
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.orderdesk.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/orderdesk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/orderdesk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/orderdesk-finops.yml
created: '2026-07-11'
description: Order Desk is an ecommerce order management and fulfillment routing platform that centralizes orders from shopping carts and marketplaces, then automates routing to print-on-demand, dropshipping, warehouse, and shipping providers via a rule builder and 300-plus integrations. Its public REST API (base https://app.orderdesk.me/api/v2, authenticated with store-id and api-key headers) exposes Orders, Order Items, Shipments, Inventory Items, and Store settings so developers can create and update orders, manage line items, record shipments and tracking, and sync inventory programmatically.
finops:
- name: Orderdesk Finops
  service_category: Ecommerce and Order Management
  slug: orderdesk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/orderdesk.png
layout: provider
modified: '2026-07-11'
name: Order Desk
nav: Providers
network: true
overview: 'Order Desk publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Inventory Items API, Order Items API, Orders API, and 2 more. Tagged areas include E-Commerce, Order Management, Fulfillment, Dropshipping, and Inventory.


  Order Desk''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Orderdesk Plans Pricing
  plan_count: 4
  slug: orderdesk-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Orderdesk Rate Limits
  slug: orderdesk-rate-limits
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 59.6
    developer_ergonomics: 29.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/orderdesk/refs/heads/main/screenshots/orderdesk-2026-08-07T190910.png
security:
- kind: authentication
  name: Orderdesk Authentication
  slug: orderdesk-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Orderdesk Domain Security
  slug: orderdesk-domain-security
  summary_line: TLSv1.3 · DMARC
slug: orderdesk
tags:
- E-Commerce
- Order Management
- Fulfillment
- Dropshipping
- Inventory
- Shipping
website: https://www.orderdesk.com
---

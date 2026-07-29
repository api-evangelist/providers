---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 6
apis:
- description: Programmatic access to sales/fulfillment orders - create and manage orders that flow into Hopstack's omnichannel order management and picking, packing, and shipping workflows. Orders is one of the cor
  name: Hopstack Orders API
  slug: hopstack-orders-api
- description: Programmatic access to consignments - the inbound/receiving records that bring stock into a Hopstack-managed warehouse. Consignments is explicitly called out alongside orders as a core resource expose
  name: Hopstack Consignments API
  slug: hopstack-consignments-api
- description: Inventory and stock-ledger operations for Hopstack's inventory management module - tracking on-hand quantities, locations, and stock movements across warehouses. Modeled from Hopstack's documented WMS
  name: Hopstack Inventory API
  slug: hopstack-inventory-api
- description: Shipment creation and management tied to Hopstack's picking, packing, and shipping workflows and its multi-carrier integrations (FedEx, UPS, DHL, EasyPost, Shippo, and others). Modeled from Hopstack's
  name: Hopstack Shipments API
  slug: hopstack-shipments-api
- description: Product and SKU catalog management underpinning inventory and orders in Hopstack. Modeled from Hopstack's documented WMS data model; specific API endpoints are not confirmed in the public reference (e
  name: Hopstack Products API
  slug: hopstack-products-api
- description: Warehouse and location configuration for multi-warehouse, multi-client (3PL) operations. Modeled from Hopstack's documented warehouse management module; specific API endpoints are not confirmed in the
  name: Hopstack Warehouses API
  slug: hopstack-warehouses-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hopstack-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hopstack.io/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hopstack
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.hopstack.io/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.hopstack.io/reference
- group: docs
  title: ''
  type: Documentation
  url: https://help.hopstack.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/hopstack-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hopstack-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hopstack-finops.yml
created: '2026-07-05'
description: Hopstack is an AI-native, cloud-based warehouse management system (WMS) and fulfillment operations platform that helps warehouses, 3PLs, and e-commerce operators optimize inbound logistics, inventory, order processing, picking, packing, shipping, and returns across channels. Hopstack exposes a documented RESTful API (referenced at apidocs.hopstack.io) for programmatic access to core resources such as orders and consignments, secured with a per-user X-API-Key generated from the Hopstack Dashboard. API access is gated - a customer must contact Hopstack Support to enable API-key generation in the UI - and the full endpoint surface, base URL, and machine-readable specification are published behind that account/partner reference rather than as a fully open catalog.
finops:
- name: Hopstack Finops
  service_category: Warehouse Management and Fulfillment
  slug: hopstack-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hopstack.png
layout: provider
modified: '2026-07-05'
name: Hopstack
nav: Providers
network: true
overview: 'Hopstack publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Warehouse Management, WMS, Fulfillment, Logistics, and Supply Chain.


  Hopstack''s developer surface includes documentation, API reference, and 7 more developer resources.'
plans:
- name: Hopstack Plans Pricing
  plan_count: 1
  slug: hopstack-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 2
  name: Hopstack Rate Limits
  slug: hopstack-rate-limits
score:
  band: emerging
  composite: 18.0
  delta: -2.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 20.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hopstack/refs/heads/main/screenshots/hopstack-2026-07-25T221422.png
security:
- kind: domain-security
  name: Hopstack Domain Security
  slug: hopstack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hopstack
tags:
- Warehouse Management
- WMS
- Fulfillment
- Logistics
- Supply Chain
- Inventory
- 3PL
- E-commerce
website: https://www.hopstack.io/
---

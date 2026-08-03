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
    agentic_access: false
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
  score: 28.4
  scored_at: '2026-08-03'
api_count: 7
apis:
- description: 'Query bookings by Zencargo reference and retrieve booking details: cargo, consignor/consignee, forwarder, incoterms, load type, mode of transport, bills of lading, required delivery date, and attached'
  name: Zencargo Bookings API
  slug: zencargo-bookings-api
- description: Track shipment progress through scheduled carriage legs, cargo journey details (estimated/actual collection and delivery), and voyage milestones (collected, gate in, cargo aboard, departed/arrived ter
  name: Zencargo Shipment Visibility API
  slug: zencargo-shipment-visibility-api
- description: Create, query, update, close, and delete purchase orders and their ordered line items and SKU-level Lots. Keeps an ERP in sync with Zencargo as the source of truth for pre-booking PO data (cargo ready
  name: Zencargo Purchase Orders API
  slug: zencargo-purchase-orders-api
- description: Manage the product catalog - create, query, update, archive, and unarchive products (and core products with characteristics, dimensions, weights, tariff codes, and pricing), plus product categories an
  name: Zencargo Products API
  slug: zencargo-products-api
- description: Query packing lists for a booking (BOOKING_REFERENCE) or a specific cargo (CARGO_ID), returning per-container lines with the Lot and Product behind each packed item. Available for POs on FCL bookings.
  name: Zencargo Packing Lists API
  slug: zencargo-packing-lists-api
- description: Retrieve account details by UUID and search assignable accounts (customers, suppliers, manufacturers) and their locations to resolve the origin, destination, and manufacturer IDs referenced when creat
  name: Zencargo Accounts and Locations API
  slug: zencargo-accounts-locations-api
- description: Outbound HTTP webhooks. Zencargo POSTs a JSON payload (topic, targetType, targetId) to a customer-registered HTTPS callback URL when events such as BOOKING_CREATED occur, signed with a base64 Zencargo
  name: Zencargo Webhooks
  slug: zencargo-webhooks
artifact_total: 13
collections:
- collection_type: open
  name: Zencargo GraphQL API
  slug: open-zencargo
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zencargo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zencargo-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zencargo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zencargo
- group: company
  title: ''
  type: Website
  url: https://www.zencargo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.zencargo.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/zencargo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zencargo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zencargo-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.zencargo.com/resources/
created: '2026-07-12'
description: Zencargo is a digital freight forwarder and supply-chain visibility platform for ocean, air, road, and rail shipments. Its GraphQL API gives enterprise customers programmatic access to bookings, shipment tracking and voyage milestones, purchase orders, products, packing lists, and accounts, plus HTTP webhooks for booking and purchase-order events. The API is customer-provisioned - each account is issued a dedicated staging and production endpoint and API-key credentials by their Zencargo account manager.
finops:
- name: Zencargo Finops
  service_category: Logistics and Supply Chain
  slug: zencargo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zencargo.png
layout: provider
modified: '2026-07-12'
name: Zencargo
nav: Providers
network: true
overview: 'Zencargo publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Freight Forwarding, Supply Chain, Logistics, Ocean Freight, and Shipment Tracking.


  Zencargo''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Zencargo Plans Pricing
  plan_count: 1
  slug: zencargo-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Zencargo Rate Limits
  slug: zencargo-rate-limits
score:
  band: thin
  composite: 32.2
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 43.2
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 32.2
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Zencargo Authentication
  slug: zencargo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zencargo Domain Security
  slug: zencargo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zencargo
tags:
- Freight Forwarding
- Supply Chain
- Logistics
- Ocean Freight
- Shipment Tracking
- Bookings
- Supply Chain Visibility
- Freight
- SaaS
- GraphQL
website: https://www.zencargo.com/
---

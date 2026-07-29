---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
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
api_count: 6
apis:
- description: 'Access to dealership customer and prospect records held in the Reynolds ERA-IGNITE / POWER DMS - contact details, ownership history, and marketing consent - read and (per certification scope) written '
  name: Reynolds DMS Customer Data API
  slug: reynolds-reynolds-dms-customer-data-api
- description: New and used vehicle inventory in the Reynolds DMS - VINs, stock numbers, pricing, and status - available to certified partners for read and pricing write-back (the "DMS writeback" pattern used by inv
  name: Reynolds Vehicle Inventory API
  slug: reynolds-reynolds-vehicle-inventory-api
- description: Retail and lease deal, desking, and Finance and Insurance (F&I) data in the Reynolds DMS - deal structures, lender submissions, and F&I products - for certified partners to read and, where authorized,
  name: Reynolds Sales, Deals and F&I API
  slug: reynolds-reynolds-sales-deals-fi-api
- description: Service department data - repair orders, labor operations, and appointments - in the Reynolds DMS. Certified service and scheduling partners push appointments into the DMS and pull DMS appointments an
  name: Reynolds Service and Repair Orders API
  slug: reynolds-reynolds-service-repair-orders-api
- description: Parts department data in the Reynolds DMS - on-hand quantities, pricing, purchase orders, and suppliers - for certified parts, catalog, and e-commerce partners. Gated behind RCI certification; endpoin
  name: Reynolds Parts Inventory API
  slug: reynolds-reynolds-parts-inventory-api
- description: Dealership accounting data in the Reynolds DMS - general ledger entries, accounts receivable and payable, cash receipts, and postings - exposed to certified accounting, reconciliation, and reporting p
  name: Reynolds Accounting API
  slug: reynolds-reynolds-accounting-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reynolds-reynolds-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/reynolds-and-reynolds
- group: company
  title: ''
  type: Website
  url: https://www.reyrey.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.reyrey.com/partners/reynolds-certified-interface
- group: start
  title: ''
  type: SignUp
  url: https://www.reyrey.com/company/reynolds-data-management
- group: commercial
  title: ''
  type: Plans
  url: plans/reynolds-reynolds-plans-pricing.yml
created: '2026-07-10'
description: Reynolds and Reynolds is one of the automotive industry's largest Dealership Management System (DMS) providers, running the ERA-IGNITE and POWER platforms that operate the core of thousands of franchised car dealerships - sales and desking, F&I, service and repair orders, parts inventory, CRM, and dealership accounting. Reynolds does NOT publish an open, self-serve developer API. All programmatic access to DMS data flows through the Reynolds Certified Interface (RCI) program, a certification-gated, contract-and-NDA partner program run by Reynolds Data Management. RCI provides secured, real-time, bi-directional interfaces so certified third parties can read from and write back to a dealer's Reynolds DMS. There is no public developer portal, no public API reference, and no published OpenAPI. The APIs below are logical groupings of the DMS data domains exposed through RCI; endpoints are modeled, not sourced from public documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reynolds-reynolds.png
layout: provider
modified: '2026-07-10'
name: Reynolds and Reynolds
nav: Providers
network: true
overview: 'Reynolds and Reynolds publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Dealership Management System, DMS, Reynolds Certified Interface, and RCI.


  Reynolds and Reynolds'' developer surface includes documentation, signup flow, and 4 more developer resources.'
plans:
- name: Reynolds Reynolds Plans Pricing
  plan_count: 2
  slug: reynolds-reynolds-plans-pricing
random_paper: 34
score:
  band: emerging
  composite: 15.1
  delta: -2.2
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Reynolds Reynolds Domain Security
  slug: reynolds-reynolds-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: reynolds-reynolds
tags:
- Automotive
- Dealership Management System
- DMS
- Reynolds Certified Interface
- RCI
- Certified Interface
- Partner API
- Gated Access
website: https://www.reyrey.com
---

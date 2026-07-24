---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 4
apis:
- description: Logical Point of Sale capability of the Tillpoint platform - ringing up sales, applying discounts, splitting payments, issuing receipts and refunds, and reconciling tills. Endpoints are modeled, not d
  name: Tillpoint Point of Sale API
  slug: tillpoint-point-of-sale-api
- description: Logical Inventory and Products capability - product catalog, variants, pricing, real-time stock levels, low-stock alerts, and multi-location transfers. Modeled as a capability area only - Tillpoint do
  name: Tillpoint Inventory API
  slug: tillpoint-inventory-api
- description: Logical Customers/CRM capability - customer records, purchase history, loyalty programs, and marketing sync. Tillpoint's CRM module pushes customers to Mailchimp via a pre-built integration rather tha
  name: Tillpoint Customers (CRM) API
  slug: tillpoint-customers-api
- description: Logical Accounting capability - built-in double-entry accounting plus sync to QuickBooks Online and Xero through pre-built integrations. Modeled as a capability area - no public accounting API is docu
  name: Tillpoint Accounting API
  slug: tillpoint-accounting-api
artifact_total: 6
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tillpoint
- group: company
  title: ''
  type: Website
  url: https://www.tillpoint.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.tillpoint.com/pos-system-integration/
- group: commercial
  title: ''
  type: Plans
  url: plans/tillpoint-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tillpoint-finops.yml
created: '2026-07-11'
description: Tillpoint is a modular, cloud-based EPOS (electronic point of sale) and business management platform for retail, hospitality, and services. A single subscription bundles 25+ modules - Point of Sale, Inventory, Customers/CRM, Staff, Accounting, Purchase Orders, Reporting, and more - across one terminal or thousands of locations. As of this review Tillpoint does not publish a documented public or partner developer API - there is no developer portal, no API reference, and no OpenAPI. Connectivity is delivered through pre-built integrations (QuickBooks Online, Xero, WooCommerce, PayPal, Worldpay, Mailchimp). The API surfaces catalogued here (Point of Sale, Inventory, Customers, Accounting) are logical capability areas of the platform and are honestly marked as endpointsModeled - no endpoints are fabricated. Direct/programmatic access requires contacting Tillpoint.
finops:
- name: Tillpoint Finops
  service_category: Point of Sale and Business Management
  slug: tillpoint-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tillpoint.png
layout: provider
modified: '2026-07-11'
name: Tillpoint
nav: Providers
network: true
overview: 'Tillpoint publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Point of Sale, POS, EPOS, Retail, and Business Management.


  Tillpoint''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: Tillpoint Plans Pricing
  plan_count: 3
  slug: tillpoint-plans-pricing
random_paper: 22
score:
  band: emerging
  composite: 18.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
slug: tillpoint
tags:
- Point of Sale
- POS
- EPOS
- Retail
- Business Management
- Inventory
- Hospitality
- CRM
- Accounting
website: https://www.tillpoint.com
---

---
access_model:
  confidence: medium
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
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
- description: Modeled tee sheet and tee-time booking surface for creating, searching, and managing tee-time reservations, availability, and rate types. Teesnap does not publish public API documentation for this cap
  name: Teesnap Tee Sheet API
  slug: teesnap-tee-sheet-api
- description: Modeled point-of-sale surface covering pro-shop and food-and-beverage sales, orders, tenders, and payment capture (Teesnap integrates Heartland payment processing and syncs to QuickBooks Online). No p
  name: Teesnap Point of Sale API
  slug: teesnap-point-of-sale-api
- description: Modeled customer and membership surface for managing golfer profiles, memberships, and account data that feeds Teesnap's marketing system. Player profile sync to Golf Genius Tournament Management is o
  name: Teesnap Members and Customers API
  slug: teesnap-members-customers-api
- description: 'Modeled product catalog and inventory surface backing the pro-shop POS and Teesnap online store - products, pricing, and stock levels. No public API documentation is published; endpoints are honestly '
  name: Teesnap Products and Inventory API
  slug: teesnap-products-inventory-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teesnap-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/teesnap
- group: company
  title: ''
  type: Website
  url: https://www.teesnap.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.teesnap.com
- group: commercial
  title: ''
  type: Plans
  url: plans/teesnap-plans-pricing.yml
created: '2026-07-11'
description: Teesnap is an all-in-one golf course management platform and point-of-sale system for golf operators, founded in 2013 and based in Las Vegas, Nevada. Its cloud software suite covers a tee sheet and tee-time booking engine, golf and food-and-beverage point of sale, customer and membership management, an online store, websites, payments, and a marketing and reporting system. Teesnap connects to the wider golf ecosystem through partner integrations - GolfNow (its official online tee-time distribution partner via NBC Sports Next), Priswing dynamic pricing, Golf Genius tournament management, QuickBooks Online accounting, Gallus mobile apps, Heartland payment processing, and range hardware from eRange and Select Pi. As of this catalog's review date Teesnap does not publish a public, self-service developer API or developer portal; integrations are delivered through partner-gated, business-development relationships. The APIs listed here are honestly modeled from Teesnap's public product
  surface and are not sourced from published API documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/teesnap.png
layout: provider
modified: '2026-07-11'
name: Teesnap
nav: Providers
network: true
overview: 'Teesnap publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Golf, Point of Sale, POS, Tee Times, and Golf Course Management.


  Teesnap''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: Teesnap Plans Pricing
  plan_count: 1
  slug: teesnap-plans-pricing
random_paper: 38
score:
  band: minimal
  composite: 14.7
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Teesnap Domain Security
  slug: teesnap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: teesnap
tags:
- Golf
- Point of Sale
- POS
- Tee Times
- Golf Course Management
- Booking
- Partner Gated
website: https://www.teesnap.com
---

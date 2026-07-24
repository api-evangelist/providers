---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source: []
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
api_count: 3
apis:
- description: Conceptual product/catalog surface covering Printique's print products - photo prints, fine-art giclee prints, photo books, albums, metal, acrylic, canvas, glass, framed and wood wall decor, cards, ca
  name: Printique Product Catalog (Modeled)
  slug: printique-catalog-api
- description: Conceptual order-placement and fulfillment surface. Automated order fulfillment is real but is delivered through partner platforms - the Squarespace integration automates fulfillment directly from a s
  name: Printique Orders and Fulfillment (Modeled)
  slug: printique-orders-api
- description: Conceptual order-status, production, and shipment-tracking surface. Printique communicates production and shipping status (including white-label blind shipping for Pro members) through its account UI,
  name: Printique Order Status and Shipping (Modeled)
  slug: printique-order-status-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/printique-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/printique-by-adorama
- group: company
  title: ''
  type: Website
  url: https://www.printique.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.printique.com/company/printique-pro-photo-lab-for-businesses/
- group: commercial
  title: ''
  type: Plans
  url: plans/printique-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://www.printique.com/blog/
created: '2026-07-11'
description: Printique (An Adorama Company, formerly AdoramaPix) is a professional online photo lab based in Brooklyn, NYC that produces photo prints, fine-art giclee prints, photo books, albums, wall decor (metal, acrylic, canvas, glass, framed, wood), cards, calendars, and photo gifts. Printique does NOT publish a documented public developer or fulfillment API. There is no developer portal, no published REST reference, no API keys, and no OpenAPI definition on the open web. Programmatic and automated ordering is instead delivered through prebuilt partner-platform integrations - a Squarespace integration that syncs products and automates order fulfillment, a PhotoShelter wholesale print-and-product integration for professional photographers, Fundy Designer album integration, and desktop plugins for Adobe Lightroom and Capture One that publish images directly to Printique. A Pro membership tier ($14.95/month or $159.95/year) unlocks tiered wholesale savings, white-label blind shipping, and
  dedicated support for photography businesses. The logical API surfaces below (catalog, orders, order status) are honestly modeled from Printique's public product, Pro, and integration pages to describe how ordering works conceptually; they are NOT transcribed from any released or documented Printique API. No public endpoints, paths, or request/response schemas are published, so endpointsModeled is true and no endpoint surface has been fabricated beyond these named, integration-delivered capabilities.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/printique.png
layout: provider
modified: '2026-07-11'
name: Printique
nav: Providers
network: true
overview: 'Printique publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Photo Printing, Print Fulfillment, Photo Lab, Photography, and Prints.


  Printique''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Printique Plans Pricing
  plan_count: 0
  slug: printique-plans-pricing
random_paper: 24
score:
  band: minimal
  composite: 10.9
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Printique Domain Security
  slug: printique-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: printique
tags:
- Photo Printing
- Print Fulfillment
- Photo Lab
- Photography
- Prints
- Albums
- Wall Art
- Print on Demand
website: https://www.printique.com
---

---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
api_count: 2
apis:
- description: 'Jane''s documented HTTP API (published as a Swagger UI at api.iheartjane.com/jane-api-docs) for retrieving live store menu products and for generating the access tokens used to authenticate downstream '
  name: Jane Menu Products API
  slug: iheartjane-menu-products-api
- description: 'The Jane DM SDK is a TypeScript/JavaScript library (usable in client-side React/Angular/Vue and server-side Node.js/Express apps) that embeds MyHigh-powered personalization and publisher monetization '
  name: Jane Digital Merchandising SDK (Jane DM SDK)
  slug: iheartjane-digital-merchandising-sdk
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iheartjane-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jane-technologies-inc
- group: company
  title: ''
  type: Website
  url: https://www.iheartjane.com
- group: docs
  title: ''
  type: Documentation
  url: https://dm-sdk-docs.iheartjane.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.iheartjane.com/jane-api-docs/index.html
created: '2026-07-03'
description: Jane Technologies (iHeartJane) is a cannabis ecommerce and marketplace platform that powers real-time online menus, point-of-sale and kiosk checkout, order and reservation flows, and the Jane Universal Product Catalog for 2,500+ dispensaries and brands across the United States and Canada. Jane exposes a documented HTTP API (the Jane API, published as Swagger at api.iheartjane.com/jane-api-docs) for retrieving live store menu products and generating access tokens, and a partner Digital Merchandising SDK (Jane DM SDK) for embedding MyHigh-powered personalization and sponsored-product widgets into a retailer's own menu. Both surfaces are partner-gated - access requires approval and credentials from a Jane account representative - so the endpoints listed here are modeled from Jane's public documentation rather than exercised against a live, open, unauthenticated API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iheartjane.png
layout: provider
modified: '2026-07-03'
name: Jane (iHeartJane)
nav: Providers
network: true
overview: 'Jane (iHeartJane) publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cannabis, Ecommerce, Marketplace, Dispensary, and Menu.


  Jane (iHeartJane)''s developer surface includes documentation and 4 more developer resources.'
random_paper: 67
score:
  band: minimal
  composite: 10.3
  delta: -2.4
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/iheartjane/refs/heads/main/screenshots/iheartjane-2026-07-25T222053.png
security:
- kind: domain-security
  name: Iheartjane Domain Security
  slug: iheartjane-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iheartjane
tags:
- Cannabis
- Ecommerce
- Marketplace
- Dispensary
- Menu
- Products
- Retail
- Point of Sale
- Personalization
website: https://www.iheartjane.com
---

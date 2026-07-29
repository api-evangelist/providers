---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API for managing orders, inventory, shipments, and returns within the Stord commerce fulfillment platform. Built with an API-first design using JSON:API specification and OpenAPI annotations. Sup
  name: Stord API
  slug: stord-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/stord-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stord-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stord.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.stord.com/integrations
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/stordco
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stord
- group: company
  title: ''
  type: Blog
  url: https://www.stord.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stord.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.stord.com/
- group: other
  title: ''
  type: X
  url: https://x.com/getstord
- group: commercial
  title: ''
  type: Plans
  url: plans/stord-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stord-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/stord-finops.yml
created: '2026-06-13'
description: Stord is a commerce fulfillment platform that combines physical warehouse infrastructure with integrated software to manage omnichannel logistics for DTC and B2B brands. The platform provides REST APIs for managing orders, inventory, shipments, and returns across a network of 20+ fulfillment nodes, with pre-built integrations for Shopify, BigCommerce, Magento, WooCommerce, Amazon, and ERP systems such as Oracle NetSuite. Stord One Commerce (OMS) and Stord One Warehouse (WMS) deliver real-time supply chain visibility and AI-powered parcel optimization, powering over $10 billion in annual commerce for brands including AG1, Native, and Legion Athletics.
finops:
- name: Stord Finops
  service_category: ''
  slug: stord-finops
graphqls:
- description: This conceptual GraphQL schema represents the Stord commerce fulfillment platform API surface. Stord provides omnichannel logistics for DTC and B2B brands, managing orders, inventory, shipments, and r
  name: Stord GraphQL Schema
  slug: stord-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stord.png
layout: provider
modified: '2026-06-13'
name: Stord
nav: Providers
network: true
overview: 'Stord publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Commerce Fulfillment, Order Management, Inventory Management, Shipment Tracking, and Returns Management.


  Stord''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Stord Plans Pricing
  plan_count: 0
  slug: stord-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Stord Rate Limits
  slug: stord-rate-limits
score:
  band: thin
  composite: 29.1
  delta: 0.2
  facets:
    commercial_clarity: 26.3
    contract_quality: 48.1
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 28.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stord/refs/heads/main/screenshots/stord-2026-06-20T194604.png
security:
- kind: domain-security
  name: Stord Domain Security
  slug: stord-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Stord Trust Center
  slug: stord-trust-center
  summary_line: SOC 2, GDPR
slug: stord
tags:
- Commerce Fulfillment
- Order Management
- Inventory Management
- Shipment Tracking
- Returns Management
- Warehouse Management
- Logistics
- Supply Chain
- Shopify Integration
- BigCommerce Integration
- ERP Integration
- EDI
website: https://www.stord.com/
---

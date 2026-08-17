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
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: Fedex Agentic Access
  operation_count: 7
  slug: fedex-agentic-access
  summary_line: 7 operations · 7 acting · 1 human-in-the-loop
api_count: 10
apis:
- description: Track API allows customers and partners to retrieve up-to-the-minute package and shipment status, scan events, delivery details, and proof of delivery using tracking numbers, reference numbers, or TCN
  name: FedEx Track API
  slug: track
- description: Ship API lets developers create domestic and international shipments, generate shipping labels, validate addresses, schedule pickups, and manage end-to-end shipment workflows programmatically.
  name: FedEx Ship API
  slug: ship
- description: Rate API returns rate quotes and transit times for FedEx Express, Ground, Freight, and SmartPost services so applications can present pricing and delivery options at checkout or during fulfillment.
  name: FedEx Rate API
  slug: rate
- description: Address Validation API verifies postal addresses for deliverability, classifies them as residential or commercial, and corrects common formatting and spelling issues prior to shipment creation.
  name: FedEx Address Validation API
  slug: address-validation
- description: Pickup API provides programmatic access to schedule, modify, and cancel package pickups, and to determine pickup availability for a given origin and service combination.
  name: FedEx Pickup API
  slug: pickup
- description: Locations API helps applications find FedEx Office, FedEx Ship Center, drop boxes, and authorized ship centers near a given address or coordinate, including hours of operation and supported services.
  name: FedEx Locations API
  slug: locations
- description: Authorization API issues OAuth 2.0 access tokens used to authenticate all other FedEx API calls. Tokens are obtained via client credentials generated from a FedEx Developer Portal project.
  name: FedEx Authorization API
  slug: authorization
- description: Shipment Visibility Webhook pushes near real-time tracking events to a registered HTTPS endpoint, eliminating the need to repeatedly poll the Track API for shipment status changes.
  name: FedEx Shipment Visibility Webhook
  slug: shipment-visibility-webhook
- description: OAuth 2.0 token issuance for FedEx APIs
  name: FedEx Authorization API
  slug: fedex-authorization-api
- description: Track API v1 operations
  name: FedEx Track API
  slug: fedex-track-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FedEx Track Authorization API
  slug: open-fedex-authorization-api
- collection_type: open
  name: FedEx Authorization Track API
  slug: open-fedex-track-api
- collection_type: open
  name: FedEx Track API
  slug: open-fedex
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fedex-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fedex-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fedex-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fedex
- group: company
  title: ''
  type: Website
  url: https://www.fedex.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.fedex.com/api/en-us/home.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.fedex.com/api/en-us/get-started.html
- group: other
  title: ''
  type: Catalog
  url: https://developer.fedex.com/api/en-us/catalog.html
- group: start
  title: ''
  type: Signup
  url: https://developer.fedex.com/api/en-us/home.html
created: '2025-03-01'
description: FedEx is a logistics company that provides shipping and delivery services worldwide. They offer a range of solutions for individuals and businesses, including express shipping, freight services, and e-commerce fulfillment. FedEx publishes a suite of REST APIs covering tracking, shipping, rating, address validation, pickup, locator, trade documents, and post-shipment visibility through their developer portal.
features:
- 'FedEx: API access via partner / B2B contracts only'
- No public API pricing published — contact enterprise sales
- FedEx Developer Portal APIs (Ship, Rate, Track, Address Validation) require an account; rates vary by ship date / weight / zone.
finops:
- name: Fedex Finops
  service_category: Logistics / Shipping
  slug: fedex-finops
graphqls:
- description: This conceptual GraphQL schema represents the FedEx shipping and logistics platform APIs, covering the full lifecycle of shipment creation, tracking, rating, pickup scheduling, location lookup, and ad
  name: FedEx GraphQL Schema
  slug: fedex-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fedex.png
layout: provider
modified: '2026-05-04'
name: FedEx
nav: Providers
network: true
overview: 'FedEx publishes 2 APIs on the [APIs.io](https://apis.io/) network: Authorization API and Track API. Tagged areas include Address Validation, Freight, Logistics, Pickup, and Rating.


  FedEx''s developer surface includes authentication, documentation, getting-started guide, signup flow, and 5 more developer resources.'
plans:
- name: Fedex Plans Pricing
  plan_count: 1
  slug: fedex-plans-pricing
press:
- date: '2026-05-25'
  title: FedEx to Offer Access to AI-Powered Post-Purchase ...
  url: https://newsroom.fedex.com/newsroom/global-english/fedex-to-offer-access-to-ai-powered-post-purchase-solutions-for-enterprises
- date: '2026-05-25'
  title: FedEx and Cisco Transform Business Through AI Workflows
  url: https://www.virtasant.com/ai-today/unlocking-potential-ai-workflows-at-fedex-cisco
- date: '2026-05-25'
  title: FedEx Freight Adds AI Tools to Boost Win Percentage - TT
  url: https://www.ttnews.com/articles/fedex-freight-ai-tools-2026
- date: '2026-05-25'
  title: Technology and Innovation Policy Perspectives
  url: https://www.fedex.com/en-us/about/policy/technology-innovation.html
- date: '2026-05-25'
  title: FedEx Announces Expansion of FedEx Fulfillment With ...
  url: https://newsroom.fedex.com/newsroom/global-english/fedex-announces-expansion-of-fedex-fulfillment-with-nimble-alliance
random_paper: 77
rate_limits:
- limit_count: 1
  name: Fedex Rate Limits
  slug: fedex-rate-limits
score:
  band: thin
  composite: 35.0
  delta: 0.0
  facets:
    commercial_clarity: 26.3
    contract_quality: 62.3
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fedex/refs/heads/main/screenshots/fedex-2026-06-20T181131.png
security:
- kind: authentication
  name: Fedex Authentication
  slug: fedex-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fedex Domain Security
  slug: fedex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fedex
tags:
- Address Validation
- Freight
- Logistics
- Pickup
- Rating
- Shipping
- Tracking
- Webhooks
- Fortune 100
website: https://www.fedex.com/
---

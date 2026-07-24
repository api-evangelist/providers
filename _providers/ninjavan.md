---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Ninjavan Agentic Access
  operation_count: 12
  slug: ninjavan-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 5
apis:
- description: OAuth2 client-credentials token issuance.
  name: Ninja Van OAuth API API
  slug: ninjavan-oauth-api-api
- description: Create and cancel delivery orders and generate waybills.
  name: Ninja Van Order API API
  slug: ninjavan-order-api-api
- description: Ninja Point pick-up / drop-off locations and shipper drop-off.
  name: Ninja Van PUDO API API
  slug: ninjavan-pudo-api-api
- description: Estimate shipping price.
  name: Ninja Van Tariff API API
  slug: ninjavan-tariff-api-api
- description: Pull tracking events for parcels.
  name: Ninja Van Tracking API API
  slug: ninjavan-tracking-api-api
artifact_total: 12
collections:
- collection_type: open
  name: Ninja Van API (ninjaAPI)
  slug: open-ninjavan
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ninjavan-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ninjavan-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ninjavan-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ninja-van
- group: company
  title: ''
  type: Website
  url: https://www.ninjavan.co/en-sg
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.ninjavan.co/
- group: commercial
  title: ''
  type: Plans
  url: plans/ninjavan-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ninjavan-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ninjavan-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.ninjavan.co/en-sg/
created: '2026-07-12'
description: Ninja Van is a Southeast Asian last-mile logistics and parcel-delivery company operating across Singapore, Malaysia, Indonesia, Philippines, Vietnam, and Thailand. Its ninjaAPI lets merchants and e-commerce platforms integrate shipping programmatically - create and cancel delivery orders, generate waybills (AWB), estimate tariffs, look up Ninja Point (PUDO) drop-off locations, receive parcel status updates via webhooks, and pull tracking events. The API is country-scoped (the country code is part of the path, e.g. https://api.ninjavan.co/SG/...) and authenticated with OAuth2 client credentials; access is granted per merchant after an onboarding and integration audit.
finops:
- name: Ninjavan Finops
  service_category: Logistics and Shipping
  slug: ninjavan-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ninjavan.png
layout: provider
modified: '2026-07-12'
name: Ninja Van
nav: Providers
network: true
overview: 'Ninja Van publishes 5 APIs on the [APIs.io](https://apis.io/) network, including OAuth API API, Order API API, PUDO API API, and 2 more. Tagged areas include Logistics, Last-Mile Delivery, Shipping, Southeast Asia, and Parcels.


  Ninja Van''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Ninjavan Plans Pricing
  plan_count: 3
  slug: ninjavan-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 4
  name: Ninjavan Rate Limits
  slug: ninjavan-rate-limits
score:
  band: thin
  composite: 37.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 59.1
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Ninjavan Authentication
  slug: ninjavan-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Ninjavan Domain Security
  slug: ninjavan-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ninjavan
tags:
- Logistics
- Last-Mile Delivery
- Shipping
- Southeast Asia
- Parcels
- Tracking
- Fulfillment
- E-commerce Logistics
- Waybill
- SaaS
website: https://www.ninjavan.co/en-sg
---

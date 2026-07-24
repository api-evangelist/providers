---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Parcelsapp Agentic Access
  operation_count: 4
  slug: parcelsapp-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 3
apis:
- description: Subscription usage and account limits
  name: Parcels App Account API
  slug: parcelsapp-account-api
- description: Create tracking requests and read results
  name: Parcels App Tracking API
  slug: parcelsapp-tracking-api
- description: Callbacks sent to your `webhookUrl` when tracking progresses or completes. Pass `webhookUrl` in `POST /shipments/tracking`; Parcels sends JSON `POST` requests to that URL.
  name: Parcels App Webhooks API
  slug: parcelsapp-webhooks-api
artifact_total: 9
collections:
- collection_type: open
  name: Parcels App Tracking API
  slug: open-parcelsapp
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/parcelsapp-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parcelsapp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://parcelsapp.com
- group: docs
  title: ''
  type: Documentation
  url: https://parcelsapp.com/api-docs/
- group: start
  title: ''
  type: Portal
  url: https://parcelsapp.com/dashboard/
- group: commercial
  title: ''
  type: Pricing
  url: https://parcelsapp.com/pricing-api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://parcelsapp.com/terms-api
- group: company
  title: ''
  type: Blog
  url: https://parcelsapp.com/blog
- group: commercial
  title: ''
  type: Plans
  url: plans/parcelsapp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/parcelsapp-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/parcelsapp-finops.yml
created: '2026-07-11'
description: Parcels App (parcelsapp.com) is a universal parcel tracking service that tracks packages, air cargo (AWB), road freight (LTL/FTL), and sea freight across 1,540 postal operators, couriers, and logistics carriers worldwide - USPS, UPS, FedEx, DHL, Royal Mail, China Post, Cainiao, 4PX, and many more. The Parcels API v3 is an asynchronous shipment tracking API - create a tracking request, then poll by UUID or receive webhook callbacks until results are complete - with automatic carrier detection, localized tracking events, and cached results returned immediately.
finops:
- name: Parcelsapp Finops
  service_category: Integration
  slug: parcelsapp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/parcelsapp.png
layout: provider
modified: '2026-07-11'
name: Parcels App
nav: Providers
network: true
overview: 'Parcels App publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account API, Tracking API, and Webhooks API. Tagged areas include Parcel Tracking, Shipment Status, Package Tracking, Logistics, and Shipping.


  Parcels App''s developer surface includes documentation, developer portal, pricing, engineering blog, and 7 more developer resources.'
plans:
- name: Parcelsapp Plans Pricing
  plan_count: 4
  slug: parcelsapp-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 4
  name: Parcelsapp Rate Limits
  slug: parcelsapp-rate-limits
score:
  band: thin
  composite: 39.9
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 52.2
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Parcelsapp Domain Security
  slug: parcelsapp-domain-security
  summary_line: TLSv1.2 · DMARC
slug: parcelsapp
tags:
- Parcel Tracking
- Shipment Status
- Package Tracking
- Logistics
- Shipping
- Carriers
website: https://parcelsapp.com
---

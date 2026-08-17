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
    agentic_access: derived
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
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Parcelperform Agentic Access
  operation_count: 13
  slug: parcelperform-agentic-access
  summary_line: 13 operations · 7 acting
api_count: 7
apis:
- description: Delivery-experience performance metrics behind the Analyze product. Entirely MODELED - no public reference page found.
  name: Parcel Perform Analytics API
  slug: parcelperform-analytics-api
- description: OAuth2 client-credentials token issuance. CONFIRMED path.
  name: Parcel Perform Authentication API
  slug: parcelperform-authentication-api
- description: Carrier/courier reference data. Entirely MODELED - no public reference page found.
  name: Parcel Perform Couriers API
  slug: parcelperform-couriers-api
- description: Create returns and return shipments. CONFIRMED operations; MODELED paths/schemas.
  name: Parcel Perform Returns API
  slug: parcelperform-returns-api
- description: Create, retrieve, list, and update shipments. CONFIRMED operations; MODELED paths/schemas.
  name: Parcel Perform Shipments API
  slug: parcelperform-shipments-api
- description: Normalized carrier tracking event timeline. CONFIRMED operations; MODELED paths/schemas.
  name: Parcel Perform Tracking Events API
  slug: parcelperform-tracking-events-api
- description: Outgoing webhook subscriptions for tracking updates. CONFIRMED operations; MODELED paths/schemas.
  name: Parcel Perform Webhooks API
  slug: parcelperform-webhooks-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Parcel Perform Analytics API
  slug: open-parcelperform-analytics-api
- collection_type: open
  name: Parcel Perform Analytics Authentication API
  slug: open-parcelperform-authentication-api
- collection_type: open
  name: Parcel Perform Analytics Couriers API
  slug: open-parcelperform-couriers-api
- collection_type: open
  name: Parcel Perform Analytics Returns API
  slug: open-parcelperform-returns-api
- collection_type: open
  name: Parcel Perform Analytics Shipments API
  slug: open-parcelperform-shipments-api
- collection_type: open
  name: Parcel Perform Analytics Tracking Events API
  slug: open-parcelperform-tracking-events-api
- collection_type: open
  name: Parcel Perform Analytics Webhooks API
  slug: open-parcelperform-webhooks-api
- collection_type: open
  name: Parcel Perform API
  slug: open-parcelperform
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/parcelperform-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/parcelperform-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parcelperform-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/parcelperform-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ParcelPerform
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/parcel-perform
- group: company
  title: ''
  type: Website
  url: https://www.parcelperform.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.parcelperform.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/parcelperform-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/parcelperform-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/parcelperform-finops.yml
created: '2026-07-03'
description: Parcel Perform is a Singapore-headquartered Data & Delivery Experience Platform that aggregates real-time tracking data across hundreds of carriers worldwide into one standardized event model, then layers post-purchase tracking pages, proactive notifications, logistics performance analytics, and returns management on top. The Parcel Perform API (developer portal at developer.parcelperform.com) lets merchants and platforms create and retrieve shipments and their tracking events, manage returns, and receive outgoing webhooks for tracking-status changes, authenticated with OAuth2 client-credentials bearer tokens.
finops:
- name: Parcelperform Finops
  service_category: Logistics and Delivery Experience
  slug: parcelperform-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/parcelperform.png
layout: provider
modified: '2026-07-03'
name: Parcel Perform
nav: Providers
network: true
overview: 'Parcel Perform publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Authentication API, Couriers API, and 4 more. Tagged areas include Logistics, Shipment Tracking, Post-Purchase, Delivery Experience, and Returns.


  Parcel Perform''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Parcelperform Plans Pricing
  plan_count: 1
  slug: parcelperform-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 3
  name: Parcelperform Rate Limits
  slug: parcelperform-rate-limits
score:
  band: thin
  composite: 37.2
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 61.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/parcelperform/refs/heads/main/screenshots/parcelperform-2026-08-07T191537.png
security:
- kind: authentication
  name: Parcelperform Authentication
  slug: parcelperform-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Parcelperform Domain Security
  slug: parcelperform-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Parcelperform Vulnerability Disclosure
  slug: parcelperform-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: parcelperform
tags:
- Logistics
- Shipment Tracking
- Post-Purchase
- Delivery Experience
- Returns
- E-Commerce
website: https://www.parcelperform.com/
---

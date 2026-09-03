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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Parcelsapp Agentic Access
  operation_count: 4
  slug: parcelsapp-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 1
apis:
- baseURL: https://parcelsapp.com/api/v3
  baseurl_source: declared
  description: Subscription usage and account limits
  name: Parcels App Account API
  slug: parcelsapp-account-api
- baseURL: https://parcelsapp.com/api/v3
  baseurl_source: declared
  description: Create tracking requests and read results
  name: Parcels App Tracking API
  slug: parcelsapp-tracking-api
- baseURL: https://parcelsapp.com/api/v3
  baseurl_source: declared
  description: Callbacks sent to your `webhookUrl` when tracking progresses or completes. Pass `webhookUrl` in `POST /shipments/tracking`; Parcels sends JSON `POST` requests to that URL.
  name: Parcels App Webhooks API
  slug: parcelsapp-webhooks-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Parcels Account API
  slug: open-parcelsapp-account-api
- collection_type: open
  name: Parcels Account Tracking API
  slug: open-parcelsapp-tracking-api
- collection_type: open
  name: Parcels Account Webhooks API
  slug: open-parcelsapp-webhooks-api
- collection_type: open
  name: Parcels App Tracking API
  slug: open-parcelsapp
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/parcelsapp-capability-edges.yml
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


  Parcels App''s developer surface includes documentation, developer portal, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Parcelsapp Plans Pricing
  plan_count: 4
  slug: parcelsapp-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 4
  name: Parcelsapp Rate Limits
  slug: parcelsapp-rate-limits
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 52.4
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 13.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/parcelsapp/refs/heads/main/screenshots/parcelsapp-2026-08-07T191439.png
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

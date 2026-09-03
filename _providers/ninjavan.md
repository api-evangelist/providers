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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Ninjavan Agentic Access
  operation_count: 12
  slug: ninjavan-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.ninjavan.co/{countryCode}
  baseurl_source: declared
  description: OAuth2 client-credentials token issuance.
  name: Ninja Van OAuth API API
  slug: ninjavan-oauth-api-api
- baseURL: https://api.ninjavan.co/{countryCode}
  baseurl_source: declared
  description: Create and cancel delivery orders and generate waybills.
  name: Ninja Van Order API API
  slug: ninjavan-order-api-api
- baseURL: https://api.ninjavan.co/{countryCode}
  baseurl_source: declared
  description: Ninja Point pick-up / drop-off locations and shipper drop-off.
  name: Ninja Van PUDO API API
  slug: ninjavan-pudo-api-api
- baseURL: https://api.ninjavan.co/{countryCode}
  baseurl_source: declared
  description: Estimate shipping price.
  name: Ninja Van Tariff API API
  slug: ninjavan-tariff-api-api
- baseURL: https://api.ninjavan.co/{countryCode}
  baseurl_source: declared
  description: Pull tracking events for parcels.
  name: Ninja Van Tracking API API
  slug: ninjavan-tracking-api-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ninja Van API (ninjaAPI) OAuth API API
  slug: open-ninjavan-oauth-api-api
- collection_type: open
  name: Ninja Van API (ninjaAPI) OAuth API Order API API
  slug: open-ninjavan-order-api-api
- collection_type: open
  name: Ninja Van API (ninjaAPI) OAuth API PUDO API API
  slug: open-ninjavan-pudo-api-api
- collection_type: open
  name: Ninja Van API (ninjaAPI) OAuth API Tariff API API
  slug: open-ninjavan-tariff-api-api
- collection_type: open
  name: Ninja Van API (ninjaAPI) OAuth API Tracking API API
  slug: open-ninjavan-tracking-api-api
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
overview: 'Ninja Van publishes 5 APIs on the [APIs.io](https://apis.io/) network, including OAuth API API, Order API API, PUDO API API, and 2 more. Tagged areas include Logistics, Last Mile Delivery, Shipping, Southeast Asia, and Parcels.


  Ninja Van''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Ninjavan Plans Pricing
  plan_count: 3
  slug: ninjavan-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Ninjavan Rate Limits
  slug: ninjavan-rate-limits
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 14.0
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 29.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ninjavan/refs/heads/main/screenshots/ninjavan-2026-08-07T185328.png
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
- Last Mile Delivery
- Shipping
- Southeast Asia
- Parcels
- Tracking
- Fulfillment
- E-commerce Logistics
- Waybill
- Software-as-a-Service
website: https://www.ninjavan.co/en-sg
---

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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.3
  scored_at: '2026-09-20'
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
  name: Ninja Van OAuth API
  slug: ninjavan-oauth-api-api
- baseURL: https://api.ninjavan.co/{countryCode}
  baseurl_source: declared
  description: Create and cancel delivery orders and generate waybills.
  name: Ninja Van Order API
  slug: ninjavan-order-api-api
- baseURL: https://api.ninjavan.co/{countryCode}
  baseurl_source: declared
  description: Ninja Point pick-up / drop-off locations and shipper drop-off.
  name: Ninja Van PUDO API
  slug: ninjavan-pudo-api-api
- baseURL: https://api.ninjavan.co/{countryCode}
  baseurl_source: declared
  description: Estimate shipping price.
  name: Ninja Van Tariff API
  slug: ninjavan-tariff-api-api
- baseURL: https://api.ninjavan.co/{countryCode}
  baseurl_source: declared
  description: Pull tracking events for parcels.
  name: Ninja Van Tracking API
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
  href: https://raw.githubusercontent.com/api-evangelist/ninjavan/refs/heads/main/agentic-access/ninjavan-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ninjavan-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ninjavan/refs/heads/main/security/ninjavan-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ninjavan-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ninjavan/refs/heads/main/authentication/ninjavan-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/ninjavan/refs/heads/main/plans/ninjavan-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ninjavan-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ninjavan/refs/heads/main/rate-limits/ninjavan-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ninjavan-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ninjavan/refs/heads/main/finops/ninjavan-finops.yml
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
modified: '2026-09-16'
name: Ninja Van
nav: Providers
network: true
overview: 'Ninja Van publishes 5 APIs on the [APIs.io](https://apis.io/) network, including OAuth API, Order API, PUDO API, and 2 more. Tagged areas include Logistics, Last Mile Delivery, Shipping, Southeast Asia, and Parcel.


  Ninja Van''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Ninjavan Plans Pricing
  plan_count: 3
  slug: ninjavan-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 4
  name: Ninjavan Rate Limits
  slug: ninjavan-rate-limits
score:
  band: thin
  composite: 38.6
  coverage:
    artifact_dirs: 13
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 56.2
    developer_ergonomics: 32.1
    discoverability: 68.5
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 38.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
- Parcel
- Tracking
- Fulfillment
- E-commerce Logistics
- Waybill
- Software-as-a-Service
website: https://www.ninjavan.co/en-sg
---

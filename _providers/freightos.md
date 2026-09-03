---
access_model:
  confidence: medium
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 6
apis:
- description: Public marketplace quote endpoint returning freight price ranges (min/max), transit-time ranges, and shipping mode (air, LCL, FCL, trucking) for a given origin, destination, weight, and load type. Sup
  name: Freightos Shipping Calculator API
  slug: freightos-shipping-calculator-api
- description: Developer-portal JSON API that returns instant freight estimates for air, ocean, and trucking across core global import/export lanes, drawn from Freightos Marketplace live rates and a large historical
  name: Freightos Freight Rate Estimator API
  slug: freightos-freight-rate-estimator-api
- description: HS-code classification API that takes a free-text commodity description and returns a ranked list of matching Harmonized System (HS) codes with match probabilities and descriptions, supporting duty es
  name: Freightos Duties API
  slug: freightos-duties-api
- description: Emissions API returning EU-standard CO2 estimates across air, ocean, and trucking modes for a shipment leg or route, for carbon reporting and greener routing decisions. Documented on the developer por
  name: Freightos CO2 Calculation API
  slug: freightos-co2-calculation-api
- description: Partner-gated booking surface behind WebCargo by Freightos, giving freight forwarders and carriers live, bookable air/ocean capacity and real-time eBooking across 55+ carriers (Lufthansa, Air France K
  name: WebCargo Booking API
  slug: freightos-webcargo-booking-api
- description: Partner-gated shipment lifecycle surface for managing shipments across providers - documentation management, messaging, milestone tracking, and shipment status updates - typically integrated into a fo
  name: Freightos Shipment Management and Tracking API
  slug: freightos-shipment-tracking-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freightos-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/freightos
- group: company
  title: ''
  type: Website
  url: https://www.freightos.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.freightos.com/apis
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Freightos
- group: commercial
  title: ''
  type: Plans
  url: plans/freightos-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/freightos-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/freightos-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.freightos.com/blog/
created: '2026-07-05'
description: Freightos (NASDAQ CRGO) operates a global freight booking marketplace and, through WebCargo by Freightos, a rate-management and eBooking platform used by freight forwarders and carriers to price and book air, ocean, and trucking shipments in real time across 55+ carriers. Freightos publishes a developer portal (developers.freightos.com / developer.freightos.com) with freight-rate estimation, HS-code duties classification, and CO2 emissions APIs, plus the public Shipping Calculator on the marketplace. Bookable live rates, eBooking, and shipment tracking are offered to forwarder, carrier, and TMS/ERP partners under commercial agreements. Most developer-portal APIs are documented as beta and provided as-is, and full access is provisioned per partner rather than via open self-service signup.
finops:
- name: Freightos Finops
  service_category: Logistics and Freight
  slug: freightos-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/freightos.png
layout: provider
modified: '2026-07-05'
name: Freightos
nav: Providers
network: true
overview: 'Freightos publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Freight, Logistics, Shipping, Freight Marketplace, and Air Cargo.


  Freightos'' developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Freightos Plans Pricing
  plan_count: 3
  slug: freightos-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Freightos Rate Limits
  slug: freightos-rate-limits
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 6
    catalog_gap: 53.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 20.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/freightos/refs/heads/main/screenshots/freightos-2026-07-25T215155.png
security:
- kind: domain-security
  name: Freightos Domain Security
  slug: freightos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: freightos
tags:
- Freight
- Logistics
- Shipping
- Freight Marketplace
- Air Cargo
- Ocean Freight
- Rates
- Booking
website: https://www.freightos.com/
---

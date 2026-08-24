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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 4
apis:
- description: REST API for locating and querying Electrify America charging stations. Enables partners and OEM integrators to search for stations by geographic area or coordinates, retrieve station details (address
  name: Electrify America Stations API
  slug: stations-api
- description: Real-time charger availability API that returns live connector status (available, in-use, faulted, offline) for individual charging stations and EVSE units. Used by automotive OEM in-vehicle navigatio
  name: Electrify America Availability API
  slug: availability-api
- description: API providing per-session and per-kWh pricing data for Electrify America charging stations. Supports time-of-use (TOU) pricing retrieval so partners and in-vehicle systems can display accurate session
  name: Electrify America Pricing API
  slug: pricing-api
- description: API for initiating, monitoring, and retrieving data for EV charging sessions. Enables partner applications to start and stop charging sessions, poll live session telemetry (energy delivered, duration,
  name: Electrify America Sessions API
  slug: sessions-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/electrify-america-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.electrifyamerica.com
- group: start
  title: ''
  type: Portal
  url: https://developer.electrifyamerica.com
- group: start
  title: ''
  type: Signup
  url: https://developer.electrifyamerica.com
- group: other
  title: Electrify America iOS App
  type: MobileApp
  url: https://apps.apple.com/us/app/electrify-america/id1458030456
- group: other
  title: Electrify America Android App
  type: MobileApp
  url: https://play.google.com/store/apps/details?id=com.ea.evowner
- group: commercial
  title: ''
  type: Pricing
  url: https://www.electrifyamerica.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://cloud.email.electrifyamerica.com/network-and-planned-maintenance
- group: company
  title: ''
  type: Newsroom
  url: https://media.electrifyamerica.com/
- group: operate
  title: ''
  type: FAQ
  url: https://www.electrifyamerica.com/mobile-faq/
- group: other
  title: ''
  type: StationLocator
  url: https://www.electrifyamerica.com/locate-charger/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/electrify-america
- group: company
  title: ''
  type: Twitter
  url: https://x.com/ElectrifyAm
- group: commercial
  title: ''
  type: Plans
  url: plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/finops.yml
created: '2026-06-13'
description: Electrify America is the largest open EV fast-charging network in the United States, operating more than 5,600 DC fast chargers at over 1,080 locations across the US and Canada. Subsidiary of Volkswagen Group of America, the network offers charging speeds up to 350 kW and supports CCS, CHAdeMO, and NACS connectors. Electrify America provides REST APIs through a partner developer portal that enables automotive OEMs and enterprise integrators to locate charging stations, check real-time charger availability, retrieve session pricing, and manage charging sessions. Authentication is handled via OAuth2 / Auth0. A consumer-facing mobile app (iOS/Android) provides pass-based subscription plans (Pass and Pass+) with per-kWh pricing, and the Plug&Charge standard (ISO 15118) is supported at all stations for certificate-based auto-authentication.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/electrify-america.png
layout: provider
modified: '2026-06-13'
name: Electrify America
nav: Providers
network: true
overview: 'Electrify America publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Electric Vehicles, EV Charging, Charging Stations, DC Fast Charging, and Plug and Charge.


  Electrify America''s developer surface includes developer portal, signup flow, pricing, FAQ, and 12 more developer resources.'
plans:
- name: Plans
  plan_count: 4
  slug: plans
random_paper: 12
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: emerging
  composite: 22.3
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 22.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/electrify-america/refs/heads/main/screenshots/electrify-america-2026-06-20T180553.png
security:
- kind: domain-security
  name: Electrify America Domain Security
  slug: electrify-america-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: electrify-america
tags:
- Electric Vehicles
- EV Charging
- Charging Stations
- DC Fast Charging
- Plug and Charge
- Automotive
- Energy
- Transportation
- Mobility
website: https://www.electrifyamerica.com
---

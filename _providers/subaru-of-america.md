---
access_model:
  confidence: medium
  label: Paid (free trial)
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: true
  try_now: false
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
  scored_at: '2026-09-02'
api_count: 7
apis:
- description: Private connected-vehicle backend (formerly branded Subaru STARLINK) that powers the MySubaru mobile app and owner portal. Supports remote lock / unlock, remote engine start with climate control, vehi
  name: MySubaru Connected Services API
  slug: mysubaru-connected-services-api
- description: Plan tier surface (2026+ model years) covering SOS Emergency Assistance, Enhanced Roadside Assistance, Locate Vehicle, plus the premium remote engine start and climate control add-ons. Subscription, p
  name: MySubaru Companion Plan API
  slug: mysubaru-companion-plan-api
- description: Plan tier surface (2016-2025 model years) covering safety and security protection services with an upper tier adding Remote Engine Start and Remote Vehicle Locate. Same private backend as MySubaru Con
  name: MySubaru Safety & Security Plan API
  slug: mysubaru-safety-security-plan-api
- description: In-vehicle 4G LTE Wi-Fi hotspot service delivered through a partnership with AT&T. Activation, plan management, and data billing are handled by AT&T's connected-car backend, not by Subaru. No Subaru-s
  name: Subaru AT&T Wi-Fi Hotspot API
  slug: subaru-att-wifi-hotspot-api
- description: In-vehicle satellite and streaming audio service delivered through SiriusXM. Trial activation, subscription, and entitlements are managed by SiriusXM. Subaru does not expose a developer API for this s
  name: Subaru SiriusXM API
  slug: subaru-siriusxm-api
- description: Web-facing dealer locator and inventory search powering subaru.com. Backed by an internal HTTP service; not documented or offered as a public developer API.
  name: Subaru Dealer Locator API
  slug: subaru-dealer-locator-api
- description: VIN-based recall lookup exposed through subaru.com. Backed by an internal service that aggregates Subaru and NHTSA recall data; not offered as a public API. NHTSA itself provides a public VIN recall A
  name: Subaru Recall Lookup API
  slug: subaru-recall-lookup-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/subaru-of-america-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.subaru.com/
- group: start
  title: ''
  type: Owner Portal
  url: https://www.mysubaru.com/
- group: company
  title: ''
  type: About
  url: https://www.subaru.com/our-company/about-us.html
- group: other
  title: ''
  type: Connected Services
  url: https://www.subaru.com/owners/connected-services.html
- group: other
  title: ''
  type: STARLINK / MySubaru
  url: https://www.subaru.com/owners/starlink.html
- group: operate
  title: ''
  type: Support
  url: https://www.subaru.com/customer-support.html
- group: other
  title: ''
  type: Vehicle Recalls
  url: https://www.subaru.com/owners/vehicle-recalls.html
- group: company
  title: ''
  type: Press Room
  url: https://media.subaru.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/subaru-of-america
- group: other
  title: ''
  type: X
  url: https://x.com/subaru_usa
- group: commercial
  title: ''
  type: Plans Pricing
  url: plans/subaru-of-america-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/subaru-of-america-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/subaru-of-america-finops.yml
created: '2026-05-23'
description: Subaru of America, Inc. is the United States subsidiary of Subaru Corporation (Japan), headquartered in Camden, New Jersey. SOA sells, services, and supports the Subaru lineup through more than 600 U.S. dealers and operates the MySubaru / STARLINK connected-vehicle platform that powers the MySubaru mobile app, owner portal, remote vehicle commands, safety and security services, in-vehicle Wi-Fi, and dealer integration. None of these surfaces are exposed as a public developer API; all known interfaces are private, OEM-internal, or partner-only.
finops:
- name: Subaru Of America Finops
  service_category: Connected Vehicle / Telematics
  slug: subaru-of-america-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/subaru-of-america.png
layout: provider
modified: '2026-05-23'
name: Subaru of America
nav: Providers
network: true
overview: 'Subaru of America publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automobiles, Automotive, Cars, Vehicles, and Connected Vehicle.


  Subaru of America''s developer surface includes support and 13 more developer resources.'
plans:
- name: Subaru Of America Plans Pricing
  plan_count: 5
  slug: subaru-of-america-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Subaru Of America Rate Limits
  slug: subaru-of-america-rate-limits
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 5
    catalog_gap: 53.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 19.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/subaru-of-america/refs/heads/main/screenshots/subaru-of-america-2026-06-20T194631.png
security:
- kind: domain-security
  name: Subaru Of America Domain Security
  slug: subaru-of-america-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: subaru-of-america
tags:
- Automobiles
- Automotive
- Cars
- Vehicles
- Connected Vehicle
- Telematics
- OEM
website: https://www.subaru.com/
---

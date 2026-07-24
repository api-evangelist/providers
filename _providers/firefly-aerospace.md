---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - finops
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 5
apis:
- description: 'Alpha is Firefly''s operational small-lift orbital launch vehicle in the ~1,000 kg class, serving dedicated and rideshare customers. This is an informational product surface; Firefly exposes no public '
  name: Firefly Alpha Launch
  slug: firefly-alpha-launch
- description: Eclipse (formerly the Medium Launch Vehicle, MLV) is Firefly's medium-lift, reusable launch vehicle co-developed with Northrop Grumman, targeting roughly 16,000 kg to orbit. This is an informational p
  name: Firefly Eclipse Launch
  slug: firefly-eclipse-launch
- description: Blue Ghost is Firefly's lunar lander for delivering and hosting payloads on the lunar surface, including NASA Commercial Lunar Payload Services (CLPS) task orders. This is an informational mission/ser
  name: Firefly Blue Ghost Lunar Lander
  slug: firefly-blue-ghost-lunar
- description: Elytra is Firefly's multi-mission orbital vehicle (Dawn, Dusk, and Dark configurations) providing in-space maneuverability, hosting, and servicing, and is the platform for the Ocula commercial lunar i
  name: Firefly Elytra Orbital Vehicle
  slug: firefly-elytra-orbital
- description: Firefly's "Book A Ride" rideshare and payload booking experience lets prospective customers inquire about available flights and orbits. It is a sales inquiry / web form workflow, not a programmatic AP
  name: Firefly Rideshare and Payload Booking
  slug: firefly-rideshare-payload
artifact_total: 10
collections:
- collection_type: open
  name: Firefly Aerospace
  slug: open-firefly-aerospace
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/firefly-aerospace-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/firefly-aerospace
- group: company
  title: ''
  type: Website
  url: https://fireflyspace.com/
- group: docs
  title: ''
  type: Documentation
  url: https://fireflyspace.com/wp-content/uploads/2025/07/Alpha-PUG-5.2.pdf
- group: commercial
  title: ''
  type: Plans
  url: plans/firefly-aerospace-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/firefly-aerospace-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/firefly-aerospace-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://fireflyspace.com/news/
created: '2026-06-20'
description: Firefly Aerospace is an end-to-end space transportation company building the Alpha small-lift rocket, the Eclipse (formerly MLV) medium-lift vehicle, the Blue Ghost lunar lander, and the Elytra orbital vehicle (with the Ocula lunar imaging service). Firefly sells launch, lunar delivery, and on-orbit services through sales and payload-user-guide channels; it does not publish a public developer API.
finops:
- name: Firefly Aerospace Finops
  service_category: Space and Launch Services
  slug: firefly-aerospace-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/firefly-aerospace.png
layout: provider
modified: '2026-06-20'
name: Firefly Aerospace
nav: Providers
network: true
overview: 'Firefly Aerospace publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Space, Aerospace, Launch, Lunar, and Spacecraft.


  Firefly Aerospace''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Firefly Aerospace Plans Pricing
  plan_count: 0
  slug: firefly-aerospace-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Firefly Aerospace Rate Limits
  slug: firefly-aerospace-rate-limits
score:
  band: minimal
  composite: 10.5
  delta: 0.0
  facets:
    commercial_clarity: 7.9
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/firefly-aerospace/refs/heads/main/screenshots/firefly-aerospace-2026-06-20T181231.png
security:
- kind: domain-security
  name: Firefly Aerospace Domain Security
  slug: firefly-aerospace-domain-security
  summary_line: TLSv1.3 · DMARC
slug: firefly-aerospace
tags:
- Space
- Aerospace
- Launch
- Lunar
- Spacecraft
website: https://fireflyspace.com/
---

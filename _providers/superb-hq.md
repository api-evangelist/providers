---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Logical capability for creating and managing restaurant reservations - availability, floor and table assignment, booking creation and status changes. Superb surfaces this to guests through a hosted bo
  name: Superb Reservations API
  slug: superb-hq-reservations-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/superb-hq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.superbexperience.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/superbexperience
- group: docs
  title: ''
  type: Documentation
  url: https://helpcenter.superbexperience.com/en/
- group: company
  title: ''
  type: Partners
  url: https://partner.superbexperience.com/
- group: start
  title: ''
  type: SignUp
  url: https://etch.superbexperience.com/reserve/experience
- group: commercial
  title: ''
  type: Plans
  url: plans/superb-hq-plans-pricing.yml
- group: other
  title: ''
  type: ProductPage
  url: https://helpcenter.superbexperience.com/en/article/how-to-use-booking-statuses-ne8q0n/
created: '2026-07-05'
description: Superb is a Denmark-based all-in-one Guest Experience Management (GXM) platform for restaurants, cafes and bars, bringing reservations, point of sale, payments, gift cards, online takeaway, guest CRM and marketing together in a single system. Superb does not publish a self-serve, documented public developer API. Guest bookings are taken through a hosted reservation widget, and third-party systems connect through Superb's catalog of pre-built connectors (accounting, payments, staff and stock management, marketing) plus a partner portal at partner.superbexperience.com. Any programmatic reservation, guest, booking or CRM access is partner-gated and arranged directly with Superb. The APIs listed below are logical capability groupings modeled from Superb's public product and help-center material - they are marked endpointsModeled because Superb does not publish endpoint-level REST documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/superb-hq.png
layout: provider
modified: '2026-07-25'
name: Superb
nav: Providers
network: true
overview: 'Superb publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Restaurants, Reservations, Hospitality, Guest Experience, and GXM.


  Superb''s developer surface includes documentation, signup flow, and 6 more developer resources.'
plans:
- name: Superb Hq Plans Pricing
  plan_count: 3
  slug: superb-hq-plans-pricing
random_paper: 25
score:
  band: minimal
  composite: 10.7
  delta: -4.8
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Superb Hq Domain Security
  slug: superb-hq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: superb-hq
tags:
- Restaurants
- Reservations
- Hospitality
- Guest Experience
- GXM
- Point of Sale
- CRM
- Payments
website: https://www.superbexperience.com/
---

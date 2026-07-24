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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 4
apis:
- description: Logical capability for creating and managing restaurant reservations - availability, floor and table assignment, booking creation and status changes. Superb surfaces this to guests through a hosted bo
  name: Superb Reservations API
  slug: superb-hq-reservations-api
- description: Logical capability for the booking lifecycle - confirmations, reminders, booking statuses, no-show handling and prepayment or deposit flows. Managed inside the Superb apps and communicated to guests o
  name: Superb Bookings API
  slug: superb-hq-bookings-api
- description: Logical capability for guest profiles and the guest database - contact details, visit history, notes, tags, spend and preferences that power Superb's Guest Experience Management. Exposed through the S
  name: Superb Guests API
  slug: superb-hq-guests-api
- description: Logical capability for guest CRM and email marketing - segments, campaigns and automated messaging built on the guest database. Delivered as an in-product feature and via pre-built marketing connector
  name: Superb CRM and Marketing API
  slug: superb-hq-crm-marketing-api
artifact_total: 6
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
created: '2026-07-05'
description: Superb is a Denmark-based all-in-one Guest Experience Management (GXM) platform for restaurants, cafes and bars, bringing reservations, point of sale, payments, gift cards, online takeaway, guest CRM and marketing together in a single system. Superb does not publish a self-serve, documented public developer API. Guest bookings are taken through a hosted reservation widget, and third-party systems connect through Superb's catalog of pre-built connectors (accounting, payments, staff and stock management, marketing) plus a partner portal at partner.superbexperience.com. Any programmatic reservation, guest, booking or CRM access is partner-gated and arranged directly with Superb. The APIs listed below are logical capability groupings modeled from Superb's public product and help-center material - they are marked endpointsModeled because Superb does not publish endpoint-level REST documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/superb-hq.png
layout: provider
modified: '2026-07-05'
name: Superb
nav: Providers
network: true
overview: 'Superb publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Restaurants, Reservations, Hospitality, Guest Experience, and GXM.


  Superb''s developer surface includes documentation, signup flow, and 5 more developer resources.'
plans:
- name: Superb Hq Plans Pricing
  plan_count: 3
  slug: superb-hq-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 18.5
  delta: -0.9
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 19.4
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-23'
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

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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 8
apis:
- description: Access, create, and edit member records - the central pivot of the Glofox data model, spanning leads, active members, and ex-members (soft-deleted via an active flag rather than hard-deleted). The doc
  name: Glofox Members API
  slug: glofox-members-api
- description: Manage Plans (the terms, duration, and pricing of a service offering), a member's Membership against a given Plan, and Credits - the units of value a member redeems to book Classes, Appointments, or F
  name: Glofox Memberships, Plans & Credits API
  slug: glofox-memberships-plans-credits-api
- description: Scheduled Events - classes, appointments, and facility slots - with capacity and attendance tracking that members book against within a given Location/Branch.
  name: Glofox Classes & Events API
  slug: glofox-classes-events-api
- description: Create and manage a member's booking - the record of intent to attend a scheduled Event - governed by available Credits and Event capacity. Documented end to end in the portal's "Book" integration flo
  name: Glofox Bookings API
  slug: glofox-bookings-api
- description: 'Purchase products and plans and process payments through the Payment Collector flow - a hosted, domain-authorized iframe kept out of direct API credential exposure - covering transaction handling for '
  name: Glofox Payments & Purchases API
  slug: glofox-payments-purchases-api
- description: Capture prospective members as leads and convert them into paying members through the "Lead Sale" integration flow documented in the developer portal.
  name: Glofox Leads API
  slug: glofox-leads-api
- description: Locations/Branches are the physical studios or gyms that contextualize Plans, Events, and Bookings. Every API request is scoped to a branch via the required x-glofox-branch-id header.
  name: Glofox Branches (Locations) API
  slug: glofox-branches-locations-api
- description: Outbound change-data-capture webhooks - an HMAC-SHA256-signed Member Webhook (MEMBER_CREATED, MEMBER_UPDATED; deletes are soft via an active flag, no MEMBER_DELETED event) and an Access Webhook that k
  name: Glofox CDC Webhooks
  slug: glofox-cdc-webhooks
artifact_total: 13
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/glofox-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/glofox-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/glofoxinc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/abcglofox
- group: company
  title: ''
  type: Website
  url: https://www.glofox.com
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs-plat.aws.glofox.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/glofox-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/glofox-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/glofox-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.glofox.com/feed/
created: '2026-07-03'
description: Glofox is boutique gym and fitness studio management software - member management, class/appointment scheduling, bookings, memberships, credits, payments, and lead conversion for studios, gyms, and fitness franchises. Glofox was acquired by ABC Fitness Solutions in August 2022 and now operates as the ABC Glofox business unit within ABC's fitness technology platform. Glofox publishes a partner/developer REST API (the "ABC Glofox API Developer Portal") covering members, memberships, plans, credits, classes, bookings, purchases, branches, and leads, plus CDC (change data capture) webhooks for member and access-control events. Access is gated - integrators request x-api-key and x-glofox-api-token credentials by email before they can call the API.
finops:
- name: Glofox Finops
  service_category: Vertical SaaS - Fitness & Studio Management
  slug: glofox-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/glofox.png
layout: provider
modified: '2026-07-03'
name: Glofox
nav: Providers
network: true
overview: 'Glofox publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fitness, Gym Management, Boutique Fitness, Class Scheduling, and Bookings.


  Glofox''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Glofox Plans Pricing
  plan_count: 3
  slug: glofox-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Glofox Rate Limits
  slug: glofox-rate-limits
score:
  band: emerging
  composite: 21.8
  delta: -2.1
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 23.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/glofox/refs/heads/main/screenshots/glofox-2026-07-25T215925.png
security:
- kind: domain-security
  name: Glofox Domain Security
  slug: glofox-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Glofox Trust Center
  slug: glofox-trust-center
  summary_line: ISO 27001, PCI DSS, GDPR
slug: glofox
tags:
- Fitness
- Gym Management
- Boutique Fitness
- Class Scheduling
- Bookings
- Memberships
- Leads
- ABC Fitness
- CDC Webhooks
website: https://www.glofox.com
---

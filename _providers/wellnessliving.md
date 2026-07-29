---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 16
  human_in_the_loop: 1
  name: Wellnessliving Agentic Access
  operation_count: 55
  slug: wellnessliving-agentic-access
  summary_line: 55 operations · 16 acting · 1 human-in-the-loop
api_count: 15
apis:
- description: The Appointments API from WellnessLiving — 4 operation(s) for appointments.
  name: WellnessLiving Appointments API
  slug: wellnessliving-appointments-api
- description: The Authentication API from WellnessLiving — 4 operation(s) for authentication.
  name: WellnessLiving Authentication API
  slug: wellnessliving-authentication-api
- description: The Booking API from WellnessLiving — 4 operation(s) for booking.
  name: WellnessLiving Booking API
  slug: wellnessliving-booking-api
- description: The Business API from WellnessLiving — 4 operation(s) for business.
  name: WellnessLiving Business API
  slug: wellnessliving-business-api
- description: The Catalog API from WellnessLiving — 4 operation(s) for catalog.
  name: WellnessLiving Catalog API
  slug: wellnessliving-catalog-api
- description: The Classes API from WellnessLiving — 4 operation(s) for classes.
  name: WellnessLiving Classes API
  slug: wellnessliving-classes-api
- description: The Clients API from WellnessLiving — 4 operation(s) for clients.
  name: WellnessLiving Clients API
  slug: wellnessliving-clients-api
- description: The Locations API from WellnessLiving — 4 operation(s) for locations.
  name: WellnessLiving Locations API
  slug: wellnessliving-locations-api
- description: The Payments API from WellnessLiving — 4 operation(s) for payments.
  name: WellnessLiving Payments API
  slug: wellnessliving-payments-api
- description: The Promotions API from WellnessLiving — 4 operation(s) for promotions.
  name: WellnessLiving Promotions API
  slug: wellnessliving-promotions-api
- description: The Reports API from WellnessLiving — 3 operation(s) for reports.
  name: WellnessLiving Reports API
  slug: wellnessliving-reports-api
- description: The Reviews API from WellnessLiving — 3 operation(s) for reviews.
  name: WellnessLiving Reviews API
  slug: wellnessliving-reviews-api
- description: The Rewards API from WellnessLiving — 4 operation(s) for rewards.
  name: WellnessLiving Rewards API
  slug: wellnessliving-rewards-api
- description: The Staff API from WellnessLiving — 4 operation(s) for staff.
  name: WellnessLiving Staff API
  slug: wellnessliving-staff-api
- description: The WebSocket API from WellnessLiving — 1 operation(s) for websocket.
  name: WellnessLiving WebSocket API
  slug: wellnessliving-websocket-api
artifact_total: 24
asyncapis:
- description: WellnessLiving's own web and mobile clients (Achieve, Elevate, the backend console) receive live updates - report-generation progress, visit/attendance status changes, and messenger chat messages - ov
  name: WellnessLiving Real-Time Notifications (WebSocket)
  slug: wellnessliving-asyncapi
collections:
- collection_type: open
  name: WellnessLiving API
  slug: open-wellnessliving
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wellnessliving-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wellnessliving-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wellnessliving-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wellnessliving
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wellnesslivingsoftware
- group: company
  title: ''
  type: Website
  url: https://www.wellnessliving.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.wellnessliving.com/developer-portal/getting-started/introduction/
- group: commercial
  title: ''
  type: Plans
  url: plans/wellnessliving-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wellnessliving-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wellnessliving-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.wellnessliving.com/blog/feed/
created: '2026-07-03'
description: 'WellnessLiving is all-in-one business-management software for fitness studios, gyms, spas, salons, and wellness businesses - scheduling, point of sale, memberships/passes, marketing, and client engagement in one platform, serving over 10 million users worldwide. WellnessLiving publishes a real, extensive RESTful API (324+ JSON-over-HTTPS endpoints across 45+ resource areas as of the 2026-06-20 build) that powers its own Achieve client app and Elevate staff app - documented in an official public OpenAPI specification (github.com/wellnessliving/openapi) and public PHP/JavaScript SDKs (wl-sdk, wl-sdk-js) - but the API itself is partner-gated: access requires contacting a WellnessLiving Account Executive or Support, completing an API Access Questionnaire, and signing an NDA and API Agreement before the Integrations Team issues application credentials for staging and production. Core resources cover clients/members, classes and schedules, one-on-one appointments, the shared booking/checkout
  wizard, memberships and passes (Purchase Options), staff, locations, business configuration, retail sales/catalog, payments (the Thoth payment microservice), authentication, rewards/loyalty, reviews, reporting, and a channel-based real-time WebSocket notification layer.'
finops:
- name: Wellnessliving Finops
  service_category: Business Applications and SaaS
  slug: wellnessliving-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wellnessliving.png
layout: provider
modified: '2026-07-03'
name: WellnessLiving
nav: Providers
network: true
overview: 'WellnessLiving publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Appointments API, Authentication API, Booking API, and 12 more. Tagged areas include Fitness, Wellness, Spa, Business Management, and Scheduling.


  The WellnessLiving catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  WellnessLiving''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Wellnessliving Plans Pricing
  plan_count: 4
  slug: wellnessliving-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 4
  name: Wellnessliving Rate Limits
  slug: wellnessliving-rate-limits
rules:
- name: WellnessLiving API Rules
  rule_count: 2
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 1
  slug: wellnessliving-asyncapi-spectral-rules
score:
  band: developing
  composite: 44.5
  delta: -2.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 70.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 20.8
    operational_transparency: 36.8
  previous_composite: 47.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Wellnessliving Authentication
  slug: wellnessliving-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Wellnessliving Domain Security
  slug: wellnessliving-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wellnessliving
tags:
- Fitness
- Wellness
- Spa
- Business Management
- Scheduling
- Memberships
- Point of Sale
website: https://www.wellnessliving.com/
---

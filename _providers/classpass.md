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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: 'ClassPass''s named partner integration API for studios and their scheduling/booking software. Per ClassPass partner-marketing pages and integration-partner help centers (e.g. studio scheduling vendors '
  name: ClassPass Inventory API
  slug: classpass-inventory-api
- description: The client-side application shell served at developers.classpass.com (inspectable without authenticating) declares Redux state entities named cpToken, integratorSettings, specDoc, validationTests, and
  name: ClassPass Partner Certification & Token Portal
  slug: classpass-partner-certification-portal
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/classpass-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://classpass.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/classpass
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.classpass.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.classpass.com/hc/en-us/articles/360061293531-What-is-ClassPass-s-API-Access-Terms-of-Use
- group: build
  title: ''
  type: BookingIntegrations
  url: https://classpass.com/partners/classpass-booking-integrations
- group: commercial
  title: ''
  type: Plans
  url: plans/classpass-plans-pricing.yml
created: '2026-07-03'
description: ClassPass is a fitness and wellness marketplace that lets consumers book classes, gym visits, and spa/wellness experiences across a network of studios in a single app using a monthly credit subscription. On the supply side, ClassPass runs a partner integration platform - centered on a named "ClassPass Inventory API" - that lets studios and their scheduling/booking software (100+ platforms, including Mindbody, Vagaro, Zen Planner, and Eversports Manager) push live class schedules, availability, and pricing to ClassPass and receive bookings and cancellations back. The partner developer portal at developers.classpass.com requires an approved partner login (Auth0) to view the API specification document and run certification tests; ClassPass does not publish a public, unauthenticated API reference, OpenAPI file, or Postman collection. ClassPass is now part of Playlist, the group formed together with Mindbody and Booker.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/classpass.png
layout: provider
modified: '2026-07-03'
name: ClassPass
nav: Providers
network: true
overview: ClassPass publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fitness, Wellness, Class Booking, Marketplace, and Studios.
plans:
- name: Classpass Plans Pricing
  plan_count: 2
  slug: classpass-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 16.4
  delta: 3.4
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/classpass/refs/heads/main/screenshots/classpass-2026-07-25T205520.png
security:
- kind: domain-security
  name: Classpass Domain Security
  slug: classpass-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: classpass
tags:
- Fitness
- Wellness
- Class Booking
- Marketplace
- Studios
- Gyms
- Scheduling
- Partner API
website: https://classpass.com
---

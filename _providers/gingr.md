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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Gingr Agentic Access
  operation_count: 48
  slug: gingr-agentic-access
  summary_line: 48 operations · 22 acting
api_count: 9
apis:
- description: Invoices and charges.
  name: Gingr Invoices API
  slug: gingr-invoices-api
- description: Owner/client ("parent") records.
  name: Gingr Owners API
  slug: gingr-owners-api
- description: Charging and refunding cards on file, invoices, and deposits.
  name: Gingr Payments API
  slug: gingr-payments-api
- description: Pet profiles belonging to an owner.
  name: Gingr Pets API
  slug: gingr-pets-api
- description: Daily activity report cards generated for a pet's stay.
  name: Gingr Report Cards API
  slug: gingr-report-cards-api
- description: Bookings/reservations for daycare, boarding, training, and grooming.
  name: Gingr Reservations API
  slug: gingr-reservations-api
- description: Service catalog and facility configuration.
  name: Gingr Services API
  slug: gingr-services-api
- description: Pet immunization/vaccination records.
  name: Gingr Vaccinations API
  slug: gingr-vaccinations-api
- description: Managing bookings that are on the facility waitlist.
  name: Gingr Waitlist API
  slug: gingr-waitlist-api
artifact_total: 16
collections:
- collection_type: open
  name: Gingr Partner API
  slug: open-gingr
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gingr-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gingr-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gingr-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gingr-llc
- group: company
  title: ''
  type: Website
  url: https://www.gingrapp.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.gingrapp.com/hc/en-us
- group: commercial
  title: ''
  type: Plans
  url: plans/gingr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gingr-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gingr-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.gingrapp.com/blog
created: '2026-07-04'
description: Gingr is pet-care business management software for dog daycare, boarding, training, and grooming facilities, covering reservations, check-in/checkout, client and pet records, feeding and medication schedules, immunizations, report cards, point of sale, and payments. Gingr publishes a JSON:API-style Partner API (api.gingr.io, X-Api-Key header, live OpenAPI/Swagger and Postman collection at docs.gingr.io) covering owners (parents), pets, bookings/reservations, invoices and payments, immunizations, and report cards, alongside an older subdomain-scoped legacy reporting API used for read-only pulls of owners and reservations.
finops:
- name: Gingr Finops
  service_category: Vertical SaaS - Pet Care Business Management
  slug: gingr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gingr.png
layout: provider
modified: '2026-07-04'
name: Gingr
nav: Providers
network: true
overview: 'Gingr publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Invoices API, Owners API, Payments API, and 6 more. Tagged areas include Pet Care, Pet Daycare, Boarding, Grooming, and Vertical SaaS.


  Gingr''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Gingr Plans Pricing
  plan_count: 4
  slug: gingr-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 3
  name: Gingr Rate Limits
  slug: gingr-rate-limits
score:
  band: thin
  composite: 35.3
  delta: -1.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.1
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.9
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 26.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Gingr Authentication
  slug: gingr-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Gingr Domain Security
  slug: gingr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gingr
tags:
- Pet Care
- Pet Daycare
- Boarding
- Grooming
- Vertical SaaS
- Scheduling
- Payments
website: https://www.gingrapp.com
---

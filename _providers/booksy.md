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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The Booksy Public API is a partner-facing REST API for managing Booksy businesses and their booking data. It is organized around resource-oriented URLs, returns JSON, uses standard HTTP verbs and stat
  name: Booksy Public API
  slug: booksy-public-api
artifact_total: 7
asyncapis:
- description: ''
  name: Booksy Appointment Webhooks
  slug: booksy-appointment-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://booksy.com/en-us/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.booksy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.booksy.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.booksy.com/v01.html
- group: company
  title: ''
  type: Blog
  url: https://blog.booksy.com/us/
- group: operate
  title: ''
  type: Support
  url: https://help.booksy.com/hc/en-us
- group: commercial
  title: ''
  type: Pricing
  url: https://biz.booksy.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://biz.booksy.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://booksy.com/en-us/p/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://booksy.com/en-us/p/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.booksy.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.booksy.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://biz.booksy.com/whats-new
- group: auth
  title: ''
  type: Authentication
  url: authentication/booksy-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/booksy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/booksy-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/booksy-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/booksy-plans.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/booksy-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/booksy-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/booksy-appointment-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/booksy-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/booksy-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/booksy-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/booksy-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/booksy-llms.txt
created: '2026-07-31'
description: Booksy is a beauty, wellness and health services platform that pairs a consumer appointment marketplace (booksy.com) with Booksy Biz, a subscription business-management application for salons, barbershops, spas, nail studios, tattoo artists, massage therapists and other independent service providers. The platform covers online booking, calendar and staff scheduling, client records, inventory, no-show protection, digital loyalty cards, marketing tools such as Boost, reviews, and integrated card payments including a Booksy Card Reader and Tap to Pay. Booksy also operates the Booksy Public API, a partner-facing REST API documented at docs.booksy.com that exposes businesses, business categories and amenities, business and staff schedules, resources (staff and appliances), services, service variants, service categories, service and staff photos, consent forms, customers, appointments and appointment status transitions, appointment consents, reviews and review statistics, plus an
  appointment webhook. The API is versioned through an Accept header, authenticates with partner-issued RSA key pairs exchanged for short-lived JWT access tokens, and is served per country from https://<country_code>.booksy.com/public-api/<country_code>/.
image: https://cdn.prod.website-files.com/65ce807a7f0051db5b622a45/65dc8ce6b51696ab4e375751_Logo.svg
layout: provider
modified: '2026-07-31'
name: Booksy
nav: Providers
network: true
overview: 'Booksy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Beauty, Wellness, Booking, Appointments, and Scheduling.


  The Booksy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Booksy''s developer surface includes documentation, API reference, engineering blog, support, pricing, signup flow, changelog, and 19 more developer resources.'
plans:
- name: Booksy Plans
  plan_count: 2
  slug: booksy-plans
random_paper: 12
rate_limits:
- limit_count: 2
  name: Booksy Rate Limits
  slug: booksy-rate-limits
score:
  band: developing
  composite: 51.2
  coverage:
    artifact_dirs: 16
    catalog_gap: 62.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 39.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 60.5
  previous_composite: 51.2
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/booksy/refs/heads/main/screenshots/booksy-2026-08-07T162726.png
security:
- kind: authentication
  name: Booksy Authentication
  slug: booksy-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Booksy Domain Security
  slug: booksy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Booksy Trust Center
  slug: booksy-trust-center
  summary_line: trust center published
slug: booksy
tags:
- Beauty
- Wellness
- Booking
- Appointments
- Scheduling
- Marketplace
- Salons
- Barbershops
- Spas
- Payments
- Small Business
- Webhook
website: https://booksy.com/en-us/
---

---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Launch27 Agentic Access
  operation_count: 21
  slug: launch27-agentic-access
  summary_line: 21 operations · 9 acting
api_count: 6
apis:
- description: Account/tenant settings and configuration.
  name: Launch27 Account API
  slug: launch27-account-api
- description: Login and JWT bearer token issuance.
  name: Launch27 Authentication API
  slug: launch27-authentication-api
- description: Supporting data for building and pricing a booking form.
  name: Launch27 Booking Helpers API
  slug: launch27-booking-helpers-api
- description: Authenticated customer-portal booking CRUD.
  name: Launch27 Customer Bookings API
  slug: launch27-customer-bookings-api
- description: Booking creation for non-logged-in customers.
  name: Launch27 Guest Booking API
  slug: launch27-guest-booking-api
- description: Booking, reschedule, cancellation, and location policies.
  name: Launch27 Policy API
  slug: launch27-policy-api
artifact_total: 23
asyncapis:
- description: 'AsyncAPI 2.6 description of the one WebSocket surface Launch27 documents: an account-scoped notification channel reached via a `pubsub_url` returned by the authenticated `GET /settings` call (see the '
  name: Launch27 Account Notification Channel (WebSocket, minimally documented)
  slug: launch27-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Launch27 Account API
  slug: open-launch27-account-api
- collection_type: open
  name: Launch27 Account Authentication API
  slug: open-launch27-authentication-api
- collection_type: open
  name: Launch27 Account Booking Helpers API
  slug: open-launch27-booking-helpers-api
- collection_type: open
  name: Launch27 Account Customer Bookings API
  slug: open-launch27-customer-bookings-api
- collection_type: open
  name: Launch27 Account Guest Booking API
  slug: open-launch27-guest-booking-api
- collection_type: open
  name: Launch27 Account Policy API
  slug: open-launch27-policy-api
- collection_type: open
  name: Launch27 API
  slug: open-launch27
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/launch27-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/launch27-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/launch27-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/launch27-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/launch-27
- group: company
  title: ''
  type: Website
  url: https://www.launch27.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.launch27.com
- group: docs
  title: ''
  type: APIReference
  url: https://bitbucket.org/awoo23/api-2.0/wiki/Home
- group: commercial
  title: ''
  type: Plans
  url: plans/launch27-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/launch27-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/launch27-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://launch27.com/feed/
created: '2026-07-04'
description: Launch27 is a booking and scheduling platform for cleaning service businesses (maid services), offering online booking, customer/employee/team management, recurring scheduling, payments, and marketing tools. Launch27 was acquired by Fullsteam Operations in 2019 and continues to operate today as an actively sold, independently branded product; Vonigo (a broader field service management platform for home service businesses) is a sister brand under the same Fullsteam Operations portfolio, acquired separately in 2022 - Launch27 is not a Vonigo product line, though the two are frequently compared as Fullsteam-owned competitors in the same space. Launch27 publishes a real, actively used REST API (currently v2.1, with a deprecated v2.0) documented in a public Bitbucket wiki linked from the Launch27 marketing site footer, rather than in first-party developer docs at docs.launch27.com. The API is multi-tenant, meaning every client account gets its own subdomain (e.g. https://acme.launch27.com),
  and covers booking creation/management for non-logged-in and logged-in customers, booking-form helper data (services, spots, frequencies, custom fields, price estimation), booking policies, and account settings.
finops:
- name: Launch27 Finops
  service_category: Field Service Management Software
  slug: launch27-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/launch27.png
layout: provider
modified: '2026-07-04'
name: Launch27
nav: Providers
network: true
overview: 'Launch27 publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Account API, Authentication API, Booking Helpers API, and 3 more. Tagged areas include Field Service Management, Home Services, Cleaning Services, Booking, and Scheduling.


  The Launch27 catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Launch27''s developer surface includes authentication, documentation, API reference, engineering blog, and 8 more developer resources.'
plans:
- name: Launch27 Plans Pricing
  plan_count: 4
  slug: launch27-plans-pricing
random_paper: 144
rate_limits:
- limit_count: 3
  name: Launch27 Rate Limits
  slug: launch27-rate-limits
rules:
- effective_rule_count: 29
  extends:
  - spectral:asyncapi
  name: Launch27 API Rules
  rule_count: 2
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 1
  slug: launch27-asyncapi-spectral-rules
score:
  band: developing
  composite: 42.5
  delta: -1.5
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 11.4
    contract_quality: 62.2
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 11.4
    operational_transparency: 31.6
  previous_composite: 44.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/launch27/refs/heads/main/screenshots/launch27-2026-07-25T224614.png
security:
- kind: authentication
  name: Launch27 Authentication
  slug: launch27-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Launch27 Domain Security
  slug: launch27-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Launch27 Vulnerability Disclosure
  slug: launch27-vulnerability-disclosure
  summary_line: disclosure policy published
slug: launch27
tags:
- Field Service Management
- Home Services
- Cleaning Services
- Booking
- Scheduling
- Fullsteam
- Vonigo
website: https://www.launch27.com
---

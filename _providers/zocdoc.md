---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
- acting_count: 10
  human_in_the_loop: 0
  name: Zocdoc Agentic Access
  operation_count: 30
  slug: zocdoc-agentic-access
  summary_line: 30 operations · 10 acting
api_count: 10
apis:
- description: Endpoints for booking, cancelling, and rescheduling appointments, including retrieving current appointment statuses and updated information.
  name: Zocdoc appointments API
  slug: zocdoc-appointments-api
- description: Endpoints to manage timeslots for providers.
  name: Zocdoc calendar-integration-timeslots API
  slug: zocdoc-calendar-integration-timeslots-api
- description: Endpoints for managing API credentials.
  name: Zocdoc credentials API
  slug: zocdoc-credentials-api
- description: Endpoints to retrieve facilities within the developer's directory.
  name: Zocdoc facilities API
  slug: zocdoc-facilities-api
- description: Endpoints to retrieve insurance plans supported by Zocdoc.
  name: Zocdoc insurance-reference API
  slug: zocdoc-insurance-reference-api
- description: Endpoints for retrieving and modifying provider location objects and their related insurance plans and availability.
  name: Zocdoc provider-locations API
  slug: zocdoc-provider-locations-api
- description: Endpoints to retrieve providers within the developer's directory.
  name: Zocdoc providers API
  slug: zocdoc-providers-api
- description: Endpoints to retrieve information about the developer's directory.
  name: Zocdoc reference API
  slug: zocdoc-reference-api
- description: Endpoints to retrieve schedulable entities with availability information.
  name: Zocdoc schedulable-entities API
  slug: zocdoc-schedulable-entities-api
- description: Sandbox endpoints to mock webhook behavior
  name: Zocdoc webhook API
  slug: zocdoc-webhook-api
artifact_total: 23
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zocdoc-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zocdoc-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zocdoc-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zocdoc-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.zocdoc.com
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.zocdoc.com/guides
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Zocdoc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zocdoc
- group: company
  title: ''
  type: Blog
  url: https://medium.com/zocdoc-engineering
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zocdoc.com/about/news/zocdoc-launches-its-first-ever-public-api-platform-zocdoc-for-developers/
- group: other
  title: ''
  type: X
  url: https://x.com/Zocdoc
- group: commercial
  title: ''
  type: Plans
  url: plans/zocdoc-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zocdoc-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zocdoc-finops.yml
created: '2026-06-13'
description: Zocdoc is a healthcare appointment booking platform that provides a REST API for accessing provider availability, booking appointments, managing insurance verification, and patient scheduling. The Zocdoc for Developers platform enables integration with Zocdoc's provider network through patient booking, provider calendar integration, and insurance APIs using OAuth 2.0 authentication with both sandbox and production environments.
examples:
- key_count: 2
  name: Availability Response
  slug: availability-response
- key_count: 2
  name: Book Appointment Request
  slug: book-appointment-request
- key_count: 2
  name: Book Appointment Response
  slug: book-appointment-response
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zocdoc.png
json_schemas:
- name: Appointment
  property_count: 6
  slug: zocdoc-appointment
- name: Availability
  property_count: 3
  slug: zocdoc-availability
- name: Provider
  property_count: 16
  slug: zocdoc-provider
jsonld:
- class_count: 0
  name: Zocdoc Context
  property_count: 70
  slug: zocdoc-context
layout: provider
modified: '2026-06-13'
name: Zocdoc
nav: Providers
network: true
overview: 'Zocdoc publishes 10 APIs on the [APIs.io](https://apis.io/) network, including appointments API, calendar-integration-timeslots API, credentials API, and 7 more. Tagged areas include Healthcare, Appointments, Booking, Providers, and Insurance.


  The Zocdoc catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Zocdoc''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Zocdoc Plans Pricing
  plan_count: 2
  slug: zocdoc-plans-pricing
random_paper: 30
rules:
- name: Zocdoc API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: zocdoc-jsonschema-spectral-rules
scopes:
- name: Zocdoc Scopes
  scope_count: 6
  slug: zocdoc-scopes
  summary_line: 6 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 48.1
  delta: 1.9
  facets:
    commercial_clarity: 31.6
    contract_quality: 64.0
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 5.3
  previous_composite: 46.2
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 58.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zocdoc/refs/heads/main/screenshots/zocdoc-2026-06-20T201932.png
security:
- kind: authentication
  name: Zocdoc Authentication
  slug: zocdoc-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Zocdoc Domain Security
  slug: zocdoc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zocdoc
tags:
- Healthcare
- Appointments
- Booking
- Providers
- Insurance
- Telehealth
- Scheduling
website: https://www.zocdoc.com
---

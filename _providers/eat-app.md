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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Eat App Agentic Access
  operation_count: 15
  slug: eat-app-agentic-access
  summary_line: 15 operations · 4 acting
api_count: 7
apis:
- description: Concierge bookable time-slot lookups over a date range.
  name: Eat App Concierge - Availability API
  slug: eat-app-concierge-availability-api
- description: Concierge guest search and profile retrieval.
  name: Eat App Concierge - Guests API
  slug: eat-app-concierge-guests-api
- description: Concierge bootstrap data - resources, groups, restaurants.
  name: Eat App Concierge - Reference API
  slug: eat-app-concierge-reference-api
- description: Concierge reservation create, list, get, and update/cancel.
  name: Eat App Concierge - Reservations API
  slug: eat-app-concierge-reservations-api
- description: Partner API real-time availability lookups.
  name: Eat App Partner - Availability API
  slug: eat-app-partner-availability-api
- description: Partner API reservation creation.
  name: Eat App Partner - Reservations API
  slug: eat-app-partner-reservations-api
- description: Honestly-modeled table and floor-plan operations. Not documented in the public Partner or Concierge references; confirm before use.
  name: Eat App Tables and Floor Plans (Modeled) API
  slug: eat-app-tables-and-floor-plans-modeled-api
artifact_total: 13
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/eat-app-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eat-app-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/eat-app-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eatapp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eat-app
- group: company
  title: ''
  type: Website
  url: https://eatapp.co
- group: docs
  title: ''
  type: Documentation
  url: https://restaurant.eatapp.co/knowledge/documentation
- group: start
  title: ''
  type: SignUp
  url: https://eatapp.co/integrations
- group: commercial
  title: ''
  type: Plans
  url: plans/eat-app-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/eat-app-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/eat-app-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://restaurant.eatapp.co/blog
created: '2026-07-05'
description: Eat App is a restaurant reservation and table management platform used by restaurants and restaurant groups to take bookings, manage floor plans and tables, build guest CRM profiles, and run front-of-house operations. Its developer surface is a partner/key-gated REST platform - a Partner API for booking channels to read availability and post reservations, and a Concierge API for restaurants, vendors, and groups to sync reservations, guests, availability, restaurants, and groups. Both use JSON:API-style responses, Bearer-token authentication, and an api.eat-sandbox.co sandbox mirroring api.eatapp.co production. Eat App also exposes a Restaurant MCP server for connecting AI assistants. API access is granted on request rather than fully self-serve.
finops:
- name: Eat App Finops
  service_category: Business Applications
  slug: eat-app-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eat-app.png
layout: provider
modified: '2026-07-05'
name: Eat App
nav: Providers
network: true
overview: 'Eat App publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Concierge - Availability API, Concierge - Guests API, Concierge - Reference API, and 4 more. Tagged areas include Restaurant, Reservations, Table Management, Hospitality, and Bookings.


  Eat App''s developer surface includes authentication, documentation, signup flow, engineering blog, and 8 more developer resources.'
plans:
- name: Eat App Plans Pricing
  plan_count: 5
  slug: eat-app-plans-pricing
random_paper: 100
rate_limits:
- limit_count: 3
  name: Eat App Rate Limits
  slug: eat-app-rate-limits
score:
  band: developing
  composite: 42.4
  delta: -0.6
  facets:
    commercial_clarity: 52.6
    contract_quality: 61.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 43.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eat-app/refs/heads/main/screenshots/eat-app-2026-07-25T212721.png
security:
- kind: authentication
  name: Eat App Authentication
  slug: eat-app-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Eat App Domain Security
  slug: eat-app-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: eat-app
tags:
- Restaurant
- Reservations
- Table Management
- Hospitality
- Bookings
- Guest CRM
- Availability
website: https://eatapp.co
---

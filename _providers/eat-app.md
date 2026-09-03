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
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Eat App Agentic Access
  operation_count: 15
  slug: eat-app-agentic-access
  summary_line: 15 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.eatapp.co/partners/v2
  baseurl_source: declared
  description: Concierge bookable time-slot lookups over a date range.
  name: Eat App Concierge - Availability API
  slug: eat-app-concierge-availability-api
- baseURL: https://api.eatapp.co/partners/v2
  baseurl_source: declared
  description: Concierge guest search and profile retrieval.
  name: Eat App Concierge - Guests API
  slug: eat-app-concierge-guests-api
- baseURL: https://api.eatapp.co/partners/v2
  baseurl_source: declared
  description: Concierge bootstrap data - resources, groups, restaurants.
  name: Eat App Concierge - Reference API
  slug: eat-app-concierge-reference-api
- baseURL: https://api.eatapp.co/partners/v2
  baseurl_source: declared
  description: Concierge reservation create, list, get, and update/cancel.
  name: Eat App Concierge - Reservations API
  slug: eat-app-concierge-reservations-api
- baseURL: https://api.eatapp.co/partners/v2
  baseurl_source: declared
  description: Partner API real-time availability lookups.
  name: Eat App Partner - Availability API
  slug: eat-app-partner-availability-api
- baseURL: https://api.eatapp.co/partners/v2
  baseurl_source: declared
  description: Partner API reservation creation.
  name: Eat App Partner - Reservations API
  slug: eat-app-partner-reservations-api
- baseURL: https://api.eatapp.co/partners/v2
  baseurl_source: declared
  description: Honestly-modeled table and floor-plan operations. Not documented in the public Partner or Concierge references; confirm before use.
  name: Eat App Tables and Floor Plans (Modeled) API
  slug: eat-app-tables-and-floor-plans-modeled-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Eat App Platform Concierge - Availability API
  slug: open-eat-app-concierge-availability-api
- collection_type: open
  name: Eat App Platform Concierge - Availability Concierge - Guests API
  slug: open-eat-app-concierge-guests-api
- collection_type: open
  name: Eat App Platform Concierge - Availability Concierge - Reference API
  slug: open-eat-app-concierge-reference-api
- collection_type: open
  name: Eat App Platform Concierge - Availability Concierge - Reservations API
  slug: open-eat-app-concierge-reservations-api
- collection_type: open
  name: Eat App Platform Concierge - Availability Partner - Availability API
  slug: open-eat-app-partner-availability-api
- collection_type: open
  name: Eat App Platform Concierge - Availability Partner - Reservations API
  slug: open-eat-app-partner-reservations-api
- collection_type: open
  name: Eat App Platform Concierge - Availability Tables and Floor Plans (Modeled) API
  slug: open-eat-app-tables-and-floor-plans-modeled-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/eat-app-capability-edges.yml
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


  Eat App''s developer surface includes authentication, documentation, signup flow, engineering blog, and 9 more developer resources.'
plans:
- name: Eat App Plans Pricing
  plan_count: 5
  slug: eat-app-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 3
  name: Eat App Rate Limits
  slug: eat-app-rate-limits
score:
  band: developing
  composite: 43.1
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 56.4
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 43.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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

---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Tickettailor Agentic Access
  operation_count: 26
  slug: tickettailor-agentic-access
  summary_line: 26 operations · 13 acting
api_count: 1
apis:
- baseURL: https://api.tickettailor.com/v1
  baseurl_source: declared
  description: Attendee check-ins recorded at the door.
  name: Ticket Tailor Check-ins API
  slug: tickettailor-check-ins-api
- baseURL: https://api.tickettailor.com/v1
  baseurl_source: declared
  description: Parent containers that group one or more event dates.
  name: Ticket Tailor Event Series API
  slug: tickettailor-event-series-api
- baseURL: https://api.tickettailor.com/v1
  baseurl_source: declared
  description: Individual scheduled event dates in a box office.
  name: Ticket Tailor Events API
  slug: tickettailor-events-api
- baseURL: https://api.tickettailor.com/v1
  baseurl_source: declared
  description: Individual tickets issued to attendees.
  name: Ticket Tailor Issued Tickets API
  slug: tickettailor-issued-tickets-api
- baseURL: https://api.tickettailor.com/v1
  baseurl_source: declared
  description: Orders belonging to a box office.
  name: Ticket Tailor Orders API
  slug: tickettailor-orders-api
- baseURL: https://api.tickettailor.com/v1
  baseurl_source: declared
  description: Ticket types and ticket groups scoped to an event series.
  name: Ticket Tailor Ticket Types API
  slug: tickettailor-ticket-types-api
- baseURL: https://api.tickettailor.com/v1
  baseurl_source: declared
  description: Connectivity and account overview.
  name: Ticket Tailor Utility API
  slug: tickettailor-utility-api
- baseURL: https://api.tickettailor.com/v1
  baseurl_source: declared
  description: Vouchers and their redeemable codes.
  name: Ticket Tailor Vouchers API
  slug: tickettailor-vouchers-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ticket Tailor Check-ins API
  slug: open-tickettailor-check-ins-api
- collection_type: open
  name: Ticket Tailor Check-ins Event Series API
  slug: open-tickettailor-event-series-api
- collection_type: open
  name: Ticket Tailor Check-ins Events API
  slug: open-tickettailor-events-api
- collection_type: open
  name: Ticket Tailor Check-ins Issued Tickets API
  slug: open-tickettailor-issued-tickets-api
- collection_type: open
  name: Ticket Tailor Check-ins Orders API
  slug: open-tickettailor-orders-api
- collection_type: open
  name: Ticket Tailor Check-ins Ticket Types API
  slug: open-tickettailor-ticket-types-api
- collection_type: open
  name: Ticket Tailor Check-ins Utility API
  slug: open-tickettailor-utility-api
- collection_type: open
  name: Ticket Tailor Check-ins Vouchers API
  slug: open-tickettailor-vouchers-api
- collection_type: open
  name: Ticket Tailor API
  slug: open-tickettailor
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tickettailor-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tickettailor-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tickettailor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tickettailor-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ticket-tailor
- group: company
  title: ''
  type: Website
  url: https://www.tickettailor.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.tickettailor.com/docs/intro/
- group: commercial
  title: ''
  type: Plans
  url: plans/tickettailor-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tickettailor-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tickettailor-finops.yml
created: '2026-07-05'
description: Ticket Tailor is an online event ticketing platform that lets organizers sell tickets and manage box offices for events, from single dates to recurring event series. Its public REST API (base https://api.tickettailor.com/v1) exposes the box office programmatically - events, event series, orders, issued tickets, ticket types, vouchers, and check-ins - authenticated with an API key over HTTP Basic Auth. The API is read-and-write, supports cursor-based pagination, and is rate limited to 5000 requests per 30 minutes.
finops:
- name: Tickettailor Finops
  service_category: Event Ticketing
  slug: tickettailor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tickettailor.png
layout: provider
modified: '2026-07-05'
name: Ticket Tailor
nav: Providers
network: true
overview: 'Ticket Tailor publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Check-ins API, Event Series API, Events API, and 5 more. Tagged areas include Event Ticketing, Event, Ticketing, Box Office, and Payments.


  Ticket Tailor''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Tickettailor Plans Pricing
  plan_count: 3
  slug: tickettailor-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: Tickettailor Rate Limits
  slug: tickettailor-rate-limits
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 56.5
    developer_ergonomics: 29.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 28.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tickettailor/refs/heads/main/screenshots/tickettailor-2026-09-02T163709.png
security:
- kind: authentication
  name: Tickettailor Authentication
  slug: tickettailor-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tickettailor Domain Security
  slug: tickettailor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tickettailor Vulnerability Disclosure
  slug: tickettailor-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tickettailor
tags:
- Event Ticketing
- Event
- Ticketing
- Box Office
- Payments
- Registration
website: https://www.tickettailor.com
---

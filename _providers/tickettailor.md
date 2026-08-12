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
- acting_count: 13
  human_in_the_loop: 0
  name: Tickettailor Agentic Access
  operation_count: 26
  slug: tickettailor-agentic-access
  summary_line: 26 operations · 13 acting
api_count: 8
apis:
- description: Attendee check-ins recorded at the door.
  name: Ticket Tailor Check-ins API
  slug: tickettailor-check-ins-api
- description: Parent containers that group one or more event dates.
  name: Ticket Tailor Event Series API
  slug: tickettailor-event-series-api
- description: Individual scheduled event dates in a box office.
  name: Ticket Tailor Events API
  slug: tickettailor-events-api
- description: Individual tickets issued to attendees.
  name: Ticket Tailor Issued Tickets API
  slug: tickettailor-issued-tickets-api
- description: Orders belonging to a box office.
  name: Ticket Tailor Orders API
  slug: tickettailor-orders-api
- description: Ticket types and ticket groups scoped to an event series.
  name: Ticket Tailor Ticket Types API
  slug: tickettailor-ticket-types-api
- description: Connectivity and account overview.
  name: Ticket Tailor Utility API
  slug: tickettailor-utility-api
- description: Vouchers and their redeemable codes.
  name: Ticket Tailor Vouchers API
  slug: tickettailor-vouchers-api
artifact_total: 16
collections:
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
overview: 'Ticket Tailor publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Check-ins API, Event Series API, Events API, and 5 more. Tagged areas include Event Ticketing, Events, Ticketing, Box Office, and Payments.


  Ticket Tailor''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Tickettailor Plans Pricing
  plan_count: 3
  slug: tickettailor-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Tickettailor Rate Limits
  slug: tickettailor-rate-limits
score:
  band: thin
  composite: 36.4
  delta: -0.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.9
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
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
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
- Events
- Ticketing
- Box Office
- Payments
- Registration
website: https://www.tickettailor.com
---

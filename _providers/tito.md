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
- acting_count: 35
  human_in_the_loop: 0
  name: Tito Agentic Access
  operation_count: 57
  slug: tito-agentic-access
  summary_line: 57 operations · 35 acting
api_count: 10
apis:
- description: Authentication check and account discovery.
  name: Tito Account API
  slug: tito-account-api
- description: Capacity-bound sessions releases can attach to.
  name: Tito Activities API
  slug: tito-activities-api
- description: Lists defining which tickets can be checked in.
  name: Tito Check-in Lists API
  slug: tito-check-in-lists-api
- description: Percentage or fixed discounts applied at checkout.
  name: Tito Discount Codes API
  slug: tito-discount-codes-api
- description: Events that tickets are sold for.
  name: Tito Events API
  slug: tito-events-api
- description: Refund records against registrations.
  name: Tito Refunds API
  slug: tito-refunds-api
- description: Orders that group one or more tickets.
  name: Tito Registrations API
  slug: tito-registrations-api
- description: Ticket types (releases) for an event.
  name: Tito Releases API
  slug: tito-releases-api
- description: Individual tickets held by attendees.
  name: Tito Tickets API
  slug: tito-tickets-api
- description: Endpoints Tito POSTs event notifications to.
  name: Tito Webhook Endpoints API
  slug: tito-webhook-endpoints-api
artifact_total: 17
collections:
- collection_type: open
  name: Tito Admin API
  slug: open-tito
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tito-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tito-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tito-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/teamtito
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usetito
- group: company
  title: ''
  type: Website
  url: https://ti.to
- group: docs
  title: ''
  type: Documentation
  url: https://ti.to/docs/api
- group: commercial
  title: ''
  type: Plans
  url: plans/tito-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tito-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tito-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.tito.io/
created: '2026-07-12'
description: Tito (ti.to) is an event registration and ticketing platform from Team Tito in Dublin, Ireland, used to sell tickets, collect registrations, and check in attendees for conferences and events. Organizers can sell through Tito-hosted event pages or an embeddable widget. The Admin API is a REST/JSON interface at https://api.tito.io/v3 for managing accounts, events, releases (ticket types), tickets, registrations, discount codes, activities, check-in lists, and refunds, authenticated with a secret API token. Tito also emits outbound webhooks for ticket, registration, check-in, and interested-user events, and exposes a separate unauthenticated Check-in API.
finops:
- name: Tito Finops
  service_category: Event Ticketing and Registration
  slug: tito-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tito.png
layout: provider
modified: '2026-07-12'
name: Tito
nav: Providers
network: true
overview: 'Tito publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Account API, Activities API, Check-in Lists API, and 7 more. Tagged areas include Event Ticketing, Events, Registration, Ticketing, and Conferences.


  Tito''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Tito Plans Pricing
  plan_count: 3
  slug: tito-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 2
  name: Tito Rate Limits
  slug: tito-rate-limits
score:
  band: thin
  composite: 35.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 53.6
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 35.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Tito Authentication
  slug: tito-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tito Domain Security
  slug: tito-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tito
tags:
- Event Ticketing
- Events
- Registration
- Ticketing
- Conferences
- Event Management
- Attendees
- Webhooks
- SaaS
website: https://ti.to
---

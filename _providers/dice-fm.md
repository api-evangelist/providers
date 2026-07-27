---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 5
apis:
- description: Query a partner's events through the DICE Ticket Holders GraphQL API - event name, state, start/end datetimes, currency, URL, artists, genres, ticket types, price tiers, and total ticket allocation. E
  name: DICE Events API
  slug: dice-fm-events-api
- description: Retrieve who currently holds a ticket for an event for access management and attendance tracking - ticket code, ticket type, seat, full price, fees, commission and DICE commission, the holder (fan), c
  name: DICE Tickets and Ticket Holders API
  slug: dice-fm-tickets-api
- description: 'Query orders and sales to understand event finances and feed sales into business intelligence - purchase timestamp, quantity, sales channel, full price, commission and DICE commission, fee breakdown, '
  name: DICE Orders and Sales API
  slug: dice-fm-orders-sales-api
- description: Track ticket returns and transfers - a Return links a ticket and order with a returned-at timestamp and reason, and a TicketTransfer records tickets and orders moved between fans with a transferred-at
  name: DICE Returns and Transfers API
  slug: dice-fm-returns-transfers-api
- description: Read venue details attached to events - venue name, type, age limit, address fields, coordinates, and timezone. Venues are resolved through the events they host on the Ticket Holders GraphQL schema. E
  name: DICE Venues API
  slug: dice-fm-venues-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dice-fm-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dice-fm-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dicefm
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dice-fm
- group: company
  title: ''
  type: Website
  url: https://dice.fm
- group: docs
  title: ''
  type: Documentation
  url: https://partners-endpoint.dice.fm/graphql/docs/index.html
- group: start
  title: ''
  type: Portal
  url: https://mio.dice.fm/
- group: start
  title: ''
  type: SignUp
  url: https://dice.fm/partners
- group: commercial
  title: ''
  type: Plans
  url: plans/dice-fm-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dice-fm-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dice-fm-finops.yml
created: '2026-07-05'
description: DICE is a live music and events ticketing platform (dice.fm) connecting fans to gigs, club nights, festivals, and experiences, with a fan-facing mobile app and a partner platform (MIO) for promoters, venues, and festivals. For partners, DICE exposes a documented but access-gated GraphQL API - the Ticket Holders API at partners-endpoint.dice.fm/graphql - that lets downstream systems query events, tickets and ticket holders, orders and sales, returns and transfers, fans, and venues. API tokens are generated inside MIO and passed as a Bearer authorization header; the API is available to DICE partners rather than as an open self-service developer program.
finops:
- name: Dice Fm Finops
  service_category: Ticketing and Events
  slug: dice-fm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dice-fm.png
layout: provider
modified: '2026-07-05'
name: DICE
nav: Providers
network: true
overview: 'DICE publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Ticketing, Live Music, Events, Tickets, and GraphQL.


  DICE''s developer surface includes documentation, developer portal, signup flow, and 8 more developer resources.'
plans:
- name: Dice Fm Plans Pricing
  plan_count: 2
  slug: dice-fm-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 3
  name: Dice Fm Rate Limits
  slug: dice-fm-rate-limits
score:
  band: emerging
  composite: 26.7
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 26.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dice-fm/refs/heads/main/screenshots/dice-fm-2026-07-25T211936.png
security:
- kind: domain-security
  name: Dice Fm Domain Security
  slug: dice-fm-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dice Fm Vulnerability Disclosure
  slug: dice-fm-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dice-fm
tags:
- Ticketing
- Live Music
- Events
- Tickets
- GraphQL
- Entertainment
- Partner API
website: https://dice.fm
---

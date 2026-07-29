---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Brella Agentic Access
  operation_count: 6
  slug: brella-agentic-access
  summary_line: 6 operations
api_count: 7
apis:
- description: Outbound HTTP webhooks that notify a subscriber URL when invites, attendees, speakers, sponsors, ticket purchases, or ticket types are created, updated, or deleted. Server-to-endpoint HTTP POST callba
  name: Brella Webhooks
  slug: brella-webhooks
- description: The Attendees API from Brella — 1 operation(s) for attendees.
  name: Brella Attendees API
  slug: brella-attendees-api
- description: The Events API from Brella — 1 operation(s) for events.
  name: Brella Events API
  slug: brella-events-api
- description: The Invites API from Brella — 1 operation(s) for invites.
  name: Brella Invites API
  slug: brella-invites-api
- description: The Schedule API from Brella — 1 operation(s) for schedule.
  name: Brella Schedule API
  slug: brella-schedule-api
- description: The Speakers API from Brella — 1 operation(s) for speakers.
  name: Brella Speakers API
  slug: brella-speakers-api
- description: The Sponsors API from Brella — 1 operation(s) for sponsors.
  name: Brella Sponsors API
  slug: brella-sponsors-api
artifact_total: 14
collections:
- collection_type: open
  name: Brella Integration API
  slug: open-brella
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/brella-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brella-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/brella-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brella
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/brella
- group: company
  title: ''
  type: Website
  url: https://www.brella.io
- group: docs
  title: ''
  type: Documentation
  url: https://developer.brella.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/brella-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/brella-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/brella-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.brella.io/blog
created: '2026-07-12'
description: Brella is an event networking and engagement platform for conferences, trade shows, livestreams, and hybrid events, best known for AI-powered attendee matchmaking and one-to-one meeting booking. Organizers manage events, attendees, speakers, sponsors, schedules, and networking through the Brella web and mobile apps. Brella exposes a documented public REST Integration API and outbound webhooks so organizers can read event data (events, attendees, speakers, sponsors, timeslots, invites) and sync it to registration, CRM, and analytics tools. API access is gated - an organization admin generates an API key from the Brella admin panel after the integration feature is enabled for the account.
finops:
- name: Brella Finops
  service_category: Events and Engagement
  slug: brella-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brella.png
layout: provider
modified: '2026-07-12'
name: Brella
nav: Providers
network: true
overview: 'Brella publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Attendees API, Events API, Invites API, and 3 more. Tagged areas include Events, Event Networking, Matchmaking, Event Platform, and Attendees.


  Brella''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Brella Plans Pricing
  plan_count: 1
  slug: brella-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 2
  name: Brella Rate Limits
  slug: brella-rate-limits
score:
  band: thin
  composite: 36.0
  delta: -2.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 38.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brella/refs/heads/main/screenshots/brella-2026-07-25T203750.png
security:
- kind: authentication
  name: Brella Authentication
  slug: brella-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Brella Domain Security
  slug: brella-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brella
tags:
- Events
- Event Networking
- Matchmaking
- Event Platform
- Attendees
- Engagement
- Conferences
- SaaS
website: https://www.brella.io
---

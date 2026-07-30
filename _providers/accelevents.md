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
- acting_count: 4
  human_in_the_loop: 0
  name: Accelevents Agentic Access
  operation_count: 12
  slug: accelevents-agentic-access
  summary_line: 12 operations · 4 acting
api_count: 5
apis:
- description: Event attendees and people.
  name: Accelevents Attendees API
  slug: accelevents-attendees-api
- description: Event details and configuration.
  name: Accelevents Events API
  slug: accelevents-events-api
- description: Ticketing orders and sales.
  name: Accelevents Orders API
  slug: accelevents-orders-api
- description: Agenda sessions, tracks, and speakers.
  name: Accelevents Sessions API
  slug: accelevents-sessions-api
- description: Ticket holders and ticket types.
  name: Accelevents Tickets API
  slug: accelevents-tickets-api
artifact_total: 13
collections:
- collection_type: open
  name: Accelevents Open API
  slug: open-accelevents
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/accelevents-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/accelevents-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accelevents-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/accelevents-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/accelevents
- group: company
  title: ''
  type: Website
  url: https://www.accelevents.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.accelevents.com/docs/accelevents-api-documentation
- group: docs
  title: ''
  type: APIReference
  url: https://developer.accelevents.com/reference
- group: commercial
  title: ''
  type: Plans
  url: plans/accelevents-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/accelevents-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/accelevents-finops.yml
created: '2026-07-05'
description: Accelevents is an all-in-one event management and ticketing platform for in-person, virtual, and hybrid events - covering registration, ticketing, agenda and sessions, speakers, exhibitors, networking, and engagement. The Accelevents Open API is a REST API (base https://api.accelevents.com/rest) authenticated with an organization API key generated from the account Integrations tab. It exposes event details, attendees, ticketing orders and sales, ticket holders, sessions, speakers, and attendee networking. API and webhook access is a paid-plan feature (Business tier and above), so many endpoints are documented publicly but require a provisioned key to exercise.
finops:
- name: Accelevents Finops
  service_category: Event Management and Ticketing
  slug: accelevents-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/accelevents.png
layout: provider
modified: '2026-07-05'
name: Accelevents
nav: Providers
network: true
overview: 'Accelevents publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Attendees API, Events API, Orders API, and 2 more. Tagged areas include Event Management, Ticketing, Events, Registration, and Virtual Events.


  Accelevents'' developer surface includes authentication, documentation, API reference, and 8 more developer resources.'
plans:
- name: Accelevents Plans Pricing
  plan_count: 4
  slug: accelevents-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 4
  name: Accelevents Rate Limits
  slug: accelevents-rate-limits
score:
  band: thin
  composite: 41.3
  delta: -2.1
  facets:
    commercial_clarity: 47.4
    contract_quality: 60.2
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 43.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/accelevents/refs/heads/main/screenshots/accelevents-2026-07-25T181429.png
security:
- kind: authentication
  name: Accelevents Authentication
  slug: accelevents-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Accelevents Domain Security
  slug: accelevents-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Accelevents Trust Center
  slug: accelevents-trust-center
  summary_line: SOC 2, GDPR
slug: accelevents
tags:
- Event Management
- Ticketing
- Events
- Registration
- Virtual Events
- Sessions
website: https://www.accelevents.com
---

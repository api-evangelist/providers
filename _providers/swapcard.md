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
    agentic_access: false
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
  score: 28.4
  scored_at: '2026-08-12'
api_count: 3
apis:
- description: Organizer-facing GraphQL API (the Event Admin endpoint) to fetch, create, modify, and delete event content - events, people, exhibitors, plannings/sessions, and groups. Single GraphQL endpoint over HT
  name: Swapcard Content API
  slug: swapcard-content-api
- description: 'Exhibitor-facing GraphQL API to list accessible booths (myExhibitors), export event leads with cursor pagination (myLeads), and scan badges to create leads (scanBadges). Separate GraphQL endpoint and '
  name: Swapcard Exhibitor Leads API
  slug: swapcard-leads-api
- description: GraphQL API to collect and leverage analytics on event performance and attendee behavior. Documented on the Swapcard Developer Hub; its schema is not modeled in this catalog entry (baseURL shown is in
  name: Swapcard Analytics API
  slug: swapcard-analytics-api
artifact_total: 9
collections:
- collection_type: open
  name: Swapcard GraphQL APIs
  slug: open-swapcard
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swapcard-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/swapcard-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.swapcard.com/
- group: docs
  title: ''
  type: Documentation
  url: https://swapcard.dev/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/swapcard
- group: commercial
  title: ''
  type: Plans
  url: plans/swapcard-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/swapcard-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/swapcard-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.swapcard.com/blog
created: '2026-07-12'
description: Swapcard is an AI-powered event and community engagement platform for in-person, virtual, and hybrid events - mobile and web event apps, attendee networking and matchmaking, exhibitor and lead management, registration, and onsite badging. For developers Swapcard is GraphQL-first - an organizer-facing Content (Event Admin) API to fetch, create, modify, and delete event content (events, people, exhibitors, plannings/sessions, groups); an Exhibitor Leads API to retrieve booths, export leads, and scan badges; and a GraphQL Analytics API. Access is token-based and provisioned to Swapcard customers and partners (organizers and exhibitors).
finops:
- name: Swapcard Finops
  service_category: Events and Community Engagement
  slug: swapcard-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/swapcard.png
layout: provider
modified: '2026-07-12'
name: Swapcard
nav: Providers
network: true
overview: 'Swapcard publishes 2 APIs on the [APIs.io](https://apis.io/) network: Content API and Exhibitor Leads API. Tagged areas include Events, Event Management, Community, Networking, and Event Platform.


  Swapcard''s developer surface includes authentication, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Swapcard Plans Pricing
  plan_count: 3
  slug: swapcard-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 7
  name: Swapcard Rate Limits
  slug: swapcard-rate-limits
score:
  band: thin
  composite: 33.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 37.0
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 33.0
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Swapcard Authentication
  slug: swapcard-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Swapcard Domain Security
  slug: swapcard-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: swapcard
tags:
- Events
- Event Management
- Community
- Networking
- Event Platform
- GraphQL
- Attendees
- Exhibitors
- SaaS
website: https://www.swapcard.com/
---

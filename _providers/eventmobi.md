---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: Read and update the events an Organizer manages. Confirmed request patterns include GET and PATCH on the events collection and nested resources such as /events/{event_id}/images/. Each API key is scop
  name: EventMobi Events API
  slug: eventmobi-events-api
- description: Manage the people associated with an event - attendees, speakers, and other participants - including their profile fields and visibility, which are controlled by authorization level. People are organi
  name: EventMobi People API
  slug: eventmobi-people-api
- description: Manage an event's agenda sessions - scheduling, session roles, and the speakers and content attached to each session. Endpoints are nested under an event. Exact verb/path coverage is endpointsModeled.
  name: EventMobi Sessions API
  slug: eventmobi-sessions-api
- description: Manage the companies shown in an event - sponsors, exhibitors, and vendors. Confirmed request pattern includes the nested collection /events/{event_id}/companies/. Full verb/path coverage is endpoints
  name: EventMobi Companies API
  slug: eventmobi-companies-api
- description: Create and manage people groups used to categorize attendees within an event; custom groups carry the "custom" type. Endpoints are nested under an event. Exact verb/path coverage is endpointsModeled.
  name: EventMobi Groups API
  slug: eventmobi-groups-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eventmobi-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EventMobi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eventmobi
- group: company
  title: ''
  type: Website
  url: https://www.eventmobi.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.eventmobi.com/latest/
- group: commercial
  title: ''
  type: Plans
  url: plans/eventmobi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/eventmobi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/eventmobi-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.eventmobi.com/blog/
created: '2026-07-05'
description: 'EventMobi is an event management platform for in-person, virtual, and hybrid events - event apps, registration and ticketing, event websites, badges and check-in, and live engagement - all configured through its Experience Manager. EventMobi exposes a documented public Unified API (UAPI) that lets organizers programmatically read and manage the data behind an event: events, people (attendees, speakers, and other participants), sessions, companies (sponsors and exhibitors), and groups. Access is gated by an EventMobi Organizer account - API keys are generated inside Experience Manager and carry the same access rights as the Organizer they belong to - so the API is available to paying customers rather than through open self-service signup.'
finops:
- name: Eventmobi Finops
  service_category: Event Management
  slug: eventmobi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eventmobi.png
layout: provider
modified: '2026-07-05'
name: EventMobi
nav: Providers
network: true
overview: 'EventMobi publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Events, Event Management, Event Apps, Attendees, and Sessions.


  EventMobi''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Eventmobi Plans Pricing
  plan_count: 3
  slug: eventmobi-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 3
  name: Eventmobi Rate Limits
  slug: eventmobi-rate-limits
score:
  band: emerging
  composite: 22.3
  delta: -2.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 24.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eventmobi/refs/heads/main/screenshots/eventmobi-2026-07-25T213712.png
security:
- kind: domain-security
  name: Eventmobi Domain Security
  slug: eventmobi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: eventmobi
tags:
- Events
- Event Management
- Event Apps
- Attendees
- Sessions
- Registration
website: https://www.eventmobi.com
---

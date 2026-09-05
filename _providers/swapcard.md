---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
  score: 18.0
  scored_at: '2026-09-04'
api_count: 3
apis:
- baseURL: https://developer.swapcard.com/event-admin/graphql
  baseurl_source: declared
  description: Organizer-facing GraphQL API (the Event Admin endpoint) to fetch, create, modify, and delete event content - events, people, exhibitors, plannings/sessions, and groups. Single GraphQL endpoint over HT
  name: Swapcard Content API
  slug: swapcard-content-api
- baseURL: https://developer.swapcard.com/exhibitor/graphql
  baseurl_source: declared
  description: 'Exhibitor-facing GraphQL API to list accessible booths (myExhibitors), export event leads with cursor pagination (myLeads), and scan badges to create leads (scanBadges). Separate GraphQL endpoint and '
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
overview: 'Swapcard publishes 2 APIs on the [APIs.io](https://apis.io/) network: Content API and Exhibitor Leads API. Tagged areas include Event, Event Management, Community, Networking, and Event Platform.


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
  composite: 32.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 67.0
    catalog_earned_first_party: 0.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 31.9
    developer_ergonomics: 26.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 32.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/swapcard/refs/heads/main/screenshots/swapcard-2026-09-02T161340.png
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
- Event
- Event Management
- Community
- Networking
- Event Platform
- GraphQL
- Attendees
- Exhibitors
- Software-as-a-Service
website: https://www.swapcard.com/
---

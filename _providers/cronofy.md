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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Cronofy Agentic Access
  operation_count: 16
  slug: cronofy-agentic-access
  summary_line: 16 operations · 10 acting
api_count: 1
apis:
- baseURL: https://api.cronofy.com/v1
  baseurl_source: declared
  description: Availability queries and hosted real-time scheduling.
  name: Cronofy Availability API
  slug: cronofy-availability-api
- baseURL: https://api.cronofy.com/v1
  baseurl_source: declared
  description: Connected calendars, application calendars, and account identity.
  name: Cronofy Calendars API
  slug: cronofy-calendars-api
- baseURL: https://api.cronofy.com/v1
  baseurl_source: declared
  description: Reading, creating, updating, and deleting events plus free/busy.
  name: Cronofy Events API
  slug: cronofy-events-api
- baseURL: https://api.cronofy.com/v1
  baseurl_source: declared
  description: Notification channels for real-time calendar changes.
  name: Cronofy Push Notifications API
  slug: cronofy-push-notifications-api
- baseURL: https://api.cronofy.com/v1
  baseurl_source: declared
  description: Calendar invites tracked without calendar authorization.
  name: Cronofy Smart Invites API
  slug: cronofy-smart-invites-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cronofy Availability API
  slug: open-cronofy-availability-api
- collection_type: open
  name: Cronofy Availability Calendars API
  slug: open-cronofy-calendars-api
- collection_type: open
  name: Cronofy Availability Events API
  slug: open-cronofy-events-api
- collection_type: open
  name: Cronofy Availability Push Notifications API
  slug: open-cronofy-push-notifications-api
- collection_type: open
  name: Cronofy Availability Smart Invites API
  slug: open-cronofy-smart-invites-api
- collection_type: open
  name: Cronofy API
  slug: open-cronofy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cronofy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cronofy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cronofy-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cronofy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cronofy
- group: company
  title: ''
  type: Website
  url: https://www.cronofy.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cronofy.com/developers/
- group: commercial
  title: ''
  type: Plans
  url: plans/cronofy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cronofy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cronofy-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.cronofy.com/blog
created: '2026-06-21'
description: Cronofy is a scheduling and calendar API platform that provides a unified interface to Google Calendar, Microsoft 365 / Outlook, Exchange, and Apple iCloud. Its REST API powers two-way calendar sync, real-time availability and scheduling, smart invites, scheduling links, and push notifications for software teams embedding scheduling into their products.
finops:
- name: Cronofy Finops
  service_category: Developer Tools and Scheduling
  slug: cronofy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cronofy.png
layout: provider
modified: '2026-06-21'
name: Cronofy
nav: Providers
network: true
overview: 'Cronofy publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Availability API, Calendars API, Events API, and 2 more. Tagged areas include Scheduling, Calendar, Availability, Booking, and Productivity.


  Cronofy''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Cronofy Plans Pricing
  plan_count: 4
  slug: cronofy-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Cronofy Rate Limits
  slug: cronofy-rate-limits
score:
  band: thin
  composite: 38.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 57.4
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cronofy/refs/heads/main/screenshots/cronofy-2026-07-25T210745.png
security:
- kind: authentication
  name: Cronofy Authentication
  slug: cronofy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cronofy Domain Security
  slug: cronofy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cronofy
tags:
- Scheduling
- Calendar
- Availability
- Booking
- Productivity
website: https://www.cronofy.com
---

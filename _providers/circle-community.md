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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 38
  human_in_the_loop: 0
  name: Circle Community Agentic Access
  operation_count: 69
  slug: circle-community-agentic-access
  summary_line: 69 operations · 38 acting
api_count: 1
apis:
- baseURL: wss://app.circle.so/cable
  baseurl_source: declared
  description: Beta ActionCable (Rails) WebSocket surface for realtime chat and notifications, connected at wss://app.circle.so/cable with a member Bearer access token and a whitelisted Origin header. Exposes a Noti
  name: Circle Realtime WebSocket API
  slug: circle-community-realtime-websocket-api
- baseURL: https://app.circle.so/api/admin/v2
  baseurl_source: declared
  description: Course sections, lessons, and progress.
  name: Circle Admin - Courses API
  slug: circle-community-admin-courses-api
- baseURL: https://app.circle.so/api/admin/v2
  baseurl_source: declared
  description: Events and event attendees.
  name: Circle Admin - Events API
  slug: circle-community-admin-events-api
- baseURL: https://app.circle.so/api/admin/v2
  baseurl_source: declared
  description: Admin-authenticated community member management.
  name: Circle Admin - Members API
  slug: circle-community-admin-members-api
- baseURL: https://app.circle.so/api/admin/v2
  baseurl_source: declared
  description: Posts, comments, and topics.
  name: Circle Admin - Posts API
  slug: circle-community-admin-posts-api
- baseURL: https://app.circle.so/api/admin/v2
  baseurl_source: declared
  description: Spaces, space groups, and their memberships.
  name: Circle Admin - Spaces API
  slug: circle-community-admin-spaces-api
- baseURL: https://app.circle.so/api/admin/v2
  baseurl_source: declared
  description: Member JWT token exchange for the Headless Member API.
  name: Circle Headless - Auth API
  slug: circle-community-headless-auth-api
- baseURL: https://app.circle.so/api/admin/v2
  baseurl_source: declared
  description: Member-authenticated experience endpoints.
  name: Circle Headless - Member API
  slug: circle-community-headless-member-api
artifact_total: 25
asyncapis:
- description: Circle exposes a documented public WebSocket API for realtime chat and notifications, in beta for customers on the Business plan and above. The transport is ActionCable (Rails' WebSocket framework), a
  name: Circle Realtime WebSocket API (Beta)
  slug: circle-community-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Circle Developer Platform Admin - Courses API
  slug: open-circle-community-admin-courses-api
- collection_type: open
  name: Circle Developer Platform Admin - Courses Admin - Events API
  slug: open-circle-community-admin-events-api
- collection_type: open
  name: Circle Developer Platform Admin - Courses Admin - Members API
  slug: open-circle-community-admin-members-api
- collection_type: open
  name: Circle Developer Platform Admin - Courses Admin - Posts API
  slug: open-circle-community-admin-posts-api
- collection_type: open
  name: Circle Developer Platform Admin - Courses Admin - Spaces API
  slug: open-circle-community-admin-spaces-api
- collection_type: open
  name: Circle Developer Platform Admin - Courses Headless - Auth API
  slug: open-circle-community-headless-auth-api
- collection_type: open
  name: Circle Developer Platform Admin - Courses Headless - Member API
  slug: open-circle-community-headless-member-api
- collection_type: open
  name: Circle Developer Platform API
  slug: open-circle-community
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/circle-community-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/circle-community-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/circle-community-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/circleco
- group: company
  title: ''
  type: Website
  url: https://circle.so
- group: docs
  title: ''
  type: Documentation
  url: https://api.circle.so
- group: commercial
  title: ''
  type: Plans
  url: plans/circle-community-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/circle-community-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/circle-community-finops.yml
created: '2026-07-05'
description: 'Circle (circle.so) is an all-in-one community platform for creators, coaches, and brands - hosting discussions, courses, events, live streams, memberships, paywalls, and chat under a single branded space. This is the community software company at circle.so, NOT the USDC / stablecoin financial-services company. Circle exposes a documented public developer platform: an admin-authenticated Admin API (V2) for automations, migrations, and bulk administration; a Headless offering (Member API plus Auth API) for embedding Circle features into your own website or app via member-scoped JWT tokens; and a beta ActionCable WebSocket surface for realtime chat and notifications. API access is plan-gated to the Business plan and above.'
finops:
- name: Circle Community Finops
  service_category: Community and Collaboration
  slug: circle-community-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/circle-community.png
layout: provider
modified: '2026-07-05'
name: Circle
nav: Providers
network: true
overview: 'Circle publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Realtime WebSocket API, Admin - Courses API, Admin - Events API, and 5 more. Tagged areas include Community, Creators, Courses, Memberships, and Event.


  The Circle catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Circle''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Circle Community Plans Pricing
  plan_count: 4
  slug: circle-community-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 4
  name: Circle Community Rate Limits
  slug: circle-community-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Circle API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: circle-community-asyncapi-spectral-rules
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 67.8
    catalog_earned_first_party: 0.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 11.4
    contract_quality: 58.2
    developer_ergonomics: 29.8
    discoverability: 68.5
    governance: 11.4
    operational_transparency: 31.6
  previous_composite: 41.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/circle-community/refs/heads/main/screenshots/circle-community-2026-07-25T205412.png
security:
- kind: authentication
  name: Circle Community Authentication
  slug: circle-community-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Circle Community Domain Security
  slug: circle-community-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: circle-community
tags:
- Community
- Creators
- Courses
- Memberships
- Event
- Chat
- Community Platform
website: https://circle.so
---

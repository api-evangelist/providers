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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
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
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 38
  human_in_the_loop: 0
  name: Circle Community Agentic Access
  operation_count: 69
  slug: circle-community-agentic-access
  summary_line: 69 operations · 38 acting
api_count: 8
apis:
- description: Beta ActionCable (Rails) WebSocket surface for realtime chat and notifications, connected at wss://app.circle.so/cable with a member Bearer access token and a whitelisted Origin header. Exposes a Noti
  name: Circle Realtime WebSocket API
  slug: circle-community-realtime-websocket-api
- description: Course sections, lessons, and progress.
  name: Circle Admin - Courses API
  slug: circle-community-admin-courses-api
- description: Events and event attendees.
  name: Circle Admin - Events API
  slug: circle-community-admin-events-api
- description: Admin-authenticated community member management.
  name: Circle Admin - Members API
  slug: circle-community-admin-members-api
- description: Posts, comments, and topics.
  name: Circle Admin - Posts API
  slug: circle-community-admin-posts-api
- description: Spaces, space groups, and their memberships.
  name: Circle Admin - Spaces API
  slug: circle-community-admin-spaces-api
- description: Member JWT token exchange for the Headless Member API.
  name: Circle Headless - Auth API
  slug: circle-community-headless-auth-api
- description: Member-authenticated experience endpoints.
  name: Circle Headless - Member API
  slug: circle-community-headless-member-api
artifact_total: 17
asyncapis:
- description: Circle exposes a documented public WebSocket API for realtime chat and notifications, in beta for customers on the Business plan and above. The transport is ActionCable (Rails' WebSocket framework), a
  name: Circle Realtime WebSocket API (Beta)
  slug: circle-community-asyncapi
collections:
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
overview: 'Circle publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Realtime WebSocket API, Admin - Courses API, Admin - Events API, and 5 more. Tagged areas include Community, Creators, Courses, Memberships, and Events.


  The Circle catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Circle''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Circle Community Plans Pricing
  plan_count: 4
  slug: circle-community-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 4
  name: Circle Community Rate Limits
  slug: circle-community-rate-limits
rules:
- name: Circle API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: circle-community-asyncapi-spectral-rules
score:
  band: developing
  composite: 43.3
  delta: -3.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 59.7
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 31.6
  previous_composite: 46.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
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
- Events
- Chat
- Community Platform
website: https://circle.so
---

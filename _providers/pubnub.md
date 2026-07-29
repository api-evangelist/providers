---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: false
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
  score: 29.3
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Single REST surface for publish, subscribe (long-poll), presence, history, signal, and App Context. Pub/Sub key authentication. SDKs available for 50+ languages and platforms.
  name: PubNub REST API
  slug: rest-api
- description: Edge serverless functions executed on PubNub's network in response to messages, presence events, or HTTP triggers.
  name: PubNub Functions
  slug: functions-api
artifact_total: 30
asyncapis:
- description: AsyncAPI description of PubNub's realtime subscribe surface — the event stream that delivers messages, signals, presence updates, file events, message-action events, and App Context (object) events to
  name: PubNub Realtime Streaming API
  slug: pubnub-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pubnub-domain-security.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/pubnub/skills
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pubnub
- group: start
  title: ''
  type: Portal
  url: https://www.pubnub.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.pubnub.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pubnub.com/pricing/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/pubnub
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pubnub.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/pubnub-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pubnub-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pubnub-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.pubnub.com/blog
created: '2026-05-08'
description: PubNub is a realtime communication platform supporting pub/sub, presence, chat, App Context (object metadata), Functions (server-less compute on the edge), Push Notifications, and IoT messaging across 1B+ devices. The PubNub REST API runs at ps.pndsn.com; SDKs handle the underlying long-poll / WebSocket protocol. Authentication uses a publish/subscribe key pair per keyset.
finops:
- name: Pubnub Finops
  service_category: Realtime Infrastructure
  slug: pubnub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pubnub.png
layout: provider
modified: '2026-05-29'
name: PubNub
nav: Providers
network: true
overview: 'PubNub publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Realtime, WebSockets, Pub/Sub, IoT, and Messaging.


  The PubNub catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  PubNub''s developer surface includes developer portal, documentation, pricing, GitHub presence, engineering blog, and 7 more developer resources.'
plans:
- name: Pubnub Plans Pricing
  plan_count: 6
  slug: pubnub-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Pubnub Rate Limits
  slug: pubnub-rate-limits
rules:
- name: PubNub API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: pubnub-asyncapi-spectral-rules
score:
  band: thin
  composite: 40.4
  delta: -4.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 50.6
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 47.9
    operational_transparency: 52.6
  previous_composite: 44.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pubnub/refs/heads/main/screenshots/pubnub-2026-06-20T192250.png
security:
- kind: domain-security
  name: Pubnub Domain Security
  slug: pubnub-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
skill_count: 22
skills:
- name: pubnub-app-context
  slug: pubnub-app-context
- name: pubnub-app-developer
  slug: pubnub-app-developer
- name: pubnub-chat
  slug: pubnub-chat
- name: pubnub-choose-docs-path
  slug: pubnub-choose-docs-path
- name: pubnub-events-and-actions
  slug: pubnub-events-and-actions
- name: pubnub-functions
  slug: pubnub-functions
- name: pubnub-history
  slug: pubnub-history
- name: pubnub-illuminate
  slug: pubnub-illuminate
- name: pubnub-keyset-management
  slug: pubnub-keyset-management
- name: pubnub-live-auctions
  slug: pubnub-live-auctions
- name: pubnub-live-betting-casino
  slug: pubnub-live-betting-casino
- name: pubnub-live-sport-updates
  slug: pubnub-live-sport-updates
- name: pubnub-live-stock-quote-updates
  slug: pubnub-live-stock-quote-updates
- name: pubnub-live-voting
  slug: pubnub-live-voting
- name: pubnub-multiplayer-gaming
  slug: pubnub-multiplayer-gaming
- name: pubnub-observability
  slug: pubnub-observability
- name: pubnub-order-delivery-driver
  slug: pubnub-order-delivery-driver
- name: pubnub-presence
  slug: pubnub-presence
- name: pubnub-reliability
  slug: pubnub-reliability
- name: pubnub-scale
  slug: pubnub-scale
- name: pubnub-security
  slug: pubnub-security
- name: pubnub-telemedicine
  slug: pubnub-telemedicine
slug: pubnub
tags:
- Realtime
- WebSockets
- Pub/Sub
- IoT
- Messaging
- Chat
- Presence
- Functions
website: https://www.pubnub.com/
---

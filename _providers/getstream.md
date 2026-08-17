---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 32
  human_in_the_loop: 1
  name: Getstream Agentic Access
  operation_count: 44
  slug: getstream-agentic-access
  summary_line: 44 operations · 32 acting · 1 human-in-the-loop
api_count: 14
apis:
- description: 'Build scalable activity feeds and timelines - add activities to feeds, follow and unfollow feeds, aggregate and rank activities, and fan out to followers. Powers social timelines, notification feeds, '
  name: Stream Activity Feeds API
  slug: getstream-activity-feeds-api
- description: Create and manage audio/video calls and livestreams - get-or-create calls, manage call members and permissions, start and stop recording, transcription, and broadcasting. Metered on participant minute
  name: Stream Video and Audio API
  slug: getstream-video-audio-api
- description: Application-level utilities such as rate limits and search.
  name: Stream Application API
  slug: getstream-application-api
- description: Create and control bulk messaging campaigns.
  name: Stream Campaigns API
  slug: getstream-campaigns-api
- description: Query, create, update, truncate, and delete chat channels.
  name: Stream Channels API
  slug: getstream-channels-api
- description: Register and manage push notification devices.
  name: Stream Devices API
  slug: getstream-devices-api
- description: Query and partially update channel members.
  name: Stream Members API
  slug: getstream-members-api
- description: Send, retrieve, update, delete, and search messages and replies.
  name: Stream Messages API
  slug: getstream-messages-api
- description: Ban, flag, and mute users, messages, and channels.
  name: Stream Moderation API
  slug: getstream-moderation-api
- description: Inspect application permissions.
  name: Stream Permissions API
  slug: getstream-permissions-api
- description: Add and remove emoji reactions on messages.
  name: Stream Reactions API
  slug: getstream-reactions-api
- description: List, create, and delete custom roles.
  name: Stream Roles API
  slug: getstream-roles-api
- description: Query and retrieve message threads.
  name: Stream Threads API
  slug: getstream-threads-api
- description: Upsert, query, update, deactivate, and reactivate users.
  name: Stream Users API
  slug: getstream-users-api
artifact_total: 38
asyncapis:
- description: AsyncAPI 2.6 description of Stream (GetStream.io) Chat's **real-time WebSocket** surface. Unlike the request/response server-side REST API (`https://chat.stream-io-api.com`, modeled in `openapi/getstr
  name: Stream Chat Realtime WebSocket API
  slug: getstream-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Stream Chat API (Server-side REST) Application API
  slug: open-getstream-application-api
- collection_type: open
  name: Stream Chat API (Server-side REST) Application Campaigns API
  slug: open-getstream-campaigns-api
- collection_type: open
  name: Stream Chat API (Server-side REST) Application Channels API
  slug: open-getstream-channels-api
- collection_type: open
  name: Stream Chat API (Server-side REST) Application Devices API
  slug: open-getstream-devices-api
- collection_type: open
  name: Stream Chat API (Server-side REST) Application Members API
  slug: open-getstream-members-api
- collection_type: open
  name: Stream Chat API (Server-side REST) Application Messages API
  slug: open-getstream-messages-api
- collection_type: open
  name: Stream Chat API (Server-side REST) Application Moderation API
  slug: open-getstream-moderation-api
- collection_type: open
  name: Stream Chat API (Server-side REST) Application Permissions API
  slug: open-getstream-permissions-api
- collection_type: open
  name: Stream Chat API (Server-side REST) Application Reactions API
  slug: open-getstream-reactions-api
- collection_type: open
  name: Stream Chat API (Server-side REST) Application Roles API
  slug: open-getstream-roles-api
- collection_type: open
  name: Stream Chat API (Server-side REST) Application Threads API
  slug: open-getstream-threads-api
- collection_type: open
  name: Stream Chat API (Server-side REST) Application Users API
  slug: open-getstream-users-api
- collection_type: open
  name: Stream Chat API (Server-side REST)
  slug: open-getstream
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/getstream-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/getstream-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/getstream-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/getstream-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/getstream-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GetStream
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getstream
- group: company
  title: ''
  type: Website
  url: https://getstream.io
- group: docs
  title: ''
  type: Documentation
  url: https://getstream.io/chat/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/getstream-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/getstream-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/getstream-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://getstream.io/blog/rss.xml
created: '2026-07-03'
description: Stream (GetStream.io) provides scalable, API-first infrastructure for in-app chat messaging, activity feeds, audio/video calling and livestreaming, and AI moderation. The server-side platform is a documented REST API (base https://chat.stream-io-api.com for Chat) with JWT authentication, complemented by client SDKs that open a persistent WebSocket connection to receive real-time events - message.new, typing.start, user.presence.changed, reaction.new, notification.* and periodic health.check heartbeats. Products are metered on monthly active users (Chat) and participant minutes (Video), with Free/Maker, Standard (Startup) and Enterprise tiers.
finops:
- name: Getstream Finops
  service_category: Communication and Collaboration
  slug: getstream-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/getstream.png
layout: provider
modified: '2026-07-03'
name: Stream
nav: Providers
network: true
overview: 'Stream publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Application API, Campaigns API, Channels API, and 9 more. Tagged areas include Chat, Messaging, Activity Feeds, Video, and Audio.


  The Stream catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Stream''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Getstream Plans Pricing
  plan_count: 4
  slug: getstream-plans-pricing
random_paper: 78
rate_limits:
- limit_count: 4
  name: Getstream Rate Limits
  slug: getstream-rate-limits
rules:
- name: Stream API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: getstream-asyncapi-spectral-rules
score:
  band: developing
  composite: 46.8
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 63.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 46.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/getstream/refs/heads/main/screenshots/getstream-2026-07-25T215745.png
security:
- kind: authentication
  name: Getstream Authentication
  slug: getstream-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Getstream Domain Security
  slug: getstream-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Getstream Vulnerability Disclosure
  slug: getstream-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Getstream Trust Center
  slug: getstream-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: getstream
tags:
- Chat
- Messaging
- Activity Feeds
- Video
- Audio
- Moderation
- WebSocket
- Real Time
website: https://getstream.io
---

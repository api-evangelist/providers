---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.3
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 497
  human_in_the_loop: 18
  name: Getstream Agentic Access
  operation_count: 659
  slug: getstream-agentic-access
  summary_line: 659 operations · 497 acting · 18 human-in-the-loop
api_count: 6
apis:
- description: 'Build scalable activity feeds and timelines - add activities to feeds, follow and unfollow feeds, aggregate and rank activities, and fan out to followers. Powers social timelines, notification feeds, '
  name: Stream Activity Feeds API
  slug: getstream-activity-feeds-api
- description: Create and manage audio/video calls and livestreams - get-or-create calls, manage call members and permissions, start and stop recording, transcription, and broadcasting. Metered on participant minute
  name: Stream Video and Audio API
  slug: getstream-video-audio-api
- baseURL: https://api.stream-io-api.com
  baseurl_source: declared
  description: The product:chat API from Stream — 194 operation(s) for product:chat.
  name: Stream Product:chat API
  slug: getstream-product-chat-api
- baseURL: https://api.stream-io-api.com
  baseurl_source: declared
  description: The product:common API from Stream — 54 operation(s) for product:common.
  name: Stream Product:common API
  slug: getstream-product-common-api
- baseURL: https://api.stream-io-api.com
  baseurl_source: declared
  description: The product:feeds API from Stream — 69 operation(s) for product:feeds.
  name: Stream Product:feeds API
  slug: getstream-product-feeds-api
- baseURL: https://api.stream-io-api.com
  baseurl_source: declared
  description: The product:moderation API from Stream — 56 operation(s) for product:moderation.
  name: Stream Product:moderation API
  slug: getstream-product-moderation-api
- baseURL: https://api.stream-io-api.com
  baseurl_source: declared
  description: The product:video API from Stream — 121 operation(s) for product:video.
  name: Stream Product:video API
  slug: getstream-product-video-api
artifact_total: 32
asyncapis:
- description: AsyncAPI 2.6 description of Stream (GetStream.io) Chat's **real-time WebSocket** surface. Unlike the request/response server-side REST API (`https://chat.stream-io-api.com`, modeled in `openapi/getstr
  name: Stream Chat Realtime WebSocket API
  slug: getstream-asyncapi
- description: AsyncAPI description of the Stream (GetStream) Chat realtime WebSocket API. Clients connect to `wss://chat.stream-io-api.com/connect` with a JWT user token and receive a stream of JSON events. Event t
  name: Stream Chat WebSocket API
  slug: stream-io-asyncapi
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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/getstream/refs/heads/main/capabilities/getstream-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/getstream-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getstream/refs/heads/main/agentic-access/getstream-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/getstream-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getstream/refs/heads/main/security/getstream-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/getstream-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getstream/refs/heads/main/security/getstream-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/getstream-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getstream/refs/heads/main/security/getstream-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getstream-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getstream/refs/heads/main/authentication/getstream-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/getstream/refs/heads/main/plans/getstream-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/getstream-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/getstream/refs/heads/main/rate-limits/getstream-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/getstream-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/getstream/refs/heads/main/finops/getstream-finops.yml
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
overview: 'Stream publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Product:chat API, Product:common API, Product:feeds API, and 2 more. Tagged areas include Chat, Messaging, Activity Feeds, Video, and Audio.


  The Stream catalog on APIs.io includes 2 event-driven AsyncAPI specifications and 1 Spectral governance ruleset.


  Stream''s developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Getstream Plans Pricing
  plan_count: 4
  slug: getstream-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 4
  name: Getstream Rate Limits
  slug: getstream-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Stream API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: getstream-asyncapi-spectral-rules
score:
  band: developing
  composite: 52.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 70.8
    catalog_earned_first_party: 0.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 47.4
    contract_governance: 11.4
    contract_quality: 62.8
    developer_ergonomics: 38.1
    discoverability: 74.1
    operational_transparency: 34.2
  previous_composite: 50.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 72.2
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
- Real-Time
website: https://getstream.io
---

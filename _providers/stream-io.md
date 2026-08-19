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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 497
  human_in_the_loop: 18
  name: Stream Io Agentic Access
  operation_count: 659
  slug: stream-io-agentic-access
  summary_line: 659 operations · 497 acting · 18 human-in-the-loop
api_count: 6
apis:
- description: Server-side REST API for activity feeds — flat, aggregated, notification and ranked feeds, follow graph, reactions and personalisation. Powered by Stream's original feed engine.
  name: Stream Activity Feeds API
  slug: feeds
- description: The product:chat API from Stream — 194 operation(s) for product:chat.
  name: Stream product:chat API
  slug: stream-io-product-chat-api
- description: The product:common API from Stream — 54 operation(s) for product:common.
  name: Stream product:common API
  slug: stream-io-product-common-api
- description: The product:feeds API from Stream — 69 operation(s) for product:feeds.
  name: Stream product:feeds API
  slug: stream-io-product-feeds-api
- description: The product:moderation API from Stream — 56 operation(s) for product:moderation.
  name: Stream product:moderation API
  slug: stream-io-product-moderation-api
- description: The product:video API from Stream — 121 operation(s) for product:video.
  name: Stream product:video API
  slug: stream-io-product-video-api
artifact_total: 26
asyncapis:
- description: AsyncAPI description of the Stream (GetStream) Chat realtime WebSocket API. Clients connect to `wss://chat.stream-io-api.com/connect` with a JWT user token and receive a stream of JSON events. Event t
  name: Stream Chat WebSocket API
  slug: stream-io-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Stream API
  slug: open-stream-io-chat
- collection_type: open
  name: Stream API
  slug: open-stream-io-moderation
- collection_type: open
  name: Stream product:chat API
  slug: open-stream-io-product-chat-api
- collection_type: open
  name: Stream product:chat product:common API
  slug: open-stream-io-product-common-api
- collection_type: open
  name: Stream product:chat product:feeds API
  slug: open-stream-io-product-feeds-api
- collection_type: open
  name: Stream product:chat product:moderation API
  slug: open-stream-io-product-moderation-api
- collection_type: open
  name: Stream product:chat product:video API
  slug: open-stream-io-product-video-api
- collection_type: open
  name: Stream API
  slug: open-stream-io-serverside
- collection_type: open
  name: Stream API
  slug: open-stream-io-video
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stream-io-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/stream-io-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/stream-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stream-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stream-io-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getstream
- group: company
  title: ''
  type: Website
  url: https://getstream.io/
- group: docs
  title: ''
  type: Documentation
  url: https://getstream.io/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://getstream.io/pricing/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/GetStream
- group: start
  title: ''
  type: ProtocolPortal
  url: https://getstream.github.io/protocol/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getstream.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/stream-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stream-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/stream-io-finops.yml
created: '2026-05-08'
description: Stream provides realtime APIs for chat messaging, video and audio (calls and rooms), activity feeds and moderation. Hosted on a global edge network with native SDKs for web, mobile (iOS, Android, Flutter, React Native) and game engines (Unity, Unreal). Stream publishes full OpenAPI specifications for its Chat, Video and Moderation server-side APIs.
finops:
- name: Stream Io Finops
  service_category: Realtime Communications
  slug: stream-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stream-io.png
layout: provider
modified: '2026-05-29'
name: Stream
nav: Providers
network: true
overview: 'Stream publishes 5 APIs on the [APIs.io](https://apis.io/) network, including product:chat API, product:common API, product:feeds API, and 2 more. Tagged areas include Realtime, Chat, Messaging, Video, and Audio.


  The Stream catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Stream''s developer surface includes authentication, documentation, pricing, GitHub presence, and 11 more developer resources.'
plans:
- name: Stream Io Plans Pricing
  plan_count: 8
  slug: stream-io-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Stream Io Rate Limits
  slug: stream-io-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Stream API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: stream-io-asyncapi-spectral-rules
score:
  band: thin
  composite: 38.6
  delta: -3.4
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 11.4
    contract_quality: 61.1
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 11.4
    operational_transparency: 26.3
  previous_composite: 42.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stream-io/refs/heads/main/screenshots/stream-io-2026-06-20T194617.png
security:
- kind: authentication
  name: Stream Io Authentication
  slug: stream-io-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Stream Io Domain Security
  slug: stream-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Stream Io Vulnerability Disclosure
  slug: stream-io-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Stream Io Trust Center
  slug: stream-io-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: stream-io
tags:
- Realtime
- Chat
- Messaging
- Video
- Audio
- Activity Feeds
- Moderation
- SDK
website: https://getstream.io/
---

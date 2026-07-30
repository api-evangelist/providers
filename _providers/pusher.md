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
- acting_count: 3
  human_in_the_loop: 1
  name: Pusher Agentic Access
  operation_count: 6
  slug: pusher-agentic-access
  summary_line: 6 operations · 3 acting · 1 human-in-the-loop
api_count: 5
apis:
- description: 'Pub/sub channels over WebSocket (client) and HTTP (server publish). Public, private, and presence channels supported. WebSocket endpoint at ws-{cluster}.pusher.com. Cluster hostnames include eu, us2, '
  name: Pusher Channels API
  slug: channels-api
- description: Server API for sending iOS, Android, and Web push notifications via FCM, APNs, and Web Push.
  name: Pusher Beams API
  slug: beams-api
- description: The Channels API from Pusher — 3 operation(s) for channels.
  name: Pusher Channels API
  slug: pusher-channels-api
- description: The Events API from Pusher — 2 operation(s) for events.
  name: Pusher Events API
  slug: pusher-events-api
- description: The Users API from Pusher — 1 operation(s) for users.
  name: Pusher Users API
  slug: pusher-users-api
artifact_total: 17
asyncapis:
- description: AsyncAPI definition of the Pusher Channels public WebSocket wire protocol (protocol version 7). Pusher Channels is a pub/sub realtime messaging service. Clients connect over WebSocket to `ws-{cluster}
  name: Pusher Channels WebSocket Protocol
  slug: pusher-asyncapi
collections:
- collection_type: open
  name: Pusher Channels HTTP API
  slug: open-pusher
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pusher-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pusher-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pusher-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pusher-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pusher-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pusher-app
- group: start
  title: ''
  type: Portal
  url: https://pusher.com/
- group: docs
  title: ''
  type: Documentation
  url: https://pusher.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://pusher.com/channels/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/pusher
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pusher.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/pusher-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pusher-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pusher-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://pusher.com/blog
created: '2026-05-08'
description: Pusher is a realtime communication platform owned by MessageBird/Bird. Its primary product Channels provides pub/sub messaging over WebSocket and HTTP; Beams provides device push notifications. Authentication uses an app key + secret per Pusher app. Channels and Beams are still actively sold; the older Chatkit product was sunset.
finops:
- name: Pusher Finops
  service_category: Realtime Infrastructure
  slug: pusher-finops
graphqls:
- description: This conceptual GraphQL schema models the Pusher platform — covering both **Pusher Channels** (real-time pub/sub messaging over WebSocket and HTTP) and **Pusher Beams** (cross-platform push notificati
  name: Pusher GraphQL Schema
  slug: pusher-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pusher.png
layout: provider
modified: '2026-05-29'
name: Pusher
nav: Providers
network: true
overview: 'Pusher publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Channels API, Events API, and 2 more. Tagged areas include Realtime, WebSockets, Pub/Sub, Push Notifications, and Messaging.


  The Pusher catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Pusher''s developer surface includes authentication, developer portal, documentation, pricing, GitHub presence, engineering blog, and 9 more developer resources.'
plans:
- name: Pusher Plans Pricing
  plan_count: 9
  slug: pusher-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 9
  name: Pusher Rate Limits
  slug: pusher-rate-limits
rules:
- name: Pusher API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: pusher-asyncapi-spectral-rules
score:
  band: developing
  composite: 50.7
  delta: -5.8
  facets:
    commercial_clarity: 57.9
    contract_quality: 68.6
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 52.6
  previous_composite: 56.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 31.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/pusher/refs/heads/main/screenshots/pusher-2026-06-20T192318.png
security:
- kind: authentication
  name: Pusher Authentication
  slug: pusher-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pusher Domain Security
  slug: pusher-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pusher Vulnerability Disclosure
  slug: pusher-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Pusher Trust Center
  slug: pusher-trust-center
  summary_line: ISO 27001, HIPAA, GDPR
slug: pusher
tags:
- Realtime
- WebSockets
- Pub/Sub
- Push Notifications
- Messaging
website: https://pusher.com/
---

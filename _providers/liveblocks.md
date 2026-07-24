---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 60.6
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Liveblocks Agentic Access
  operation_count: 39
  slug: liveblocks-agentic-access
  summary_line: 39 operations · 25 acting
api_count: 12
apis:
- description: 'Server-side REST API for managing rooms, room access, storage, active users, broadcast events, comments and threads, notifications, Yjs documents, and version history. Authenticated with a secret key '
  name: Liveblocks REST API
  slug: rest-api
- description: Public-facing authorization endpoint used by client SDKs to exchange a server-issued token for a Liveblocks session. Supports access token and ID token authorization patterns.
  name: Liveblocks Authorization API
  slug: authorization-api
- description: WebSocket-based client API exposed through Liveblocks client SDKs for React, JavaScript, Redux, Zustand, Vue (community), and Yjs. Provides presence, broadcast events, Live storage data structures, an
  name: Liveblocks Realtime Client API
  slug: realtime-client-api
- description: The Active Users API from Liveblocks — 2 operation(s) for active users.
  name: Liveblocks Active Users API
  slug: liveblocks-active-users-api
- description: The Comments API from Liveblocks — 2 operation(s) for comments.
  name: Liveblocks Comments API
  slug: liveblocks-comments-api
- description: The Events API from Liveblocks — 1 operation(s) for events.
  name: Liveblocks Events API
  slug: liveblocks-events-api
- description: The Reactions API from Liveblocks — 2 operation(s) for reactions.
  name: Liveblocks Reactions API
  slug: liveblocks-reactions-api
- description: The Rooms API from Liveblocks — 6 operation(s) for rooms.
  name: Liveblocks Rooms API
  slug: liveblocks-rooms-api
- description: The Storage API from Liveblocks — 2 operation(s) for storage.
  name: Liveblocks Storage API
  slug: liveblocks-storage-api
- description: The Threads API from Liveblocks — 9 operation(s) for threads.
  name: Liveblocks Threads API
  slug: liveblocks-threads-api
- description: The Versions API from Liveblocks — 3 operation(s) for versions.
  name: Liveblocks Versions API
  slug: liveblocks-versions-api
- description: The Yjs API from Liveblocks — 2 operation(s) for yjs.
  name: Liveblocks Yjs API
  slug: liveblocks-yjs-api
artifact_total: 23
asyncapis:
- description: ''
  name: Review
  slug: review
collections:
- collection_type: open
  name: Liveblocks REST API
  slug: open-liveblocks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/liveblocks-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/liveblocks-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/liveblocks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/liveblocks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/liveblocks-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://liveblocks.io
- group: start
  title: ''
  type: Portal
  url: https://liveblocks.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://liveblocks.io/docs
- group: start
  title: ''
  type: Signup
  url: https://liveblocks.io/signup
- group: start
  title: ''
  type: Login
  url: https://liveblocks.io/dashboard
- group: commercial
  title: ''
  type: Pricing
  url: https://liveblocks.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://liveblocks.io/blog
- group: build
  title: ''
  type: GitHub
  url: https://github.com/liveblocks/liveblocks
- group: build
  title: ''
  type: Examples
  url: https://liveblocks.io/examples
- group: operate
  title: ''
  type: ChangeLog
  url: https://liveblocks.io/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.liveblocks.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://liveblocks.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://liveblocks.io/privacy
- group: operate
  title: ''
  type: Support
  url: https://liveblocks.io/support
- group: operate
  title: ''
  type: Community
  url: https://liveblocks.io/discord
- group: agent
  title: ''
  type: LlmsText
  url: https://liveblocks.io/llms.txt
created: '2026-05-23'
description: Liveblocks is a real-time collaboration platform that provides ready-made building blocks for multiplayer experiences, including presence, broadcast events, shared storage (LiveObject/LiveList/LiveMap), comments and threads, notifications, and Yjs-based collaborative documents. It exposes a public authorization endpoint, a server-side private REST API, and SDKs for React, JavaScript, Node.js, Python, Redux, Zustand, and Yjs.
finops:
- name: Liveblocks Finops
  service_category: API
  slug: liveblocks-finops
graphqls:
- description: Conceptual GraphQL schema for the [Liveblocks](https://liveblocks.io) collaborative presence and real-time sync platform.
  name: Liveblocks GraphQL Schema
  slug: liveblocks-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/liveblocks.png
layout: provider
modified: '2026-05-23'
name: Liveblocks
nav: Providers
network: true
overview: 'Liveblocks publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Active Users API, Comments API, Events API, and 6 more. Tagged areas include Real-Time, Collaboration, Multiplayer, Presence, and CRDT.


  The Liveblocks catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Liveblocks'' developer surface includes authentication, developer portal, documentation, signup flow, pricing, engineering blog, GitHub presence, and 14 more developer resources.'
plans:
- name: Liveblocks Plans Pricing
  plan_count: 1
  slug: liveblocks-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 2
  name: Liveblocks Rate Limits
  slug: liveblocks-rate-limits
score:
  band: developing
  composite: 53.3
  delta: 0.0
  facets:
    commercial_clarity: 81.6
    contract_quality: 63.1
    developer_ergonomics: 34.8
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 57.9
  previous_composite: 53.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/liveblocks/refs/heads/main/screenshots/liveblocks-2026-06-20T184615.png
security:
- kind: authentication
  name: Liveblocks Authentication
  slug: liveblocks-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Liveblocks Domain Security
  slug: liveblocks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Liveblocks Vulnerability Disclosure
  slug: liveblocks-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Liveblocks Trust Center
  slug: liveblocks-trust-center
  summary_line: SOC 2, HIPAA
slug: liveblocks
tags:
- Real-Time
- Collaboration
- Multiplayer
- Presence
- CRDT
- Yjs
- Comments
- Threads
- Notifications
- WebSockets
website: https://liveblocks.io
---

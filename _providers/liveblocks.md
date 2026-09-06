---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Liveblocks Agentic Access
  operation_count: 39
  slug: liveblocks-agentic-access
  summary_line: 39 operations · 25 acting
api_count: 1
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
- baseURL: https://api.liveblocks.io/v2
  baseurl_source: declared
  description: The Active Users API from Liveblocks — 2 operation(s) for active users.
  name: Liveblocks Active Users API
  slug: liveblocks-active-users-api
- baseURL: https://api.liveblocks.io/v2
  baseurl_source: declared
  description: The Comments API from Liveblocks — 2 operation(s) for comments.
  name: Liveblocks Comments API
  slug: liveblocks-comments-api
- baseURL: https://api.liveblocks.io/v2
  baseurl_source: declared
  description: The Events API from Liveblocks — 1 operation(s) for events.
  name: Liveblocks Events API
  slug: liveblocks-events-api
- baseURL: https://api.liveblocks.io/v2
  baseurl_source: declared
  description: The Reactions API from Liveblocks — 2 operation(s) for reactions.
  name: Liveblocks Reactions API
  slug: liveblocks-reactions-api
- baseURL: https://api.liveblocks.io/v2
  baseurl_source: declared
  description: The Rooms API from Liveblocks — 6 operation(s) for rooms.
  name: Liveblocks Rooms API
  slug: liveblocks-rooms-api
- baseURL: https://api.liveblocks.io/v2
  baseurl_source: declared
  description: The Storage API from Liveblocks — 2 operation(s) for storage.
  name: Liveblocks Storage API
  slug: liveblocks-storage-api
- baseURL: https://api.liveblocks.io/v2
  baseurl_source: declared
  description: The Threads API from Liveblocks — 9 operation(s) for threads.
  name: Liveblocks Threads API
  slug: liveblocks-threads-api
- baseURL: https://api.liveblocks.io/v2
  baseurl_source: declared
  description: The Versions API from Liveblocks — 3 operation(s) for versions.
  name: Liveblocks Versions API
  slug: liveblocks-versions-api
- baseURL: https://api.liveblocks.io/v2
  baseurl_source: declared
  description: The Yjs API from Liveblocks — 2 operation(s) for yjs.
  name: Liveblocks Yjs API
  slug: liveblocks-yjs-api
artifact_total: 33
asyncapis:
- description: ''
  name: Review
  slug: review
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Liveblocks REST Active Users API
  slug: open-liveblocks-active-users-api
- collection_type: open
  name: Liveblocks REST Active Users Comments API
  slug: open-liveblocks-comments-api
- collection_type: open
  name: Liveblocks REST Active Users Events API
  slug: open-liveblocks-events-api
- collection_type: open
  name: Liveblocks REST Active Users Reactions API
  slug: open-liveblocks-reactions-api
- collection_type: open
  name: Liveblocks REST Active Users Rooms API
  slug: open-liveblocks-rooms-api
- collection_type: open
  name: Liveblocks REST Active Users Storage API
  slug: open-liveblocks-storage-api
- collection_type: open
  name: Liveblocks REST Active Users Threads API
  slug: open-liveblocks-threads-api
- collection_type: open
  name: Liveblocks REST Active Users Versions API
  slug: open-liveblocks-versions-api
- collection_type: open
  name: Liveblocks REST Active Users Yjs API
  slug: open-liveblocks-yjs-api
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
random_paper: 20
rate_limits:
- limit_count: 2
  name: Liveblocks Rate Limits
  slug: liveblocks-rate-limits
score:
  band: strong
  composite: 58.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 75.0
    commercial_clarity: 75.0
    contract_governance: 0.0
    contract_quality: 69.2
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 65.8
  previous_composite: 58.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Notification
- WebSockets
website: https://liveblocks.io
---

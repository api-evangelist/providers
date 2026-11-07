---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
  band: agent-ready
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.5
  scored_at: '2026-11-06'
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
  description: The Comments API from Liveblocks — 2 operation(s) for comments.
  name: Liveblocks Comments API
  slug: liveblocks-comments-api
- baseURL: https://api.liveblocks.io/v2
  baseurl_source: declared
  description: The Storage API from Liveblocks — 2 operation(s) for storage.
  name: Liveblocks Storage API
  slug: liveblocks-storage-api
- baseURL: https://api.liveblocks.io/v2
  baseurl_source: declared
  description: The Yjs API from Liveblocks — 2 operation(s) for yjs.
  name: Liveblocks Yjs API
  slug: liveblocks-yjs-api
- baseURL: https://api.liveblocks.io/v2
  baseurl_source: declared
  description: The AI API from Liveblocks — 9 operation(s) for ai.
  name: Liveblocks AI API
  slug: liveblocks-ai-api
- baseURL: https://api.liveblocks.io/v2
  baseurl_source: declared
  description: The Auth API from Liveblocks — 2 operation(s) for auth.
  name: Liveblocks Auth API
  slug: liveblocks-auth-api
- baseURL: https://api.liveblocks.io/v2
  baseurl_source: declared
  description: The Feeds API from Liveblocks — 4 operation(s) for feeds.
  name: Liveblocks Feeds API
  slug: liveblocks-feeds-api
- baseURL: https://api.liveblocks.io/v2
  baseurl_source: declared
  description: The Groups API from Liveblocks — 5 operation(s) for groups.
  name: Liveblocks Groups API
  slug: liveblocks-groups-api
- baseURL: https://api.liveblocks.io/v2
  baseurl_source: declared
  description: The Management API from Liveblocks — 13 operation(s) for management.
  name: Liveblocks Management API
  slug: liveblocks-management-api
- baseURL: https://api.liveblocks.io/v2
  baseurl_source: declared
  description: The Notifications API from Liveblocks — 8 operation(s) for notifications.
  name: Liveblocks Notifications API
  slug: liveblocks-notifications-api
- baseURL: https://api.liveblocks.io/v2
  baseurl_source: declared
  description: The Room API from Liveblocks — 9 operation(s) for room.
  name: Liveblocks Room API
  slug: liveblocks-room-api
- baseURL: https://api.liveblocks.io/v2
  baseurl_source: declared
  description: The Version History API from Liveblocks — 3 operation(s) for version history.
  name: Liveblocks Version History API
  slug: liveblocks-version-history-api
artifact_total: 35
asyncapis:
- description: ''
  name: Review
  slug: review
collections:
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
- group: other
  href: https://artifacts.apis.io/liveblocks/capabilities/liveblocks-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/liveblocks-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/liveblocks/plans/liveblocks-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/liveblocks-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/liveblocks/rate-limits/liveblocks-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/liveblocks-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/liveblocks/finops/liveblocks-finops.yml
  title: ''
  type: FinOps
  url: finops/liveblocks-finops.yml
- group: agent
  href: https://artifacts.apis.io/liveblocks/agentic-access/liveblocks-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/liveblocks-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/liveblocks/security/liveblocks-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/liveblocks-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/liveblocks/security/liveblocks-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/liveblocks-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/liveblocks/security/liveblocks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/liveblocks-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/liveblocks/authentication/liveblocks-authentication.yml
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
- has_sources: true
  method: derived
  name: Liveblocks Finops
  primary_unit: month billed annually
  service_category: ''
  slug: liveblocks-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/liveblocks.png
layout: provider
modified: '2026-05-23'
name: Liveblocks
nav: Providers
network: true
overview: 'Liveblocks publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Comments API, Storage API, Yjs API, and 11 more. Tagged areas include Real-Time, Collaboration, Multiplayer, Presence, and CRDT.


  The Liveblocks catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Liveblocks'' developer surface includes authentication, developer portal, documentation, signup flow, pricing, engineering blog, GitHub presence, and 18 more developer resources.'
plans:
- name: Liveblocks Plans Pricing
  plan_count: 4
  slug: liveblocks-plans-pricing
- name: Liveblocks Price Estimates
  plan_count: 0
  slug: liveblocks-price-estimates
random_paper: 14
rate_limits:
- limit_count: 2
  name: Liveblocks Rate Limits
  slug: liveblocks-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Liveblocks API Rules
  rule_count: 56
  severity_counts:
    error: 44
    hint: 0
    info: 4
    warn: 8
  slug: liveblocks-rules
score:
  band: strong
  composite: 65.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 58.5
    catalog_earned_first_party: 12.0
    catalog_gap: 56.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 85.5
    contract_governance: 13.6
    contract_quality: 66.0
    developer_ergonomics: 52.4
    discoverability: 73.2
    operational_transparency: 60.5
  previous_composite: 65.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 52.4
      total: 21
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/liveblocks/liveblocks-2026-06-20T184615.png
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
  summary_line: no policy recorded
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
- WebSocket
website: https://liveblocks.io
---

---
access_model:
  confidence: high
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Atproto Agentic Access
  operation_count: 37
  slug: atproto-agentic-access
  summary_line: 37 operations · 11 acting
api_count: 9
apis:
- description: Public WebSocket event stream providing real-time access to all public activity on the AT Protocol network, including posts, likes, follows, and other repository events. No API key is required to subs
  name: AT Protocol Firehose (Event Stream)
  slug: firehose
- description: Actor (user) profile, search, and preference operations
  name: AT Protocol actor API
  slug: atproto-actor-api
- description: Feed, post, timeline, and content operations
  name: AT Protocol feed API
  slug: atproto-feed-api
- description: Graph operations — follows, blocks, lists, and mutes
  name: AT Protocol graph API
  slug: atproto-graph-api
- description: DID and handle resolution, identity management
  name: AT Protocol identity API
  slug: atproto-identity-api
- description: Notification management
  name: AT Protocol notification API
  slug: atproto-notification-api
- description: Repository management, record CRUD operations
  name: AT Protocol repo API
  slug: atproto-repo-api
- description: Server management, session creation, account administration
  name: AT Protocol server API
  slug: atproto-server-api
- description: Data synchronization, firehose, blob access
  name: AT Protocol sync API
  slug: atproto-sync-api
artifact_total: 24
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/atproto-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/atproto-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/atproto-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://atproto.com/
- group: docs
  title: ''
  type: Documentation
  url: https://atproto.com/guides/overview
- group: company
  title: ''
  type: Blog
  url: https://atproto.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bluesky-social
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bluesky-pbc
- group: other
  title: ''
  type: X
  url: https://twitter.com/at_protocol
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bsky.app/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/bluesky-social/atproto/tree/main/packages
- group: build
  title: ''
  type: SDKs
  url: https://github.com/bluesky-social/indigo
- group: commercial
  title: ''
  type: Plans
  url: plans/atproto-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/atproto-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/atproto-finops.yml
created: '2026-06-12'
description: AT Protocol (Authenticated Transfer Protocol) is an open, federated social networking protocol developed by Bluesky Social PBC that powers the Bluesky social network and its 40M+ users. The protocol defines a public HTTP API surface via XRPC (cross-resolver protocol calls) organized under Lexicon schemas that cover identity (DIDs and handles), repository management, feed generation, labeling, and moderation. Developers can tap into a public firehose WebSocket event stream without API keys, and write operations use OAuth 2.0 or JWT bearer tokens for authentication. All data is stored in user-owned signed repositories and is 100% publicly accessible, making the protocol suitable for building social apps, feed generators, labelers, and bots.
examples:
- key_count: 4
  name: Atproto Createrecord Example
  slug: atproto-createRecord-example
- key_count: 4
  name: Atproto Createsession Example
  slug: atproto-createSession-example
- key_count: 4
  name: Atproto Getprofile Example
  slug: atproto-getProfile-example
- key_count: 4
  name: Atproto Gettimeline Example
  slug: atproto-getTimeline-example
finops:
- name: Atproto Finops
  service_category: Social Networking
  slug: atproto-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/atproto.png
json_schemas:
- name: Bluesky Post (app.bsky.feed.post)
  property_count: 9
  slug: atproto-post
- name: Bluesky Profile View Detailed (app.bsky.actor.defs#profileViewDetailed)
  property_count: 14
  slug: atproto-profile
- name: AT Protocol Session
  property_count: 10
  slug: atproto-session
jsonld:
- class_count: 17
  name: Atproto Context
  property_count: 43
  slug: atproto-context
layout: provider
modified: '2026-06-12'
name: AT Protocol
nav: Providers
network: true
overview: 'AT Protocol publishes 8 APIs on the [APIs.io](https://apis.io/) network, including actor API, feed API, graph API, and 5 more. Tagged areas include Social Networking, Decentralized, Federated, Open Source, and Bluesky.


  The AT Protocol catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AT Protocol''s developer surface includes authentication, documentation, engineering blog, and 12 more developer resources.'
plans:
- name: Atproto Plans Pricing
  plan_count: 3
  slug: atproto-plans-pricing
random_paper: 81
rate_limits:
- limit_count: 17
  name: Atproto Rate Limits
  slug: atproto-rate-limits
rules:
- name: AT Protocol API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: atproto-jsonschema-spectral-rules
score:
  band: developing
  composite: 52.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 72.1
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 52.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Atproto Authentication
  slug: atproto-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Atproto Domain Security
  slug: atproto-domain-security
  summary_line: TLSv1.3 · DMARC
slug: atproto
tags:
- Social Networking
- Decentralized
- Federated
- Open Source
- Bluesky
- Fediverse
- Identity
- XRPC
- Lexicon
website: https://atproto.com/
---

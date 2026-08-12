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
  band: agent-aware
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 8
  human_in_the_loop: 3
  name: At Protocol Agentic Access
  operation_count: 20
  slug: at-protocol-agentic-access
  summary_line: 20 operations · 8 acting · 3 human-in-the-loop
api_count: 12
apis:
- description: XRPC is the AT Protocol's HTTP-based remote procedure call layer. All protocol interactions — querying records, writing records, subscribing to streams, resolving identity, moderating content — are ex
  name: AT Protocol XRPC API
  slug: atproto-xrpc
- description: Lexicon is the schema definition language for AT Protocol. Every record type, XRPC method, and event subscription on the network is described by a Lexicon document, which acts as both contract and cod
  name: AT Protocol Lexicon Schemas
  slug: lexicon
- description: The PDS hosts a user's repository of signed records and exposes the com.atproto.* XRPC methods for account creation, authentication, record CRUD, blob upload, and repository sync. A PDS is the home se
  name: Personal Data Server (PDS) API
  slug: pds-api
- description: The Relay aggregates the com.atproto.sync.subscribeRepos firehose across PDS hosts and re-broadcasts the combined event stream over WebSocket. AppViews and indexers subscribe to a Relay to get a near-
  name: AT Protocol Relay & Firehose
  slug: relay-firehose
- description: The Bluesky AppView indexes the firehose and exposes the app.bsky.* XRPC methods that the Bluesky client (and any compatible client) uses to render timelines, threads, profiles, notifications, search,
  name: Bluesky AppView API
  slug: bsky-appview
- description: 'Identity in AT Protocol is anchored in DIDs (did:plc or did:web), with human-readable handles resolved through DNS TXT records or well-known HTTP endpoints. The protocol specifies how DIDs map to PDS '
  name: AT Protocol Identity (DID & Handles)
  slug: identity-did
- description: Bluesky actor profiles (app.bsky.actor.*)
  name: AT Protocol Actor API
  slug: at-protocol-actor-api
- description: Bluesky feeds, posts, and threads (app.bsky.feed.*)
  name: AT Protocol Feed API
  slug: at-protocol-feed-api
- description: Follow, mute, and block graph (app.bsky.graph.*)
  name: AT Protocol Graph API
  slug: at-protocol-graph-api
- description: DID and handle resolution (com.atproto.identity.*)
  name: AT Protocol Identity API
  slug: at-protocol-identity-api
- description: Repository record CRUD (com.atproto.repo.*)
  name: AT Protocol Repo API
  slug: at-protocol-repo-api
- description: Session and account management (com.atproto.server.*)
  name: AT Protocol Server API
  slug: at-protocol-server-api
artifact_total: 21
asyncapis:
- description: AsyncAPI definition for the AT Protocol event subscription surface. AT Protocol defines streaming endpoints as Lexicon "subscription" types, served over WebSocket using length-prefixed binary frames e
  name: AT Protocol Firehose & Event Streams
  slug: at-protocol-asyncapi
collections:
- collection_type: open
  name: AT Protocol XRPC API
  slug: open-at-protocol
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/bluesky-social/atproto/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/bluesky-social/atproto/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/bluesky-social/atproto/blob/main/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/bluesky-social/atproto/blob/main/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/at-protocol-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/at-protocol-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/at-protocol-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://atproto.com/
- group: docs
  title: ''
  type: Documentation
  url: https://atproto.com/guides/overview
- group: docs
  title: ''
  type: Specification
  url: https://atproto.com/specs/atp
- group: build
  title: ''
  type: SDKs
  url: https://atproto.com/sdks
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bluesky-social
- group: docs
  title: ''
  type: ReferenceImplementation
  url: https://github.com/bluesky-social/atproto
- group: other
  title: ''
  type: GoImplementation
  url: https://github.com/bluesky-social/indigo
- group: company
  title: ''
  type: Bluesky
  url: https://bsky.app/
- group: docs
  title: ''
  type: BlueskyDocs
  url: https://docs.bsky.app/
- group: company
  title: ''
  type: Blog
  url: https://bsky.social/about/blog
- group: learn
  title: ''
  type: Cookbook
  url: https://github.com/bluesky-social/cookbook
created: '2026-05-23'
description: The AT Protocol (atproto) is an open, federated networking protocol for social applications, originally developed by Bluesky Social PBC and the Bluesky team. It defines a decentralized architecture where user identity and data are portable across providers, anchored in DIDs, signed records, and content-addressed storage. The protocol is composed of independently operable services — Personal Data Servers (PDS), Relays (firehose aggregators), and AppViews (read-side indexers) — that communicate using XRPC and exchange records described by Lexicon schemas. Bluesky (bsky.app) is the reference application built on AT Protocol, but the protocol is designed for any social or social-adjacent application that wants user-owned identity, portable data, and an open federation model. Official and community SDKs exist for TypeScript, Go, Python, Rust, Dart, Swift, C#/.NET, Ruby, PHP, and more, and the full lexicon, network topology, and reference implementations are open source.
finops:
- name: At Protocol Finops
  service_category: API
  slug: at-protocol-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/at-protocol.png
layout: provider
modified: '2026-05-29'
name: AT Protocol
nav: Providers
network: true
overview: 'AT Protocol publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Relay & Firehose, Actor API, Feed API, and 4 more. Tagged areas include AT Protocol, atproto, Bluesky, Federation, and Decentralized Social.


  The AT Protocol catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  AT Protocol''s developer surface includes authentication, documentation, engineering blog, and 15 more developer resources.'
plans:
- name: At Protocol Plans Pricing
  plan_count: 1
  slug: at-protocol-plans-pricing
random_paper: 96
rate_limits:
- limit_count: 2
  name: At Protocol Rate Limits
  slug: at-protocol-rate-limits
rules:
- name: AT Protocol API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: at-protocol-asyncapi-spectral-rules
score:
  band: developing
  composite: 44.5
  delta: 3.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 55.2
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 52.6
  previous_composite: 41.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: At Protocol Authentication
  slug: at-protocol-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: At Protocol Domain Security
  slug: at-protocol-domain-security
  summary_line: TLSv1.3 · DMARC
slug: at-protocol
tags:
- AT Protocol
- atproto
- Bluesky
- Federation
- Decentralized Social
- Social Networking
- DID
- Lexicon
- XRPC
- PDS
- Relay
- AppView
- Open Protocol
website: https://atproto.com/
---

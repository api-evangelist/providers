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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 8
  human_in_the_loop: 3
  name: At Protocol Agentic Access
  operation_count: 20
  slug: at-protocol-agentic-access
  summary_line: 20 operations · 8 acting · 3 human-in-the-loop
api_count: 1
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
- baseURL: https://atproto.com/xrpc
  baseurl_source: declared
  description: Bluesky actor profiles (app.bsky.actor.*)
  name: AT Protocol Actor API
  slug: at-protocol-actor-api
- baseURL: https://atproto.com/xrpc
  baseurl_source: declared
  description: Bluesky feeds, posts, and threads (app.bsky.feed.*)
  name: AT Protocol Feed API
  slug: at-protocol-feed-api
- baseURL: https://atproto.com/xrpc
  baseurl_source: declared
  description: Follow, mute, and block graph (app.bsky.graph.*)
  name: AT Protocol Graph API
  slug: at-protocol-graph-api
- baseURL: https://atproto.com/xrpc
  baseurl_source: declared
  description: DID and handle resolution (com.atproto.identity.*)
  name: AT Protocol Identity API
  slug: at-protocol-identity-api
- baseURL: https://atproto.com/xrpc
  baseurl_source: declared
  description: Repository record CRUD (com.atproto.repo.*)
  name: AT Protocol Repo API
  slug: at-protocol-repo-api
- baseURL: https://atproto.com/xrpc
  baseurl_source: declared
  description: Session and account management (com.atproto.server.*)
  name: AT Protocol Server API
  slug: at-protocol-server-api
artifact_total: 28
asyncapis:
- description: AsyncAPI definition for the AT Protocol event subscription surface. AT Protocol defines streaming endpoints as Lexicon "subscription" types, served over WebSocket using length-prefixed binary frames e
  name: AT Protocol Firehose & Event Streams
  slug: at-protocol-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AT Protocol XRPC Actor API
  slug: open-at-protocol-actor-api
- collection_type: open
  name: AT Protocol XRPC Actor Feed API
  slug: open-at-protocol-feed-api
- collection_type: open
  name: AT Protocol XRPC Actor Graph API
  slug: open-at-protocol-graph-api
- collection_type: open
  name: AT Protocol XRPC Actor Identity API
  slug: open-at-protocol-identity-api
- collection_type: open
  name: AT Protocol XRPC Actor Repo API
  slug: open-at-protocol-repo-api
- collection_type: open
  name: AT Protocol XRPC Actor Server API
  slug: open-at-protocol-server-api
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
overview: 'AT Protocol publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Relay & Firehose, Actor API, Feed API, and 4 more. Tagged areas include At-Protocol, atproto, Bluesky, Federation, and Decentralized Social.


  The AT Protocol catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  AT Protocol''s developer surface includes authentication, documentation, engineering blog, and 15 more developer resources.'
plans:
- name: At Protocol Plans Pricing
  plan_count: 1
  slug: at-protocol-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: At Protocol Rate Limits
  slug: at-protocol-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: AT Protocol API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: at-protocol-asyncapi-spectral-rules
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 12
    catalog_gap: 55.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -4.4
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 11.4
    contract_quality: 50.3
    developer_ergonomics: 38.1
    discoverability: 68.5
    governance: 11.4
    operational_transparency: 50.0
  previous_composite: 45.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/at-protocol/refs/heads/main/screenshots/at-protocol-2026-08-17T122411.png
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
- At-Protocol
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

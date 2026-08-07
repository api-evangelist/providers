---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Ceramic Agentic Access
  operation_count: 30
  slug: ceramic-agentic-access
  summary_line: 30 operations · 5 acting
api_count: 10
apis:
- description: The Config API from Ceramic — 1 operation(s) for config.
  name: Ceramic Config API
  slug: ceramic-config-api
- description: The Debug API from Ceramic — 1 operation(s) for debug.
  name: Ceramic Debug API
  slug: ceramic-debug-api
- description: The Events API from Ceramic — 2 operation(s) for events.
  name: Ceramic Events API
  slug: ceramic-events-api
- description: The Experimental API from Ceramic — 2 operation(s) for experimental.
  name: Ceramic Experimental API
  slug: ceramic-experimental-api
- description: The Feed API from Ceramic — 2 operation(s) for feed.
  name: Ceramic Feed API
  slug: ceramic-feed-api
- description: The Interests API from Ceramic — 2 operation(s) for interests.
  name: Ceramic Interests API
  slug: ceramic-interests-api
- description: The Liveness API from Ceramic — 1 operation(s) for liveness.
  name: Ceramic Liveness API
  slug: ceramic-liveness-api
- description: The Peers API from Ceramic — 1 operation(s) for peers.
  name: Ceramic Peers API
  slug: ceramic-peers-api
- description: The Streams API from Ceramic — 1 operation(s) for streams.
  name: Ceramic Streams API
  slug: ceramic-streams-api
- description: The Version API from Ceramic — 1 operation(s) for version.
  name: Ceramic Version API
  slug: ceramic-version-api
artifact_total: 35
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ceramic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ceramic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ceramic.network/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.ceramic.network/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ceramicnetwork
- group: operate
  title: ''
  type: Discord
  url: https://chat.ceramic.network/
- group: operate
  title: ''
  type: Forums
  url: https://forum.ceramic.network/
- group: company
  title: ''
  type: Blog
  url: https://blog.ceramic.network/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ceramicnetwork
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ceramic.network/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ceramic.network/privacy-policy
- group: commercial
  title: ''
  type: Plans
  url: https://ceramic.network/plans
- group: operate
  title: ''
  type: RateLimits
  url: https://ceramic.network/rate-limits
- group: operate
  title: ''
  type: Status
  url: https://ceramic.network/status
created: '2026-06-13'
description: Ceramic is a decentralized data network built on a protocol for mutable event streams anchored to blockchain. It provides REST APIs for creating and updating mutable data streams, managing decentralized identifiers (DIDs), registering data interests, and reading stream state and events across the composable data network.
examples:
- key_count: 4
  name: Create Event
  slug: create-event
- key_count: 4
  name: Get Event Feed
  slug: get-event-feed
- key_count: 4
  name: Get Event
  slug: get-event
- key_count: 4
  name: Get Network Info
  slug: get-network-info
- key_count: 4
  name: Get Peers
  slug: get-peers
- key_count: 4
  name: Get Stream State
  slug: get-stream-state
- key_count: 4
  name: Register Interest
  slug: register-interest
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://ceramic.network/favicon.ico
json_schemas:
- name: Error response
  property_count: 1
  slug: ErrorResponse
- name: A Ceramic Event
  property_count: 2
  slug: Event
- name: A Ceramic Event Data Payload
  property_count: 1
  slug: EventData
- name: Ceramic Event feed data
  property_count: 2
  slug: EventFeed
- name: Information about multiple events.
  property_count: 3
  slug: EventsGet
- name: A recon interest
  property_count: 4
  slug: Interest
- name: Information about multiple interests.
  property_count: 1
  slug: InterestsGet
- name: Information about the Ceramic network
  property_count: 1
  slug: NetworkInfo
- name: Information about a connected peer
  property_count: 2
  slug: Peer
- name: List of Peers
  property_count: 1
  slug: Peers
- name: State of a Ceramic stream
  property_count: 5
  slug: StreamState
- name: Version
  property_count: 1
  slug: Version
layout: provider
modified: '2026-06-13'
name: Ceramic
nav: Providers
network: true
overview: 'Ceramic publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Config API, Debug API, Events API, and 7 more. Tagged areas include Decentralized, Web3, Data Streams, DID, and IPFS.


  The Ceramic catalog on APIs.io includes 1 Spectral governance ruleset.


  Ceramic''s developer surface includes documentation, GitHub presence, engineering blog, status page, and 10 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 46
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: Ceramic API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ceramic-jsonschema-spectral-rules
score:
  band: thin
  composite: 39.0
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 42.2
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ceramic/refs/heads/main/screenshots/ceramic-2026-06-20T174136.png
security:
- kind: domain-security
  name: Ceramic Domain Security
  slug: ceramic-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ceramic
tags:
- Decentralized
- Web3
- Data Streams
- DID
- IPFS
- Blockchain
- Event Streaming
- ComposeDB
website: https://ceramic.network/
---

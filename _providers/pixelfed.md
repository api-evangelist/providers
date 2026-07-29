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
    asyncapi_events: false
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Pixelfed Agentic Access
  operation_count: 68
  slug: pixelfed-agentic-access
  summary_line: 68 operations · 28 acting
api_count: 17
apis:
- description: Account management, follow/block/mute operations
  name: Pixelfed Accounts API
  slug: pixelfed-accounts-api
- description: Blocked accounts and muted accounts
  name: Pixelfed Blocks and Mutes API
  slug: pixelfed-blocks-and-mutes-api
- description: Bookmarked statuses
  name: Pixelfed Bookmarks API
  slug: pixelfed-bookmarks-api
- description: Pixelfed-specific photo collections (v1.1)
  name: Pixelfed Collections API
  slug: pixelfed-collections-api
- description: Pixelfed-specific direct messaging (v1.1)
  name: Pixelfed Direct Messages API
  slug: pixelfed-direct-messages-api
- description: Trending content, suggestions, and directory
  name: Pixelfed Discovery API
  slug: pixelfed-discovery-api
- description: Favourited statuses
  name: Pixelfed Favourites API
  slug: pixelfed-favourites-api
- description: Pending follow requests
  name: Pixelfed Follow Requests API
  slug: pixelfed-follow-requests-api
- description: Instance and federation metadata
  name: Pixelfed Instance API
  slug: pixelfed-instance-api
- description: List management and membership
  name: Pixelfed Lists API
  slug: pixelfed-lists-api
- description: Media upload and management
  name: Pixelfed Media API
  slug: pixelfed-media-api
- description: Notification retrieval and management
  name: Pixelfed Notifications API
  slug: pixelfed-notifications-api
- description: Web push subscription management (v1.1)
  name: Pixelfed Push Notifications API
  slug: pixelfed-push-notifications-api
- description: Full-text and entity search
  name: Pixelfed Search API
  slug: pixelfed-search-api
- description: Creating, reading, and interacting with statuses (posts)
  name: Pixelfed Statuses API
  slug: pixelfed-statuses-api
- description: Pixelfed-specific ephemeral stories (v1.1)
  name: Pixelfed Stories API
  slug: pixelfed-stories-api
- description: Home, public, tag, and list timelines
  name: Pixelfed Timelines API
  slug: pixelfed-timelines-api
artifact_total: 25
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pixelfed-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pixelfed-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pixelfed-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/pixelfed-scopes.yml
created: '2024-01-01'
description: Pixelfed is a decentralized, federated photo-sharing platform and open-source alternative to Instagram. Built on the ActivityPub protocol, it connects with the broader Fediverse — including Mastodon, PeerTube, and other federated networks — while giving users full ownership of their content. Pixelfed exposes a REST API that is broadly compatible with the Mastodon v1/v2 API, covering media uploads, status management, timelines, notifications, follower graphs, direct messages, stories, collections, and administrative functions. Developers can register OAuth2 applications against any public Pixelfed instance and build clients using the same patterns used for Mastodon- compatible apps.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://pixelfed.org/img/logo.svg
jsonld:
- class_count: 0
  name: Pixelfed Context
  property_count: 0
  slug: pixelfed
layout: provider
modified: '2026-06-13'
name: Pixelfed
nav: Providers
network: true
overview: 'Pixelfed publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Blocks and Mutes API, Bookmarks API, and 14 more. Tagged areas include Fediverse, ActivityPub, Photo Sharing, Social Media, and Open Source.


  The Pixelfed catalog on APIs.io includes 1 JSON-LD context.


  Pixelfed''s developer surface includes authentication and 3 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 39
rate_limits:
- limit_count: 5
  name: Rate Limits
  slug: rate-limits
scopes:
- name: Pixelfed Scopes
  scope_count: 4
  slug: pixelfed-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 36.7
  delta: -3.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.6
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 40.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pixelfed/refs/heads/main/screenshots/pixelfed-2026-06-20T191736.png
security:
- kind: authentication
  name: Pixelfed Authentication
  slug: pixelfed-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Pixelfed Domain Security
  slug: pixelfed-domain-security
  summary_line: TLSv1.3
slug: pixelfed
tags:
- Fediverse
- ActivityPub
- Photo Sharing
- Social Media
- Open Source
- Decentralized
- Mastodon Compatible
- Federation
---

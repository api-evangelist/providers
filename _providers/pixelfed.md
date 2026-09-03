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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Pixelfed Agentic Access
  operation_count: 68
  slug: pixelfed-agentic-access
  summary_line: 68 operations · 28 acting
api_count: 1
apis:
- baseURL: https://{instance}/api
  baseurl_source: declared
  description: Account management, follow/block/mute operations
  name: Pixelfed Accounts API
  slug: pixelfed-accounts-api
- baseURL: https://{instance}/api
  baseurl_source: declared
  description: Blocked accounts and muted accounts
  name: Pixelfed Blocks and Mutes API
  slug: pixelfed-blocks-and-mutes-api
- baseURL: https://{instance}/api
  baseurl_source: declared
  description: Bookmarked statuses
  name: Pixelfed Bookmarks API
  slug: pixelfed-bookmarks-api
- baseURL: https://{instance}/api
  baseurl_source: declared
  description: Pixelfed-specific photo collections (v1.1)
  name: Pixelfed Collections API
  slug: pixelfed-collections-api
- baseURL: https://{instance}/api
  baseurl_source: declared
  description: Pixelfed-specific direct messaging (v1.1)
  name: Pixelfed Direct Messages API
  slug: pixelfed-direct-messages-api
- baseURL: https://{instance}/api
  baseurl_source: declared
  description: Trending content, suggestions, and directory
  name: Pixelfed Discovery API
  slug: pixelfed-discovery-api
- baseURL: https://{instance}/api
  baseurl_source: declared
  description: Favourited statuses
  name: Pixelfed Favourites API
  slug: pixelfed-favourites-api
- baseURL: https://{instance}/api
  baseurl_source: declared
  description: Pending follow requests
  name: Pixelfed Follow Requests API
  slug: pixelfed-follow-requests-api
- baseURL: https://{instance}/api
  baseurl_source: declared
  description: Instance and federation metadata
  name: Pixelfed Instance API
  slug: pixelfed-instance-api
- baseURL: https://{instance}/api
  baseurl_source: declared
  description: List management and membership
  name: Pixelfed Lists API
  slug: pixelfed-lists-api
- baseURL: https://{instance}/api
  baseurl_source: declared
  description: Media upload and management
  name: Pixelfed Media API
  slug: pixelfed-media-api
- baseURL: https://{instance}/api
  baseurl_source: declared
  description: Notification retrieval and management
  name: Pixelfed Notifications API
  slug: pixelfed-notifications-api
- baseURL: https://{instance}/api
  baseurl_source: declared
  description: Web push subscription management (v1.1)
  name: Pixelfed Push Notifications API
  slug: pixelfed-push-notifications-api
- baseURL: https://{instance}/api
  baseurl_source: declared
  description: Full-text and entity search
  name: Pixelfed Search API
  slug: pixelfed-search-api
- baseURL: https://{instance}/api
  baseurl_source: declared
  description: Creating, reading, and interacting with statuses (posts)
  name: Pixelfed Statuses API
  slug: pixelfed-statuses-api
- baseURL: https://{instance}/api
  baseurl_source: declared
  description: Pixelfed-specific ephemeral stories (v1.1)
  name: Pixelfed Stories API
  slug: pixelfed-stories-api
- baseURL: https://{instance}/api
  baseurl_source: declared
  description: Home, public, tag, and list timelines
  name: Pixelfed Timelines API
  slug: pixelfed-timelines-api
artifact_total: 43
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pixelfed REST Accounts API
  slug: open-pixelfed-accounts-api
- collection_type: open
  name: Pixelfed REST Accounts Blocks and Mutes API
  slug: open-pixelfed-blocks-and-mutes-api
- collection_type: open
  name: Pixelfed REST Accounts Bookmarks API
  slug: open-pixelfed-bookmarks-api
- collection_type: open
  name: Pixelfed REST Accounts Collections API
  slug: open-pixelfed-collections-api
- collection_type: open
  name: Pixelfed REST Accounts Direct Messages API
  slug: open-pixelfed-direct-messages-api
- collection_type: open
  name: Pixelfed REST Accounts Discovery API
  slug: open-pixelfed-discovery-api
- collection_type: open
  name: Pixelfed REST Accounts Favourites API
  slug: open-pixelfed-favourites-api
- collection_type: open
  name: Pixelfed REST Accounts Follow Requests API
  slug: open-pixelfed-follow-requests-api
- collection_type: open
  name: Pixelfed REST Accounts Instance API
  slug: open-pixelfed-instance-api
- collection_type: open
  name: Pixelfed REST Accounts Lists API
  slug: open-pixelfed-lists-api
- collection_type: open
  name: Pixelfed REST Accounts Media API
  slug: open-pixelfed-media-api
- collection_type: open
  name: Pixelfed REST Accounts Notifications API
  slug: open-pixelfed-notifications-api
- collection_type: open
  name: Pixelfed REST Accounts Push Notifications API
  slug: open-pixelfed-push-notifications-api
- collection_type: open
  name: Pixelfed REST Accounts Search API
  slug: open-pixelfed-search-api
- collection_type: open
  name: Pixelfed REST Accounts Statuses API
  slug: open-pixelfed-statuses-api
- collection_type: open
  name: Pixelfed REST Accounts Stories API
  slug: open-pixelfed-stories-api
- collection_type: open
  name: Pixelfed REST Accounts Timelines API
  slug: open-pixelfed-timelines-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/pixelfed/pixelfed/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/pixelfed/pixelfed/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/pixelfed/pixelfed/blob/dev/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/pixelfed/pixelfed/blob/dev/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/pixelfed/pixelfed/blob/dev/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/pixelfed/pixelfed/blob/dev/LICENSE
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
overview: 'Pixelfed publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Blocks and Mutes API, Bookmarks API, and 14 more. Tagged areas include Fediverse, ActivityPub, Photo Sharing, Social-Media, and Open-Source.


  The Pixelfed catalog on APIs.io includes 1 JSON-LD context.


  Pixelfed''s developer surface includes authentication and 9 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 9
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
  band: developing
  composite: 45.7
  coverage:
    artifact_dirs: 12
    catalog_gap: 46.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 59.0
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 63.2
  open_source:
    applies: true
    score: 100.0
  previous_composite: 45.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
- Social-Media
- Open-Source
- Decentralized
- Mastodon Compatible
- Federation
---

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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 32
  human_in_the_loop: 1
  name: Lemmy Agentic Access
  operation_count: 52
  slug: lemmy-agentic-access
  summary_line: 52 operations · 32 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://lemmy.world/api/v4
  baseurl_source: declared
  description: User account management and settings
  name: Lemmy Account API
  slug: lemmy-account-api
- baseURL: https://lemmy.world/api/v4
  baseurl_source: declared
  description: Administrative actions
  name: Lemmy Admin API
  slug: lemmy-admin-api
- baseURL: https://lemmy.world/api/v4
  baseurl_source: declared
  description: Account registration, login, and password management
  name: Lemmy Authentication API
  slug: lemmy-authentication-api
- baseURL: https://lemmy.world/api/v4
  baseurl_source: declared
  description: Creating and managing comments
  name: Lemmy Comment API
  slug: lemmy-comment-api
- baseURL: https://lemmy.world/api/v4
  baseurl_source: declared
  description: Community management and discovery
  name: Lemmy Community API
  slug: lemmy-community-api
- baseURL: https://lemmy.world/api/v4
  baseurl_source: declared
  description: ActivityPub federation and cross-instance operations
  name: Lemmy Federation API
  slug: lemmy-federation-api
- baseURL: https://lemmy.world/api/v4
  baseurl_source: declared
  description: Image upload and retrieval
  name: Lemmy Images API
  slug: lemmy-images-api
- baseURL: https://lemmy.world/api/v4
  baseurl_source: declared
  description: User notifications and alerts
  name: Lemmy Notifications API
  slug: lemmy-notifications-api
- baseURL: https://lemmy.world/api/v4
  baseurl_source: declared
  description: User profiles and discovery
  name: Lemmy Person API
  slug: lemmy-person-api
- baseURL: https://lemmy.world/api/v4
  baseurl_source: declared
  description: Creating and managing posts
  name: Lemmy Post API
  slug: lemmy-post-api
- baseURL: https://lemmy.world/api/v4
  baseurl_source: declared
  description: Direct messaging between users
  name: Lemmy Private Messages API
  slug: lemmy-private-messages-api
- baseURL: https://lemmy.world/api/v4
  baseurl_source: declared
  description: Content reporting and moderation
  name: Lemmy Reports API
  slug: lemmy-reports-api
- baseURL: https://lemmy.world/api/v4
  baseurl_source: declared
  description: Search across posts, comments, communities, and users
  name: Lemmy Search API
  slug: lemmy-search-api
- baseURL: https://lemmy.world/api/v4
  baseurl_source: declared
  description: Site-level information and configuration
  name: Lemmy Site API
  slug: lemmy-site-api
artifact_total: 43
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lemmy REST Account API
  slug: open-lemmy-account-api
- collection_type: open
  name: Lemmy REST Account Admin API
  slug: open-lemmy-admin-api
- collection_type: open
  name: Lemmy REST Account Authentication API
  slug: open-lemmy-authentication-api
- collection_type: open
  name: Lemmy REST Account Comment API
  slug: open-lemmy-comment-api
- collection_type: open
  name: Lemmy REST Account Community API
  slug: open-lemmy-community-api
- collection_type: open
  name: Lemmy REST Account Federation API
  slug: open-lemmy-federation-api
- collection_type: open
  name: Lemmy REST Account Images API
  slug: open-lemmy-images-api
- collection_type: open
  name: Lemmy REST Account Notifications API
  slug: open-lemmy-notifications-api
- collection_type: open
  name: Lemmy REST Account Person API
  slug: open-lemmy-person-api
- collection_type: open
  name: Lemmy REST Account Post API
  slug: open-lemmy-post-api
- collection_type: open
  name: Lemmy REST Account Private Messages API
  slug: open-lemmy-private-messages-api
- collection_type: open
  name: Lemmy REST Account Reports API
  slug: open-lemmy-reports-api
- collection_type: open
  name: Lemmy REST Account Search API
  slug: open-lemmy-search-api
- collection_type: open
  name: Lemmy REST Account Site API
  slug: open-lemmy-site-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/LemmyNet/lemmy/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/LemmyNet/lemmy/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/LemmyNet/lemmy/blob/main/.github/SECURITY.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lemmy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lemmy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lemmy-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LemmyNet
- group: company
  title: ''
  type: Website
  url: https://join-lemmy.org
- group: docs
  title: ''
  type: Documentation
  url: https://join-lemmy.org/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://join-lemmy.org/docs/client_development/
- group: commercial
  title: ''
  type: License
  url: https://github.com/LemmyNet/lemmy/blob/main/LICENSE
- group: company
  title: ''
  type: Blog
  url: https://join-lemmy.org/news/
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lemmy-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/lemmy-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lemmy-finops.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/LemmyNet/lemmy
- group: other
  title: ''
  type: ActivityPub
  url: https://www.w3.org/TR/activitypub/
created: '2026-06-13'
description: Lemmy is a free, open-source, self-hostable federated link aggregator and discussion platform built as a Reddit alternative. It exposes a versioned REST API at /api/v4/ for creating posts, commenting, managing communities, voting, searching, and administering instances. Lemmy federates across the Fediverse using the ActivityPub protocol, allowing users on different Lemmy instances and compatible platforms (Mastodon, PeerTube, Friendica) to interact without a central server. Each instance operator configures their own rate limits; default limits include 50 comments per 10 minutes, 100 searches per 10 minutes, and 5 new registrations per day. Authentication uses JWT bearer tokens obtained via the login endpoint. The software is licensed under AGPL-3.0 and written in Rust with an Actix web framework backend.
examples:
- key_count: 4
  name: Create Post
  slug: create-post
- key_count: 5
  name: Login
  slug: login
- key_count: 4
  name: Search
  slug: search
finops:
- name: Lemmy Finops
  service_category: Social Network Data
  slug: lemmy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lemmy.png
json_schemas:
- name: Comment
  property_count: 13
  slug: comment
- name: Community
  property_count: 17
  slug: community
- name: Post
  property_count: 21
  slug: post
jsonld:
- class_count: 34
  name: Lemmy Context
  property_count: 34
  slug: lemmy-context
layout: provider
modified: '2026-06-13'
name: Lemmy
nav: Providers
network: true
overview: 'Lemmy publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Account API, Admin API, Authentication API, and 11 more. Tagged areas include Communities, Federated, Fediverse, Link Aggregator, and Open-Source.


  The Lemmy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Lemmy''s developer surface includes authentication, documentation, getting-started guide, engineering blog, and 13 more developer resources.'
plans:
- name: Lemmy Plans Pricing
  plan_count: 3
  slug: lemmy-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 6
  name: Lemmy Rate Limits
  slug: lemmy-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Lemmy API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: lemmy-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.6
  coverage:
    artifact_dirs: 15
    catalog_gap: 21.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 2.2
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 25.0
    contract_quality: 74.3
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 60.5
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lemmy/refs/heads/main/screenshots/lemmy-2026-06-20T184415.png
security:
- kind: authentication
  name: Lemmy Authentication
  slug: lemmy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lemmy Domain Security
  slug: lemmy-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: lemmy
tags:
- Communities
- Federated
- Fediverse
- Link Aggregator
- Open-Source
- Social Networks
website: https://join-lemmy.org
---

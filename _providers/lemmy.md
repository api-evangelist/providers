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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 32
  human_in_the_loop: 1
  name: Lemmy Agentic Access
  operation_count: 52
  slug: lemmy-agentic-access
  summary_line: 52 operations · 32 acting · 1 human-in-the-loop
api_count: 14
apis:
- description: User account management and settings
  name: Lemmy Account API
  slug: lemmy-account-api
- description: Administrative actions
  name: Lemmy Admin API
  slug: lemmy-admin-api
- description: Account registration, login, and password management
  name: Lemmy Authentication API
  slug: lemmy-authentication-api
- description: Creating and managing comments
  name: Lemmy Comment API
  slug: lemmy-comment-api
- description: Community management and discovery
  name: Lemmy Community API
  slug: lemmy-community-api
- description: ActivityPub federation and cross-instance operations
  name: Lemmy Federation API
  slug: lemmy-federation-api
- description: Image upload and retrieval
  name: Lemmy Images API
  slug: lemmy-images-api
- description: User notifications and alerts
  name: Lemmy Notifications API
  slug: lemmy-notifications-api
- description: User profiles and discovery
  name: Lemmy Person API
  slug: lemmy-person-api
- description: Creating and managing posts
  name: Lemmy Post API
  slug: lemmy-post-api
- description: Direct messaging between users
  name: Lemmy Private Messages API
  slug: lemmy-private-messages-api
- description: Content reporting and moderation
  name: Lemmy Reports API
  slug: lemmy-reports-api
- description: Search across posts, comments, communities, and users
  name: Lemmy Search API
  slug: lemmy-search-api
- description: Site-level information and configuration
  name: Lemmy Site API
  slug: lemmy-site-api
artifact_total: 28
common:
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


  Lemmy''s developer surface includes authentication, documentation, getting-started guide, engineering blog, and 10 more developer resources.'
plans:
- name: Lemmy Plans Pricing
  plan_count: 3
  slug: lemmy-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 6
  name: Lemmy Rate Limits
  slug: lemmy-rate-limits
rules:
- name: Lemmy API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: lemmy-jsonschema-spectral-rules
score:
  band: developing
  composite: 56.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 75.2
    developer_ergonomics: 32.6
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 36.8
  previous_composite: 56.8
  schema_version: 0.5
  scored_at: '2026-07-27'
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

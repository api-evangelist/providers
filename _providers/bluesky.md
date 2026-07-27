---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    asyncapi_events: true
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
  score: 53.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 75
  human_in_the_loop: 5
  name: Bluesky Agentic Access
  operation_count: 168
  slug: bluesky-agentic-access
  summary_line: 168 operations · 75 acting · 5 human-in-the-loop
api_count: 24
apis:
- description: Jetstream is a simplified JSON event stream for the AT Protocol that converts CBOR-encoded MST blocks from the firehose into JSON objects over WebSocket connections, making it easier to consume real-t
  name: Bluesky Jetstream
  slug: bluesky-jetstream
- description: Operations for managing user profiles, preferences, and actor information.
  name: Bluesky Actor Profiles API
  slug: bluesky-actor-profiles-api
- description: Administrative operations for managing accounts and invites.
  name: Bluesky Administration API
  slug: bluesky-administration-api
- description: Operations for managing chat actor settings and declarations.
  name: Bluesky Chat Actors API
  slug: bluesky-chat-actors-api
- description: Operations for moderating chat content.
  name: Bluesky Chat Moderation API
  slug: bluesky-chat-moderation-api
- description: Operations for managing content labelers and label subscriptions.
  name: Bluesky Content Labels API
  slug: bluesky-content-labels-api
- description: Operations for managing direct message conversations.
  name: Bluesky Conversations API
  slug: bluesky-conversations-api
- description: Operations for managing feeds, posts, likes, and reposts.
  name: Bluesky Feeds API
  slug: bluesky-feeds-api
- description: Operations for identity management and DID resolution.
  name: Bluesky Identity API
  slug: bluesky-identity-api
- description: Operations for content labeling and moderation.
  name: Bluesky Labels API
  slug: bluesky-labels-api
- description: Operations for content moderation reporting.
  name: Bluesky Moderation API
  slug: bluesky-moderation-api
- description: Operations for managing user notifications.
  name: Bluesky Notifications API
  slug: bluesky-notifications-api
- description: Ozone moderation tool communication operations.
  name: Bluesky Ozone Communication API
  slug: bluesky-ozone-communication-api
- description: Ozone moderation tool operations.
  name: Bluesky Ozone Moderation API
  slug: bluesky-ozone-moderation-api
- description: Ozone server configuration operations.
  name: Bluesky Ozone Server API
  slug: bluesky-ozone-server-api
- description: Ozone set management operations.
  name: Bluesky Ozone Sets API
  slug: bluesky-ozone-sets-api
- description: Ozone settings management operations.
  name: Bluesky Ozone Settings API
  slug: bluesky-ozone-settings-api
- description: Ozone signature and threat analysis operations.
  name: Bluesky Ozone Signatures API
  slug: bluesky-ozone-signatures-api
- description: Ozone team member management operations.
  name: Bluesky Ozone Team API
  slug: bluesky-ozone-team-api
- description: Operations for managing AT Protocol repositories.
  name: Bluesky Repository API
  slug: bluesky-repository-api
- description: Operations for server management and authentication.
  name: Bluesky Server API
  slug: bluesky-server-api
- description: Operations for managing follows, followers, blocks, mutes, and lists.
  name: Bluesky Social Graph API
  slug: bluesky-social-graph-api
- description: Operations for repository synchronization.
  name: Bluesky Sync API
  slug: bluesky-sync-api
- description: Operations for video upload and processing.
  name: Bluesky Video API
  slug: bluesky-video-api
artifact_total: 35
asyncapis:
- description: 'AsyncAPI definition for the public event streams of the Bluesky network and the underlying AT Protocol. Three streams are documented: * **`com.atproto.sync.subscribeRepos`** - the primary repository e'
  name: Bluesky / AT Protocol Event Streams
  slug: bluesky-asyncapi
collections:
- collection_type: open
  name: Bluesky Social API
  slug: open-bluesky
- collection_type: bruno
  name: Bluesky Bruno Collection
  slug: bruno
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bluesky-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bluesky-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bluesky-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bluesky-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bluesky-pbc
- group: other
  title: ''
  type: Bots
  url: https://docs.bsky.app/docs/starter-templates/bots
- group: operate
  title: ''
  type: Support
  url: https://docs.bsky.app/docs/category/support
- group: company
  title: ''
  type: Blog
  url: https://docs.bsky.app/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bsky.app/docs/get-started
- group: other
  title: ''
  type: Templates
  url: https://docs.bsky.app/docs/category/starter-templates
- group: learn
  title: ''
  type: Tutorials
  url: https://docs.bsky.app/docs/category/tutorials
- group: company
  title: ''
  type: Newsletter
  url: https://docs.bsky.app/docs/support/mailing-list
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/api-evangelist/bluesky/overview
- group: docs
  title: ''
  type: Guidelines
  url: https://docs.bsky.app/docs/support/developer-guidelines
- group: other
  title: ''
  type: CustomFeeds
  url: https://docs.bsky.app/docs/starter-templates/custom-feeds
- group: other
  title: ''
  type: Protocol
  url: https://docs.bsky.app/docs/advanced-guides/atproto
- group: docs
  title: ''
  type: AdvancedGuides
  url: https://docs.bsky.app/docs/category/advanced-guides
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bsky.social/about/support/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bsky.social/about/support/privacy-policy
- group: docs
  title: ''
  type: CommunityGuidelines
  url: https://bsky.social/about/support/community-guidelines
- group: build
  title: ''
  type: SDKs
  url: https://atproto.com/sdks
- group: other
  title: ''
  type: ProtocolOverview
  url: https://atproto.com/guides/overview
- group: docs
  title: ''
  type: Specification
  url: https://atproto.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/bluesky-social
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/bluesky-social/atproto
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/bluesky-social/feed-generator
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/bluesky-social/ozone
- group: operate
  title: ''
  type: Forums
  url: https://github.com/bluesky-social/atproto/discussions
- group: other
  title: ''
  type: Summary
  url: ''
created: '2024-11-16'
description: API for the Bluesky decentralized social network built on the AT Protocol.
finops:
- name: Bluesky Finops
  service_category: API
  slug: bluesky-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bluesky.png
layout: provider
modified: '2026-05-29'
name: Bluesky
nav: Providers
network: true
overview: 'Bluesky publishes 24 APIs on the [APIs.io](https://apis.io/) network, including Jetstream, Actor Profiles API, Administration API, and 21 more. Tagged areas include At-Protocol, Decentralized, Federated, Open-Source, and Social Networks.


  The Bluesky catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Bluesky''s developer surface includes authentication, support, engineering blog, getting-started guide, and 24 more developer resources.'
plans:
- name: Bluesky Plans Pricing
  plan_count: 3
  slug: bluesky-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Bluesky Rate Limits
  slug: bluesky-rate-limits
rules:
- name: Bluesky API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: bluesky-asyncapi-spectral-rules
score:
  band: developing
  composite: 55.1
  delta: 1.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 69.5
    developer_ergonomics: 39.1
    discoverability: 67.5
    governance: 52.6
    operational_transparency: 36.8
  previous_composite: 53.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bluesky/refs/heads/main/screenshots/bluesky-2026-06-20T173536.png
security:
- kind: authentication
  name: Bluesky Authentication
  slug: bluesky-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bluesky Domain Security
  slug: bluesky-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bluesky Vulnerability Disclosure
  slug: bluesky-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bluesky
tags:
- At-Protocol
- Decentralized
- Federated
- Open-Source
- Social Networks
- Social-Media
---

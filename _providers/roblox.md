---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    agentic_access: false
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
  score: 28.4
  scored_at: '2026-07-28'
api_count: 8
apis:
- description: The Roblox Open Cloud API is the official external REST surface for Roblox creators, studios, and partners. It exposes universes, places, place publishing, ordered and standard data stores, memory sto
  name: Roblox Open Cloud API
  slug: roblox-open-cloud-api
- description: The Data Stores Open Cloud API reads and writes persistent key-value data for an experience from outside the engine, including standard data stores and ordered data stores. Used by build pipelines, Li
  name: Roblox Open Cloud Data Stores
  slug: roblox-open-cloud-datastores
- description: The Messaging Service Open Cloud API publishes messages to a topic that running game servers can subscribe to via the in-engine MessagingService class, enabling cross-server and external-to-engine bro
  name: Roblox Open Cloud Messaging Service
  slug: roblox-open-cloud-messaging-service
- description: The Place Publishing Open Cloud API uploads .rbxl or .rbxlx files to a place in a universe and either saves or publishes the new version, enabling CI/CD pipelines for Roblox experiences.
  name: Roblox Open Cloud Place Publishing
  slug: roblox-open-cloud-place-publishing
- description: The Assets Open Cloud API creates, updates, and reads assets (audio, decals, images, models, mesh parts) on behalf of a user or group, used by asset pipelines and content factories.
  name: Roblox Open Cloud Assets
  slug: roblox-open-cloud-assets
- description: The Roblox Engine API is the in-engine scripting surface used inside experiences and Studio plugins. It is written in Luau, Roblox's typed dialect of Lua 5.1, and exposes thousands of classes includin
  name: Roblox Engine API (Luau)
  slug: roblox-engine-api-luau
- description: The Roblox Studio Plugin API is a superset of the Engine API available to plugins running inside Roblox Studio. It exposes plugin-only services for toolbars, dock widgets, selection, ChangeHistoryServ
  name: Roblox Studio Plugin API
  slug: roblox-studio-plugin-api
- description: Roblox OAuth 2.0 lets third-party applications authenticate Roblox users and obtain scoped access tokens to call permitted Open Cloud resources on the user's behalf. Apps are registered in the Creator
  name: Roblox OAuth 2.0
  slug: roblox-oauth2
artifact_total: 14
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/roblox-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/roblox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.roblox.com
- group: start
  title: ''
  type: Portal
  url: https://create.roblox.com
- group: docs
  title: ''
  type: Documentation
  url: https://create.roblox.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://create.roblox.com/docs/cloud
- group: docs
  title: ''
  type: APIReference
  url: https://create.roblox.com/docs/cloud/reference
- group: auth
  title: ''
  type: Authentication
  url: https://create.roblox.com/docs/cloud/auth
- group: other
  title: ''
  type: Marketplace
  url: https://create.roblox.com/store
- group: other
  title: ''
  type: Credentials
  url: https://create.roblox.com/dashboard/credentials
- group: operate
  title: ''
  type: Forums
  url: https://devforum.roblox.com
- group: other
  title: ''
  type: Language
  url: https://luau.org
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/luau-lang/luau
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Roblox
- group: operate
  title: ''
  type: Status
  url: https://status.roblox.com
- group: operate
  title: ''
  type: Support
  url: https://en.help.roblox.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.roblox.com/info/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.roblox.com/info/privacy
- group: docs
  title: ''
  type: CommunityGuidelines
  url: https://en.help.roblox.com/hc/en-us/articles/115004647846-Roblox-Community-Standards
- group: company
  title: ''
  type: Blog
  url: https://blog.roblox.com
- group: other
  title: ''
  type: ParentCompany
  url: https://corp.roblox.com
- group: other
  title: ''
  type: X
  url: https://x.com/Roblox
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/Roblox
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/roblox
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Roblox
created: '2024-01-01'
description: 'Roblox is a user-generated content platform where creators build, publish, and monetize immersive 3D experiences using Roblox Studio and the Luau scripting language. Roblox exposes three distinct developer surfaces: the in-engine Luau scripting API (Roblox Engine API) running inside experiences and Studio plugins, the Roblox Studio plugin API for editor tooling, and the Open Cloud API (apis.roblox.com) for external programmatic access from servers, build pipelines, and back-office tools. The Open Cloud surface covers DataStores, Memory Stores, Messaging Service, Place Publishing, Universes, Assets, Inventory, Users, Groups, Notifications, Subscriptions, and Luau Execution, authenticated either with API keys scoped per-resource or with OAuth 2.0 for third-party apps. Roblox also publishes deep documentation for the Engine API at create.roblox.com/docs and the legacy ROBLOX Web APIs that power the website (subdomains such as users.roblox.com, groups.roblox.com, inventory.roblox.com),
  which remain undocumented for third parties.'
finops:
- name: Roblox Finops
  service_category: API
  slug: roblox-finops
graphqls:
- description: Conceptual GraphQL schema for the Roblox platform, covering the Open Cloud API, Engine API, and the broader Roblox web surfaces (users, groups, games, economy, avatar, inventory, social, messaging, an
  name: Roblox GraphQL Schema
  slug: roblox-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/roblox.png
layout: provider
modified: '2026-05-23'
name: Roblox
nav: Providers
network: true
overview: 'Roblox publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Assets, DataStores, Game Development, Games, and Luau.


  Roblox''s developer surface includes developer portal, documentation, API reference, authentication, status page, support, engineering blog, and 18 more developer resources.'
plans:
- name: Roblox Plans Pricing
  plan_count: 1
  slug: roblox-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 2
  name: Roblox Rate Limits
  slug: roblox-rate-limits
score:
  band: thin
  composite: 39.9
  delta: 8.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 43.2
    developer_ergonomics: 41.3
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 31.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 36.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/roblox/refs/heads/main/screenshots/roblox-2026-06-20T193141.png
security:
- kind: domain-security
  name: Roblox Domain Security
  slug: roblox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Roblox Vulnerability Disclosure
  slug: roblox-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: roblox
tags:
- Assets
- DataStores
- Game Development
- Games
- Luau
- Messaging
- Open Cloud
- Roblox
- Scripting
- Studio
- UGC
- Universes
website: https://www.roblox.com
---

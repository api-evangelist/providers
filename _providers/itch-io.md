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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Itch Io Agentic Access
  operation_count: 36
  slug: itch-io-agentic-access
  summary_line: 36 operations · 10 acting
api_count: 11
apis:
- description: Authentication operations
  name: Itch.io Auth API
  slug: itch-io-auth-api
- description: Operations related to wharf builds
  name: Itch.io Builds API
  slug: itch-io-builds-api
- description: Operations related to game bundles
  name: Itch.io Bundles API
  slug: itch-io-bundles-api
- description: Operations related to user game collections
  name: Itch.io Collections API
  slug: itch-io-collections-api
- description: The Downloads API from Itch.io — 1 operation(s) for downloads.
  name: Itch.io Downloads API
  slug: itch-io-downloads-api
- description: Operations related to itch.io game pages
  name: Itch.io Games API
  slug: itch-io-games-api
- description: Operations related to the authenticated user's profile
  name: Itch.io Profile API
  slug: itch-io-profile-api
- description: Search operations
  name: Itch.io Search API
  slug: itch-io-search-api
- description: Operations related to game uploads and downloads
  name: Itch.io Uploads API
  slug: itch-io-uploads-api
- description: User lookup operations
  name: Itch.io Users API
  slug: itch-io-users-api
- description: Wharf build infrastructure operations (butler/CI integration)
  name: Itch.io Wharf API
  slug: itch-io-wharf-api
artifact_total: 26
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/itch-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/itch-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/itch-io-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://itch.io
- group: docs
  title: ''
  type: Documentation
  url: https://itch.io/docs/api/overview
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/itchio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/itchio
- group: company
  title: ''
  type: Blog
  url: https://itch.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://itch.io/docs/creators/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://www.saashub.com/itch-io-status
- group: other
  title: ''
  type: X
  url: https://twitter.com/itchio
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/itch-io/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/itch-io/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/itch-io/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: Itch.io is an indie game marketplace and community platform where developers can publish, sell, and distribute games, assets, and creative tools. Its REST API provides authenticated access to game metadata, developer profile information, bundle and download key management, purchase verification, community ratings, and game distribution data. The API supports OAuth 2.0 implicit flow and API key authentication to enable integrations with developer tools, game launchers, and third-party services.
examples:
- key_count: 1
  name: Get Profile
  slug: get-profile
- key_count: 1
  name: List Game Uploads
  slug: list-game-uploads
- key_count: 1
  name: List Profile Games
  slug: list-profile-games
- key_count: 1
  name: Wharf Channel
  slug: wharf-channel
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/itch-io.png
json_schemas:
- name: Build
  property_count: 12
  slug: build
- name: Game
  property_count: 23
  slug: game
- name: Upload
  property_count: 15
  slug: upload
- name: User
  property_count: 8
  slug: user
layout: provider
modified: '2026-06-13'
name: Itch.io
nav: Providers
network: true
overview: 'Itch.io publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Builds API, Bundles API, and 8 more. Tagged areas include Games, Indie Games, Game Distribution, Game Marketplace, and Developers.


  The Itch.io catalog on APIs.io includes 1 Spectral governance ruleset.


  Itch.io''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 69
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: Itch.io API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: itch-io-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.8
  delta: -4.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Itch Io Authentication
  slug: itch-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Itch Io Domain Security
  slug: itch-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: itch-io
tags:
- Games
- Indie Games
- Game Distribution
- Game Marketplace
- Developers
website: https://itch.io
---

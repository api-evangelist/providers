---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.5
  scored_at: '2026-08-24'
api_count: 10
apis:
- description: 'Epic Account Services (EAS) provides authentication and identity for players using Epic Games accounts. Supports OAuth 2.0 authorization code, device, and exchange code flows, account info retrieval, '
  name: Epic Account Services API
  slug: epic-account-services
- description: The EOS Achievements API enables developers to define, unlock, and query player achievements across platforms. Supports definitions, player progress, and unlocking via the EOS SDK or Web API.
  name: Epic Online Services Achievements API
  slug: eos-achievements
- description: The EOS Leaderboards API provides global and per-friend leaderboards backed by player stats. Developers configure leaderboards in the developer portal and query rankings via the EOS SDK or Web API.
  name: Epic Online Services Leaderboards API
  slug: eos-leaderboards
- description: The EOS Stats API tracks player statistics over time, providing the data source that powers leaderboards and achievements. Supports ingest, increment, and query operations on stat values.
  name: Epic Online Services Stats API
  slug: eos-stats
- description: The EOS Friends API exposes a player's Epic Games friends list, allowing games to surface social presence, invitations, and party formation across platforms.
  name: Epic Online Services Friends API
  slug: eos-friends
- description: The EOS Ecom (Ecommerce) Interface API exposes the player's Epic Games Store entitlements, ownership, catalog offers, and checkout flows. Used by titles published on the Epic Games Store to verify pur
  name: Epic Online Services Ecom API
  slug: eos-ecom
- description: The EOS Lobby and Sessions APIs provide matchmaking primitives for multiplayer games, including lobby creation, joining, attribute filtering, and dedicated session management.
  name: Epic Online Services Lobby and Sessions API
  slug: eos-lobby-sessions
- description: The EOS Player Data Storage and Title Storage APIs persist per-player save data and shared title-level configuration in the cloud, with cross-platform availability and versioning.
  name: Epic Online Services Player Data Storage API
  slug: eos-player-data-storage
- description: Easy Anti-Cheat (EAC) integrated into Epic Online Services provides kernel and user-mode anti-cheat protections, server-side validation, and reporting tooling for cross-platform multiplayer titles.
  name: Epic Online Services Anti-Cheat API
  slug: eos-anti-cheat
- description: The EOS Voice Interface delivers in-game voice chat using Vivox backend infrastructure, with positional audio, room management, and moderation controls across platforms.
  name: Epic Online Services Voice API
  slug: eos-voice
artifact_total: 15
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/epic-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/epic-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/epicgames
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/epic-games
- group: company
  title: ''
  type: Website
  url: https://www.epicgames.com/
- group: start
  title: ''
  type: Portal
  url: https://dev.epicgames.com/portal/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.epicgames.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.epicgames.com/docs/epic-online-services/eos-get-started
- group: auth
  title: ''
  type: Authentication
  url: https://dev.epicgames.com/docs/epic-account-services/auth/auth-interface
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dev.epicgames.com/services-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.epicgames.com/site/en-US/privacypolicy
- group: operate
  title: ''
  type: Support
  url: https://dev.epicgames.com/community/
- group: other
  title: ''
  type: Store
  url: https://store.epicgames.com/
created: '2024-07-02'
description: Epic Games operates the Epic Games Store digital storefront and the Epic Online Services (EOS) platform, providing developers with cross-platform game services. Epic Online Services is a free SDK based on Fortnite's backend infrastructure, supporting matchmaking, friends, leaderboards, achievements, voice chat, anti-cheat, and player data storage across Windows, macOS, PlayStation, Xbox, Nintendo Switch, iOS, and Android. The Epic Account Services and EOS Web APIs deliver authentication, account management, ecommerce, and analytics for games published on the Epic Games Store and other platforms.
finops:
- name: Epic Finops
  service_category: API
  slug: epic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/epic.png
layout: provider
modified: '2026-04-28'
name: Epic Games
nav: Providers
network: true
overview: 'Epic Games publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Game Services, Gaming, Cross-Platform, Achievements, and Leaderboards.


  Epic Games'' developer surface includes developer portal, documentation, getting-started guide, authentication, support, and 8 more developer resources.'
plans:
- name: Epic Plans Pricing
  plan_count: 3
  slug: epic-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Epic Rate Limits
  slug: epic-rate-limits
score:
  band: emerging
  composite: 23.6
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 23.6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/epic/refs/heads/main/screenshots/epic-2026-06-20T180752.png
security:
- kind: domain-security
  name: Epic Domain Security
  slug: epic-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Epic Vulnerability Disclosure
  slug: epic-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: epic
tags:
- Game Services
- Gaming
- Cross-Platform
- Achievements
- Leaderboards
- Matchmaking
- Anti-Cheat
- Authentication
website: https://www.epicgames.com/
---

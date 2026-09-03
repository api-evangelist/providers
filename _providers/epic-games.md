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
    delegated_identity: false
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
  score: 22.7
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 5
  human_in_the_loop: 1
  name: Epic Games Agentic Access
  operation_count: 17
  slug: epic-games-agentic-access
  summary_line: 17 operations · 5 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Epic Online Services is Epic's free cross-platform backend for games. EOS exposes both a native C/C++ SDK (with Unity, Unreal, and platform wrappers) and a set of REST web services covering identity (
  name: Epic Online Services (EOS)
  slug: epic-online-services
- description: Epic Account Services provides OAuth 2.0 / OIDC sign-in with an Epic Account, exposing user identity, display name, country, preferred language, and linked-account information to integrating games and
  name: Epic Account Services
  slug: epic-account-services
- description: The Epic Games Store publishing surface lets developers upload builds, configure store pages, manage offers, run sales, and integrate with EOS achievements and entitlements. Publishing tools include t
  name: Epic Games Store Publishing
  slug: epic-games-store-publishing
- description: Kids Web Services is Epic's compliance and parental-verification platform for games and online services that handle children's data. KWS exposes REST APIs and an SDK for age verification, parental con
  name: Kids Web Services (KWS)
  slug: kids-web-services
- description: Unreal Engine is profiled separately. See the unreal-engine entry for Unreal SDK / Plugin / Pixel Streaming / RHI / Online Subsystem details.
  name: Unreal Engine (Pointer)
  slug: unreal-engine-pointer
- baseURL: https://api.epicgames.dev
  baseurl_source: declared
  description: The Achievements API from Epic Games — 2 operation(s) for achievements.
  name: Epic Games Achievements API
  slug: epic-games-achievements-api
- baseURL: https://api.epicgames.dev
  baseurl_source: declared
  description: The Auth API from Epic Games — 4 operation(s) for auth.
  name: Epic Games Auth API
  slug: epic-games-auth-api
- baseURL: https://api.epicgames.dev
  baseurl_source: declared
  description: The Connect API from Epic Games — 1 operation(s) for connect.
  name: Epic Games Connect API
  slug: epic-games-connect-api
- baseURL: https://api.epicgames.dev
  baseurl_source: declared
  description: The Ecom API from Epic Games — 1 operation(s) for ecom.
  name: Epic Games Ecom API
  slug: epic-games-ecom-api
- baseURL: https://api.epicgames.dev
  baseurl_source: declared
  description: The Leaderboards API from Epic Games — 2 operation(s) for leaderboards.
  name: Epic Games Leaderboards API
  slug: epic-games-leaderboards-api
- baseURL: https://api.epicgames.dev
  baseurl_source: declared
  description: The PlayerDataStorage API from Epic Games — 1 operation(s) for playerdatastorage.
  name: Epic Games PlayerDataStorage API
  slug: epic-games-playerdatastorage-api
- baseURL: https://api.epicgames.dev
  baseurl_source: declared
  description: The Sanctions API from Epic Games — 1 operation(s) for sanctions.
  name: Epic Games Sanctions API
  slug: epic-games-sanctions-api
- baseURL: https://api.epicgames.dev
  baseurl_source: declared
  description: The Stats API from Epic Games — 1 operation(s) for stats.
  name: Epic Games Stats API
  slug: epic-games-stats-api
- baseURL: https://api.epicgames.dev
  baseurl_source: declared
  description: The TitleStorage API from Epic Games — 1 operation(s) for titlestorage.
  name: Epic Games TitleStorage API
  slug: epic-games-titlestorage-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Epic Online Services Web Achievements API
  slug: open-epic-games-achievements-api
- collection_type: open
  name: Epic Online Services Web Achievements Auth API
  slug: open-epic-games-auth-api
- collection_type: open
  name: Epic Online Services Web Achievements Connect API
  slug: open-epic-games-connect-api
- collection_type: open
  name: Epic Online Services Web Achievements Ecom API
  slug: open-epic-games-ecom-api
- collection_type: open
  name: Epic Online Services Web Achievements Leaderboards API
  slug: open-epic-games-leaderboards-api
- collection_type: open
  name: Epic Online Services Web Achievements PlayerDataStorage API
  slug: open-epic-games-playerdatastorage-api
- collection_type: open
  name: Epic Online Services Web Achievements Sanctions API
  slug: open-epic-games-sanctions-api
- collection_type: open
  name: Epic Online Services Web Achievements Stats API
  slug: open-epic-games-stats-api
- collection_type: open
  name: Epic Online Services Web Achievements TitleStorage API
  slug: open-epic-games-titlestorage-api
- collection_type: open
  name: Epic Online Services Web API
  slug: open-epic-games
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/epic-games-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/epic-games-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/epic-games-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/epic-games-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/epic-games-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.epicgames.com
- group: other
  title: ''
  type: Store
  url: https://store.epicgames.com
- group: start
  title: ''
  type: Portal
  url: https://dev.epicgames.com
- group: docs
  title: ''
  type: Documentation
  url: https://dev.epicgames.com/docs
- group: operate
  title: ''
  type: Community
  url: https://dev.epicgames.com/community
- group: docs
  title: ''
  type: APIReference
  url: https://dev.epicgames.com/docs/web-api-ref
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.epicgames.com/docs/epic-online-services/eos-get-started
- group: learn
  title: ''
  type: Tutorials
  url: https://dev.epicgames.com/docs/services/en-US/Tutorials
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EpicGames
- group: operate
  title: ''
  type: Status
  url: https://status.epicgames.com
- group: operate
  title: ''
  type: Support
  url: https://www.epicgames.com/help
- group: company
  title: ''
  type: Blog
  url: https://www.unrealengine.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://store.epicgames.com/en-US/eula
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.epicgames.com/site/en-US/privacypolicy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.epicgames.com/site/en-US/eula
- group: other
  title: ''
  type: X
  url: https://x.com/EpicGames
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/epicgames
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/epic-games
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@epic
created: '2024-01-01'
description: Epic Games is the studio behind Fortnite, the Unreal Engine, the Epic Games Store, MetaHuman, RealityScan, Twinmotion, RAD Game Tools, and the Epic Online Services (EOS) backend. Epic operates a unified developer portal at dev.epicgames.com that hosts the EOS SDK and REST APIs (Auth, Connect, Friends, Presence, Lobby, Sessions, Achievements, Stats, Leaderboards, Player Data Storage, Title Storage, Voice, Sanctions, Anti-Cheat, Reports, P2P, Ecom, User Info), the Unreal Engine documentation, the Epic Games Store publishing tools, and the Kids Web Services (KWS) compliance platform. EOS is cross-platform and runs on Windows, macOS, Linux, PlayStation, Xbox, Switch, iOS, Android, and web. This profile rolls Epic's developer-facing surfaces into a single index; the Unreal Engine surface has its own dedicated profile.
finops:
- name: Epic Games Finops
  service_category: API
  slug: epic-games-finops
graphqls:
- description: Epic Games exposes GraphQL surfaces across several developer-facing products. The primary surface historically lived at `https://graphql.epicgames.com/graphql` and powered the Epic Games Store catalog
  name: Epic Games GraphQL
  slug: epic-games-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/epic-games.png
layout: provider
modified: '2026-05-23'
name: Epic Games
nav: Providers
network: true
overview: 'Epic Games publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Achievements API, Auth API, Connect API, and 6 more. Tagged areas include Achievements, Anti-Cheat, Cross-Platform, EOS, and Epic Online Services.


  Epic Games'' developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, status page, support, and 17 more developer resources.'
plans:
- name: Epic Games Plans Pricing
  plan_count: 1
  slug: epic-games-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Epic Games Rate Limits
  slug: epic-games-rate-limits
scopes:
- name: Epic Games Scopes
  scope_count: 1
  slug: epic-games-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 47.9
  coverage:
    artifact_dirs: 12
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 56.0
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 47.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/epic-games/refs/heads/main/screenshots/epic-games-2026-06-20T180759.png
security:
- kind: authentication
  name: Epic Games Authentication
  slug: epic-games-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Epic Games Domain Security
  slug: epic-games-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Epic Games Vulnerability Disclosure
  slug: epic-games-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: epic-games
tags:
- Achievements
- Anti-Cheat
- Cross-Platform
- EOS
- Epic Online Services
- Game Backend
- Game Development
- Games
- Identity
- Lobby
- Matchmaking
- Multiplayer
- Sessions
- Unreal Engine
- Voice
website: https://www.epicgames.com
---

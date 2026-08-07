---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Steam Agentic Access
  operation_count: 11
  slug: steam-agentic-access
  summary_line: 11 operations
api_count: 25
apis:
- description: ISteamNews exposes per-game news feeds via GetNewsForApp. Path pattern http://api.steampowered.com/ISteamNews/<method>/v<version>/.
  name: ISteamNews
  slug: steam-news-api
- description: ISteamUserStats provides global achievement percentages, schema for game stats and achievements, and per-user achievement / stats retrieval (GetGlobalAchievementPercentagesForApp, GetSchemaForGame, Ge
  name: ISteamUserStats
  slug: steam-user-stats-api
- description: ISteamUser exposes player profile, friend list, and ban-status endpoints (GetPlayerSummaries, GetFriendList, GetPlayerBans, ResolveVanityURL).
  name: ISteamUser
  slug: steam-user-api
- description: ISteamUserAuth issues and validates Steam session tickets (AuthenticateUserTicket, AuthenticateUser) used by partner servers to verify a connecting player's Steam identity.
  name: ISteamUserAuth
  slug: steam-user-auth-api
- description: ISteamApps exposes catalog and server queries (GetAppList, GetServersAtAddress, UpToDateCheck) used to enumerate Steam applications and validate version state.
  name: ISteamApps
  slug: steam-apps-api
- description: ISteamCommunity provides restricted access to Steam Community features (e.g., ReportAbuse) for trusted partners.
  name: ISteamCommunity
  slug: steam-community-api
- description: ISteamEconomy is a secondary economy-system interface (GetAssetClassInfo, GetAssetPrices, FinalizeAssetTransaction) used to look up asset metadata and pricing for in-game items.
  name: ISteamEconomy
  slug: steam-economy-api
- description: IGameInventory is the primary inventory-economy interface used by partner servers to manipulate item ownership (AddItem, ConsumeItem, GetUserInventory, GetItemDefArchive).
  name: IGameInventory
  slug: steam-game-inventory-api
- description: IInventoryService is the modern Steam Inventory Service interface used to add/remove/exchange items, manage definitions, and query inventories at scale.
  name: IInventoryService
  slug: steam-inventory-service-api
- description: ISteamGameServer issues and manages persistent Game Server Login Tokens (GSLTs) used by dedicated game servers to authenticate to Steam.
  name: ISteamGameServer
  slug: steam-game-server-api
- description: ISteamRemoteStorage exposes Steam Cloud and UGC (user-generated content) storage endpoints — fetching files, retrieving UGC details, and listing published files.
  name: ISteamRemoteStorage
  slug: steam-remote-storage-api
- description: ISteamLeaderboards manages per-app leaderboards — creation, score upload/reset, and entry retrieval.
  name: ISteamLeaderboards
  slug: steam-leaderboards-api
- description: IPlayerService exposes player-centric endpoints (GetOwnedGames, GetRecentlyPlayedGames, GetSteamLevel, GetBadges, IsPlayingSharedGame).
  name: IPlayerService
  slug: steam-player-service-api
- description: IGameNotificationsService delivers turn-based and prompt-style in-game notifications to players (UpdateNotificationSettings, UserCreateSession).
  name: IGameNotificationsService
  slug: steam-game-notifications-api
- description: ISteamWebAPIUtil provides helper endpoints — GetServerInfo (Steam server time/version) and GetSupportedAPIList (interfaces and methods callable by the API key).
  name: ISteamWebAPIUtil
  slug: steam-webapi-util-api
- description: IPublishedFileService manages Steam Workshop / UGC published files — query, vote, change visibility, manage tags and previews.
  name: IPublishedFileService
  slug: steam-publishedfile-api
- description: IBroadcastService exposes Steam game-broadcast metadata and stream-discovery endpoints used for in-app broadcast lookups.
  name: IBroadcastService
  slug: steam-broadcast-api
- description: An unofficial-but-widely-used set of storefront endpoints (https://store.steampowered.com/api/) returns app details, package details, currency conversion, and feature lists. Used by community sites an
  name: Steam Store API
  slug: steam-storefront-api
- description: ISteamCheckout is the partner-only interface used to initiate, authorize, and finalize in-game microtransaction purchases through Steam Checkout.
  name: ISteamCheckout
  slug: steam-checkout-api
- description: ISteamMicroTxn / ISteamMicroTxnSandbox handle the full microtransaction lifecycle — InitTxn, FinalizeTxn, GetReport, RefundTxn, QueryTxn — used by F2P and live-service titles.
  name: ISteamMicroTxn
  slug: steam-microtxn-api
- description: ISteamDeepLinkService creates and resolves time-limited deep links into the Steam client and store, useful for marketing campaigns and partner referrals.
  name: ISteamDeepLinkService
  slug: steam-deeplinkservice-api
- description: The IPlayerService API from Steam — 3 operation(s) for iplayerservice.
  name: Steam IPlayerService API
  slug: steam-iplayerservice-api
- description: The ISteamNews API from Steam — 1 operation(s) for isteamnews.
  name: Steam ISteamNews API
  slug: steam-isteamnews-api
- description: The ISteamUser API from Steam — 4 operation(s) for isteamuser.
  name: Steam ISteamUser API
  slug: steam-isteamuser-api
- description: The ISteamUserStats API from Steam — 3 operation(s) for isteamuserstats.
  name: Steam ISteamUserStats API
  slug: steam-isteamuserstats-api
artifact_total: 32
collections:
- collection_type: open
  name: Steamworks Web API
  slug: open-steam
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/steam-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/steam-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/steam-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/valvesoftware
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/valvesoftware
- group: company
  title: ''
  type: Website
  url: https://store.steampowered.com/
- group: docs
  title: ''
  type: Documentation
  url: https://partner.steamgames.com/doc/home
- group: docs
  title: ''
  type: APIReference
  url: https://partner.steamgames.com/doc/webapi
- group: docs
  title: ''
  type: Public Web API Docs
  url: https://steamcommunity.com/dev
- group: start
  title: ''
  type: GettingStarted
  url: https://partner.steamgames.com/doc/gettingstarted
- group: auth
  title: ''
  type: API Key Registration
  url: https://steamcommunity.com/dev/apikey
- group: other
  title: ''
  type: Steam Direct
  url: https://partner.steamgames.com/steamdirect
- group: build
  title: ''
  type: Steamworks SDK
  url: https://partner.steamgames.com/doc/sdk
- group: docs
  title: ''
  type: Steam Workshop Docs
  url: https://partner.steamgames.com/doc/features/workshop
- group: start
  title: ''
  type: Signup
  url: https://partner.steamgames.com/
- group: start
  title: ''
  type: Login
  url: https://store.steampowered.com/login/
- group: operate
  title: ''
  type: StatusPage
  url: https://steamstat.us/
- group: operate
  title: ''
  type: Status (Official)
  url: https://store.steampowered.com/stats/
- group: other
  title: ''
  type: Steam Store
  url: https://store.steampowered.com/
- group: operate
  title: ''
  type: Steam Community
  url: https://steamcommunity.com/
- group: operate
  title: ''
  type: Steamworks Discord
  url: https://discord.gg/steamworks
- group: docs
  title: ''
  type: Steamworks Documentation
  url: https://partner.steamgames.com/doc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://store.steampowered.com/privacy_agreement/
- group: commercial
  title: ''
  type: Subscriber Agreement
  url: https://store.steampowered.com/subscriber_agreement/
- group: commercial
  title: ''
  type: Steam Web API Terms of Use
  url: https://steamcommunity.com/dev/apiterms
- group: operate
  title: ''
  type: Steamworks Forum
  url: https://steamcommunity.com/groups/steamworks
- group: commercial
  title: ''
  type: Plans
  url: plans/steam-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/steam-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/steam-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://store.steampowered.com/feeds/news.xml
created: '2026-05-08'
description: Steam is Valve's PC gaming platform and digital distribution storefront. Valve exposes the Steamworks Web API at https://api.steampowered.com/ — a constellation of HTTP interfaces for games, players, friends, achievements, items, the economy, leaderboards, remote storage, and the Steam Workshop. A subset of read-only interfaces are public (with a Steam Web API key); the full Steamworks set requires a publisher account and partner-restricted methods. There is no per-call fee for the Steamworks Web API itself; Valve monetizes through a $100 Steam Direct submission fee per product and a revenue share on store sales.
finops:
- name: Steam Finops
  service_category: Gaming Distribution
  slug: steam-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/steam.png
layout: provider
modified: '2026-05-08'
name: Steam
nav: Providers
network: true
overview: 'Steam publishes 4 APIs on the [APIs.io](https://apis.io/) network, including IPlayerService API, ISteamNews API, ISteamUser API, and 1 more. Tagged areas include Gaming, Valve, Distribution, Steamworks, and Marketplace.


  Steam''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, engineering blog, and 24 more developer resources.'
plans:
- name: Steam Plans Pricing
  plan_count: 3
  slug: steam-plans-pricing
random_paper: 86
rate_limits:
- limit_count: 5
  name: Steam Rate Limits
  slug: steam-rate-limits
score:
  band: developing
  composite: 45.8
  delta: 0.0
  facets:
    commercial_clarity: 63.2
    contract_quality: 51.9
    developer_ergonomics: 39.1
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 45.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/steam/refs/heads/main/screenshots/steam-2026-06-20T194532.png
security:
- kind: authentication
  name: Steam Authentication
  slug: steam-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Steam Domain Security
  slug: steam-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: steam
tags:
- Gaming
- Valve
- Distribution
- Steamworks
- Marketplace
- Web API
website: https://store.steampowered.com/
---

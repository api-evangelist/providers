---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 62
  human_in_the_loop: 3
  name: Unity Agentic Access
  operation_count: 98
  slug: unity-agentic-access
  summary_line: 98 operations · 62 acting · 3 human-in-the-loop
api_count: 33
apis:
- description: Vivox provides voice and text-based communication services for games, with APIs for managing channels, participants, and communication sessions across platforms. Supports 2D and 3D positional audio.
  name: Unity Vivox Voice and Text Chat API
  slug: vivox
- description: 'The User Generated Content (UGC) API is a format and content-agnostic service for incorporating user-generated content features into games, handling content storage, discovery, ingestion, moderation, '
  name: Unity User Generated Content API
  slug: user-generated-content
- description: Allocate servers for game sessions
  name: Unity Allocations API
  slug: unity-allocations-api
- description: Player sign-in and token management
  name: Unity Authentication API
  slug: unity-authentication-api
- description: Manage blocked players
  name: Unity Blocks API
  slug: unity-blocks-api
- description: Configure build targets and platforms
  name: Unity Build Targets API
  slug: unity-build-targets-api
- description: Manage and trigger builds
  name: Unity Builds API
  slug: unity-builds-api
- description: Manage remote configuration key-value pairs
  name: Unity Config API
  slug: unity-config-api
- description: Admin endpoints for managing economy resources
  name: Unity Configuration API
  slug: unity-configuration-api
- description: Manage virtual currencies and player balances
  name: Unity Currencies API
  slug: unity-currencies-api
- description: Manage custom data with access class controls
  name: Unity Custom Data API
  slug: unity-custom-data-api
- description: Ingest analytics events
  name: Unity Events API
  slug: unity-events-api
- description: Execute cloud code scripts
  name: Unity Executions API
  slug: unity-executions-api
- description: Manage server fleets
  name: Unity Fleets API
  slug: unity-fleets-api
- description: Send and receive friend requests
  name: Unity Friend Requests API
  slug: unity-friend-requests-api
- description: Manage player friend lists
  name: Unity Friends API
  slug: unity-friends-api
- description: External identity provider linking
  name: Unity Identity Providers API
  slug: unity-identity-providers-api
- description: Manage inventory items and player inventory
  name: Unity Inventory API
  slug: unity-inventory-api
- description: Manage leaderboard definitions and configuration
  name: Unity Leaderboards API
  slug: unity-leaderboards-api
- description: Create and manage game lobbies
  name: Unity Lobbies API
  slug: unity-lobbies-api
- description: Manage C# cloud code modules
  name: Unity Modules API
  slug: unity-modules-api
- description: Manage targeting rules for configuration overrides
  name: Unity Override Rules API
  slug: unity-override-rules-api
- description: Manage player-scoped key-value data
  name: Unity Player Data API
  slug: unity-player-data-api
- description: Manage players within a lobby
  name: Unity Players API
  slug: unity-players-api
- description: Process virtual and real-money purchases
  name: Unity Purchases API
  slug: unity-purchases-api
- description: Query stored data using indexes
  name: Unity Queries API
  slug: unity-queries-api
- description: Configure matchmaking queues and pools
  name: Unity Queues API
  slug: unity-queues-api
- description: Submit and retrieve leaderboard scores
  name: Unity Scores API
  slug: unity-scores-api
- description: Manage JavaScript cloud code scripts
  name: Unity Scripts API
  slug: unity-scripts-api
- description: Discover and join lobbies
  name: Unity Search API
  slug: unity-search-api
- description: Manage individual server instances
  name: Unity Servers API
  slug: unity-servers-api
- description: Manage configuration settings and schemas
  name: Unity Settings API
  slug: unity-settings-api
- description: Create and manage matchmaking tickets
  name: Unity Tickets API
  slug: unity-tickets-api
arazzos:
- description: Validate an analytics event batch against the schema, then record it only when validation passes.
  name: Unity Analytics Validate and Record
  slug: unity-analytics-validate-and-record-workflow
- description: Sign a player in anonymously and immediately exchange the session for a refreshed access token.
  name: Unity Anonymous Sign-In and Token Refresh
  slug: unity-anonymous-signin-refresh-workflow
- description: Confirm a build target, start a clean build, then poll the build until it succeeds or fails.
  name: Unity Build Automation Trigger and Poll
  slug: unity-build-trigger-and-poll-workflow
- description: Create a JavaScript Cloud Code script, confirm it deployed, then execute it with parameters.
  name: Unity Cloud Code Deploy and Run
  slug: unity-cloudcode-deploy-and-run-workflow
- description: Write a server-protected stat, publish a public profile item, then read the player's data back.
  name: Unity Cloud Save Publish Public Profile
  slug: unity-cloudsave-publish-public-profile-workflow
- description: Write player data items, query them by an indexed field, then read the full item list back.
  name: Unity Cloud Save Set and Query
  slug: unity-cloudsave-set-and-query-workflow
- description: Resolve a currency configuration, increment a player's balance, then read back the updated balances.
  name: Unity Economy Grant Currency
  slug: unity-economy-grant-currency-workflow
- description: Check a player's currency balances, make a virtual purchase, then confirm the resulting inventory.
  name: Unity Economy Virtual Purchase
  slug: unity-economy-virtual-purchase-workflow
- description: List incoming friend requests, accept the first pending one, then confirm it appears in the friend list.
  name: Unity Friends Accept Incoming Request
  slug: unity-friends-accept-request-workflow
- description: Create a leaderboard, seed it with an initial player score, then read the top scores.
  name: Unity Leaderboard Provisioning
  slug: unity-leaderboard-provision-workflow
- description: Confirm a leaderboard exists, submit a player's score, then read back the player's rank.
  name: Unity Leaderboard Submit Score and Read Rank
  slug: unity-leaderboard-submit-score-workflow
- description: Create a public lobby, send a keep-alive heartbeat, then confirm it is discoverable via query.
  name: Unity Lobby Host and Query
  slug: unity-lobby-host-and-query-workflow
- description: Join a private lobby by code, set the joining player's data, then heartbeat to stay active.
  name: Unity Lobby Join By Code
  slug: unity-lobby-join-by-code-workflow
- description: Create a matchmaking queue, read it back, then list all queues to confirm it is registered.
  name: Unity Matchmaker Queue Provisioning
  slug: unity-matchmaker-queue-provision-workflow
- description: Create a matchmaking ticket, poll until matched, then allocate a Multiplay game server for the session.
  name: Unity Matchmaking to Server Allocation
  slug: unity-matchmaking-allocate-server-workflow
- description: Create a matchmaking ticket and poll its status until a match is found or matchmaking fails.
  name: Unity Matchmaking Ticket and Poll
  slug: unity-matchmaking-ticket-poll-workflow
- description: Register a server build, create a fleet that runs it, then allocate a server from the fleet.
  name: Unity Multiplay Fleet Provisioning and Allocation
  slug: unity-multiplay-fleet-allocate-workflow
- description: Create a username/password player account, link an external identity, then read back the admin player record.
  name: Unity Player Sign-Up and Identity Linking
  slug: unity-player-signup-and-link-workflow
- description: Add a config setting, create a targeted override rule for it, then confirm the rule is listed.
  name: Unity Remote Config Feature Rollout
  slug: unity-remote-config-rollout-workflow
artifact_total: 220
collections:
- collection_type: postman
  name: Unity Analytics Allocations API
  slug: postman-unity-allocations-api
- collection_type: postman
  name: Unity Analytics Allocations Authentication API
  slug: postman-unity-authentication-api
- collection_type: postman
  name: Unity Analytics Allocations Blocks API
  slug: postman-unity-blocks-api
- collection_type: postman
  name: Unity Analytics Allocations Build Targets API
  slug: postman-unity-build-targets-api
- collection_type: postman
  name: Unity Analytics Allocations Builds API
  slug: postman-unity-builds-api
- collection_type: postman
  name: Unity Analytics Allocations Config API
  slug: postman-unity-config-api
- collection_type: postman
  name: Unity Analytics Allocations Configuration API
  slug: postman-unity-configuration-api
- collection_type: postman
  name: Unity Analytics Allocations Currencies API
  slug: postman-unity-currencies-api
- collection_type: postman
  name: Unity Analytics Allocations Custom Data API
  slug: postman-unity-custom-data-api
- collection_type: postman
  name: Unity Analytics Allocations Events API
  slug: postman-unity-events-api
- collection_type: postman
  name: Unity Analytics Allocations Executions API
  slug: postman-unity-executions-api
- collection_type: postman
  name: Unity Analytics Allocations Fleets API
  slug: postman-unity-fleets-api
- collection_type: postman
  name: Unity Analytics Allocations Friend Requests API
  slug: postman-unity-friend-requests-api
- collection_type: postman
  name: Unity Analytics Allocations Friends API
  slug: postman-unity-friends-api
- collection_type: postman
  name: Unity Analytics Allocations Identity Providers API
  slug: postman-unity-identity-providers-api
- collection_type: postman
  name: Unity Analytics Allocations Inventory API
  slug: postman-unity-inventory-api
- collection_type: postman
  name: Unity Analytics Allocations Leaderboards API
  slug: postman-unity-leaderboards-api
- collection_type: postman
  name: Unity Analytics Allocations Lobbies API
  slug: postman-unity-lobbies-api
- collection_type: postman
  name: Unity Analytics Allocations Modules API
  slug: postman-unity-modules-api
- collection_type: postman
  name: Unity Analytics Allocations Override Rules API
  slug: postman-unity-override-rules-api
- collection_type: postman
  name: Unity Analytics Allocations Player Data API
  slug: postman-unity-player-data-api
- collection_type: postman
  name: Unity Analytics Allocations Players API
  slug: postman-unity-players-api
- collection_type: postman
  name: Unity Analytics Allocations Purchases API
  slug: postman-unity-purchases-api
- collection_type: postman
  name: Unity Analytics Allocations Queries API
  slug: postman-unity-queries-api
- collection_type: postman
  name: Unity Analytics Allocations Queues API
  slug: postman-unity-queues-api
- collection_type: postman
  name: Unity Analytics Allocations Scores API
  slug: postman-unity-scores-api
- collection_type: postman
  name: Unity Analytics Allocations Scripts API
  slug: postman-unity-scripts-api
- collection_type: postman
  name: Unity Analytics Allocations Search API
  slug: postman-unity-search-api
- collection_type: postman
  name: Unity Analytics Allocations Servers API
  slug: postman-unity-servers-api
- collection_type: postman
  name: Unity Analytics Allocations Settings API
  slug: postman-unity-settings-api
- collection_type: postman
  name: Unity Analytics Allocations Tickets API
  slug: postman-unity-tickets-api
- collection_type: open
  name: Unity Analytics API
  slug: open-unity-analytics
- collection_type: open
  name: Unity Build Automation API
  slug: open-unity-build-automation
- collection_type: open
  name: Unity Cloud Code API
  slug: open-unity-cloud-code
- collection_type: open
  name: Unity Cloud Save API
  slug: open-unity-cloud-save
- collection_type: open
  name: Unity Economy API
  slug: open-unity-economy
- collection_type: open
  name: Unity Friends API
  slug: open-unity-friends
- collection_type: open
  name: Unity Leaderboards API
  slug: open-unity-leaderboards
- collection_type: open
  name: Unity Lobby API
  slug: open-unity-lobby
- collection_type: open
  name: Unity Matchmaker API
  slug: open-unity-matchmaker
- collection_type: open
  name: Unity Multiplay Game Server Hosting API
  slug: open-unity-multiplay
- collection_type: open
  name: Unity Player Authentication API
  slug: open-unity-player-authentication
- collection_type: open
  name: Unity Remote Config API
  slug: open-unity-remote-config
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/unity/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/unity-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/unity-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unity-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unity-authentication.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/unity-analytics-validate-and-record-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/unity-anonymous-signin-refresh-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/unity-build-trigger-and-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/unity-cloudcode-deploy-and-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/unity-cloudsave-publish-public-profile-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/unity-cloudsave-set-and-query-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/unity-economy-grant-currency-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/unity-economy-virtual-purchase-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/unity-friends-accept-request-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/unity-leaderboard-provision-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/unity-leaderboard-submit-score-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/unity-lobby-host-and-query-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/unity-lobby-join-by-code-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/unity-matchmaker-queue-provision-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/unity-matchmaking-allocate-server-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/unity-matchmaking-ticket-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/unity-multiplay-fleet-allocate-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/unity-player-signup-and-link-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/unity-remote-config-rollout-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unity
- group: start
  title: ''
  type: Portal
  url: https://cloud.unity.com
- group: other
  title: ''
  type: Dashboard
  url: https://dashboard.unity3d.com
- group: start
  title: ''
  type: Signup
  url: https://id.unity.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.unity.com
- group: operate
  title: ''
  type: Support
  url: https://support.unity.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://unity.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://unity.com/legal/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://blog.unity.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Unity-Technologies
- group: docs
  title: ''
  type: APIReference
  url: https://services.docs.unity.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unity.com/ugs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.unity.com/ugs/en-us/manual/overview/manual/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://services.docs.unity.com/docs/service-account-auth/
- group: auth
  title: ''
  type: Authentication
  url: https://services.docs.unity.com/docs/client-auth/
- group: commercial
  title: ''
  type: Pricing
  url: https://unity.com/products/gaming-services/pricing
- group: operate
  title: ''
  type: Forums
  url: https://discussions.unity.com/
- group: operate
  title: ''
  type: Community
  url: https://unity.com/community
- group: build
  title: ''
  type: Developer Tools
  url: https://unity.com/developer-tools
- group: operate
  title: ''
  type: FAQ
  url: https://unity.com/faq
- group: design
  title: ''
  type: ErrorCodes
  url: https://services.docs.unity.com/docs/errors/
- group: design
  title: ''
  type: API Lifecycle
  url: https://services.docs.unity.com/docs/api-lifecycle/
- group: operate
  title: ''
  type: ChangeLog
  url: https://unity.com/releases/unity-6/support
- group: other
  title: ''
  type: Marketplace
  url: https://assetstore.unity.com
- group: learn
  title: ''
  type: Learning
  url: https://learn.unity.com
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/rules/unity-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/vocabulary/unity-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/json-ld/unity-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.unity.com/llms.txt
created: '2025-01-08'
description: Unity is a cross-platform real-time development platform that provides a comprehensive suite of APIs and services for game development, interactive 3D content creation, and live game operations including multiplayer, analytics, economy, authentication, and DevOps tooling.
examples:
- key_count: 4
  name: Unity Cloud Save Set Player Data Example
  slug: unity-cloud-save-set-player-data-example
- key_count: 4
  name: Unity Economy Make Virtual Purchase Example
  slug: unity-economy-make-virtual-purchase-example
- key_count: 4
  name: Unity Leaderboards Add Player Score Example
  slug: unity-leaderboards-add-player-score-example
- key_count: 4
  name: Unity Lobby Create Lobby Example
  slug: unity-lobby-create-lobby-example
- key_count: 4
  name: Unity Matchmaker Create Ticket Example
  slug: unity-matchmaker-create-ticket-example
- key_count: 4
  name: Unity Player Authentication Sign In Anonymously Example
  slug: unity-player-authentication-sign-in-anonymously-example
finops:
- name: Unity Finops
  service_category: Game Development Platform
  slug: unity-finops
graphqls:
- description: 'This conceptual GraphQL schema represents the Unity Gaming Services (UGS) platform, covering the full breadth of cloud services available to game developers. Unity Gaming Services provides a suite of '
  name: Unity Gaming Services GraphQL Schema
  slug: unity-graphql
image: https://unity.com/logo.png
json_schemas:
- name: AllocateServerRequest
  property_count: 1
  slug: unity-allocateserverrequest
- name: Allocation
  property_count: 5
  slug: unity-allocation
- name: AnalyticsEvent
  property_count: 13
  slug: unity-analyticsevent
- name: AnonymousSignInRequest
  property_count: 1
  slug: unity-anonymoussigninrequest
- name: AuthResponse
  property_count: 5
  slug: unity-authresponse
- name: Build
  property_count: 10
  slug: unity-build
- name: BuildArtifact
  property_count: 5
  slug: unity-buildartifact
- name: BuildConfiguration
  property_count: 7
  slug: unity-buildconfiguration
- name: BuildList
  property_count: 1
  slug: unity-buildlist
- name: BuildTarget
  property_count: 7
  slug: unity-buildtarget
- name: Config
  property_count: 7
  slug: unity-config
- name: ConfigList
  property_count: 1
  slug: unity-configlist
- name: CreateBuildRequest
  property_count: 2
  slug: unity-createbuildrequest
- name: CreateBuildTargetRequest
  property_count: 4
  slug: unity-createbuildtargetrequest
- name: CreateFleetRequest
  property_count: 3
  slug: unity-createfleetrequest
- name: CreateLobbyRequest
  property_count: 5
  slug: unity-createlobbyrequest
- name: CreatePlayerRequest
  property_count: 2
  slug: unity-createplayerrequest
- name: CreateQueueRequest
  property_count: 4
  slug: unity-createqueuerequest
- name: CreateRuleRequest
  property_count: 8
  slug: unity-createrulerequest
- name: CreateScriptRequest
  property_count: 4
  slug: unity-createscriptrequest
- name: CreateTicketRequest
  property_count: 3
  slug: unity-createticketrequest
- name: CurrencyBalance
  property_count: 5
  slug: unity-currencybalance
- name: CurrencyBalanceUpdate
  property_count: 2
  slug: unity-currencybalanceupdate
- name: DataItem
  property_count: 5
  slug: unity-dataitem
- name: DataObject
  property_count: 3
  slug: unity-dataobject
- name: Unity Economy Configuration
  property_count: 8
  slug: unity-economy-config
- name: EconomyConfig
  property_count: 8
  slug: unity-economyconfig
- name: EconomyConfigList
  property_count: 2
  slug: unity-economyconfiglist
- name: EscalationRules
  property_count: 2
  slug: unity-escalationrules
- name: ExternalTokenSignInRequest
  property_count: 3
  slug: unity-externaltokensigninrequest
- name: FieldFilter
  property_count: 3
  slug: unity-fieldfilter
- name: Fleet
  property_count: 10
  slug: unity-fleet
- name: FleetList
  property_count: 1
  slug: unity-fleetlist
- name: FriendList
  property_count: 2
  slug: unity-friendlist
- name: FriendRequestList
  property_count: 2
  slug: unity-friendrequestlist
- name: InventoryItem
  property_count: 7
  slug: unity-inventoryitem
- name: JoinLobbyRequest
  property_count: 2
  slug: unity-joinlobbyrequest
- name: Unity Leaderboard
  property_count: 8
  slug: unity-leaderboard
- name: LeaderboardCreate
  property_count: 5
  slug: unity-leaderboardcreate
- name: LeaderboardList
  property_count: 2
  slug: unity-leaderboardlist
- name: LeaderboardScoreList
  property_count: 4
  slug: unity-leaderboardscorelist
- name: LeaderboardUpdate
  property_count: 3
  slug: unity-leaderboardupdate
- name: Lobby
  property_count: 12
  slug: unity-lobby
- name: LobbyList
  property_count: 2
  slug: unity-lobbylist
- name: LobbyPlayer
  property_count: 4
  slug: unity-lobbyplayer
- name: MatchAssignment
  property_count: 2
  slug: unity-matchassignment
- name: MatchLogic
  property_count: 2
  slug: unity-matchlogic
- name: Module
  property_count: 6
  slug: unity-module
- name: ModuleList
  property_count: 1
  slug: unity-modulelist
- name: Unity Player
  property_count: 5
  slug: unity-player
- name: PlayerCurrencyBalances
  property_count: 1
  slug: unity-playercurrencybalances
- name: PlayerDataList
  property_count: 2
  slug: unity-playerdatalist
- name: PlayerInventory
  property_count: 1
  slug: unity-playerinventory
- name: PlayerList
  property_count: 2
  slug: unity-playerlist
- name: PlayerProfile
  property_count: 3
  slug: unity-playerprofile
- name: PlayerScore
  property_count: 7
  slug: unity-playerscore
- name: Pool
  property_count: 4
  slug: unity-pool
- name: Presence
  property_count: 2
  slug: unity-presence
- name: QueryFilter
  property_count: 3
  slug: unity-queryfilter
- name: QueryLobbiesRequest
  property_count: 4
  slug: unity-querylobbiesrequest
- name: QueryOrder
  property_count: 2
  slug: unity-queryorder
- name: QueryRequest
  property_count: 4
  slug: unity-queryrequest
- name: QueryResult
  property_count: 4
  slug: unity-queryresult
- name: Queue
  property_count: 6
  slug: unity-queue
- name: QueueList
  property_count: 1
  slug: unity-queuelist
- name: RecordEventsRequest
  property_count: 1
  slug: unity-recordeventsrequest
- name: RefreshTokenRequest
  property_count: 1
  slug: unity-refreshtokenrequest
- name: Relationship
  property_count: 4
  slug: unity-relationship
- name: RelationshipList
  property_count: 1
  slug: unity-relationshiplist
- name: ResetConfig
  property_count: 3
  slug: unity-resetconfig
- name: Rule
  property_count: 9
  slug: unity-rule
- name: RuleList
  property_count: 1
  slug: unity-rulelist
- name: RunScriptRequest
  property_count: 1
  slug: unity-runscriptrequest
- name: ScalingSettings
  property_count: 2
  slug: unity-scalingsettings
- name: ScoreSubmission
  property_count: 2
  slug: unity-scoresubmission
- name: Script
  property_count: 7
  slug: unity-script
- name: ScriptList
  property_count: 2
  slug: unity-scriptlist
- name: ScriptParameter
  property_count: 3
  slug: unity-scriptparameter
- name: ScriptRunResult
  property_count: 1
  slug: unity-scriptrunresult
- name: ScriptVersion
  property_count: 2
  slug: unity-scriptversion
- name: Server
  property_count: 7
  slug: unity-server
- name: ServerList
  property_count: 1
  slug: unity-serverlist
- name: SetPlayerDataRequest
  property_count: 1
  slug: unity-setplayerdatarequest
- name: Setting
  property_count: 4
  slug: unity-setting
- name: SettingsList
  property_count: 1
  slug: unity-settingslist
- name: StartBuildRequest
  property_count: 2
  slug: unity-startbuildrequest
- name: TicketAttributes
  property_count: 2
  slug: unity-ticketattributes
- name: TicketCreated
  property_count: 1
  slug: unity-ticketcreated
- name: TicketStatus
  property_count: 3
  slug: unity-ticketstatus
- name: TieringConfig
  property_count: 2
  slug: unity-tieringconfig
- name: Timestamp
  property_count: 1
  slug: unity-timestamp
- name: UnlinkIdentityRequest
  property_count: 1
  slug: unity-unlinkidentityrequest
- name: UpdateBuildTargetRequest
  property_count: 3
  slug: unity-updatebuildtargetrequest
- name: UpdateConfigRequest
  property_count: 2
  slug: unity-updateconfigrequest
- name: UpdateFleetRequest
  property_count: 3
  slug: unity-updatefleetrequest
- name: UpdateLobbyRequest
  property_count: 6
  slug: unity-updatelobbyrequest
- name: UpdatePlayerRequest
  property_count: 1
  slug: unity-updateplayerrequest
- name: UpdateQueueRequest
  property_count: 3
  slug: unity-updatequeuerequest
- name: UpdateRuleRequest
  property_count: 8
  slug: unity-updaterulerequest
- name: UpdateScriptRequest
  property_count: 2
  slug: unity-updatescriptrequest
- name: UsernamePasswordSignInRequest
  property_count: 2
  slug: unity-usernamepasswordsigninrequest
- name: UsernamePasswordSignUpRequest
  property_count: 2
  slug: unity-usernamepasswordsignuprequest
- name: ValidationResult
  property_count: 1
  slug: unity-validationresult
- name: VirtualPurchaseRequest
  property_count: 1
  slug: unity-virtualpurchaserequest
- name: VirtualPurchaseResult
  property_count: 3
  slug: unity-virtualpurchaseresult
json_structures:
- name: Unity Lobby Structure
  property_count: 0
  slug: unity-lobby-structure
- name: Unity Player Structure
  property_count: 0
  slug: unity-player-structure
- name: Unity Structure
  property_count: 0
  slug: unity-structure
jsonld:
- class_count: 8
  name: Unity Context
  property_count: 28
  slug: unity-context
layout: provider
modified: '2026-05-19'
name: Unity
nav: Providers
network: true
overview: 'Unity publishes 31 APIs on the [APIs.io](https://apis.io/) network, including Allocations API, Authentication API, Blocks API, and 28 more. Tagged areas include Game Development, Real-Time 3D, Multiplayer, Game Services, and Cloud Gaming.


  The Unity catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Unity''s developer surface includes authentication, developer portal, signup flow, support, engineering blog, API reference, documentation, and 46 more developer resources.'
plans:
- name: Unity Plans Pricing
  plan_count: 1
  slug: unity-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Unity Rate Limits
  slug: unity-rate-limits
rules:
- name: Unity API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: unity-jsonschema-spectral-rules
- name: Unity API Rules
  rule_count: 23
  severity_counts:
    error: 8
    hint: 1
    info: 2
    warn: 12
  slug: unity-spectral-rules
score:
  band: strong
  composite: 65.2
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 74.1
    developer_ergonomics: 56.5
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 57.9
  previous_composite: 65.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 31
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/screenshots/unity-2026-06-20T200106.png
security:
- kind: authentication
  name: Unity Authentication
  slug: unity-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Unity Domain Security
  slug: unity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Unity Trust Center
  slug: unity-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: unity
tags:
- Game Development
- Real-Time 3D
- Multiplayer
- Game Services
- Cloud Gaming
website: https://cloud.unity.com
---

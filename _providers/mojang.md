---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Mojang Agentic Access
  operation_count: 29
  slug: mojang-agentic-access
  summary_line: 29 operations · 14 acting · 1 human-in-the-loop
api_count: 14
apis:
- description: Profanity filter, friends, chat preferences
  name: Mojang Attributes API
  slug: mojang-attributes-api
- description: Exchange Xbox Live tokens for Minecraft access tokens
  name: Mojang Authentication API
  slug: mojang-authentication-api
- description: Player privacy blocklist
  name: Mojang Blocklist API
  slug: mojang-blocklist-api
- description: Cape selection and visibility
  name: Mojang Capes API
  slug: mojang-capes-api
- description: Account ownership and entitlement checks
  name: Mojang Entitlements API
  slug: mojang-entitlements-api
- description: Friends graph (list, add, remove)
  name: Mojang Friends API
  slug: mojang-friends-api
- description: Player UUID and username lookup
  name: Mojang Identity API
  slug: mojang-identity-api
- description: Signature keypairs and Mojang public keys
  name: Mojang Keys API
  slug: mojang-keys-api
- description: Online / playing presence reporting
  name: Mojang Presence API
  slug: mojang-presence-api
- description: Authenticated profile and name management
  name: Mojang Profile API
  slug: mojang-profile-api
- description: Server-policy artifacts (blocked servers)
  name: Mojang Server API
  slug: mojang-server-api
- description: Login-handshake session verification
  name: Mojang Session API
  slug: mojang-session-api
- description: Skin selection, upload, and reset
  name: Mojang Skins API
  slug: mojang-skins-api
- description: Player skin and cape texture lookup
  name: Mojang Textures API
  slug: mojang-textures-api
artifact_total: 129
collections:
- collection_type: open
  name: Minecraft Services API
  slug: open-mojang-minecraft-services
- collection_type: open
  name: Mojang Public API
  slug: open-mojang-public-api
- collection_type: open
  name: Mojang Session Server
  slug: open-mojang-session-server
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mojang-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mojang-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mojang-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.minecraft.net
- group: docs
  title: ''
  type: Documentation
  url: https://minecraft.wiki/w/Mojang_API
- group: docs
  title: Microsoft / Xbox Authentication Flow
  type: Documentation
  url: https://minecraft.wiki/w/Microsoft_authentication
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Mojang
- group: build
  title: Brigadier Command Parser
  type: GitHubRepository
  url: https://github.com/Mojang/brigadier
- group: build
  title: DataFixerUpper
  type: GitHubRepository
  url: https://github.com/Mojang/DataFixerUpper
- group: build
  title: Bedrock Network Protocol Docs
  type: GitHubRepository
  url: https://github.com/Mojang/bedrock-protocol-docs
- group: build
  title: Bedrock Edition Add-on Samples
  type: GitHubRepository
  url: https://github.com/Mojang/bedrock-samples
- group: build
  title: Minecraft Creator Tools
  type: GitHubRepository
  url: https://github.com/Mojang/minecraft-creator-tools
- group: build
  title: Minecraft VS Code Debugger
  type: GitHubRepository
  url: https://github.com/Mojang/minecraft-debugger
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mojang-rate-limits.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/mojang-vocabulary.yaml
- group: design
  title: ''
  type: SpectralRules
  url: rules/mojang-spectral-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/mojang-api-context.jsonld
created: '2026-05-28'
description: 'Mojang Studios is the developer of Minecraft. The Mojang / Minecraft Services API surface covers Minecraft player identity (UUID and profile lookup), skins and capes, name history and name change, server session verification, blocked server lists, player attributes (privacy, chat, friends settings), friends graph, presence, public keys for profile signature verification, and account entitlements. Endpoints span three hosts: the legacy api.mojang.com, the session-server sessionserver.mojang.com (Yggdrasil), and the modern Microsoft-side api.minecraftservices.com. Most read endpoints are public and unauthenticated; player-account endpoints require a Bearer Minecraft access token obtained via the Xbox Live / XSTS authentication chain.'
examples:
- key_count: 5
  name: Minecraft Services Authenticated Profile Example
  slug: minecraft-services-authenticated-profile-example
- key_count: 1
  name: Minecraft Services Ban Status Example
  slug: minecraft-services-ban-status-example
- key_count: 1
  name: Minecraft Services Blocklist Example
  slug: minecraft-services-blocklist-example
- key_count: 4
  name: Minecraft Services Cape Example
  slug: minecraft-services-cape-example
- key_count: 1
  name: Minecraft Services Cape Selection Example
  slug: minecraft-services-cape-selection-example
- key_count: 2
  name: Minecraft Services Change Skin Request Example
  slug: minecraft-services-change-skin-request-example
- key_count: 3
  name: Minecraft Services Entitlement Item Example
  slug: minecraft-services-entitlement-item-example
- key_count: 3
  name: Minecraft Services Entitlements Example
  slug: minecraft-services-entitlements-example
- key_count: 2
  name: Minecraft Services Friend Example
  slug: minecraft-services-friend-example
- key_count: 3
  name: Minecraft Services Friend Update Request Example
  slug: minecraft-services-friend-update-request-example
- key_count: 4
  name: Minecraft Services Friends List Example
  slug: minecraft-services-friends-list-example
- key_count: 1
  name: Minecraft Services Friends Preferences Example
  slug: minecraft-services-friends-preferences-example
- key_count: 5
  name: Minecraft Services Minecraft Access Token Example
  slug: minecraft-services-minecraft-access-token-example
- key_count: 1
  name: Minecraft Services Name Availability Example
  slug: minecraft-services-name-availability-example
- key_count: 3
  name: Minecraft Services Name Change Info Example
  slug: minecraft-services-name-change-info-example
- key_count: 4
  name: Minecraft Services Player Attributes Example
  slug: minecraft-services-player-attributes-example
- key_count: 2
  name: Minecraft Services Player Attributes Update Example
  slug: minecraft-services-player-attributes-update-example
- key_count: 5
  name: Minecraft Services Player Certificates Example
  slug: minecraft-services-player-certificates-example
- key_count: 3
  name: Minecraft Services Presence Entry Example
  slug: minecraft-services-presence-entry-example
- key_count: 2
  name: Minecraft Services Presence Report Example
  slug: minecraft-services-presence-report-example
- key_count: 4
  name: Minecraft Services Privilege Map Example
  slug: minecraft-services-privilege-map-example
- key_count: 1
  name: Minecraft Services Profanity Filter Preferences Example
  slug: minecraft-services-profanity-filter-preferences-example
- key_count: 2
  name: Minecraft Services Profile Example
  slug: minecraft-services-profile-example
- key_count: 1
  name: Minecraft Services Public Key Entry Example
  slug: minecraft-services-public-key-entry-example
- key_count: 3
  name: Minecraft Services Public Keys Example
  slug: minecraft-services-public-keys-example
- key_count: 6
  name: Minecraft Services Skin Example
  slug: minecraft-services-skin-example
- key_count: 2
  name: Minecraft Services Xbox Login Request Example
  slug: minecraft-services-xbox-login-request-example
- key_count: 2
  name: Public Api Name Change Example
  slug: public-api-name-change-example
- key_count: 4
  name: Public Api Profile Example
  slug: public-api-profile-example
- key_count: 3
  name: Public Api Sale Statistics Example
  slug: public-api-sale-statistics-example
- key_count: 1
  name: Public Api Sale Statistics Request Example
  slug: public-api-sale-statistics-request-example
- key_count: 3
  name: Session Server Join Request Example
  slug: session-server-join-request-example
- key_count: 4
  name: Session Server Session Profile Example
  slug: session-server-session-profile-example
- key_count: 3
  name: Session Server Session Property Example
  slug: session-server-session-property-example
image: https://www.minecraft.net/etc.clientlibs/minecraft/clientlibs/main/resources/img/menu/menu-buy--reversed.gif
json_schemas:
- name: AuthenticatedProfile
  property_count: 5
  slug: minecraft-services-authenticated-profile
- name: BanStatus
  property_count: 1
  slug: minecraft-services-ban-status
- name: Blocklist
  property_count: 1
  slug: minecraft-services-blocklist
- name: Cape
  property_count: 4
  slug: minecraft-services-cape
- name: CapeSelection
  property_count: 1
  slug: minecraft-services-cape-selection
- name: ChangeSkinRequest
  property_count: 2
  slug: minecraft-services-change-skin-request
- name: EntitlementItem
  property_count: 3
  slug: minecraft-services-entitlement-item
- name: Entitlements
  property_count: 3
  slug: minecraft-services-entitlements
- name: Friend
  property_count: 2
  slug: minecraft-services-friend
- name: FriendUpdateRequest
  property_count: 3
  slug: minecraft-services-friend-update-request
- name: FriendsList
  property_count: 4
  slug: minecraft-services-friends-list
- name: FriendsPreferences
  property_count: 1
  slug: minecraft-services-friends-preferences
- name: MinecraftAccessToken
  property_count: 5
  slug: minecraft-services-minecraft-access-token
- name: NameAvailability
  property_count: 1
  slug: minecraft-services-name-availability
- name: NameChangeInfo
  property_count: 3
  slug: minecraft-services-name-change-info
- name: PlayerAttributes
  property_count: 4
  slug: minecraft-services-player-attributes
- name: PlayerAttributesUpdate
  property_count: 2
  slug: minecraft-services-player-attributes-update
- name: PlayerCertificates
  property_count: 5
  slug: minecraft-services-player-certificates
- name: PresenceEntry
  property_count: 3
  slug: minecraft-services-presence-entry
- name: PresenceReport
  property_count: 2
  slug: minecraft-services-presence-report
- name: PrivilegeMap
  property_count: 4
  slug: minecraft-services-privilege-map
- name: ProfanityFilterPreferences
  property_count: 1
  slug: minecraft-services-profanity-filter-preferences
- name: Profile
  property_count: 2
  slug: minecraft-services-profile
- name: PublicKeyEntry
  property_count: 1
  slug: minecraft-services-public-key-entry
- name: PublicKeys
  property_count: 3
  slug: minecraft-services-public-keys
- name: Skin
  property_count: 6
  slug: minecraft-services-skin
- name: XboxLoginRequest
  property_count: 2
  slug: minecraft-services-xbox-login-request
- name: NameChange
  property_count: 2
  slug: public-api-name-change
- name: Profile
  property_count: 4
  slug: public-api-profile
- name: SaleStatisticsRequest
  property_count: 1
  slug: public-api-sale-statistics-request
- name: SaleStatistics
  property_count: 3
  slug: public-api-sale-statistics
- name: JoinRequest
  property_count: 3
  slug: session-server-join-request
- name: SessionProfile
  property_count: 4
  slug: session-server-session-profile
- name: SessionProperty
  property_count: 3
  slug: session-server-session-property
json_structures:
- name: Minecraft Services Authenticated Profile Structure
  property_count: 5
  slug: minecraft-services-authenticated-profile-structure
- name: Minecraft Services Ban Status Structure
  property_count: 1
  slug: minecraft-services-ban-status-structure
- name: Minecraft Services Blocklist Structure
  property_count: 1
  slug: minecraft-services-blocklist-structure
- name: Minecraft Services Cape Selection Structure
  property_count: 1
  slug: minecraft-services-cape-selection-structure
- name: Minecraft Services Cape Structure
  property_count: 4
  slug: minecraft-services-cape-structure
- name: Minecraft Services Change Skin Request Structure
  property_count: 2
  slug: minecraft-services-change-skin-request-structure
- name: Minecraft Services Entitlement Item Structure
  property_count: 3
  slug: minecraft-services-entitlement-item-structure
- name: Minecraft Services Entitlements Structure
  property_count: 3
  slug: minecraft-services-entitlements-structure
- name: Minecraft Services Friend Structure
  property_count: 2
  slug: minecraft-services-friend-structure
- name: Minecraft Services Friend Update Request Structure
  property_count: 3
  slug: minecraft-services-friend-update-request-structure
- name: Minecraft Services Friends List Structure
  property_count: 4
  slug: minecraft-services-friends-list-structure
- name: Minecraft Services Friends Preferences Structure
  property_count: 1
  slug: minecraft-services-friends-preferences-structure
- name: Minecraft Services Minecraft Access Token Structure
  property_count: 5
  slug: minecraft-services-minecraft-access-token-structure
- name: Minecraft Services Name Availability Structure
  property_count: 1
  slug: minecraft-services-name-availability-structure
- name: Minecraft Services Name Change Info Structure
  property_count: 3
  slug: minecraft-services-name-change-info-structure
- name: Minecraft Services Player Attributes Structure
  property_count: 4
  slug: minecraft-services-player-attributes-structure
- name: Minecraft Services Player Attributes Update Structure
  property_count: 2
  slug: minecraft-services-player-attributes-update-structure
- name: Minecraft Services Player Certificates Structure
  property_count: 5
  slug: minecraft-services-player-certificates-structure
- name: Minecraft Services Presence Entry Structure
  property_count: 3
  slug: minecraft-services-presence-entry-structure
- name: Minecraft Services Presence Report Structure
  property_count: 2
  slug: minecraft-services-presence-report-structure
- name: Minecraft Services Privilege Map Structure
  property_count: 4
  slug: minecraft-services-privilege-map-structure
- name: Minecraft Services Profanity Filter Preferences Structure
  property_count: 1
  slug: minecraft-services-profanity-filter-preferences-structure
- name: Minecraft Services Profile Structure
  property_count: 2
  slug: minecraft-services-profile-structure
- name: Minecraft Services Public Key Entry Structure
  property_count: 1
  slug: minecraft-services-public-key-entry-structure
- name: Minecraft Services Public Keys Structure
  property_count: 3
  slug: minecraft-services-public-keys-structure
- name: Minecraft Services Skin Structure
  property_count: 6
  slug: minecraft-services-skin-structure
- name: Minecraft Services Xbox Login Request Structure
  property_count: 2
  slug: minecraft-services-xbox-login-request-structure
- name: Public Api Name Change Structure
  property_count: 2
  slug: public-api-name-change-structure
- name: Public Api Profile Structure
  property_count: 4
  slug: public-api-profile-structure
- name: Public Api Sale Statistics Request Structure
  property_count: 1
  slug: public-api-sale-statistics-request-structure
- name: Public Api Sale Statistics Structure
  property_count: 3
  slug: public-api-sale-statistics-structure
- name: Session Server Join Request Structure
  property_count: 3
  slug: session-server-join-request-structure
- name: Session Server Session Profile Structure
  property_count: 4
  slug: session-server-session-profile-structure
- name: Session Server Session Property Structure
  property_count: 3
  slug: session-server-session-property-structure
jsonld:
- class_count: 0
  name: Mojang Api Context
  property_count: 0
  slug: mojang-api-context
- class_count: 32
  name: Mojang Minecraft Services Context
  property_count: 55
  slug: mojang-minecraft-services-context
- class_count: 5
  name: Mojang Public Api Context
  property_count: 8
  slug: mojang-public-api-context
- class_count: 4
  name: Mojang Session Server Context
  property_count: 8
  slug: mojang-session-server-context
layout: provider
modified: '2026-05-30'
name: Mojang
nav: Providers
network: true
overview: 'Mojang publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Attributes API, Authentication API, Blocklist API, and 11 more. Tagged areas include Games And Comics, Minecraft, Gaming, Identity, and Player Profiles.


  The Mojang catalog on APIs.io includes 4 JSON-LD contexts and 2 Spectral governance rulesets.


  Mojang''s developer surface includes authentication, documentation, and 16 more developer resources.'
random_paper: 66
rate_limits:
- limit_count: 6
  name: Mojang Rate Limits
  slug: mojang-rate-limits
rules:
- name: Mojang API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: mojang-jsonschema-spectral-rules
- name: Mojang API Rules
  rule_count: 48
  severity_counts:
    error: 12
    hint: 0
    info: 12
    warn: 24
  slug: mojang-spectral-rules
score:
  band: thin
  composite: 31.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 24.4
    developer_ergonomics: 19.6
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 31.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 14
      marker_coverage: 100.0
      total: 14
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mojang/refs/heads/main/screenshots/mojang-2026-06-20T185707.png
security:
- kind: authentication
  name: Mojang Authentication
  slug: mojang-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mojang Domain Security
  slug: mojang-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: mojang
tags:
- Games And Comics
- Minecraft
- Gaming
- Identity
- Player Profiles
- Session
- Public APIs
website: https://www.minecraft.net
---

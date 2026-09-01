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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Blizzard Entertainment Agentic Access
  operation_count: 26
  slug: blizzard-entertainment-agentic-access
  summary_line: 26 operations · 2 acting
api_count: 5
apis:
- description: Retrieve achievement reference data.
  name: Blizzard Entertainment Achievements API
  slug: blizzard-entertainment-achievements-api
- description: Retrieve Diablo III act reference data.
  name: Blizzard Entertainment Acts API
  slug: blizzard-entertainment-acts-api
- description: Retrieve artisan and recipe reference data.
  name: Blizzard Entertainment Artisans API
  slug: blizzard-entertainment-artisans-api
- description: Retrieve live auction-house listings per connected realm.
  name: Blizzard Entertainment Auctions API
  slug: blizzard-entertainment-auctions-api
- description: User-context authorization endpoints.
  name: Blizzard Entertainment Authorization API
  slug: blizzard-entertainment-authorization-api
- description: Retrieve Hearthstone card-back data.
  name: Blizzard Entertainment Card Backs API
  slug: blizzard-entertainment-card-backs-api
- description: Search and retrieve Hearthstone cards.
  name: Blizzard Entertainment Cards API
  slug: blizzard-entertainment-cards-api
- description: Retrieve character class and skill reference data.
  name: Blizzard Entertainment Characters API
  slug: blizzard-entertainment-characters-api
- description: Decode Hearthstone deck codes.
  name: Blizzard Entertainment Decks API
  slug: blizzard-entertainment-decks-api
- description: Retrieve guild profile data.
  name: Blizzard Entertainment Guilds API
  slug: blizzard-entertainment-guilds-api
- description: Retrieve item type and item reference data.
  name: Blizzard Entertainment Items API
  slug: blizzard-entertainment-items-api
- description: Retrieve ladder, grandmaster, and season data.
  name: Blizzard Entertainment Ladders API
  slug: blizzard-entertainment-ladders-api
- description: Retrieve Hearthstone metadata reference data.
  name: Blizzard Entertainment Metadata API
  slug: blizzard-entertainment-metadata-api
- description: Retrieve mount index and detail data.
  name: Blizzard Entertainment Mounts API
  slug: blizzard-entertainment-mounts-api
- description: Retrieve player career and hero profile data.
  name: Blizzard Entertainment Profiles API
  slug: blizzard-entertainment-profiles-api
- description: Retrieve realm and connected-realm reference data.
  name: Blizzard Entertainment Realms API
  slug: blizzard-entertainment-realms-api
- description: Token issuance and inspection endpoints.
  name: Blizzard Entertainment Token API
  slug: blizzard-entertainment-token-api
- description: OpenID Connect userinfo endpoint.
  name: Blizzard Entertainment UserInfo API
  slug: blizzard-entertainment-userinfo-api
artifact_total: 64
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Diablo III Community API
  slug: open-blizzard-diablo-iii
- collection_type: open
  name: Diablo III Community Achievements API
  slug: open-blizzard-entertainment-achievements-api
- collection_type: open
  name: Diablo III Community Achievements Acts API
  slug: open-blizzard-entertainment-acts-api
- collection_type: open
  name: Diablo III Community Achievements Artisans API
  slug: open-blizzard-entertainment-artisans-api
- collection_type: open
  name: Diablo III Community Achievements Auctions API
  slug: open-blizzard-entertainment-auctions-api
- collection_type: open
  name: Diablo III Community Achievements Authorization API
  slug: open-blizzard-entertainment-authorization-api
- collection_type: open
  name: Diablo III Community Achievements Card Backs API
  slug: open-blizzard-entertainment-card-backs-api
- collection_type: open
  name: Diablo III Community Achievements Cards API
  slug: open-blizzard-entertainment-cards-api
- collection_type: open
  name: Diablo III Community Achievements Characters API
  slug: open-blizzard-entertainment-characters-api
- collection_type: open
  name: Diablo III Community Achievements Decks API
  slug: open-blizzard-entertainment-decks-api
- collection_type: open
  name: Diablo III Community Achievements Guilds API
  slug: open-blizzard-entertainment-guilds-api
- collection_type: open
  name: Diablo III Community Achievements Items API
  slug: open-blizzard-entertainment-items-api
- collection_type: open
  name: Diablo III Community Achievements Ladders API
  slug: open-blizzard-entertainment-ladders-api
- collection_type: open
  name: Diablo III Community Achievements Metadata API
  slug: open-blizzard-entertainment-metadata-api
- collection_type: open
  name: Diablo III Community Achievements Mounts API
  slug: open-blizzard-entertainment-mounts-api
- collection_type: open
  name: Diablo III Community Achievements Profiles API
  slug: open-blizzard-entertainment-profiles-api
- collection_type: open
  name: Diablo III Community Achievements Realms API
  slug: open-blizzard-entertainment-realms-api
- collection_type: open
  name: Diablo III Community Achievements Token API
  slug: open-blizzard-entertainment-token-api
- collection_type: open
  name: Diablo III Community Achievements UserInfo API
  slug: open-blizzard-entertainment-userinfo-api
- collection_type: open
  name: Hearthstone Game Data API
  slug: open-blizzard-hearthstone
- collection_type: open
  name: Battle.net OAuth API
  slug: open-blizzard-oauth
- collection_type: open
  name: StarCraft II Community API
  slug: open-blizzard-starcraft-ii
- collection_type: open
  name: World of Warcraft Game Data API
  slug: open-blizzard-world-of-warcraft
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/blizzard-entertainment-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blizzard-entertainment-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/blizzard-entertainment-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Blizzard
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/blizzard-entertainment
- group: company
  title: ''
  type: Website
  url: https://www.blizzard.com/
- group: start
  title: ''
  type: Portal
  url: https://develop.battle.net/
- group: docs
  title: ''
  type: Documentation
  url: https://develop.battle.net/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://develop.battle.net/documentation/guides/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://develop.battle.net/documentation/guides/using-oauth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blizzard.com/legal/8b946525-de01-481a-9f4f-89af2c4f5d29/blizzard-end-user-license-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blizzard.com/legal/fba4d00f-c7e4-4883-b8b9-1b4500a402ea/blizzard-entertainment-privacy-notice
- group: operate
  title: ''
  type: Forums
  url: https://us.forums.blizzard.com/en/blizzard/c/api-discussion/18
- group: design
  title: ''
  type: SpectralRules
  url: rules/blizzard-entertainment-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/blizzard-entertainment-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/blizzard-entertainment-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/blizzard-entertainment-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/blizzard-entertainment-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/blizzard-entertainment-finops.yml
- group: auth
  title: ''
  type: Compliance
  url: ''
created: '2026-05-05'
description: Blizzard Entertainment is an American video game developer and publisher and a subsidiary of Activision Blizzard. Blizzard exposes a Battle.net Developer Portal that provides public OAuth 2.0 protected APIs returning game data and player profile data for its major franchises including World of Warcraft, Diablo III, StarCraft II, and Hearthstone.
features:
- description: Single platform exposes Game Data and Community APIs for World of Warcraft, Diablo III, StarCraft II, and Hearthstone
  name: Multi-Game Coverage
- description: Client credentials flow for public game data and authorization code flow for player-profile data
  name: OAuth 2.0 Authentication
- description: Independent regional endpoints for US, EU, KR, TW, and CN with locale-aware responses
  name: Regional API Hosts
- description: OpenID Connect compatible login that lets third-party apps authenticate Battle.net users
  name: Battle.net Account Login
- description: Game Data APIs are partitioned by namespace (static-, dynamic-, profile-) to separate patch-stable reference data from live state
  name: Static and Dynamic Namespaces
- description: Endpoint exposing live World of Warcraft auction house listings per connected realm
  name: Auction House Data
finops:
- name: Blizzard Entertainment Finops
  service_category: API
  slug: blizzard-entertainment-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blizzard-entertainment.png
integrations:
- description: Battle.net account linking is widely combined with Discord OAuth for community gating
  name: Discord
- description: Companion overlays and stream tools surface live ladder and profile data
  name: Twitch
- description: Community service that aggregates WoW profile and mythic-plus data via the Game Data API
  name: Raider.IO
jsonld:
- class_count: 38
  name: Blizzard Entertainment Context
  property_count: 9
  slug: blizzard-entertainment-context
layout: provider
modified: '2026-05-19'
name: Blizzard Entertainment
nav: Providers
network: true
overview: 'Blizzard Entertainment publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Achievements API, Acts API, Artisans API, and 15 more. Tagged areas include Games, Entertainment, Video Games, Game Data, and Battle.net.


  The Blizzard Entertainment catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Blizzard Entertainment''s developer surface includes authentication, developer portal, documentation, getting-started guide, and 15 more developer resources.'
plans:
- name: Blizzard Entertainment Plans Pricing
  plan_count: 2
  slug: blizzard-entertainment-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Blizzard Entertainment Rate Limits
  slug: blizzard-entertainment-rate-limits
rules:
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Blizzard Entertainment API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: blizzard-entertainment-rules
score:
  band: developing
  composite: 47.4
  coverage:
    artifact_dirs: 13
    catalog_gap: 24.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 60.6
    contract_quality: 59.4
    developer_ergonomics: 14.3
    discoverability: 74.1
    governance: 60.6
    operational_transparency: 34.2
  previous_composite: 47.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blizzard-entertainment/refs/heads/main/screenshots/blizzard-entertainment-2026-06-20T173354.png
security:
- kind: authentication
  name: Blizzard Entertainment Authentication
  slug: blizzard-entertainment-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Blizzard Entertainment Domain Security
  slug: blizzard-entertainment-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blizzard-entertainment
tags:
- Games
- Entertainment
- Video Games
- Game Data
- Battle.net
use_cases:
- description: Build mobile and web companion apps that surface character, guild, ladder, and profile data
  name: Companion Apps
- description: Power character optimizer, mythic-plus rank tracker, and deck-tracker sites with first-party data
  name: Theorycrafting and Stats Sites
- description: Pull ladder and seasonal data for esports brackets, statistics, and broadcast overlays
  name: Esports Tooling
- description: Provide authoritative reference data to community add-on libraries and mod managers
  name: Add-on and Mod Ecosystems
- description: Let players authenticate with their Battle.net account in third-party communities and tournament platforms
  name: Account Linking
website: https://www.blizzard.com/
---

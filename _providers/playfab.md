---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: derived
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Playfab Agentic Access
  operation_count: 13
  slug: playfab-agentic-access
  summary_line: 13 operations · 13 acting
api_count: 18
apis:
- baseURL: https://titleId.playfabapi.com/Client
  baseurl_source: declared
  description: The PlayFab Client API is the player-facing REST surface used by game clients for login, account linking, virtual currency, inventory, friends, leaderboards, statistics, player data, cloud script exec
  name: PlayFab Client API
  slug: playfab-client-api
- baseURL: https://titleId.playfabapi.com/Server
  baseurl_source: declared
  description: The PlayFab Server API is the server-trusted REST surface for custom game servers and trusted backends. It mirrors much of the Client API but operates with the title's developer secret key and can act
  name: PlayFab Server API
  slug: playfab-server-api
- baseURL: https://titleId.playfabapi.com/Admin
  baseurl_source: declared
  description: The PlayFab Admin API is the privileged REST surface for studio and ops tooling. It covers title configuration, virtual currency catalogs, catalog items, store configuration, content (CDN) uploads, se
  name: PlayFab Admin API
  slug: playfab-admin-api
- baseURL: https://titleId.playfabapi.com/Authentication
  baseurl_source: declared
  description: The PlayFab Authentication API issues and validates entity tokens used by the Entity Programming Model that underlies CloudScript using Azure Functions, Groups, Data, Profiles, Events, and Multiplayer
  name: PlayFab Authentication API
  slug: playfab-entity-authentication-api
- baseURL: https://titleId.playfabapi.com/CloudScript
  baseurl_source: declared
  description: PlayFab CloudScript runs server-authoritative game logic in PlayFab. Modern CloudScript using Azure Functions registers Azure Function endpoints that can be invoked from clients or servers via Execute
  name: PlayFab CloudScript API
  slug: playfab-cloudscript-api
- baseURL: https://titleId.playfabapi.com/Multiplayer
  baseurl_source: declared
  description: The PlayFab Multiplayer API powers PlayFab Multiplayer Servers (managed game server hosting on Azure), Party (low-latency voice and data networking), Lobby, and matchmaking server build management.
  name: PlayFab Multiplayer API
  slug: playfab-multiplayer-api
- description: The PlayFab Matchmaking API exposes ticket-based matchmaking, queue management, match results, and matchmaking rule configuration on top of PlayFab Multiplayer.
  name: PlayFab Matchmaking API
  slug: playfab-matchmaking-api
- baseURL: https://titleId.playfabapi.com/Catalog
  baseurl_source: declared
  description: 'PlayFab Economy v2 is the modern catalog, inventory, store, and virtual-currency surface. It covers catalog item authoring, inventory transactions, transactional and subscription stores, item search, '
  name: PlayFab Economy (Catalog / Inventory) API
  slug: playfab-economy-api
- baseURL: https://titleId.playfabapi.com/File
  baseurl_source: declared
  description: The PlayFab Data API stores arbitrary file and object data attached to any entity (player, title, character, group). It exposes GetFiles, GetObjects, InitiateFileUploads, AbortFileUploads, FinalizeFil
  name: PlayFab Data API
  slug: playfab-data-api
- baseURL: https://titleId.playfabapi.com/Group
  baseurl_source: declared
  description: The PlayFab Groups API supports guilds, clans, parties, and other player-managed organizations on the Entity model with roles, memberships, applications, and invitations.
  name: PlayFab Groups API
  slug: playfab-groups-api
- baseURL: https://titleId.playfabapi.com/Profile
  baseurl_source: declared
  description: The PlayFab Profiles API reads and writes Entity Profiles, including display name, language, lineage, and per-entity policies (ACLs) used across the Entity-model APIs.
  name: PlayFab Profiles API
  slug: playfab-profiles-api
- baseURL: https://titleId.playfabapi.com/Event
  baseurl_source: declared
  description: The PlayFab Events API writes PlayStream and custom telemetry events into PlayFab's pipeline for downstream segmentation, rules, and Insights analytics.
  name: PlayFab Events API
  slug: playfab-events-api
- baseURL: https://insights.playfab.com
  baseurl_source: declared
  description: PlayFab Insights is the managed analytics surface (built on Azure Data Explorer / Kusto) for querying telemetry generated by PlayFab titles. The Insights API manages Insights performance levels and su
  name: PlayFab Insights API
  slug: playfab-insights-api
- baseURL: https://titleId.playfabapi.com/Locale
  baseurl_source: declared
  description: The PlayFab Localization API returns the set of languages supported by the title and is used by clients to negotiate locale.
  name: PlayFab Localization API
  slug: playfab-localization-api
- baseURL: https://titleId.playfabapi.com
  baseurl_source: declared
  description: The PlayFab Add-on API for configuring third-party marketplace and platform integrations (Apple, Google, Steam, Facebook, PlayStation, Nintendo, Twitch, Kongregate) on a PlayFab title.
  name: PlayFab Addon API
  slug: playfab-addon-api
- baseURL: https://titleId.playfabapi.com
  baseurl_source: declared
  description: The PlayFab Experimentation API for creating, running and analysing A/B experiments and exclusion groups on a PlayFab title.
  name: PlayFab Experimentation API
  slug: playfab-experimentation-api
- baseURL: https://titleId.playfabapi.com
  baseurl_source: declared
  description: The PlayFab Leaderboards API (entity leaderboards and statistics v2) for defining leaderboards, updating entity statistics and reading ranked results.
  name: PlayFab Leaderboards API
  slug: playfab-leaderboards-api
- baseURL: https://titleId.playfabapi.com
  baseurl_source: declared
  description: The PlayFab Progression API for entity statistic definitions, leaderboard definitions and entity progression data.
  name: PlayFab Progression API
  slug: playfab-progression-api
- baseURL: https://titleId.playfabapi.com/Client
  baseurl_source: declared
  description: PlayFab account metadata.
  name: PlayFab Account API
  slug: playfab-account-api
- baseURL: https://titleId.playfabapi.com/Client
  baseurl_source: declared
  description: Login, registration, and identity provider sign-in.
  name: PlayFab Authentication API
  slug: playfab-authentication-api
artifact_total: 35
collections:
- collection_type: open
  name: PlayFab Client Account API
  slug: open-playfab-account-api
- collection_type: open
  name: PlayFab Client Account Authentication API
  slug: open-playfab-authentication-api
- collection_type: open
  name: PlayFab Client API
  slug: open-playfab
common:
- group: agent
  href: https://artifacts.apis.io/playfab/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/playfab/conventions/playfab-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/playfab-conventions.yml
- group: design
  href: https://artifacts.apis.io/playfab/conventions/playfab-conventions.yml
  title: ''
  type: Conventions
  url: conventions/playfab-conventions.yml
- group: design
  href: https://artifacts.apis.io/playfab/rules/playfab-rules.yml
  title: ''
  type: Spectral
  url: rules/playfab-rules.yml
- group: design
  href: https://artifacts.apis.io/playfab/json-ld/playfab-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/playfab-context.jsonld
- group: design
  href: https://artifacts.apis.io/playfab/vocabulary/playfab-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/playfab-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/playfab/data-model/playfab-data-model.yml
  title: ''
  type: DataModel
  url: data-model/playfab-data-model.yml
- group: design
  href: https://artifacts.apis.io/playfab/lifecycle/playfab-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/playfab-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/playfab/errors/playfab-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/playfab-problem-types.yml
- group: design
  href: https://artifacts.apis.io/playfab/conformance/playfab-conformance.yml
  title: ''
  type: Conformance
  url: conformance/playfab-conformance.yml
- group: auth
  href: https://artifacts.apis.io/playfab/well-known/playfab-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/playfab-www-security.txt
- group: auth
  href: https://artifacts.apis.io/playfab/well-known/playfab-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/playfab-status-security.txt
- group: agent
  href: https://artifacts.apis.io/playfab/well-known/playfab-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/playfab-well-known.yml
- group: other
  href: https://artifacts.apis.io/playfab/hosts/playfab-hosts.yml
  title: ''
  type: Hosts
  url: hosts/playfab-hosts.yml
- group: other
  href: https://artifacts.apis.io/playfab/vendors/playfab-vendors.yml
  title: ''
  type: Vendors
  url: vendors/playfab-vendors.yml
- group: build
  href: https://artifacts.apis.io/playfab/packages/playfab-packages.yml
  title: ''
  type: Packages
  url: packages/playfab-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.playfab.com/
- group: commercial
  href: https://artifacts.apis.io/playfab/plans/playfab-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/playfab-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/playfab/rate-limits/playfab-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/playfab-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/playfab/finops/playfab-finops.yml
  title: ''
  type: FinOps
  url: finops/playfab-finops.yml
- group: agent
  href: https://artifacts.apis.io/playfab/agentic-access/playfab-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/playfab-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/playfab/security/playfab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/playfab-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/playfab/authentication/playfab-authentication.yml
  title: ''
  type: Authentication
  url: authentication/playfab-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://playfab.com
- group: start
  title: ''
  type: Portal
  url: https://developer.playfab.com
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/gaming/playfab/
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/rest/api/playfab/
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/gaming/playfab/sdks/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/gaming/playfab/personas/developer
- group: commercial
  title: ''
  type: Pricing
  url: https://learn.microsoft.com/en-us/gaming/playfab/features/pricing/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://learn.microsoft.com/en-us/gaming/playfab/personas/release-notes
- group: operate
  title: ''
  type: Status
  url: https://status.playfab.com
- group: operate
  title: ''
  type: Forums
  url: https://community.playfab.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PlayFab
- group: company
  title: ''
  type: Blog
  url: https://blog.playfab.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/servicesagreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: other
  title: ''
  type: X
  url: https://x.com/AzurePlayFab
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoft-azure
- group: other
  href: https://artifacts.apis.io/playfab/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2024-01-01'
description: PlayFab is Microsoft Azure's backend-as-a-service for live games. PlayFab exposes a large REST API surface (Client, Server, Admin, Authentication, CloudScript, Multiplayer, Economy v2, Matchmaking, Insights, Groups, Data, Profiles, Events, Localization) plus first-party SDKs for Unity, Unreal, Cocos, Phaser, JavaScript, C++, C#, Java, Lua, Objective-C, and Python. Every PlayFab game (a "title") gets its own scoped subdomain at https://[titleId].playfabapi.com. Sessions, identity, progression, inventory, leaderboards, segmentation, A/B testing, push, scheduled tasks, CloudScript (Azure Functions), and PlayFab Multiplayer Servers all run on this surface. PlayFab is operated as part of Azure Gaming and the documentation lives at learn.microsoft.com/en-us/gaming/playfab.
finops:
- has_sources: false
  method: generated
  name: Playfab Finops
  primary_unit: ''
  service_category: API
  slug: playfab-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/playfab.png
json_schemas:
- name: GetPlayerCombinedInfoRequestParams
  property_count: 10
  slug: playfab-get-player-combined-info-request-params
- name: LoginResultEnvelope
  property_count: 3
  slug: playfab-login-result-envelope
jsonld:
- class_count: 120
  name: Playfab Context
  property_count: 184
  slug: playfab-context
layout: provider
modified: '2026-11-05'
name: PlayFab
nav: Providers
network: true
overview: 'PlayFab publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including Client API, Server API, Admin API, and 17 more. Tagged areas include Authentication, Microsoft Azure, Backend, Backend-as-a-Service, and CloudScript.


  The PlayFab catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  PlayFab''s developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, pricing, release notes, and 33 more developer resources.'
plans:
- name: Playfab Plans Pricing
  plan_count: 1
  slug: playfab-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Playfab Rate Limits
  slug: playfab-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: PlayFab API Rules
  rule_count: 59
  severity_counts:
    error: 44
    hint: 0
    info: 3
    warn: 12
  slug: playfab-rules
score:
  band: developing
  composite: 51.8
  coverage:
    artifact_dirs: 30
    catalog_earned: 69.8
    catalog_earned_first_party: 0.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 10.1
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 62.3
    developer_ergonomics: 54.2
    discoverability: 78.6
    operational_transparency: 52.6
  previous_composite: 41.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/playfab/playfab-2026-06-20T191806.png
security:
- kind: authentication
  name: Playfab Authentication
  slug: playfab-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Playfab Domain Security
  slug: playfab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: playfab-inventory-economy
  slug: playfab-inventory-economy
- name: playfab-player-login-and-data
  slug: playfab-player-login-and-data
slug: playfab
tags:
- Authentication
- Microsoft Azure
- Backend
- Backend-as-a-Service
- CloudScript
- Economy
- Game Backend
- Game Development
- Games
- Leaderboards
- Matchmaking
- Microsoft
- Multiplayer
- PlayFab
- REST
website: https://playfab.com
---

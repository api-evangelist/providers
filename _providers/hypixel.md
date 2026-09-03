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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Hypixel Agentic Access
  operation_count: 68
  slug: hypixel-agentic-access
  summary_line: 68 operations
api_count: 2
apis:
- baseURL: https://api.hypixel.net/v2
  baseurl_source: declared
  description: Hypixel Housing — active public houses, per-player public houses, and per-house information.
  name: Hypixel Housing API
  slug: hypixel-housing-api
- baseURL: https://api.hypixel.net/v2
  baseurl_source: declared
  description: Network-wide telemetry — boosters, counts, leaderboards, punishment statistics.
  name: Hypixel Other API
  slug: hypixel-other-api
- baseURL: https://api.hypixel.net/v2
  baseurl_source: declared
  description: Hypixel network player profiles, recent games, online status, friends, and guild lookups.
  name: Hypixel Player Data API
  slug: hypixel-player-data-api
- baseURL: https://api.hypixel.net/v2
  baseurl_source: declared
  description: Static reference data — games, achievements, challenges, quests, guild achievements, vanity pets and companions.
  name: Hypixel Resources API
  slug: hypixel-resources-api
- baseURL: https://api.hypixel.net/v2
  baseurl_source: declared
  description: Hypixel SkyBlock — auctions, bazaar, profiles, museum, garden, bingo, fire sales, and SkyBlock-specific reference data.
  name: Hypixel SkyBlock API
  slug: hypixel-skyblock-api
artifact_total: 53
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hypixel Public Housing API
  slug: open-hypixel-housing-api
- collection_type: open
  name: Hypixel Public Housing Other API
  slug: open-hypixel-other-api
- collection_type: open
  name: Hypixel Public Housing Player Data API
  slug: open-hypixel-player-data-api
- collection_type: open
  name: Hypixel Public API
  slug: open-hypixel-public-api
- collection_type: open
  name: Hypixel Public Housing Resources API
  slug: open-hypixel-resources-api
- collection_type: open
  name: Hypixel Public Housing SkyBlock API
  slug: open-hypixel-skyblock-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/HypixelDev/PublicAPI/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/HypixelDev/PublicAPI/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/HypixelDev/PublicAPI/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hypixel-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hypixel-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hypixel-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hypixel-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://hypixel.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.hypixel.net/
- group: operate
  title: ''
  type: ApiHelpForum
  url: https://hypixel.net/forums/api-help.111/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hypixel.net/tos
- group: other
  title: ''
  type: Policies
  url: https://developer.hypixel.net/policies
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HypixelDev
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/HypixelDev/PublicAPI
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: commercial
  title: ''
  type: Plans
  url: plans/hypixel-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hypixel-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hypixel-finops.yml
- group: design
  title: ''
  type: Spectral
  url: rules/hypixel-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/hypixel-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hypixel-public-api-context.jsonld
created: '2026-05-28'
description: Hypixel Public API — the official REST API of the Hypixel Minecraft server network, the largest Minecraft minigame server. The API exposes player profiles and stats, guilds, friends, recent games, online status, server-wide counts, network boosters, punishment statistics, leaderboards, housing, and the full SkyBlock economy (auctions, bazaar, profiles, museum, garden, bingo, fire sales). All endpoints are read-only HTTP GET requests returning JSON, authenticated with a per-application API key issued via the Hypixel Developer Dashboard.
examples:
- key_count: 7
  name: Hypixel Public Api Booster Example
  slug: hypixel-public-api-booster-example
- key_count: 6
  name: Hypixel Public Api Game Example
  slug: hypixel-public-api-game-example
- key_count: 6
  name: Hypixel Public Api Housing House Example
  slug: hypixel-public-api-housing-house-example
- key_count: 18
  name: Hypixel Public Api Sky Block Auction Example
  slug: hypixel-public-api-sky-block-auction-example
- key_count: 5
  name: Hypixel Public Api Sky Block Fire Sale Example
  slug: hypixel-public-api-sky-block-fire-sale-example
- key_count: 10
  name: Hypixel Public Api Sky Block Garden Example
  slug: hypixel-public-api-sky-block-garden-example
- key_count: 6
  name: Hypixel Public Api Sky Block Item Example
  slug: hypixel-public-api-sky-block-item-example
- key_count: 4
  name: Hypixel Public Api Sky Block Museum Example
  slug: hypixel-public-api-sky-block-museum-example
- key_count: 7
  name: Hypixel Public Api Sky Block Profile Example
  slug: hypixel-public-api-sky-block-profile-example
finops:
- name: Hypixel Finops
  service_category: Gaming Network API
  slug: hypixel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hypixel.png
json_schemas:
- name: ActiveBooster
  property_count: 0
  slug: hypixel-public-api-active-booster
- name: Booster
  property_count: 7
  slug: hypixel-public-api-booster
- name: Game
  property_count: 6
  slug: hypixel-public-api-game
- name: HousingHouse
  property_count: 6
  slug: hypixel-public-api-housing-house
- name: QueuedBooster
  property_count: 0
  slug: hypixel-public-api-queued-booster
- name: SkyBlockAuction
  property_count: 18
  slug: hypixel-public-api-sky-block-auction
- name: SkyBlockFireSale
  property_count: 5
  slug: hypixel-public-api-sky-block-fire-sale
- name: SkyBlockGarden
  property_count: 10
  slug: hypixel-public-api-sky-block-garden
- name: SkyBlockItem
  property_count: 6
  slug: hypixel-public-api-sky-block-item
- name: SkyBlockMuseum
  property_count: 4
  slug: hypixel-public-api-sky-block-museum
- name: SkyBlockProfile
  property_count: 7
  slug: hypixel-public-api-sky-block-profile
json_structures:
- name: Hypixel Public Api Active Booster Structure
  property_count: 0
  slug: hypixel-public-api-active-booster-structure
- name: Hypixel Public Api Booster Structure
  property_count: 7
  slug: hypixel-public-api-booster-structure
- name: Hypixel Public Api Game Structure
  property_count: 6
  slug: hypixel-public-api-game-structure
- name: Hypixel Public Api Housing House Structure
  property_count: 6
  slug: hypixel-public-api-housing-house-structure
- name: Hypixel Public Api Queued Booster Structure
  property_count: 0
  slug: hypixel-public-api-queued-booster-structure
- name: Hypixel Public Api Sky Block Auction Structure
  property_count: 18
  slug: hypixel-public-api-sky-block-auction-structure
- name: Hypixel Public Api Sky Block Fire Sale Structure
  property_count: 5
  slug: hypixel-public-api-sky-block-fire-sale-structure
- name: Hypixel Public Api Sky Block Garden Structure
  property_count: 10
  slug: hypixel-public-api-sky-block-garden-structure
- name: Hypixel Public Api Sky Block Item Structure
  property_count: 6
  slug: hypixel-public-api-sky-block-item-structure
- name: Hypixel Public Api Sky Block Museum Structure
  property_count: 4
  slug: hypixel-public-api-sky-block-museum-structure
- name: Hypixel Public Api Sky Block Profile Structure
  property_count: 7
  slug: hypixel-public-api-sky-block-profile-structure
jsonld:
- class_count: 11
  name: Hypixel Public Api Context
  property_count: 74
  slug: hypixel-public-api-context
layout: provider
modified: '2026-05-30'
name: Hypixel
nav: Providers
network: true
overview: 'Hypixel publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Housing API, Other API, Player Data API, and 2 more. Tagged areas include Games And Comics, Gaming, Minecraft, Player Stats, and Leaderboards.


  The Hypixel catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Hypixel''s developer surface includes authentication and 20 more developer resources.'
plans:
- name: Hypixel Plans Pricing
  plan_count: 2
  slug: hypixel-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Hypixel Rate Limits
  slug: hypixel-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Hypixel API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: hypixel-jsonschema-spectral-rules
- effective_rule_count: 81
  extends:
  - spectral:oas
  name: Hypixel API Rules
  rule_count: 40
  severity_counts:
    error: 16
    hint: 0
    info: 6
    warn: 18
  slug: hypixel-spectral-rules
score:
  band: developing
  composite: 47.7
  coverage:
    artifact_dirs: 15
    catalog_gap: 34.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 28.8
    contract_quality: 68.6
    developer_ergonomics: 38.1
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 50.0
  open_source:
    applies: true
    score: 25.0
  previous_composite: 47.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hypixel/refs/heads/main/screenshots/hypixel-2026-07-25T221929.png
security:
- kind: authentication
  name: Hypixel Authentication
  slug: hypixel-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Hypixel Domain Security
  slug: hypixel-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Hypixel Vulnerability Disclosure
  slug: hypixel-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: hypixel
tags:
- Games And Comics
- Gaming
- Minecraft
- Player Stats
- Leaderboards
- SkyBlock
- Public APIs
website: https://hypixel.net/
---

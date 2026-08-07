---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
  name: Activision Blizzard Agentic Access
  operation_count: 17
  slug: activision-blizzard-agentic-access
  summary_line: 17 operations
api_count: 5
apis:
- description: Battle.net account and user profile APIs
  name: activision-blizzard Account API
  slug: activision-blizzard-account-api
- description: Diablo III game data and profile APIs
  name: activision-blizzard Diablo III API
  slug: activision-blizzard-diablo-iii-api
- description: Hearthstone game data APIs
  name: activision-blizzard Hearthstone API
  slug: activision-blizzard-hearthstone-api
- description: StarCraft II game data and profile APIs
  name: activision-blizzard StarCraft II API
  slug: activision-blizzard-starcraft-ii-api
- description: World of Warcraft game data and profile APIs
  name: activision-blizzard World of Warcraft API
  slug: activision-blizzard-world-of-warcraft-api
artifact_total: 68
collections:
- collection_type: open
  name: Activision Blizzard Battle.net API
  slug: open-activision-blizzard-battle-net
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/activision-blizzard-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/activision-blizzard-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/activision-blizzard-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/activision-blizzard-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/activision-blizzard
- group: company
  title: ''
  type: Website
  url: https://www.activision-blizzard.com
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
  type: Pricing
  url: https://develop.battle.net/documentation/guides/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Blizzard
- group: design
  title: ''
  type: SpectralRules
  url: rules/activision-blizzard-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/activision-blizzard-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/activision-blizzard-context.jsonld
description: Activision Blizzard is a global video game developer and publisher producing franchises including Call of Duty, World of Warcraft, Diablo, Overwatch, and Candy Crush across console, PC, and mobile platforms.
examples:
- key_count: 3
  name: Activision Blizzard Battle Net Profile Example
  slug: activision-blizzard-battle-net-profile-example
- key_count: 8
  name: Activision Blizzard D3 Career Profile Example
  slug: activision-blizzard-d3-career-profile-example
- key_count: 13
  name: Activision Blizzard D3 Hero Example
  slug: activision-blizzard-d3-hero-example
- key_count: 7
  name: Activision Blizzard D3 Hero Summary Example
  slug: activision-blizzard-d3-hero-summary-example
- key_count: 18
  name: Activision Blizzard Hearthstone Card Example
  slug: activision-blizzard-hearthstone-card-example
- key_count: 4
  name: Activision Blizzard Hearthstone Cards Response Example
  slug: activision-blizzard-hearthstone-cards-response-example
- key_count: 8
  name: Activision Blizzard Hearthstone Deck Example
  slug: activision-blizzard-hearthstone-deck-example
- key_count: 2
  name: Activision Blizzard Sc2 Profile Example
  slug: activision-blizzard-sc2-profile-example
- key_count: 2
  name: Activision Blizzard Wo W Account Example
  slug: activision-blizzard-wo-w-account-example
- key_count: 3
  name: Activision Blizzard Wo W Character Achievements Example
  slug: activision-blizzard-wo-w-character-achievements-example
- key_count: 13
  name: Activision Blizzard Wo W Character Example
  slug: activision-blizzard-wo-w-character-example
- key_count: 10
  name: Activision Blizzard Wo W Character Summary Example
  slug: activision-blizzard-wo-w-character-summary-example
- key_count: 6
  name: Activision Blizzard Wo W Guild Example
  slug: activision-blizzard-wo-w-guild-example
- key_count: 9
  name: Activision Blizzard Wo W Item Example
  slug: activision-blizzard-wo-w-item-example
- key_count: 2
  name: Activision Blizzard Wo W Profile Summary Example
  slug: activision-blizzard-wo-w-profile-summary-example
- key_count: 9
  name: Activision Blizzard Wo W Realm Example
  slug: activision-blizzard-wo-w-realm-example
- key_count: 1
  name: Activision Blizzard Wo W Realms Index Example
  slug: activision-blizzard-wo-w-realms-index-example
finops:
- name: Activision Blizzard Finops
  service_category: Gaming / Game Data
  slug: activision-blizzard-finops
graphqls:
- description: This is a conceptual GraphQL schema for the Activision Blizzard / Battle.net platform. It is derived from the publicly documented Battle.net REST API (https://develop.battle.net/documentation) and cov
  name: Activision Blizzard GraphQL Schema
  slug: activision-blizzard-graphql
image: /assets/icons/activision-blizzard.png
json_schemas:
- name: BattleNetProfile
  property_count: 3
  slug: activision-blizzard-battle-net-profile
- name: D3CareerProfile
  property_count: 8
  slug: activision-blizzard-d3-career-profile
- name: D3Hero
  property_count: 13
  slug: activision-blizzard-d3-hero
- name: D3HeroSummary
  property_count: 7
  slug: activision-blizzard-d3-hero-summary
- name: HearthstoneCard
  property_count: 18
  slug: activision-blizzard-hearthstone-card
- name: HearthstoneCardsResponse
  property_count: 4
  slug: activision-blizzard-hearthstone-cards-response
- name: HearthstoneDeck
  property_count: 8
  slug: activision-blizzard-hearthstone-deck
- name: SC2Profile
  property_count: 2
  slug: activision-blizzard-sc2-profile
- name: WoWAccount
  property_count: 2
  slug: activision-blizzard-wo-w-account
- name: WoWCharacterAchievements
  property_count: 3
  slug: activision-blizzard-wo-w-character-achievements
- name: WoWCharacter
  property_count: 13
  slug: activision-blizzard-wo-w-character
- name: WoWCharacterSummary
  property_count: 10
  slug: activision-blizzard-wo-w-character-summary
- name: WoWGuild
  property_count: 6
  slug: activision-blizzard-wo-w-guild
- name: WoWItem
  property_count: 9
  slug: activision-blizzard-wo-w-item
- name: WoWProfileSummary
  property_count: 2
  slug: activision-blizzard-wo-w-profile-summary
- name: WoWRealm
  property_count: 9
  slug: activision-blizzard-wo-w-realm
- name: WoWRealmsIndex
  property_count: 1
  slug: activision-blizzard-wo-w-realms-index
json_structures:
- name: Activision Blizzard Battle Net Profile Structure
  property_count: 3
  slug: activision-blizzard-battle-net-profile-structure
- name: Activision Blizzard D3 Career Profile Structure
  property_count: 8
  slug: activision-blizzard-d3-career-profile-structure
- name: Activision Blizzard D3 Hero Structure
  property_count: 13
  slug: activision-blizzard-d3-hero-structure
- name: Activision Blizzard D3 Hero Summary Structure
  property_count: 7
  slug: activision-blizzard-d3-hero-summary-structure
- name: Activision Blizzard Hearthstone Card Structure
  property_count: 18
  slug: activision-blizzard-hearthstone-card-structure
- name: Activision Blizzard Hearthstone Cards Response Structure
  property_count: 4
  slug: activision-blizzard-hearthstone-cards-response-structure
- name: Activision Blizzard Hearthstone Deck Structure
  property_count: 8
  slug: activision-blizzard-hearthstone-deck-structure
- name: Activision Blizzard Sc2 Profile Structure
  property_count: 2
  slug: activision-blizzard-sc2-profile-structure
- name: Activision Blizzard Wo W Account Structure
  property_count: 2
  slug: activision-blizzard-wo-w-account-structure
- name: Activision Blizzard Wo W Character Achievements Structure
  property_count: 3
  slug: activision-blizzard-wo-w-character-achievements-structure
- name: Activision Blizzard Wo W Character Structure
  property_count: 13
  slug: activision-blizzard-wo-w-character-structure
- name: Activision Blizzard Wo W Character Summary Structure
  property_count: 10
  slug: activision-blizzard-wo-w-character-summary-structure
- name: Activision Blizzard Wo W Guild Structure
  property_count: 6
  slug: activision-blizzard-wo-w-guild-structure
- name: Activision Blizzard Wo W Item Structure
  property_count: 9
  slug: activision-blizzard-wo-w-item-structure
- name: Activision Blizzard Wo W Profile Summary Structure
  property_count: 2
  slug: activision-blizzard-wo-w-profile-summary-structure
- name: Activision Blizzard Wo W Realm Structure
  property_count: 9
  slug: activision-blizzard-wo-w-realm-structure
- name: Activision Blizzard Wo W Realms Index Structure
  property_count: 1
  slug: activision-blizzard-wo-w-realms-index-structure
jsonld:
- class_count: 17
  name: Activision Blizzard Context
  property_count: 79
  slug: activision-blizzard-context
layout: provider
modified: '2026-05-19'
name: activision-blizzard
nav: Providers
network: true
overview: 'activision-blizzard publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Account API, Diablo III API, Hearthstone API, and 2 more. Tagged areas include Fortune 1000.


  The activision-blizzard catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  activision-blizzard''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, and 10 more developer resources.'
plans:
- name: Activision Blizzard Plans Pricing
  plan_count: 2
  slug: activision-blizzard-plans-pricing
press:
- date: '2026-05-25'
  title: Microsoft to acquire Activision Blizzard to bring the joy and ...
  url: https://www.prnewswire.com/news-releases/microsoft-to-acquire-activision-blizzard-to-bring-the-joy-and-community-of-gaming-to-everyone-across-every-device-301462759.html
- date: '2026-05-25'
  title: 'Our vision for gaming: More choice and ...'
  url: https://news.microsoft.com/activision-blizzard-acquisition
- date: '2026-05-25'
  title: Mobile Game Developer King Acquires Artificial Intelligence ...
  url: https://investor.activision.com/news-releases/news-release-details/mobile-game-developer-king-acquires-artificial-intelligence
- date: '2026-05-25'
  title: Microsoft and Activision Blizzard - UR Scholarship Repository
  url: https://scholarship.richmond.edu/cgi/viewcontent.cgi?article=1022&context=robins-case-network
- date: '2026-05-25'
  title: Activision Blizzard and Google Enter Into Multi-year ...
  url: https://www.googlecloudpresscorner.com/2020-01-24-Activision-Blizzard-and-Google-Enter-Into-Multi-year-Strategic-Relationship-to-Power-New-Player-Experiences
random_paper: 71
rate_limits:
- limit_count: 2
  name: Activision Blizzard Rate Limits
  slug: activision-blizzard-rate-limits
rules:
- name: activision-blizzard API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: activision-blizzard-jsonschema-spectral-rules
- name: activision-blizzard API Rules
  rule_count: 28
  severity_counts:
    error: 9
    hint: 0
    info: 3
    warn: 16
  slug: activision-blizzard-spectral-rules
scopes:
- name: Activision Blizzard Scopes
  scope_count: 3
  slug: activision-blizzard-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 40.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 35.3
    developer_ergonomics: 39.1
    discoverability: 40.7
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/activision-blizzard/refs/heads/main/screenshots/activision-blizzard-2026-06-20T164248.png
security:
- kind: authentication
  name: Activision Blizzard Authentication
  slug: activision-blizzard-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Activision Blizzard Domain Security
  slug: activision-blizzard-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: activision-blizzard
tags:
- Fortune 1000
website: https://www.activision-blizzard.com
---

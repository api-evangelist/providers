---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Arcade Games Nl Agentic Access
  operation_count: 15
  slug: arcade-games-nl-agentic-access
  summary_line: 15 operations · 8 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: /
  baseurl_source: spec
  description: The Activity API from Mind Arcade — 1 operation(s) for activity.
  name: Mind Arcade Activity API
  slug: arcade-games-nl-activity-api
- baseURL: /
  baseurl_source: spec
  description: The Agents API from Mind Arcade — 13 operation(s) for agents.
  name: Mind Arcade Agents API
  slug: arcade-games-nl-agents-api
- baseURL: /
  baseurl_source: spec
  description: The Insights API from Mind Arcade — 1 operation(s) for insights.
  name: Mind Arcade Insights API
  slug: arcade-games-nl-insights-api
artifact_total: 31
common:
- group: agent
  href: https://artifacts.apis.io/arcade-games-nl/agentic-access/arcade-games-nl-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/arcade-games-nl-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/arcade-games-nl/rules/arcade-games-nl-rules.yml
  title: ''
  type: Spectral
  url: rules/arcade-games-nl-rules.yml
- group: design
  href: https://artifacts.apis.io/arcade-games-nl/json-ld/arcade-games-nl-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/arcade-games-nl-context.jsonld
- group: design
  href: https://artifacts.apis.io/arcade-games-nl/vocabulary/arcade-games-nl-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/arcade-games-nl-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/arcade-games-nl/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/arcade-games-nl/data-model/arcade-games-nl-data-model.yml
  title: ''
  type: DataModel
  url: data-model/arcade-games-nl-data-model.yml
- group: build
  href: https://artifacts.apis.io/arcade-games-nl/cli/arcade-games-nl-cli.yml
  title: ''
  type: CLI
  url: cli/arcade-games-nl-cli.yml
- group: auth
  href: https://artifacts.apis.io/arcade-games-nl/authentication/arcade-games-nl-authentication.yml
  title: ''
  type: Authentication
  url: authentication/arcade-games-nl-authentication.yml
- group: design
  href: https://artifacts.apis.io/arcade-games-nl/errors/arcade-games-nl-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/arcade-games-nl-problem-types.yml
- group: design
  href: https://artifacts.apis.io/arcade-games-nl/conformance/arcade-games-nl-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arcade-games-nl-conformance.yml
- group: agent
  href: https://artifacts.apis.io/arcade-games-nl/llms/arcade-games-nl-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arcade-games-nl-llms.txt
- group: other
  href: https://artifacts.apis.io/arcade-games-nl/hosts/arcade-games-nl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arcade-games-nl-hosts.yml
- group: auth
  href: https://artifacts.apis.io/arcade-games-nl/security/arcade-games-nl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arcade-games-nl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arcade-games.nl/
- group: docs
  title: ''
  type: Documentation
  url: https://arcade-games.nl/openapi.json
created: '2026-11-01'
description: Mind Arcade is an online playground offering six free browser puzzle games that blend human curiosity with AI challenges. Players can explore a 3D constellation puzzle prototype, tackling deduction, circuit optimization, strategy, planning, pattern recognition, and pathfinding. The platform also provides an Agent Game API (openapi.json) enabling developers to integrate game data and AI-driven interactions into their applications.
image: https://arcade-games.nl/favicon.svg
json_schemas:
- name: ChannelInsights
  property_count: 5
  slug: arcade-games-nl-channel-insights
- name: Move
  property_count: 0
  slug: arcade-games-nl-move
- name: PlayerProfile
  property_count: 8
  slug: arcade-games-nl-player-profile
- name: Score
  property_count: 6
  slug: arcade-games-nl-score
- name: State
  property_count: 39
  slug: arcade-games-nl-state
jsonld:
- class_count: 8
  name: Arcade Games Nl Context
  property_count: 59
  slug: arcade-games-nl-context
layout: provider
modified: '2026-11-01'
name: Mind Arcade
nav: Providers
network: true
overview: 'Mind Arcade publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Activity API, Agents API, and Insights API. Tagged areas include Company, Gaming, Puzzle, Artificial Intelligence, and Browser.


  The Mind Arcade catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Mind Arcade''s developer surface includes CLI, authentication, documentation, and 12 more developer resources.'
plans:
- name: Arcade Games Nl Plans Pricing
  plan_count: 0
  slug: arcade-games-nl-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Arcade Games Nl Rate Limits
  slug: arcade-games-nl-rate-limits
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: Mind Arcade API Rules
  rule_count: 39
  severity_counts:
    error: 36
    hint: 0
    info: 2
    warn: 1
  slug: arcade-games-nl-rules
scopes:
- name: Arcade Games Nl Scopes
  scope_count: 0
  slug: arcade-games-nl-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 30
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 53.6
    developer_ergonomics: 30.2
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 30.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arcade Games Nl Authentication
  slug: arcade-games-nl-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Arcade Games Nl Domain Security
  slug: arcade-games-nl-domain-security
  summary_line: TLSv1.3
skill_count: 15
skills:
- name: active-a-i-sessions
  slug: activeAISessions-skill
- name: create-a-i-account
  slug: createAIAccount-skill
- name: daily-challenges
  slug: dailyChallenges-skill
- name: delete-a-i-account
  slug: deleteAIAccount-skill
- name: gameplay-insights
  slug: gameplayInsights-skill
- name: list-a-i-scores
  slug: listAIScores-skill
- name: play-agent-move
  slug: playAgentMove-skill
- name: public-a-i-profile
  slug: publicAIProfile-skill
- name: public-game-replay
  slug: publicGameReplay-skill
- name: read-agent-game
  slug: readAgentGame-skill
- name: record-browser-activity
  slug: recordBrowserActivity-skill
- name: revoke-account-access
  slug: revokeAccountAccess-skill
- name: rotate-account-token
  slug: rotateAccountToken-skill
- name: start-agent-game
  slug: startAgentGame-skill
- name: submit-agent-score
  slug: submitAgentScore-skill
slug: arcade-games-nl
tags:
- Company
- Gaming
- Puzzle
- Artificial Intelligence
- Browser
website: https://arcade-games.nl/
---

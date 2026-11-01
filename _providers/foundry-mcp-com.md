---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 89
  human_in_the_loop: 4
  name: Foundry Mcp Com Agentic Access
  operation_count: 129
  slug: foundry-mcp-com-agentic-access
  summary_line: 129 operations · 89 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.foundry-mcp.com/v1
  baseurl_source: declared
  description: Endpoints reachable without authentication. Used for health checks and other infrastructure-level probes.
  name: foundry-mcp-com Public API
  slug: foundry-mcp-com-public-api
- baseURL: https://api.foundry-mcp.com/v1
  baseurl_source: declared
  description: Available to Adventurer Patreon subscribers and above (`adventurer`, `dm`).
  name: foundry-mcp-com Tier Adventurer API
  slug: foundry-mcp-com-tier-adventurer-api
- baseURL: https://api.foundry-mcp.com/v1
  baseurl_source: declared
  description: Available to Dungeon Master Patreon subscribers only — the highest tier.
  name: foundry-mcp-com Tier Dm API
  slug: foundry-mcp-com-tier-dm-api
- baseURL: https://api.foundry-mcp.com/v1
  baseurl_source: declared
  description: Available to free Patreon subscribers and above (`free`, `adventurer`, `dm`).
  name: foundry-mcp-com Tier Free API
  slug: foundry-mcp-com-tier-free-api
- baseURL: https://api.foundry-mcp.com/v1
  baseurl_source: declared
  description: Available to any caller with a valid API key, regardless of Patreon subscription status. The minimum authenticated surface.
  name: foundry-mcp-com Tier Guest API
  slug: foundry-mcp-com-tier-guest-api
artifact_total: 25
common:
- group: agent
  href: https://artifacts.apis.io/foundry-mcp-com/agentic-access/foundry-mcp-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/foundry-mcp-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/foundry-mcp-com/rules/foundry-mcp-com-rules.yml
  title: ''
  type: Spectral
  url: rules/foundry-mcp-com-rules.yml
- group: design
  href: https://artifacts.apis.io/foundry-mcp-com/json-ld/foundry-mcp-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/foundry-mcp-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/foundry-mcp-com/vocabulary/foundry-mcp-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/foundry-mcp-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/foundry-mcp-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/foundry-mcp-com/data-model/foundry-mcp-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/foundry-mcp-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/foundry-mcp-com/errors/foundry-mcp-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/foundry-mcp-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/foundry-mcp-com/conformance/foundry-mcp-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/foundry-mcp-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/foundry-mcp-com/well-known/foundry-mcp-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/foundry-mcp-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/foundry-mcp-com/hosts/foundry-mcp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/foundry-mcp-com-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://api.foundry-mcp.com/docs
- group: auth
  href: https://artifacts.apis.io/foundry-mcp-com/authentication/foundry-mcp-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/foundry-mcp-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/foundry-mcp-com/security/foundry-mcp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/foundry-mcp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://foundry-mcp.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://foundry-mcp.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://foundry-mcp.com/terms
- group: docs
  title: ''
  type: APIReference
  url: https://registry.modelcontextprotocol.io/v0/servers?search=com.foundry-mcp
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://registry.modelcontextprotocol.io/openapi.json
  - status: null
    url: https://api.foundry-mcp.com/openapi.json
  - status: 401
    url: https://foundry-mcp.com/mcp
  - status: 401
    url: https://foundry-mcp.com/api/graphql
  - status: 200
    url: https://foundry-mcp.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Foundry MCP provides a bridge between the Foundry Virtual Tabletop (VTT) platform and large language model (LLM) assistants such as Claude, ChatGPT, Codex, and Cursor. It enables AI-driven gameplay by allowing bots to roll dice, manage combat, write journal entries, move tokens, import compendium data, and interact with game mechanics without running a local server. The service offers a public REST API for bots and custom tools, free to start, and integrates with the MCP client ecosystem. It supports D&D 5e, PF2e and other systems, offering features like initiative tracking, skill checks, spell casting, and world time management, all via outgoing connections only.
image: https://foundry-mcp.com/assets/og.png
json_schemas:
- name: RollAttackRequest
  property_count: 5
  slug: foundry-mcp-com-roll-attack-request
- name: RollDamageRequest
  property_count: 4
  slug: foundry-mcp-com-roll-damage-request
- name: RollSkillRequest
  property_count: 5
  slug: foundry-mcp-com-roll-skill-request
- name: SendChatMessageRequest
  property_count: 6
  slug: foundry-mcp-com-send-chat-message-request
- name: UpdateMacroRequest
  property_count: 7
  slug: foundry-mcp-com-update-macro-request
- name: UpdateSceneRequest
  property_count: 15
  slug: foundry-mcp-com-update-scene-request
jsonld:
- class_count: 120
  name: Foundry Mcp Com Context
  property_count: 169
  slug: foundry-mcp-com-context
layout: provider
modified: '2026-10-30'
name: foundry-mcp-com
nav: Providers
network: true
overview: 'foundry-mcp-com publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Public API, Tier Adventurer API, Tier Dm API, and 2 more. Tagged areas include FoundryVTT, MCP, AI, Gaming, and Automation.


  The foundry-mcp-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  foundry-mcp-com''s developer surface includes documentation, authentication, API reference, and 14 more developer resources.'
plans:
- name: Foundry Mcp Com Plans
  plan_count: 0
  slug: foundry-mcp-com-plans
random_paper: 16
rate_limits:
- limit_count: 0
  name: Foundry Mcp Com Rate Limits
  slug: foundry-mcp-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: foundry-mcp-com API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 6
  slug: foundry-mcp-com-rules
scopes:
- name: Foundry Mcp Com Scopes
  scope_count: 0
  slug: foundry-mcp-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.9
  coverage:
    artifact_dirs: 29
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 59.8
    developer_ergonomics: 35.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Foundry Mcp Com Authentication
  slug: foundry-mcp-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Foundry Mcp Com Domain Security
  slug: foundry-mcp-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 6
skills:
- name: actors
  slug: foundry-mcp-com-actors
- name: chat
  slug: foundry-mcp-com-chat
- name: combat
  slug: foundry-mcp-com-combat
- name: foundry-mcp-com-create-actor
  slug: foundry-mcp-com-create-actor
- name: foundry-mcp-com-create-and-broadcast-journal
  slug: foundry-mcp-com-create-and-broadcast-journal
- name: foundry-mcp-com-run-combat
  slug: foundry-mcp-com-run-combat
slug: foundry-mcp-com
tags:
- FoundryVTT
- MCP
- AI
- Gaming
- Automation
website: https://foundry-mcp.com/
---

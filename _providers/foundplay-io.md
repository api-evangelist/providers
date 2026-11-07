---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Foundplay Io Agentic Access
  operation_count: 1
  slug: foundplay-io-agentic-access
  summary_line: 1 operation
api_count: 2
apis:
- baseURL: https://foundplay.io
  baseurl_source: declared
  description: The Games API from foundplay-io — 1 operation(s) for games.
  name: foundplay-io Games API
  slug: foundplay-io-games-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/foundplay-io/agentic-access/foundplay-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/foundplay-io-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/foundplay-io/rules/foundplay-io-rules.yml
  title: ''
  type: Spectral
  url: rules/foundplay-io-rules.yml
- group: agent
  href: https://artifacts.apis.io/foundplay-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/foundplay-io/conformance/foundplay-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/foundplay-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/foundplay-io/llms/foundplay-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/foundplay-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/foundplay-io/mcp/foundplay-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/foundplay-io-mcp.yml
- group: other
  href: https://artifacts.apis.io/foundplay-io/hosts/foundplay-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/foundplay-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/foundplay-io/vendors/foundplay-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/foundplay-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://foundplay.io/terms
- group: start
  title: ''
  type: Sandbox
  url: https://foundplay.io/tags/sandbox
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://foundplay.io/privacy
- group: start
  title: ''
  type: Login
  url: https://foundplay.io/signin
- group: auth
  href: https://artifacts.apis.io/foundplay-io/security/foundplay-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/foundplay-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://foundplay.io/
- group: company
  title: ''
  type: Blog
  url: https://foundplay.io/drops/feed.xml
created: '2026-10-30'
description: Foundplay is a platform that aggregates free browser games, including indie and AI‑generated titles. It offers a catalog of over 2,300 games that can be played directly in the browser without downloads. New games are added twice daily, and the site provides an RSS feed for drops. The service is accessible via web at foundplay.io.
image: https://foundplay.io/opengraph-image.jpg?v=2
json_schemas:
- name: RollAttackRequest
  property_count: 5
  slug: foundplay-io-roll-attack-request
- name: RollDamageRequest
  property_count: 4
  slug: foundplay-io-roll-damage-request
- name: RollSkillRequest
  property_count: 5
  slug: foundplay-io-roll-skill-request
- name: SendChatMessageRequest
  property_count: 6
  slug: foundplay-io-send-chat-message-request
- name: UpdateMacroRequest
  property_count: 7
  slug: foundplay-io-update-macro-request
- name: UpdateSceneRequest
  property_count: 15
  slug: foundplay-io-update-scene-request
jsonld:
- class_count: 120
  name: Foundplay Io Context
  property_count: 169
  slug: foundplay-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at foundplay.io.
  name: foundplay-io MCP Server
  slug: foundplay-io-mcp-yml
modified: '2026-10-30'
name: foundplay-io
nav: Providers
network: true
overview: 'foundplay-io publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Games API. Tagged areas include Games, Browser, Indie, AI-Generated, and Free.


  The foundplay-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  foundplay-io''s developer surface includes sandbox, engineering blog, and 13 more developer resources.'
plans:
- name: Foundplay Io Plans Pricing
  plan_count: 0
  slug: foundplay-io-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Foundplay Io Rate Limits
  slug: foundplay-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: foundplay-io API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: foundplay-io-rules
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 28
    catalog_earned: 52.5
    catalog_earned_first_party: 0.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.3
  facets:
    access_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 51.7
    developer_ergonomics: 11.2
    discoverability: 75.0
    operational_transparency: 0.0
  previous_composite: 31.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/foundplay-io/foundplay-io-2026-11-03T132308.png
security:
- kind: authentication
  name: Foundplay Io Authentication
  slug: foundplay-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Foundplay Io Domain Security
  slug: foundplay-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: foundplay-io-create-and-broadcast-journal
  slug: foundplay-io-create-and-broadcast-journal
- name: foundplay-io-create-combat-with-combatants
  slug: foundplay-io-create-combat-with-combatants
- name: search-games
  slug: foundplay-io-search-games
- name: foundplay-io-send-chat-message
  slug: foundplay-io-send-chat-message
slug: foundplay-io
tags:
- Games
- Browser
- Indie
- AI-Generated
- Free
website: https://foundplay.io/
---

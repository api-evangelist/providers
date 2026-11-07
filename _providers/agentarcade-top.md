---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: near-conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: derived
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for publishing games, playing, and accessing platform data.
  name: Agent Arcade API
  slug: agent-arcade-api
- baseURL: /
  baseurl_source: declared
  description: Executable Protocol 5 contract; runtime status is reported by /api/v5/index.
  name: Agent Arcade Protocol 5 publishing and play API Openapi API
  slug: agent-arcade-protocol-5-publishing-and-play-api-openapi-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/agentarcade-top/rules/agentarcade-top-rules.yml
  title: ''
  type: Spectral
  url: rules/agentarcade-top-rules.yml
- group: design
  href: https://artifacts.apis.io/agentarcade-top/json-ld/agentarcade-top-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentarcade-top-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentarcade-top/vocabulary/agentarcade-top-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentarcade-top-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agentarcade-top/conventions/agentarcade-top-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/agentarcade-top-conventions.yml
- group: design
  href: https://artifacts.apis.io/agentarcade-top/conventions/agentarcade-top-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agentarcade-top-conventions.yml
- group: design
  href: https://artifacts.apis.io/agentarcade-top/conformance/agentarcade-top-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentarcade-top-conformance.yml
- group: design
  href: https://artifacts.apis.io/agentarcade-top/data-model/agentarcade-top-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentarcade-top-data-model.yml
- group: design
  href: https://artifacts.apis.io/agentarcade-top/errors/agentarcade-top-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentarcade-top-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/agentarcade-top/llms/agentarcade-top-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentarcade-top-llms.txt
- group: other
  href: https://artifacts.apis.io/agentarcade-top/a2a/agentarcade-top-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentarcade-top-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agentarcade-top/mcp/agentarcade-top-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentarcade-top-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agentarcade-top/well-known/agentarcade-top-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentarcade-top-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentarcade-top/hosts/agentarcade-top-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentarcade-top-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentarcade-top/vendors/agentarcade-top-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentarcade-top-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://agentarcade.top/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentarcade.top/terms
- group: auth
  title: ''
  type: Security
  url: https://agentarcade.top/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentarcade.top/privacy
- group: auth
  href: https://artifacts.apis.io/agentarcade-top/security/agentarcade-top-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentarcade-top-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentarcade.top/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agentarcade.top/developers
- group: docs
  title: ''
  type: Documentation
  url: https://agentarcade.top/developers
- group: docs
  title: ''
  type: APIReference
  url: https://agentarcade.top/api/v5/openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://agentarcade.top/developers
created: '2026-10-31'
description: Agent Arcade is a platform where AI agents create, play, and certify declarative games. The site offers a game store, live rankings, replays, and governance tools. It provides AI documentation, publisher tools, and an operations hub for developers to integrate with the Agent Arcade API, enabling autonomous game interactions and data access.
json_schemas:
- name: AuthorStepPreviewResponse
  property_count: 16
  slug: agentarcade-top-author-step-preview-response
- name: FeedbackSubmission
  property_count: 12
  slug: agentarcade-top-feedback-submission
- name: FeedbackSummary
  property_count: 8
  slug: agentarcade-top-feedback-summary
- name: PlayActionResult
  property_count: 16
  slug: agentarcade-top-play-action-result
- name: PlayReplay
  property_count: 15
  slug: agentarcade-top-play-replay
- name: PlaySessionState
  property_count: 14
  slug: agentarcade-top-play-session-state
jsonld:
- class_count: 24
  name: Agentarcade Top Context
  property_count: 121
  slug: agentarcade-top-context
layout: provider
mcp_servers:
- description: Remote MCP server at agentarcade.top.
  name: Agent Arcade MCP Server
  slug: agentarcade-top-mcp-yml
modified: '2026-10-31'
name: Agent Arcade
nav: Providers
network: true
overview: 'Agent Arcade publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Protocol 5 publishing and play API Openapi API, and 1 more. Tagged areas include Gaming, Artificial Intelligence, Platform, Games, and Autonomous.


  The Agent Arcade catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Agent Arcade''s developer surface includes documentation, API reference, getting-started guide, and 21 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: Agent Arcade API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 1
  slug: agentarcade-top-rules
score:
  band: thin
  composite: 29.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.3
  facets:
    access_clarity: 14.5
    contract_governance: 22.0
    contract_quality: 50.7
    developer_ergonomics: 19.0
    discoverability: 61.7
    operational_transparency: 5.3
  previous_composite: 37.3
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentarcade Top Domain Security
  slug: agentarcade-top-domain-security
  summary_line: TLSv1.3
slug: agentarcade-top
tags:
- Gaming
- Artificial Intelligence
- Platform
- Games
- Autonomous
website: https://agentarcade.top/
---

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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.8
  scored_at: '2026-11-06'
api_count: 5
apis:
- description: MCP JSON-RPC tools endpoint providing programmatic access to AnchorPad functionality.
  name: AnchorPad MCP
  slug: anchorpad-mcp
- description: The Agent API from AnchorPad — 1 operation(s) for agent.
  name: AnchorPad Agent API
  slug: anchorpad-fun-agent-api
- description: The Agents API from AnchorPad — 2 operation(s) for agents.
  name: AnchorPad Agents API
  slug: anchorpad-fun-agents-api
- description: The Launches API from AnchorPad — 1 operation(s) for launches.
  name: AnchorPad Launches API
  slug: anchorpad-fun-launches-api
- description: The Mcp API from AnchorPad — 1 operation(s) for mcp.
  name: AnchorPad MCP API
  slug: anchorpad-fun-mcp-api
artifact_total: 20
common:
- group: design
  href: https://artifacts.apis.io/anchorpad-fun/rules/anchorpad-fun-rules.yml
  title: ''
  type: Spectral
  url: rules/anchorpad-fun-rules.yml
- group: design
  href: https://artifacts.apis.io/anchorpad-fun/json-ld/anchorpad-fun-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/anchorpad-fun-context.jsonld
- group: design
  href: https://artifacts.apis.io/anchorpad-fun/vocabulary/anchorpad-fun-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/anchorpad-fun-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/anchorpad-fun/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/anchorpad-fun/data-model/anchorpad-fun-data-model.yml
  title: ''
  type: DataModel
  url: data-model/anchorpad-fun-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://anchorpad.fun/#terms
- group: design
  href: https://artifacts.apis.io/anchorpad-fun/conformance/anchorpad-fun-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anchorpad-fun-conformance.yml
- group: agent
  href: https://artifacts.apis.io/anchorpad-fun/llms/anchorpad-fun-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anchorpad-fun-llms.txt
- group: agent
  href: https://artifacts.apis.io/anchorpad-fun/mcp/anchorpad-fun-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/anchorpad-fun-mcp.yml
- group: auth
  href: https://artifacts.apis.io/anchorpad-fun/well-known/anchorpad-fun-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/anchorpad-fun-security.txt
- group: agent
  href: https://artifacts.apis.io/anchorpad-fun/well-known/anchorpad-fun-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anchorpad-fun-well-known.yml
- group: other
  href: https://artifacts.apis.io/anchorpad-fun/hosts/anchorpad-fun-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anchorpad-fun-hosts.yml
- group: other
  href: https://artifacts.apis.io/anchorpad-fun/vendors/anchorpad-fun-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anchorpad-fun-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://anchorpad.fun/media/ai-launch-walkthrough.mp4
- group: docs
  title: ''
  type: Documentation
  url: https://dev.t.me/
- group: auth
  href: https://artifacts.apis.io/anchorpad-fun/security/anchorpad-fun-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/anchorpad-fun-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/anchorpad-fun/security/anchorpad-fun-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anchorpad-fun-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anchorpad.fun/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://anchorpad.fun/docs
- group: docs
  title: ''
  type: APIReference
  url: https://anchorpad.fun/api
- group: operate
  title: ''
  type: Support
  url: https://t.me/anchorpad
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: null
    url: https://anchorpad.fun/mcp
  - status: 401
    url: https://t.me/api/mcp
  - status: 200
    url: https://anchorpad.fun/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AnchorPad is a Solana launchpad that leverages AI agents to help users create and launch new crypto coins quickly. Users can connect AI models like Claude, ChatGPT, Cursor, or Gemini CLI to generate coin parameters, review them, and approve the launch directly from their wallet. The platform charges a 0.4% creator fee on each trade, and offers both assisted and automatic launch modes without requiring an API key or account registration. AnchorPad aims to simplify token creation while ensuring creators retain fee rights.
image: https://anchorpad.fun/ai/share.png
json_schemas:
- name: PostApiAgentRequestsRequest
  property_count: 1
  slug: anchorpad-fun-post-api-agent-requests-request
- name: PostApiAgentsRegisterRequest
  property_count: 5
  slug: anchorpad-fun-post-api-agents-register-request
jsonld:
- class_count: 2
  name: Anchorpad Fun Context
  property_count: 6
  slug: anchorpad-fun-context
layout: provider
mcp_servers:
- description: Remote MCP server at anchorpad.fun.
  name: AnchorPad MCP Server
  slug: anchorpad-fun-mcp-yml
modified: '2026-11-01'
name: AnchorPad
nav: Providers
network: true
overview: 'AnchorPad is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including Agent API, Agents API, Launches API, and 2 more. Tagged areas include Company, Solana, Artificial Intelligence, Cryptocurrency, and Launchpad.


  The AnchorPad catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AnchorPad''s developer surface includes documentation, API reference, support, and 18 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: AnchorPad API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: anchorpad-fun-rules
scopes:
- name: Anchorpad Fun Scopes
  scope_count: 0
  slug: anchorpad-fun-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 20.1
    developer_ergonomics: 21.9
    discoverability: 62.5
    operational_transparency: 5.3
  previous_composite: 24.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: first-party
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
  name: Anchorpad Fun Authentication
  slug: anchorpad-fun-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Anchorpad Fun Domain Security
  slug: anchorpad-fun-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Anchorpad Fun Vulnerability Disclosure
  slug: anchorpad-fun-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 6
skills:
- name: anchorpad-my-coins
  slug: anchorpad-fun-anchorpad_my_coins
- name: anchorpad-pairs
  slug: anchorpad-fun-anchorpad_pairs
- name: anchorpad-prepare-claim
  slug: anchorpad-fun-anchorpad_prepare_claim
- name: anchorpad-prepare-launch
  slug: anchorpad-fun-anchorpad_prepare_launch
- name: anchorpad-prepare-trade
  slug: anchorpad-fun-anchorpad_prepare_trade
- name: anchorpad-request-status
  slug: anchorpad-fun-anchorpad_request_status
slug: anchorpad-fun
tags:
- Company
- Solana
- Artificial Intelligence
- Cryptocurrency
- Launchpad
website: https://anchorpad.fun/
---

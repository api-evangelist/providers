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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API reference for Central City platform
  name: Central City API
  slug: central-city-api
- description: 'Central City API as documented publicly: 41 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Central City API
  slug: centralcity-ai-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/centralcity-ai/rules/centralcity-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/centralcity-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/centralcity-ai/json-ld/centralcity-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/centralcity-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/centralcity-ai/vocabulary/centralcity-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/centralcity-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/centralcity-ai/data-model/centralcity-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/centralcity-ai-data-model.yml
- group: build
  href: https://artifacts.apis.io/centralcity-ai/cli/centralcity-ai-cli.yml
  title: ''
  type: CLI
  url: cli/centralcity-ai-cli.yml
- group: design
  href: https://artifacts.apis.io/centralcity-ai/conventions/centralcity-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/centralcity-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/centralcity-ai/conventions/centralcity-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/centralcity-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/centralcity-ai/authentication/centralcity-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/centralcity-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/centralcity-ai/conformance/centralcity-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/centralcity-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/centralcity-ai/llms/centralcity-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/centralcity-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/centralcity-ai/mcp/centralcity-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/centralcity-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/centralcity-ai/well-known/centralcity-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/centralcity-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/centralcity-ai/well-known/centralcity-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/centralcity-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/centralcity-ai/hosts/centralcity-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/centralcity-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/centralcity-ai/vendors/centralcity-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/centralcity-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://centralcity.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://centralcity.ai/support
- group: operate
  title: ''
  type: StatusPage
  url: https://centralcity.ai/status
- group: auth
  title: ''
  type: Security
  url: https://centralcity.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://centralcity.ai/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://centralcity.ai/news
- group: docs
  title: ''
  type: Documentation
  url: https://centralcity.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://centralcity.ai/docs/api.md#connecting-clients
- group: auth
  href: https://artifacts.apis.io/centralcity-ai/security/centralcity-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/centralcity-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/centralcity-ai/security/centralcity-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/centralcity-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://centralcity.ai/
coverage:
  checked: '2026-11-03'
  detail: Documentation pages are served as markdown but require rendering to access specs, none found.
  evidence:
  - status: 200
    url: https://centralcity.ai/docs/api.md
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: Central City is a platform where AI agents converge, offering a collaborative marketplace for AI services, tools, and interactions. The site provides documentation, use‑case examples, and a developer portal, positioning itself as a hub for AI‑driven applications and community engagement.
image: https://centralcity.ai/brand/og/og-default.png
json_schemas:
- name: PatchApiRoomsRoomRequest
  property_count: 2
  slug: centralcity-ai-patch-api-rooms-room-request
- name: PostApiRoomsRoomMembersAgentidRemoveRequest
  property_count: 2
  slug: centralcity-ai-post-api-rooms-room-members-agentid-remove-request
- name: PostApiRoomsRoomMembersAgentidRemoveResponse
  property_count: 4
  slug: centralcity-ai-post-api-rooms-room-members-agentid-remove-response
- name: PostApiRoomsRoomMuteRequest
  property_count: 3
  slug: centralcity-ai-post-api-rooms-room-mute-request
- name: PostApiRoomsRoomTasksRequest
  property_count: 4
  slug: centralcity-ai-post-api-rooms-room-tasks-request
- name: PostApiRoomsRoomTasksTaskCommentsRequest
  property_count: 3
  slug: centralcity-ai-post-api-rooms-room-tasks-task-comments-request
jsonld:
- class_count: 24
  name: Centralcity Ai Context
  property_count: 25
  slug: centralcity-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at centralcity.ai.
  name: Central City MCP Server
  slug: centralcity-ai-mcp-yml
modified: '2026-11-03'
name: Central City
nav: Providers
network: true
overview: 'Central City is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Platform, Marketplace, and Agents.


  The Central City catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Central City''s developer surface includes CLI, authentication, support, documentation, getting-started guide, and 21 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Central City API Rules
  rule_count: 44
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 1
  slug: centralcity-ai-rules
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 32.1
    discoverability: 57.5
    operational_transparency: 13.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Centralcity Ai Authentication
  slug: centralcity-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Centralcity Ai Domain Security
  slug: centralcity-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Centralcity Ai Vulnerability Disclosure
  slug: centralcity-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: centralcity-ai
tags:
- Company
- Artificial Intelligence
- Platform
- Marketplace
- Agents
- Collaboration
website: https://centralcity.ai/
---

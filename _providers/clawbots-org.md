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
    agent_card: flavored
    agent_skills: unknown
    agentic_access: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for Axiom AI agent platform providing tool endpoints and agent capabilities.
  name: Axiom API
  slug: axiom-api
- description: 'Axiom API as documented publicly: 28 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Axiom API
  slug: clawbots-org-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/clawbots-org/rules/clawbots-org-rules.yml
  title: ''
  type: Spectral
  url: rules/clawbots-org-rules.yml
- group: design
  href: https://artifacts.apis.io/clawbots-org/json-ld/clawbots-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clawbots-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/clawbots-org/vocabulary/clawbots-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clawbots-org-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/clawbots-org/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/clawbots-org/data-model/clawbots-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clawbots-org-data-model.yml
- group: operate
  href: https://artifacts.apis.io/clawbots-org/changelog/clawbots-org-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/clawbots-org-changelog.yml
- group: design
  href: https://artifacts.apis.io/clawbots-org/conformance/clawbots-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clawbots-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/clawbots-org/llms/clawbots-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clawbots-org-llms.txt
- group: other
  href: https://artifacts.apis.io/clawbots-org/a2a/clawbots-org-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/clawbots-org-a2a.yml
- group: agent
  href: https://artifacts.apis.io/clawbots-org/mcp/clawbots-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/clawbots-org-mcp.yml
- group: agent
  href: https://artifacts.apis.io/clawbots-org/well-known/clawbots-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clawbots-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/clawbots-org/hosts/clawbots-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clawbots-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/clawbots-org/vendors/clawbots-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clawbots-org-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.clawbots.org/writing/management
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MeltedMindz
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.clawbots.org/changelog
- group: auth
  href: https://artifacts.apis.io/clawbots-org/security/clawbots-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clawbots-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clawbots.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.clawbots.org/api/manifest
- group: docs
  title: ''
  type: APIReference
  url: https://www.clawbots.org/api/manifest
- group: start
  title: ''
  type: GettingStarted
  url: https://www.clawbots.org/about
coverage:
  checked: '2026-11-04'
  detail: OpenAPI spec not found at https://www.clawbots.org/openapi.json (404)
  evidence:
  - status: 404
    url: https://www.clawbots.org/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Axiom is an AI agent on Base offering a suite of HTTP tools, essays, and a token. Built in public since January 2026, it provides 41 endpoints, 41 ERC‑8257 anchors, and a growing ecosystem of AI‑driven utilities. The platform showcases agent‑tool integration, on‑chain analytics, and open‑source tooling for developers exploring the emerging agent economy.
image: https://www.clawbots.org/og-v2.png
json_schemas:
- name: GetApiToolsBankrLeaderboardResponse
  property_count: 5
  slug: clawbots-org-get-api-tools-bankr-leaderboard-response
- name: GetApiToolsBaseEcosystemRadarResponse
  property_count: 5
  slug: clawbots-org-get-api-tools-base-ecosystem-radar-response
- name: GetApiToolsContractAbiInspectorResponse
  property_count: 5
  slug: clawbots-org-get-api-tools-contract-abi-inspector-response
- name: GetApiToolsNftHolderOverlapResponse
  property_count: 5
  slug: clawbots-org-get-api-tools-nft-holder-overlap-response
- name: PostApiToolsAgentBindingScoutResponse
  property_count: 10
  slug: clawbots-org-post-api-tools-agent-binding-scout-response
- name: PostApiToolsX402CostGuardRequest
  property_count: 5
  slug: clawbots-org-post-api-tools-x402-cost-guard-request
jsonld:
- class_count: 24
  name: Clawbots Org Context
  property_count: 107
  slug: clawbots-org-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.clawbots.org.
  name: Axiom MCP Server
  slug: clawbots-org-mcp-yml
modified: '2026-11-03'
name: Axiom
nav: Providers
network: true
overview: 'Axiom is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Agents, Tools, Blockchain, and Open Source.


  The Axiom catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Axiom''s developer surface includes changelog, documentation, API reference, getting-started guide, and 17 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: Axiom API Rules
  rule_count: 40
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 5
  slug: clawbots-org-rules
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 20.7
    discoverability: 57.5
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clawbots Org Domain Security
  slug: clawbots-org-domain-security
  summary_line: TLSv1.3 · HSTS
slug: clawbots-org
tags:
- Artificial Intelligence
- Agents
- Tools
- Blockchain
- Open Source
website: https://clawbots.org/
---

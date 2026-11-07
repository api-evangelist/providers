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
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Agent Manager Dev Agentic Access
  operation_count: 9
  slug: agent-manager-dev-agentic-access
  summary_line: 9 operations · 2 acting
api_count: 1
apis:
- baseURL: https://agent-manager.dev
  baseurl_source: declared
  description: The documentation, as data and as Markdown.
  name: agent-manager-dev Docs API
  slug: agent-manager-dev-docs-api
- baseURL: https://agent-manager.dev
  baseurl_source: declared
  description: What this API offers.
  name: agent-manager-dev Meta API
  slug: agent-manager-dev-meta-api
- baseURL: https://agent-manager.dev
  baseurl_source: declared
  description: The CLIs agent-manager manages and the tools it exposes.
  name: agent-manager-dev Product API
  slug: agent-manager-dev-product-api
- baseURL: https://agent-manager.dev
  baseurl_source: declared
  description: The current release and how to install it.
  name: agent-manager-dev Releases API
  slug: agent-manager-dev-releases-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/agent-manager-dev/llms/agent-manager-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agent-manager-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/agent-manager-dev/agentic-access/agent-manager-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agent-manager-dev-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agent-manager-dev/rules/agent-manager-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/agent-manager-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/agent-manager-dev/json-ld/agent-manager-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agent-manager-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/agent-manager-dev/vocabulary/agent-manager-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agent-manager-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agent-manager-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agent-manager-dev/data-model/agent-manager-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agent-manager-dev-data-model.yml
- group: build
  href: https://artifacts.apis.io/agent-manager-dev/cli/agent-manager-dev-cli.yml
  title: ''
  type: CLI
  url: cli/agent-manager-dev-cli.yml
- group: operate
  href: https://artifacts.apis.io/agent-manager-dev/changelog/agent-manager-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/agent-manager-dev-changelog.yml
- group: design
  href: https://artifacts.apis.io/agent-manager-dev/errors/agent-manager-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agent-manager-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agent-manager-dev/conformance/agent-manager-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agent-manager-dev-conformance.yml
- group: other
  href: https://artifacts.apis.io/agent-manager-dev/a2a/agent-manager-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agent-manager-dev-a2a.yml
- group: build
  href: https://artifacts.apis.io/agent-manager-dev/mcp/agent-manager-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agent-manager-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/agent-manager-dev/mcp/agent-manager-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agent-manager-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agent-manager-dev/well-known/agent-manager-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agent-manager-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/agent-manager-dev/hosts/agent-manager-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agent-manager-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/agent-manager-dev/vendors/agent-manager-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agent-manager-dev-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agent-manager.dev/privacy/
- group: docs
  title: ''
  type: Documentation
  url: https://agent-manager.dev/docs/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/YoanWai/agent-manager/releases
- group: docs
  title: ''
  type: APIReference
  url: https://agent-manager.dev/llms.txt
- group: company
  title: ''
  type: Website
  url: https://agent-manager.dev/
- group: auth
  href: https://artifacts.apis.io/agent-manager-dev/security/agent-manager-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agent-manager-dev-domain-security.yml
created: '2026-10-30'
description: agent-manager-dev appears to be an open-source Go terminal UI project for managing AI coding agents within tmux, rather than a traditional company. The project provides a TUI that integrates multiple AI agents, offering features like side‑by‑side sessions, quick prompts, and diff reviewing. It is hosted at agent-manager.dev and its source code is available on GitHub. No verified corporate website or official company information could be confirmed, and the listed website points to the project’s documentation site rather than a business entity.
image: https://via.placeholder.com/150
json_schemas:
- name: Agent
  property_count: 5
  slug: agent-manager-dev-agent
- name: McpTool
  property_count: 3
  slug: agent-manager-dev-mcp-tool
- name: PageSummary
  property_count: 6
  slug: agent-manager-dev-page-summary
- name: SearchResult
  property_count: 7
  slug: agent-manager-dev-search-result
jsonld:
- class_count: 5
  name: Agent Manager Dev Context
  property_count: 15
  slug: agent-manager-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at agent-manager.dev.
  name: agent-manager-dev MCP Server
  slug: agent-manager-dev-mcp-yml
modified: '2026-10-30'
name: agent-manager-dev
nav: Providers
network: true
overview: 'agent-manager-dev publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Docs API, Meta API, Product API, and 1 more. Tagged areas include Artificial Intelligence, Agents, Terminal, Open Source, and Go.


  The agent-manager-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  agent-manager-dev''s developer surface includes CLI, changelog, documentation, API reference, and 19 more developer resources.'
plans:
- name: Agent Manager Dev Plans Pricing
  plan_count: 0
  slug: agent-manager-dev-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Agent Manager Dev Rate Limits
  slug: agent-manager-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: agent-manager-dev API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: agent-manager-dev-rules
scopes:
- name: Agent Manager Dev Scopes
  scope_count: 0
  slug: agent-manager-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 31
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 60.7
    developer_ergonomics: 21.9
    discoverability: 65.0
    operational_transparency: 7.9
  previous_composite: 35.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/agent-manager-dev/agent-manager-dev-2026-11-03T120346.png
security:
- kind: authentication
  name: Agent Manager Dev Authentication
  slug: agent-manager-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Agent Manager Dev Domain Security
  slug: agent-manager-dev-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: search-docs
  slug: agent-manager-dev-search-docs
slug: agent-manager-dev
tags:
- Artificial Intelligence
- Agents
- Terminal
- Open Source
- Go
website: https://agent-manager.dev/
---

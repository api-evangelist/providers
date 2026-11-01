---
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 108
  human_in_the_loop: 13
  name: Neruva Io Agentic Access
  operation_count: 173
  slug: neruva-io-agentic-access
  summary_line: 173 operations · 108 acting · 13 human-in-the-loop
api_count: 1
apis:
- description: Internal API for Neruva platform.
  name: Neruva Internal API
  slug: neruva-internal-api
- baseURL: https://api.neruva.io
  baseurl_source: declared
  description: The agent-cognitive API from neruva-io — 13 operation(s) for agent-cognitive.
  name: neruva-io Agent Cognitive API
  slug: neruva-io-agent-cognitive-api
- baseURL: https://api.neruva.io
  baseurl_source: declared
  description: The agent-federated API from neruva-io — 20 operation(s) for agent-federated.
  name: neruva-io Agent Federated API
  slug: neruva-io-agent-federated-api
- baseURL: https://api.neruva.io
  baseurl_source: declared
  description: The audit API from neruva-io — 3 operation(s) for audit.
  name: neruva-io Audit API
  slug: neruva-io-audit-api
- baseURL: https://api.neruva.io
  baseurl_source: declared
  description: The commons API from neruva-io — 39 operation(s) for commons.
  name: neruva-io Commons API
  slug: neruva-io-commons-api
- baseURL: https://api.neruva.io
  baseurl_source: declared
  description: The hd-native API from neruva-io — 37 operation(s) for hd-native.
  name: neruva-io Hd Native API
  slug: neruva-io-hd-native-api
- baseURL: https://api.neruva.io
  baseurl_source: declared
  description: The Health API from neruva-io — 1 operation(s) for health.
  name: neruva-io Health API
  slug: neruva-io-health-api
- baseURL: https://api.neruva.io
  baseurl_source: declared
  description: The Indexes API from neruva-io — 16 operation(s) for indexes.
  name: neruva-io Indexes API
  slug: neruva-io-indexes-api
- baseURL: https://api.neruva.io
  baseurl_source: declared
  description: The me API from neruva-io — 5 operation(s) for me.
  name: neruva-io Me API
  slug: neruva-io-me-api
- baseURL: https://api.neruva.io
  baseurl_source: declared
  description: The Memory API from neruva-io — 1 operation(s) for memory.
  name: neruva-io Memory API
  slug: neruva-io-memory-api
- baseURL: https://api.neruva.io
  baseurl_source: declared
  description: The Neruva API from neruva-io — 1 operation(s) for neruva.
  name: neruva-io Neruva API
  slug: neruva-io-neruva-api
- baseURL: https://api.neruva.io
  baseurl_source: declared
  description: The pii API from neruva-io — 4 operation(s) for pii.
  name: neruva-io Pii API
  slug: neruva-io-pii-api
- baseURL: https://api.neruva.io
  baseurl_source: declared
  description: The records API from neruva-io — 12 operation(s) for records.
  name: neruva-io Records API
  slug: neruva-io-records-api
artifact_total: 27
common:
- group: agent
  href: https://artifacts.apis.io/neruva-io/agentic-access/neruva-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/neruva-io-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/neruva-io/rules/neruva-io-rules.yml
  title: ''
  type: Spectral
  url: rules/neruva-io-rules.yml
- group: design
  href: https://artifacts.apis.io/neruva-io/json-ld/neruva-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/neruva-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/neruva-io/vocabulary/neruva-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/neruva-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/neruva-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/neruva-io/data-model/neruva-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/neruva-io-data-model.yml
- group: auth
  href: https://artifacts.apis.io/neruva-io/authentication/neruva-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/neruva-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/neruva-io/errors/neruva-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/neruva-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/neruva-io/conformance/neruva-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/neruva-io-conformance.yml
- group: build
  href: https://artifacts.apis.io/neruva-io/mcp/neruva-io-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/neruva-io-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/neruva-io/mcp/neruva-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/neruva-io-mcp.yml
- group: other
  href: https://artifacts.apis.io/neruva-io/hosts/neruva-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/neruva-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/neruva-io/vendors/neruva-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/neruva-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/neruva-io/packages/neruva-io-packages.yml
  title: ''
  type: SDKs
  url: packages/neruva-io-packages.yml
- group: build
  href: https://artifacts.apis.io/neruva-io/packages/neruva-io-packages.yml
  title: ''
  type: Packages
  url: packages/neruva-io-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://neruva.io/terms/
- group: auth
  title: ''
  type: Security
  url: https://neruva.io/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://neruva.io/privacy/
- group: auth
  href: https://artifacts.apis.io/neruva-io/security/neruva-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/neruva-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://neruva.io/
- group: docs
  title: ''
  type: Documentation
  url: https://api.neruva.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.neruva.io/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://neruva.io/#use
- group: operate
  title: ''
  type: Support
  url: https://simgen.dev/contact
created: '2026-10-29'
description: Neruva provides a memory layer for AI coding agents, enabling them to recall prior decisions, facts, and session data across runs. Built for Claude Code, it offers an MCP server at api.neruva.io that stores records, knowledge graphs, causal links, analogies, and memory indexes. The platform powers the SECOND STRIKE game and supports developers to build stateful AI applications with persistent memory, versioned records, and secure storage.
image: https://neruva.io/brand/og_image.png
json_schemas:
- name: AgentRecallRequest
  property_count: 7
  slug: neruva-io-agent-recall-request
- name: AgentRememberRequest
  property_count: 10
  slug: neruva-io-agent-remember-request
- name: ModelBeliefAddRequest
  property_count: 12
  slug: neruva-io-model-belief-add-request
- name: RecordQueryRequest
  property_count: 11
  slug: neruva-io-record-query-request
- name: RungIn
  property_count: 15
  slug: neruva-io-rung-in
- name: Rung
  property_count: 22
  slug: neruva-io-rung
jsonld:
- class_count: 120
  name: Neruva Io Context
  property_count: 265
  slug: neruva-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at simgen.dev.
  name: neruva-io MCP Server
  slug: neruva-io-mcp-yml
modified: '2026-10-29'
name: neruva-io
nav: Providers
network: true
overview: 'neruva-io publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Cognitive API, Agent Federated API, Audit API, and 10 more. Tagged areas include Company, Memory, AI, Agents, and MCP.


  The neruva-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  neruva-io''s developer surface includes authentication, documentation, API reference, getting-started guide, support, and 19 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: neruva-io API Rules
  rule_count: 12
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 6
  slug: neruva-io-rules
scopes:
- name: Neruva Io Scopes
  scope_count: 0
  slug: neruva-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 41.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 50.7
    developer_ergonomics: 58.8
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
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
  name: Neruva Io Authentication
  slug: neruva-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Neruva Io Domain Security
  slug: neruva-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: neruva-io-hd-native
  slug: neruva-io-hd-native
slug: neruva-io
tags:
- Company
- Memory
- AI
- Agents
- MCP
website: https://neruva.io/
---

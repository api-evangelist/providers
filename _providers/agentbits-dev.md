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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Agentbits Dev Agentic Access
  operation_count: 19
  slug: agentbits-dev-agentic-access
  summary_line: 19 operations · 12 acting
api_count: 2
apis:
- baseURL: https://agentbits.dev
  baseurl_source: declared
  description: The Health API from Agent Bits — 1 operation(s) for health.
  name: Agent Bits Health API
  slug: agentbits-dev-health-api
- baseURL: https://agentbits.dev
  baseurl_source: declared
  description: Deterministic utilities and lookups
  name: Agent Bits Tool API
  slug: agentbits-dev-tool-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/agentbits-dev/agentic-access/agentbits-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentbits-dev-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agentbits-dev/rules/agentbits-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/agentbits-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/agentbits-dev/vocabulary/agentbits-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentbits-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agentbits-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agentbits-dev/errors/agentbits-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentbits-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentbits-dev/conformance/agentbits-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentbits-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentbits-dev/llms/agentbits-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentbits-dev-llms.txt
- group: build
  href: https://artifacts.apis.io/agentbits-dev/mcp/agentbits-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agentbits-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/agentbits-dev/mcp/agentbits-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentbits-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agentbits-dev/well-known/agentbits-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentbits-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentbits-dev/hosts/agentbits-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentbits-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentbits-dev/vendors/agentbits-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentbits-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agentbits-dev/security/agentbits-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentbits-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentbits.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://agentbits.dev/openapi.json
created: '2026-11-01'
description: Agent Bits provides machine‑readable utilities and datasets for AI agents, offering a suite of tools such as Base64 encoding/decoding, country and currency lookups, ISBN validation, and more. All capabilities are accessible via simple HTTP MCP endpoints without requiring API keys, enabling agents to enrich data, transform content, and perform validation tasks programmatically. The service is openly documented and includes an OpenAPI spec, catalog, and developer guides.
jsonld:
- class_count: 47
  name: Agentbits Dev Context
  property_count: 190
  slug: agentbits-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at agentbits.dev.
  name: Agent Bits MCP Server
  slug: agentbits-dev-mcp-yml
modified: '2026-11-01'
name: Agent Bits
nav: Providers
network: true
overview: 'Agent Bits publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Health API and Tool API. Tagged areas include Artificial Intelligence, Utilities, Data, Tools, and Machine-Readable.


  The Agent Bits catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Agent Bits'' developer surface includes API reference and 14 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Agent Bits API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: agentbits-dev-rules
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.9
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 39.6
    developer_ergonomics: 5.4
    discoverability: 61.7
    operational_transparency: 0.0
  previous_composite: 17.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 33.3
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentbits Dev Authentication
  slug: agentbits-dev-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Agentbits Dev Domain Security
  slug: agentbits-dev-domain-security
  summary_line: TLSv1.3
skill_count: 2
skills:
- name: agentbits-dev-base64-encode-decode
  slug: agentbits-dev-base64-encode-decode
- name: agentbits-dev-register-and-view-profile
  slug: agentbits-dev-register-and-view-profile
slug: agentbits-dev
tags:
- Artificial Intelligence
- Utilities
- Data
- Tools
- Machine-Readable
website: https://agentbits.dev/
---

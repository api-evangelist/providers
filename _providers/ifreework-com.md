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
  band: agent-ready
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Ifreework Com Agentic Access
  operation_count: 1
  slug: ifreework-com-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://ifreework.com
  baseurl_source: declared
  description: The Mcp API from ifreework-com — 1 operation(s) for mcp.
  name: ifreework-com MCP API
  slug: ifreework-com-mcp-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/ifreework-com/llms/ifreework-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ifreework-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/ifreework-com/agentic-access/ifreework-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ifreework-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/ifreework-com/rules/ifreework-com-rules.yml
  title: ''
  type: Spectral
  url: rules/ifreework-com-rules.yml
- group: design
  href: https://artifacts.apis.io/ifreework-com/json-ld/ifreework-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ifreework-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/ifreework-com/vocabulary/ifreework-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ifreework-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ifreework-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ifreework-com/data-model/ifreework-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ifreework-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/ifreework-com/errors/ifreework-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ifreework-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ifreework-com/conformance/ifreework-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ifreework-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/ifreework-com/a2a/ifreework-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/ifreework-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/ifreework-com/mcp/ifreework-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ifreework-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/ifreework-com/well-known/ifreework-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ifreework-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ifreework-com/hosts/ifreework-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ifreework-com-hosts.yml
- group: other
  title: ''
  type: Leadership
  url: https://ifreework.com/team/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/userifw
- group: company
  title: ''
  type: Blog
  url: https://ifreework.com/blog/
- group: company
  title: ''
  type: Website
  url: https://ifreework.com/
- group: auth
  href: https://artifacts.apis.io/ifreework-com/security/ifreework-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ifreework-com-domain-security.yml
created: '2026-10-30'
description: No public website or documentation could be identified for ifreework-com; attempts to access https://ifreework.com/ returned a personal developer page unrelated to the company. No API documentation, developer portal, or other corporate web presence was discovered.
image: https://ifreework.com/favicon.ico
json_schemas:
- name: JsonRpcRequest
  property_count: 4
  slug: ifreework-com-json-rpc-request
- name: JsonRpcResponse
  property_count: 4
  slug: ifreework-com-json-rpc-response
jsonld:
- class_count: 2
  name: Ifreework Com Context
  property_count: 6
  slug: ifreework-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at ifreework.com.
  name: ifreework-com MCP Server
  slug: ifreework-com-mcp-yml
modified: '2026-10-30'
name: ifreework-com
nav: Providers
network: true
overview: 'ifreework-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: MCP API. Tagged areas include Company and Harvest.


  The ifreework-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ifreework-com''s developer surface includes engineering blog and 17 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: ifreework-com API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: ifreework-com-rules
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 53.0
    developer_ergonomics: 7.6
    discoverability: 57.5
    operational_transparency: 2.6
  previous_composite: 24.4
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
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ifreework-com/ifreework-com-2026-11-03T133638.png
security:
- kind: domain-security
  name: Ifreework Com Domain Security
  slug: ifreework-com-domain-security
  summary_line: TLSv1.3
slug: ifreework-com
tags:
- Company
- Harvest
website: https://ifreework.com/
---

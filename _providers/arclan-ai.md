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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Arclan Ai Agentic Access
  operation_count: 5
  slug: arclan-ai-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 1
apis:
- baseURL: https://arclan.ai
  baseurl_source: declared
  description: The Registry API from Arclan — 3 operation(s) for registry.
  name: Arclan Registry API
  slug: arclan-ai-registry-api
- baseURL: https://arclan.ai
  baseurl_source: declared
  description: The Stats API from Arclan — 1 operation(s) for stats.
  name: Arclan Stats API
  slug: arclan-ai-stats-api
- baseURL: https://arclan.ai
  baseurl_source: declared
  description: The Submit API from Arclan — 1 operation(s) for submit.
  name: Arclan Submit API
  slug: arclan-ai-submit-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/arclan-ai/agentic-access/arclan-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/arclan-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/arclan-ai/rules/arclan-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/arclan-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/arclan-ai/json-ld/arclan-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/arclan-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/arclan-ai/vocabulary/arclan-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/arclan-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/arclan-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/arclan-ai/data-model/arclan-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/arclan-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/arclan-ai/errors/arclan-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/arclan-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/arclan-ai/conformance/arclan-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arclan-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/arclan-ai/llms/arclan-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arclan-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/arclan-ai/well-known/arclan-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arclan-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/arclan-ai/hosts/arclan-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arclan-ai-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://arclan.ai/api/docs
- group: auth
  href: https://artifacts.apis.io/arclan-ai/security/arclan-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arclan-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arclan.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://arclan.ai/api/registry
created: '2026-11-01'
description: Arclan provides a continuously validated registry of MCP servers, OpenAPI tools, and AI plugins, offering discovery, validation, and reliability metrics for agents. The platform indexes tools from GitHub, npm, PyPI, and well‑known MCP endpoints, delivering up‑to‑date information and security checks.
image: https://arclan.ai/favicon.svg
json_schemas:
- name: RegistryListResponse
  property_count: 0
  slug: arclan-ai-registry-list-response
- name: ServerDetail
  property_count: 0
  slug: arclan-ai-server-detail
- name: StatsResponse
  property_count: 0
  slug: arclan-ai-stats-response
jsonld:
- class_count: 1
  name: Arclan Ai Context
  property_count: 14
  slug: arclan-ai-context
layout: provider
modified: '2026-11-01'
name: Arclan
nav: Providers
network: true
overview: 'Arclan publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Registry API, Stats API, and Submit API. Tagged areas include Company, Registry, MCP, OpenAPI, and Artificial Intelligence.


  The Arclan catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Arclan''s developer surface includes documentation, API reference, and 13 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: Arclan API Rules
  rule_count: 38
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 1
  slug: arclan-ai-rules
scopes:
- name: Arclan Ai Scopes
  scope_count: 0
  slug: arclan-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 26.1
  coverage:
    artifact_dirs: 26
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 53.0
    developer_ergonomics: 14.8
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 27.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arclan Ai Authentication
  slug: arclan-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Arclan Ai Domain Security
  slug: arclan-ai-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 3
skills:
- name: get-server
  slug: arclan-ai-get-server
- name: list-servers
  slug: arclan-ai-list-servers
- name: submit-server
  slug: arclan-ai-submit-server
slug: arclan-ai
tags:
- Company
- Registry
- MCP
- OpenAPI
- Artificial Intelligence
- Validation
website: https://arclan.ai/
---

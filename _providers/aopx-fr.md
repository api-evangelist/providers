---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Aopx Fr Agentic Access
  operation_count: 5
  slug: aopx-fr-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.aopx.fr
  baseurl_source: declared
  description: The AOPX Recommend v0 API from aopx-fr — 5 operation(s) for aopx recommend v0.
  name: aopx-fr AOPX Recommend v0 API
  slug: aopx-fr-aopx-recommend-v0-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/aopx-fr/agentic-access/aopx-fr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aopx-fr-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/aopx-fr/rules/aopx-fr-rules.yml
  title: ''
  type: Spectral
  url: rules/aopx-fr-rules.yml
- group: design
  href: https://artifacts.apis.io/aopx-fr/json-ld/aopx-fr-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aopx-fr-context.jsonld
- group: design
  href: https://artifacts.apis.io/aopx-fr/vocabulary/aopx-fr-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aopx-fr-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aopx-fr/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aopx-fr/data-model/aopx-fr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aopx-fr-data-model.yml
- group: design
  href: https://artifacts.apis.io/aopx-fr/errors/aopx-fr-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aopx-fr-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aopx-fr/conformance/aopx-fr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aopx-fr-conformance.yml
- group: build
  href: https://artifacts.apis.io/aopx-fr/mcp/aopx-fr-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aopx-fr-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/aopx-fr/mcp/aopx-fr-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aopx-fr-mcp.yml
- group: other
  href: https://artifacts.apis.io/aopx-fr/hosts/aopx-fr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aopx-fr-hosts.yml
- group: other
  href: https://artifacts.apis.io/aopx-fr/vendors/aopx-fr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aopx-fr-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aopx-fr/security/aopx-fr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aopx-fr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aopx.fr/
- group: docs
  title: ''
  type: Documentation
  url: https://aopx.fr/api-reference.html
- group: docs
  title: ''
  type: APIReference
  url: https://aopx.fr/api-reference.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aopx.fr/legals.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aopx.fr/legals.html
created: '2026-10-30'
description: AOPX Labs provides an evidence‑based provider‑selection layer for software agents, routing search API requests through measured benchmarks, fallback logic, and reported production outcomes. Originating from a token experiment, the project now focuses on AI agent routing, MCP tools, public benchmarks, and transparent evidence of provider performance.
image: https://aopx.fr/bonhomme.png
json_schemas:
- name: OutcomeRequest
  property_count: 2
  slug: aopx-fr-outcome-request
- name: OutcomeResponse
  property_count: 5
  slug: aopx-fr-outcome-response
- name: RecommendRequest
  property_count: 6
  slug: aopx-fr-recommend-request
- name: RecommendResponse
  property_count: 11
  slug: aopx-fr-recommend-response
jsonld:
- class_count: 7
  name: Aopx Fr Context
  property_count: 30
  slug: aopx-fr-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.aopx.fr.
  name: aopx-fr MCP Server
  slug: aopx-fr-mcp-yml
modified: '2026-10-30'
name: aopx-fr
nav: Providers
network: true
overview: 'aopx-fr publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: AOPX Recommend v0 API. Tagged areas include Search, AI, Routing, Benchmark, and Evidence.


  The aopx-fr catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  aopx-fr''s developer surface includes documentation, API reference, and 16 more developer resources.'
plans:
- name: Aopx Fr Plans Pricing
  plan_count: 0
  slug: aopx-fr-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Aopx Fr Rate Limits
  slug: aopx-fr-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: aopx-fr API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: aopx-fr-rules
scopes:
- name: Aopx Fr Scopes
  scope_count: 0
  slug: aopx-fr-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 28
    catalog_earned: 77.7
    catalog_earned_first_party: 0.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 79.1
    contract_quality: 51.6
    developer_ergonomics: 23.1
    discoverability: 65.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aopx Fr Authentication
  slug: aopx-fr-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aopx Fr Domain Security
  slug: aopx-fr-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: aopx-fr-recommend-provider
  slug: aopx-fr-recommend-provider
slug: aopx-fr
tags:
- Search
- AI
- Routing
- Benchmark
- Evidence
website: https://aopx.fr/
---

---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Realworldapis Com Agentic Access
  operation_count: 13
  slug: realworldapis-com-agentic-access
  summary_line: 13 operations · 2 acting
api_count: 1
apis:
- description: Remote MCP discovery, decision and verification service.
  name: RealWorldAPIs MCP
  slug: realworldapis-mcp
- baseURL: https://realworldapis.com
  baseurl_source: declared
  description: The Ai Recommend API from realworldapis-com — 1 operation(s) for ai recommend.
  name: realworldapis-com Ai Recommend API
  slug: realworldapis-com-ai-recommend-api
- baseURL: https://realworldapis.com
  baseurl_source: declared
  description: The Apis API from realworldapis-com — 1 operation(s) for apis.
  name: realworldapis-com APIs API
  slug: realworldapis-com-apis-api
- baseURL: https://realworldapis.com
  baseurl_source: declared
  description: The Capabilities.json API from realworldapis-com — 1 operation(s) for capabilities.json.
  name: realworldapis-com Capabilities.json API
  slug: realworldapis-com-capabilities-json-api
- baseURL: https://realworldapis.com
  baseurl_source: declared
  description: The Catalog.json API from realworldapis-com — 1 operation(s) for catalog.json.
  name: realworldapis-com Catalog.json API
  slug: realworldapis-com-catalog-json-api
- baseURL: https://realworldapis.com
  baseurl_source: declared
  description: The Categories.json API from realworldapis-com — 1 operation(s) for categories.json.
  name: realworldapis-com Categories.json API
  slug: realworldapis-com-categories-json-api
- baseURL: https://realworldapis.com
  baseurl_source: declared
  description: The Recommend API from realworldapis-com — 1 operation(s) for recommend.
  name: realworldapis-com Recommend API
  slug: realworldapis-com-recommend-api
- baseURL: https://realworldapis.com
  baseurl_source: declared
  description: The Research API from realworldapis-com — 1 operation(s) for research.
  name: realworldapis-com Research API
  slug: realworldapis-com-research-api
- baseURL: https://realworldapis.com
  baseurl_source: declared
  description: The Verify Requirement API from realworldapis-com — 1 operation(s) for verify requirement.
  name: realworldapis-com Verify Requirement API
  slug: realworldapis-com-verify-requirement-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/realworldapis-com/agentic-access/realworldapis-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/realworldapis-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/realworldapis-com/rate-limits/realworldapis-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/realworldapis-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/realworldapis-com/rules/realworldapis-com-rules.yml
  title: ''
  type: Spectral
  url: rules/realworldapis-com-rules.yml
- group: design
  href: https://artifacts.apis.io/realworldapis-com/json-ld/realworldapis-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/realworldapis-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/realworldapis-com/vocabulary/realworldapis-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/realworldapis-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/realworldapis-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/realworldapis-com/data-model/realworldapis-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/realworldapis-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/realworldapis-com/components/realworldapis-com-components.yml
  title: ''
  type: Components
  url: components/realworldapis-com-components.yml
- group: design
  href: https://artifacts.apis.io/realworldapis-com/conventions/realworldapis-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/realworldapis-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/realworldapis-com/authentication/realworldapis-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/realworldapis-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/realworldapis-com/lifecycle/realworldapis-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/realworldapis-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/realworldapis-com/errors/realworldapis-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/realworldapis-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/realworldapis-com/conformance/realworldapis-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/realworldapis-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/realworldapis-com/llms/realworldapis-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/realworldapis-com-llms.txt
- group: build
  href: https://artifacts.apis.io/realworldapis-com/mcp/realworldapis-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/realworldapis-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/realworldapis-com/mcp/realworldapis-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/realworldapis-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/realworldapis-com/hosts/realworldapis-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/realworldapis-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/realworldapis-com/vendors/realworldapis-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/realworldapis-com-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://realworldapis.com/go/docs/mapbox
- group: auth
  href: https://artifacts.apis.io/realworldapis-com/security/realworldapis-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/realworldapis-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://realworldapis.com/
created: '2026-10-31'
description: RealWorldAPIs is an evidence-first API discovery and decision layer for AI agents connecting to the physical world. RWAPIS matches tasks to verified API capabilities and checks access, approval, safety, reversibility and execution constraints before ranking. A real-world API connects software or AI agents to data, devices, infrastructure or services representing the physical world — including weather, maps, mobility, logistics, IoT, energy and robotics.
image: https://realworldapis.com/favicon.png
jsonld:
- class_count: 2
  name: Realworldapis Com Context
  property_count: 21
  slug: realworldapis-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.realworldapis.com.
  name: realworldapis-com MCP Server
  slug: realworldapis-com-mcp-yml
modified: '2026-10-31'
name: realworldapis-com
nav: Providers
network: true
overview: 'realworldapis-com publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Ai Recommend API, APIs API, Capabilities.json API, and 6 more. Tagged areas include Discovery, Artificial Intelligence, PhysicalWorld, and RealWorldAPIs.


  The realworldapis-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  realworldapis-com''s developer surface includes authentication, documentation, and 19 more developer resources.'
plans:
- name: Realworldapis Com Plans Pricing
  plan_count: 0
  slug: realworldapis-com-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Realworldapis Com Rate Limits
  slug: realworldapis-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: realworldapis-com API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: realworldapis-com-rules
scopes:
- name: Realworldapis Com Scopes
  scope_count: 0
  slug: realworldapis-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 29
    catalog_earned: 57.8
    catalog_earned_first_party: 12.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.7
  facets:
    access_clarity: 0.0
    contract_governance: 35.6
    contract_quality: 44.3
    developer_ergonomics: 23.1
    discoverability: 56.7
    operational_transparency: 31.6
  previous_composite: 32.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
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
screenshot: https://apis.io/screenshots/realworldapis-com/realworldapis-com-2026-11-03T142030.png
security:
- kind: authentication
  name: Realworldapis Com Authentication
  slug: realworldapis-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Realworldapis Com Domain Security
  slug: realworldapis-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: realworldapis-com
tags:
- Discovery
- Artificial Intelligence
- PhysicalWorld
- RealWorldAPIs
website: https://realworldapis.com/
---

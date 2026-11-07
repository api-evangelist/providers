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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 11.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Modular deterministic computation API.
  name: APIShed
  slug: apished
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/apished-com/rules/apished-com-rules.yml
  title: ''
  type: Spectral
  url: rules/apished-com-rules.yml
- group: design
  href: https://artifacts.apis.io/apished-com/json-ld/apished-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apished-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/apished-com/vocabulary/apished-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apished-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/apished-com/conformance/apished-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apished-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apished-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/apished-com/data-model/apished-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apished-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/apished-com/errors/apished-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apished-com-problem-types.yml
- group: build
  href: https://artifacts.apis.io/apished-com/mcp/apished-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/apished-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/apished-com/mcp/apished-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/apished-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/apished-com/hosts/apished-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apished-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/apished-com/security/apished-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apished-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apished.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apished.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://apished.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://apished.com/docs
created: '2026-10-29'
description: APIShed is a modular HTTP API server that provides deterministic computation endpoints for tasks such as checksums, date arithmetic, character counts, and token counts. It offers a RESTful interface and MCP tools without requiring API keys or sign‑up, making it suitable for edge devices and IoT boards. The service is rate‑limited to 1 request per second per IP per endpoint and returns standard HTTP status codes. Documentation and an OpenAPI specification are publicly available.
image: https://apished.com
jsonld:
- class_count: 85
  name: Apished Com Context
  property_count: 103
  slug: apished-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at apished.com.
  name: apished-com MCP Server
  slug: apished-com-mcp-yml
modified: '2026-10-29'
name: apished-com
nav: Providers
network: true
overview: 'apished-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Modular, OpenAPI, MCP, and Utilities.


  The apished-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  apished-com''s developer surface includes documentation, API reference, getting-started guide, and 12 more developer resources.'
plans:
- name: Apished Com Plans Pricing
  plan_count: 0
  slug: apished-com-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Apished Com Rate Limits
  slug: apished-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: apished-com API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: apished-com-rules
scopes:
- name: Apished Com Scopes
  scope_count: 0
  slug: apished-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.8
  coverage:
    artifact_dirs: 26
    catalog_earned: 53.0
    catalog_earned_first_party: 0.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.3
  facets:
    access_clarity: 0.0
    contract_governance: 19.7
    contract_quality: 14.7
    developer_ergonomics: 20.7
    discoverability: 68.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 22.1
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/apished-com/apished-com-2026-11-03T121004.png
security:
- kind: authentication
  name: Apished Com Authentication
  slug: apished-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Apished Com Domain Security
  slug: apished-com-domain-security
  summary_line: TLSv1.3 · DNSSEC
skill_count: 1
skills:
- name: apished-com-mcp-setup
  slug: apished-com-mcp-setup
slug: apished-com
tags:
- Company
- Modular
- OpenAPI
- MCP
- Utilities
website: https://apished.com/
---

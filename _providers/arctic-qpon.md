---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Arctic provides an OpenAI‑compatible API for accessing AI models and blockchain‑linked data.
  name: Arctic API
  slug: arctic-api
- description: 'Arctic API as documented publicly: 16 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Arctic API
  slug: arctic-qpon-api
artifact_total: 14
common:
- group: operate
  href: https://artifacts.apis.io/arctic-qpon/rate-limits/arctic-qpon-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/arctic-qpon-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/arctic-qpon/plans/arctic-qpon-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/arctic-qpon-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/arctic-qpon/rules/arctic-qpon-rules.yml
  title: ''
  type: Spectral
  url: rules/arctic-qpon-rules.yml
- group: design
  href: https://artifacts.apis.io/arctic-qpon/json-ld/arctic-qpon-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/arctic-qpon-context.jsonld
- group: design
  href: https://artifacts.apis.io/arctic-qpon/vocabulary/arctic-qpon-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/arctic-qpon-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/arctic-qpon/data-model/arctic-qpon-data-model.yml
  title: ''
  type: DataModel
  url: data-model/arctic-qpon-data-model.yml
- group: build
  href: https://artifacts.apis.io/arctic-qpon/cli/arctic-qpon-cli.yml
  title: ''
  type: CLI
  url: cli/arctic-qpon-cli.yml
- group: design
  href: https://artifacts.apis.io/arctic-qpon/conventions/arctic-qpon-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/arctic-qpon-conventions.yml
- group: design
  href: https://artifacts.apis.io/arctic-qpon/conventions/arctic-qpon-conventions.yml
  title: ''
  type: Conventions
  url: conventions/arctic-qpon-conventions.yml
- group: auth
  href: https://artifacts.apis.io/arctic-qpon/authentication/arctic-qpon-authentication.yml
  title: ''
  type: Authentication
  url: authentication/arctic-qpon-authentication.yml
- group: design
  href: https://artifacts.apis.io/arctic-qpon/errors/arctic-qpon-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/arctic-qpon-problem-types.yml
- group: design
  href: https://artifacts.apis.io/arctic-qpon/conformance/arctic-qpon-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arctic-qpon-conformance.yml
- group: build
  href: https://artifacts.apis.io/arctic-qpon/mcp/arctic-qpon-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/arctic-qpon-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/arctic-qpon/mcp/arctic-qpon-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/arctic-qpon-mcp.yml
- group: other
  href: https://artifacts.apis.io/arctic-qpon/hosts/arctic-qpon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arctic-qpon-hosts.yml
- group: other
  href: https://artifacts.apis.io/arctic-qpon/vendors/arctic-qpon-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arctic-qpon-vendors.yml
- group: auth
  href: https://artifacts.apis.io/arctic-qpon/security/arctic-qpon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arctic-qpon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arctic.qpon/
- group: docs
  title: ''
  type: Documentation
  url: https://www.arctic.qpon/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.arctic.qpon/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.arctic.qpon/playground
- group: operate
  title: ''
  type: Roadmap
  url: https://www.arctic.qpon/roadmap
- group: operate
  title: ''
  type: Support
  url: https://www.arctic.qpon/console
- group: agent
  title: ''
  type: MCP
  url: https://www.arctic.qpon/mcp
created: '2026-11-01'
description: Arctic provides a unified platform for accessing a wide range of free AI models through a single OpenAI‑compatible API. Users can compare models side‑by‑side, run them via the web playground, integrate via the API & CLI, and explore blockchain‑linked data on the Robinhood Chain. The service is free, open, and includes tools such as MCP server, console, and community features like roadmaps and a shared inference ledger.
image: https://www.arctic.qpon/film/arctic.jpg
json_schemas:
- name: GetApiRadarResponse
  property_count: 2
  slug: arctic-qpon-get-api-radar-response
- name: GetApiScanResponse
  property_count: 23
  slug: arctic-qpon-get-api-scan-response
- name: GetApiV1AudioSpeechResponse
  property_count: 1
  slug: arctic-qpon-get-api-v1-audio-speech-response
- name: PostApiV1ChatCompletionsRequest
  property_count: 2
  slug: arctic-qpon-post-api-v1-chat-completions-request
jsonld:
- class_count: 4
  name: Arctic Qpon Context
  property_count: 28
  slug: arctic-qpon-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.arctic.qpon.
  name: Arctic MCP Server
  slug: arctic-qpon-mcp-yml
modified: '2026-11-01'
name: Arctic
nav: Providers
network: true
overview: 'Arctic is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Machine Learning, OpenAI-Compatible, Cryptocurrency, and Platform.


  The Arctic catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Arctic''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, support, and 18 more developer resources.'
plans:
- name: Arctic Qpon Plans Pricing
  plan_count: 4
  slug: arctic-qpon-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 4
  name: Arctic Qpon Rate Limits
  slug: arctic-qpon-rate-limits
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: Arctic API Rules
  rule_count: 40
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 1
  slug: arctic-qpon-rules
scopes:
- name: Arctic Qpon Scopes
  scope_count: 0
  slug: arctic-qpon-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.2
  coverage:
    artifact_dirs: 27
    catalog_earned: 78.8
    catalog_earned_first_party: 24.0
    catalog_gap: 36.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 22.1
    developer_ergonomics: 35.7
    discoverability: 56.7
    operational_transparency: 34.2
  previous_composite: 36.8
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arctic Qpon Authentication
  slug: arctic-qpon-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Arctic Qpon Domain Security
  slug: arctic-qpon-domain-security
  summary_line: TLSv1.3 · HSTS
slug: arctic-qpon
tags:
- Artificial Intelligence
- Machine Learning
- OpenAI-Compatible
- Cryptocurrency
- Platform
website: https://www.arctic.qpon/
---

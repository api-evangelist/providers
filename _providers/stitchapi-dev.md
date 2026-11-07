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
    agent_skills: false
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.1
  scored_at: '2026-11-06'
api_count: 4
apis:
- description: StitchAPI provides a Model Context Protocol (MCP) endpoint for AI agents, exposing tools such as search_docs and get_doc for documentation search and retrieval.
  name: StitchAPI MCP
  slug: stitchapi-mcp
- description: 'stitchapi-dev For agents API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: stitchapi-dev For agents API
  slug: agents-api
- description: 'stitchapi-dev core API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: stitchapi-dev core API
  slug: core-api
- description: 'stitchapi-dev Scenarios API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: stitchapi-dev Scenarios API
  slug: scenarios-api
artifact_total: 15
common:
- group: design
  href: https://artifacts.apis.io/stitchapi-dev/rules/stitchapi-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/stitchapi-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/stitchapi-dev/json-ld/stitchapi-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/stitchapi-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/stitchapi-dev/vocabulary/stitchapi-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/stitchapi-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/stitchapi-dev/data-model/stitchapi-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/stitchapi-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/stitchapi-dev/conformance/stitchapi-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/stitchapi-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/stitchapi-dev/llms/stitchapi-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stitchapi-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/stitchapi-dev/mcp/stitchapi-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/stitchapi-dev-mcp.yml
- group: other
  href: https://artifacts.apis.io/stitchapi-dev/hosts/stitchapi-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stitchapi-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/stitchapi-dev/vendors/stitchapi-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/stitchapi-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/stitchapi-dev/packages/stitchapi-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/stitchapi-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/stitchapi-dev/packages/stitchapi-dev-packages.yml
  title: ''
  type: Packages
  url: packages/stitchapi-dev-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: https://stitchapi.dev/playground
- group: auth
  href: https://artifacts.apis.io/stitchapi-dev/security/stitchapi-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stitchapi-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stitchapi.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://stitchapi.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://stitchapi.dev/docs/guides/auth/api-key
- group: start
  title: ''
  type: GettingStarted
  url: https://stitchapi.dev/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://stitchapi.dev/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rejifald
created: '2026-10-31'
description: StitchAPI is an open-source tool that lets developers turn any existing API into a typed, resilient function. By declaring endpoints once with type definitions, authentication, retries, rate limiting, and validation, developers can call APIs like local functions from JavaScript, TypeScript, Node.js, Deno, or browsers. The platform provides a CLI, an HTTP route, and integration with the Model Context Protocol (MCP) for AI agents, enabling zero-code API stitching without server-side code generation. It aims to simplify API integration, improve reliability, and accelerate development.
image: https://stitchapi.dev/og/home
json_schemas:
- name: GetLlmsFullTxtResponse
  property_count: 1
  slug: stitchapi-dev-get-llms-full-txt-response
- name: GetLlmsTxtResponse
  property_count: 1
  slug: stitchapi-dev-get-llms-txt-response
- name: GetOrdersResponse
  property_count: 1
  slug: stitchapi-dev-get-orders-response
- name: GetResponse
  property_count: 1
  slug: stitchapi-dev-get-response
- name: GetUsers1Response
  property_count: 1
  slug: stitchapi-dev-get-users1-response
jsonld:
- class_count: 5
  name: Stitchapi Dev Context
  property_count: 4
  slug: stitchapi-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at stitchapi.dev.
  name: stitchapi-dev MCP Server
  slug: stitchapi-dev-mcp-yml
modified: '2026-10-31'
name: stitchapi-dev
nav: Providers
network: true
overview: 'stitchapi-dev is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including For agents API, core API, Scenarios API, and 1 more. Tagged areas include Company, Integration, TypeScript, Node.js, and OpenAPI.


  The stitchapi-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  stitchapi-dev''s developer surface includes sandbox, documentation, API reference, getting-started guide, engineering blog, and 14 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: stitchapi-dev API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: stitchapi-dev-rules
scopes:
- name: Stitchapi Dev Scopes
  scope_count: 0
  slug: stitchapi-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 27
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 21.1
    developer_ergonomics: 26.2
    discoverability: 61.7
    operational_transparency: 2.6
  previous_composite: 24.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/stitchapi-dev/stitchapi-dev-2026-11-03T143825.png
security:
- kind: authentication
  name: Stitchapi Dev Authentication
  slug: stitchapi-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Stitchapi Dev Domain Security
  slug: stitchapi-dev-domain-security
  summary_line: TLSv1.3 · HSTS
slug: stitchapi-dev
tags:
- Company
- Integration
- TypeScript
- Node.js
- OpenAPI
- MCP
- Resilience
website: https://stitchapi.dev/
---

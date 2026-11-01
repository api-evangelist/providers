---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 46.5
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Read and write your memories over plain HTTPS, using the same OAuth token your MCP clients already use. No SDK, no API key.
  name: Agentage Memory REST API
  slug: agentage-memory-rest-api
- baseURL: https://api.agentage.io
  baseurl_source: declared
  description: 'agentage-io API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: agentage-io API
  slug: agentage-io-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/agentage-io/rules/agentage-io-rules.yml
  title: ''
  type: Spectral
  url: rules/agentage-io-rules.yml
- group: design
  href: https://artifacts.apis.io/agentage-io/json-ld/agentage-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentage-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentage-io/vocabulary/agentage-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentage-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agentage-io/data-model/agentage-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentage-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/agentage-io/conventions/agentage-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agentage-io-conventions.yml
- group: auth
  href: https://artifacts.apis.io/agentage-io/authentication/agentage-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentage-io-authentication.yml
- group: auth
  href: https://artifacts.apis.io/agentage-io/scopes/agentage-io-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/agentage-io-scopes.yml
- group: operate
  href: https://artifacts.apis.io/agentage-io/lifecycle/agentage-io-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/agentage-io-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/agentage-io/lifecycle/agentage-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agentage-io-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/agentage-io/errors/agentage-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentage-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentage-io/conformance/agentage-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentage-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentage-io/llms/agentage-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentage-io-llms.txt
- group: build
  href: https://artifacts.apis.io/agentage-io/mcp/agentage-io-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agentage-io-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/agentage-io/mcp/agentage-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentage-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agentage-io/well-known/agentage-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentage-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentage-io/hosts/agentage-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentage-io-hosts.yml
- group: auth
  href: https://artifacts.apis.io/agentage-io/security/agentage-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentage-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentage.io/
- group: docs
  title: ''
  type: Documentation
  url: https://agentage.io/docs
- group: company
  title: ''
  type: Blog
  url: https://agentage.io/blog
- group: operate
  title: ''
  type: Support
  url: https://agentage.io/contacts
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentage.io/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentage.io/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agentage
- group: start
  title: ''
  type: GettingStarted
  url: https://agentage.io/docs
coverage:
  checked: '2026-10-30'
  detail: Docs provide a Base URL but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract.
  evidence:
  - status: 200
    url: https://docs.agentage.io/rest-api.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Agentage provides a shared markdown memory layer for AI assistants like Claude, ChatGPT, Cursor, and others. Users can store notes, decisions, and context in plain markdown, which is EU‑hosted, exportable, and portable across tools. The platform emphasizes privacy, open data formats, and avoids lock‑in, offering a collaborative memory that syncs across multiple AI interfaces without requiring API keys.
image: https://agentage.io/favicon.ico
json_schemas:
- name: GetV1MemoriesMemoryNotesPathResponse
  property_count: 7
  slug: agentage-io-get-v1-memories-memory-notes-path-response
- name: GetV1MemoriesMemoryNotesResponse
  property_count: 13
  slug: agentage-io-get-v1-memories-memory-notes-response
- name: GetV1MemoriesMemorySearchResponse
  property_count: 7
  slug: agentage-io-get-v1-memories-memory-search-response
- name: GetV1MemoriesResponse
  property_count: 1
  slug: agentage-io-get-v1-memories-response
- name: PatchV1MemoriesMemoryNotesPathRequest
  property_count: 5
  slug: agentage-io-patch-v1-memories-memory-notes-path-request
- name: PostV1MemoriesResponse
  property_count: 7
  slug: agentage-io-post-v1-memories-response
jsonld:
- class_count: 14
  name: Agentage Io Context
  property_count: 22
  slug: agentage-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at memory.agentage.io requiring OAuth.
  name: agentage-io MCP Server
  slug: agentage-io-mcp-yml
modified: '2026-10-29'
name: agentage-io
nav: Providers
network: true
overview: 'agentage-io is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Memory, Collaboration, and Privacy.


  The agentage-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  agentage-io''s developer surface includes authentication, documentation, engineering blog, support, getting-started guide, and 20 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: agentage-io API Rules
  rule_count: 14
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 0
  slug: agentage-io-rules
scopes:
- name: Agentage Io Scopes
  scope_count: 0
  slug: agentage-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 62.0
    catalog_earned_first_party: 0.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 19.7
    contract_quality: 26.1
    developer_ergonomics: 40.5
    discoverability: 65.0
    operational_transparency: 13.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: first-party
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
  name: Agentage Io Authentication
  slug: agentage-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agentage Io Domain Security
  slug: agentage-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agentage-io
tags:
- Company
- AI
- Memory
- Collaboration
- Privacy
- EU-Hosted
website: https://agentage.io/
---

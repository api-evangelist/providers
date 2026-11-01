---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: documented
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 62.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Ydb Qdrant Tech Agentic Access
  operation_count: 83
  slug: ydb-qdrant-tech-agentic-access
  summary_line: 83 operations · 26 acting
api_count: 3
apis:
- baseURL: https://gravity-ai.ydb-qdrant.tech
  baseurl_source: declared
  description: Interface generation and refinement.
  name: ydb-qdrant-tech Agent API
  slug: ydb-qdrant-tech-agent-api
- baseURL: https://ydb-qdrant.tech
  baseurl_source: declared
  description: Qdrant-compatible collection metadata operations
  name: ydb-qdrant-tech Collections API
  slug: ydb-qdrant-tech-collections-api
- baseURL: https://gravity-ai.ydb-qdrant.tech
  baseurl_source: declared
  description: Agent-readable discovery metadata.
  name: ydb-qdrant-tech Discovery API
  slug: ydb-qdrant-tech-discovery-api
- baseURL: https://gravity-ai.ydb-qdrant.tech
  baseurl_source: declared
  description: Publish liked generated interfaces.
  name: ydb-qdrant-tech Feedback API
  slug: ydb-qdrant-tech-feedback-api
- baseURL: https://gravity-ai.ydb-qdrant.tech
  baseurl_source: declared
  description: Streamable HTTP MCP transport.
  name: ydb-qdrant-tech MCP API
  slug: ydb-qdrant-tech-mcp-api
- baseURL: https://pets.ydb-qdrant.tech
  baseurl_source: declared
  description: Approved public Codex pet registry data.
  name: ydb-qdrant-tech Pets API
  slug: ydb-qdrant-tech-pets-api
- baseURL: https://ydb-qdrant.tech
  baseurl_source: declared
  description: Qdrant-compatible point retrieval, upsert, search, query, and delete operations
  name: ydb-qdrant-tech Points API
  slug: ydb-qdrant-tech-points-api
- baseURL: https://pets.ydb-qdrant.tech
  baseurl_source: declared
  description: Public pet generation request workflow.
  name: ydb-qdrant-tech Requests API
  slug: ydb-qdrant-tech-requests-api
- baseURL: https://ydb-qdrant.tech
  baseurl_source: declared
  description: Root and health endpoints
  name: ydb-qdrant-tech Service API
  slug: ydb-qdrant-tech-service-api
- baseURL: https://pets.ydb-qdrant.tech
  baseurl_source: declared
  description: Public pet pack submission workflow.
  name: ydb-qdrant-tech Submissions API
  slug: ydb-qdrant-tech-submissions-api
artifact_total: 38
common:
- group: agent
  href: https://artifacts.apis.io/ydb-qdrant-tech/agentic-access/ydb-qdrant-tech-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ydb-qdrant-tech-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/ydb-qdrant-tech/rules/ydb-qdrant-tech-rules.yml
  title: ''
  type: Spectral
  url: rules/ydb-qdrant-tech-rules.yml
- group: design
  href: https://artifacts.apis.io/ydb-qdrant-tech/json-ld/ydb-qdrant-tech-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ydb-qdrant-tech-context.jsonld
- group: design
  href: https://artifacts.apis.io/ydb-qdrant-tech/vocabulary/ydb-qdrant-tech-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ydb-qdrant-tech-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ydb-qdrant-tech/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ydb-qdrant-tech/data-model/ydb-qdrant-tech-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ydb-qdrant-tech-data-model.yml
- group: design
  href: https://artifacts.apis.io/ydb-qdrant-tech/conventions/ydb-qdrant-tech-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/ydb-qdrant-tech-conventions.yml
- group: design
  href: https://artifacts.apis.io/ydb-qdrant-tech/conventions/ydb-qdrant-tech-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ydb-qdrant-tech-conventions.yml
- group: auth
  href: https://artifacts.apis.io/ydb-qdrant-tech/authentication/ydb-qdrant-tech-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ydb-qdrant-tech-authentication.yml
- group: operate
  href: https://artifacts.apis.io/ydb-qdrant-tech/lifecycle/ydb-qdrant-tech-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/ydb-qdrant-tech-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://ydb-qdrant.tech/code-indexer/status/
- group: design
  href: https://artifacts.apis.io/ydb-qdrant-tech/lifecycle/ydb-qdrant-tech-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ydb-qdrant-tech-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/ydb-qdrant-tech/errors/ydb-qdrant-tech-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ydb-qdrant-tech-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ydb-qdrant-tech/conformance/ydb-qdrant-tech-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ydb-qdrant-tech-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ydb-qdrant-tech/llms/ydb-qdrant-tech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ydb-qdrant-tech-llms.txt
- group: other
  href: https://artifacts.apis.io/ydb-qdrant-tech/a2a/ydb-qdrant-tech-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/ydb-qdrant-tech-a2a.yml
- group: agent
  href: https://artifacts.apis.io/ydb-qdrant-tech/mcp/ydb-qdrant-tech-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ydb-qdrant-tech-mcp.yml
- group: agent
  href: https://artifacts.apis.io/ydb-qdrant-tech/well-known/ydb-qdrant-tech-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ydb-qdrant-tech-well-known.yml
- group: other
  href: https://artifacts.apis.io/ydb-qdrant-tech/hosts/ydb-qdrant-tech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ydb-qdrant-tech-hosts.yml
- group: build
  href: https://artifacts.apis.io/ydb-qdrant-tech/packages/ydb-qdrant-tech-packages.yml
  title: ''
  type: SDKs
  url: packages/ydb-qdrant-tech-packages.yml
- group: build
  href: https://artifacts.apis.io/ydb-qdrant-tech/packages/ydb-qdrant-tech-packages.yml
  title: ''
  type: Packages
  url: packages/ydb-qdrant-tech-packages.yml
- group: auth
  href: https://artifacts.apis.io/ydb-qdrant-tech/security/ydb-qdrant-tech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ydb-qdrant-tech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ydb-qdrant.tech/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ydb-qdrant.tech/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://ydb-qdrant.tech/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://ydb-qdrant.tech/openapi.json
- group: operate
  title: ''
  type: Support
  url: https://ydb-qdrant.tech/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ydb-qdrant.tech/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://ydb-qdrant.tech/pricing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/astandrik/ydb-qdrant
created: '2026-10-30'
description: YDB-Qdrant provides a Qdrant‑compatible vector search API built on YDB, offering exact top‑k search over a single‑table layout via a REST interface and a Node.js library. It enables developers to store and query high‑dimensional vectors without managing a separate vector database cluster, includes free self‑hosted packages, and integrates with YDB’s scalable storage. The service features open‑source SDKs, Docker images, and comprehensive documentation for quick integration.
image: https://ydb-qdrant.tech/assets/preview.png
json_schemas:
- name: AgentDiscovery
  property_count: 10
  slug: ydb-qdrant-tech-agent-discovery
- name: CreateGenerationRequestForm
  property_count: 6
  slug: ydb-qdrant-tech-create-generation-request-form
- name: CreateGenerationRequest
  property_count: 5
  slug: ydb-qdrant-tech-create-generation-request
- name: DeletePointsRequest
  property_count: 0
  slug: ydb-qdrant-tech-delete-points-request
- name: DesignFeedbackRequest
  property_count: 9
  slug: ydb-qdrant-tech-design-feedback-request
- name: McpServerCard
  property_count: 8
  slug: ydb-qdrant-tech-mcp-server-card
- name: McpWellKnownDocument
  property_count: 11
  slug: ydb-qdrant-tech-mcp-well-known-document
- name: OAuthAuthorizationServerMetadata
  property_count: 10
  slug: ydb-qdrant-tech-oauth-authorization-server-metadata
- name: OAuthProtectedResourceMetadata
  property_count: 8
  slug: ydb-qdrant-tech-oauth-protected-resource-metadata
- name: OpenIdConfiguration
  property_count: 0
  slug: ydb-qdrant-tech-open-id-configuration
- name: PetsResponse
  property_count: 3
  slug: ydb-qdrant-tech-pets-response
- name: QueryPointsEnvelope
  property_count: 0
  slug: ydb-qdrant-tech-query-points-envelope
- name: QueryPointsRequest
  property_count: 9
  slug: ydb-qdrant-tech-query-points-request
- name: RegisterSubmissionForm
  property_count: 9
  slug: ydb-qdrant-tech-register-submission-form
- name: RetrievePointsRequest
  property_count: 3
  slug: ydb-qdrant-tech-retrieve-points-request
- name: SearchPointsRequest
  property_count: 6
  slug: ydb-qdrant-tech-search-points-request
- name: TagsResponse
  property_count: 3
  slug: ydb-qdrant-tech-tags-response
- name: UpsertPointsRequest
  property_count: 1
  slug: ydb-qdrant-tech-upsert-points-request
jsonld:
- class_count: 45
  name: Ydb Qdrant Tech Context
  property_count: 135
  slug: ydb-qdrant-tech-context
layout: provider
mcp_servers:
- description: Remote MCP server at code-indexer.ydb-qdrant.tech.
  name: ydb-qdrant-tech MCP Server
  slug: ydb-qdrant-tech-mcp-yml
modified: '2026-10-30'
name: ydb-qdrant-tech
nav: Providers
network: true
overview: 'ydb-qdrant-tech publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, Collections API, Discovery API, and 7 more. Tagged areas include Company, Vector Search, Database, API, and YDB.


  The ydb-qdrant-tech catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ydb-qdrant-tech''s developer surface includes authentication, documentation, API reference, support, pricing, and 25 more developer resources.'
plans:
- name: Ydb Qdrant Tech Plans Pricing
  plan_count: 0
  slug: ydb-qdrant-tech-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Ydb Qdrant Tech Rate Limits
  slug: ydb-qdrant-tech-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: ydb-qdrant-tech API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 1
  slug: ydb-qdrant-tech-rules
scopes:
- name: Ydb Qdrant Tech Scopes
  scope_count: 0
  slug: ydb-qdrant-tech-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.5
  coverage:
    artifact_dirs: 29
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 61.2
    developer_ergonomics: 56.4
    discoverability: 70.0
    operational_transparency: 28.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ydb Qdrant Tech Authentication
  slug: ydb-qdrant-tech-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Ydb Qdrant Tech Domain Security
  slug: ydb-qdrant-tech-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: search-points
  slug: ydb-qdrant-tech-search-points
slug: ydb-qdrant-tech
tags:
- Company
- Vector Search
- Database
- API
- YDB
- Qdrant
website: https://ydb-qdrant.tech/
---

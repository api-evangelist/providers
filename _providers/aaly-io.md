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
  band: agent-ready
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Aaly REST API as documented in the provider's reference.
  name: Aaly REST API
  slug: aaly-rest-api
- baseURL: https://api.aaly.io
  baseurl_source: declared
  description: 'Aaly API as documented publicly: 12 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: Aaly API
  slug: aaly-io-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/aaly-io/rules/aaly-io-rules.yml
  title: ''
  type: Spectral
  url: rules/aaly-io-rules.yml
- group: design
  href: https://artifacts.apis.io/aaly-io/json-ld/aaly-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aaly-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/aaly-io/vocabulary/aaly-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aaly-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aaly-io/data-model/aaly-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aaly-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/aaly-io/changelog/aaly-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aaly-io-changelog.yml
- group: auth
  href: https://artifacts.apis.io/aaly-io/authentication/aaly-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aaly-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/aaly-io/errors/aaly-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aaly-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aaly-io/conformance/aaly-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aaly-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aaly-io/llms/aaly-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aaly-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/aaly-io/mcp/aaly-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aaly-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/aaly-io/well-known/aaly-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aaly-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/aaly-io/hosts/aaly-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aaly-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/aaly-io/vendors/aaly-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aaly-io-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.aaly.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://aaly.io/changelog
- group: auth
  href: https://artifacts.apis.io/aaly-io/security/aaly-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aaly-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aaly.io/
- group: docs
  title: ''
  type: Documentation
  url: https://aaly.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://aaly.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://aaly.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://aaly.io/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aaly.io/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.aaly.io?ref=nav_signup
coverage:
  checked: '2026-10-31'
  detail: REST API requires bearer token authentication; no public spec is available.
  evidence:
  - status: 200
    url: https://aaly.io/docs/rest-api
  reason: auth-required
  state: gated
created: '2026-10-31'
description: Aaly is a multi-tenant backend platform for AI‑built applications. It lets coding agents define data models—entities, fields, relationships and rules—and automatically serves a production REST API with built‑in authentication, validation, tenant isolation and OpenAPI spec generation. Features include Google sign‑in, rotating tokens, presigned uploads, server‑side Python functions, webhooks, and usage‑based pricing. The platform enforces isolation at the platform level, removing the need for row‑level security policies.
image: https://aaly.io/og-card.png
json_schemas:
- name: GetYourslugProjectTasksResponse
  property_count: 5
  slug: aaly-io-get-yourslug-project-tasks-response
- name: PostAuthChangePasswordRequest
  property_count: 2
  slug: aaly-io-post-auth-change-password-request
- name: PostAuthChangePasswordResponse
  property_count: 2
  slug: aaly-io-post-auth-change-password-response
- name: PostAuthRefreshResponse
  property_count: 2
  slug: aaly-io-post-auth-refresh-response
- name: PostFilesPresignedUrlRequest
  property_count: 3
  slug: aaly-io-post-files-presigned-url-request
- name: PostFilesPresignedUrlResponse
  property_count: 1
  slug: aaly-io-post-files-presigned-url-response
jsonld:
- class_count: 7
  name: Aaly Io Context
  property_count: 14
  slug: aaly-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.aaly.io.
  name: Aaly MCP Server
  slug: aaly-io-mcp-yml
modified: '2026-10-31'
name: Aaly
nav: Providers
network: true
overview: 'Aaly is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Backend, Multi-Tenant, Software-as-a-Service, and Platform.


  The Aaly catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Aaly''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, signup flow, and 16 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Aaly API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: aaly-io-rules
scopes:
- name: Aaly Io Scopes
  scope_count: 0
  slug: aaly-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 26.0
    developer_ergonomics: 31.0
    discoverability: 65.0
    operational_transparency: 7.9
  previous_composite: 36.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aaly Io Authentication
  slug: aaly-io-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Aaly Io Domain Security
  slug: aaly-io-domain-security
  summary_line: TLSv1.3
slug: aaly-io
tags:
- Artificial Intelligence
- Backend
- Multi-Tenant
- Software-as-a-Service
- Platform
website: https://aaly.io/
---

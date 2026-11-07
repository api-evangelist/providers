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
  band_gated_from: agent-native
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Agentsurface Dev Agentic Access
  operation_count: 2
  slug: agentsurface-dev-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- baseURL: https://agentsurface.dev
  baseurl_source: declared
  description: The Docs API from Agent Surface — 1 operation(s) for docs.
  name: Agent Surface Docs API
  slug: agentsurface-dev-docs-api
- baseURL: https://agentsurface.dev
  baseurl_source: declared
  description: The Md API from Agent Surface — 1 operation(s) for md.
  name: Agent Surface Md API
  slug: agentsurface-dev-md-api
artifact_total: 24
asyncapis:
- description: ''
  name: Agentsurface Dev Webhooks
  slug: agentsurface-dev-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/agentsurface-dev/agentic-access/agentsurface-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentsurface-dev-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agentsurface-dev/rules/agentsurface-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/agentsurface-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/agentsurface-dev/json-ld/agentsurface-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentsurface-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentsurface-dev/vocabulary/agentsurface-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentsurface-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agentsurface-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agentsurface-dev/data-model/agentsurface-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentsurface-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/agentsurface-dev/conventions/agentsurface-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agentsurface-dev-conventions.yml
- group: auth
  href: https://artifacts.apis.io/agentsurface-dev/authentication/agentsurface-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentsurface-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentsurface-dev/errors/agentsurface-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentsurface-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentsurface-dev/conformance/agentsurface-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentsurface-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentsurface-dev/llms/agentsurface-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentsurface-dev-llms.txt
- group: build
  href: https://artifacts.apis.io/agentsurface-dev/mcp/agentsurface-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agentsurface-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/agentsurface-dev/mcp/agentsurface-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentsurface-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agentsurface-dev/well-known/agentsurface-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentsurface-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentsurface-dev/hosts/agentsurface-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentsurface-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentsurface-dev/vendors/agentsurface-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentsurface-dev-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://agentsurface.dev/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/agentsurface-dev/security/agentsurface-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentsurface-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentsurface.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://agentsurface.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://agentsurface.dev/openapi.json
- group: operate
  title: ''
  type: Support
  url: https://agentsurface.dev/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentsurface.dev/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/howells/agentsurface
created: '2026-11-01'
description: 'A practical guide to agent-ready websites and apps. Explore discovery, understanding, connections, permissions, usability, reliability, payments, and measurement, with clear recommendations and detailed implementation docs. Help agents find your product, understand what it offers, and use it on a customer’s behalf. Explain what your product does and what its data means. Provide prices, terms, and limits. Offer direct ways agents work with your product: APIs, MCP servers, command-line tools, and SDKs.'
image: https://agentsurface.dev/og/Make%20software%20legible%20to%20agents
json_schemas:
- name: GetActionsResponse
  property_count: 6
  slug: agentsurface-dev-get-actions-response
- name: GetAskResponse
  property_count: 2
  slug: agentsurface-dev-get-ask-response
- name: GetDeploymentsDeploymentidResponse
  property_count: 3
  slug: agentsurface-dev-get-deployments-deploymentid-response
- name: GetV1FilesResponse
  property_count: 2
  slug: agentsurface-dev-get-v1-files-response
- name: PostDeploymentsResponse
  property_count: 3
  slug: agentsurface-dev-post-deployments-response
- name: PostOrdersRequest
  property_count: 3
  slug: agentsurface-dev-post-orders-request
- name: PostOrdersResponse
  property_count: 1
  slug: agentsurface-dev-post-orders-response
- name: PostResponsesRequest
  property_count: 4
  slug: agentsurface-dev-post-responses-request
- name: PostV1ChatCompletionsRequest
  property_count: 4
  slug: agentsurface-dev-post-v1-chat-completions-request
- name: PostV1ChatCompletionsResponse
  property_count: 4
  slug: agentsurface-dev-post-v1-chat-completions-response
- name: PostV1EvalsEvalidRunsRequest
  property_count: 2
  slug: agentsurface-dev-post-v1-evals-evalid-runs-request
- name: PostV1FilesResponse
  property_count: 9
  slug: agentsurface-dev-post-v1-files-response
- name: PostZonesZoneidDnsRecordsRequest
  property_count: 8
  slug: agentsurface-dev-post-zones-zoneid-dns-records-request
jsonld:
- class_count: 1
  name: Agentsurface Dev Context
  property_count: 11
  slug: agentsurface-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at agentsurface.dev.
  name: Agent Surface MCP Server
  slug: agentsurface-dev-mcp-yml
modified: '2026-11-01'
name: Agent Surface
nav: Providers
network: true
overview: 'Agent Surface publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Docs API and Md API. Tagged areas include Artificial Intelligence, Agents, Documentation, and Integration.


  The Agent Surface catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Agent Surface''s developer surface includes authentication, getting-started guide, documentation, API reference, support, and 19 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Agent Surface API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: agentsurface-dev-rules
scopes:
- name: Agentsurface Dev Scopes
  scope_count: 0
  slug: agentsurface-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 27
    catalog_earned: 45.8
    catalog_earned_first_party: 0.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 26.2
    developer_ergonomics: 35.0
    discoverability: 56.7
    operational_transparency: 2.6
  previous_composite: 30.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 40.0
      derived: 6
      marker_coverage: 75.0
      total: 8
    mcp: first-party
    skills: unknown
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
  name: Agentsurface Dev Authentication
  slug: agentsurface-dev-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Agentsurface Dev Domain Security
  slug: agentsurface-dev-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: surface
  slug: agentsurface-dev-surface
slug: agentsurface-dev
tags:
- Artificial Intelligence
- Agents
- Documentation
- Integration
website: https://agentsurface.dev/
---

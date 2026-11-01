---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: REST API for Apick services as documented in the developer guide.
  name: Apick API
  slug: apick-api
- description: 'apick-app API as documented publicly: 27 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: apick-app API
  slug: apick-app-api
artifact_total: 15
common:
- group: design
  href: https://artifacts.apis.io/apick-app/rules/apick-app-rules.yml
  title: ''
  type: Spectral
  url: rules/apick-app-rules.yml
- group: design
  href: https://artifacts.apis.io/apick-app/json-ld/apick-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apick-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/apick-app/vocabulary/apick-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apick-app-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/apick-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/apick-app/data-model/apick-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apick-app-data-model.yml
- group: auth
  href: https://artifacts.apis.io/apick-app/authentication/apick-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apick-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/apick-app/errors/apick-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apick-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/apick-app/conformance/apick-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apick-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apick-app/llms/apick-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apick-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/apick-app/mcp/apick-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/apick-app-mcp.yml
- group: other
  href: https://artifacts.apis.io/apick-app/hosts/apick-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apick-app-hosts.yml
- group: auth
  href: https://artifacts.apis.io/apick-app/security/apick-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apick-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apick.app/
- group: docs
  title: ''
  type: Documentation
  url: https://apick.app/dev_guide/start
- group: docs
  title: ''
  type: APIReference
  url: https://apick.app/dev_guide/start
- group: start
  title: ''
  type: GettingStarted
  url: https://apick.app/dev_guide/start
- group: operate
  title: ''
  type: Support
  url: https://apick.app/
- group: company
  title: ''
  type: Blog
  url: https://apick-api.tistory.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://apick.app/ai_llm_pricing
- group: start
  title: ''
  type: SignUp
  url: https://apick.app/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apick.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apick.app/personal_policy
coverage:
  checked: '2026-10-29'
  detail: The provider's documentation is public HTML but no OpenAPI/GraphQL/AsyncAPI spec is published.
  evidence:
  - status: 404
    url: https://apick.app/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Apick.app (에이픽) is a Korean API service platform that provides a wide range of REST APIs for identity verification, financial data, AI services, and more. Developers can obtain API keys, read detailed guides, and integrate services such as ID verification, account real‑name checks, business information lookup, AI large‑language‑model calls, image generation, and video processing. The platform offers a developer guide, pricing information, and a support contact point, and it publishes its terms of service and privacy policy.
image: https://apick.app/images/og/8a5edab282632443219e.png
json_schemas:
- name: GetRestLlmSessionsCreateResponse
  property_count: 2
  slug: apick-app-get-rest-llm-sessions-create-response
- name: GetRestLlmSessionsDeleteResponse
  property_count: 2
  slug: apick-app-get-rest-llm-sessions-delete-response
- name: GetRestLlmSessionsGetResponse
  property_count: 2
  slug: apick-app-get-rest-llm-sessions-get-response
- name: GetRestLlmSessionsListResponse
  property_count: 2
  slug: apick-app-get-rest-llm-sessions-list-response
- name: GetRestXPostResponse
  property_count: 2
  slug: apick-app-get-rest-xpost-response
- name: PostNasaStatusStatuidResponse
  property_count: 2
  slug: apick-app-post-nasa-status-statuid-response
jsonld:
- class_count: 20
  name: Apick App Context
  property_count: 6
  slug: apick-app-context
layout: provider
mcp_servers:
- description: Remote MCP server at apick.app.
  name: apick-app MCP Server
  slug: apick-app-mcp-yml
modified: '2026-10-29'
name: apick-app
nav: Providers
network: true
overview: 'apick-app is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API, Korean, Platform, Data, and Services.


  The apick-app catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  apick-app''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 15 more developer resources.'
random_paper: 22
rate_limits:
- limit_count: 0
  name: Apick App Rate Limits
  slug: apick-app-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: apick-app API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: apick-app-rules
scopes:
- name: Apick App Scopes
  scope_count: 0
  slug: apick-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 22.6
    developer_ergonomics: 54.0
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Apick App Authentication
  slug: apick-app-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Apick App Domain Security
  slug: apick-app-domain-security
  summary_line: TLSv1.3 · HSTS
slug: apick-app
tags:
- API
- Korean
- Platform
- Data
- Services
website: https://apick.app/
---

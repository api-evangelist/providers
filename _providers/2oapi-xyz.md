---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 2O provides a REST API for AI agents to request human verification of claims, facts, and real-world information.
  name: 2O API
  slug: 2o-api
- description: '2O API as documented publicly: 15 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: 2O API
  slug: 2oapi-xyz-api
artifact_total: 15
common:
- group: operate
  href: https://artifacts.apis.io/2oapi-xyz/rate-limits/2oapi-xyz-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/2oapi-xyz-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/2oapi-xyz/plans/2oapi-xyz-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/2oapi-xyz-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/2oapi-xyz/rules/2oapi-xyz-rules.yml
  title: ''
  type: Spectral
  url: rules/2oapi-xyz-rules.yml
- group: design
  href: https://artifacts.apis.io/2oapi-xyz/json-ld/2oapi-xyz-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/2oapi-xyz-context.jsonld
- group: design
  href: https://artifacts.apis.io/2oapi-xyz/vocabulary/2oapi-xyz-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/2oapi-xyz-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/2oapi-xyz/data-model/2oapi-xyz-data-model.yml
  title: ''
  type: DataModel
  url: data-model/2oapi-xyz-data-model.yml
- group: auth
  href: https://artifacts.apis.io/2oapi-xyz/authentication/2oapi-xyz-authentication.yml
  title: ''
  type: Authentication
  url: authentication/2oapi-xyz-authentication.yml
- group: design
  href: https://artifacts.apis.io/2oapi-xyz/conformance/2oapi-xyz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/2oapi-xyz-conformance.yml
- group: agent
  href: https://artifacts.apis.io/2oapi-xyz/llms/2oapi-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/2oapi-xyz-llms.txt
- group: other
  href: https://artifacts.apis.io/2oapi-xyz/a2a/2oapi-xyz-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/2oapi-xyz-a2a.yml
- group: build
  href: https://artifacts.apis.io/2oapi-xyz/mcp/2oapi-xyz-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/2oapi-xyz-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/2oapi-xyz/mcp/2oapi-xyz-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/2oapi-xyz-mcp.yml
- group: agent
  href: https://artifacts.apis.io/2oapi-xyz/well-known/2oapi-xyz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/2oapi-xyz-well-known.yml
- group: other
  href: https://artifacts.apis.io/2oapi-xyz/hosts/2oapi-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/2oapi-xyz-hosts.yml
- group: other
  href: https://artifacts.apis.io/2oapi-xyz/vendors/2oapi-xyz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/2oapi-xyz-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://www.2oapi.xyz/console
- group: auth
  href: https://artifacts.apis.io/2oapi-xyz/security/2oapi-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/2oapi-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://2oapi.xyz/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.2oapi.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://www.2oapi.xyz/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.2oapi.xyz/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.2oapi.xyz/integrate
- group: start
  title: ''
  type: SignUp
  url: https://www.2oapi.xyz/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.2oapi.xyz/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.2oapi.xyz/privacy
coverage:
  checked: '2026-10-31'
  detail: The provider's public documentation describes the API but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable spec is published.
  evidence:
  - status: 200
    url: https://www.2oapi.xyz/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: When your AI agent needs verification, it calls 2O. Human experts respond with structured, quality‑scored results. Programmatically. Identity, reputation, payments, and accountability for autonomous AI systems. The trust layer agents need to transact, verify, and collaborate.
image: https://www.2oapi.xyz/favicon.svg
json_schemas:
- name: GetV1VerifyIdResponse
  property_count: 9
  slug: 2oapi-xyz-get-v1-verify-id-response
- name: GetV1VerifyIdResultResponse
  property_count: 9
  slug: 2oapi-xyz-get-v1-verify-id-result-response
- name: PostApiV1VerifyResponse
  property_count: 8
  slug: 2oapi-xyz-post-api-v1-verify-response
- name: PostV1EmpathizeRequest
  property_count: 6
  slug: 2oapi-xyz-post-v1-empathize-request
- name: PostV1VerifyRequest
  property_count: 9
  slug: 2oapi-xyz-post-v1-verify-request
- name: PostV1WitnessRequest
  property_count: 6
  slug: 2oapi-xyz-post-v1-witness-request
jsonld:
- class_count: 15
  name: 2Oapi Xyz Context
  property_count: 38
  slug: 2oapi-xyz-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.2oapi.xyz requiring an API key.
  name: 2O MCP Server
  slug: 2oapi-xyz-mcp-yml
modified: '2026-10-31'
name: 2O
nav: Providers
network: true
overview: '2O is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Verification, Human-in-the-Loop, Trust, and Agents.


  The 2O catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  2O''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, signup flow, and 19 more developer resources.'
plans:
- name: 2Oapi Xyz Plans Pricing
  plan_count: 3
  slug: 2oapi-xyz-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: 2Oapi Xyz Rate Limits
  slug: 2oapi-xyz-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: 2O API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 1
  slug: 2oapi-xyz-rules
score:
  band: thin
  composite: 34.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 77.8
    catalog_earned_first_party: 20.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 48.7
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 34.5
    discoverability: 56.7
    operational_transparency: 21.1
  previous_composite: 42.9
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
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 2Oapi Xyz Authentication
  slug: 2oapi-xyz-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: 2Oapi Xyz Domain Security
  slug: 2oapi-xyz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 2oapi-xyz
tags:
- Artificial Intelligence
- Verification
- Human-in-the-Loop
- Trust
- Agents
website: https://2oapi.xyz/
---

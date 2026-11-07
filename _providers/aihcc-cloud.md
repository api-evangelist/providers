---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API documentation available at https://aihcc.cloud/docs
  name: AIHCC API
  slug: aihcc-api
- description: 'AIHCC API as documented publicly: 33 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AIHCC API
  slug: aihcc-cloud-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/aihcc-cloud/plans/aihcc-cloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aihcc-cloud-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aihcc-cloud/rules/aihcc-cloud-rules.yml
  title: ''
  type: Spectral
  url: rules/aihcc-cloud-rules.yml
- group: design
  href: https://artifacts.apis.io/aihcc-cloud/json-ld/aihcc-cloud-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aihcc-cloud-context.jsonld
- group: design
  href: https://artifacts.apis.io/aihcc-cloud/vocabulary/aihcc-cloud-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aihcc-cloud-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aihcc-cloud/data-model/aihcc-cloud-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aihcc-cloud-data-model.yml
- group: operate
  href: https://artifacts.apis.io/aihcc-cloud/changelog/aihcc-cloud-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aihcc-cloud-changelog.yml
- group: design
  href: https://artifacts.apis.io/aihcc-cloud/conformance/aihcc-cloud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aihcc-cloud-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aihcc-cloud/llms/aihcc-cloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aihcc-cloud-llms.txt
- group: agent
  href: https://artifacts.apis.io/aihcc-cloud/mcp/aihcc-cloud-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aihcc-cloud-mcp.yml
- group: agent
  href: https://artifacts.apis.io/aihcc-cloud/well-known/aihcc-cloud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aihcc-cloud-well-known.yml
- group: other
  href: https://artifacts.apis.io/aihcc-cloud/hosts/aihcc-cloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aihcc-cloud-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aihcc.cloud/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aihcc.cloud/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://aihcc.cloud/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://aihcc.cloud/news
- group: start
  title: ''
  type: Login
  url: https://aihcc.cloud/login
- group: docs
  title: ''
  type: Documentation
  url: https://aihcc.cloud/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://aihcc.cloud/changelog
- group: auth
  href: https://artifacts.apis.io/aihcc-cloud/security/aihcc-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aihcc-cloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aihcc.cloud/
coverage:
  checked: '2026-11-01'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://aihcc.cloud/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AIHCC, operated by Shenzhen LianShi Technology Co., Ltd., provides AI safety infrastructure for agents, offering hallucination detection, prompt injection protection, and full‑chain audit tools. Their platform includes products like HallucC Verify, Duet proactive agents, and CUA risk detection, serving developers, enterprises, and content creators with free and paid tiers. The service emphasizes reliable AI output verification, multi‑model cross‑validation, and compliance auditing, with detailed pricing, documentation, and support resources available on their website.
json_schemas:
- name: PostApiDetectRequest
  property_count: 4
  slug: aihcc-cloud-post-api-detect-request
- name: PostApiDetectResponse
  property_count: 7
  slug: aihcc-cloud-post-api-detect-response
- name: PostBatchRequest
  property_count: 5
  slug: aihcc-cloud-post-batch-request
- name: PostCuaAuditCodeRequest
  property_count: 4
  slug: aihcc-cloud-post-cua-audit-code-request
- name: PostDetectAgentRequest
  property_count: 6
  slug: aihcc-cloud-post-detect-agent-request
- name: PostDetectResponse
  property_count: 7
  slug: aihcc-cloud-post-detect-response
jsonld:
- class_count: 54
  name: Aihcc Cloud Context
  property_count: 82
  slug: aihcc-cloud-context
layout: provider
mcp_servers:
- description: Remote MCP server at aihcc.cloud.
  name: AIHCC MCP Server
  slug: aihcc-cloud-mcp-yml
modified: '2026-11-01'
name: AIHCC
nav: Providers
network: true
overview: 'AIHCC is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Safety, Agent Tools, Hallucination Detection, Prompt Injection, and Chinese.


  The AIHCC catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AIHCC''s developer surface includes changelog, pricing, documentation, and 17 more developer resources.'
plans:
- name: Aihcc Cloud Plans Pricing
  plan_count: 6
  slug: aihcc-cloud-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: AIHCC API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: aihcc-cloud-rules
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 67.8
    catalog_earned_first_party: 12.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.1
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 4.8
    discoverability: 54.2
    operational_transparency: 7.9
  previous_composite: 34.2
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
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aihcc Cloud Domain Security
  slug: aihcc-cloud-domain-security
  summary_line: TLSv1.3
slug: aihcc-cloud
tags:
- AI Safety
- Agent Tools
- Hallucination Detection
- Prompt Injection
- Chinese
website: https://aihcc.cloud/
---

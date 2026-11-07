---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Human-as-a-Service API for AI agents, enabling task delegation to human workers.
  name: NeedHuman AI API
  slug: needhuman-ai-api-2
- description: 'needhuman-ai API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: needhuman-ai API
  slug: needhuman-ai-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/needhuman-ai/rules/needhuman-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/needhuman-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/needhuman-ai/json-ld/needhuman-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/needhuman-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/needhuman-ai/vocabulary/needhuman-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/needhuman-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/needhuman-ai/data-model/needhuman-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/needhuman-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/needhuman-ai/security/needhuman-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/needhuman-ai-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/needhuman-ai/conformance/needhuman-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/needhuman-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/needhuman-ai/llms/needhuman-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/needhuman-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/needhuman-ai/well-known/needhuman-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/needhuman-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/needhuman-ai/well-known/needhuman-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/needhuman-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/needhuman-ai/hosts/needhuman-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/needhuman-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/needhuman-ai/vendors/needhuman-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/needhuman-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://needhuman.ai/terms
- group: auth
  href: https://artifacts.apis.io/needhuman-ai/security/needhuman-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/needhuman-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/needhuman-ai/security/needhuman-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/needhuman-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://needhuman.ai/
coverage:
  checked: '2026-10-31'
  detail: Provider only offers plain-text docs (llms.txt) with no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts.
  evidence:
  - status: 200
    url: https://needhuman.ai/llms.txt
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: NeedHuman AI provides Human-as-a-Service platform enabling AI agents to outsource tasks to human workers. The service offers an API for creating, listing, and managing tasks, with endpoints for registration, health checks, and tool integration. It aims to bridge the gap between automated AI processes and human expertise, supporting scalable human-in-the-loop workflows for diverse applications.
image: https://needhuman.ai/og.png
json_schemas:
- name: GetApiV1HealthResponse
  property_count: 2
  slug: needhuman-ai-get-api-v1-health-response
- name: GetApiV1TasksResponse
  property_count: 1
  slug: needhuman-ai-get-api-v1-tasks-response
- name: PatchApiV1TasksTaskidRequest
  property_count: 5
  slug: needhuman-ai-patch-api-v1-tasks-taskid-request
- name: PatchApiV1TasksTaskidResponse
  property_count: 14
  slug: needhuman-ai-patch-api-v1-tasks-taskid-response
- name: PostApiV1KeysRegisterResponse
  property_count: 3
  slug: needhuman-ai-post-api-v1-keys-register-response
- name: PostApiV1TasksResponse
  property_count: 12
  slug: needhuman-ai-post-api-v1-tasks-response
jsonld:
- class_count: 8
  name: Needhuman Ai Context
  property_count: 21
  slug: needhuman-ai-context
layout: provider
modified: '2026-10-30'
name: needhuman-ai
nav: Providers
network: true
overview: 'needhuman-ai is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Human-in-the-Loop, Platform, and Automation.


  The needhuman-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: needhuman-ai API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: needhuman-ai-rules
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 24.9
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 18.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/needhuman-ai/needhuman-ai-2026-11-03T140058.png
security:
- kind: domain-security
  name: Needhuman Ai Domain Security
  slug: needhuman-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Needhuman Ai Vulnerability Disclosure
  slug: needhuman-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: needhuman-ai
tags:
- Company
- Artificial Intelligence
- Human-in-the-Loop
- Platform
- Automation
website: https://needhuman.ai/
---

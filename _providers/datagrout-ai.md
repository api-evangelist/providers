---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for DataGrout platform, documented at the developer portal.
  name: DataGrout API
  slug: datagrout-api
- baseURL: https://gateway.datagrout.ai
  baseurl_source: declared
  description: 'DataGrout API as documented publicly: 21 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: DataGrout API
  slug: datagrout-ai-api
artifact_total: 13
asyncapis:
- description: ''
  name: Datagrout Ai Webhooks
  slug: datagrout-ai-webhooks
common:
- group: design
  href: https://artifacts.apis.io/datagrout-ai/rules/datagrout-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/datagrout-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/datagrout-ai/json-ld/datagrout-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/datagrout-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/datagrout-ai/vocabulary/datagrout-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/datagrout-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/datagrout-ai/asyncapi/datagrout-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/datagrout-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/datagrout-ai/data-model/datagrout-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/datagrout-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/datagrout-ai/authentication/datagrout-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/datagrout-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/datagrout-ai/conformance/datagrout-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datagrout-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/datagrout-ai/llms/datagrout-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datagrout-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/datagrout-ai/well-known/datagrout-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datagrout-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/datagrout-ai/hosts/datagrout-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datagrout-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/datagrout-ai/vendors/datagrout-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datagrout-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/datagrout-ai/packages/datagrout-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/datagrout-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/datagrout-ai/packages/datagrout-ai-packages.yml
  title: ''
  type: Packages
  url: packages/datagrout-ai-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.datagrout.ai/users/log-in
- group: start
  title: ''
  type: Sandbox
  url: https://library.datagrout.ai/sandbox
- group: commercial
  title: ''
  type: Pricing
  url: https://datagrout.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://api.datagrout.ai/users/log-in
- group: start
  title: ''
  type: DeveloperPortal
  url: https://datagrout.ai/roles/developer
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.datagrout.ai/quick-start
- group: docs
  title: ''
  type: Documentation
  url: https://docs.datagrout.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DataGrout
- group: auth
  href: https://artifacts.apis.io/datagrout-ai/security/datagrout-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datagrout-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datagrout.ai/
coverage:
  checked: '2026-11-05'
  detail: Docs site renders HTML shells and hides the OpenAPI spec behind a JavaScript UI.
  evidence:
  - status: 200
    url: https://docs.datagrout.ai/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: DataGrout provides AI agents with memory, reliability, and cost control. It offers a platform to connect to any system, remember across sessions, and run continuously without burning budgets. Built for production teams, it includes tools for data integration, prompt injection defense, and AI workflow automation, targeting enterprises across finance, healthcare, gaming, and more.
image: https://media.base44.com/images/public/68eadd766119b64d13710a59/cae7bbd53_YouTubeCoverImage1.png/v1/fill/w_1200,h_630/cae7bbd53_YouTubeCoverImage1.png
json_schemas:
- name: GetTasksTaskidResponse
  property_count: 5
  slug: datagrout-ai-get-tasks-taskid-response
- name: PostAnswersResponse
  property_count: 8
  slug: datagrout-ai-post-answers-response
- name: PostApiV1ServersUuidConclusionsRequest
  property_count: 3
  slug: datagrout-ai-post-api-v1-servers-uuid-conclusions-request
- name: PostConclusionsRequest
  property_count: 8
  slug: datagrout-ai-post-conclusions-request
- name: PostMemoriesNameRecallResponse
  property_count: 5
  slug: datagrout-ai-post-memories-name-recall-response
- name: PostTransformsResponse
  property_count: 5
  slug: datagrout-ai-post-transforms-response
jsonld:
- class_count: 26
  name: Datagrout Ai Context
  property_count: 38
  slug: datagrout-ai-context
layout: provider
modified: '2026-11-05'
name: DataGrout
nav: Providers
network: true
overview: 'DataGrout is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Enterprise, Platform, Memory, and Tools.


  The DataGrout catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  DataGrout''s developer surface includes authentication, sandbox, pricing, getting-started guide, documentation, and 18 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: DataGrout API Rules
  rule_count: 46
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 3
  slug: datagrout-ai-rules
score:
  band: thin
  composite: 37.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 33.9
    developer_ergonomics: 57.1
    discoverability: 57.1
    operational_transparency: 13.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Datagrout Ai Authentication
  slug: datagrout-ai-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Datagrout Ai Domain Security
  slug: datagrout-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: datagrout-ai
tags:
- Artificial Intelligence
- Enterprise
- Platform
- Memory
- Tools
website: https://datagrout.ai/
---

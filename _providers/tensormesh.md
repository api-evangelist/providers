---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.4
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: API for TensorMesh platform providing KV caching and deployment management for vLLM fleets.
  name: TensorMesh API
  slug: tensormesh-api-2
- baseURL: https://operator.tensormesh.ai
  baseurl_source: declared
  description: 'TensorMesh API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: TensorMesh API
  slug: tensormesh-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/tensormesh/rules/tensormesh-rules.yml
  title: ''
  type: Spectral
  url: rules/tensormesh-rules.yml
- group: design
  href: https://artifacts.apis.io/tensormesh/json-ld/tensormesh-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tensormesh-context.jsonld
- group: design
  href: https://artifacts.apis.io/tensormesh/vocabulary/tensormesh-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tensormesh-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/tensormesh/data-model/tensormesh-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tensormesh-data-model.yml
- group: build
  href: https://artifacts.apis.io/tensormesh/cli/tensormesh-cli.yml
  title: ''
  type: CLI
  url: cli/tensormesh-cli.yml
- group: operate
  href: https://artifacts.apis.io/tensormesh/changelog/tensormesh-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tensormesh-changelog.yml
- group: design
  href: https://artifacts.apis.io/tensormesh/conformance/tensormesh-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tensormesh-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tensormesh/llms/tensormesh-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tensormesh-llms.txt
- group: other
  href: https://artifacts.apis.io/tensormesh/a2a/tensormesh-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/tensormesh-a2a.yml
- group: agent
  href: https://artifacts.apis.io/tensormesh/well-known/tensormesh-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tensormesh-well-known.yml
- group: other
  href: https://artifacts.apis.io/tensormesh/hosts/tensormesh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tensormesh-hosts.yml
- group: other
  href: https://artifacts.apis.io/tensormesh/vendors/tensormesh-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tensormesh-vendors.yml
- group: build
  href: https://artifacts.apis.io/tensormesh/packages/tensormesh-packages.yml
  title: ''
  type: SDKs
  url: packages/tensormesh-packages.yml
- group: build
  href: https://artifacts.apis.io/tensormesh/packages/tensormesh-packages.yml
  title: ''
  type: Packages
  url: packages/tensormesh-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.tensormesh.ai/release-notes
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tensormesh.ai/v1.0.1/reference/cli
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tensormesh.ai/v1.0.1/installation/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tensormesh.ai/
- group: auth
  href: https://artifacts.apis.io/tensormesh/security/tensormesh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tensormesh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tensormesh.ai/
coverage:
  checked: '2026-10-19'
  detail: Documentation is available as markdown but no OpenAPI, GraphQL schema, or other machine-readable contract was found.
  evidence:
  - status: 200
    url: https://docs.tensormesh.ai/v1.0.1/introduction
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: TensorMesh provides a high-performance, scalable platform for building and deploying tensor-based computational meshes. Their services enable developers to create, visualize, and manage complex data structures for AI, scientific computing, and simulation workloads. The company focuses on delivering robust APIs, comprehensive documentation, and enterprise-grade security to support a wide range of applications across industries.
json_schemas:
- name: PostV1ChatCompletionsRequest
  property_count: 3
  slug: tensormesh-post-v1-chat-completions-request
jsonld:
- class_count: 1
  name: Tensormesh Context
  property_count: 3
  slug: tensormesh-context
layout: provider
modified: '2026-10-19'
name: TensorMesh
nav: Providers
network: true
overview: 'TensorMesh is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Data Processing, Cloud Platform, and Machine Learning.


  The TensorMesh catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TensorMesh''s developer surface includes CLI, changelog, API reference, getting-started guide, documentation, and 15 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: TensorMesh API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: tensormesh-rules
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 46.2
    catalog_earned_first_party: 0.0
    catalog_gap: 68.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 17.8
    developer_ergonomics: 42.9
    discoverability: 53.6
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Tensormesh Domain Security
  slug: tensormesh-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tensormesh
tags:
- Company
- Artificial Intelligence
- Data Processing
- Cloud Platform
- Machine Learning
website: https://tensormesh.ai/
---

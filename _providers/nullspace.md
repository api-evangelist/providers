---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.13-215-85-171.sslip.io
  baseurl_source: declared
  description: 'Nullspace API as documented publicly: 20 operations. Contract generated from the documentation by API Evangelist (2026-10-24); not the provider''s own document.'
  name: Nullspace API
  slug: nullspace-api
artifact_total: 13
asyncapis:
- description: ''
  name: Nullspace Webhooks
  slug: nullspace-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/nullspace/plans/nullspace-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nullspace-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/nullspace/rules/nullspace-rules.yml
  title: ''
  type: Spectral
  url: rules/nullspace-rules.yml
- group: design
  href: https://artifacts.apis.io/nullspace/json-ld/nullspace-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/nullspace-context.jsonld
- group: design
  href: https://artifacts.apis.io/nullspace/vocabulary/nullspace-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/nullspace-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/nullspace/asyncapi/nullspace-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/nullspace-webhooks.yml
- group: design
  href: https://artifacts.apis.io/nullspace/data-model/nullspace-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nullspace-data-model.yml
- group: operate
  href: https://artifacts.apis.io/nullspace/changelog/nullspace-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/nullspace-changelog.yml
- group: design
  href: https://artifacts.apis.io/nullspace/conventions/nullspace-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/nullspace-conventions.yml
- group: design
  href: https://artifacts.apis.io/nullspace/conventions/nullspace-conventions.yml
  title: ''
  type: Conventions
  url: conventions/nullspace-conventions.yml
- group: auth
  href: https://artifacts.apis.io/nullspace/authentication/nullspace-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nullspace-authentication.yml
- group: design
  href: https://artifacts.apis.io/nullspace/conformance/nullspace-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nullspace-conformance.yml
- group: agent
  href: https://artifacts.apis.io/nullspace/llms/nullspace-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nullspace-llms.txt
- group: other
  href: https://artifacts.apis.io/nullspace/a2a/nullspace-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/nullspace-a2a.yml
- group: other
  href: https://artifacts.apis.io/nullspace/hosts/nullspace-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nullspace-hosts.yml
- group: other
  href: https://artifacts.apis.io/nullspace/vendors/nullspace-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nullspace-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://ns.rocks/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ns.rocks/templates/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ns.rocks/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ns.rocks/api-reference
- group: auth
  href: https://artifacts.apis.io/nullspace/security/nullspace-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nullspace-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ns.rocks
coverage:
  checked: '2026-10-24'
  detail: The homepage renders a JavaScript SPA, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://ns.rocks
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: Nullspace provides cloud infrastructure that runs production AI agents such as LangGraph, Claude Agent SDK, CrewAI, or custom scripts on dedicated machines sized with the exact CPU, memory, GPU, and tools required. Developers deploy agents as callable functions that start on demand, execute in isolated environments, and shut down when finished, with built‑in observability and safety controls.
image: https://ns.rocks/og.svg
json_schemas:
- name: GetV1MachinesIdGitLogResponse
  property_count: 1
  slug: nullspace-get-v1-machines-id-git-log-response
- name: GetV1MachinesIdPtyResponse
  property_count: 5
  slug: nullspace-get-v1-machines-id-pty-response
- name: GetV1MachinesIdPtySidResponse
  property_count: 5
  slug: nullspace-get-v1-machines-id-pty-sid-response
- name: GetV1SnapshotsResponse
  property_count: 5
  slug: nullspace-get-v1-snapshots-response
- name: PostV1KeysIdRotateResponse
  property_count: 6
  slug: nullspace-post-v1-keys-id-rotate-response
- name: PostV1MachinesIdFilesInfoResponse
  property_count: 11
  slug: nullspace-post-v1-machines-id-files-info-response
jsonld:
- class_count: 14
  name: Nullspace Context
  property_count: 36
  slug: nullspace-context
layout: provider
modified: '2026-10-24'
name: Nullspace
nav: Providers
network: true
overview: 'Nullspace is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Infrastructure and AI Agents.


  The Nullspace catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Nullspace''s developer surface includes changelog, authentication, pricing, getting-started guide, documentation, API reference, and 15 more developer resources.'
plans:
- name: Nullspace Plans Pricing
  plan_count: 1
  slug: nullspace-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Nullspace API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: nullspace-rules
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 34.2
    developer_ergonomics: 40.5
    discoverability: 57.1
    operational_transparency: 23.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Nullspace Authentication
  slug: nullspace-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Nullspace Domain Security
  slug: nullspace-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nullspace
tags:
- Cloud Infrastructure
- AI Agents
website: https://ns.rocks
---

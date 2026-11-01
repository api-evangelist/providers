---
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
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: API for Subquadratic's AI decision models and platform services. Documentation is hosted at docs.subq.ai and the API is accessed via subq.ai endpoints.
  name: Subquadratic API
  slug: subquadratic-api
- baseURL: https://api.subq.ai
  baseurl_source: declared
  description: 'Subquadratic API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: Subquadratic API
  slug: subq-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/subq/rules/subq-rules.yml
  title: ''
  type: Spectral
  url: rules/subq-rules.yml
- group: design
  href: https://artifacts.apis.io/subq/json-ld/subq-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/subq-context.jsonld
- group: design
  href: https://artifacts.apis.io/subq/vocabulary/subq-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/subq-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/subq/data-model/subq-data-model.yml
  title: ''
  type: DataModel
  url: data-model/subq-data-model.yml
- group: auth
  href: https://artifacts.apis.io/subq/authentication/subq-authentication.yml
  title: ''
  type: Authentication
  url: authentication/subq-authentication.yml
- group: design
  href: https://artifacts.apis.io/subq/conformance/subq-conformance.yml
  title: ''
  type: Conformance
  url: conformance/subq-conformance.yml
- group: agent
  href: https://artifacts.apis.io/subq/llms/subq-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/subq-llms.txt
- group: other
  href: https://artifacts.apis.io/subq/hosts/subq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/subq-hosts.yml
- group: other
  href: https://artifacts.apis.io/subq/vendors/subq-vendors.yml
  title: ''
  type: Vendors
  url: vendors/subq-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.subq.ai/
- group: auth
  href: https://artifacts.apis.io/subq/security/subq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/subq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://subq.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.subq.ai/
- group: company
  title: ''
  type: Blog
  url: https://subq.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://subq.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://subq.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://subq.ai/privacy-policy
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://subq.ai/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: Subquadratic builds advanced AI decision models for enterprise workflows, offering the SubQ Snap long‑context multimodal model and SubQ Small language model. Their platform enables structured, high‑token decision making, integrates with enterprise tools, and provides APIs for developers to embed decision intelligence into applications. Founded by researchers and engineers, Subquadratic focuses on real‑world enterprise use cases with extensive context handling.
image: https://subq.ai/images/introducing-subq.png
json_schemas:
- name: DeleteV1FilesFileidResponse
  property_count: 3
  slug: subq-delete-v1-files-fileid-response
- name: GetV1FilesFileidResponse
  property_count: 8
  slug: subq-get-v1-files-fileid-response
- name: PostV1FilesResponse
  property_count: 3
  slug: subq-post-v1-files-response
- name: PostV1ResponsesResponse
  property_count: 5
  slug: subq-post-v1-responses-response
- name: PostV1SystemoneResponse
  property_count: 3
  slug: subq-post-v1-systemone-response
jsonld:
- class_count: 5
  name: Subq Context
  property_count: 17
  slug: subq-context
layout: provider
modified: '2026-10-18'
name: Subquadratic
nav: Providers
network: true
overview: 'Subquadratic is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Enterprise, Decision Models, and Long Context.


  The Subquadratic catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Subquadratic''s developer surface includes authentication, documentation, engineering blog, pricing, and 13 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Subquadratic API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: subq-rules
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 39.5
    contract_governance: 22.0
    contract_quality: 26.4
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Subq Authentication
  slug: subq-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Subq Domain Security
  slug: subq-domain-security
  summary_line: TLSv1.3 · DMARC
slug: subq
tags:
- Company
- Artificial Intelligence
- Enterprise
- Decision Models
- Long Context
website: https://subq.ai/
---

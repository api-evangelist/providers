---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Bilinc Cloud provides a RESTful API for verifiable memory operations, as documented in the Cloud API reference.
  name: Bilinc Cloud API
  slug: bilinc-cloud-api
- description: 'Bilinc API as documented publicly: 14 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: Bilinc API
  slug: bilinc-space-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/bilinc-space/plans/bilinc-space-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bilinc-space-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bilinc-space/rules/bilinc-space-rules.yml
  title: ''
  type: Spectral
  url: rules/bilinc-space-rules.yml
- group: design
  href: https://artifacts.apis.io/bilinc-space/json-ld/bilinc-space-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bilinc-space-context.jsonld
- group: design
  href: https://artifacts.apis.io/bilinc-space/vocabulary/bilinc-space-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bilinc-space-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bilinc-space/data-model/bilinc-space-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bilinc-space-data-model.yml
- group: build
  href: https://artifacts.apis.io/bilinc-space/cli/bilinc-space-cli.yml
  title: ''
  type: CLI
  url: cli/bilinc-space-cli.yml
- group: design
  href: https://artifacts.apis.io/bilinc-space/conventions/bilinc-space-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/bilinc-space-conventions.yml
- group: design
  href: https://artifacts.apis.io/bilinc-space/conventions/bilinc-space-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bilinc-space-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://bilinc.space/trust
- group: auth
  href: https://artifacts.apis.io/bilinc-space/authentication/bilinc-space-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bilinc-space-authentication.yml
- group: design
  href: https://artifacts.apis.io/bilinc-space/conformance/bilinc-space-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bilinc-space-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bilinc-space/llms/bilinc-space-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bilinc-space-llms.txt
- group: auth
  href: https://artifacts.apis.io/bilinc-space/well-known/bilinc-space-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bilinc-space-security.txt
- group: agent
  href: https://artifacts.apis.io/bilinc-space/well-known/bilinc-space-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bilinc-space-well-known.yml
- group: other
  href: https://artifacts.apis.io/bilinc-space/hosts/bilinc-space-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bilinc-space-hosts.yml
- group: other
  href: https://artifacts.apis.io/bilinc-space/vendors/bilinc-space-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bilinc-space-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://bilinc.space/trust
- group: operate
  title: ''
  type: StatusPage
  url: https://bilinc.space/status
- group: auth
  href: https://artifacts.apis.io/bilinc-space/security/bilinc-space-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bilinc-space-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bilinc-space/security/bilinc-space-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bilinc-space-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bilinc.space/
- group: docs
  title: ''
  type: Documentation
  url: https://bilinc.space/docs
- group: docs
  title: ''
  type: APIReference
  url: https://bilinc.space/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://bilinc.space/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://bilinc.space/support
- group: company
  title: ''
  type: Blog
  url: https://bilinc.space/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ReARCLabs
- group: operate
  title: ''
  type: Roadmap
  url: https://bilinc.space/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://bilinc.space/pricing
- group: start
  title: ''
  type: SignUp
  url: https://bilinc.space/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bilinc.space/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bilinc.space/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/rearclabs/workspace/bilinc/overview
coverage:
  checked: '2026-11-02'
  detail: Docs provide API reference but no OpenAPI/AsyncAPI/GraphQL spec is published.
  evidence:
  - status: 200
    url: https://bilinc.space/docs/api-reference.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Bilinc Cloud provides verifiable memory for AI agents, allowing them to store, recall, and audit changes over time. The platform offers free tier with 2,000 operations monthly, supports integration via MCP, and includes features like snapshots, rollbacks, and detailed audit trails. It targets developers using Claude, Cursor, Codex, and other AI agents, emphasizing transparency of data provenance and versioned memory.
image: https://bilinc.space/bilinc-og-dusk.jpg
json_schemas:
- name: PostApiCloudMemoryCommitRequest
  property_count: 5
  slug: bilinc-space-post-api-cloud-memory-commit-request
- name: PostApiCloudMemoryDiffRequest
  property_count: 3
  slug: bilinc-space-post-api-cloud-memory-diff-request
- name: PostApiCloudMemoryListRequest
  property_count: 5
  slug: bilinc-space-post-api-cloud-memory-list-request
- name: PostApiCloudMemoryRecallRequest
  property_count: 3
  slug: bilinc-space-post-api-cloud-memory-recall-request
- name: PostApiCloudMemoryReviseRequest
  property_count: 4
  slug: bilinc-space-post-api-cloud-memory-revise-request
- name: PostApiCloudMemoryRollbackRequest
  property_count: 3
  slug: bilinc-space-post-api-cloud-memory-rollback-request
jsonld:
- class_count: 11
  name: Bilinc Space Context
  property_count: 19
  slug: bilinc-space-context
layout: provider
modified: '2026-11-02'
name: Bilinc
nav: Providers
network: true
overview: 'Bilinc is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Memory, Platform, Developer Tools, and Cloud.


  The Bilinc catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bilinc''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 26 more developer resources.'
plans:
- name: Bilinc Space Plans Pricing
  plan_count: 5
  slug: bilinc-space-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: Bilinc API Rules
  rule_count: 39
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 1
  slug: bilinc-space-rules
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 57.9
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 39.3
    discoverability: 57.1
    operational_transparency: 18.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bilinc Space Authentication
  slug: bilinc-space-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bilinc Space Domain Security
  slug: bilinc-space-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bilinc Space Vulnerability Disclosure
  slug: bilinc-space-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bilinc-space
tags:
- Artificial Intelligence
- Memory
- Platform
- Developer Tools
- Cloud
website: https://bilinc.space/
---

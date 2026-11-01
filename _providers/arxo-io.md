---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Reference documentation for the Arxo Law platform.
  name: Arxo Law
  slug: arxo-law
- description: 'arxo-io API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: arxo-io API
  slug: arxo-io-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/arxo-io/rules/arxo-io-rules.yml
  title: ''
  type: Spectral
  url: rules/arxo-io-rules.yml
- group: design
  href: https://artifacts.apis.io/arxo-io/json-ld/arxo-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/arxo-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/arxo-io/vocabulary/arxo-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/arxo-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/arxo-io/data-model/arxo-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/arxo-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/arxo-io/errors/arxo-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/arxo-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/arxo-io/conformance/arxo-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arxo-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/arxo-io/llms/arxo-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arxo-io-llms.txt
- group: other
  href: https://artifacts.apis.io/arxo-io/hosts/arxo-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arxo-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/arxo-io/vendors/arxo-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arxo-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/arxo-io/packages/arxo-io-packages.yml
  title: ''
  type: SDKs
  url: packages/arxo-io-packages.yml
- group: build
  href: https://artifacts.apis.io/arxo-io/packages/arxo-io-packages.yml
  title: ''
  type: Packages
  url: packages/arxo-io-packages.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.arxo.io/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.arxo.io/guide/quickstart/
- group: auth
  href: https://artifacts.apis.io/arxo-io/security/arxo-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arxo-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arxo.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arxo.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.arxo.io/
- group: company
  title: ''
  type: Blog
  url: https://medium.com/@arxo
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/arxohq
coverage:
  checked: '2026-10-29'
  detail: Documentation is public but no machine‑readable OpenAPI/GraphQL/AsyncAPI contract is provided.
  evidence:
  - status: 200
    url: https://docs.arxo.io/reference/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Arxo provides Law as Code infrastructure, writing statutes and regulations as executable models that run on case facts and return answers with the underlying provisions. The platform enables applications and AI agents to query versioned legal models, see where official text does not apply, and publish findings to a public register after notifying responsible offices.
image: https://www.arxo.io/og.png
json_schemas:
- name: GetApiDeadlineCaptureResponse
  property_count: 11
  slug: arxo-io-get-api-deadline-capture-response
- name: PostApiDeadlineEvaluateRequest
  property_count: 3
  slug: arxo-io-post-api-deadline-evaluate-request
- name: PostApiDeadlineEvaluateResponse
  property_count: 4
  slug: arxo-io-post-api-deadline-evaluate-response
- name: PostApiDeadlineReplayResponse
  property_count: 2
  slug: arxo-io-post-api-deadline-replay-response
- name: PostMcpRequest
  property_count: 4
  slug: arxo-io-post-mcp-request
- name: PostMcpResponse
  property_count: 5
  slug: arxo-io-post-mcp-response
jsonld:
- class_count: 7
  name: Arxo Io Context
  property_count: 27
  slug: arxo-io-context
layout: provider
modified: '2026-10-29'
name: arxo-io
nav: Providers
network: true
overview: 'arxo-io is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, LawTech, LegalTech, RegTech, and AI.


  The arxo-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  arxo-io''s developer surface includes API reference, getting-started guide, documentation, engineering blog, and 15 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: arxo-io API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: arxo-io-rules
scopes:
- name: Arxo Io Scopes
  scope_count: 0
  slug: arxo-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 57.0
    catalog_earned_first_party: 0.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 19.7
    contract_quality: 23.5
    developer_ergonomics: 47.6
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arxo Io Authentication
  slug: arxo-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Arxo Io Domain Security
  slug: arxo-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arxo-io
tags:
- Company
- LawTech
- LegalTech
- RegTech
- AI
website: https://arxo.io/
---

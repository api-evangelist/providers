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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: GraphQL API for the compliance portal, providing access to audits, documents, subprocessor data, and related compliance information.
  name: Compliance GraphQL API
  slug: compliance-graphql
- baseURL: https://api.paperinstruments.com
  baseurl_source: declared
  description: 'Paper Instruments API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Paper Instruments API
  slug: paper-instruments-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/paper-instruments/rules/paper-instruments-rules.yml
  title: ''
  type: Spectral
  url: rules/paper-instruments-rules.yml
- group: design
  href: https://artifacts.apis.io/paper-instruments/json-ld/paper-instruments-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/paper-instruments-context.jsonld
- group: design
  href: https://artifacts.apis.io/paper-instruments/vocabulary/paper-instruments-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/paper-instruments-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/paper-instruments/data-model/paper-instruments-data-model.yml
  title: ''
  type: DataModel
  url: data-model/paper-instruments-data-model.yml
- group: design
  href: https://artifacts.apis.io/paper-instruments/conformance/paper-instruments-conformance.yml
  title: ''
  type: Conformance
  url: conformance/paper-instruments-conformance.yml
- group: agent
  href: https://artifacts.apis.io/paper-instruments/llms/paper-instruments-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/paper-instruments-llms.txt
- group: other
  href: https://artifacts.apis.io/paper-instruments/hosts/paper-instruments-hosts.yml
  title: ''
  type: Hosts
  url: hosts/paper-instruments-hosts.yml
- group: other
  href: https://artifacts.apis.io/paper-instruments/vendors/paper-instruments-vendors.yml
  title: ''
  type: Vendors
  url: vendors/paper-instruments-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.paperinstruments.com/docs/ultramarine
- group: auth
  href: https://artifacts.apis.io/paper-instruments/security/paper-instruments-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/paper-instruments-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://paperinstruments.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.paperinstruments.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.paperinstruments.com/
- group: company
  title: ''
  type: Blog
  url: https://www.paperinstruments.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.paperinstruments.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.paperinstruments.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/paper-instruments
created: '2026-10-29'
description: Paper Instruments provides frontier open‑source AI models for knowledge work, spanning finance, consulting, law, and operations. Their platform offers model libraries, Python SDKs, and tools that enable professionals to automate analysis, generate reports, and streamline decision‑making across multiple domains.
image: https://www.paperinstruments.com/favicon.svg
json_schemas:
- name: GetV1UsageResponse
  property_count: 2
  slug: paper-instruments-get-v1-usage-response
- name: PostV1ChatCompletionsRequest
  property_count: 25
  slug: paper-instruments-post-v1-chat-completions-request
- name: PostV1MessagesRequest
  property_count: 15
  slug: paper-instruments-post-v1-messages-request
- name: PostV1MessagesResponse
  property_count: 3
  slug: paper-instruments-post-v1-messages-response
- name: PostV1ResponsesRequest
  property_count: 17
  slug: paper-instruments-post-v1-responses-request
- name: PostV1ResponsesResponse
  property_count: 5
  slug: paper-instruments-post-v1-responses-response
jsonld:
- class_count: 8
  name: Paper Instruments Context
  property_count: 52
  slug: paper-instruments-context
layout: provider
modified: '2026-10-29'
name: Paper Instruments
nav: Providers
network: true
overview: 'Paper Instruments is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Open Source, Finance, Consulting, and Law.


  The Paper Instruments catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Paper Instruments'' developer surface includes getting-started guide, documentation, API reference, engineering blog, and 13 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Paper Instruments API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: paper-instruments-rules
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 26.0
    developer_ergonomics: 15.5
    discoverability: 73.2
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 27.2
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
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/paper-instruments/paper-instruments-2026-11-03T140922.png
security:
- kind: domain-security
  name: Paper Instruments Domain Security
  slug: paper-instruments-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: paper-instruments
tags:
- Artificial Intelligence
- Open Source
- Finance
- Consulting
- Law
website: https://paperinstruments.com
---

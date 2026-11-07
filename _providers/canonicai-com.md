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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
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
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Canonicai Com Agentic Access
  operation_count: 9
  slug: canonicai-com-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- baseURL: https://canonicai.com
  baseurl_source: declared
  description: The Answers API from CanonicAI — 5 operation(s) for answers.
  name: CanonicAI Answers API
  slug: canonicai-com-answers-api
- baseURL: https://canonicai.com
  baseurl_source: declared
  description: The Canons API from CanonicAI — 3 operation(s) for canons.
  name: CanonicAI Canons API
  slug: canonicai-com-canons-api
- baseURL: https://canonicai.com
  baseurl_source: declared
  description: The Llms.txt API from CanonicAI — 1 operation(s) for llms.txt.
  name: CanonicAI Llms.txt API
  slug: canonicai-com-llms-txt-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/canonicai-com/agentic-access/canonicai-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/canonicai-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/canonicai-com/rules/canonicai-com-rules.yml
  title: ''
  type: Spectral
  url: rules/canonicai-com-rules.yml
- group: design
  href: https://artifacts.apis.io/canonicai-com/json-ld/canonicai-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/canonicai-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/canonicai-com/vocabulary/canonicai-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/canonicai-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/canonicai-com/data-model/canonicai-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/canonicai-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/canonicai-com/errors/canonicai-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/canonicai-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/canonicai-com/conformance/canonicai-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/canonicai-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/canonicai-com/llms/canonicai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/canonicai-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/canonicai-com/well-known/canonicai-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/canonicai-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/canonicai-com/hosts/canonicai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/canonicai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/canonicai-com/vendors/canonicai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/canonicai-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://canonicai.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.canonicai.com/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.canonicai.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/canonicai-com/security/canonicai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canonicai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://canonicai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://canonicai.com/explainer
- group: operate
  title: ''
  type: Support
  url: https://canonicai.com/support
created: '2026-11-04'
description: CanonicAI provides an AI‑powered automated information extraction and tagging system that transforms unstructured knowledge—such as books, research papers, and domain documents—into canonical, queryable datasets with full provenance. The platform offers a production‑line style workflow with quality assurance, provenance tracking, and inventory control, enabling organizations to build reliable canonical data assets for analytics and AI applications.
image: https://canonicai.com/og-image.png
json_schemas:
- name: AnswerListResponse
  property_count: 2
  slug: canonicai-com-answer-list-response
- name: Answer
  property_count: 11
  slug: canonicai-com-answer
- name: AnswerSearchResponse
  property_count: 3
  slug: canonicai-com-answer-search-response
- name: AnswerSummary
  property_count: 6
  slug: canonicai-com-answer-summary
- name: CanonRecord
  property_count: 10
  slug: canonicai-com-canon-record
- name: ConstructSearchResponse
  property_count: 3
  slug: canonicai-com-construct-search-response
jsonld:
- class_count: 10
  name: Canonicai Com Context
  property_count: 37
  slug: canonicai-com-context
layout: provider
modified: '2026-11-04'
name: CanonicAI
nav: Providers
network: true
overview: 'CanonicAI publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Answers API, Canons API, and Llms.txt API. Tagged areas include Company, Artificial Intelligence, Data Extraction, Tagging, and CanonicalDatasets.


  The CanonicAI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CanonicAI''s developer surface includes getting-started guide, API reference, documentation, support, and 14 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: CanonicAI API Rules
  rule_count: 38
  severity_counts:
    error: 33
    hint: 0
    info: 4
    warn: 1
  slug: canonicai-com-rules
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 55.9
    developer_ergonomics: 16.7
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Canonicai Com Domain Security
  slug: canonicai-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: canonicai-com
tags:
- Company
- Artificial Intelligence
- Data Extraction
- Tagging
- CanonicalDatasets
- Automation
website: https://canonicai.com/
---

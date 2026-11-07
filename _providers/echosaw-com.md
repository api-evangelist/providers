---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Echosaw REST API provides endpoints for media analysis, status polling, result retrieval, and search as documented in the API Reference.
  name: Echosaw REST API
  slug: echosaw-rest-api
- baseURL: https://api.echosaw.com
  baseurl_source: declared
  description: 'Echosaw API as documented publicly: 12 operations. Contract generated from the documentation by API Evangelist (2026-11-06); not the provider''s own document.'
  name: Echosaw API
  slug: echosaw-com-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/echosaw-com/plans/echosaw-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/echosaw-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/echosaw-com/rules/echosaw-com-rules.yml
  title: ''
  type: Spectral
  url: rules/echosaw-com-rules.yml
- group: design
  href: https://artifacts.apis.io/echosaw-com/json-ld/echosaw-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/echosaw-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/echosaw-com/vocabulary/echosaw-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/echosaw-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/echosaw-com/data-model/echosaw-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/echosaw-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/echosaw-com/conformance/echosaw-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/echosaw-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/echosaw-com/llms/echosaw-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/echosaw-com-llms.txt
- group: other
  href: https://artifacts.apis.io/echosaw-com/hosts/echosaw-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/echosaw-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/echosaw-com/vendors/echosaw-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/echosaw-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://echosaw.com/login/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/matthew-b-simpson
- group: auth
  href: https://artifacts.apis.io/echosaw-com/security/echosaw-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/echosaw-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://echosaw.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://echosaw.com/developers/api-reference/
- group: docs
  title: ''
  type: Documentation
  url: https://echosaw.com/developers/api-reference/
- group: docs
  title: ''
  type: APIReference
  url: https://echosaw.com/developers/api-reference/
- group: commercial
  title: ''
  type: Pricing
  url: https://echosaw.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://echosaw.com/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://echosaw.com/legal/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://echosaw.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://echosaw.com/contact/
created: '2026-11-06'
description: Echosaw provides an AI video analyzer that watches video, audio, and documents, enabling users to ask questions, search transcripts, and receive timestamped key moments and study guides. The platform offers features such as video summarization, moderation, surveillance, and customizable rubrics, targeting academic and professional use cases.
image: https://echosaw.com/og-image.png
json_schemas:
- name: GetV1AnalysisResultsMediaidResponse
  property_count: 12
  slug: echosaw-com-get-v1-analysis-results-mediaid-response
- name: PatchV1MediaLibraryFolderRequest
  property_count: 2
  slug: echosaw-com-patch-v1-media-library-folder-request
- name: PatchV1MediaLibraryMoveRequest
  property_count: 2
  slug: echosaw-com-patch-v1-media-library-move-request
- name: PostV1AnalyzeUrlRequest
  property_count: 3
  slug: echosaw-com-post-v1-analyze-url-request
- name: PostV1MediaAskRequest
  property_count: 3
  slug: echosaw-com-post-v1-media-ask-request
- name: PostV1MediaLibraryFolderRequest
  property_count: 2
  slug: echosaw-com-post-v1-media-library-folder-request
jsonld:
- class_count: 14
  name: Echosaw Com Context
  property_count: 40
  slug: echosaw-com-context
layout: provider
modified: '2026-11-06'
name: Echosaw
nav: Providers
network: true
overview: 'Echosaw is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Video, Analyzer, Summarization, and Education.


  The Echosaw catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Echosaw''s developer surface includes documentation, API reference, pricing, engineering blog, support, and 16 more developer resources.'
plans:
- name: Echosaw Com Plans Pricing
  plan_count: 4
  slug: echosaw-com-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Echosaw API Rules
  rule_count: 48
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 1
  slug: echosaw-com-rules
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 26.1
    developer_ergonomics: 33.3
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Echosaw Com Domain Security
  slug: echosaw-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: echosaw-com
tags:
- Artificial Intelligence
- Video
- Analyzer
- Summarization
- Education
website: https://echosaw.com/
---

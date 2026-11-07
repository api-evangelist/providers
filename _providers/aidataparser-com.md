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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'AIDataParser API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AIDataParser API
  slug: aidataparser-com-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/aidataparser-com/rules/aidataparser-com-rules.yml
  title: ''
  type: Spectral
  url: rules/aidataparser-com-rules.yml
- group: design
  href: https://artifacts.apis.io/aidataparser-com/json-ld/aidataparser-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aidataparser-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/aidataparser-com/vocabulary/aidataparser-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aidataparser-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aidataparser-com/data-model/aidataparser-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aidataparser-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/aidataparser-com/conformance/aidataparser-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aidataparser-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aidataparser-com/llms/aidataparser-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aidataparser-com-llms.txt
- group: other
  href: https://artifacts.apis.io/aidataparser-com/hosts/aidataparser-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aidataparser-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aidataparser-com/vendors/aidataparser-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aidataparser-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aidataparser.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aidataparser.com/privacy
- group: auth
  href: https://artifacts.apis.io/aidataparser-com/security/aidataparser-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aidataparser-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aidataparser.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aidataparser.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://aidataparser.com/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://aidataparser.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://aidataparser.com/docs#quickstart
created: '2026-11-01'
description: AIDataParser provides a schema‑first data‑extraction API that turns messy PDFs and images into structured JSON for AI agents and developers. It offers credit‑based pricing, a free tier with 50 credits, and a quick‑start guide. The service emphasizes clean JSON output, confidence scoring, and easy integration via a simple POST request.
json_schemas:
- name: GetV1CreditsResponse
  property_count: 4
  slug: aidataparser-com-get-v1-credits-response
- name: PostV1McpRequest
  property_count: 4
  slug: aidataparser-com-post-v1-mcp-request
- name: PostV1ParseDocumentRequest
  property_count: 2
  slug: aidataparser-com-post-v1-parse-document-request
- name: PostV1ParseDocumentResponse
  property_count: 6
  slug: aidataparser-com-post-v1-parse-document-response
- name: PostV1ParseTextRequest
  property_count: 5
  slug: aidataparser-com-post-v1-parse-text-request
- name: PostV1ParseTextResponse
  property_count: 6
  slug: aidataparser-com-post-v1-parse-text-response
jsonld:
- class_count: 12
  name: Aidataparser Com Context
  property_count: 20
  slug: aidataparser-com-context
layout: provider
modified: '2026-11-01'
name: AIDataParser
nav: Providers
network: true
overview: 'AIDataParser is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Data Extraction, JSON, PDF, and Image Processing.


  The AIDataParser catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AIDataParser''s developer surface includes documentation, API reference, pricing, getting-started guide, and 12 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: AIDataParser API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: aidataparser-com-rules
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 25.0
    developer_ergonomics: 14.3
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 26.6
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
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aidataparser Com Domain Security
  slug: aidataparser-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aidataparser-com
tags:
- Artificial Intelligence
- Data Extraction
- JSON
- PDF
- Image Processing
website: https://aidataparser.com/
---

---
access_model:
  confidence: low
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
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'EasyData API as documented publicly: 23 operations. Contract generated from the documentation by API Evangelist (2026-11-06); not the provider''s own document.'
  name: EasyData API
  slug: easydata-cc-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/easydata-cc/rules/easydata-cc-rules.yml
  title: ''
  type: Spectral
  url: rules/easydata-cc-rules.yml
- group: design
  href: https://artifacts.apis.io/easydata-cc/json-ld/easydata-cc-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/easydata-cc-context.jsonld
- group: design
  href: https://artifacts.apis.io/easydata-cc/vocabulary/easydata-cc-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/easydata-cc-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/easydata-cc/data-model/easydata-cc-data-model.yml
  title: ''
  type: DataModel
  url: data-model/easydata-cc-data-model.yml
- group: auth
  href: https://artifacts.apis.io/easydata-cc/authentication/easydata-cc-authentication.yml
  title: ''
  type: Authentication
  url: authentication/easydata-cc-authentication.yml
- group: design
  href: https://artifacts.apis.io/easydata-cc/conformance/easydata-cc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/easydata-cc-conformance.yml
- group: agent
  href: https://artifacts.apis.io/easydata-cc/llms/easydata-cc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/easydata-cc-llms.txt
- group: agent
  href: https://artifacts.apis.io/easydata-cc/well-known/easydata-cc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/easydata-cc-well-known.yml
- group: other
  href: https://artifacts.apis.io/easydata-cc/hosts/easydata-cc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/easydata-cc-hosts.yml
- group: other
  href: https://artifacts.apis.io/easydata-cc/vendors/easydata-cc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/easydata-cc-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://easydata.cc/en/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://easydata.cc/en/support
- group: operate
  title: ''
  type: Roadmap
  url: https://easydata.cc/en/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://easydata.cc/en/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://easydata.cc/login
- group: auth
  href: https://artifacts.apis.io/easydata-cc/security/easydata-cc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/easydata-cc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://easydata.cc/
- group: docs
  title: ''
  type: Documentation
  url: https://easydata.cc/en/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://easydata.cc/en#pricing
- group: operate
  title: ''
  type: Changelog
  url: https://easydata.cc/en/changelog
- group: operate
  title: ''
  type: FAQ
  url: https://easydata.cc/en#faq
coverage:
  checked: '2026-11-06'
  detail: Documentation is a JavaScript‑rendered site with no machine‑readable OpenAPI spec discovered.
  evidence:
  - status: 200
    url: https://easydata.cc/en/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-06'
description: Organize, connect, and analyze your data with EasyData. An AI‑assisted data management platform for spreadsheets, everyday tracking, and team records. It helps you build connected records, offers AI‑generated schemas, and supports export to Excel, CSV, JSON, or Google Sheets.
image: https://easydata.cc/twitter-card.png
json_schemas:
- name: PatchApiPublicV1NamedSchemasSchemaidRecordsRequest
  property_count: 1
  slug: easydata-cc-patch-api-public-v1-named-schemas-schemaid-records-request
- name: PostApiPublicV1CreditPurchasesRequest
  property_count: 2
  slug: easydata-cc-post-api-public-v1-credit-purchases-request
- name: PostApiPublicV1CreditPurchasesResponse
  property_count: 1
  slug: easydata-cc-post-api-public-v1-credit-purchases-response
- name: PostApiPublicV1NamedSchemasSchemaidRecordsQueryRequest
  property_count: 2
  slug: easydata-cc-post-api-public-v1-named-schemas-schemaid-records-query-request
- name: PostApiPublicV1NamedSchemasSchemaidRecordsRequest
  property_count: 1
  slug: easydata-cc-post-api-public-v1-named-schemas-schemaid-records-request
- name: PostApiPublicV1SchemasRequest
  property_count: 1
  slug: easydata-cc-post-api-public-v1-schemas-request
jsonld:
- class_count: 6
  name: Easydata Cc Context
  property_count: 7
  slug: easydata-cc-context
layout: provider
modified: '2026-11-06'
name: EasyData
nav: Providers
network: true
overview: 'EasyData is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data Management, Artificial Intelligence, Spreadsheets, Collaboration, and Software-as-a-Service.


  The EasyData catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  EasyData''s developer surface includes authentication, support, documentation, pricing, changelog, FAQ, and 15 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: EasyData API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: easydata-cc-rules
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 21.9
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 5.3
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
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Easydata Cc Authentication
  slug: easydata-cc-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Easydata Cc Domain Security
  slug: easydata-cc-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: easydata-cc
tags:
- Data Management
- Artificial Intelligence
- Spreadsheets
- Collaboration
- Software-as-a-Service
website: https://easydata.cc/
---

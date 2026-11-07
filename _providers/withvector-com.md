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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.withvector.com
  baseurl_source: declared
  description: 'Vector API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: Vector API
  slug: withvector-com-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/withvector-com/rules/withvector-com-rules.yml
  title: ''
  type: Spectral
  url: rules/withvector-com-rules.yml
- group: design
  href: https://artifacts.apis.io/withvector-com/json-ld/withvector-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/withvector-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/withvector-com/vocabulary/withvector-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/withvector-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/withvector-com/data-model/withvector-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/withvector-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/withvector-com/conformance/withvector-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/withvector-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/withvector-com/llms/withvector-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/withvector-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/withvector-com/well-known/withvector-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/withvector-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/withvector-com/hosts/withvector-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/withvector-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/withvector-com/vendors/withvector-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/withvector-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.withvector.com/terms-service/
- group: operate
  title: ''
  type: Support
  url: https://support.withvector.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.withvector.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.withvector.com/press/
- group: company
  title: ''
  type: Blog
  url: https://www.withvector.com/blog/
- group: auth
  href: https://artifacts.apis.io/withvector-com/security/withvector-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/withvector-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://withvector.com
created: '2026-10-21'
description: Vector is a venture‑backed technology company focused on building data‑driven platforms for enterprises. Backed by 8vc, Vector aims to simplify complex workflows with scalable APIs and developer tools, serving a growing customer base across multiple industries.
image: https://www.withvector.com/wp-content/uploads/2025/10/og-homepage.jpg
json_schemas:
- name: Get10EntitiesRecordsUniqueidResponse
  property_count: 14
  slug: withvector-com-get10-entities-records-uniqueid-response
- name: Post10EntitiesActionsIngestionBolIngestRequest
  property_count: 2
  slug: withvector-com-post10-entities-actions-ingestion-bol-ingest-request
- name: Post10EntitiesActionsIngestionBolIngestResponse
  property_count: 2
  slug: withvector-com-post10-entities-actions-ingestion-bol-ingest-response
- name: Post10EntitiesQueryRequest
  property_count: 3
  slug: withvector-com-post10-entities-query-request
- name: Post10EntitiesQueryResponse
  property_count: 2
  slug: withvector-com-post10-entities-query-response
- name: Post10EntitiesRecordsRequest
  property_count: 1
  slug: withvector-com-post10-entities-records-request
jsonld:
- class_count: 7
  name: Withvector Com Context
  property_count: 21
  slug: withvector-com-context
layout: provider
modified: '2026-10-21'
name: Vector
nav: Providers
network: true
overview: 'Vector is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Platform, and Enterprise.


  The Vector catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Vector''s developer surface includes support, engineering blog, and 14 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Vector API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: withvector-com-rules
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 26.2
    developer_ergonomics: 3.6
    discoverability: 65.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 23.0
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
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/withvector-com/withvector-com-2026-11-03T150220.png
security:
- kind: domain-security
  name: Withvector Com Domain Security
  slug: withvector-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: withvector-com
tags:
- Company
- Data
- Platform
- Enterprise
website: https://withvector.com
---

---
agent_readiness:
  band: agent-aware
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.4
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Arcwise provides an AI‑powered analytics platform that detects metric shifts early and explains them with hallucination‑free, traceable insights linked to your data and documentation.
  name: Arcwise API
  slug: arcwise-api-2
- description: 'Arcwise API as documented publicly: 18 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Arcwise API
  slug: arcwise-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/arcwise/rules/arcwise-rules.yml
  title: ''
  type: Spectral
  url: rules/arcwise-rules.yml
- group: design
  href: https://artifacts.apis.io/arcwise/json-ld/arcwise-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/arcwise-context.jsonld
- group: design
  href: https://artifacts.apis.io/arcwise/vocabulary/arcwise-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/arcwise-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/arcwise/data-model/arcwise-data-model.yml
  title: ''
  type: DataModel
  url: data-model/arcwise-data-model.yml
- group: operate
  href: https://artifacts.apis.io/arcwise/changelog/arcwise-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/arcwise-changelog.yml
- group: design
  href: https://artifacts.apis.io/arcwise/conformance/arcwise-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arcwise-conformance.yml
- group: agent
  href: https://artifacts.apis.io/arcwise/llms/arcwise-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arcwise-llms.txt
- group: other
  href: https://artifacts.apis.io/arcwise/a2a/arcwise-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/arcwise-a2a.yml
- group: agent
  href: https://artifacts.apis.io/arcwise/well-known/arcwise-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arcwise-well-known.yml
- group: other
  href: https://artifacts.apis.io/arcwise/hosts/arcwise-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arcwise-hosts.yml
- group: other
  href: https://artifacts.apis.io/arcwise/vendors/arcwise-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arcwise-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arcwise.app/terms-free
- group: auth
  title: ''
  type: Security
  url: https://arcwise.app/security
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.arcwise.app/arcwise-setup
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arcwise.app/
- group: auth
  href: https://artifacts.apis.io/arcwise/security/arcwise-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arcwise-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arcwise.app
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arcwise.app/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sql.arcwise.app/
coverage:
  checked: '2026-10-29'
  detail: Public documentation exists but no machine‑readable OpenAPI/GraphQL/AsyncAPI spec was found.
  evidence:
  - status: 404
    url: https://api.arcwise.app/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Arcwise provides an AI-powered analytics platform that detects metric shifts early and explains them with hallucination‑free, traceable insights linked to your data and documentation. Teams can make informed decisions quickly, leveraging real‑time explanations of why metrics moved, improving operational efficiency and strategic planning.
image: https://cdn.prod.website-files.com/695faa4e2ada6fec687076cc/696a49a8ecb2e28da38df5a5_image%20fill.svg
json_schemas:
- name: GetCubejsApiV1DataSourcesResponse
  property_count: 1
  slug: arcwise-get-cubejs-api-v1-data-sources-response
- name: GetCubejsApiV1EntitiesOrdersResponse
  property_count: 11
  slug: arcwise-get-cubejs-api-v1-entities-orders-response
- name: PostCubejsApiV1ConvertQueryResponse
  property_count: 2
  slug: arcwise-post-cubejs-api-v1-convert-query-response
- name: PostCubejsApiV1LoadResponse
  property_count: 5
  slug: arcwise-post-cubejs-api-v1-load-response
- name: PostCubejsApiV1PreAggregationsJobsRequest
  property_count: 2
  slug: arcwise-post-cubejs-api-v1-pre-aggregations-jobs-request
- name: PostCubejsApiV1SqlFiltersResponse
  property_count: 7
  slug: arcwise-post-cubejs-api-v1-sql-filters-response
jsonld:
- class_count: 11
  name: Arcwise Context
  property_count: 25
  slug: arcwise-context
layout: provider
modified: '2026-10-28'
name: Arcwise
nav: Providers
network: true
overview: 'Arcwise is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Metrics, Analytics, and Decision-Making.


  The Arcwise catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Arcwise''s developer surface includes changelog, getting-started guide, documentation, and 16 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 0
  name: Arcwise Rate Limits
  slug: arcwise-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Arcwise API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: arcwise-rules
scopes:
- name: Arcwise Scopes
  scope_count: 0
  slug: arcwise-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 27
    catalog_earned: 57.0
    catalog_earned_first_party: 0.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 19.7
    contract_quality: 24.9
    developer_ergonomics: 31.0
    discoverability: 57.1
    operational_transparency: 26.3
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
    score: 26.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arcwise Authentication
  slug: arcwise-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Arcwise Domain Security
  slug: arcwise-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: arcwise
tags:
- Company
- AI
- Metrics
- Analytics
- Decision-Making
website: https://arcwise.app
---

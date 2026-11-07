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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Provides programmatic access to clearance search records and related data.
  name: Clearances Search Engine API
  slug: clearances-search-engine-api
- description: 'CASE API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: CASE API
  slug: clearancesearchengine-com-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/clearancesearchengine-com/rules/clearancesearchengine-com-rules.yml
  title: ''
  type: Spectral
  url: rules/clearancesearchengine-com-rules.yml
- group: design
  href: https://artifacts.apis.io/clearancesearchengine-com/json-ld/clearancesearchengine-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clearancesearchengine-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/clearancesearchengine-com/vocabulary/clearancesearchengine-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clearancesearchengine-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/clearancesearchengine-com/data-model/clearancesearchengine-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clearancesearchengine-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/clearancesearchengine-com/conformance/clearancesearchengine-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clearancesearchengine-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/clearancesearchengine-com/llms/clearancesearchengine-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clearancesearchengine-com-llms.txt
- group: other
  href: https://artifacts.apis.io/clearancesearchengine-com/hosts/clearancesearchengine-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clearancesearchengine-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/clearancesearchengine-com/vendors/clearancesearchengine-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clearancesearchengine-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clearancesearchengine.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clearancesearchengine.com/privacy
- group: start
  title: ''
  type: Login
  url: https://www.clearancesearchengine.com/sign-in
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.clearancesearchengine.com/developers
- group: auth
  href: https://artifacts.apis.io/clearancesearchengine-com/security/clearancesearchengine-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clearancesearchengine-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clearancesearchengine.com/
coverage:
  checked: '2026-11-04'
  detail: Developer portal provides only HTML docs with no OpenAPI or other machine-readable contract.
  evidence:
  - status: 200
    url: https://www.clearancessearchengine.com/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: CASE (Clearance Adjudication Search Engine) provides a searchable knowledge base of Department of Homeland Security (DOHA) security clearance decisions dating back to 1996. Users can query outcomes, view statistics, and access citations for over 30,000 public clearance records. The platform offers descriptive analysis without predictions, supporting researchers, employers, and individuals seeking transparent clearance information.
image: https://www.clearancesearchengine.com/icon-512.png
json_schemas:
- name: GetApiV1CandorResponse
  property_count: 2
  slug: clearancesearchengine-com-get-api-v1-candor-response
- name: GetApiV1CasesIdResponse
  property_count: 2
  slug: clearancesearchengine-com-get-api-v1-cases-id-response
- name: GetApiV1RecencyResponse
  property_count: 3
  slug: clearancesearchengine-com-get-api-v1-recency-response
- name: GetApiV1StatsResponse
  property_count: 3
  slug: clearancesearchengine-com-get-api-v1-stats-response
jsonld:
- class_count: 4
  name: Clearancesearchengine Com Context
  property_count: 3
  slug: clearancesearchengine-com-context
layout: provider
modified: '2026-11-03'
name: CASE
nav: Providers
network: true
overview: 'CASE is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Security Clearance, Legal Research, and Knowledge Base.


  The CASE catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: CASE API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: clearancesearchengine-com-rules
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 46.8
    catalog_earned_first_party: 0.0
    catalog_gap: 68.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 20.1
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clearancesearchengine Com Domain Security
  slug: clearancesearchengine-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clearancesearchengine-com
tags:
- Security Clearance
- Legal Research
- Knowledge Base
website: https://clearancesearchengine.com/
---

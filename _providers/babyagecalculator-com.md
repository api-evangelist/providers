---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    auth_clarity: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Free JSON API providing baby age, zodiac, birthstone, milestones without API key.
  name: Baby Age Calculator API
  slug: baby-age-calculator-api
- description: 'Baby Age Calculator API as documented publicly: 21 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: Baby Age Calculator API
  slug: babyagecalculator-com-api
artifact_total: 16
common:
- group: design
  href: https://artifacts.apis.io/babyagecalculator-com/rules/babyagecalculator-com-rules.yml
  title: ''
  type: Spectral
  url: rules/babyagecalculator-com-rules.yml
- group: design
  href: https://artifacts.apis.io/babyagecalculator-com/json-ld/babyagecalculator-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/babyagecalculator-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/babyagecalculator-com/vocabulary/babyagecalculator-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/babyagecalculator-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/babyagecalculator-com/data-model/babyagecalculator-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/babyagecalculator-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/babyagecalculator-com/conformance/babyagecalculator-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/babyagecalculator-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/babyagecalculator-com/llms/babyagecalculator-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/babyagecalculator-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/babyagecalculator-com/mcp/babyagecalculator-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/babyagecalculator-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/babyagecalculator-com/hosts/babyagecalculator-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/babyagecalculator-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/babyagecalculator-com/vendors/babyagecalculator-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/babyagecalculator-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/babyagecalculator-com/security/babyagecalculator-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/babyagecalculator-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://babyagecalculator.com/
- group: docs
  title: ''
  type: Documentation
  url: https://babyagecalculator.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://babyagecalculator.com/docs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://babyagecalculator.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://babyagecalculator.com/privacy/
created: '2026-11-02'
description: Baby Age Calculator is a free online tool that accurately calculates a baby's exact age in years, months, weeks, and days, and provides related milestones, zodiac signs, and birthstone guides. Built with precise mathematical calculations, it supports leap years and varying month lengths, helping parents and caregivers track developmental milestones and plan pediatric appointments. The service also offers a JSON API for developers and AI tools, delivering the same data without requiring an API key or sign‑up.
image: https://babyagecalculator.com/logo.png
json_schemas:
- name: GetApiAgeCalculateResponse
  property_count: 8
  slug: babyagecalculator-com-get-api-age-calculate-response
- name: GetApiAgeResponse
  property_count: 8
  slug: babyagecalculator-com-get-api-age-response
- name: GetApiAgeResponse2
  property_count: 12
  slug: babyagecalculator-com-get-api-age-response2
- name: GetApiBirthstonesMonthGetResponse
  property_count: 22
  slug: babyagecalculator-com-get-api-birthstones-month-get-response
- name: GetApiMilestonesListResponse
  property_count: 9
  slug: babyagecalculator-com-get-api-milestones-list-response
- name: GetApiZodiacResponse2
  property_count: 9
  slug: babyagecalculator-com-get-api-zodiac-response2
jsonld:
- class_count: 20
  name: Babyagecalculator Com Context
  property_count: 47
  slug: babyagecalculator-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at babyagecalculator.com.
  name: Baby Age Calculator MCP Server
  slug: babyagecalculator-com-mcp-yml
modified: '2026-11-02'
name: Baby Age Calculator
nav: Providers
network: true
overview: 'Baby Age Calculator is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Baby, age, Calculator, Parenting, and Health.


  The Baby Age Calculator catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Baby Age Calculator''s developer surface includes documentation, API reference, and 13 more developer resources.'
plans:
- name: Babyagecalculator Com Plans Pricing
  plan_count: 0
  slug: babyagecalculator-com-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Babyagecalculator Com Rate Limits
  slug: babyagecalculator-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 73
  extends:
  - spectral:oas
  name: Baby Age Calculator API Rules
  rule_count: 32
  severity_counts:
    error: 29
    hint: 0
    info: 1
    warn: 2
  slug: babyagecalculator-com-rules
scopes:
- name: Babyagecalculator Com Scopes
  scope_count: 0
  slug: babyagecalculator-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.3
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 22.8
    developer_ergonomics: 8.3
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 24.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Babyagecalculator Com Authentication
  slug: babyagecalculator-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Babyagecalculator Com Domain Security
  slug: babyagecalculator-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: babyagecalculator-com
tags:
- Baby
- age
- Calculator
- Parenting
- Health
- Milestones
website: https://babyagecalculator.com/
---

---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
  score: 22.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Carbon intelligence API converting transactions, activities, flights, shipments, and EU CBAM imports into verified CO₂e numbers.
  name: MyCO2 Suite API
  slug: myco2-suite-api
- description: 'myco2suite-io API as documented publicly: 14 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: myco2suite-io API
  slug: myco2suite-io-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/myco2suite-io/plans/myco2suite-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/myco2suite-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/myco2suite-io/rules/myco2suite-io-rules.yml
  title: ''
  type: Spectral
  url: rules/myco2suite-io-rules.yml
- group: design
  href: https://artifacts.apis.io/myco2suite-io/json-ld/myco2suite-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/myco2suite-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/myco2suite-io/vocabulary/myco2suite-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/myco2suite-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/myco2suite-io/data-model/myco2suite-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/myco2suite-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/myco2suite-io/conformance/myco2suite-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/myco2suite-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/myco2suite-io/llms/myco2suite-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/myco2suite-io-llms.txt
- group: other
  href: https://artifacts.apis.io/myco2suite-io/a2a/myco2suite-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/myco2suite-io-a2a.yml
- group: other
  href: https://artifacts.apis.io/myco2suite-io/hosts/myco2suite-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/myco2suite-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/myco2suite-io/vendors/myco2suite-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/myco2suite-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/myco2suite-io/security/myco2suite-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/myco2suite-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://myco2suite.io/
- group: docs
  title: ''
  type: Documentation
  url: https://myco2suite.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://app.myco2suite.io/login
- group: commercial
  title: ''
  type: Pricing
  url: https://myco2suite.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://myco2suite.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://myco2suite.io/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.myco2suite.io/login
- group: start
  title: ''
  type: Login
  url: https://app.myco2suite.io/login
coverage:
  checked: '2026-10-30'
  detail: Documentation exists but no OpenAPI, AsyncAPI, GraphQL, or other contract was found.
  evidence:
  - status: 404
    url: https://api.myco2suite.io/openapi.json
  - status: 404
    url: https://api.myco2suite.io/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: MyCO2 Suite provides a carbon intelligence API that converts transactions, activities, flights, shipments, and EU CBAM imports into verified CO₂e numbers in a single call. It offers 223,850 licensed factors across 200+ countries, supports Scope 1·2·3, and is payable per call via x402 on Base with a free tier of 1,000 calls/month.
json_schemas:
- name: GetV1FactorResponse
  property_count: 9
  slug: myco2suite-io-get-v1-factor-response
- name: PostV1CbamRequest
  property_count: 8
  slug: myco2suite-io-post-v1-cbam-request
- name: PostV1FlightResponse
  property_count: 10
  slug: myco2suite-io-post-v1-flight-response
- name: PostV1FreightResponse
  property_count: 10
  slug: myco2suite-io-post-v1-freight-response
- name: PostV1TransactionRequest
  property_count: 14
  slug: myco2suite-io-post-v1-transaction-request
- name: PostV1TransactionResponse
  property_count: 10
  slug: myco2suite-io-post-v1-transaction-response
jsonld:
- class_count: 19
  name: Myco2Suite Io Context
  property_count: 60
  slug: myco2suite-io-context
layout: provider
modified: '2026-10-30'
name: myco2suite-io
nav: Providers
network: true
overview: 'myco2suite-io is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Carbon, Climate, Sustainability, and Data.


  The myco2suite-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  myco2suite-io''s developer surface includes documentation, getting-started guide, pricing, signup flow, and 15 more developer resources.'
plans:
- name: Myco2Suite Io Plans Pricing
  plan_count: 6
  slug: myco2suite-io-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: myco2suite-io API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: myco2suite-io-rules
score:
  band: emerging
  composite: 26.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 62.8
    catalog_earned_first_party: 12.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.1
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 10.7
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 34.2
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
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/myco2suite-io/myco2suite-io-2026-11-03T135931.png
security:
- kind: domain-security
  name: Myco2Suite Io Domain Security
  slug: myco2suite-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: myco2suite-io
tags:
- Carbon
- Climate
- Sustainability
- Data
website: https://myco2suite.io/
---

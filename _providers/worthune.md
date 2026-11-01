---
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
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Worthune API as documented publicly: 22 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: Worthune API
  slug: worthune-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/worthune/plans/worthune-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/worthune-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/worthune/rules/worthune-rules.yml
  title: ''
  type: Spectral
  url: rules/worthune-rules.yml
- group: design
  href: https://artifacts.apis.io/worthune/json-ld/worthune-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/worthune-context.jsonld
- group: design
  href: https://artifacts.apis.io/worthune/vocabulary/worthune-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/worthune-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/worthune/data-model/worthune-data-model.yml
  title: ''
  type: DataModel
  url: data-model/worthune-data-model.yml
- group: auth
  href: https://artifacts.apis.io/worthune/authentication/worthune-authentication.yml
  title: ''
  type: Authentication
  url: authentication/worthune-authentication.yml
- group: design
  href: https://artifacts.apis.io/worthune/conformance/worthune-conformance.yml
  title: ''
  type: Conformance
  url: conformance/worthune-conformance.yml
- group: agent
  href: https://artifacts.apis.io/worthune/llms/worthune-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/worthune-llms.txt
- group: other
  href: https://artifacts.apis.io/worthune/hosts/worthune-hosts.yml
  title: ''
  type: Hosts
  url: hosts/worthune-hosts.yml
- group: other
  href: https://artifacts.apis.io/worthune/vendors/worthune-vendors.yml
  title: ''
  type: Vendors
  url: vendors/worthune-vendors.yml
- group: build
  href: https://artifacts.apis.io/worthune/packages/worthune-packages.yml
  title: ''
  type: SDKs
  url: packages/worthune-packages.yml
- group: build
  href: https://artifacts.apis.io/worthune/packages/worthune-packages.yml
  title: ''
  type: Packages
  url: packages/worthune-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://worthune.com/terms
- group: operate
  title: ''
  type: Support
  url: https://worthune.com/help
- group: start
  title: ''
  type: Sandbox
  url: https://worthune.com/console
- group: operate
  title: ''
  type: Roadmap
  url: https://worthune.com/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://worthune.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://worthune.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://worthune.com/models/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://worthune.com/docs
- group: auth
  href: https://artifacts.apis.io/worthune/security/worthune-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/worthune-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://worthune.com/
created: '2026-10-19'
description: Worthune provides a unified household management platform offering headless financial planning APIs. It delivers verified calculators, a full planning engine, and wealth‑tech infrastructure via a single REST API that can be white‑labeled. Models include tax calculations, retirement projections, and asset management, each with versioned specifications and evidence records.
image: https://worthune.com/api/og/scenarios/fire
json_schemas:
- name: GetApiV1ProjectExamplesRetiredCoupleSpousalResponse
  property_count: 1
  slug: worthune-get-api-v1-project-examples-retired-couple-spousal-response
- name: GetApiV1ProjectResponse
  property_count: 1
  slug: worthune-get-api-v1-project-response
- name: PostApiV1HouseholdsIdDecisionsRequest
  property_count: 1
  slug: worthune-post-api-v1-households-id-decisions-request
- name: PostApiV1VerifyEmergencyFundRequest
  property_count: 2
  slug: worthune-post-api-v1-verify-emergency-fund-request
jsonld:
- class_count: 4
  name: Worthune Context
  property_count: 5
  slug: worthune-context
layout: provider
modified: '2026-10-19'
name: Worthune
nav: Providers
network: true
overview: 'Worthune is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, WealthTech, and Platform.


  The Worthune catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Worthune''s developer surface includes authentication, support, sandbox, pricing, changelog, API reference, and 16 more developer resources.'
plans:
- name: Worthune Plans Pricing
  plan_count: 4
  slug: worthune-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Worthune API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: worthune-rules
score:
  band: thin
  composite: 36.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 58.0
    catalog_earned_first_party: 12.0
    catalog_gap: 57.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 19.7
    contract_quality: 20.1
    developer_ergonomics: 38.1
    discoverability: 48.2
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 13
      marker_coverage: 100.0
      total: 13
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Worthune Authentication
  slug: worthune-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Worthune Domain Security
  slug: worthune-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: worthune
tags:
- Company
- Finance
- WealthTech
- Platform
website: https://worthune.com/
---

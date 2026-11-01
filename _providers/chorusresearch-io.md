---
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Programmatically create surveys, launch them to targeted audiences, and export responses.
  name: Chorus Research REST API
  slug: chorus-research-rest-api
- baseURL: https://api.chorusresearch.io
  baseurl_source: declared
  description: 'chorusresearch-io API as documented publicly: 12 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: chorusresearch-io API
  slug: chorusresearch-io-api
artifact_total: 15
common:
- group: operate
  href: https://artifacts.apis.io/chorusresearch-io/rate-limits/chorusresearch-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/chorusresearch-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/chorusresearch-io/plans/chorusresearch-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chorusresearch-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/chorusresearch-io/rules/chorusresearch-io-rules.yml
  title: ''
  type: Spectral
  url: rules/chorusresearch-io-rules.yml
- group: design
  href: https://artifacts.apis.io/chorusresearch-io/json-ld/chorusresearch-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/chorusresearch-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/chorusresearch-io/vocabulary/chorusresearch-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chorusresearch-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/chorusresearch-io/data-model/chorusresearch-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/chorusresearch-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/chorusresearch-io/conventions/chorusresearch-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/chorusresearch-io-conventions.yml
- group: auth
  href: https://artifacts.apis.io/chorusresearch-io/authentication/chorusresearch-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chorusresearch-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/chorusresearch-io/errors/chorusresearch-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/chorusresearch-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/chorusresearch-io/conformance/chorusresearch-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chorusresearch-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/chorusresearch-io/llms/chorusresearch-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chorusresearch-io-llms.txt
- group: other
  href: https://artifacts.apis.io/chorusresearch-io/hosts/chorusresearch-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chorusresearch-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/chorusresearch-io/vendors/chorusresearch-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chorusresearch-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chorusresearch.io/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chorusresearch.io/legal/privacy
- group: auth
  href: https://artifacts.apis.io/chorusresearch-io/security/chorusresearch-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chorusresearch-io-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://chorusresearch.io/docs/guide
- group: docs
  title: ''
  type: APIReference
  url: https://chorusresearch.io/docs/api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.chorusresearch.io
- group: start
  title: ''
  type: GettingStarted
  url: https://chorusresearch.io/docs/guide
- group: company
  title: ''
  type: Blog
  url: https://chorusresearch.io/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.chorusresearch.io
- group: company
  title: ''
  type: Website
  url: https://chorusresearch.io/
coverage:
  checked: '2026-10-30'
  detail: OpenAPI spec at https://api.chorusresearch.io/openapi.json returns 401 Unauthorized, indicating the contract is behind authentication.
  evidence:
  - status: 401
    url: https://api.chorusresearch.io/openapi.json
  reason: auth-required
  state: gated
created: '2026-10-30'
description: Chorus Research is an AI-native survey platform that enables users to create surveys via a conversational AI assistant, launch them to real respondents, and retrieve automated analysis. It provides a Machine-Readable Control Protocol (MCP) and a REST API for programmatic integration, as well as a web app for manual operation, streamlining research workflows for businesses and developers.
image: https://chorusresearch.io/og-default.png
json_schemas:
- name: GetAudiencesIdResponse
  property_count: 9
  slug: chorusresearch-io-get-audiences-id-response
- name: GetSurveysIdResponse
  property_count: 8
  slug: chorusresearch-io-get-surveys-id-response
- name: GetSurveysIdStatusResponse
  property_count: 8
  slug: chorusresearch-io-get-surveys-id-status-response
- name: PostPricingEstimateRequest
  property_count: 3
  slug: chorusresearch-io-post-pricing-estimate-request
- name: PostSurveysIdLaunchConfirmResponse
  property_count: 7
  slug: chorusresearch-io-post-surveys-id-launch-confirm-response
- name: PostSurveysRequest
  property_count: 4
  slug: chorusresearch-io-post-surveys-request
jsonld:
- class_count: 16
  name: Chorusresearch Io Context
  property_count: 42
  slug: chorusresearch-io-context
layout: provider
modified: '2026-10-30'
name: chorusresearch-io
nav: Providers
network: true
overview: 'chorusresearch-io is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Survey, AI, Research, and MCP.


  The chorusresearch-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  chorusresearch-io''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, signup flow, and 17 more developer resources.'
plans:
- name: Chorusresearch Io Plans Pricing
  plan_count: 1
  slug: chorusresearch-io-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Chorusresearch Io Rate Limits
  slug: chorusresearch-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: chorusresearch-io API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: chorusresearch-io-rules
scopes:
- name: Chorusresearch Io Scopes
  scope_count: 0
  slug: chorusresearch-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 56.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 92.1
    catalog_earned_first_party: 0.0
    catalog_gap: 22.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.2
    contract_governance: 79.1
    contract_quality: 55.6
    developer_ergonomics: 52.4
    discoverability: 66.1
    operational_transparency: 18.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Chorusresearch Io Authentication
  slug: chorusresearch-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Chorusresearch Io Domain Security
  slug: chorusresearch-io-domain-security
  summary_line: TLSv1.3 · HSTS
slug: chorusresearch-io
tags:
- Company
- Survey
- AI
- Research
- MCP
- API
- Automation
website: https://chorusresearch.io/
---

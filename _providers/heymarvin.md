---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    idempotency: verified
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
  score: 43.7
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: API for importing audio, video, documents, and images into Marvin, and managing projects, files, and CSV imports.
  name: HeyMarvin API
  slug: heymarvin-api-2
- baseURL: https://app.heymarvin.com
  baseurl_source: declared
  description: 'HeyMarvin API as documented publicly: 16 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: HeyMarvin API
  slug: heymarvin-api
artifact_total: 16
common:
- group: operate
  href: https://artifacts.apis.io/heymarvin/rate-limits/heymarvin-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/heymarvin-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/heymarvin/plans/heymarvin-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/heymarvin-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/heymarvin/rules/heymarvin-rules.yml
  title: ''
  type: Spectral
  url: rules/heymarvin-rules.yml
- group: design
  href: https://artifacts.apis.io/heymarvin/json-ld/heymarvin-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/heymarvin-context.jsonld
- group: design
  href: https://artifacts.apis.io/heymarvin/vocabulary/heymarvin-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/heymarvin-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/heymarvin/data-model/heymarvin-data-model.yml
  title: ''
  type: DataModel
  url: data-model/heymarvin-data-model.yml
- group: design
  href: https://artifacts.apis.io/heymarvin/conventions/heymarvin-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/heymarvin-conventions.yml
- group: design
  href: https://artifacts.apis.io/heymarvin/conventions/heymarvin-conventions.yml
  title: ''
  type: Conventions
  url: conventions/heymarvin-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://heymarvin.com/security
- group: auth
  href: https://artifacts.apis.io/heymarvin/authentication/heymarvin-authentication.yml
  title: ''
  type: Authentication
  url: authentication/heymarvin-authentication.yml
- group: auth
  href: https://artifacts.apis.io/heymarvin/scopes/heymarvin-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/heymarvin-scopes.yml
- group: design
  href: https://artifacts.apis.io/heymarvin/conformance/heymarvin-conformance.yml
  title: ''
  type: Conformance
  url: conformance/heymarvin-conformance.yml
- group: agent
  href: https://artifacts.apis.io/heymarvin/llms/heymarvin-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/heymarvin-llms.txt
- group: auth
  href: https://artifacts.apis.io/heymarvin/well-known/heymarvin-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/heymarvin-help-security.txt
- group: agent
  href: https://artifacts.apis.io/heymarvin/well-known/heymarvin-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/heymarvin-well-known.yml
- group: other
  href: https://artifacts.apis.io/heymarvin/hosts/heymarvin-hosts.yml
  title: ''
  type: Hosts
  url: hosts/heymarvin-hosts.yml
- group: other
  href: https://artifacts.apis.io/heymarvin/vendors/heymarvin-vendors.yml
  title: ''
  type: Vendors
  url: vendors/heymarvin-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.heymarvin.com/
- group: auth
  title: ''
  type: Security
  url: https://heymarvin.com/security
- group: auth
  href: https://artifacts.apis.io/heymarvin/security/heymarvin-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/heymarvin-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/heymarvin/security/heymarvin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/heymarvin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://heymarvin.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://heymarvin.com/mcp/
- group: docs
  title: ''
  type: Documentation
  url: https://heymarvin.com/mcp/
- group: docs
  title: ''
  type: APIReference
  url: https://heymarvin.com/mcp/
- group: start
  title: ''
  type: GettingStarted
  url: https://heymarvin.com/demo/get-demo/
- group: operate
  title: ''
  type: Support
  url: https://help.heymarvin.com/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://heymarvin.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://heymarvin.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://heymarvin.com/privacy/
- group: start
  title: ''
  type: SignUp
  url: https://app.heymarvin.com/accounts/signup/
coverage:
  checked: '2026-10-28'
  detail: Public documentation pages list API endpoints but no machine‑readable OpenAPI/AsyncAPI/GraphQL spec is available.
  evidence:
  - status: 200
    url: https://docs.heymarvin.com/reference/files
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: HeyMarvin provides an AI‑native platform that aggregates customer feedback and insights into a centralized repository, enabling organizations to access, analyze, and act on 360° customer knowledge across products and services. The service offers searchable data, integration capabilities, and tools for research, product design, and marketing teams.
image: https://cdn.prod.website-files.com/69413b330f3775fbe4358643_Brand%20White%20Logo.svg
json_schemas:
- name: GetApiV1DeveloperImportFilesResponse
  property_count: 4
  slug: heymarvin-get-api-v1-developer-import-files-response
- name: GetApiV1DeveloperImportFilesWavkeyStatusResponse
  property_count: 5
  slug: heymarvin-get-api-v1-developer-import-files-wavkey-status-response
- name: GetApiV1DeveloperImportSurveysUploadkeyStatusResponse
  property_count: 11
  slug: heymarvin-get-api-v1-developer-import-surveys-uploadkey-status-response
- name: PostApiV1DeveloperImportFilesInitializeResponse
  property_count: 4
  slug: heymarvin-post-api-v1-developer-import-files-initialize-response
- name: PostApiV1DeveloperImportSurveysInitializeRequest
  property_count: 9
  slug: heymarvin-post-api-v1-developer-import-surveys-initialize-request
- name: PostBucketResponse
  property_count: 4
  slug: heymarvin-post-bucket-response
jsonld:
- class_count: 19
  name: Heymarvin Context
  property_count: 36
  slug: heymarvin-context
layout: provider
modified: '2026-10-28'
name: HeyMarvin
nav: Providers
network: true
overview: 'HeyMarvin is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI, CustomerInsights, Analytics, SaaS, and Platform.


  The HeyMarvin catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  HeyMarvin''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Heymarvin Plans Pricing
  plan_count: 4
  slug: heymarvin-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Heymarvin Rate Limits
  slug: heymarvin-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: HeyMarvin API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: heymarvin-rules
scopes:
- name: Heymarvin Scopes
  scope_count: 6
  slug: heymarvin-scopes
  summary_line: 6 scopes
score:
  band: strong
  composite: 55.2
  coverage:
    artifact_dirs: 24
    catalog_earned: 77.8
    catalog_earned_first_party: 20.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 35.6
    contract_quality: 26.1
    developer_ergonomics: 54.8
    discoverability: 57.1
    operational_transparency: 47.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Heymarvin Authentication
  slug: heymarvin-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Heymarvin Domain Security
  slug: heymarvin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Heymarvin Trust Center
  slug: heymarvin-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: heymarvin
tags:
- AI
- CustomerInsights
- Analytics
- SaaS
- Platform
website: https://heymarvin.com/
---

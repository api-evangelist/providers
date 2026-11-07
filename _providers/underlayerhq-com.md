---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  - sandbox
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
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: REST API for Underlayer's embedded training platform.
  name: Underlayer API
  slug: underlayer-api
- description: 'underlayerhq-com API as documented publicly: 61 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: underlayerhq-com API
  slug: underlayerhq-com-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/underlayerhq-com/plans/underlayerhq-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/underlayerhq-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/underlayerhq-com/rules/underlayerhq-com-rules.yml
  title: ''
  type: Spectral
  url: rules/underlayerhq-com-rules.yml
- group: design
  href: https://artifacts.apis.io/underlayerhq-com/json-ld/underlayerhq-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/underlayerhq-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/underlayerhq-com/vocabulary/underlayerhq-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/underlayerhq-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/underlayerhq-com/data-model/underlayerhq-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/underlayerhq-com-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://underlayerhq.com/security
- group: design
  href: https://artifacts.apis.io/underlayerhq-com/conformance/underlayerhq-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/underlayerhq-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/underlayerhq-com/llms/underlayerhq-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/underlayerhq-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/underlayerhq-com/well-known/underlayerhq-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/underlayerhq-com-security.txt
- group: agent
  href: https://artifacts.apis.io/underlayerhq-com/well-known/underlayerhq-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/underlayerhq-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/underlayerhq-com/hosts/underlayerhq-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/underlayerhq-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/underlayerhq-com/vendors/underlayerhq-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/underlayerhq-com-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://underlayerhq.com/dashboard/webhooks
- group: auth
  title: ''
  type: Security
  url: https://underlayerhq.com/security
- group: start
  title: ''
  type: Sandbox
  url: https://underlayerhq.com/sandbox
- group: auth
  href: https://artifacts.apis.io/underlayerhq-com/security/underlayerhq-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/underlayerhq-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/underlayerhq-com/security/underlayerhq-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/underlayerhq-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/underlayerhq-com/security/underlayerhq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/underlayerhq-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://underlayerhq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://underlayerhq.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://underlayerhq.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://underlayerhq.com/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://underlayerhq.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://underlayerhq.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://underlayerhq.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://underlayerhq.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Underlayerhq
coverage:
  checked: '2026-10-31'
  detail: The provider's public API reference page lists the base URL but no machine‑readable OpenAPI, AsyncAPI, GraphQL, or other spec is published.
  evidence:
  - status: 200
    url: https://underlayerhq.com/docs/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Underlayer provides an embedded training API for SaaS products, allowing developers to build courses via API and embed them via an iframe. It offers a headless LMS with no portal or learner accounts, pricing per course view, and supports SCORM export, webhooks, and MCP tools. The platform is built by Outworx and integrates with popular services.
image: https://underlayerhq.com/icon.svg
json_schemas:
- name: GetCollectionsIdResponse
  property_count: 5
  slug: underlayerhq-com-get-collections-id-response
- name: GetCoursesIdTranslatableResponse
  property_count: 7
  slug: underlayerhq-com-get-courses-id-translatable-response
- name: GetCoursesResponse
  property_count: 16
  slug: underlayerhq-com-get-courses-response
- name: GetIssuedCertificatesSerialResponse
  property_count: 9
  slug: underlayerhq-com-get-issued-certificates-serial-response
- name: PatchApiV1CoursesC123Request
  property_count: 4
  slug: underlayerhq-com-patch-api-v1-courses-c123-request
- name: PostApiV1CoursesCourseidScormResponse
  property_count: 2
  slug: underlayerhq-com-post-api-v1-courses-courseid-scorm-response
jsonld:
- class_count: 71
  name: Underlayerhq Com Context
  property_count: 59
  slug: underlayerhq-com-context
layout: provider
modified: '2026-10-31'
name: underlayerhq-com
nav: Providers
network: true
overview: 'underlayerhq-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Software-as-a-Service, Training, LMS, and Embeddings.


  The underlayerhq-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  underlayerhq-com''s developer surface includes sandbox, documentation, API reference, getting-started guide, pricing, signup flow, and 21 more developer resources.'
plans:
- name: Underlayerhq Com Plans Pricing
  plan_count: 3
  slug: underlayerhq-com-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: underlayerhq-com API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 2
  slug: underlayerhq-com-rules
score:
  band: thin
  composite: 34.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.6
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 17.9
    discoverability: 57.1
    operational_transparency: 11.8
  previous_composite: 45.8
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
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/underlayerhq-com/underlayerhq-com-2026-11-03T145413.png
security:
- kind: domain-security
  name: Underlayerhq Com Domain Security
  slug: underlayerhq-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Underlayerhq Com Vulnerability Disclosure
  slug: underlayerhq-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Underlayerhq Com Trust Center
  slug: underlayerhq-com-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: underlayerhq-com
tags:
- Education
- Software-as-a-Service
- Training
- LMS
- Embeddings
website: https://underlayerhq.com/
---

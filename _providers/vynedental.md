---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Vynedental Agentic Access
  operation_count: 17
  slug: vynedental-agentic-access
  summary_line: 17 operations · 12 acting
api_count: 1
apis:
- baseURL: https://production.onederful.co
  baseurl_source: declared
  description: Real-time and asynchronous dental eligibility and benefits checks (JSON, HTML and EDI 271 responses), enhanced/ClearCoverage eligibility, async status and response retrieval, and OAuth2 token issuance
  name: Vyne Dental Eligibility and Benefits API (Onederful)
  slug: eligibility-and-benefits-api
- baseURL: https://production.onederful.co
  baseurl_source: declared
  description: The Async API from Vyne Dental — 4 operation(s) for async.
  name: Vyne Dental Async API
  slug: vynedental-async-api
- baseURL: https://production.onederful.co
  baseurl_source: declared
  description: The EDI API from Vyne Dental — 4 operation(s) for edi.
  name: Vyne Dental EDI API
  slug: vynedental-edi-api
- baseURL: https://production.onederful.co
  baseurl_source: declared
  description: The Eligibility Response API from Vyne Dental — 2 operation(s) for eligibility response.
  name: Vyne Dental Eligibility Response API
  slug: vynedental-eligibility-response-api
- baseURL: https://production.onederful.co
  baseurl_source: declared
  description: The Eligibility Status API from Vyne Dental — 1 operation(s) for eligibility status.
  name: Vyne Dental Eligibility Status API
  slug: vynedental-eligibility-status-api
- baseURL: https://production.onederful.co
  baseurl_source: declared
  description: The Enhanced Eligibility API from Vyne Dental — 2 operation(s) for enhanced eligibility.
  name: Vyne Dental Enhanced Eligibility API
  slug: vynedental-enhanced-eligibility-api
- baseURL: https://production.onederful.co
  baseurl_source: declared
  description: The Oauth2 API from Vyne Dental — 2 operation(s) for oauth2.
  name: Vyne Dental Oauth2 API
  slug: vynedental-oauth2-api
- baseURL: https://production.onederful.co
  baseurl_source: declared
  description: The .well Known API from Vyne Dental — 1 operation(s) for .well known.
  name: Vyne Dental .well Known API
  slug: vynedental-well-known-api
artifact_total: 19
common:
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/vynedental/refs/heads/main/sandbox/vynedental-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/vynedental-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vynedental/refs/heads/main/agentic-access/vynedental-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/vynedental-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vynedental/refs/heads/main/rules/vynedental-rules.yml
  title: ''
  type: Spectral
  url: rules/vynedental-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vynedental/refs/heads/main/json-ld/vynedental-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/vynedental-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vynedental/refs/heads/main/vocabulary/vynedental-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/vynedental-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vynedental/refs/heads/main/data-model/vynedental-data-model.yml
  title: ''
  type: DataModel
  url: data-model/vynedental-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vynedental/refs/heads/main/errors/vynedental-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/vynedental-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vynedental/refs/heads/main/conformance/vynedental-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vynedental-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/vynedental/refs/heads/main/hosts/vynedental-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vynedental-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/vynedental/refs/heads/main/vendors/vynedental-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vynedental-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://vynedental.com/resources/blog/release-notes/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vynedental/refs/heads/main/authentication/vynedental-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vynedental-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vynedental/refs/heads/main/security/vynedental-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vynedental-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vynedental.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.onederful.co/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.onederful.co/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://production.onederful.co/api-docs/
- group: company
  title: ''
  type: Blog
  url: https://developer.onederful.co/blog/
- group: operate
  title: ''
  type: Support
  url: https://developer.onederful.co/docs/faq/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vynedental.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vynedental.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vynedental.com/privacy/
- group: start
  title: ''
  type: Login
  url: https://app.vynetrellis.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://vynedental.com/schedule-a-demo/
created: '2026-10-13'
description: 'Vyne Dental is a dental revenue-cycle and connectivity company: clearinghouse claims and attachments (FastAttach), eligibility and benefits verification, patient statements and payments, and the Vyne Trellis practice portal. Its developer surface is the Eligibility and Benefits API family (Onederful API, ClearCoverage API, Standard API) documented at the Vyne API Documentation Portal (developers.onederful.co), returning JSON, HTML or X12 270/271 responses from hundreds of dental payers, with OAuth2 bearer authentication and a sandbox.'
image: https://developer.onederful.co/img/Vyne_Dental_Logo_Primary_Full_Color__2_.png
json_schemas:
- name: BenefitType
  property_count: 15
  slug: vynedental-benefit-type
- name: EBGenericBenefitType
  property_count: 26
  slug: vynedental-ebgeneric-benefit-type
- name: PartialBenefitType
  property_count: 15
  slug: vynedental-partial-benefit-type
- name: PatientType
  property_count: 10
  slug: vynedental-patient-type
- name: PlanType
  property_count: 15
  slug: vynedental-plan-type
- name: RulesType
  property_count: 11
  slug: vynedental-rules-type
jsonld:
- class_count: 120
  name: Vynedental Context
  property_count: 365
  slug: vynedental-context
layout: provider
modified: '2026-10-13'
name: Vyne Dental
nav: Providers
network: true
overview: 'Vyne Dental publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Eligibility and Benefits API (Onederful), Async API, EDI API, and 5 more. Tagged areas include Company, Dental, Healthcare, Insurance, and Eligibility.


  The Vyne Dental catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Vyne Dental''s developer surface includes sandbox, changelog, authentication, documentation, API reference, engineering blog, support, and 17 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: Vyne Dental API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: vynedental-rules
score:
  band: developing
  composite: 46.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 52.8
    developer_ergonomics: 52.4
    discoverability: 66.1
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Vynedental Authentication
  slug: vynedental-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Vynedental Domain Security
  slug: vynedental-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vynedental
tags:
- Company
- Dental
- Healthcare
- Insurance
- Eligibility
- Claims
- EDI
- Payments
website: https://vynedental.com
---

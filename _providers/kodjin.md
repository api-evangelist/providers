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
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.3
  scored_at: '2026-11-06'
api_count: 5
apis:
- baseURL: https://sandbox.fhir.elationemr.com
  baseurl_source: spec
  description: FHIR‑based data platform API providing access to clinical data and analytics.
  name: Kodjin API
  slug: kodjin-api
- baseURL: https://sandbox.fhir.elationemr.com
  baseurl_source: declared
  description: The Auth API from Kodjin — 3 operation(s) for auth.
  name: Kodjin Auth API
  slug: kodjin-auth-api
- baseURL: https://sandbox.fhir.elationemr.com
  baseurl_source: declared
  description: The Fhir API from Kodjin — 11 operation(s) for fhir.
  name: Kodjin Fhir API
  slug: kodjin-fhir-api
- baseURL: https://sandbox.fhir.elationemr.com
  baseurl_source: declared
  description: The Patient API from Kodjin — 2 operation(s) for patient.
  name: Kodjin Patient API
  slug: kodjin-patient-api
- baseURL: https://sandbox.fhir.elationemr.com
  baseurl_source: declared
  description: The Terminology API from Kodjin — 1 operation(s) for terminology.
  name: Kodjin Terminology API
  slug: kodjin-terminology-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/kodjin/rules/kodjin-rules.yml
  title: ''
  type: Spectral
  url: rules/kodjin-rules.yml
- group: design
  href: https://artifacts.apis.io/kodjin/json-ld/kodjin-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/kodjin-context.jsonld
- group: design
  href: https://artifacts.apis.io/kodjin/vocabulary/kodjin-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kodjin-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/kodjin/data-model/kodjin-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kodjin-data-model.yml
- group: operate
  href: https://artifacts.apis.io/kodjin/changelog/kodjin-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/kodjin-changelog.yml
- group: design
  href: https://artifacts.apis.io/kodjin/conventions/kodjin-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kodjin-conventions.yml
- group: design
  href: https://artifacts.apis.io/kodjin/conformance/kodjin-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kodjin-conformance.yml
- group: agent
  href: https://artifacts.apis.io/kodjin/llms/kodjin-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kodjin-llms.txt
- group: agent
  href: https://artifacts.apis.io/kodjin/well-known/kodjin-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kodjin-well-known.yml
- group: other
  href: https://artifacts.apis.io/kodjin/hosts/kodjin-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kodjin-hosts.yml
- group: other
  href: https://artifacts.apis.io/kodjin/vendors/kodjin-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kodjin-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kodjin.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kodjin.com/privacy-policy/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.kodjin.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.kodjin.com/changelog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kodjin.com/uscdi_v3/getting-started-with-standartized-api/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.kodjin.com/
- group: auth
  href: https://artifacts.apis.io/kodjin/security/kodjin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kodjin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kodjin.com
- group: company
  title: ''
  type: Blog
  url: https://kodjin.com/blog
coverage:
  checked: '2026-10-14'
  detail: No OpenAPI or other machine‑readable contract was found on the provider's API hosts.
  evidence:
  - status: 0
    url: https://api.kodjin.com/openapi.json
  - status: 404
    url: https://dev.kodjin.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Kodjin offers an AI‑powered healthcare data platform that unifies clinical data across systems, enables interoperability, and supports advanced analytics, AI, and smarter decisions. It provides a FHIR‑based data warehouse, ETL tools, and Kubernetes‑based deployment options for cloud or on‑premise environments, targeting healthcare organizations seeking integrated data solutions.
image: https://kodjin.com/wp-content/uploads/2026/01/kodjinopengraphimage1.png
json_schemas:
- name: GetAuthRealmsFhirClientsRegistrationsOpenidConnectResponse
  property_count: 17
  slug: kodjin-get-auth-realms-fhir-clients-registrations-openid-connect-response
- name: GetFhirVersionsResponse
  property_count: 2
  slug: kodjin-get-fhir-versions-response
- name: PostFhirApplyFhirpathRequest
  property_count: 2
  slug: kodjin-post-fhir-apply-fhirpath-request
- name: PostFhirPatientValidateRequest
  property_count: 10
  slug: kodjin-post-fhir-patient-validate-request
- name: PostFhirReindexRequest
  property_count: 2
  slug: kodjin-post-fhir-reindex-request
- name: PostPatientValidateRequest
  property_count: 2
  slug: kodjin-post-patient-validate-request
jsonld:
- class_count: 7
  name: Kodjin Context
  property_count: 30
  slug: kodjin-context
layout: provider
modified: '2026-10-13'
name: Kodjin
nav: Providers
network: true
overview: 'Kodjin is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Fhir API, and 3 more. Tagged areas include Company, Low-Code, Platform, Automation, and Integration.


  The Kodjin catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Kodjin''s developer surface includes changelog, getting-started guide, documentation, engineering blog, and 16 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Kodjin API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: kodjin-rules
score:
  band: emerging
  composite: 22.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.1
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 25.8
    developer_ergonomics: 16.7
    discoverability: 69.6
    operational_transparency: 7.9
  previous_composite: 29.7
  provenance:
    conformance: derived
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
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/kodjin/kodjin-2026-11-03T134506.png
security:
- kind: domain-security
  name: Kodjin Domain Security
  slug: kodjin-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kodjin
tags:
- Company
- Low-Code
- Platform
- Automation
- Integration
website: https://kodjin.com
---

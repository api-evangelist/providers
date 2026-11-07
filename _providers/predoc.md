---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 13
  name: Predoc Agentic Access
  operation_count: 40
  slug: predoc-agentic-access
  summary_line: 40 operations · 13 acting · 13 human-in-the-loop
api_count: 1
apis:
- baseURL: https://partner-sandbox.predoc.ai/api/v1
  baseurl_source: declared
  description: The Authentication API from Predoc — 1 operation(s) for authentication.
  name: Predoc Authentication API
  slug: predoc-authentication-api
- baseURL: https://partner-sandbox.predoc.ai/api/v1
  baseurl_source: declared
  description: The Documents API from Predoc — 1 operation(s) for documents.
  name: Predoc Documents API
  slug: predoc-documents-api
- baseURL: https://partner-sandbox.predoc.ai/api/v1
  baseurl_source: declared
  description: The Events API from Predoc — 2 operation(s) for events.
  name: Predoc Events API
  slug: predoc-events-api
- baseURL: https://partner-sandbox.predoc.ai/api/v1
  baseurl_source: declared
  description: The Patient API from Predoc — 23 operation(s) for patient.
  name: Predoc Patient API
  slug: predoc-patient-api
- baseURL: https://partner-sandbox.predoc.ai/api/v1
  baseurl_source: declared
  description: The Record Request API from Predoc — 3 operation(s) for record request.
  name: Predoc Record Request API
  slug: predoc-record-request-api
- baseURL: https://partner-sandbox.predoc.ai/api/v1
  baseurl_source: declared
  description: The Record Upload API from Predoc — 3 operation(s) for record upload.
  name: Predoc Record Upload API
  slug: predoc-record-upload-api
- baseURL: https://partner-sandbox.predoc.ai/api/v1
  baseurl_source: declared
  description: The Retrieval API from Predoc — 2 operation(s) for retrieval.
  name: Predoc Retrieval API
  slug: predoc-retrieval-api
artifact_total: 23
asyncapis:
- description: ''
  name: Predoc Webhooks
  slug: predoc-webhooks
common:
- group: other
  href: https://artifacts.apis.io/predoc/capabilities/predoc-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/predoc-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/predoc/agentic-access/predoc-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/predoc-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/predoc/rules/predoc-rules.yml
  title: ''
  type: Spectral
  url: rules/predoc-rules.yml
- group: design
  href: https://artifacts.apis.io/predoc/json-ld/predoc-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/predoc-context.jsonld
- group: design
  href: https://artifacts.apis.io/predoc/vocabulary/predoc-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/predoc-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/predoc/hosts/predoc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/predoc-hosts.yml
- group: other
  href: https://artifacts.apis.io/predoc/vendors/predoc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/predoc-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.predoc.ai/news
- group: auth
  href: https://artifacts.apis.io/predoc/security/predoc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/predoc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.predoc.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.predoc.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.predoc.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.predoc.ai/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.predoc.ai/get-started
- group: start
  title: ''
  type: Login
  url: https://app.predoc.ai/login
- group: company
  title: ''
  type: Blog
  url: https://www.predoc.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.predoc.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.predoc.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.predoc.ai/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://predoc.statuspage.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.predoc.ai/changelog
- group: auth
  title: ''
  type: Compliance
  url: https://www.predoc.ai/security-compliance
- group: agent
  href: https://artifacts.apis.io/predoc/llms/predoc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/predoc-llms.txt
- group: auth
  href: https://artifacts.apis.io/predoc/authentication/predoc-authentication.yml
  title: ''
  type: Authentication
  url: authentication/predoc-authentication.yml
- group: design
  href: https://artifacts.apis.io/predoc/conventions/predoc-conventions.yml
  title: ''
  type: Conventions
  url: conventions/predoc-conventions.yml
- group: design
  href: https://artifacts.apis.io/predoc/conformance/predoc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/predoc-conformance.yml
- group: auth
  href: https://artifacts.apis.io/predoc/security/predoc-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/predoc-trust-center.yml
- group: design
  href: https://artifacts.apis.io/predoc/lifecycle/predoc-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/predoc-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/predoc/lifecycle/predoc-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/predoc-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/predoc/changelog/predoc-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/predoc-changelog.yml
- group: start
  href: https://artifacts.apis.io/predoc/sandbox/predoc-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/predoc-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/predoc/mcp/predoc-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/predoc-mcp.yml
- group: design
  href: https://artifacts.apis.io/predoc/asyncapi/predoc-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/predoc-webhooks.yml
- group: design
  href: https://artifacts.apis.io/predoc/data-model/predoc-data-model.yml
  title: ''
  type: DataModel
  url: data-model/predoc-data-model.yml
- group: design
  href: https://artifacts.apis.io/predoc/errors/predoc-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/predoc-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/predoc/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Predoc is an AI-native medical records platform that automates the retrieval, aggregation, normalization, de-duplication, and structured delivery of complete patient histories. It queries health information exchanges (HIEs) and initiates outreach to non-connected providers, ingests faxes, PDFs, and digital formats, and delivers clean, FHIR-compliant clinical data to healthcare organizations and clinical research teams via a REST Partner API, file exports, or direct EHR integration. The Predoc Partner API (v1.4.1) exposes patient management, record-retrieval requests, record uploads, granular clinical document endpoints (medications, labs, imaging, procedures, notes, vaccines, allergies), clinical summaries, and webhook event notifications, secured with short-lived JWT bearer tokens.
image: https://cdn.prod.website-files.com/6827c1994862c627993a82d8/688c883a300cc1480f08f8a1_favicon_32.png
json_schemas:
- name: CreateCrrInpDto
  property_count: 13
  slug: predoc-create-crr-inp-dto
- name: CreatePatientV2InpDto
  property_count: 10
  slug: predoc-create-patient-v2-inp-dto
- name: CreatePatientWithCrrV2InpDto
  property_count: 23
  slug: predoc-create-patient-with-crr-v2-inp-dto
- name: ModifyCrrInpDto
  property_count: 13
  slug: predoc-modify-crr-inp-dto
- name: PatientInfoResponseDto
  property_count: 14
  slug: predoc-patient-info-response-dto
- name: UpdatePatientInformationInpDto
  property_count: 11
  slug: predoc-update-patient-information-inp-dto
jsonld:
- class_count: 120
  name: Predoc Context
  property_count: 339
  slug: predoc-context
layout: provider
modified: '2026-07-20'
name: Predoc
nav: Providers
network: true
overview: 'Predoc publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Documents API, Events API, and 4 more. Tagged areas include Company, Healthcare, Medical Records, Health Information Exchange, and FHIR.


  The Predoc catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Predoc''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, authentication, and 29 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Predoc API Rules
  rule_count: 14
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 4
  slug: predoc-rules
score:
  band: strong
  composite: 59.8
  coverage:
    artifact_dirs: 27
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.8
  facets:
    access_clarity: 43.4
    contract_governance: 35.6
    contract_quality: 73.4
    developer_ergonomics: 66.1
    discoverability: 74.1
    operational_transparency: 47.4
  previous_composite: 55.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 27.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/predoc/predoc-2026-08-17T081335.png
security:
- kind: authentication
  name: Predoc Authentication
  slug: predoc-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Predoc Domain Security
  slug: predoc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Predoc Trust Center
  slug: predoc-trust-center
  summary_line: SOC 2 Type II, HIPAA, FDA 21 CFR Part 11
skill_count: 3
skills:
- name: Generate and download a patient clinical summary
  slug: predoc-clinical-summary
- name: Request and retrieve a patient's medical records
  slug: predoc-retrieve-patient-records
- name: Configure webhooks for record lifecycle events
  slug: predoc-webhook-setup
slug: predoc
tags:
- Company
- Healthcare
- Medical Records
- Health Information Exchange
- FHIR
- Clinical Data
- Artificial Intelligence
- Interoperability
- EHR Integration
- Webhook
- Clinical Research
website: https://www.predoc.ai
---

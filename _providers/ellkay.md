---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 114
  human_in_the_loop: 0
  name: Ellkay Agentic Access
  operation_count: 233
  slug: ellkay-agentic-access
  summary_line: 233 operations · 114 acting
api_count: 2
apis:
- description: Single-endpoint healthcare interoperability API exposing proprietary LK* operations (appointments, patient bridge/search, documents, charges, patient balance, master lists) that bi-directionally conne
  name: LKCloud Interop API
  slug: lkcloud-interop-api
- description: HL7 FHIR R4 RESTful API (read/search/create/update/delete across R4 resources) over the ELLKAY interoperability platform, with a published CapabilityStatement. OAuth 2.0 Bearer + SiteServiceKey; error
  name: LKCloud FHIR R4 API
  slug: lkcloud-fhir-r4-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The Account API from ELLKAY — 2 operation(s) for account.
  name: ELLKAY Account API
  slug: ellkay-account-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The Appointment API from ELLKAY — 2 operation(s) for appointment.
  name: ELLKAY Appointment API
  slug: ellkay-appointment-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The Binary API from ELLKAY — 1 operation(s) for binary.
  name: ELLKAY Binary API
  slug: ellkay-binary-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The ClinicalImpression API from ELLKAY — 2 operation(s) for clinicalimpression.
  name: ELLKAY Clinical Impression API
  slug: ellkay-clinicalimpression-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The Communication API from ELLKAY — 2 operation(s) for communication.
  name: ELLKAY Communication API
  slug: ellkay-communication-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The CommunicationRequest API from ELLKAY — 2 operation(s) for communicationrequest.
  name: ELLKAY Communication Request API
  slug: ellkay-communicationrequest-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The Condition API from ELLKAY — 2 operation(s) for condition.
  name: ELLKAY Condition API
  slug: ellkay-condition-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The Coverage API from ELLKAY — 2 operation(s) for coverage.
  name: ELLKAY Coverage API
  slug: ellkay-coverage-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The DiagnosticReport API from ELLKAY — 2 operation(s) for diagnosticreport.
  name: ELLKAY Diagnostic Report API
  slug: ellkay-diagnosticreport-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The Encounter API from ELLKAY — 2 operation(s) for encounter.
  name: ELLKAY Encounter API
  slug: ellkay-encounter-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The FamilyMemberHistory API from ELLKAY — 2 operation(s) for familymemberhistory.
  name: ELLKAY Family Member History API
  slug: ellkay-familymemberhistory-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The Immunization API from ELLKAY — 2 operation(s) for immunization.
  name: ELLKAY Immunization API
  slug: ellkay-immunization-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: Ellkay Appointment endpoints
  name: ELLKAY LK Appointments API
  slug: ellkay-lkappointments-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: Ellkay Bridge
  name: ELLKAY LK Bridge API
  slug: ellkay-lkbridge-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: Charge details
  name: ELLKAY LK Charges API
  slug: ellkay-lkcharges-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: LKDocuments endpoints
  name: ELLKAY LK Documents API
  slug: ellkay-lkdocuments-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: Master List.
  name: ELLKAY LK Master List API
  slug: ellkay-lkmasterlist-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: Load patient's balances. Allows patients to apply payments.
  name: ELLKAY LK Patient Balance API
  slug: ellkay-lkpatientbalance-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: PatientDataLink endpoint
  name: ELLKAY LK Patient Data Link API
  slug: ellkay-lkpatientdatalink-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The Location API from ELLKAY — 2 operation(s) for location.
  name: ELLKAY Location API
  slug: ellkay-location-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The Medication API from ELLKAY — 2 operation(s) for medication.
  name: ELLKAY Medication API
  slug: ellkay-medication-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The MedicationStatement API from ELLKAY — 2 operation(s) for medicationstatement.
  name: ELLKAY Medication Statement API
  slug: ellkay-medicationstatement-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The Metadata API from ELLKAY — 1 operation(s) for metadata.
  name: ELLKAY Metadata API
  slug: ellkay-metadata-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The Observation API from ELLKAY — 2 operation(s) for observation.
  name: ELLKAY Observation API
  slug: ellkay-observation-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The Operations API from ELLKAY — 1 operation(s) for operations.
  name: ELLKAY Operations API
  slug: ellkay-operations-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The Organization API from ELLKAY — 2 operation(s) for organization.
  name: ELLKAY Organization API
  slug: ellkay-organization-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The Patient API from ELLKAY — 2 operation(s) for patient.
  name: ELLKAY Patient API
  slug: ellkay-patient-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The Person API from ELLKAY — 2 operation(s) for person.
  name: ELLKAY Person API
  slug: ellkay-person-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The Practitioner API from ELLKAY — 2 operation(s) for practitioner.
  name: ELLKAY Practitioner API
  slug: ellkay-practitioner-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The Procedure API from ELLKAY — 2 operation(s) for procedure.
  name: ELLKAY Procedure API
  slug: ellkay-procedure-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The Questionnaire API from ELLKAY — 2 operation(s) for questionnaire.
  name: ELLKAY Questionnaire API
  slug: ellkay-questionnaire-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The QuestionnaireResponse API from ELLKAY — 2 operation(s) for questionnaireresponse.
  name: ELLKAY Questionnaire Response API
  slug: ellkay-questionnaireresponse-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The RelatedPerson API from ELLKAY — 2 operation(s) for relatedperson.
  name: ELLKAY Related Person API
  slug: ellkay-relatedperson-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The ServiceRequest API from ELLKAY — 2 operation(s) for servicerequest.
  name: ELLKAY Service Request API
  slug: ellkay-servicerequest-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The Slot API from ELLKAY — 2 operation(s) for slot.
  name: ELLKAY Slot API
  slug: ellkay-slot-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: UpdatePatient endpoint
  name: ELLKAY Update Patient API
  slug: ellkay-updatepatient-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The Allergy Intolerance API from ELLKAY — 2 operation(s) for allergy intolerance.
  name: ELLKAY Allergy Intolerance API
  slug: ellkay-allergy-intolerance-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The Document Reference API from ELLKAY — 2 operation(s) for document reference.
  name: ELLKAY Document Reference API
  slug: ellkay-document-reference-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The Insurance Plan API from ELLKAY — 2 operation(s) for insurance plan.
  name: ELLKAY Insurance Plan API
  slug: ellkay-insurance-plan-api
- baseURL: https://services.lkcloud.com
  baseurl_source: declared
  description: The Medication Request API from ELLKAY — 2 operation(s) for medication request.
  name: ELLKAY Medication Request API
  slug: ellkay-medication-request-api
artifact_total: 60
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ellkay/refs/heads/main/agentic-access/ellkay-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ellkay-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ellkay/refs/heads/main/rules/ellkay-rules.yml
  title: ''
  type: Spectral
  url: rules/ellkay-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ellkay/refs/heads/main/json-ld/ellkay-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ellkay-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ellkay/refs/heads/main/vocabulary/ellkay-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ellkay-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ellkay/refs/heads/main/data-model/ellkay-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ellkay-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ellkay/refs/heads/main/errors/ellkay-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ellkay-problem-types.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ellkay/refs/heads/main/hosts/ellkay-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ellkay-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ellkay/refs/heads/main/integrations/ellkay-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/ellkay-integration-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ellkay/refs/heads/main/vendors/ellkay-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ellkay-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.ellkay.com/leadership
- group: company
  title: ''
  type: Website
  url: https://www.ellkay.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://lkcloud-api.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://lkcloud-api.readme.io/docs/lk-cloud-overview
- group: docs
  title: ''
  type: APIReference
  url: https://lkcloud-api.readme.io/reference
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ellkay/refs/heads/main/authentication/ellkay-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ellkay-authentication.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ellkay/refs/heads/main/changelog/ellkay-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ellkay-changelog.yml
- group: company
  title: ''
  type: Blog
  url: https://www.ellkay.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.ellkay.com/support
- group: start
  title: ''
  type: Login
  url: https://dashboard.ellkay.com/Login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ellkay.com/privacy-policy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ellkay/refs/heads/main/well-known/ellkay-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ellkay-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ellkay/refs/heads/main/conventions/ellkay-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ellkay-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ellkay/refs/heads/main/errors/ellkay-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/ellkay-error-codes.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ellkay/refs/heads/main/rate-limits/ellkay-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ellkay-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ellkay/refs/heads/main/lifecycle/ellkay-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ellkay-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ellkay/refs/heads/main/conformance/ellkay-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ellkay-conformance.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/ellkay/refs/heads/main/sandbox/ellkay-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/ellkay-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ellkay/refs/heads/main/mcp/ellkay-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/ellkay-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ellkay/refs/heads/main/security/ellkay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ellkay-domain-security.yml
created: '2026-07-17'
description: 'ELLKAY is a healthcare data interoperability and data-management company that connects disparate health IT systems so clinical and financial data can move where it is needed. Its LKOpera, LKOrbit, and LKOasis product lines provide interface-engine integration, orders and results, payer data retrieval, network/lab connectivity, and data archiving/migration across 750+ EMR/PM systems, 400+ hospitals, 58k+ practices, and 725+ laboratories. For developers, ELLKAY exposes the LKCloud platform: a single-endpoint Interop API (proprietary LK* operations) and a full HL7 FHIR R4 RESTful API, both authenticated with OAuth 2.0 against the LKIdentity authorization server and routed with a SiteServiceKey.'
image: https://cdn.prod.website-files.com/68470d9028f4a074323fde70/689b3ac60177b4bae93d407b_Asset%2028.png
json_schemas:
- name: Account
  property_count: 0
  slug: ellkay-account
- name: AllergyIntolerance
  property_count: 0
  slug: ellkay-allergy-intolerance
- name: Appointment
  property_count: 0
  slug: ellkay-appointment
- name: Binary
  property_count: 0
  slug: ellkay-binary
- name: Bundle
  property_count: 0
  slug: ellkay-bundle
- name: CapabilityStatement
  property_count: 0
  slug: ellkay-capability-statement
- name: LKCloudConnect.Contracts.Appointments.Appointment
  property_count: 20
  slug: ellkay-lkcloud-connect-contracts-appointments-appointment
- name: LKCloudConnect.Contracts.Bridge.GetGuarantorResult
  property_count: 30
  slug: ellkay-lkcloud-connect-contracts-bridge-get-guarantor-result
- name: LKCloudConnect.Contracts.PatientDataLink.GetDiagnosesResult
  property_count: 36
  slug: ellkay-lkcloud-connect-contracts-patient-data-link-get-diagnoses-result
- name: LKCloudConnect.Contracts.PatientDataLink.GetImmunizationsResult
  property_count: 30
  slug: ellkay-lkcloud-connect-contracts-patient-data-link-get-immunizations-result
- name: LKCloudConnect.Contracts.PatientDataLink.GetMedicationsResult
  property_count: 34
  slug: ellkay-lkcloud-connect-contracts-patient-data-link-get-medications-result
- name: LKCloudConnect.Contracts.PatientDataLink.GetProceduresResult
  property_count: 43
  slug: ellkay-lkcloud-connect-contracts-patient-data-link-get-procedures-result
jsonld:
- class_count: 120
  name: Ellkay Context
  property_count: 214
  slug: ellkay-context
layout: provider
modified: '2026-07-19'
name: ELLKAY
nav: Providers
network: true
overview: 'ELLKAY publishes 42 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Appointment API, Binary API, and 39 more. Tagged areas include Company, Healthcare, Interoperability, FHIR, and HL7.


  The ELLKAY catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ELLKAY''s developer surface includes documentation, API reference, authentication, changelog, engineering blog, support, sandbox, and 22 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 1
  name: Ellkay Rate Limits
  slug: ellkay-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: ELLKAY API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: ellkay-rules
score:
  band: developing
  composite: 45.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 18.8
  facets:
    access_clarity: 17.1
    contract_governance: 35.6
    contract_quality: 60.5
    developer_ergonomics: 39.3
    discoverability: 67.9
    operational_transparency: 36.8
  previous_composite: 27.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 40
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/ellkay/refs/heads/main/screenshots/ellkay-2026-07-25T213153.png
security:
- kind: authentication
  name: Ellkay Authentication
  slug: ellkay-authentication
  summary_line: oauth2 · 3 schemes
- kind: domain-security
  name: Ellkay Domain Security
  slug: ellkay-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ellkay
tags:
- Company
- Healthcare
- Interoperability
- FHIR
- HL7
- EHR Integration
- Health Data
website: https://www.ellkay.com/
---

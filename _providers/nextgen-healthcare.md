---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Nextgen Healthcare Agentic Access
  operation_count: 108
  slug: nextgen-healthcare-agentic-access
  summary_line: 108 operations · 8 acting
api_count: 2
apis:
- description: HL7 FHIR API for the NextGen Enterprise EHR, certified under the 21st Century Cures Act Patient Access criteria, exposing USCDI data to patient-facing apps. Available in FHIR R4 (4.0.1) and legacy DST
  name: NextGen Enterprise Patient Access FHIR API
  slug: nextgen-enterprise-patient-access-fhir-api
- description: 'An extensive collection of JSON-based RESTful APIs (800+ routes) that power apps used by provider organizations on the NextGen Enterprise platform (v5.9.0+), covering clinical and practice-management '
  name: NextGen Enterprise API
  slug: nextgen-enterprise-api
- description: HL7 FHIR STU3 (R3) API for the NextGen Office EHR with C-CDA support, authenticated with SMART App Launch / OpenID Connect OAuth2 via Keycloak. Predecessor surface to the R4 Patient Access API.
  name: NextGen Office FHIR R3 API
  slug: nextgen-office-fhir-r3-api
- description: FHIR R4-based Patient Access API for NextGen Office (formerly MediTouch) ambulatory practices. Enables patients and authorized apps to access personal health information via the YourHealthFile patient
  name: NextGen Office Patient FHIR API
  slug: nextgen-office-patient-fhir-api
- description: SMART on FHIR App Launch API for NextGen Office enabling vendor applications to obtain USCDIv1 clinical data for a single patient. Compliant with 21st Century Cures Act requirements. Supports HL7 SMAR
  name: NextGen Office SMART App Launch FHIR API
  slug: nextgen-office-smart-app-launch-fhir-api
- description: Bulk FHIR API for NextGen Office enabling authorized vendors to obtain USCDIv1 data for multiple patients in a group using the HL7 FHIR Bulk Data Access specification. Compliant with 21st Century Cure
  name: NextGen Office Bulk FHIR API
  slug: nextgen-office-bulk-fhir-api
- description: 'API for NextGen Mirth Connect, an open-source healthcare integration engine supporting HL7 v2, FHIR, and other healthcare data standards for interoperability between clinical systems. Enables message '
  name: NextGen Mirth Connect Integration Engine API
  slug: nextgen-mirth-connect-integration-engine-api
- baseURL: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/
  baseurl_source: declared
  description: https://hl7.org/fhir/R4/careteam.html
  name: NextGen Healthcare Care Team API
  phrasing_intents:
  - id: getFhirR4CareTeamById
    intent: Get one care team member record
    question: Can I look up one care team entry directly by its id?
  - id: getFhirR4CareTeam
    intent: Search a patient's care team
    question: Who is on a patient's care team?
  phrasing_ops: 2
  slug: nextgen-healthcare-careteam-api
- baseURL: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/
  baseurl_source: declared
  description: The CCDA API from NextGen Healthcare — 1 operation(s) for ccda.
  name: NextGen Healthcare CCDA API
  phrasing_intents:
  - id: getCcda
    intent: Export a patient's record as a C-CDA document
    question: How do I get a patient's summary as a C-CDA document?
  phrasing_ops: 1
  slug: nextgen-healthcare-ccda-api
- baseURL: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/
  baseurl_source: declared
  description: https://hl7.org/fhir/R4/condition.html
  name: NextGen Healthcare Condition API
  phrasing_intents:
  - id: getFhirR4ConditionById
    intent: Get one condition or problem
    question: Can I fetch a single diagnosis or problem by its resource id?
  - id: getFhirR4Condition
    intent: List a patient's conditions and problems
    question: What problems and diagnoses are on a patient's problem list?
  phrasing_ops: 2
  slug: nextgen-healthcare-condition-api
- baseURL: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/
  baseurl_source: declared
  description: https://hl7.org/fhir/R4/coverage.html
  name: NextGen Healthcare Coverage API
  phrasing_intents:
  - id: getFhirR4CoverageById
    intent: Get one insurance coverage record
    question: Can I pull one insurance coverage record by its id?
  - id: getFhirR4Coverage
    intent: List a patient's insurance coverage
    question: What insurance plans does a patient have on file?
  phrasing_ops: 2
  slug: nextgen-healthcare-coverage-api
- baseURL: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/
  baseurl_source: declared
  description: https://hl7.org/fhir/R4/device.html
  name: NextGen Healthcare Device API
  phrasing_intents:
  - id: getFhirR4DeviceById
    intent: Get one implantable device
    question: Can I get one implanted device record by id?
  - id: getFhirR4Device
    intent: List a patient's implantable devices
    question: Which implanted devices does a patient have?
  phrasing_ops: 2
  slug: nextgen-healthcare-device-api
- baseURL: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/
  baseurl_source: declared
  description: https://hl7.org/fhir/R4/diagnosticreport.html
  name: NextGen Healthcare Diagnostic Report API
  phrasing_intents:
  - id: getFhirR4DiagnosticReportById
    intent: Get one lab or imaging report
    question: Can I open a single lab or radiology report by its id?
  - id: getFhirR4DiagnosticReport
    intent: List a patient's lab and imaging reports
    question: Where do I find all of a patient's lab and radiology results?
  phrasing_ops: 2
  slug: nextgen-healthcare-diagnosticreport-api
- baseURL: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/
  baseurl_source: declared
  description: https://hl7.org/fhir/R4/encounter.html
  name: NextGen Healthcare Encounter API
  phrasing_intents:
  - id: getFhirR4EncounterById
    intent: Get one patient encounter
    question: Can I get a single visit record by its encounter id?
  - id: getFhirR4Encounter
    intent: Search a patient's encounters
    question: How do I list all visits a patient has had?
  phrasing_ops: 2
  slug: nextgen-healthcare-encounter-api
- baseURL: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/
  baseurl_source: declared
  description: The Export APIs API from NextGen Healthcare — 2 operation(s) for export apis.
  name: NextGen Healthcare Export APIs API
  phrasing_intents:
  - id: groupExport
    intent: Start a bulk FHIR export for a patient group
    question: How do I export all FHIR data for every patient in a group from NextGen Office?
  - id: pollJobStatus
    intent: Check the status of a bulk export job
    question: Is my bulk data export finished yet?
  - id: deleteJob
    intent: Cancel a running bulk export job
    question: Can I cancel a bulk FHIR export that is still running?
  phrasing_ops: 3
  slug: nextgen-healthcare-export-apis-api
- baseURL: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/
  baseurl_source: declared
  description: https://hl7.org/fhir/R4/goal.html
  name: NextGen Healthcare Goal API
  phrasing_intents:
  - id: getFhirR4GoalById
    intent: Get one patient goal
    question: Can I fetch one patient goal by its id?
  - id: getFhirR4Goal
    intent: List a patient's health goals
    question: What health goals are set for a patient?
  phrasing_ops: 2
  slug: nextgen-healthcare-goal-api
- baseURL: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/
  baseurl_source: declared
  description: The Group APIs API from NextGen Healthcare — 2 operation(s) for group apis.
  name: NextGen Healthcare Group APIs API
  phrasing_intents:
  - id: createGroup
    intent: Create a patient group for bulk export
    question: How do I define a new group of patients to run a bulk FHIR export against?
  - id: getAllGroups
    intent: List all bulk FHIR patient groups
    question: Which patient groups have I already set up for bulk FHIR export in NextGen Office?
  - id: updateGroup
    intent: Add or remove patients in an existing group
    question: Can I add patients to a group I already created without rebuilding it?
  - id: deleteGroup
    intent: Delete a patient group
    question: How do I permanently remove a patient group I no longer export?
  - id: getGroup
    intent: Retrieve one patient group
    question: How can I look up the details of a single patient group by its ID?
  phrasing_ops: 5
  slug: nextgen-healthcare-group-apis-api
- baseURL: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/
  baseurl_source: declared
  description: https://hl7.org/fhir/R4/immunization.html
  name: NextGen Healthcare Immunization API
  phrasing_intents:
  - id: getFhirR4ImmunizationById
    intent: Get one immunization record
    question: Can I fetch a single vaccination record by id?
  - id: getFhirR4Immunization
    intent: List a patient's immunizations
    question: Which vaccines has a patient received?
  phrasing_ops: 2
  slug: nextgen-healthcare-immunization-api
- baseURL: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/
  baseurl_source: declared
  description: https://hl7.org/fhir/R4/location.html
  name: NextGen Healthcare Location API
  phrasing_intents:
  - id: getFhirR4LocationById
    intent: Get a care location
    question: Can I look up a clinic or facility by its location id?
  phrasing_ops: 1
  slug: nextgen-healthcare-location-api
- baseURL: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/
  baseurl_source: declared
  description: The MedicationDispense API from NextGen Healthcare — 2 operation(s) for medicationdispense.
  name: NextGen Healthcare Medication Dispense API
  phrasing_intents:
  - id: getFhirR4MedicationDispenseById
    intent: Get one medication dispense
    question: Can I fetch a single pharmacy dispense record by id?
  - id: getFhirR4MedicationDispense
    intent: List medications dispensed to a patient
    question: Which medications have been dispensed to a patient?
  phrasing_ops: 2
  slug: nextgen-healthcare-medicationdispense-api
- baseURL: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/
  baseurl_source: declared
  description: https://hl7.org/fhir/R4/observation.html
  name: NextGen Healthcare Observation API
  phrasing_intents:
  - id: getFhirR4ObservationById
    intent: Get one observation
    question: Can I fetch a single vital sign or lab value by its observation id?
  - id: getFhirR4Observation
    intent: List a patient's observations and vitals
    question: How do I get a patient's vital signs and lab values?
  phrasing_ops: 2
  slug: nextgen-healthcare-observation-api
- baseURL: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/
  baseurl_source: declared
  description: https://hl7.org/fhir/R4/organization.html
  name: NextGen Healthcare Organization API
  phrasing_intents:
  - id: getFhirR4OrganizationById
    intent: Get an organization
    question: Can I look up a healthcare organization by its id?
  phrasing_ops: 1
  slug: nextgen-healthcare-organization-api
- baseURL: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/
  baseurl_source: declared
  description: https://hl7.org/fhir/R4/patient.html
  name: NextGen Healthcare Patient API
  phrasing_intents:
  - id: getFhirR4PatientById
    intent: Get one patient's demographics
    question: How do I pull a patient's demographics if I know their patient id?
  - id: getFhirR4Patient
    intent: Search for patients
    question: How do I find a patient by name and date of birth?
  phrasing_ops: 2
  slug: nextgen-healthcare-patient-api
- baseURL: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/
  baseurl_source: declared
  description: The Patient Search API from NextGen Healthcare — 1 operation(s) for patient search.
  name: NextGen Healthcare Patient Search API
  phrasing_intents:
  - id: searchPatients
    intent: Search patients for bulk FHIR access
    question: How do I find a patient by chart number in NextGen Office bulk FHIR?
  phrasing_ops: 1
  slug: nextgen-healthcare-patient-search-api
- baseURL: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/
  baseurl_source: declared
  description: https://hl7.org/fhir/R4/practitioner.html
  name: NextGen Healthcare Practitioner API
  phrasing_intents:
  - id: getFhirR4PractitionerById
    intent: Get a practitioner
    question: Can I look up a doctor or clinician by practitioner id?
  phrasing_ops: 1
  slug: nextgen-healthcare-practitioner-api
- baseURL: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/
  baseurl_source: declared
  description: https://hl7.org/fhir/R4/procedure.html
  name: NextGen Healthcare Procedure API
  phrasing_intents:
  - id: getFhirR4ProcedureById
    intent: Get one procedure
    question: Can I fetch a single procedure record by id?
  - id: getFhirR4Procedure
    intent: List a patient's procedures
    question: What procedures has a patient had?
  phrasing_ops: 2
  slug: nextgen-healthcare-procedure-api
- baseURL: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/
  baseurl_source: declared
  description: https://hl7.org/fhir/R4/provenance.html
  name: NextGen Healthcare Provenance API
  phrasing_intents:
  - id: getFhirR4ProvenanceById
    intent: Get a provenance record
    question: How do I see who authored a clinical record and when?
  phrasing_ops: 1
  slug: nextgen-healthcare-provenance-api
- baseURL: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/
  baseurl_source: declared
  description: https://hl7.org/fhir/R4/relatedperson.html
  name: NextGen Healthcare Related Person API
  phrasing_intents:
  - id: getFhirR4RelatedPersonById
    intent: Get one related person
    question: Can I fetch one patient contact or relative by its id?
  - id: getFhirR4RelatedPerson
    intent: List a patient's related persons
    question: Who are a patient's family members or caregivers on file?
  phrasing_ops: 2
  slug: nextgen-healthcare-relatedperson-api
- baseURL: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/
  baseurl_source: declared
  description: https://hl7.org/fhir/R4/specimen.html
  name: NextGen Healthcare Specimen API
  phrasing_intents:
  - id: getFhirR4SpecimenById
    intent: Get one specimen
    question: Can I fetch one lab specimen by its logical id?
  - id: getFhirR4Specimen
    intent: Search specimens by patient
    question: Which specimens were collected from a patient?
  phrasing_ops: 2
  slug: nextgen-healthcare-specimen-api
- baseURL: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/
  baseurl_source: declared
  description: https://hl7.org/fhir/R4/allergyintolerance.html
  name: NextGen Healthcare Allergy Intolerance API
  phrasing_intents:
  - id: getFhirR4AllergyIntoleranceById
    intent: Get one allergy or intolerance record
    question: Can I pull a single allergy record if I already have its FHIR id?
  - id: getFhirR4AllergyIntolerance
    intent: List a patient's allergies and intolerances
    question: How do I see every allergy a patient has on file in NextGen?
  phrasing_ops: 2
  slug: nextgen-healthcare-allergy-intolerance-api
- baseURL: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/
  baseurl_source: declared
  description: https://hl7.org/fhir/R4/careplan.html
  name: NextGen Healthcare Care plan API
  phrasing_intents:
  - id: getFhirR4CarePlanById
    intent: Get one care plan or assessment
    question: Can I open one specific care plan by its id?
  - id: getFhirR4CarePlan
    intent: List a patient's care plans
    question: Which care plans and treatment orders does a patient have?
  phrasing_ops: 2
  slug: nextgen-healthcare-care-plan-api
- baseURL: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/
  baseurl_source: declared
  description: https://hl7.org/fhir/R4/documentreference.html
  name: NextGen Healthcare Document Reference API
  phrasing_intents:
  - id: getFhirR4DocumentReferenceById
    intent: Get one clinical document reference
    question: Can I fetch one clinical note's document reference by id?
  - id: getFhirR4DocumentReference
    intent: List a patient's clinical documents
    question: How do I list a patient's discharge summaries and progress notes?
  phrasing_ops: 2
  slug: nextgen-healthcare-document-reference-api
- baseURL: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/
  baseurl_source: declared
  description: https://hl7.org/fhir/R4/medicationadministration.html
  name: NextGen Healthcare Medication Administration API
  phrasing_intents:
  - id: getFhirR4MedicationAdministrationById
    intent: Get one medication administration
    question: Can I fetch a single record of a medication being given by id?
  - id: getFhirR4MedicationAdministration
    intent: List medications administered to a patient
    question: What medications has a patient actually been given?
  phrasing_ops: 2
  slug: nextgen-healthcare-medication-administration-api
- baseURL: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/
  baseurl_source: declared
  description: https://hl7.org/fhir/R4/medicationrequest.html
  name: NextGen Healthcare Medication Request API
  phrasing_intents:
  - id: getFhirR4MedicationRequestById
    intent: Get one prescription
    question: Can I fetch one prescription record by its id?
  - id: getFhirR4MedicationRequest
    intent: List a patient's prescriptions
    question: Which prescriptions does a patient have?
  phrasing_ops: 2
  slug: nextgen-healthcare-medication-request-api
- baseURL: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/
  baseurl_source: declared
  description: https://hl7.org/fhir/R4/practitionerrole.html
  name: NextGen Healthcare Practitioner Role API
  phrasing_intents:
  - id: getFhirR4PractitionerRoleById
    intent: Get one practitioner role
    question: Can I fetch a single practitioner role by its role id?
  - id: getFhirR4PractitionerRole
    intent: List a practitioner's roles
    question: Which roles does a given practitioner hold?
  phrasing_ops: 2
  slug: nextgen-healthcare-practitioner-role-api
artifact_total: 94
collections:
- collection_type: open
  name: API Collection
  slug: open-nextgen-healthcare-fhir-capability-statement
- collection_type: open
  name: NextGen Office BulK FHIR API
  slug: open-nextgen-office-bulk-fhir-r4
common:
- group: design
  href: https://artifacts.apis.io/nextgen-healthcare/rules/nextgen-healthcare-rules.yml
  title: ''
  type: Spectral
  url: rules/nextgen-healthcare-rules.yml
- group: design
  href: https://artifacts.apis.io/nextgen-healthcare/json-ld/nextgen-healthcare-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/nextgen-healthcare-context.jsonld
- group: design
  href: https://artifacts.apis.io/nextgen-healthcare/vocabulary/nextgen-healthcare-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/nextgen-healthcare-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/nextgen-healthcare/security/nextgen-healthcare-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/nextgen-healthcare-trust-center.yml
- group: other
  href: https://artifacts.apis.io/nextgen-healthcare/hosts/nextgen-healthcare-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nextgen-healthcare-hosts.yml
- group: other
  href: https://artifacts.apis.io/nextgen-healthcare/vendors/nextgen-healthcare-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nextgen-healthcare-vendors.yml
- group: build
  href: https://artifacts.apis.io/nextgen-healthcare/packages/nextgen-healthcare-packages.yml
  title: ''
  type: SDKs
  url: packages/nextgen-healthcare-packages.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.nextgen.com/company/leadership
- group: other
  href: https://artifacts.apis.io/nextgen-healthcare/capabilities/nextgen-healthcare-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/nextgen-healthcare-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/nextgen-healthcare/security/nextgen-healthcare-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nextgen-healthcare-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/nextgen-healthcare/agentic-access/nextgen-healthcare-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/nextgen-healthcare-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/nextgen-healthcare/scopes/nextgen-healthcare-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/nextgen-healthcare-scopes.yml
- group: auth
  href: https://artifacts.apis.io/nextgen-healthcare/authentication/nextgen-healthcare-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nextgen-healthcare-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.nextgen.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.nextgen.com/developer-program
- group: start
  title: ''
  type: Portal
  url: https://developer.nextgen.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.nextgen.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://www.nextgen.com/api/regulatory-nge
- group: start
  title: ''
  type: GettingStarted
  url: https://www.nextgen.com/api-on-boarding
- group: other
  title: ''
  type: Marketplace
  url: https://www.nextgen.com/marketplace
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NextGenHealthcare
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nextgen-healthcare-information-systems
- group: company
  title: ''
  type: Blog
  url: https://www.nextgen.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.nextgen.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nextgen.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nextgen.com/legal/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.nextgen.com/trust
- group: auth
  title: ''
  type: Compliance
  url: https://www.nextgen.com/trust
- group: design
  href: https://artifacts.apis.io/nextgen-healthcare/conformance/nextgen-healthcare-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nextgen-healthcare-conformance.yml
- group: agent
  href: https://artifacts.apis.io/nextgen-healthcare/well-known/nextgen-healthcare-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nextgen-healthcare-well-known.yml
- group: design
  href: https://artifacts.apis.io/nextgen-healthcare/conventions/nextgen-healthcare-conventions.yml
  title: ''
  type: Conventions
  url: conventions/nextgen-healthcare-conventions.yml
- group: design
  href: https://artifacts.apis.io/nextgen-healthcare/errors/nextgen-healthcare-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/nextgen-healthcare-problem-types.yml
- group: design
  href: https://artifacts.apis.io/nextgen-healthcare/lifecycle/nextgen-healthcare-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/nextgen-healthcare-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/nextgen-healthcare/data-model/nextgen-healthcare-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nextgen-healthcare-data-model.yml
- group: build
  href: https://artifacts.apis.io/nextgen-healthcare/packages/nextgen-healthcare-packages.yml
  title: ''
  type: Packages
  url: packages/nextgen-healthcare-packages.yml
- group: agent
  href: https://artifacts.apis.io/nextgen-healthcare/llms/nextgen-healthcare-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nextgen-healthcare-llms.txt
- group: agent
  href: https://artifacts.apis.io/nextgen-healthcare/mcp/nextgen-healthcare-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/nextgen-healthcare-mcp.yml
- group: agent
  href: https://artifacts.apis.io/nextgen-healthcare/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/nextgen-healthcare/overlays/nextgen-healthcare-office-fhir-r4-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/nextgen-healthcare-office-fhir-r4-overlay.yaml
- group: other
  href: https://artifacts.apis.io/nextgen-healthcare/overlays/nextgen-healthcare-office-bulk-fhir-r4-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/nextgen-healthcare-office-bulk-fhir-r4-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev-cd.nextgen.com/api
- group: other
  title: ''
  type: DeveloperProgram
  url: https://www.nextgen.com/developer-program
- group: other
  title: ''
  type: Marketplace
  url: https://www.nextgen.com/solutions/marketplace
- group: build
  title: ''
  type: GitHub
  url: https://github.com/nextgenhealthcare
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nextgenhealthcareinc
- group: other
  title: ''
  type: X
  url: https://twitter.com/nextgen
- group: company
  title: ''
  type: Newsroom
  url: https://www.nextgen.com/company/newsroom
- group: other
  title: ''
  type: Interoperability
  url: https://www.nextgen.com/solutions/interoperability/api-fhir
- group: commercial
  href: https://artifacts.apis.io/nextgen-healthcare/plans/nextgen-healthcare-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nextgen-healthcare-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/nextgen-healthcare/rate-limits/nextgen-healthcare-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/nextgen-healthcare-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/nextgen-healthcare/finops/nextgen-healthcare-finops.yml
  title: ''
  type: FinOps
  url: finops/nextgen-healthcare-finops.yml
- group: build
  href: https://artifacts.apis.io/nextgen-healthcare/cli/nextgen-healthcare-cli.yml
  title: ''
  type: CLI
  url: cli/nextgen-healthcare-cli.yml
- group: operate
  href: https://artifacts.apis.io/nextgen-healthcare/changelog/nextgen-healthcare-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/nextgen-healthcare-changelog.yml
- group: start
  href: https://artifacts.apis.io/nextgen-healthcare/sandbox/nextgen-healthcare-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/nextgen-healthcare-sandbox.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nextgen.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://developer.nextgen.com/login?returnUrl=%2F
created: '2026-07-24'
description: 'NextGen Healthcare is a United States ambulatory electronic health record (EHR/EMR) and practice-management vendor headquartered in Remote-first / Atlanta, Georgia, serving outpatient specialties and community health with its NextGen Enterprise and NextGen Office platforms plus the Mirth Connect interoperability engine. Its developer surface is standards-driven: 21st Century Cures Act-certified HL7 FHIR APIs for patient access and provider apps, a SMART App Launch API, and a Bulk FHIR (Flat FHIR) API delivering USCDI data, alongside an 800+ route JSON RESTful Enterprise API family. NextGen Enterprise exposes live FHIR R4 and DSTU2 service base URLs with SMART-on-FHIR OAuth2, and NextGen Office exposes live FHIR R3/R4 and Bulk FHIR endpoints. FHIR resources are coded against the US Core / USCDIv1 implementation guides. Developer onboarding is gated behind an API onboarding form and app registration, which is standard for regulated health-data access in the US market.'
finops:
- has_sources: true
  method: derived
  name: Nextgen Healthcare Finops
  primary_unit: ''
  service_category: ''
  slug: nextgen-healthcare-finops
  template: true
image: https://nextgen.widen.net/content/mcckjhwu0f/svg/NG_Logo_Final_RGB.svg
json_schemas:
- name: AllergyIntoleranceBundled
  property_count: 7
  slug: nextgen-healthcare-allergy-intolerance-bundled
- name: AllergyIntolerance
  property_count: 9
  slug: nextgen-healthcare-allergy-intolerance
- name: BulkDataStatusResponse
  property_count: 5
  slug: nextgen-healthcare-bulk-data-status-response
- name: CarePlanBundled
  property_count: 7
  slug: nextgen-healthcare-care-plan-bundled
- name: CarePlan
  property_count: 9
  slug: nextgen-healthcare-care-plan
- name: CareTeamBundled
  property_count: 7
  slug: nextgen-healthcare-care-team-bundled
- name: ConditionBundled
  property_count: 7
  slug: nextgen-healthcare-condition-bundled
- name: Condition
  property_count: 10
  slug: nextgen-healthcare-condition
- name: CoverageBundled
  property_count: 7
  slug: nextgen-healthcare-coverage-bundled
- name: Coverage
  property_count: 12
  slug: nextgen-healthcare-coverage
- name: CreateBulkFhirPatientGroup
  property_count: 3
  slug: nextgen-healthcare-create-bulk-fhir-patient-group
- name: DeviceBundled
  property_count: 7
  slug: nextgen-healthcare-device-bundled
- name: Device
  property_count: 14
  slug: nextgen-healthcare-device
- name: DiagnosticReportBundled
  property_count: 7
  slug: nextgen-healthcare-diagnostic-report-bundled
- name: DiagnosticReport
  property_count: 12
  slug: nextgen-healthcare-diagnostic-report
- name: DocumentReferenceBundled
  property_count: 7
  slug: nextgen-healthcare-document-reference-bundled
- name: EncounterBundled
  property_count: 7
  slug: nextgen-healthcare-encounter-bundled
- name: Encounter
  property_count: 13
  slug: nextgen-healthcare-encounter
- name: GoalBundled
  property_count: 7
  slug: nextgen-healthcare-goal-bundled
- name: Goal
  property_count: 7
  slug: nextgen-healthcare-goal
- name: ImmunizationBundled
  property_count: 7
  slug: nextgen-healthcare-immunization-bundled
- name: Immunization
  property_count: 9
  slug: nextgen-healthcare-immunization
- name: Location
  property_count: 9
  slug: nextgen-healthcare-location
- name: MedicationAdministrationBundled
  property_count: 7
  slug: nextgen-healthcare-medication-administration-bundled
- name: MedicationAdministration
  property_count: 11
  slug: nextgen-healthcare-medication-administration
- name: MedicationDispenseBundled
  property_count: 7
  slug: nextgen-healthcare-medication-dispense-bundled
- name: MedicationDispense
  property_count: 11
  slug: nextgen-healthcare-medication-dispense
- name: MedicationRequestBundled
  property_count: 7
  slug: nextgen-healthcare-medication-request-bundled
- name: MedicationRequest
  property_count: 15
  slug: nextgen-healthcare-medication-request
- name: ObservationBundled
  property_count: 7
  slug: nextgen-healthcare-observation-bundled
- name: Observation
  property_count: 12
  slug: nextgen-healthcare-observation
- name: Organization
  property_count: 8
  slug: nextgen-healthcare-organization
- name: PatientBundled
  property_count: 6
  slug: nextgen-healthcare-patient-bundled
- name: Patient
  property_count: 12
  slug: nextgen-healthcare-patient
- name: PractitionerRoleBundled
  property_count: 7
  slug: nextgen-healthcare-practitioner-role-bundled
- name: PractitionerRole
  property_count: 9
  slug: nextgen-healthcare-practitioner-role
- name: Practitioner
  property_count: 7
  slug: nextgen-healthcare-practitioner
- name: ProcedureBundled
  property_count: 7
  slug: nextgen-healthcare-procedure-bundled
- name: Procedure
  property_count: 7
  slug: nextgen-healthcare-procedure
- name: Provenance
  property_count: 6
  slug: nextgen-healthcare-provenance
- name: RelatedPersonBundled
  property_count: 7
  slug: nextgen-healthcare-related-person-bundled
- name: RelatedPerson
  property_count: 9
  slug: nextgen-healthcare-related-person
- name: SpecimenBundled
  property_count: 4
  slug: nextgen-healthcare-specimen-bundled
- name: Specimen
  property_count: 6
  slug: nextgen-healthcare-specimen
- name: UpdateBulkFhirPatientGroup
  property_count: 5
  slug: nextgen-healthcare-update-bulk-fhir-patient-group
jsonld:
- class_count: 22
  name: Nextgen Healthcare Context
  property_count: 2
  slug: nextgen-healthcare-context
layout: provider
modified: '2026-08-14'
name: NextGen Healthcare
nav: Providers
network: true
overview: 'NextGen Healthcare publishes 35 API contracts indexed on the [APIs.io](https://apis.io/) network, including Care Team API, CCDA API, Condition API, and 32 more. Tagged areas include Healthcare, United States, Electronic Health Records, FHIR, and HL7.


  The NextGen Healthcare catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  NextGen Healthcare''s developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, engineering blog, support, and 49 more developer resources.'
plans:
- name: Nextgen Healthcare Plans Pricing
  plan_count: 3
  slug: nextgen-healthcare-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Nextgen Healthcare Rate Limits
  slug: nextgen-healthcare-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: NextGen Healthcare API Rules
  rule_count: 17
  severity_counts:
    error: 14
    hint: 0
    info: 2
    warn: 1
  slug: nextgen-healthcare-rules
scopes:
- name: Nextgen Healthcare Scopes
  scope_count: 12
  slug: nextgen-healthcare-scopes
  summary_line: 12 scopes · authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 66.5
  coverage:
    artifact_dirs: 37
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 78.9
    contract_governance: 35.6
    contract_quality: 68.7
    developer_ergonomics: 70.8
    discoverability: 75.0
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 66.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 28
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 51.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/nextgen-healthcare/nextgen-healthcare-2026-08-07T185204.png
security:
- kind: authentication
  name: Nextgen Healthcare Authentication
  slug: nextgen-healthcare-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Nextgen Healthcare Domain Security
  slug: nextgen-healthcare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Nextgen Healthcare Trust Center
  slug: nextgen-healthcare-trust-center
  summary_line: SOC 2 Type II, HITRUST CSF, ISO 27001, HIPAA, PCI DSS, NIST
skill_count: 2
skills:
- name: nextgen-office-bulk-fhir-export
  slug: nextgen-healthcare-bulk-fhir-export
- name: smart-patient-access
  slug: nextgen-healthcare-smart-patient-access
slug: nextgen-healthcare
tags:
- Healthcare
- United States
- Electronic Health Records
- FHIR
- HL7
- Interoperability
- SMART on FHIR
- USCDI
- Bulk FHIR
- Patient Access
- 21st Century Cures
website: https://www.nextgen.com/
---

---
access_model:
  confidence: medium
  label: Freemium · Requires approval
  onboarding: approval
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.6
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Athenahealth Agentic Access
  operation_count: 40
  slug: athenahealth-agentic-access
  summary_line: 40 operations · 9 acting
api_count: 5
apis:
- description: The athenaOne proprietary REST API suite provides over 800 endpoints covering patient management, scheduling, clinical data, revenue cycle, and care coordination. Requires OAuth 2.0 authentication and
  name: athenaOne APIs
  slug: athenaone-apis
- description: athenahealth FHIR R4 APIs provide standards-based access to clinical and administrative data. Supports SMART on FHIR scopes for compliant patient and provider-facing applications. Includes FHIR Subscr
  name: FHIR APIs
  slug: fhir-apis
- description: FHIR API Server for athenaPractice and athenaFlow products, enabling developers to build integrations with athenahealth's on-premise and hybrid deployment products using FHIR R4 standards.
  name: athenaFlex (athenaPractice/athenaFlow) API
  slug: athenaflex-api
- baseURL: https://api.platform.athenahealth.com/v1/{practiceid}
  baseurl_source: declared
  description: The Appointment API from athenahealth — 1 operation(s) for appointment.
  name: athenahealth Appointment API
  phrasing_intents:
  - id: searchFhirAppointments
    intent: Search FHIR Appointment resources
    question: How do I get a patient's appointments as FHIR Appointment resources?
  phrasing_ops: 1
  slug: athena-health-appointment-api
- baseURL: https://api.platform.athenahealth.com/v1/{practiceid}
  baseurl_source: declared
  description: The Appointments API from athenahealth — 6 operation(s) for appointments.
  name: athenahealth Appointments API
  phrasing_intents:
  - id: searchAppointments
    intent: Find booked appointments in a department
    question: Which appointments are booked in a department this week?
  - id: getOpenAppointmentSlots
    intent: Find open appointment slots
    question: Where can I see open slots a patient could book in a department?
  - id: getAppointment
    intent: Look up one appointment
    question: How do I pull the details of a single appointment by its ID?
  - id: cancelAppointment
    intent: Cancel an appointment
    question: How do I cancel a patient's scheduled appointment?
  - id: checkInAppointment
    intent: Check a patient in for an appointment
    question: How do I mark a patient as arrived for their appointment?
  - id: rescheduleAppointment
    intent: Reschedule an appointment
    question: How do I move an existing appointment to a different time?
  phrasing_ops: 6
  slug: athena-health-appointments-api
- baseURL: https://api.platform.athenahealth.com/v1/{practiceid}
  baseurl_source: declared
  description: The Bulk Data API from athenahealth — 2 operation(s) for bulk data.
  name: athenahealth Bulk Data API
  phrasing_intents:
  - id: groupBulkExport
    intent: Start a bulk FHIR export for a patient group
    question: How do I export all FHIR data for a group of patients at once?
  - id: getBulkExportStatus
    intent: Check progress of a bulk export job
    question: Is my bulk data export finished yet?
  - id: cancelBulkExport
    intent: Cancel a running bulk export
    question: How do I stop a bulk export that is still running?
  phrasing_ops: 3
  slug: athena-health-bulk-data-api
- baseURL: https://api.platform.athenahealth.com/v1/{practiceid}
  baseurl_source: declared
  description: The CDS Hooks API from athenahealth — 2 operation(s) for cds hooks.
  name: athenahealth CDS Hooks API
  phrasing_intents:
  - id: discoverCdsServices
    intent: Discover available CDS Hooks services
    question: Which clinical decision support services can I call?
  - id: invokeCdsService
    intent: Invoke a CDS Hooks service for decision cards
    question: How do I call a CDS service to get decision support cards for a patient context?
  phrasing_ops: 2
  slug: athena-health-cds-hooks-api
- baseURL: https://api.platform.athenahealth.com/v1/{practiceid}
  baseurl_source: declared
  description: The Claims API from athenahealth — 1 operation(s) for claims.
  name: athenahealth Claims API
  phrasing_intents:
  - id: searchClaims
    intent: Search billing claims
    question: Which claims have been filed for a patient?
  phrasing_ops: 1
  slug: athena-health-claims-api
- baseURL: https://api.platform.athenahealth.com/v1/{practiceid}
  baseurl_source: declared
  description: The Condition API from athenahealth — 1 operation(s) for condition.
  name: athenahealth Condition API
  phrasing_intents:
  - id: searchFhirConditions
    intent: Get a patient's conditions and problems
    question: What diagnoses or problems are on a patient's list?
  phrasing_ops: 1
  slug: athena-health-condition-api
- baseURL: https://api.platform.athenahealth.com/v1/{practiceid}
  baseurl_source: declared
  description: The Conformance API from athenahealth — 1 operation(s) for conformance.
  name: athenahealth Conformance API
  phrasing_intents:
  - id: getCapabilityStatement
    intent: Get the FHIR server capability statement
    question: Which FHIR resources and interactions does the server support?
  phrasing_ops: 1
  slug: athena-health-conformance-api
- baseURL: https://api.platform.athenahealth.com/v1/{practiceid}
  baseurl_source: declared
  description: The Departments API from athenahealth — 1 operation(s) for departments.
  name: athenahealth Departments API
  phrasing_intents:
  - id: listDepartments
    intent: List practice departments
    question: What departments does my practice have?
  phrasing_ops: 1
  slug: athena-health-departments-api
- baseURL: https://api.platform.athenahealth.com/v1/{practiceid}
  baseurl_source: declared
  description: The DiagnosticReport API from athenahealth — 1 operation(s) for diagnosticreport.
  name: athenahealth DiagnosticReport API
  phrasing_intents:
  - id: searchFhirDiagnosticReports
    intent: Get a patient's diagnostic reports
    question: What lab or imaging reports exist for a patient?
  phrasing_ops: 1
  slug: athena-health-diagnosticreport-api
- baseURL: https://api.platform.athenahealth.com/v1/{practiceid}
  baseurl_source: declared
  description: The Documents API from athenahealth — 1 operation(s) for documents.
  name: athenahealth Documents API
  phrasing_intents:
  - id: listPatientDocuments
    intent: List documents in a patient's chart
    question: Which documents are attached to a patient's athenaOne chart?
  phrasing_ops: 1
  slug: athena-health-documents-api
- baseURL: https://api.platform.athenahealth.com/v1/{practiceid}
  baseurl_source: declared
  description: The Encounter API from athenahealth — 2 operation(s) for encounter.
  name: athenahealth Encounter API
  phrasing_intents:
  - id: searchFhirEncounters
    intent: Search FHIR Encounter resources
    question: How do I find a patient's encounters as FHIR Encounter resources?
  - id: readFhirEncounter
    intent: Read one FHIR Encounter resource
    question: How do I fetch a single FHIR Encounter by its resource id?
  phrasing_ops: 2
  slug: athena-health-encounter-api
- baseURL: https://api.platform.athenahealth.com/v1/{practiceid}
  baseurl_source: declared
  description: The Encounters API from athenahealth — 2 operation(s) for encounters.
  name: athenahealth Encounters API
  phrasing_intents:
  - id: listPatientEncounters
    intent: List a patient's chart encounters
    question: Which visits are recorded in a patient's chart?
  - id: getEncounter
    intent: Get one chart encounter
    question: How do I open a specific chart encounter by encounter ID?
  phrasing_ops: 2
  slug: athena-health-encounters-api
- baseURL: https://api.platform.athenahealth.com/v1/{practiceid}
  baseurl_source: declared
  description: The Immunization API from athenahealth — 1 operation(s) for immunization.
  name: athenahealth Immunization API
  phrasing_intents:
  - id: searchFhirImmunizations
    intent: Get a patient's immunization history
    question: Which vaccines has a patient received?
  phrasing_ops: 1
  slug: athena-health-immunization-api
- baseURL: https://api.platform.athenahealth.com/v1/{practiceid}
  baseurl_source: declared
  description: The Observation API from athenahealth — 1 operation(s) for observation.
  name: athenahealth Observation API
  phrasing_intents:
  - id: searchFhirObservations
    intent: Search a patient's observations and vitals
    question: How do I get a patient's vital signs or lab results as observations?
  phrasing_ops: 1
  slug: athena-health-observation-api
- baseURL: https://api.platform.athenahealth.com/v1/{practiceid}
  baseurl_source: declared
  description: The Patient API from athenahealth — 2 operation(s) for patient.
  name: athenahealth Patient API
  phrasing_intents:
  - id: searchFhirPatients
    intent: Search FHIR Patient resources
    question: How do I search FHIR Patient resources by family and given name?
  - id: readFhirPatient
    intent: Read one FHIR Patient resource
    question: How do I fetch a FHIR Patient resource by its logical id?
  phrasing_ops: 2
  slug: athena-health-patient-api
- baseURL: https://api.platform.athenahealth.com/v1/{practiceid}
  baseurl_source: declared
  description: The Patients API from athenahealth — 2 operation(s) for patients.
  name: athenahealth Patients API
  phrasing_intents:
  - id: searchPatients
    intent: Search patients by name or birth date
    question: How do I find a patient in athenaOne by first and last name?
  - id: createPatient
    intent: Register a new patient
    question: How do I register a brand-new patient in a department?
  - id: getPatient
    intent: Get a patient's demographics by patient ID
    question: How do I pull up a patient's record when I know their athenaOne patient ID?
  - id: updatePatient
    intent: Update a patient's contact details
    question: How do I change a patient's mobile phone or email on file?
  phrasing_ops: 4
  slug: athena-health-patients-api
- baseURL: https://api.platform.athenahealth.com/v1/{practiceid}
  baseurl_source: declared
  description: The Practice API from athenahealth — 1 operation(s) for practice.
  name: athenahealth Practice API
  phrasing_intents:
  - id: getPracticeInfo
    intent: Get practice information
    question: What practice details does my athenahealth account expose?
  phrasing_ops: 1
  slug: athena-health-practice-api
- baseURL: https://api.platform.athenahealth.com/v1/{practiceid}
  baseurl_source: declared
  description: The Providers API from athenahealth — 1 operation(s) for providers.
  name: athenahealth Providers API
  phrasing_intents:
  - id: listProviders
    intent: List providers in the practice
    question: Which clinicians are set up as providers in the practice?
  phrasing_ops: 1
  slug: athena-health-providers-api
- baseURL: https://api.platform.athenahealth.com/v1/{practiceid}
  baseurl_source: declared
  description: The Subscription API from athenahealth — 3 operation(s) for subscription.
  name: athenahealth Subscription API
  phrasing_intents:
  - id: searchSubscriptions
    intent: List FHIR event subscriptions
    question: Which FHIR subscriptions have I already set up?
  - id: createSubscription
    intent: Subscribe to FHIR resource change notifications
    question: How do I get notified when FHIR resources matching some criteria change?
  - id: readSubscription
    intent: Read one FHIR subscription
    question: How do I see the criteria and channel of one subscription I created?
  - id: deleteSubscription
    intent: Delete a FHIR subscription
    question: How do I stop receiving notifications from a subscription?
  - id: getSubscriptionStatus
    intent: Check a FHIR subscription's delivery status
    question: Is my FHIR subscription healthy and delivering events?
  phrasing_ops: 5
  slug: athena-health-subscription-api
- baseURL: https://api.platform.athenahealth.com/v1/{practiceid}
  baseurl_source: declared
  description: The Allergy Intolerance API from athenahealth — 1 operation(s) for allergy intolerance.
  name: athenahealth Allergy Intolerance API
  phrasing_intents:
  - id: searchFhirAllergies
    intent: Get a patient's allergies
    question: What allergies does a patient have on record?
  phrasing_ops: 1
  slug: athenahealth-allergy-intolerance-api
- baseURL: https://api.platform.athenahealth.com/v1/{practiceid}
  baseurl_source: declared
  description: The Document Reference API from athenahealth — 1 operation(s) for document reference.
  name: athenahealth Document Reference API
  phrasing_intents:
  - id: searchFhirDocumentReferences
    intent: Search FHIR DocumentReference resources
    question: How do I find clinical documents for a patient as FHIR DocumentReferences?
  phrasing_ops: 1
  slug: athenahealth-document-reference-api
- baseURL: https://api.platform.athenahealth.com/v1/{practiceid}
  baseurl_source: declared
  description: The Medication Request API from athenahealth — 1 operation(s) for medication request.
  name: athenahealth Medication Request API
  phrasing_intents:
  - id: searchFhirMedicationRequests
    intent: Get a patient's medication orders
    question: What medications have been prescribed to a patient?
  phrasing_ops: 1
  slug: athenahealth-medication-request-api
artifact_total: 70
asyncapis:
- description: Event-driven notifications from the athenahealth Event Subscription Platform. Delivered as FHIR Bundle notifications (R5 Backport) over rest-hook channel with id-only payloads. Subscriber webhooks mus
  name: athenahealth FHIR Subscriptions Events
  slug: athenahealth-fhir-subscriptions-asyncapi
collections:
- collection_type: open
  name: athenahealth athenaOne REST AllergyIntolerance API
  slug: open-athenahealth-allergyintolerance-api
- collection_type: open
  name: athenahealth athenaOne REST AllergyIntolerance Appointment API
  slug: open-athenahealth-appointment-api
- collection_type: open
  name: athenahealth athenaOne REST AllergyIntolerance Appointments API
  slug: open-athenahealth-appointments-api
- collection_type: open
  name: athenahealth athenaOne REST API
  slug: open-athenahealth-athenaone-rest-api
- collection_type: open
  name: athenahealth athenaOne REST AllergyIntolerance Bulk Data API
  slug: open-athenahealth-bulk-data-api
- collection_type: open
  name: athenahealth athenaOne REST AllergyIntolerance CDS Hooks API
  slug: open-athenahealth-cds-hooks-api
- collection_type: open
  name: athenahealth athenaOne REST AllergyIntolerance Claims API
  slug: open-athenahealth-claims-api
- collection_type: open
  name: athenahealth athenaOne REST AllergyIntolerance Condition API
  slug: open-athenahealth-condition-api
- collection_type: open
  name: athenahealth athenaOne REST AllergyIntolerance Conformance API
  slug: open-athenahealth-conformance-api
- collection_type: open
  name: athenahealth athenaOne REST AllergyIntolerance Departments API
  slug: open-athenahealth-departments-api
- collection_type: open
  name: athenahealth athenaOne REST AllergyIntolerance DiagnosticReport API
  slug: open-athenahealth-diagnosticreport-api
- collection_type: open
  name: athenahealth athenaOne REST AllergyIntolerance DocumentReference API
  slug: open-athenahealth-documentreference-api
- collection_type: open
  name: athenahealth athenaOne REST AllergyIntolerance Documents API
  slug: open-athenahealth-documents-api
- collection_type: open
  name: athenahealth athenaOne REST AllergyIntolerance Encounter API
  slug: open-athenahealth-encounter-api
- collection_type: open
  name: athenahealth athenaOne REST AllergyIntolerance Encounters API
  slug: open-athenahealth-encounters-api
- collection_type: open
  name: athenahealth FHIR Bulk Data Access API
  slug: open-athenahealth-fhir-bulk-data-api
- collection_type: open
  name: athenahealth FHIR R4 API
  slug: open-athenahealth-fhir-r4-api
- collection_type: open
  name: athenahealth FHIR Subscriptions API
  slug: open-athenahealth-fhir-subscriptions-api
- collection_type: open
  name: athenahealth athenaOne REST AllergyIntolerance Immunization API
  slug: open-athenahealth-immunization-api
- collection_type: open
  name: athenahealth athenaOne REST AllergyIntolerance MedicationRequest API
  slug: open-athenahealth-medicationrequest-api
- collection_type: open
  name: athenahealth athenaOne REST AllergyIntolerance Observation API
  slug: open-athenahealth-observation-api
- collection_type: open
  name: athenahealth athenaOne REST AllergyIntolerance Patient API
  slug: open-athenahealth-patient-api
- collection_type: open
  name: athenahealth athenaOne REST AllergyIntolerance Patients API
  slug: open-athenahealth-patients-api
- collection_type: open
  name: athenahealth athenaOne REST AllergyIntolerance Practice API
  slug: open-athenahealth-practice-api
- collection_type: open
  name: athenahealth athenaOne REST AllergyIntolerance Providers API
  slug: open-athenahealth-providers-api
- collection_type: open
  name: athenahealth athenaOne REST AllergyIntolerance Subscription API
  slug: open-athenahealth-subscription-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/overlays/athenahealth-allergyintolerance-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/athenahealth-allergyintolerance-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/overlays/athenahealth-documentreference-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/athenahealth-documentreference-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/overlays/athenahealth-medicationrequest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/athenahealth-medicationrequest-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/capabilities/athenahealth-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/athenahealth-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/athenahealth/aone-fhir-subscriptions/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/athenahealth/aone-fhir-subscriptions/blob/main/LICENSE
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/security/athenahealth-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/athenahealth-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.athenahealth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.athenahealth.com/api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.athenahealth.com/developer-portal
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/athenahealth
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/athenahealth
- group: company
  title: ''
  type: Blog
  url: https://www.athenahealth.com/resources/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.athenahealth.com/why-choose-us/cost-value
- group: operate
  title: ''
  type: StatusPage
  url: https://status.athenahealth.com/
- group: other
  title: ''
  type: X
  url: https://x.com/athenahealth
- group: other
  title: ''
  type: Marketplace
  url: https://www.athenahealth.com/solutions/marketplace-partners
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/plans/athenahealth-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/athenahealth-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/rate-limits/athenahealth-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/athenahealth-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/finops/athenahealth-finops.yml
  title: ''
  type: FinOps
  url: finops/athenahealth-finops.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/agentic-access/athenahealth-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/athenahealth-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/security/athenahealth-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/athenahealth-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/authentication/athenahealth-authentication.yml
  title: ''
  type: Authentication
  url: authentication/athenahealth-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/scopes/athenahealth-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/athenahealth-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://www.athenahealth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.athenahealth.com/api/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.athenahealth.com/api/guides/overview
- group: start
  title: ''
  type: Portal
  url: https://mydata.athenahealth.com/access-the-apis
- group: start
  title: ''
  type: Sandbox
  url: https://docs.athenahealth.com/api/sandbox
- group: docs
  title: ''
  type: Documentation
  url: https://docs.athenahealth.com/api/guides/athenaone-environments
- group: docs
  title: ''
  type: Documentation
  url: https://docs.athenahealth.com/api/guides/base-fhir-urls
- group: docs
  title: ''
  type: Documentation
  url: https://docs.athenahealth.com/api/guides/onboarding-overview
- group: operate
  title: ''
  type: Support
  url: https://docs.athenahealth.com/api/support
- group: other
  title: ''
  type: Marketplace
  url: https://www.athenahealth.com/solutions/marketplace
- group: company
  title: ''
  type: Blog
  url: https://www.athenahealth.com/knowledge-hub
- group: other
  title: ''
  type: Source
  url: https://github.com/athenahealth
- group: docs
  title: ''
  type: Documentation
  url: https://fhir.athena.io/athenacoreext/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://mydata.athenahealth.com/fhirapidoc/r4
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/plans/athenahealth-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/athenahealth-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/rate-limits/athenahealth-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/athenahealth-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/finops/athenahealth-finops.yml
  title: ''
  type: FinOps
  url: finops/athenahealth-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/vocabulary/athenahealth-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/athenahealth-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/rules/athenahealth-rules.yml
  title: ''
  type: Spectral
  url: rules/athenahealth-rules.yml
- group: build
  title: ''
  type: Examples
  url: https://github.com/athenahealth/mdp
- group: build
  title: ''
  type: Examples
  url: https://github.com/athenahealth/apiserver-athenaFlex
- group: build
  title: ''
  type: Examples
  url: https://github.com/athenahealth/aone-fhir-subscriptions
- group: build
  title: ''
  type: Tools
  url: https://github.com/athenahealth/vscode-cql-extension
- group: build
  title: ''
  type: SDKs
  url: https://github.com/eleanorhealth/go-athenahealth
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/agentic-access/athenahealth-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/athenahealth-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/security/athenahealth-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/athenahealth-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/authentication/athenahealth-authentication.yml
  title: ''
  type: Authentication
  url: authentication/athenahealth-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/scopes/athenahealth-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/athenahealth-scopes.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/plans/athenahealth-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/athenahealth-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/rate-limits/athenahealth-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/athenahealth-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/finops/athenahealth-finops.yml
  title: ''
  type: FinOps
  url: finops/athenahealth-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/vocabulary/athenahealth-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/athenahealth-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/rules/athenahealth-rules.yml
  title: ''
  type: Spectral
  url: rules/athenahealth-rules.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/packages/athenahealth-packages.yml
  title: ''
  type: Packages
  url: packages/athenahealth-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/well-known/athenahealth-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/athenahealth-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/mcp/athenahealth-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/athenahealth-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/mcp/athenahealth-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/athenahealth-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/llms/athenahealth-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/athenahealth-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/conformance/athenahealth-conformance.yml
  title: ''
  type: Conformance
  url: conformance/athenahealth-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/security/athenahealth-trust-center.yml
  title: ''
  type: Compliance
  url: security/athenahealth-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/security/athenahealth-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/athenahealth-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/errors/athenahealth-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/athenahealth-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/lifecycle/athenahealth-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/athenahealth-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/conventions/athenahealth-conventions.yml
  title: ''
  type: Conventions
  url: conventions/athenahealth-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/changelog/athenahealth-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/athenahealth-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/data-model/athenahealth-data-model.yml
  title: ''
  type: DataModel
  url: data-model/athenahealth-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/sandbox/athenahealth-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/athenahealth-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/asyncapi/athenahealth-fhir-subscriptions-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/athenahealth-fhir-subscriptions-asyncapi.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/asyncapi/athenahealth-fhir-subscriptions-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/athenahealth-fhir-subscriptions-asyncapi.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/conformance/athenahealth-fhir-capabilitystatement.json
  title: ''
  type: CapabilityStatement
  url: conformance/athenahealth-fhir-capabilitystatement.json
- group: docs
  title: ''
  type: APIReference
  url: https://docs.athenahealth.com/api/api-ref
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.athenahealth.com/api/guides/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/athenahealth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.athenahealth.com/terms-and-conditions/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.athenahealth.com/privacy-rights
- group: start
  title: ''
  type: SignUp
  url: https://mydata.athenahealth.com/access-the-apis
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.athenahealth.com/api/resources/release-notes-and-change-logs
created: '2026-06-13'
description: athenahealth is a cloud-based healthcare network offering REST APIs for electronic health records (EHR), practice management, patient portal, revenue cycle management, and care coordination across ambulatory and acute care settings. The platform provides over 800 API endpoints enabling developers to extend athenaOne and integrate clinical, financial, and operational workflows across a national network of 84,000+ care sites.
examples:
- key_count: 2
  name: Athenahealth Fhir Read Patient Example
  slug: athenahealth-fhir-read-patient-example
- key_count: 2
  name: Athenahealth Search Patients Example
  slug: athenahealth-search-patients-example
- key_count: 2
  name: Athenahealth Subscription Notification Example
  slug: athenahealth-subscription-notification-example
finops:
- name: Athenahealth Finops
  service_category: ''
  slug: athenahealth-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/athenahealth.png
json_schemas:
- name: athenahealth Appointment
  property_count: 14
  slug: athenahealth-appointment
- name: athenahealth FHIR R4 Patient (US Core profile)
  property_count: 11
  slug: athenahealth-fhir-patient
- name: athenahealth Patient
  property_count: 20
  slug: athenahealth-patient
jsonld:
- class_count: 27
  name: Athenahealth Context
  property_count: 0
  slug: athenahealth-context
layout: provider
modified: '2026-08-14'
name: athenahealth
nav: Providers
network: true
overview: 'athenahealth publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Appointment API, Appointments API, Bulk Data API, and 22 more. Tagged areas include Healthcare, EHR, Electronic Health Records, Practice Management, and Revenue Cycle Management.


  The athenahealth catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  athenahealth''s developer surface includes documentation, engineering blog, pricing, authentication, developer portal, sandbox, support, and 75 more developer resources.'
plans:
- name: Athenahealth Plans Pricing
  plan_count: 0
  slug: athenahealth-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Athenahealth Rate Limits
  slug: athenahealth-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: athenahealth API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: athenahealth-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: athenahealth API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: athenahealth-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: athenahealth API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 4
  slug: athenahealth-rules
scopes:
- name: Athenahealth Scopes
  scope_count: 1
  slug: athenahealth-scopes
  summary_line: 1 scope · clientCredentials/authorizationCode
score:
  band: exemplar
  composite: 69.6
  coverage:
    artifact_dirs: 32
    catalog_earned: 69.0
    catalog_earned_first_party: 0.0
    catalog_gap: 46.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 68.4
    contract_governance: 45.5
    contract_quality: 69.3
    developer_ergonomics: 73.2
    discoverability: 78.6
    operational_transparency: 42.1
  previous_composite: 69.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 95.5
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 51.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/screenshots/athenahealth-2026-06-20T172519.png
security:
- kind: authentication
  name: Athenahealth Authentication
  slug: athenahealth-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Athenahealth Domain Security
  slug: athenahealth-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Athenahealth Trust Center
  slug: athenahealth-trust-center
  summary_line: HITRUST CSF Certified, PCI DSS, SOC 1 (SSAE 18), EPCS (Electronic Prescriptions for Controlled Substances), DirectTrust HISP accreditation, DirectTrust CA/RA accreditation, Kantara full-service Credentialing Service Provider, EHNAC accreditation, ONC Certified Health IT, 2015 Edition
slug: athenahealth
tags:
- Healthcare
- EHR
- Electronic Health Records
- Practice Management
- Revenue Cycle Management
- Patient Portal
- FHIR
- Care Coordination
- Interoperability
- HL7
website: https://www.athenahealth.com/
---

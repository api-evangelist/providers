---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 30
  human_in_the_loop: 0
  name: Canvas Medical Agentic Access
  operation_count: 85
  slug: canvas-medical-agentic-access
  summary_line: 85 operations · 30 acting
api_count: 1
apis:
- description: A FHIR R4-compliant REST API providing secure access to electronic health record data including 41 FHIR resources (21 with write capabilities) covering clinical, administrative, financial, and care co
  name: Canvas Medical FHIR API
  slug: canvas-medical-fhir-api
- description: A Python SDK that enables developers to build plugins that execute natively within the Canvas EMR infrastructure. Supports an event-driven architecture with over 650 clinical and operational events, D
  name: Canvas Medical SDK
  slug: canvas-medical-sdk
- baseURL: https://fumage-{canvas-instance}.canvasmedical.com
  baseurl_source: declared
  description: Appointment scheduling and management
  name: Canvas Medical Appointment API
  slug: canvas-medical-appointment-api
- baseURL: https://fumage-{canvas-instance}.canvasmedical.com
  baseurl_source: declared
  description: Care team coordination
  name: Canvas Medical CareTeam API
  slug: canvas-medical-careteam-api
- baseURL: https://fumage-{canvas-instance}.canvasmedical.com
  baseurl_source: declared
  description: Insurance claims and billing
  name: Canvas Medical Claim API
  slug: canvas-medical-claim-api
- baseURL: https://fumage-{canvas-instance}.canvasmedical.com
  baseurl_source: declared
  description: Communications with or about a patient
  name: Canvas Medical Communication API
  slug: canvas-medical-communication-api
- baseURL: https://fumage-{canvas-instance}.canvasmedical.com
  baseurl_source: declared
  description: Patient conditions, problems, and diagnoses
  name: Canvas Medical Condition API
  slug: canvas-medical-condition-api
- baseURL: https://fumage-{canvas-instance}.canvasmedical.com
  baseurl_source: declared
  description: Patient consent records
  name: Canvas Medical Consent API
  slug: canvas-medical-consent-api
- baseURL: https://fumage-{canvas-instance}.canvasmedical.com
  baseurl_source: declared
  description: Insurance coverage records
  name: Canvas Medical Coverage API
  slug: canvas-medical-coverage-api
- baseURL: https://fumage-{canvas-instance}.canvasmedical.com
  baseurl_source: declared
  description: Diagnostic test reports
  name: Canvas Medical DiagnosticReport API
  slug: canvas-medical-diagnosticreport-api
- baseURL: https://fumage-{canvas-instance}.canvasmedical.com
  baseurl_source: declared
  description: Clinical encounters and visits
  name: Canvas Medical Encounter API
  slug: canvas-medical-encounter-api
- baseURL: https://fumage-{canvas-instance}.canvasmedical.com
  baseurl_source: declared
  description: Patient care goals
  name: Canvas Medical Goal API
  slug: canvas-medical-goal-api
- baseURL: https://fumage-{canvas-instance}.canvasmedical.com
  baseurl_source: declared
  description: Immunization records
  name: Canvas Medical Immunization API
  slug: canvas-medical-immunization-api
- baseURL: https://fumage-{canvas-instance}.canvasmedical.com
  baseurl_source: declared
  description: Physical practice locations
  name: Canvas Medical Location API
  slug: canvas-medical-location-api
- baseURL: https://fumage-{canvas-instance}.canvasmedical.com
  baseurl_source: declared
  description: FHIR server capabilities
  name: Canvas Medical Metadata API
  slug: canvas-medical-metadata-api
- baseURL: https://fumage-{canvas-instance}.canvasmedical.com
  baseurl_source: declared
  description: Clinical observations, vitals, and lab results
  name: Canvas Medical Observation API
  slug: canvas-medical-observation-api
- baseURL: https://fumage-{canvas-instance}.canvasmedical.com
  baseurl_source: declared
  description: Healthcare organization information
  name: Canvas Medical Organization API
  slug: canvas-medical-organization-api
- baseURL: https://fumage-{canvas-instance}.canvasmedical.com
  baseurl_source: declared
  description: Patient demographic and administrative data
  name: Canvas Medical Patient API
  slug: canvas-medical-patient-api
- baseURL: https://fumage-{canvas-instance}.canvasmedical.com
  baseurl_source: declared
  description: Healthcare provider information
  name: Canvas Medical Practitioner API
  slug: canvas-medical-practitioner-api
- baseURL: https://fumage-{canvas-instance}.canvasmedical.com
  baseurl_source: declared
  description: Clinical procedures performed
  name: Canvas Medical Procedure API
  slug: canvas-medical-procedure-api
- baseURL: https://fumage-{canvas-instance}.canvasmedical.com
  baseurl_source: declared
  description: Structured data collection forms
  name: Canvas Medical Questionnaire API
  slug: canvas-medical-questionnaire-api
- baseURL: https://fumage-{canvas-instance}.canvasmedical.com
  baseurl_source: declared
  description: Patient responses to questionnaires
  name: Canvas Medical QuestionnaireResponse API
  slug: canvas-medical-questionnaireresponse-api
- baseURL: https://fumage-{canvas-instance}.canvasmedical.com
  baseurl_source: declared
  description: Practitioner availability schedules
  name: Canvas Medical Schedule API
  slug: canvas-medical-schedule-api
- baseURL: https://fumage-{canvas-instance}.canvasmedical.com
  baseurl_source: declared
  description: Orders for laboratory, imaging, and referrals
  name: Canvas Medical ServiceRequest API
  slug: canvas-medical-servicerequest-api
- baseURL: https://fumage-{canvas-instance}.canvasmedical.com
  baseurl_source: declared
  description: Available appointment time slots
  name: Canvas Medical Slot API
  slug: canvas-medical-slot-api
- baseURL: https://fumage-{canvas-instance}.canvasmedical.com
  baseurl_source: declared
  description: Clinical and administrative tasks
  name: Canvas Medical Task API
  slug: canvas-medical-task-api
- baseURL: https://fumage-{canvas-instance}.canvasmedical.com
  baseurl_source: declared
  description: Allergy and intolerance records
  name: Canvas Medical Allergy Intolerance API
  slug: canvas-medical-allergy-intolerance-api
- baseURL: https://fumage-{canvas-instance}.canvasmedical.com
  baseurl_source: declared
  description: Care plan management
  name: Canvas Medical Care plan API
  slug: canvas-medical-care-plan-api
- baseURL: https://fumage-{canvas-instance}.canvasmedical.com
  baseurl_source: declared
  description: Clinical documents and attachments
  name: Canvas Medical Document Reference API
  slug: canvas-medical-document-reference-api
- baseURL: https://fumage-{canvas-instance}.canvasmedical.com
  baseurl_source: declared
  description: Medication prescriptions and orders
  name: Canvas Medical Medication Request API
  slug: canvas-medical-medication-request-api
arazzos:
- description: Locate a patient, find a practitioner's schedule, search for a free slot, then book and confirm an appointment.
  name: Canvas Medical Appointment Scheduling
  slug: canvas-medical-appointment-scheduling-workflow
- description: Read the patient, record a care Goal, then retrieve the active CarePlan and the CareTeam coordinating it.
  name: Canvas Medical Care Plan Management
  slug: canvas-medical-care-plan-management-workflow
- description: Place a laboratory order with a ServiceRequest, then retrieve the resulting DiagnosticReport and the discrete Observation results.
  name: Canvas Medical Lab Order to Results
  slug: canvas-medical-lab-order-results-workflow
- description: Read the patient, check existing allergies and active medications for safety, then write a new prescription and confirm it.
  name: Canvas Medical Medication Prescribing
  slug: canvas-medical-medication-prescribing-workflow
- description: Search for an existing patient by identifier and update it if found, otherwise create a new US Core Patient.
  name: Canvas Medical Patient Registration (Upsert)
  slug: canvas-medical-patient-registration-workflow
- description: Find a questionnaire by title, submit a completed QuestionnaireResponse, then read it back to confirm capture.
  name: Canvas Medical Questionnaire Assessment Capture
  slug: canvas-medical-questionnaire-assessment-workflow
- description: Discover server capabilities, locate a patient, then pull the US Core clinical summary - problems, vitals/labs, medications, and allergies.
  name: Canvas Medical SMART on FHIR US Core Retrieval
  slug: canvas-medical-smart-us-core-patient-retrieval-workflow
artifact_total: 120
asyncapis:
- description: ''
  name: Canvas Medical Events Webhooks
  slug: canvas-medical-events-webhooks
collections:
- collection_type: open
  name: Canvas Medical FHIR AllergyIntolerance API
  slug: open-canvas-medical-allergyintolerance-api
- collection_type: open
  name: Canvas Medical FHIR AllergyIntolerance Appointment API
  slug: open-canvas-medical-appointment-api
- collection_type: open
  name: Canvas Medical FHIR AllergyIntolerance CarePlan API
  slug: open-canvas-medical-careplan-api
- collection_type: open
  name: Canvas Medical FHIR AllergyIntolerance CareTeam API
  slug: open-canvas-medical-careteam-api
- collection_type: open
  name: Canvas Medical FHIR AllergyIntolerance Claim API
  slug: open-canvas-medical-claim-api
- collection_type: open
  name: Canvas Medical FHIR AllergyIntolerance Communication API
  slug: open-canvas-medical-communication-api
- collection_type: open
  name: Canvas Medical FHIR AllergyIntolerance Condition API
  slug: open-canvas-medical-condition-api
- collection_type: open
  name: Canvas Medical FHIR AllergyIntolerance Consent API
  slug: open-canvas-medical-consent-api
- collection_type: open
  name: Canvas Medical FHIR AllergyIntolerance Coverage API
  slug: open-canvas-medical-coverage-api
- collection_type: open
  name: Canvas Medical FHIR AllergyIntolerance DiagnosticReport API
  slug: open-canvas-medical-diagnosticreport-api
- collection_type: open
  name: Canvas Medical FHIR AllergyIntolerance DocumentReference API
  slug: open-canvas-medical-documentreference-api
- collection_type: open
  name: Canvas Medical FHIR AllergyIntolerance Encounter API
  slug: open-canvas-medical-encounter-api
- collection_type: open
  name: Canvas Medical FHIR AllergyIntolerance Goal API
  slug: open-canvas-medical-goal-api
- collection_type: open
  name: Canvas Medical FHIR AllergyIntolerance Immunization API
  slug: open-canvas-medical-immunization-api
- collection_type: open
  name: Canvas Medical FHIR AllergyIntolerance Location API
  slug: open-canvas-medical-location-api
- collection_type: open
  name: Canvas Medical FHIR AllergyIntolerance MedicationRequest API
  slug: open-canvas-medical-medicationrequest-api
- collection_type: open
  name: Canvas Medical FHIR AllergyIntolerance Metadata API
  slug: open-canvas-medical-metadata-api
- collection_type: open
  name: Canvas Medical FHIR AllergyIntolerance Observation API
  slug: open-canvas-medical-observation-api
- collection_type: open
  name: Canvas Medical FHIR AllergyIntolerance Organization API
  slug: open-canvas-medical-organization-api
- collection_type: open
  name: Canvas Medical FHIR AllergyIntolerance Patient API
  slug: open-canvas-medical-patient-api
- collection_type: open
  name: Canvas Medical FHIR AllergyIntolerance Practitioner API
  slug: open-canvas-medical-practitioner-api
- collection_type: open
  name: Canvas Medical FHIR AllergyIntolerance Procedure API
  slug: open-canvas-medical-procedure-api
- collection_type: open
  name: Canvas Medical FHIR AllergyIntolerance Questionnaire API
  slug: open-canvas-medical-questionnaire-api
- collection_type: open
  name: Canvas Medical FHIR AllergyIntolerance QuestionnaireResponse API
  slug: open-canvas-medical-questionnaireresponse-api
- collection_type: open
  name: Canvas Medical FHIR AllergyIntolerance Schedule API
  slug: open-canvas-medical-schedule-api
- collection_type: open
  name: Canvas Medical FHIR AllergyIntolerance ServiceRequest API
  slug: open-canvas-medical-servicerequest-api
- collection_type: open
  name: Canvas Medical FHIR AllergyIntolerance Slot API
  slug: open-canvas-medical-slot-api
- collection_type: open
  name: Canvas Medical FHIR AllergyIntolerance Task API
  slug: open-canvas-medical-task-api
common:
- group: design
  href: https://artifacts.apis.io/canvas-medical/rules/canvas-medical-rules.yml
  title: ''
  type: Spectral
  url: rules/canvas-medical-rules.yml
- group: design
  href: https://artifacts.apis.io/canvas-medical/rules/canvas-medical-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/canvas-medical-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/canvas-medical/json-ld/canvas-medical-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/canvas-medical-context.jsonld
- group: design
  href: https://artifacts.apis.io/canvas-medical/vocabulary/canvas-medical-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/canvas-medical-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/canvas-medical/grpc/canvas-medical-plugins.proto
  title: ''
  type: Protobuf
  url: grpc/canvas-medical-plugins.proto
- group: other
  href: https://artifacts.apis.io/canvas-medical/grpc/canvas-medical-plugin-runner.proto
  title: ''
  type: Protobuf
  url: grpc/canvas-medical-plugin-runner.proto
- group: other
  href: https://artifacts.apis.io/canvas-medical/hosts/canvas-medical-hosts.yml
  title: ''
  type: Hosts
  url: hosts/canvas-medical-hosts.yml
- group: build
  href: https://artifacts.apis.io/canvas-medical/integrations/canvas-medical-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/canvas-medical-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/canvas-medical/vendors/canvas-medical-vendors.yml
  title: ''
  type: Vendors
  url: vendors/canvas-medical-vendors.yml
- group: other
  href: https://artifacts.apis.io/canvas-medical/capabilities/canvas-medical-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/canvas-medical-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/canvas-medical/agentic-access/canvas-medical-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/canvas-medical-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/canvas-medical/security/canvas-medical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canvas-medical-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/canvas-medical/authentication/canvas-medical-authentication.yml
  title: ''
  type: Authentication
  url: authentication/canvas-medical-authentication.yml
- group: auth
  href: https://artifacts.apis.io/canvas-medical/scopes/canvas-medical-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/canvas-medical-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.canvasmedical.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.canvasmedical.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/canvas-medical
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/canvas-medical
- group: company
  title: ''
  type: Blog
  url: https://www.canvasmedical.com/articles
- group: commercial
  title: ''
  type: Pricing
  url: https://www.canvasmedical.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.canvasmedical.com/
- group: other
  title: ''
  type: X
  url: https://x.com/canvasmedical
- group: commercial
  href: https://artifacts.apis.io/canvas-medical/plans/canvas-medical-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/canvas-medical-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/canvas-medical/rate-limits/canvas-medical-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/canvas-medical-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/canvas-medical/finops/canvas-medical-finops.yml
  title: ''
  type: FinOps
  url: finops/canvas-medical-finops.yml
- group: start
  title: ''
  type: Sandbox
  url: https://www.canvasmedical.com/emrs/developer-sandbox
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.canvasmedical.com/learn/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.canvasmedical.com/product-updates/release-notes/
- group: operate
  title: ''
  type: Support
  url: https://help.canvasmedical.com/
- group: design
  title: ''
  type: ArazzoWorkflows
  url: ''
- group: build
  href: https://artifacts.apis.io/canvas-medical/packages/canvas-medical-packages.yml
  title: ''
  type: Packages
  url: packages/canvas-medical-packages.yml
- group: build
  href: https://artifacts.apis.io/canvas-medical/packages/canvas-medical-packages.yml
  title: ''
  type: SDKs
  url: packages/canvas-medical-packages.yml
- group: build
  href: https://artifacts.apis.io/canvas-medical/cli/canvas-medical-cli.yml
  title: ''
  type: CLI
  url: cli/canvas-medical-cli.yml
- group: design
  href: https://artifacts.apis.io/canvas-medical/components/canvas-medical-components.yml
  title: ''
  type: Components
  url: components/canvas-medical-components.yml
- group: agent
  href: https://artifacts.apis.io/canvas-medical/well-known/canvas-medical-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/canvas-medical-well-known.yml
- group: other
  href: https://artifacts.apis.io/canvas-medical/well-known/canvas-medical-fhir-service-base-urls-production.json
  title: ''
  type: APICatalog
  url: well-known/canvas-medical-fhir-service-base-urls-production.json
- group: agent
  href: https://artifacts.apis.io/canvas-medical/llms/canvas-medical-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/canvas-medical-llms.txt
- group: other
  href: https://artifacts.apis.io/canvas-medical/overlays/canvas-medical-fhir-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canvas-medical-fhir-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/canvas-medical/grpc/canvas-medical-events.proto
  title: ''
  type: Protobuf
  url: grpc/canvas-medical-events.proto
- group: other
  href: https://artifacts.apis.io/canvas-medical/grpc/canvas-medical-effects.proto
  title: ''
  type: Protobuf
  url: grpc/canvas-medical-effects.proto
- group: design
  href: https://artifacts.apis.io/canvas-medical/conformance/canvas-medical-conformance.yml
  title: ''
  type: Conformance
  url: conformance/canvas-medical-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.canvasmedical.com/guides/platform-security-overview/
- group: design
  href: https://artifacts.apis.io/canvas-medical/errors/canvas-medical-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/canvas-medical-problem-types.yml
- group: design
  href: https://artifacts.apis.io/canvas-medical/lifecycle/canvas-medical-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/canvas-medical-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.canvasmedical.com/product-updates/important-dates/
- group: design
  href: https://artifacts.apis.io/canvas-medical/conventions/canvas-medical-conventions.yml
  title: ''
  type: Conventions
  url: conventions/canvas-medical-conventions.yml
- group: operate
  href: https://artifacts.apis.io/canvas-medical/changelog/canvas-medical-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/canvas-medical-changelog.yml
- group: design
  href: https://artifacts.apis.io/canvas-medical/data-model/canvas-medical-data-model.yml
  title: ''
  type: DataModel
  url: data-model/canvas-medical-data-model.yml
- group: start
  href: https://artifacts.apis.io/canvas-medical/sandbox/canvas-medical-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/canvas-medical-sandbox.yml
- group: design
  href: https://artifacts.apis.io/canvas-medical/asyncapi/canvas-medical-events-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/canvas-medical-events-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/canvas-medical/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.canvasmedical.com/product-updates/roadmap/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.canvasmedical.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.canvasmedical.com/api/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.canvasmedical.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.canvasmedical.com/terms
created: '2026-06-13'
description: Canvas Medical is a developer-first EHR platform built for virtual and value-based care, offering a comprehensive FHIR R4 REST API with 41 resources for clinical workflows, patient management, and care team coordination. The platform combines a standards-based FHIR API with a native Python SDK that enables plugins to execute synchronously within the EMR, supporting scheduling, charting, billing, and custom workflow automation across more than 650 clinical and operational events.
examples:
- key_count: 12
  name: Canvas Medical Appointment Example
  slug: canvas-medical-appointment-example
- key_count: 11
  name: Canvas Medical Observation Example
  slug: canvas-medical-observation-example
- key_count: 12
  name: Canvas Medical Patient Example
  slug: canvas-medical-patient-example
finops:
- has_sources: true
  method: derived
  name: Canvas Medical Finops
  primary_unit: visit
  service_category: ''
  slug: canvas-medical-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/canvas-medical.png
json_schemas:
- name: AllergyIntolerance
  property_count: 11
  slug: canvas-medical-allergy-intolerance
- name: Appointment
  property_count: 11
  slug: canvas-medical-appointment
- name: Bundle
  property_count: 6
  slug: canvas-medical-bundle
- name: CapabilityStatement
  property_count: 6
  slug: canvas-medical-capability-statement
- name: CarePlan
  property_count: 11
  slug: canvas-medical-care-plan
- name: CareTeam
  property_count: 8
  slug: canvas-medical-care-team
- name: Claim
  property_count: 12
  slug: canvas-medical-claim
- name: Communication
  property_count: 9
  slug: canvas-medical-communication
- name: Condition
  property_count: 12
  slug: canvas-medical-condition
- name: Consent
  property_count: 9
  slug: canvas-medical-consent
- name: Coverage
  property_count: 12
  slug: canvas-medical-coverage
- name: DiagnosticReport
  property_count: 10
  slug: canvas-medical-diagnostic-report
- name: DocumentReference
  property_count: 10
  slug: canvas-medical-document-reference
- name: Encounter
  property_count: 10
  slug: canvas-medical-encounter
- name: Goal
  property_count: 10
  slug: canvas-medical-goal
- name: Immunization
  property_count: 10
  slug: canvas-medical-immunization
- name: Location
  property_count: 8
  slug: canvas-medical-location
- name: MedicationRequest
  property_count: 12
  slug: canvas-medical-medication-request
- name: Observation
  property_count: 13
  slug: canvas-medical-observation
- name: Organization
  property_count: 10
  slug: canvas-medical-organization
- name: Canvas Medical FHIR Patient
  property_count: 14
  slug: canvas-medical-patient
- name: Practitioner
  property_count: 10
  slug: canvas-medical-practitioner
- name: Procedure
  property_count: 9
  slug: canvas-medical-procedure
- name: QuestionnaireResponse
  property_count: 9
  slug: canvas-medical-questionnaire-response
- name: Questionnaire
  property_count: 8
  slug: canvas-medical-questionnaire
- name: Schedule
  property_count: 8
  slug: canvas-medical-schedule
- name: ServiceRequest
  property_count: 11
  slug: canvas-medical-service-request
- name: Slot
  property_count: 8
  slug: canvas-medical-slot
- name: Task
  property_count: 12
  slug: canvas-medical-task
jsonld:
- class_count: 39
  name: Canvas Medical Context
  property_count: 59
  slug: canvas-medical-context
layout: provider
modified: '2026-08-14'
name: Canvas Medical
nav: Providers
network: true
overview: 'Canvas Medical publishes 30 API contracts indexed on the [APIs.io](https://apis.io/) network, including Appointment API, CareTeam API, Claim API, and 27 more. Tagged areas include Electronic Health Records, FHIR, Healthcare, Virtual Care, and Clinical Workflows.


  The Canvas Medical catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Canvas Medical''s developer surface includes authentication, documentation, engineering blog, pricing, sandbox, getting-started guide, release notes, and 48 more developer resources.'
plans:
- name: Canvas Medical Plans Pricing
  plan_count: 3
  slug: canvas-medical-plans-pricing
- name: Canvas Medical Price Estimates
  plan_count: 0
  slug: canvas-medical-price-estimates
random_paper: 8
rate_limits:
- limit_count: 0
  name: Canvas Medical Rate Limits
  slug: canvas-medical-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Canvas Medical — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: canvas-medical-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Canvas Medical API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: canvas-medical-rules
scopes:
- name: Canvas Medical Scopes
  scope_count: 20
  slug: canvas-medical-scopes
  summary_line: 20 scopes · clientCredentials/authorizationCode
score:
  band: exemplar
  composite: 69.7
  coverage:
    artifact_dirs: 41
    catalog_earned: 81.5
    catalog_earned_first_party: 17.0
    catalog_gap: 33.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 47.4
    contract_governance: 47.0
    contract_quality: 75.5
    developer_ergonomics: 83.3
    discoverability: 73.2
    operational_transparency: 50.0
  previous_composite: 68.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 28
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    - jurisdiction: US
      standard: us-core
    jurisdictions_satisfied: 1
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
screenshot: https://apis.io/screenshots/canvas-medical/canvas-medical-2026-06-20T173934.png
security:
- kind: authentication
  name: Canvas Medical Authentication
  slug: canvas-medical-authentication
  summary_line: oauth2/http/openIdConnect · 3 schemes
- kind: domain-security
  name: Canvas Medical Domain Security
  slug: canvas-medical-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 11
skills:
- name: canvas-sdk
  slug: canvas-medical-canvas-sdk
- name: companion-app-patterns
  slug: canvas-medical-companion-app-patterns
- name: custom-data-patterns
  slug: canvas-medical-custom-data-patterns
- name: database-performance
  slug: canvas-medical-database-performance
- name: fhir-api-client-development
  slug: canvas-medical-fhir-api-client-development
- name: fhir-api-client-security
  slug: canvas-medical-fhir-api-client-security
- name: icon-generation
  slug: canvas-medical-icon-generation
- name: instance-analyze
  slug: canvas-medical-instance-analyze
- name: plugin-api-server-security
  slug: canvas-medical-plugin-api-server-security
- name: plugin-patterns
  slug: canvas-medical-plugin-patterns
- name: testing
  slug: canvas-medical-testing
slug: canvas-medical
tags:
- Electronic Health Records
- FHIR
- Healthcare
- Virtual Care
- Clinical Workflows
- Patient Management
- Care Coordination
website: https://www.canvasmedical.com/
---

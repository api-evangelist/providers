---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.9
  scored_at: '2026-09-01'
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
- description: Allergy and intolerance records
  name: Canvas Medical AllergyIntolerance API
  slug: canvas-medical-allergyintolerance-api
- description: Appointment scheduling and management
  name: Canvas Medical Appointment API
  slug: canvas-medical-appointment-api
- description: Care plan management
  name: Canvas Medical CarePlan API
  slug: canvas-medical-careplan-api
- description: Care team coordination
  name: Canvas Medical CareTeam API
  slug: canvas-medical-careteam-api
- description: Insurance claims and billing
  name: Canvas Medical Claim API
  slug: canvas-medical-claim-api
- description: Communications with or about a patient
  name: Canvas Medical Communication API
  slug: canvas-medical-communication-api
- description: Patient conditions, problems, and diagnoses
  name: Canvas Medical Condition API
  slug: canvas-medical-condition-api
- description: Patient consent records
  name: Canvas Medical Consent API
  slug: canvas-medical-consent-api
- description: Insurance coverage records
  name: Canvas Medical Coverage API
  slug: canvas-medical-coverage-api
- description: Diagnostic test reports
  name: Canvas Medical DiagnosticReport API
  slug: canvas-medical-diagnosticreport-api
- description: Clinical documents and attachments
  name: Canvas Medical DocumentReference API
  slug: canvas-medical-documentreference-api
- description: Clinical encounters and visits
  name: Canvas Medical Encounter API
  slug: canvas-medical-encounter-api
- description: Patient care goals
  name: Canvas Medical Goal API
  slug: canvas-medical-goal-api
- description: Immunization records
  name: Canvas Medical Immunization API
  slug: canvas-medical-immunization-api
- description: Physical practice locations
  name: Canvas Medical Location API
  slug: canvas-medical-location-api
- description: Medication prescriptions and orders
  name: Canvas Medical MedicationRequest API
  slug: canvas-medical-medicationrequest-api
- description: FHIR server capabilities
  name: Canvas Medical Metadata API
  slug: canvas-medical-metadata-api
- description: Clinical observations, vitals, and lab results
  name: Canvas Medical Observation API
  slug: canvas-medical-observation-api
- description: Healthcare organization information
  name: Canvas Medical Organization API
  slug: canvas-medical-organization-api
- description: Patient demographic and administrative data
  name: Canvas Medical Patient API
  slug: canvas-medical-patient-api
- description: Healthcare provider information
  name: Canvas Medical Practitioner API
  slug: canvas-medical-practitioner-api
- description: Clinical procedures performed
  name: Canvas Medical Procedure API
  slug: canvas-medical-procedure-api
- description: Structured data collection forms
  name: Canvas Medical Questionnaire API
  slug: canvas-medical-questionnaire-api
- description: Patient responses to questionnaires
  name: Canvas Medical QuestionnaireResponse API
  slug: canvas-medical-questionnaireresponse-api
- description: Practitioner availability schedules
  name: Canvas Medical Schedule API
  slug: canvas-medical-schedule-api
- description: Orders for laboratory, imaging, and referrals
  name: Canvas Medical ServiceRequest API
  slug: canvas-medical-servicerequest-api
- description: Available appointment time slots
  name: Canvas Medical Slot API
  slug: canvas-medical-slot-api
- description: Clinical and administrative tasks
  name: Canvas Medical Task API
  slug: canvas-medical-task-api
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
artifact_total: 81
asyncapis:
- description: ''
  name: Canvas Medical Events Webhooks
  slug: canvas-medical-events-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/canvas-medical-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/canvas-medical-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/canvas-medical-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/canvas-medical-authentication.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/canvas-medical-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/canvas-medical-rate-limits.yml
- group: commercial
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
  title: ''
  type: Packages
  url: packages/canvas-medical-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/canvas-medical-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/canvas-medical-cli.yml
- group: design
  title: ''
  type: Components
  url: components/canvas-medical-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/canvas-medical-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/canvas-medical-fhir-service-base-urls-production.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/canvas-medical-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/canvas-medical-fhir-api-overlay.yaml
- group: other
  title: ''
  type: Protobuf
  url: grpc/canvas-medical-events.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/canvas-medical-effects.proto
- group: design
  title: ''
  type: Conformance
  url: conformance/canvas-medical-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.canvasmedical.com/guides/platform-security-overview/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/canvas-medical-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/canvas-medical-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.canvasmedical.com/product-updates/important-dates/
- group: design
  title: ''
  type: Conventions
  url: conventions/canvas-medical-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/canvas-medical-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/canvas-medical-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/canvas-medical-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/canvas-medical-events-webhooks.yml
- group: agent
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
- name: Canvas Medical Finops
  service_category: ''
  slug: canvas-medical-finops
graphqls:
- description: 'This conceptual GraphQL schema represents the Canvas Medical EHR platform''s data model, derived from its FHIR R4 REST API and Python SDK capabilities. Canvas Medical is a developer-first EHR platform '
  name: Canvas Medical GraphQL Schema
  slug: canvas-medical-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/canvas-medical.png
json_schemas:
- name: Canvas Medical FHIR Patient
  property_count: 14
  slug: canvas-medical-patient
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
overview: 'Canvas Medical publishes 28 APIs on the [APIs.io](https://apis.io/) network, including AllergyIntolerance API, Appointment API, CarePlan API, and 25 more. Tagged areas include EHR, FHIR, Healthcare, Electronic Health Records, and Virtual Care.


  The Canvas Medical catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Canvas Medical''s developer surface includes authentication, documentation, engineering blog, pricing, sandbox, getting-started guide, release notes, and 39 more developer resources.'
plans:
- name: Canvas Medical Plans Pricing
  plan_count: 2
  slug: canvas-medical-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Canvas Medical Rate Limits
  slug: canvas-medical-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Canvas Medical API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: canvas-medical-jsonschema-spectral-rules
scopes:
- name: Canvas Medical Scopes
  scope_count: 20
  slug: canvas-medical-scopes
  summary_line: 20 scopes · clientCredentials/authorizationCode
score:
  band: exemplar
  composite: 67.6
  coverage:
    artifact_dirs: 36
    catalog_gap: 52.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 28.0
    contract_quality: 76.2
    developer_ergonomics: 76.2
    discoverability: 75.9
    governance: 28.0
    operational_transparency: 42.1
  previous_composite: 67.6
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
    score: 82.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/canvas-medical/refs/heads/main/screenshots/canvas-medical-2026-06-20T173934.png
security:
- kind: authentication
  name: Canvas Medical Authentication
  slug: canvas-medical-authentication
  summary_line: oauth2/http/openIdConnect · 3 schemes
- kind: domain-security
  name: Canvas Medical Domain Security
  slug: canvas-medical-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: canvas-medical
tags:
- EHR
- FHIR
- Healthcare
- Electronic Health Records
- Virtual Care
- Clinical Workflows
- Patient Management
- Care Coordination
website: https://www.canvasmedical.com/
---

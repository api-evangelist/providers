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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 30
  human_in_the_loop: 0
  name: Canvas Medical Agentic Access
  operation_count: 85
  slug: canvas-medical-agentic-access
  summary_line: 85 operations · 30 acting
api_count: 30
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
artifact_total: 51
common:
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
modified: '2026-06-13'
name: Canvas Medical
nav: Providers
network: true
overview: 'Canvas Medical publishes 28 APIs on the [APIs.io](https://apis.io/) network, including AllergyIntolerance API, Appointment API, CarePlan API, and 25 more. Tagged areas include EHR, FHIR, Healthcare, Electronic Health Records, and Virtual Care.


  The Canvas Medical catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Canvas Medical''s developer surface includes authentication, documentation, engineering blog, pricing, sandbox, getting-started guide, release notes, and 12 more developer resources.'
plans:
- name: Canvas Medical Plans Pricing
  plan_count: 2
  slug: canvas-medical-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Canvas Medical Rate Limits
  slug: canvas-medical-rate-limits
rules:
- name: Canvas Medical API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: canvas-medical-jsonschema-spectral-rules
scopes:
- name: Canvas Medical Scopes
  scope_count: 11
  slug: canvas-medical-scopes
  summary_line: 11 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 56.4
  delta: 0.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.1
    developer_ergonomics: 43.5
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 36.8
  previous_composite: 56.0
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 58.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/canvas-medical/refs/heads/main/screenshots/canvas-medical-2026-06-20T173934.png
security:
- kind: authentication
  name: Canvas Medical Authentication
  slug: canvas-medical-authentication
  summary_line: http/oauth2 · 3 schemes
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

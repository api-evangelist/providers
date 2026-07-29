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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 163
  human_in_the_loop: 0
  name: Drchrono Agentic Access
  operation_count: 327
  slug: drchrono-agentic-access
  summary_line: 327 operations · 163 acting
api_count: 6
apis:
- description: Create and manage administrative resources
  name: drchrono Administrative API
  slug: drchrono-administrative-api
- description: Search Audit Logs
  name: drchrono Audit API
  slug: drchrono-audit-api
- description: The Availability API from drchrono — 1 operation(s) for availability.
  name: drchrono Availability API
  slug: drchrono-availability-api
- description: Create and manage billing resources
  name: drchrono Billing API
  slug: drchrono-billing-api
- description: Create and manage clinical resources
  name: drchrono Clinical API
  slug: drchrono-clinical-api
- description: Create and manage practice management resources
  name: drchrono Practice Management API
  slug: drchrono-practice-management-api
arazzos:
- description: Read a patient record, book an appointment, then read the appointment back to confirm it was created.
  name: drChrono Appointment Scheduling
  slug: drchrono-appointment-scheduling-workflow
- description: Pull a patient chart by reading the patient, listing problems and medications, and exporting a C-CDA document.
  name: drChrono Chart Export
  slug: drchrono-chart-export-workflow
- description: Document a patient visit by recording a problem, a medication, and a clinical note.
  name: drChrono Clinical Documentation
  slug: drchrono-clinical-documentation-workflow
- description: Run the revenue cycle by checking insurance eligibility, reviewing day sheet charges, and adding a claim billing note.
  name: drChrono Eligibility and Billing
  slug: drchrono-eligibility-and-billing-workflow
- description: Search for an existing patient by name and update it if found, otherwise create a new patient record.
  name: drChrono Patient Registration (Upsert)
  slug: drchrono-patient-registration-workflow
artifact_total: 166
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/drchrono-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/drchrono-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/drchrono-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/drchrono-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.drchrono.com
- group: docs
  title: ''
  type: Documentation
  url: https://app.drchrono.com/api-docs/tutorial/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/drchrono
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/drchrono
- group: company
  title: ''
  type: Blog
  url: https://blog.drchrono.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.drchrono.com/plans-and-pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.drchrono.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/drchrono
- group: commercial
  title: ''
  type: Plans
  url: plans/drchrono-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/drchrono-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/drchrono-finops.yml
- group: company
  title: ''
  type: Partners
  url: https://www.drchrono.com/partners/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.drchrono.com/api-development-terms-conditions/
- group: start
  title: ''
  type: SupportPortal
  url: https://support.drchrono.com/home/api
- group: design
  title: ''
  type: ArazzoWorkflows
  url: ''
created: '2026-06-13'
description: drchrono is an EHR platform with a REST API for managing patient records, clinical encounters, appointments, prescriptions, billing, and HIPAA-compliant medical data exchange. It provides OAuth 2.0-secured endpoints covering patient management, clinical documentation, lab integration, scheduling, billing, and practice administration, enabling healthcare app developers to build integrations with the drchrono EHR ecosystem.
examples:
- key_count: 5
  name: Appointment Example
  slug: appointment-example
- key_count: 5
  name: Appointmentprofile Example
  slug: appointmentprofile-example
- key_count: 5
  name: Appointmenttemplate Example
  slug: appointmenttemplate-example
- key_count: 5
  name: Billinglineitem Example
  slug: billinglineitem-example
- key_count: 5
  name: Billingprofile Example
  slug: billingprofile-example
- key_count: 5
  name: Careplan Example
  slug: careplan-example
- key_count: 5
  name: Careteammember Example
  slug: careteammember-example
- key_count: 5
  name: Cashpayment Example
  slug: cashpayment-example
- key_count: 5
  name: Cashpaymentlog Example
  slug: cashpaymentlog-example
- key_count: 5
  name: Claimbillingnotes Example
  slug: claimbillingnotes-example
- key_count: 5
  name: Clinicalnote Example
  slug: clinicalnote-example
- key_count: 5
  name: Consentform Example
  slug: consentform-example
- key_count: 5
  name: Coverage Example
  slug: coverage-example
- key_count: 5
  name: Customappointmentfieldtype Example
  slug: customappointmentfieldtype-example
- key_count: 5
  name: Custominsuranceplanname Example
  slug: custominsuranceplanname-example
- key_count: 5
  name: Custompatientfieldtype Example
  slug: custompatientfieldtype-example
- key_count: 5
  name: Customvitaltype Example
  slug: customvitaltype-example
- key_count: 5
  name: Doctor Example
  slug: doctor-example
- key_count: 5
  name: Doctorfeeschedule Example
  slug: doctorfeeschedule-example
- key_count: 5
  name: Doctormessage Example
  slug: doctormessage-example
- key_count: 5
  name: Doctoroptions Example
  slug: doctoroptions-example
- key_count: 5
  name: Eobobject Example
  slug: eobobject-example
- key_count: 5
  name: Feeschedule Example
  slug: feeschedule-example
- key_count: 5
  name: Implantabledevice Example
  slug: implantabledevice-example
- key_count: 5
  name: Insurance Example
  slug: insurance-example
- key_count: 5
  name: Inventorycategory Example
  slug: inventorycategory-example
- key_count: 5
  name: Inventoryvaccine Example
  slug: inventoryvaccine-example
- key_count: 5
  name: Laborder Example
  slug: laborder-example
- key_count: 5
  name: Laborderdocument Example
  slug: laborderdocument-example
- key_count: 5
  name: Labresult Example
  slug: labresult-example
- key_count: 5
  name: Labtest Example
  slug: labtest-example
- key_count: 5
  name: Labvendorlocation Example
  slug: labvendorlocation-example
- key_count: 5
  name: Lineitemtransaction Example
  slug: lineitemtransaction-example
- key_count: 5
  name: Office Example
  slug: office-example
- key_count: 5
  name: Patient Example
  slug: patient-example
- key_count: 5
  name: Patientallergy Example
  slug: patientallergy-example
- key_count: 5
  name: Patientamendment Example
  slug: patientamendment-example
- key_count: 5
  name: Patientcommunication Example
  slug: patientcommunication-example
- key_count: 5
  name: Patientdrug Example
  slug: patientdrug-example
- key_count: 5
  name: Patientflagtype Example
  slug: patientflagtype-example
- key_count: 5
  name: Patientintervention Example
  slug: patientintervention-example
- key_count: 5
  name: Patientlabresultset Example
  slug: patientlabresultset-example
- key_count: 5
  name: Patientmessage Example
  slug: patientmessage-example
- key_count: 5
  name: Patientphysicalexam Example
  slug: patientphysicalexam-example
- key_count: 5
  name: Patientproblem Example
  slug: patientproblem-example
- key_count: 5
  name: Patientriskassessment Example
  slug: patientriskassessment-example
- key_count: 5
  name: Patientvaccinerecord Example
  slug: patientvaccinerecord-example
- key_count: 5
  name: Phonecalllog Example
  slug: phonecalllog-example
- key_count: 5
  name: Prescriptionmessage Example
  slug: prescriptionmessage-example
- key_count: 5
  name: Procedure Example
  slug: procedure-example
- key_count: 5
  name: Reminderprofile Example
  slug: reminderprofile-example
- key_count: 5
  name: Scannedclinicaldocument Example
  slug: scannedclinicaldocument-example
- key_count: 5
  name: Scheduleblock Example
  slug: scheduleblock-example
- key_count: 5
  name: Signedconsentform Example
  slug: signedconsentform-example
- key_count: 5
  name: Soapnotecustomreport Example
  slug: soapnotecustomreport-example
- key_count: 5
  name: Soapnotelineitemfieldtype Example
  slug: soapnotelineitemfieldtype-example
- key_count: 5
  name: Soapnotelineitemfieldvalue Example
  slug: soapnotelineitemfieldvalue-example
- key_count: 5
  name: Staff Example
  slug: staff-example
- key_count: 5
  name: Task Example
  slug: task-example
- key_count: 5
  name: Taskcategory Example
  slug: taskcategory-example
- key_count: 5
  name: Tasknote Example
  slug: tasknote-example
- key_count: 5
  name: Taskstatus Example
  slug: taskstatus-example
- key_count: 5
  name: Tasktemplate Example
  slug: tasktemplate-example
- key_count: 5
  name: Telemedicineappointment Example
  slug: telemedicineappointment-example
- key_count: 5
  name: Telemedicineappointmenteventlog Example
  slug: telemedicineappointmenteventlog-example
- key_count: 5
  name: Userprofile Example
  slug: userprofile-example
- key_count: 5
  name: Userprofilesgroup Example
  slug: userprofilesgroup-example
- key_count: 5
  name: Workschedule Example
  slug: workschedule-example
- key_count: 5
  name: Yellownotepad Example
  slug: yellownotepad-example
finops:
- name: Drchrono Finops
  service_category: ''
  slug: drchrono-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/drchrono.png
json_schemas:
- name: Appointment
  property_count: 57
  slug: appointment
- name: AppointmentProfile
  property_count: 9
  slug: appointmentprofile
- name: AppointmentTemplate
  property_count: 11
  slug: appointmenttemplate
- name: AsyncResourceError
  property_count: 3
  slug: asyncresourceerror
- name: AuditLog
  property_count: 13
  slug: auditlog
- name: BillingLineItem
  property_count: 31
  slug: billinglineitem
- name: BillingLineItemDeletion
  property_count: 3
  slug: billinglineitemdeletion
- name: BillingProfile
  property_count: 11
  slug: billingprofile
- name: CarePlan
  property_count: 12
  slug: careplan
- name: CareTeamMember
  property_count: 5
  slug: careteammember
- name: CashPayment
  property_count: 15
  slug: cashpayment
- name: CashPaymentLog
  property_count: 10
  slug: cashpaymentlog
- name: ClaimBillingNotes
  property_count: 5
  slug: claimbillingnotes
- name: ClinicalNote
  property_count: 5
  slug: clinicalnote
- name: ConsentForm
  property_count: 10
  slug: consentform
- name: Coverage
  property_count: 12
  slug: coverage
- name: CustomAppointmentFieldType
  property_count: 8
  slug: customappointmentfieldtype
- name: CustomInsurancePlanName
  property_count: 7
  slug: custominsuranceplanname
- name: CustomPatientFieldType
  property_count: 7
  slug: custompatientfieldtype
- name: CustomVitalType
  property_count: 10
  slug: customvitaltype
- name: Doctor
  property_count: 20
  slug: doctor
- name: DoctorFeeSchedule
  property_count: 24
  slug: doctorfeeschedule
- name: DoctorMessage
  property_count: 28
  slug: doctormessage
- name: DoctorOptions
  property_count: 13
  slug: doctoroptions
- name: EOBObject
  property_count: 12
  slug: eobobject
- name: FeeSchedule
  property_count: 11
  slug: feeschedule
- name: FeeScheduleItem
  property_count: 23
  slug: feescheduleitem
- name: ImplantableDevice
  property_count: 16
  slug: implantabledevice
- name: Insurance
  property_count: 3
  slug: insurance
- name: InventoryCategory
  property_count: 7
  slug: inventorycategory
- name: InventoryVaccine
  property_count: 20
  slug: inventoryvaccine
- name: LabOrder
  property_count: 13
  slug: laborder
- name: LabOrderDocument
  property_count: 6
  slug: laborderdocument
- name: LabResult
  property_count: 17
  slug: labresult
- name: LabTest
  property_count: 12
  slug: labtest
- name: LabVendorLocation
  property_count: 4
  slug: labvendorlocation
- name: LineItemTransaction
  property_count: 17
  slug: lineitemtransaction
- name: Office
  property_count: 18
  slug: office
- name: Patient
  property_count: 65
  slug: patient
- name: PatientAllergy
  property_count: 11
  slug: patientallergy
- name: PatientAmendment
  property_count: 7
  slug: patientamendment
- name: PatientAuthorization
  property_count: 17
  slug: patientauthorization
- name: PatientCommunication
  property_count: 12
  slug: patientcommunication
- name: PatientDrug
  property_count: 24
  slug: patientdrug
- name: PatientFlagType
  property_count: 8
  slug: patientflagtype
- name: PatientIntervention
  property_count: 12
  slug: patientintervention
- name: PatientLabResultSet
  property_count: 19
  slug: patientlabresultset
- name: PatientMessage
  property_count: 9
  slug: patientmessage
- name: PatientPhysicalExam
  property_count: 12
  slug: patientphysicalexam
- name: PatientProblem
  property_count: 19
  slug: patientproblem
- name: PatientRiskAssessment
  property_count: 12
  slug: patientriskassessment
- name: PatientVaccineRecord
  property_count: 28
  slug: patientvaccinerecord
- name: PhoneCallLog
  property_count: 14
  slug: phonecalllog
- name: PrescriptionMessage
  property_count: 10
  slug: prescriptionmessage
- name: Procedure
  property_count: 11
  slug: procedure
- name: ReminderProfile
  property_count: 4
  slug: reminderprofile
- name: ScannedClinicalDocument
  property_count: 9
  slug: scannedclinicaldocument
- name: ScheduleBlock
  property_count: 11
  slug: scheduleblock
- name: SignedConsentForm
  property_count: 8
  slug: signedconsentform
- name: SignedConsentFormUpdate
  property_count: 5
  slug: signedconsentformupdate
- name: SoapNoteCustomReport
  property_count: 10
  slug: soapnotecustomreport
- name: SoapNoteLineItemFieldType
  property_count: 8
  slug: soapnotelineitemfieldtype
- name: SoapNoteLineItemFieldValue
  property_count: 6
  slug: soapnotelineitemfieldvalue
- name: Staff
  property_count: 12
  slug: staff
- name: Task
  property_count: 15
  slug: task
- name: TaskCategory
  property_count: 7
  slug: taskcategory
- name: TaskNote
  property_count: 7
  slug: tasknote
- name: TaskStatus
  property_count: 8
  slug: taskstatus
- name: TaskTemplate
  property_count: 14
  slug: tasktemplate
- name: TelemedicineAppointment
  property_count: 7
  slug: telemedicineappointment
- name: TelemedicineAppointmentEventLog
  property_count: 3
  slug: telemedicineappointmenteventlog
- name: UserProfile
  property_count: 7
  slug: userprofile
- name: UserProfilesGroup
  property_count: 7
  slug: userprofilesgroup
- name: WorkDay
  property_count: 4
  slug: workday
- name: WorkHours
  property_count: 4
  slug: workhours
- name: WorkSchedule
  property_count: 4
  slug: workschedule
- name: YellowNotepad
  property_count: 3
  slug: yellownotepad
jsonld:
- class_count: 96
  name: Drchrono Context
  property_count: 4
  slug: drchrono-context
layout: provider
modified: '2026-06-13'
name: drchrono
nav: Providers
network: true
overview: 'drchrono publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Administrative API, Audit API, Availability API, and 3 more. Tagged areas include EHR, Electronic Health Records, Healthcare, Medical Records, and Practice Management.


  The drchrono catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  drchrono''s developer surface includes authentication, documentation, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Drchrono Plans Pricing
  plan_count: 5
  slug: drchrono-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Drchrono Rate Limits
  slug: drchrono-rate-limits
rules:
- name: drchrono API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: drchrono-jsonschema-spectral-rules
scopes:
- name: Drchrono Scopes
  scope_count: 23
  slug: drchrono-scopes
  summary_line: 23 scopes · authorizationCode
score:
  band: developing
  composite: 49.2
  delta: -6.4
  facets:
    commercial_clarity: 60.5
    contract_quality: 52.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 55.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 47.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/drchrono/refs/heads/main/screenshots/drchrono-2026-06-20T180219.png
security:
- kind: authentication
  name: Drchrono Authentication
  slug: drchrono-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Drchrono Domain Security
  slug: drchrono-domain-security
  summary_line: TLSv1.3 · DMARC
slug: drchrono
tags:
- EHR
- Electronic Health Records
- Healthcare
- Medical Records
- Practice Management
- HIPAA
- Appointments
- Billing
- Prescriptions
- Lab Integration
- FHIR
website: https://www.drchrono.com
---

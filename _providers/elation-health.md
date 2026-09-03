---
access_model:
  confidence: medium
  label: Paid · Partner / sandbox onboarding
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - authentication
  - documentation
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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 455
  human_in_the_loop: 0
  name: Elation Health Agentic Access
  operation_count: 846
  slug: elation-health-agentic-access
  summary_line: 846 operations · 455 acting
api_count: 19
apis:
- baseURL: https://app.elationemr.com/api/2.0/
  baseurl_source: declared
  description: Allergy and drug intolerance tracking
  name: Elation Health Allergies API
  slug: elation-allergies-api
- baseURL: https://app.elationemr.com/api/2.0/
  baseurl_source: declared
  description: Scheduling and appointment management
  name: Elation Health Appointments API
  slug: elation-appointments-api
- baseURL: https://app.elationemr.com/api/2.0/
  baseurl_source: declared
  description: OAuth2 token management
  name: Elation Health Authentication API
  slug: elation-authentication-api
- baseURL: https://app.elationemr.com/api/2.0/
  baseurl_source: declared
  description: Billing codes and bill management
  name: Elation Health Billing API
  slug: elation-billing-api
- baseURL: https://app.elationemr.com/api/2.0/
  baseurl_source: declared
  description: Insurance company, plan, and policy management
  name: Elation Health Insurance API
  slug: elation-insurance-api
- baseURL: https://app.elationemr.com/api/2.0/
  baseurl_source: declared
  description: Laboratory order management
  name: Elation Health Lab Orders API
  slug: elation-lab-orders-api
- baseURL: https://app.elationemr.com/api/2.0/
  baseurl_source: declared
  description: Medication and prescription management
  name: Elation Health Medications API
  slug: elation-medications-api
- baseURL: https://app.elationemr.com/api/2.0/
  baseurl_source: declared
  description: Secure direct messaging
  name: Elation Health Messaging API
  slug: elation-messaging-api
- baseURL: https://app.elationemr.com/api/2.0/
  baseurl_source: declared
  description: Patient profile management
  name: Elation Health Patients API
  slug: elation-patients-api
- baseURL: https://app.elationemr.com/api/2.0/
  baseurl_source: declared
  description: Provider and staff management
  name: Elation Health Physicians API
  slug: elation-physicians-api
- baseURL: https://app.elationemr.com/api/2.0/
  baseurl_source: declared
  description: Practice administration
  name: Elation Health Practices API
  slug: elation-practices-api
- baseURL: https://app.elationemr.com/api/2.0/
  baseurl_source: declared
  description: Patient problem list management
  name: Elation Health Problems API
  slug: elation-problems-api
- baseURL: https://app.elationemr.com/api/2.0/
  baseurl_source: declared
  description: Clinical encounter documentation
  name: Elation Health Visit Notes API
  slug: elation-visit-notes-api
- description: HL7 FHIR R4 (v4.0.1) API with US Core v5.0.1 and SMART on FHIR 1.0.0 support, used for standards-based interoperability and ONC / CMS 21st Century Cures Act certified health IT use cases. Exposed to r
  name: Elation FHIR R4 API
  slug: fhir-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Allergy Documentation API from Elation Health — 2 operation(s) for allergy documentation.
  name: Elation Health Allergy Documentation API
  slug: elation-health-allergy-documentation-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Allergy Documentation (NKDA) API from Elation Health — 2 operation(s) for allergy documentation (nkda).
  name: Elation Health Allergy Documentation (NKDA) API
  slug: elation-health-allergy-documentation-nkda-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Ancillary Companies API from Elation Health — 4 operation(s) for ancillary companies.
  name: Elation Health Ancillary Companies API
  slug: elation-health-ancillary-companies-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The API Settings API from Elation Health — 1 operation(s) for api settings.
  name: Elation Health API Settings API
  slug: elation-health-api-settings-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The App API from Elation Health — 4 operation(s) for app.
  name: Elation Health App API
  slug: elation-health-app-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Appointment Rooms API from Elation Health — 1 operation(s) for appointment rooms.
  name: Elation Health Appointment Rooms API
  slug: elation-health-appointment-rooms-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Appointment Types API from Elation Health — 4 operation(s) for appointment types.
  name: Elation Health Appointment Types API
  slug: elation-health-appointment-types-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Billing Codes API from Elation Health — 6 operation(s) for billing codes.
  name: Elation Health Billing Codes API
  slug: elation-health-billing-codes-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Bills API from Elation Health — 6 operation(s) for bills.
  name: Elation Health Bills API
  slug: elation-health-bills-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Broadcast Messages API from Elation Health — 2 operation(s) for broadcast messages.
  name: Elation Health Broadcast Messages API
  slug: elation-health-broadcast-messages-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Cardiac Centers API from Elation Health — 4 operation(s) for cardiac centers.
  name: Elation Health Cardiac Centers API
  slug: elation-health-cardiac-centers-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Cardiac Order Tests API from Elation Health — 4 operation(s) for cardiac order tests.
  name: Elation Health Cardiac Order Tests API
  slug: elation-health-cardiac-order-tests-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Cardiac Orders API from Elation Health — 4 operation(s) for cardiac orders.
  name: Elation Health Cardiac Orders API
  slug: elation-health-cardiac-orders-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Caregaps API from Elation Health — 2 operation(s) for caregaps.
  name: Elation Health Caregaps API
  slug: elation-health-caregaps-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Ccda API from Elation Health — 4 operation(s) for ccda.
  name: Elation Health Ccda API
  slug: elation-health-ccda-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Clinical Documents API from Elation Health — 4 operation(s) for clinical documents.
  name: Elation Health Clinical Documents API
  slug: elation-health-clinical-documents-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Clinical Questionnaires API from Elation Health — 2 operation(s) for clinical questionnaires.
  name: Elation Health Clinical Questionnaires API
  slug: elation-health-clinical-questionnaires-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Contacts API from Elation Health — 8 operation(s) for contacts.
  name: Elation Health Contacts API
  slug: elation-health-contacts-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Custom Blocks API from Elation Health — 1 operation(s) for custom blocks.
  name: Elation Health Custom Blocks API
  slug: elation-health-custom-blocks-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The parent resource for tracking batches of individual patient chart imports.
  name: Elation Health Data Import Request API
  slug: elation-health-data-import-request-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Definitions API from Elation Health — 2 operation(s) for definitions.
  name: Elation Health Definitions API
  slug: elation-health-definitions-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Delegate Permissions API from Elation Health — 4 operation(s) for delegate permissions.
  name: Elation Health Delegate Permissions API
  slug: elation-health-delegate-permissions-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Discontinued Medication API from Elation Health — 1 operation(s) for discontinued medication.
  name: Elation Health Discontinued Medication API
  slug: elation-health-discontinued-medication-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Discontinued Medications API from Elation Health — 4 operation(s) for discontinued medications.
  name: Elation Health Discontinued Medications API
  slug: elation-health-discontinued-medications-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Document Tags API from Elation Health — 4 operation(s) for document tags.
  name: Elation Health Document Tags API
  slug: elation-health-document-tags-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Drug Intolerances API from Elation Health — 4 operation(s) for drug intolerances.
  name: Elation Health Drug Intolerances API
  slug: elation-health-drug-intolerances-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Event Subscriptions API from Elation Health — 8 operation(s) for event subscriptions.
  name: Elation Health Event Subscriptions API
  slug: elation-health-event-subscriptions-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Family Histories API from Elation Health — 4 operation(s) for family histories.
  name: Elation Health Family Histories API
  slug: elation-health-family-histories-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Fax Lines API from Elation Health — 2 operation(s) for fax lines.
  name: Elation Health Fax Lines API
  slug: elation-health-fax-lines-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Fills API from Elation Health — 4 operation(s) for fills.
  name: Elation Health Fills API
  slug: elation-health-fills-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Handouts API from Elation Health — 5 operation(s) for handouts.
  name: Elation Health Handouts API
  slug: elation-health-handouts-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Historical Medication Download Requests API from Elation Health — 2 operation(s) for historical medication download requests.
  name: Elation Health Historical Medication Download Requests API
  slug: elation-health-historical-medication-download-requests-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Histories API from Elation Health — 4 operation(s) for histories.
  name: Elation Health Histories API
  slug: elation-health-histories-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Imaging Centers API from Elation Health — 4 operation(s) for imaging centers.
  name: Elation Health Imaging Centers API
  slug: elation-health-imaging-centers-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Imaging Order Tests API from Elation Health — 4 operation(s) for imaging order tests.
  name: Elation Health Imaging Order Tests API
  slug: elation-health-imaging-order-tests-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Imaging Orders API from Elation Health — 4 operation(s) for imaging orders.
  name: Elation Health Imaging Orders API
  slug: elation-health-imaging-orders-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Immunizations API from Elation Health — 4 operation(s) for immunizations.
  name: Elation Health Immunizations API
  slug: elation-health-immunizations-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Incoming Files API from Elation Health — 8 operation(s) for incoming files.
  name: Elation Health Incoming Files API
  slug: elation-health-incoming-files-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Injections API from Elation Health — 2 operation(s) for injections.
  name: Elation Health Injections API
  slug: elation-health-injections-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Injections (BETA) API from Elation Health — 2 operation(s) for injections (beta).
  name: Elation Health Injections (BETA) API
  slug: elation-health-injections-beta-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Insurance Card API from Elation Health — 1 operation(s) for insurance card.
  name: Elation Health Insurance Card API
  slug: elation-health-insurance-card-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Insurance Companies API from Elation Health — 5 operation(s) for insurance companies.
  name: Elation Health Insurance Companies API
  slug: elation-health-insurance-companies-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Insurance Eligibility API from Elation Health — 2 operation(s) for insurance eligibility.
  name: Elation Health Insurance Eligibility API
  slug: elation-health-insurance-eligibility-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Insurance Eligibility Usage API from Elation Health — 1 operation(s) for insurance eligibility usage.
  name: Elation Health Insurance Eligibility Usage API
  slug: elation-health-insurance-eligibility-usage-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Insurance Plans API from Elation Health — 5 operation(s) for insurance plans.
  name: Elation Health Insurance Plans API
  slug: elation-health-insurance-plans-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Lab Facility Identifiers API from Elation Health — 6 operation(s) for lab facility identifiers.
  name: Elation Health Lab Facility Identifiers API
  slug: elation-health-lab-facility-identifiers-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Lab Order Compendiums API from Elation Health — 4 operation(s) for lab order compendiums.
  name: Elation Health Lab Order Compendiums API
  slug: elation-health-lab-order-compendiums-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Lab Order Sets API from Elation Health — 4 operation(s) for lab order sets.
  name: Elation Health Lab Order Sets API
  slug: elation-health-lab-order-sets-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Lab Order Tests API from Elation Health — 4 operation(s) for lab order tests.
  name: Elation Health Lab Order Tests API
  slug: elation-health-lab-order-tests-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Lab Vendor Integrations API from Elation Health — 4 operation(s) for lab vendor integrations.
  name: Elation Health Lab Vendor Integrations API
  slug: elation-health-lab-vendor-integrations-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Lab Vendor Patient Sites API from Elation Health — 4 operation(s) for lab vendor patient sites.
  name: Elation Health Lab Vendor Patient Sites API
  slug: elation-health-lab-vendor-patient-sites-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Lab Vendors API from Elation Health — 4 operation(s) for lab vendors.
  name: Elation Health Lab Vendors API
  slug: elation-health-lab-vendors-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Languages API from Elation Health — 2 operation(s) for languages.
  name: Elation Health Languages API
  slug: elation-health-languages-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Letters API from Elation Health — 3 operation(s) for letters.
  name: Elation Health Letters API
  slug: elation-health-letters-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Medication History Download Fills API from Elation Health — 2 operation(s) for medication history download fills.
  name: Elation Health Medication History Download Fills API
  slug: elation-health-medication-history-download-fills-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Medication History Downloads API from Elation Health — 2 operation(s) for medication history downloads.
  name: Elation Health Medication History Downloads API
  slug: elation-health-medication-history-downloads-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Medication Order Templates API from Elation Health — 4 operation(s) for medication order templates.
  name: Elation Health Medication Order Templates API
  slug: elation-health-medication-order-templates-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Medication Refills API from Elation Health — 2 operation(s) for medication refills.
  name: Elation Health Medication Refills API
  slug: elation-health-medication-refills-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Message Threads API from Elation Health — 7 operation(s) for message threads.
  name: Elation Health Message Threads API
  slug: elation-health-message-threads-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Methods Put And Patch Not Allowed. API from Elation Health — 1 operation(s) for methods put and patch not allowed..
  name: Elation Health Methods Put And Patch Not Allowed. API
  slug: elation-health-methods-put-and-patch-not-allowed-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Non Visit Notes API from Elation Health — 4 operation(s) for non visit notes.
  name: Elation Health Non Visit Notes API
  slug: elation-health-non-visit-notes-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Notes API from Elation Health — 3 operation(s) for notes.
  name: Elation Health Notes API
  slug: elation-health-notes-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Notes v1 API from Elation Health — 2 operation(s) for notes v1.
  name: Elation Health Notes v1 API
  slug: elation-health-notes-v1-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Notes v2 API from Elation Health — 7 operation(s) for notes v2.
  name: Elation Health Notes v2 API
  slug: elation-health-notes-v2-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Office Staff API from Elation Health — 4 operation(s) for office staff.
  name: Elation Health Office Staff API
  slug: elation-health-office-staff-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Outstanding Balance API from Elation Health — 1 operation(s) for outstanding balance.
  name: Elation Health Outstanding Balance API
  slug: elation-health-outstanding-balance-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Packaged Medication (Beta) API from Elation Health — 2 operation(s) for packaged medication (beta).
  name: Elation Health Packaged Medication (Beta) API
  slug: elation-health-packaged-medication-beta-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Packaged Medication Labeler (Beta) API from Elation Health — 2 operation(s) for packaged medication labeler (beta).
  name: Elation Health Packaged Medication Labeler (Beta) API
  slug: elation-health-packaged-medication-labeler-beta-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Packaged Medication Labelers API from Elation Health — 2 operation(s) for packaged medication labelers.
  name: Elation Health Packaged Medication Labelers API
  slug: elation-health-packaged-medication-labelers-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Packaged Medications API from Elation Health — 2 operation(s) for packaged medications.
  name: Elation Health Packaged Medications API
  slug: elation-health-packaged-medications-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The patient chart import API from Elation Health — 3 operation(s) for patient chart import.
  name: Elation Health patient chart import API
  slug: elation-health-patient-chart-import-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Patient Form Requests API from Elation Health — 4 operation(s) for patient form requests.
  name: Elation Health Patient Form Requests API
  slug: elation-health-patient-form-requests-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Patient Form Submissions API from Elation Health — 2 operation(s) for patient form submissions.
  name: Elation Health Patient Form Submissions API
  slug: elation-health-patient-form-submissions-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Patient Forms API from Elation Health — 4 operation(s) for patient forms.
  name: Elation Health Patient Forms API
  slug: elation-health-patient-forms-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Patient Insurances API from Elation Health — 2 operation(s) for patient insurances.
  name: Elation Health Patient Insurances API
  slug: elation-health-patient-insurances-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Patient Letter Categories API from Elation Health — 2 operation(s) for patient letter categories.
  name: Elation Health Patient Letter Categories API
  slug: elation-health-patient-letter-categories-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Patient Letters (BETA) API from Elation Health — 4 operation(s) for patient letters (beta).
  name: Elation Health Patient Letters (BETA) API
  slug: elation-health-patient-letters-beta-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Patient Profile Photo API from Elation Health — 2 operation(s) for patient profile photo.
  name: Elation Health Patient Profile Photo API
  slug: elation-health-patient-profile-photo-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Patient Provider Team Members API from Elation Health — 2 operation(s) for patient provider team members.
  name: Elation Health Patient Provider Team Members API
  slug: elation-health-patient-provider-team-members-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Patient Provider Teams API from Elation Health — 2 operation(s) for patient provider teams.
  name: Elation Health Patient Provider Teams API
  slug: elation-health-patient-provider-teams-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Pharmacies API from Elation Health — 4 operation(s) for pharmacies.
  name: Elation Health Pharmacies API
  slug: elation-health-pharmacies-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Practice Medications API from Elation Health — 4 operation(s) for practice medications.
  name: Elation Health Practice Medications API
  slug: elation-health-practice-medications-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Prescription Fills API from Elation Health — 2 operation(s) for prescription fills.
  name: Elation Health Prescription Fills API
  slug: elation-health-prescription-fills-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Print Headers API from Elation Health — 4 operation(s) for print headers.
  name: Elation Health Print Headers API
  slug: elation-health-print-headers-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Provider Team API from Elation Health — 6 operation(s) for provider team.
  name: Elation Health Provider Team API
  slug: elation-health-provider-team-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Pulmonary Centers API from Elation Health — 4 operation(s) for pulmonary centers.
  name: Elation Health Pulmonary Centers API
  slug: elation-health-pulmonary-centers-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Pulmonary Order Tests API from Elation Health — 4 operation(s) for pulmonary order tests.
  name: Elation Health Pulmonary Order Tests API
  slug: elation-health-pulmonary-order-tests-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Pulmonary Orders API from Elation Health — 4 operation(s) for pulmonary orders.
  name: Elation Health Pulmonary Orders API
  slug: elation-health-pulmonary-orders-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Recurring Event Groups API from Elation Health — 5 operation(s) for recurring event groups.
  name: Elation Health Recurring Event Groups API
  slug: elation-health-recurring-event-groups-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Reference Medication (Beta) API from Elation Health — 2 operation(s) for reference medication (beta).
  name: Elation Health Reference Medication (Beta) API
  slug: elation-health-reference-medication-beta-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Reference Medications API from Elation Health — 2 operation(s) for reference medications.
  name: Elation Health Reference Medications API
  slug: elation-health-reference-medications-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Referral Orders API from Elation Health — 2 operation(s) for referral orders.
  name: Elation Health Referral Orders API
  slug: elation-health-referral-orders-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Referrals API from Elation Health — 4 operation(s) for referrals.
  name: Elation Health Referrals API
  slug: elation-health-referrals-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Refills API from Elation Health — 2 operation(s) for refills.
  name: Elation Health Refills API
  slug: elation-health-refills-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Report Internal Notes API from Elation Health — 2 operation(s) for report internal notes.
  name: Elation Health Report Internal Notes API
  slug: elation-health-report-internal-notes-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Report Types API from Elation Health — 4 operation(s) for report types.
  name: Elation Health Report Types API
  slug: elation-health-report-types-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Reports API from Elation Health — 9 operation(s) for reports.
  name: Elation Health Reports API
  slug: elation-health-reports-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Reports Ext API from Elation Health — 1 operation(s) for reports ext.
  name: Elation Health Reports Ext API
  slug: elation-health-reports-ext-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Service Locations API from Elation Health — 4 operation(s) for service locations.
  name: Elation Health Service Locations API
  slug: elation-health-service-locations-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Sleep Centers API from Elation Health — 4 operation(s) for sleep centers.
  name: Elation Health Sleep Centers API
  slug: elation-health-sleep-centers-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Sleep Order Tests API from Elation Health — 4 operation(s) for sleep order tests.
  name: Elation Health Sleep Order Tests API
  slug: elation-health-sleep-order-tests-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Sleep Orders API from Elation Health — 4 operation(s) for sleep orders.
  name: Elation Health Sleep Orders API
  slug: elation-health-sleep-orders-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Staff Group API from Elation Health — 1 operation(s) for staff group.
  name: Elation Health Staff Group API
  slug: elation-health-staff-group-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Staff Groups API from Elation Health — 4 operation(s) for staff groups.
  name: Elation Health Staff Groups API
  slug: elation-health-staff-groups-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Thread Members API from Elation Health — 5 operation(s) for thread members.
  name: Elation Health Thread Members API
  slug: elation-health-thread-members-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Thread Messages API from Elation Health — 5 operation(s) for thread messages.
  name: Elation Health Thread Messages API
  slug: elation-health-thread-messages-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Users API from Elation Health — 4 operation(s) for users.
  name: Elation Health Users API
  slug: elation-health-users-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Vaccine API from Elation Health — 2 operation(s) for vaccine.
  name: Elation Health Vaccine API
  slug: elation-health-vaccine-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Vaccines API from Elation Health — 1 operation(s) for vaccines.
  name: Elation Health Vaccines API
  slug: elation-health-vaccines-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Visit Note Templates API from Elation Health — 4 operation(s) for visit note templates.
  name: Elation Health Visit Note Templates API
  slug: elation-health-visit-note-templates-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Visit Note Types API from Elation Health — 5 operation(s) for visit note types.
  name: Elation Health Visit Note Types API
  slug: elation-health-visit-note-types-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Vitals API from Elation Health — 5 operation(s) for vitals.
  name: Elation Health Vitals API
  slug: elation-health-vitals-api
artifact_total: 182
asyncapis:
- description: ''
  name: Elation Health Events Webhooks
  slug: elation-health-events-webhooks
collections:
- collection_type: postman
  name: API Authentication
  slug: postman-elation-api-authentication
- collection_type: postman
  name: Billing API
  slug: postman-elation-billing-api
- collection_type: postman
  name: Care Gaps API
  slug: postman-elation-care-gaps-api-1
- collection_type: postman
  name: Elation Import API
  slug: postman-elation-elation-import-api
- collection_type: postman
  name: Event Subscription API
  slug: postman-elation-event-subscription-api
- collection_type: postman
  name: Insurance API
  slug: postman-elation-insurance-api
- collection_type: postman
  name: Messaging API
  slug: postman-elation-messaging-api
- collection_type: postman
  name: Orders API
  slug: postman-elation-orders-api
- collection_type: postman
  name: Patient Document API
  slug: postman-elation-patient-document-api
- collection_type: postman
  name: Patient Profile API
  slug: postman-elation-patient-profile-api
- collection_type: postman
  name: Practice API
  slug: postman-elation-practice-api
- collection_type: postman
  name: '[Premium] Patient Insurance API'
  slug: postman-elation-premium-patient-insurance-api
- collection_type: postman
  name: Reference Data API
  slug: postman-elation-reference-data-api
- collection_type: postman
  name: Scheduling API
  slug: postman-elation-scheduling-api
- collection_type: postman
  name: User Management API
  slug: postman-elation-user-management-api
- collection_type: postman
  name: Visit Notes API
  slug: postman-elation-visit-notes-api
- collection_type: open
  name: API Authentication
  slug: open-elation-api-authentication
- collection_type: open
  name: API Settings
  slug: open-elation-api-settings
- collection_type: open
  name: Billing API
  slug: open-elation-billing-api
- collection_type: open
  name: Care Gaps API
  slug: open-elation-care-gaps-api-1
- collection_type: open
  name: Elation Import API
  slug: open-elation-elation-import-api
- collection_type: open
  name: Event Subscription API
  slug: open-elation-event-subscription-api
- collection_type: open
  name: Elation Health REST Allergies API
  slug: open-elation-health-allergies-api
- collection_type: open
  name: Elation Health REST Allergies Appointments API
  slug: open-elation-health-appointments-api
- collection_type: open
  name: Elation Health REST Allergies Authentication API
  slug: open-elation-health-authentication-api
- collection_type: open
  name: Elation Health REST Allergies Lab Orders API
  slug: open-elation-health-lab-orders-api
- collection_type: open
  name: Elation Health REST Allergies Medications API
  slug: open-elation-health-medications-api
- collection_type: open
  name: Elation Health REST Allergies Patients API
  slug: open-elation-health-patients-api
- collection_type: open
  name: Elation Health REST Allergies Physicians API
  slug: open-elation-health-physicians-api
- collection_type: open
  name: Elation Health REST Allergies Practices API
  slug: open-elation-health-practices-api
- collection_type: open
  name: Elation Health REST Allergies Problems API
  slug: open-elation-health-problems-api
- collection_type: open
  name: Insurance API
  slug: open-elation-insurance-api
- collection_type: open
  name: Messaging API
  slug: open-elation-messaging-api
- collection_type: open
  name: Orders API
  slug: open-elation-orders-api
- collection_type: open
  name: Patient Document API
  slug: open-elation-patient-document-api
- collection_type: open
  name: Patient Profile API
  slug: open-elation-patient-profile-api
- collection_type: open
  name: Practice API
  slug: open-elation-practice-api
- collection_type: open
  name: '[Premium] Patient Insurance API'
  slug: open-elation-premium-patient-insurance-api
- collection_type: open
  name: Reference Data API
  slug: open-elation-reference-data-api
- collection_type: open
  name: Scheduling API
  slug: open-elation-scheduling-api
- collection_type: open
  name: User Management API
  slug: open-elation-user-management-api
- collection_type: open
  name: Visit Notes API
  slug: open-elation-visit-notes-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/elation-health-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/elation-health-api-authentication-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/elation-health-patient-profile-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/elation-health-visit-notes-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/elation-health-patient-document-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/elation-health-orders-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/elation-health-scheduling-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/elation-health-billing-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/elation-health-insurance-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/elation-health-premium-patient-insurance-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/elation-health-practice-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/elation-health-user-management-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/elation-health-messaging-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/elation-health-event-subscription-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/elation-health-reference-data-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/elation-health-care-gaps-api-1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/elation-health-elation-import-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/elation-health-api-full-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/elation-health/overview
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/elation-health-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/elation-health-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/elation-health-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/elation-health-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/elation-health-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/elation-health-problem-types.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.elationhealth.com/solutions/ehr/
- group: design
  title: ''
  type: Conformance
  url: conformance/elation-health-conformance.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/elation-health-tool-crosswalk.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/elation-health-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/elation-health-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/elation-health-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/elation-health-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elation-health-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/elation-health-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/elation-health-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/elation-health-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.elationhealth.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.elationhealth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.elationhealth.com/docs/api-overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.elationhealth.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.elationhealth.com/docs/getting-started-2
- group: auth
  title: ''
  type: Authentication
  url: https://docs.elationhealth.com/docs/oauth
- group: design
  title: ''
  type: Webhooks
  url: https://docs.elationhealth.com/docs/webhooks
- group: other
  title: ''
  type: ModelContextProtocol
  url: https://docs.elationhealth.com/docs/mcp
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/elationemr
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/elationhealth/
- group: company
  title: ''
  type: Blog
  url: https://www.elationhealth.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.elationhealth.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.elationhealth.com/contact-us/sandbox/
- group: operate
  title: ''
  type: Support
  url: https://www.elationhealth.com/contact-us/
- group: operate
  title: ''
  type: StatusPage
  url: https://elationhealth.statuspage.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.elationhealth.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.elationhealth.com/privacy-policy/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.elationhealth.com/reference/api-overview
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/elationemr
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/elationhealth
- group: company
  title: ''
  type: Blog
  url: https://www.elationhealth.com/resources/blogs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.elationhealth.com/contact-us/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://elationhealth.statuspage.io
- group: other
  title: ''
  type: X
  url: https://x.com/elationhealth
- group: commercial
  title: ''
  type: Plans
  url: plans/elation-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/elation-health-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/elation-health-finops.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/elation-health-a2a.yml
- group: build
  title: ''
  type: Examples
  url: examples/elation-health-patient-example.json
- group: build
  title: ''
  type: Examples
  url: examples/elation-health-appointment-example.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/elation-health-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/elation-health-jsonschema-spectral-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/elation-health-patient-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/elation-health-context.jsonld
- group: agent
  title: ''
  type: AgentSkill
  url: skills/elation-health-provider-published-skill.md
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.elationhealth.com/api-reference
- group: docs
  title: ''
  type: Documentation
  url: https://help.elationhealth.com/articles/rest/overview/api-overview
- group: docs
  title: ''
  type: APIReference
  url: https://help.elationhealth.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://help.elationhealth.com/articles/rest/overview/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://help.elationhealth.com/articles/rest/overview/oauth
- group: auth
  title: ''
  type: OAuthScopes
  url: https://help.elationhealth.com/articles/rest/overview/scopes
- group: design
  title: ''
  type: Webhooks
  url: https://help.elationhealth.com/articles/rest/overview/webhooks
- group: other
  title: ''
  type: ModelContextProtocol
  url: https://help.elationhealth.com/articles/rest/overview/mcp-server
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.elationhealth.com/articles/rest/changelog/changelog
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.elationhealth.com/
- group: operate
  title: ''
  type: Support
  url: https://help.elationhealth.com/articles/rest/overview/getting-help
- group: auth
  title: ''
  type: Compliance
  url: https://help.elationhealth.com/compliance-quality
created: '2026-07-24'
description: Elation Health is a United States clinical-first electronic health record (EHR/EMR) and healthcare technology company, founded in 2010 and headquartered in San Francisco, California, serving independent primary care practices, value-based care organizations, digital health startups, and health-tech partners. Beyond its provider-facing EHR, Elation ships a broad, well-documented public REST API (v2.0) that lets partners read and write clinical and administrative data - patient profiles and demographics, allergies and problems, visit notes, clinical and lab/imaging orders, patient documents, scheduling, billing, insurance and eligibility, messaging, practice and user management, care gaps, and data import - authenticated with OAuth2. The API is documented on a ReadMe developer portal backed by machine-readable OpenAPI definitions, augmented with event subscription webhooks and a Model Context Protocol (MCP) server for agentic access. Elation also operates login-gated HL7 FHIR
  R4 and SMART-on-FHIR interoperability endpoints for ONC/CMS 21st Century Cures Act information-blocking compliance, exposed to registered applications rather than anonymously. Positioned as an independent challenger to the US EHR duopoly, Elation targets the primary-care and value-based-care segment of the largest, most commercial healthcare-API market.
examples:
- key_count: 18
  name: Elation Health Appointment Example
  slug: elation-health-appointment-example
- key_count: 25
  name: Elation Health Patient Example
  slug: elation-health-patient-example
finops:
- name: Elation Health Finops
  service_category: ''
  slug: elation-health-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
json_schemas:
- name: Patient
  property_count: 43
  slug: elation-health-patient
jsonld:
- class_count: 28
  name: Elation Health Context
  property_count: 69
  slug: elation-health-context
layout: provider
mcp_servers:
- description: ''
  name: Elation Health MCP Server
  slug: elation-health-mcp-server
modified: '2026-08-14'
name: Elation Health
nav: Providers
network: true
overview: 'Elation Health publishes 125 APIs on the [APIs.io](https://apis.io/) network, including Allergies API, Appointments API, Authentication API, and 122 more. Tagged areas include Healthcare, United States, EHR, EMR, and FHIR.


  The Elation Health catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Elation Health''s developer surface includes sandbox, changelog, authentication, documentation, API reference, getting-started guide, engineering blog, and 77 more developer resources.'
plans:
- name: Elation Health Plans Pricing
  plan_count: 3
  slug: elation-health-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Elation Health Rate Limits
  slug: elation-health-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Elation Health API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: elation-health-jsonschema-spectral-rules
scopes:
- name: Elation Health Scopes
  scope_count: 154
  slug: elation-health-scopes
  summary_line: 154 scopes · clientCredentials/password
score:
  band: exemplar
  composite: 81.2
  coverage:
    artifact_dirs: 34
    catalog_gap: 43.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 43.2
    contract_quality: 73.0
    developer_ergonomics: 76.2
    discoverability: 75.9
    governance: 43.2
    operational_transparency: 42.1
  previous_composite: 81.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 125
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 92.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/screenshots/elation-health-2026-07-25T213054.png
security:
- kind: authentication
  name: Elation Health Authentication
  slug: elation-health-authentication
  summary_line: http/oauth2 · 4 schemes
- kind: domain-security
  name: Elation Health Domain Security
  slug: elation-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: elation-health
tags:
- Healthcare
- United States
- EHR
- EMR
- FHIR
- HL7
- Interoperability
- SMART on FHIR
- Primary Care
- Value-Based Care
- Eligibility
- Clinical Data
- Scheduling
- e-Prescribing
- Digital Health
website: https://www.elationhealth.com/
---

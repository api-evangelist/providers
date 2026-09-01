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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
  schema_version: 0.2
  score: 29.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 211
  human_in_the_loop: 9
  name: Alayacare Agentic Access
  operation_count: 437
  slug: alayacare-agentic-access
  summary_line: 437 operations · 211 acting · 9 human-in-the-loop
api_count: 15
apis:
- description: 'REST API for managing employee records including staff information, designations, departments, and employee-level attributes. Enables HR and workforce management integrations. Supports pagination and '
  name: AlayaCare Employee API
  slug: alayacare-employee-api
- description: REST API for accessing and managing visit scheduling data, including visit details, facility information, and service delivery records. Supports filtering by date range and pagination. Critical for bu
  name: AlayaCare Scheduler API
  slug: alayacare-scheduler-api
- description: REST API for accessing clinical documentation including progress notes, medications, vital signs, and clinical observations recorded during care visits. Supports integration with EMR/EHR systems and c
  name: AlayaCare Clinical API
  slug: alayacare-clinical-api
- description: REST API (v1 and v2) for managing care tasks assigned to clients and employees within AlayaCare. Supports creating, retrieving, and updating task records. Tasks v2 adds expanded capabilities. Used for
  name: AlayaCare Tasks API
  slug: alayacare-tasks-api
- description: 'REST API for accessing digital form submissions captured during care delivery, including assessment forms, intake forms, and clinical documentation forms. Updated November 2024 with Forms v2 support. '
  name: AlayaCare Forms API
  slug: alayacare-forms-api
- description: REST API for financial operations within AlayaCare, including billing records, invoices, and accounting data. Supports integration with payroll systems, financial reporting tools, and ERP platforms. A
  name: AlayaCare Accounting API
  slug: alayacare-accounting-api
- description: REST API for managing medication records associated with client care plans in AlayaCare. Supports retrieval of medication lists, dosage information, and administration records for integration with pha
  name: AlayaCare Medication API
  slug: alayacare-medication-api
- description: REST API for the AlayaMarket staffing marketplace enabling supply and demand organizations to exchange shift offers and staffing requests. Demand organizations use Outbox APIs to publish staffing need
  name: AlayaMarket Marketplace API
  slug: alayamarket-marketplace-api
- description: REST API for AlayaCare's residential aged care product, supporting client extensions, resident management, and care documentation specific to residential facility settings. Separate from the home care
  name: AlayaCare Residential (Resi) API
  slug: alayacare-residential-resi-api
- description: The Accounts API from AlayaCare — 2 operation(s) for accounts.
  name: AlayaCare Accounts API
  slug: alayacare-accounts-api
- description: The Activities of Daily Living (ADL) API from AlayaCare — 2 operation(s) for activities of daily living (adl).
  name: AlayaCare Activities of Daily Living (ADL) API
  slug: alayacare-activities-of-daily-living-adl-api
- description: The Activity Codes API from AlayaCare — 1 operation(s) for activity codes.
  name: AlayaCare Activity Codes API
  slug: alayacare-activity-codes-api
- description: The Attachment Directory API from AlayaCare — 2 operation(s) for attachment directory.
  name: AlayaCare Attachment Directory API
  slug: alayacare-attachment-directory-api
- description: The Attachment File API from AlayaCare — 2 operation(s) for attachment file.
  name: AlayaCare Attachment File API
  slug: alayacare-attachment-file-api
- description: The Bill Code Rate RRules API from AlayaCare — 2 operation(s) for bill code rate rrules.
  name: AlayaCare Bill Code Rate RRules API
  slug: alayacare-bill-code-rate-rrules-api
- description: The Bill Code Rates API from AlayaCare — 2 operation(s) for bill code rates.
  name: AlayaCare Bill Code Rates API
  slug: alayacare-bill-code-rates-api
- description: The Bill Codes API from AlayaCare — 4 operation(s) for bill codes.
  name: AlayaCare Bill Codes API
  slug: alayacare-bill-codes-api
- description: The Billing Cycles API from AlayaCare — 5 operation(s) for billing cycles.
  name: AlayaCare Billing Cycles API
  slug: alayacare-billing-cycles-api
- description: The Billing Periods API from AlayaCare — 4 operation(s) for billing periods.
  name: AlayaCare Billing Periods API
  slug: alayacare-billing-periods-api
- description: Branch related endpoints.
  name: AlayaCare Branches API
  slug: alayacare-branches-api
- description: The Bulk Actions API from AlayaCare — 2 operation(s) for bulk actions.
  name: AlayaCare Bulk Actions API
  slug: alayacare-bulk-actions-api
- description: The Care plan API from AlayaCare — 10 operation(s) for care plan.
  name: AlayaCare Care plan API
  slug: alayacare-care-plan-api
- description: The Care Plan Interventions API from AlayaCare — 2 operation(s) for care plan interventions.
  name: AlayaCare Care Plan Interventions API
  slug: alayacare-care-plan-interventions-api
- description: Care provider note related endpoints.
  name: AlayaCare Care Provider Notes API
  slug: alayacare-care-provider-notes-api
- description: Client contact related endpoints.
  name: AlayaCare Client Contacts API
  slug: alayacare-client-contacts-api
- description: The Client Cost Centres API from AlayaCare — 3 operation(s) for client cost centres.
  name: AlayaCare Client Cost Centres API
  slug: alayacare-client-cost-centres-api
- description: The Client Risks API from AlayaCare — 4 operation(s) for client risks.
  name: AlayaCare Client Risks API
  slug: alayacare-client-risks-api
- description: Client status related endpoints.
  name: AlayaCare Client Status API
  slug: alayacare-client-status-api
- description: Client related endpoints.
  name: AlayaCare Clients API
  slug: alayacare-clients-api
- description: The Comments API from AlayaCare — 2 operation(s) for comments.
  name: AlayaCare Comments API
  slug: alayacare-comments-api
- description: The Configured Vitals API from AlayaCare — 1 operation(s) for configured vitals.
  name: AlayaCare Configured Vitals API
  slug: alayacare-configured-vitals-api
- description: The Cost Centres API from AlayaCare — 1 operation(s) for cost centres.
  name: AlayaCare Cost Centres API
  slug: alayacare-cost-centres-api
- description: The Departments API from AlayaCare — 1 operation(s) for departments.
  name: AlayaCare Departments API
  slug: alayacare-departments-api
- description: The Designations API from AlayaCare — 1 operation(s) for designations.
  name: AlayaCare Designations API
  slug: alayacare-designations-api
- description: The Diagnoses API from AlayaCare — 4 operation(s) for diagnoses.
  name: AlayaCare Diagnoses API
  slug: alayacare-diagnoses-api
- description: The Directory API from AlayaCare — 1 operation(s) for directory.
  name: AlayaCare Directory API
  slug: alayacare-directory-api
- description: The Employee Contacts API from AlayaCare — 3 operation(s) for employee contacts.
  name: AlayaCare Employee Contacts API
  slug: alayacare-employee-contacts-api
- description: The Employee Cost Centres API from AlayaCare — 3 operation(s) for employee cost centres.
  name: AlayaCare Employee Cost Centres API
  slug: alayacare-employee-cost-centres-api
- description: The Employee Notes API from AlayaCare — 2 operation(s) for employee notes.
  name: AlayaCare Employee Notes API
  slug: alayacare-employee-notes-api
- description: The Employee Skills API from AlayaCare — 4 operation(s) for employee skills.
  name: AlayaCare Employee Skills API
  slug: alayacare-employee-skills-api
- description: The Employee Unavailabilities API from AlayaCare — 2 operation(s) for employee unavailabilities.
  name: AlayaCare Employee Unavailabilities API
  slug: alayacare-employee-unavailabilities-api
- description: The Employees API from AlayaCare — 7 operation(s) for employees.
  name: AlayaCare Employees API
  slug: alayacare-employees-api
- description: The Employment Types API from AlayaCare — 1 operation(s) for employment types.
  name: AlayaCare Employment Types API
  slug: alayacare-employment-types-api
- description: The EVV API from AlayaCare — 1 operation(s) for evv.
  name: AlayaCare EVV API
  slug: alayacare-evv-api
- description: The EVV Export API from AlayaCare — 4 operation(s) for evv export.
  name: AlayaCare EVV Export API
  slug: alayacare-evv-export-api
- description: The Facilities API from AlayaCare — 4 operation(s) for facilities.
  name: AlayaCare Facilities API
  slug: alayacare-facilities-api
- description: The File API from AlayaCare — 1 operation(s) for file.
  name: AlayaCare File API
  slug: alayacare-file-api
- description: The form submission inbox API from AlayaCare — 1 operation(s) for form submission inbox.
  name: AlayaCare form submission inbox API
  slug: alayacare-form-submission-inbox-api
- description: The form submission outbox API from AlayaCare — 2 operation(s) for form submission outbox.
  name: AlayaCare form submission outbox API
  slug: alayacare-form-submission-outbox-api
- description: The Form Submissions API from AlayaCare — 4 operation(s) for form submissions.
  name: AlayaCare Form Submissions API
  slug: alayacare-form-submissions-api
- description: The form template inbox API from AlayaCare — 1 operation(s) for form template inbox.
  name: AlayaCare form template inbox API
  slug: alayacare-form-template-inbox-api
- description: The Forms API from AlayaCare — 1 operation(s) for forms.
  name: AlayaCare Forms API
  slug: alayacare-forms-api
- description: The Funders API from AlayaCare — 2 operation(s) for funders.
  name: AlayaCare Funders API
  slug: alayacare-funders-api
- description: The Goals API from AlayaCare — 5 operation(s) for goals.
  name: AlayaCare Goals API
  slug: alayacare-goals-api
- description: Client group related endpoints.
  name: AlayaCare Groups API
  slug: alayacare-groups-api
- description: The Interventions API from AlayaCare — 5 operation(s) for interventions.
  name: AlayaCare Interventions API
  slug: alayacare-interventions-api
- description: The Invoice Items API from AlayaCare — 2 operation(s) for invoice items.
  name: AlayaCare Invoice Items API
  slug: alayacare-invoice-items-api
- description: The Invoices API from AlayaCare — 5 operation(s) for invoices.
  name: AlayaCare Invoices API
  slug: alayacare-invoices-api
- description: The Latest Vitals API from AlayaCare — 2 operation(s) for latest vitals.
  name: AlayaCare Latest Vitals API
  slug: alayacare-latest-vitals-api
- description: The Medication Administration API from AlayaCare — 2 operation(s) for medication administration.
  name: AlayaCare Medication Administration API
  slug: alayacare-medication-administration-api
- description: The Medication API from AlayaCare — 5 operation(s) for medication.
  name: AlayaCare Medication API
  slug: alayacare-medication-api
- description: The Medication settings API from AlayaCare — 3 operation(s) for medication settings.
  name: AlayaCare Medication settings API
  slug: alayacare-medication-settings-api
- description: The message inbox API from AlayaCare — 4 operation(s) for message inbox.
  name: AlayaCare message inbox API
  slug: alayacare-message-inbox-api
- description: The message outbox API from AlayaCare — 4 operation(s) for message outbox.
  name: AlayaCare message outbox API
  slug: alayacare-message-outbox-api
- description: The message sys_admin API from AlayaCare — 2 operation(s) for message sys_admin.
  name: AlayaCare message sys_admin API
  slug: alayacare-message-sys-admin-api
- description: The Note Types API from AlayaCare — 1 operation(s) for note types.
  name: AlayaCare Note Types API
  slug: alayacare-note-types-api
- description: The offer inbox API from AlayaCare — 4 operation(s) for offer inbox.
  name: AlayaCare offer inbox API
  slug: alayacare-offer-inbox-api
- description: The offer outbox API from AlayaCare — 5 operation(s) for offer outbox.
  name: AlayaCare offer outbox API
  slug: alayacare-offer-outbox-api
- description: The offer outbox bundle API from AlayaCare — 2 operation(s) for offer outbox bundle.
  name: AlayaCare offer outbox bundle API
  slug: alayacare-offer-outbox-bundle-api
- description: The offer status API from AlayaCare — 1 operation(s) for offer status.
  name: AlayaCare offer status API
  slug: alayacare-offer-status-api
- description: The offer sys_admin API from AlayaCare — 3 operation(s) for offer sys_admin.
  name: AlayaCare offer sys_admin API
  slug: alayacare-offer-sys-admin-api
- description: The organization settings API from AlayaCare — 1 operation(s) for organization settings.
  name: AlayaCare organization settings API
  slug: alayacare-organization-settings-api
- description: The organization settings sys_admin API from AlayaCare — 1 operation(s) for organization settings sys_admin.
  name: AlayaCare organization settings sys_admin API
  slug: alayacare-organization-settings-sys-admin-api
- description: The Premium Bill Codes API from AlayaCare — 1 operation(s) for premium bill codes.
  name: AlayaCare Premium Bill Codes API
  slug: alayacare-premium-bill-codes-api
- description: The Premiums API from AlayaCare — 2 operation(s) for premiums.
  name: AlayaCare Premiums API
  slug: alayacare-premiums-api
- description: Profile attribute related endpoints.
  name: AlayaCare Profile API
  slug: alayacare-profile-api
- description: The Progress Notes API from AlayaCare — 3 operation(s) for progress notes.
  name: AlayaCare Progress Notes API
  slug: alayacare-progress-notes-api
- description: The referral inbox API from AlayaCare — 5 operation(s) for referral inbox.
  name: AlayaCare referral inbox API
  slug: alayacare-referral-inbox-api
- description: The referral outbox API from AlayaCare — 4 operation(s) for referral outbox.
  name: AlayaCare referral outbox API
  slug: alayacare-referral-outbox-api
- description: The referral sys_admin API from AlayaCare — 2 operation(s) for referral sys_admin.
  name: AlayaCare referral sys_admin API
  slug: alayacare-referral-sys-admin-api
- description: The Roles API from AlayaCare — 1 operation(s) for roles.
  name: AlayaCare Roles API
  slug: alayacare-roles-api
- description: The sequence inbox API from AlayaCare — 1 operation(s) for sequence inbox.
  name: AlayaCare sequence inbox API
  slug: alayacare-sequence-inbox-api
- description: The sequence outbox API from AlayaCare — 1 operation(s) for sequence outbox.
  name: AlayaCare sequence outbox API
  slug: alayacare-sequence-outbox-api
- description: The sequence sys_admin API from AlayaCare — 1 operation(s) for sequence sys_admin.
  name: AlayaCare sequence sys_admin API
  slug: alayacare-sequence-sys-admin-api
- description: The Service Codes API from AlayaCare — 2 operation(s) for service codes.
  name: AlayaCare Service Codes API
  slug: alayacare-service-codes-api
- description: The Service Forms API from AlayaCare — 1 operation(s) for service forms.
  name: AlayaCare Service Forms API
  slug: alayacare-service-forms-api
- description: Service status related endpoints.
  name: AlayaCare Service Status API
  slug: alayacare-service-status-api
- description: The Service Tags API from AlayaCare — 1 operation(s) for service tags.
  name: AlayaCare Service Tags API
  slug: alayacare-service-tags-api
- description: The Services API from AlayaCare — 3 operation(s) for services.
  name: AlayaCare Services API
  slug: alayacare-services-api
- description: The Skill Categories API from AlayaCare — 1 operation(s) for skill categories.
  name: AlayaCare Skill Categories API
  slug: alayacare-skill-categories-api
- description: The Skills API from AlayaCare — 2 operation(s) for skills.
  name: AlayaCare Skills API
  slug: alayacare-skills-api
- description: The Status Reasons API from AlayaCare — 1 operation(s) for status reasons.
  name: AlayaCare Status Reasons API
  slug: alayacare-status-reasons-api
- description: The Subtasks API from AlayaCare — 3 operation(s) for subtasks.
  name: AlayaCare Subtasks API
  slug: alayacare-subtasks-api
- description: The Tags API from AlayaCare — 1 operation(s) for tags.
  name: AlayaCare Tags API
  slug: alayacare-tags-api
- description: The take rates API from AlayaCare — 3 operation(s) for take rates.
  name: AlayaCare take rates API
  slug: alayacare-take-rates-api
- description: The Tasks API from AlayaCare — 10 operation(s) for tasks.
  name: AlayaCare Tasks API
  slug: alayacare-tasks-api
- description: The Time Off Types API from AlayaCare — 1 operation(s) for time off types.
  name: AlayaCare Time Off Types API
  slug: alayacare-time-off-types-api
- description: The Transactions API from AlayaCare — 2 operation(s) for transactions.
  name: AlayaCare Transactions API
  slug: alayacare-transactions-api
- description: The Unavailabilities API from AlayaCare — 1 operation(s) for unavailabilities.
  name: AlayaCare Unavailabilities API
  slug: alayacare-unavailabilities-api
- description: The Visit accounting API from AlayaCare — 4 operation(s) for visit accounting.
  name: AlayaCare Visit accounting API
  slug: alayacare-visit-accounting-api
- description: The visit inbox API from AlayaCare — 14 operation(s) for visit inbox.
  name: AlayaCare visit inbox API
  slug: alayacare-visit-inbox-api
- description: The Visit interventions API from AlayaCare — 3 operation(s) for visit interventions.
  name: AlayaCare Visit interventions API
  slug: alayacare-visit-interventions-api
- description: The Visit notes API from AlayaCare — 2 operation(s) for visit notes.
  name: AlayaCare Visit notes API
  slug: alayacare-visit-notes-api
- description: The visit outbox API from AlayaCare — 2 operation(s) for visit outbox.
  name: AlayaCare visit outbox API
  slug: alayacare-visit-outbox-api
- description: The Visit Premiums API from AlayaCare — 2 operation(s) for visit premiums.
  name: AlayaCare Visit Premiums API
  slug: alayacare-visit-premiums-api
- description: The visit sys_admin API from AlayaCare — 2 operation(s) for visit sys_admin.
  name: AlayaCare visit sys_admin API
  slug: alayacare-visit-sys-admin-api
- description: The Visit tags API from AlayaCare — 5 operation(s) for visit tags.
  name: AlayaCare Visit tags API
  slug: alayacare-visit-tags-api
- description: The Visit Verification API from AlayaCare — 1 operation(s) for visit verification.
  name: AlayaCare Visit Verification API
  slug: alayacare-visit-verification-api
- description: The Visits API from AlayaCare — 8 operation(s) for visits.
  name: AlayaCare Visits API
  slug: alayacare-visits-api
- description: The Vital Metadata API from AlayaCare — 2 operation(s) for vital metadata.
  name: AlayaCare Vital Metadata API
  slug: alayacare-vital-metadata-api
- description: The Vitals API from AlayaCare — 3 operation(s) for vitals.
  name: AlayaCare Vitals API
  slug: alayacare-vitals-api
- description: The work session inbox API from AlayaCare — 2 operation(s) for work session inbox.
  name: AlayaCare work session inbox API
  slug: alayacare-work-session-inbox-api
- description: The work session outbox API from AlayaCare — 1 operation(s) for work session outbox.
  name: AlayaCare work session outbox API
  slug: alayacare-work-session-outbox-api
artifact_total: 239
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AlayaCare Accounting Accounts API
  slug: open-alayacare-accounts-api
- collection_type: open
  name: AlayaCare Accounting Accounts Activities of Daily Living (ADL) API
  slug: open-alayacare-activities-of-daily-living-adl-api
- collection_type: open
  name: AlayaCare Accounting Accounts Activity Codes API
  slug: open-alayacare-activity-codes-api
- collection_type: open
  name: AlayaCare Accounting Accounts Attachment Directory API
  slug: open-alayacare-attachment-directory-api
- collection_type: open
  name: AlayaCare Accounting Accounts Attachment File API
  slug: open-alayacare-attachment-file-api
- collection_type: open
  name: AlayaCare Accounting Accounts Bill Code Rate RRules API
  slug: open-alayacare-bill-code-rate-rrules-api
- collection_type: open
  name: AlayaCare Accounting Accounts Bill Code Rates API
  slug: open-alayacare-bill-code-rates-api
- collection_type: open
  name: AlayaCare Accounting Accounts Bill Codes API
  slug: open-alayacare-bill-codes-api
- collection_type: open
  name: AlayaCare Accounting Accounts Billing Cycles API
  slug: open-alayacare-billing-cycles-api
- collection_type: open
  name: AlayaCare Accounting Accounts Billing Periods API
  slug: open-alayacare-billing-periods-api
- collection_type: open
  name: AlayaCare Accounting Accounts Branches API
  slug: open-alayacare-branches-api
- collection_type: open
  name: AlayaCare Accounting Accounts Bulk Actions API
  slug: open-alayacare-bulk-actions-api
- collection_type: open
  name: AlayaCare Accounting Accounts Care plan API
  slug: open-alayacare-care-plan-api
- collection_type: open
  name: AlayaCare Accounting Accounts Care Plan Interventions API
  slug: open-alayacare-care-plan-interventions-api
- collection_type: open
  name: AlayaCare Accounting Accounts Care Provider Notes API
  slug: open-alayacare-care-provider-notes-api
- collection_type: open
  name: AlayaCare Accounting Accounts Client Contacts API
  slug: open-alayacare-client-contacts-api
- collection_type: open
  name: AlayaCare Accounting Accounts Client Cost Centres API
  slug: open-alayacare-client-cost-centres-api
- collection_type: open
  name: AlayaCare Accounting Accounts Client Risks API
  slug: open-alayacare-client-risks-api
- collection_type: open
  name: AlayaCare Accounting Accounts Client Status API
  slug: open-alayacare-client-status-api
- collection_type: open
  name: AlayaCare Accounting Accounts Clients API
  slug: open-alayacare-clients-api
- collection_type: open
  name: AlayaCare Accounting Accounts Comments API
  slug: open-alayacare-comments-api
- collection_type: open
  name: AlayaCare Accounting Accounts Configured Vitals API
  slug: open-alayacare-configured-vitals-api
- collection_type: open
  name: AlayaCare Accounting Accounts Cost Centres API
  slug: open-alayacare-cost-centres-api
- collection_type: open
  name: AlayaCare Accounting Accounts Departments API
  slug: open-alayacare-departments-api
- collection_type: open
  name: AlayaCare Accounting Accounts Designations API
  slug: open-alayacare-designations-api
- collection_type: open
  name: AlayaCare Accounting Accounts Diagnoses API
  slug: open-alayacare-diagnoses-api
- collection_type: open
  name: AlayaCare Accounting Accounts Directory API
  slug: open-alayacare-directory-api
- collection_type: open
  name: AlayaCare Accounting Accounts Employee Contacts API
  slug: open-alayacare-employee-contacts-api
- collection_type: open
  name: AlayaCare Accounting Accounts Employee Cost Centres API
  slug: open-alayacare-employee-cost-centres-api
- collection_type: open
  name: AlayaCare Accounting Accounts Employee Notes API
  slug: open-alayacare-employee-notes-api
- collection_type: open
  name: AlayaCare Accounting Accounts Employee Skills API
  slug: open-alayacare-employee-skills-api
- collection_type: open
  name: AlayaCare Accounting Accounts Employee Unavailabilities API
  slug: open-alayacare-employee-unavailabilities-api
- collection_type: open
  name: AlayaCare Accounting Accounts Employees API
  slug: open-alayacare-employees-api
- collection_type: open
  name: AlayaCare Accounting Accounts Employment Types API
  slug: open-alayacare-employment-types-api
- collection_type: open
  name: AlayaCare Accounting Accounts EVV API
  slug: open-alayacare-evv-api
- collection_type: open
  name: AlayaCare Accounting Accounts EVV Export API
  slug: open-alayacare-evv-export-api
- collection_type: open
  name: AlayaCare Accounting Accounts Facilities API
  slug: open-alayacare-facilities-api
- collection_type: open
  name: AlayaCare Accounting Accounts File API
  slug: open-alayacare-file-api
- collection_type: open
  name: AlayaCare Accounting Accounts form submission inbox API
  slug: open-alayacare-form-submission-inbox-api
- collection_type: open
  name: AlayaCare Accounting Accounts form submission outbox API
  slug: open-alayacare-form-submission-outbox-api
- collection_type: open
  name: AlayaCare Accounting Accounts Form Submissions API
  slug: open-alayacare-form-submissions-api
- collection_type: open
  name: AlayaCare Accounting Accounts form template inbox API
  slug: open-alayacare-form-template-inbox-api
- collection_type: open
  name: AlayaCare Accounting Accounts Forms API
  slug: open-alayacare-forms-api
- collection_type: open
  name: AlayaCare Accounting Accounts Funders API
  slug: open-alayacare-funders-api
- collection_type: open
  name: AlayaCare Accounting Accounts Goals API
  slug: open-alayacare-goals-api
- collection_type: open
  name: AlayaCare Accounting Accounts Groups API
  slug: open-alayacare-groups-api
- collection_type: open
  name: AlayaCare Accounting Accounts Interventions API
  slug: open-alayacare-interventions-api
- collection_type: open
  name: AlayaCare Accounting Accounts Invoice Items API
  slug: open-alayacare-invoice-items-api
- collection_type: open
  name: AlayaCare Accounting Accounts Invoices API
  slug: open-alayacare-invoices-api
- collection_type: open
  name: AlayaCare Accounting Accounts Latest Vitals API
  slug: open-alayacare-latest-vitals-api
- collection_type: open
  name: AlayaCare Accounting Accounts Medication Administration API
  slug: open-alayacare-medication-administration-api
- collection_type: open
  name: AlayaCare Accounting Accounts Medication API
  slug: open-alayacare-medication-api
- collection_type: open
  name: AlayaCare Accounting Accounts Medication settings API
  slug: open-alayacare-medication-settings-api
- collection_type: open
  name: AlayaCare Accounting Accounts message inbox API
  slug: open-alayacare-message-inbox-api
- collection_type: open
  name: AlayaCare Accounting Accounts message outbox API
  slug: open-alayacare-message-outbox-api
- collection_type: open
  name: AlayaCare Accounting Accounts message sys_admin API
  slug: open-alayacare-message-sys-admin-api
- collection_type: open
  name: AlayaCare Accounting Accounts Note Types API
  slug: open-alayacare-note-types-api
- collection_type: open
  name: AlayaCare Accounting Accounts offer inbox API
  slug: open-alayacare-offer-inbox-api
- collection_type: open
  name: AlayaCare Accounting Accounts offer outbox API
  slug: open-alayacare-offer-outbox-api
- collection_type: open
  name: AlayaCare Accounting Accounts offer outbox bundle API
  slug: open-alayacare-offer-outbox-bundle-api
- collection_type: open
  name: AlayaCare Accounting Accounts offer status API
  slug: open-alayacare-offer-status-api
- collection_type: open
  name: AlayaCare Accounting Accounts offer sys_admin API
  slug: open-alayacare-offer-sys-admin-api
- collection_type: open
  name: AlayaCare Accounting Accounts organization settings API
  slug: open-alayacare-organization-settings-api
- collection_type: open
  name: AlayaCare Accounting Accounts organization settings sys_admin API
  slug: open-alayacare-organization-settings-sys-admin-api
- collection_type: open
  name: AlayaCare Accounting Accounts Premium Bill Codes API
  slug: open-alayacare-premium-bill-codes-api
- collection_type: open
  name: AlayaCare Accounting Accounts Premiums API
  slug: open-alayacare-premiums-api
- collection_type: open
  name: AlayaCare Accounting Accounts Profile API
  slug: open-alayacare-profile-api
- collection_type: open
  name: AlayaCare Accounting Accounts Progress Notes API
  slug: open-alayacare-progress-notes-api
- collection_type: open
  name: AlayaCare Accounting Accounts referral inbox API
  slug: open-alayacare-referral-inbox-api
- collection_type: open
  name: AlayaCare Accounting Accounts referral outbox API
  slug: open-alayacare-referral-outbox-api
- collection_type: open
  name: AlayaCare Accounting Accounts referral sys_admin API
  slug: open-alayacare-referral-sys-admin-api
- collection_type: open
  name: AlayaCare Accounting Accounts Roles API
  slug: open-alayacare-roles-api
- collection_type: open
  name: AlayaCare Accounting Accounts sequence inbox API
  slug: open-alayacare-sequence-inbox-api
- collection_type: open
  name: AlayaCare Accounting Accounts sequence outbox API
  slug: open-alayacare-sequence-outbox-api
- collection_type: open
  name: AlayaCare Accounting Accounts sequence sys_admin API
  slug: open-alayacare-sequence-sys-admin-api
- collection_type: open
  name: AlayaCare Accounting Accounts Service Codes API
  slug: open-alayacare-service-codes-api
- collection_type: open
  name: AlayaCare Accounting Accounts Service Forms API
  slug: open-alayacare-service-forms-api
- collection_type: open
  name: AlayaCare Accounting Accounts Service Status API
  slug: open-alayacare-service-status-api
- collection_type: open
  name: AlayaCare Accounting Accounts Service Tags API
  slug: open-alayacare-service-tags-api
- collection_type: open
  name: AlayaCare Accounting Accounts Services API
  slug: open-alayacare-services-api
- collection_type: open
  name: AlayaCare Accounting Accounts Skill Categories API
  slug: open-alayacare-skill-categories-api
- collection_type: open
  name: AlayaCare Accounting Accounts Skills API
  slug: open-alayacare-skills-api
- collection_type: open
  name: AlayaCare Accounting Accounts Status Reasons API
  slug: open-alayacare-status-reasons-api
- collection_type: open
  name: AlayaCare Accounting Accounts Subtasks API
  slug: open-alayacare-subtasks-api
- collection_type: open
  name: AlayaCare Accounting Accounts Tags API
  slug: open-alayacare-tags-api
- collection_type: open
  name: AlayaCare Accounting Accounts take rates API
  slug: open-alayacare-take-rates-api
- collection_type: open
  name: AlayaCare Accounting Accounts Tasks API
  slug: open-alayacare-tasks-api
- collection_type: open
  name: AlayaCare Accounting Accounts Time Off Types API
  slug: open-alayacare-time-off-types-api
- collection_type: open
  name: AlayaCare Accounting Accounts Transactions API
  slug: open-alayacare-transactions-api
- collection_type: open
  name: AlayaCare Accounting Accounts Unavailabilities API
  slug: open-alayacare-unavailabilities-api
- collection_type: open
  name: AlayaCare Accounting Accounts Visit accounting API
  slug: open-alayacare-visit-accounting-api
- collection_type: open
  name: AlayaCare Accounting Accounts visit inbox API
  slug: open-alayacare-visit-inbox-api
- collection_type: open
  name: AlayaCare Accounting Accounts Visit interventions API
  slug: open-alayacare-visit-interventions-api
- collection_type: open
  name: AlayaCare Accounting Accounts Visit notes API
  slug: open-alayacare-visit-notes-api
- collection_type: open
  name: AlayaCare Accounting Accounts visit outbox API
  slug: open-alayacare-visit-outbox-api
- collection_type: open
  name: AlayaCare Accounting Accounts Visit Premiums API
  slug: open-alayacare-visit-premiums-api
- collection_type: open
  name: AlayaCare Accounting Accounts visit sys_admin API
  slug: open-alayacare-visit-sys-admin-api
- collection_type: open
  name: AlayaCare Accounting Accounts Visit tags API
  slug: open-alayacare-visit-tags-api
- collection_type: open
  name: AlayaCare Accounting Accounts Visit Verification API
  slug: open-alayacare-visit-verification-api
- collection_type: open
  name: AlayaCare Accounting Accounts Visits API
  slug: open-alayacare-visits-api
- collection_type: open
  name: AlayaCare Accounting Accounts Vital Metadata API
  slug: open-alayacare-vital-metadata-api
- collection_type: open
  name: AlayaCare Accounting Accounts Vitals API
  slug: open-alayacare-vitals-api
- collection_type: open
  name: AlayaCare Accounting Accounts work session inbox API
  slug: open-alayacare-work-session-inbox-api
- collection_type: open
  name: AlayaCare Accounting Accounts work session outbox API
  slug: open-alayacare-work-session-outbox-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/alayacare-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/alayacare-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alayacare-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/alayacare-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://alayacare.com/
- group: docs
  title: ''
  type: Documentation
  url: https://alayacare.github.io/external-integration-docs/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/alayacare
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alayacare/
- group: company
  title: ''
  type: Blog
  url: https://alayacare.com/blog/
- group: build
  title: ''
  type: IntegrationsBrochure
  url: https://alayacare.com/brochures/alayacare-integrations-and-apis/
- group: commercial
  title: ''
  type: APITerms
  url: https://alayacare.com/wp-content/uploads/2022/12/AlayaCare-API-Developer-Access-Terms-.pdf
- group: commercial
  title: ''
  type: Plans
  url: plans/alayacare-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/alayacare-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/alayacare-finops.yml
created: '2026-06-13'
description: AlayaCare is a cloud-based home and community care management platform providing REST APIs for managing client profiles, scheduling visits, documenting clinical care, processing billing and accounting, and tracking patient outcomes. The platform serves home care agencies, nursing registries, and government-funded community care programs globally. APIs cover clients, employees, scheduling, clinical records, tasks, forms, medications, accounting, and file management, with integration via REST and AWS SQS event streaming. AlayaCare also offers AlayaMarket, a staffing marketplace API for matching supply and demand organizations, and AlayaCare Residential for residential aged care settings.
examples:
- key_count: 9
  name: Alayacare Medication Examples
  slug: alayacare-medication-examples
- key_count: 3
  name: Alayacare Services Examples
  slug: alayacare-services-examples
finops:
- name: Alayacare Finops
  service_category: ''
  slug: alayacare-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alayacare.png
json_schemas:
- name: AlayaCare Accounting API Schemas
  property_count: 0
  slug: alayacare-accounting
- name: AlayaCare Careplan API Schemas
  property_count: 0
  slug: alayacare-careplan
- name: AlayaCare Client API Schemas
  property_count: 0
  slug: alayacare-client
- name: AlayaCare Clinical API Schemas
  property_count: 0
  slug: alayacare-clinical
- name: AlayaCare Employee API Schemas
  property_count: 0
  slug: alayacare-employee
- name: AlayaCare Market API Schemas
  property_count: 0
  slug: alayacare-market
- name: AlayaCare Medication API Schemas
  property_count: 0
  slug: alayacare-medication
- name: AlayaCare Scheduler API Schemas
  property_count: 0
  slug: alayacare-scheduler
- name: AlayaCare Services API Schemas
  property_count: 0
  slug: alayacare-services
- name: AlayaCare Tasks API Schemas
  property_count: 0
  slug: alayacare-tasks
- name: AlayaCare Tasks-V2 API Schemas
  property_count: 0
  slug: alayacare-tasks-v2
jsonld:
- class_count: 16
  name: Alayacare Context
  property_count: 49
  slug: alayacare-context
layout: provider
modified: '2026-06-13'
name: AlayaCare
nav: Providers
network: true
overview: 'AlayaCare publishes 107 APIs on the [APIs.io](https://apis.io/) network, including Tasks API, Forms API, Medication API, and 104 more. Tagged areas include Home Care, Community Care, Healthcare, Scheduling, and Clinical.


  The AlayaCare catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AlayaCare''s developer surface includes authentication, documentation, GitHub presence, engineering blog, and 10 more developer resources.'
plans:
- name: Alayacare Plans Pricing
  plan_count: 4
  slug: alayacare-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 4
  name: Alayacare Rate Limits
  slug: alayacare-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: AlayaCare API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: alayacare-jsonschema-spectral-rules
score:
  band: developing
  composite: 39.8
  coverage:
    artifact_dirs: 16
    catalog_gap: 36.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 55.7
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 36.8
  previous_composite: 39.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 104
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alayacare/refs/heads/main/screenshots/alayacare-2026-06-20T171503.png
security:
- kind: authentication
  name: Alayacare Authentication
  slug: alayacare-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Alayacare Domain Security
  slug: alayacare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alayacare
tags:
- Home Care
- Community Care
- Healthcare
- Scheduling
- Clinical
- Billing
- Client Management
- Care Management
- Aged Care
- Workforce Management
website: https://alayacare.com/
---

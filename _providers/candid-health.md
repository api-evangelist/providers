---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 141
  human_in_the_loop: 0
  name: Candid Health Agentic Access
  operation_count: 251
  slug: candid-health-agentic-access
  summary_line: 251 operations · 141 acting
api_count: 1
apis:
- description: Manage patient invoicing, payments, refunds, and accounts receivable. Automates patient billing workflows and tracks outstanding balances.
  name: Candid Health Patient Collections API
  slug: candid-health-patient-collections-api
- description: Create and manage charge capture claims and bundles for batch claim processing. Enables claim creation from clinical encounters.
  name: Candid Health Charge Capture API
  slug: candid-health-charge-capture-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: Download CSV exports of claim status changes, financial data, and reporting information for revenue cycle analytics and reconciliation.
  name: Candid Health Exports API
  slug: candid-health-exports-api
- baseURL: https://pre-api.joincandidhealth.com
  baseurl_source: declared
  description: Core patient management and search capabilities including coverages, appointments, images, notes, lists, and tagging for pre-encounter workflows.
  name: Candid Health Patients API
  slug: candid-health-patients-api
- description: Manage provider and facility credentialing spans, organization providers, service facilities, contracts, payers, and fee schedules.
  name: Candid Health Credentialing API
  slug: candid-health-credentialing-api
- description: OAuth 2.0 client credentials token generation for authenticating API access to all Candid Health REST endpoints.
  name: Candid Health Auth API
  slug: candid-health-auth-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The default API from Candid Health — 1 operation(s) for default.
  name: Candid Health Default API
  slug: candid-health-default-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The diagnoses API from Candid Health — 2 operation(s) for diagnoses.
  name: Candid Health Diagnoses API
  slug: candid-health-diagnoses-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Appointments API from Candid Health — 7 operation(s) for appointments.
  name: Candid Health Appointments API
  slug: candid-health-appointments-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Billing Notes API from Candid Health — 2 operation(s) for billing notes.
  name: Candid Health Billing Notes API
  slug: candid-health-billing-notes-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Charge Capture Claim Creation API from Candid Health — 4 operation(s) for charge capture claim creation.
  name: Candid Health Charge Capture Claim Creation API
  slug: candid-health-charge-capture-claim-creation-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Charge Captures API from Candid Health — 5 operation(s) for charge captures.
  name: Candid Health Charge Captures API
  slug: candid-health-charge-captures-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Contracts API from Candid Health — 8 operation(s) for contracts.
  name: Candid Health Contracts API
  slug: candid-health-contracts-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Coverages API from Candid Health — 9 operation(s) for coverages.
  name: Candid Health Coverages API
  slug: candid-health-coverages-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Custom Schemas API from Candid Health — 2 operation(s) for custom schemas.
  name: Candid Health Custom Schemas API
  slug: candid-health-custom-schemas-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Eligibility API from Candid Health — 1 operation(s) for eligibility.
  name: Candid Health Eligibility API
  slug: candid-health-eligibility-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Eligibility Checks API from Candid Health — 9 operation(s) for eligibility checks.
  name: Candid Health Eligibility Checks API
  slug: candid-health-eligibility-checks-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Encounter Attachments API from Candid Health — 4 operation(s) for encounter attachments.
  name: Candid Health Encounter Attachments API
  slug: candid-health-encounter-attachments-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Encounter Providers API from Candid Health — 9 operation(s) for encounter providers.
  name: Candid Health Encounter Providers API
  slug: candid-health-encounter-providers-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Encounter Supplemental Information API from Candid Health — 2 operation(s) for encounter supplemental information.
  name: Candid Health Encounter Supplemental Information API
  slug: candid-health-encounter-supplemental-information-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Encounters API from Candid Health — 6 operation(s) for encounters.
  name: Candid Health Encounters API
  slug: candid-health-encounters-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Events API from Candid Health — 2 operation(s) for events.
  name: Candid Health Events API
  slug: candid-health-events-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Exports API from Candid Health — 1 operation(s) for exports.
  name: Candid Health Exports API
  slug: candid-health-exports-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The External Payment Account Config API from Candid Health — 1 operation(s) for external payment account config.
  name: Candid Health External Payment Account Config API
  slug: candid-health-external-payment-account-config-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Fee Schedules API from Candid Health — 11 operation(s) for fee schedules.
  name: Candid Health Fee Schedules API
  slug: candid-health-fee-schedules-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Guarantors API from Candid Health — 2 operation(s) for guarantors.
  name: Candid Health Guarantors API
  slug: candid-health-guarantors-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Health Care Code Informations API from Candid Health — 1 operation(s) for health care code informations.
  name: Candid Health Health Care Code Informations API
  slug: candid-health-health-care-code-informations-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Images API from Candid Health — 3 operation(s) for images.
  name: Candid Health Images API
  slug: candid-health-images-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Import Invoice API from Candid Health — 2 operation(s) for import invoice.
  name: Candid Health Import Invoice API
  slug: candid-health-import-invoice-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Insurance Adjudications API from Candid Health — 1 operation(s) for insurance adjudications.
  name: Candid Health Insurance Adjudications API
  slug: candid-health-insurance-adjudications-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Insurance Refunds API from Candid Health — 2 operation(s) for insurance refunds.
  name: Candid Health Insurance Refunds API
  slug: candid-health-insurance-refunds-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Lists API from Candid Health — 2 operation(s) for lists.
  name: Candid Health Lists API
  slug: candid-health-lists-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Medication Dispense API from Candid Health — 1 operation(s) for medication dispense.
  name: Candid Health Medication Dispense API
  slug: candid-health-medication-dispense-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Non Insurance Payer Payments API from Candid Health — 2 operation(s) for non insurance payer payments.
  name: Candid Health Non Insurance Payer Payments API
  slug: candid-health-non-insurance-payer-payments-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Non Insurance Payer Refunds API from Candid Health — 2 operation(s) for non insurance payer refunds.
  name: Candid Health Non Insurance Payer Refunds API
  slug: candid-health-non-insurance-payer-refunds-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Non Insurance Payers API from Candid Health — 4 operation(s) for non insurance payers.
  name: Candid Health Non Insurance Payers API
  slug: candid-health-non-insurance-payers-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Notes API from Candid Health — 3 operation(s) for notes.
  name: Candid Health Notes API
  slug: candid-health-notes-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Organization External Providers API from Candid Health — 4 operation(s) for organization external providers.
  name: Candid Health Organization External Providers API
  slug: candid-health-organization-external-providers-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Organization Providers API from Candid Health — 5 operation(s) for organization providers.
  name: Candid Health Organization Providers API
  slug: candid-health-organization-providers-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Organization Service Facilities API from Candid Health — 3 operation(s) for organization service facilities.
  name: Candid Health Organization Service Facilities API
  slug: candid-health-organization-service-facilities-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Patient Ar API from Candid Health — 2 operation(s) for patient ar.
  name: Candid Health Patient Ar API
  slug: candid-health-patient-ar-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Patient Merge API from Candid Health — 5 operation(s) for patient merge.
  name: Candid Health Patient Merge API
  slug: candid-health-patient-merge-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Patient Payments API from Candid Health — 2 operation(s) for patient payments.
  name: Candid Health Patient Payments API
  slug: candid-health-patient-payments-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Patient Refunds API from Candid Health — 2 operation(s) for patient refunds.
  name: Candid Health Patient Refunds API
  slug: candid-health-patient-refunds-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Patients API from Candid Health — 11 operation(s) for patients.
  name: Candid Health Patients API
  slug: candid-health-patients-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Payer Plan Groups API from Candid Health — 2 operation(s) for payer plan groups.
  name: Candid Health Payer Plan Groups API
  slug: candid-health-payer-plan-groups-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Payers API from Candid Health — 4 operation(s) for payers.
  name: Candid Health Payers API
  slug: candid-health-payers-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Provider Credentialing Span API from Candid Health — 4 operation(s) for provider credentialing span.
  name: Candid Health Provider Credentialing Span API
  slug: candid-health-provider-credentialing-span-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Service Lines API from Candid Health — 4 operation(s) for service lines.
  name: Candid Health Service Lines API
  slug: candid-health-service-lines-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Superbill API from Candid Health — 1 operation(s) for superbill.
  name: Candid Health Superbill API
  slug: candid-health-superbill-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Tags API from Candid Health — 3 operation(s) for tags.
  name: Candid Health Tags API
  slug: candid-health-tags-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Tasks API from Candid Health — 3 operation(s) for tasks.
  name: Candid Health Tasks API
  slug: candid-health-tasks-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The Write Offs API from Candid Health — 5 operation(s) for write offs.
  name: Candid Health Write Offs API
  slug: candid-health-write-offs-api
artifact_total: 136
collections:
- collection_type: open
  name: Candid Health Auth API
  slug: open-candid-health-auth-api
- collection_type: open
  name: Candid Health Auth Charge Capture API
  slug: open-candid-health-charge-capture-api
- collection_type: open
  name: Candid Health Auth Eligibility API
  slug: open-candid-health-eligibility-api
- collection_type: open
  name: Candid Health Auth Encounters API
  slug: open-candid-health-encounters-api
- collection_type: open
  name: Candid Health Auth Events API
  slug: open-candid-health-events-api
- collection_type: open
  name: Candid Health Auth Fee Schedules API
  slug: open-candid-health-fee-schedules-api
- collection_type: open
  name: Candid Health Auth Insurance Adjudications API
  slug: open-candid-health-insurance-adjudications-api
- collection_type: open
  name: Candid Health Auth Payers API
  slug: open-candid-health-payers-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default API
  slug: open-candid-health-subpackage-auth-subpackage-auth-default-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_billing-notes.subpackage_billing-notes/v2 API
  slug: open-candid-health-subpackage-billing-notes-subpackage-billing-notes-v2-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_charge-capture-bundles.subpackage_charge-capture-bundles/v1 API
  slug: open-candid-health-subpackage-charge-capture-bundles-subpackage-charge-capture-bundles-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_charge-capture.subpackage_charge-capture/v1 API
  slug: open-candid-health-subpackage-charge-capture-subpackage-charge-capture-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_contracts.subpackage_contracts/v2 API
  slug: open-candid-health-subpackage-contracts-subpackage-contracts-v2-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_contracts.subpackage_contracts/v3 API
  slug: open-candid-health-subpackage-contracts-subpackage-contracts-v3-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_credentialing.subpackage_credentialing/v2 API
  slug: open-candid-health-subpackage-credentialing-subpackage-credentialing-v2-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_custom-schemas.subpackage_custom-schemas/v1 API
  slug: open-candid-health-subpackage-custom-schemas-subpackage-custom-schemas-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_diagnoses API
  slug: open-candid-health-subpackage-diagnoses-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_eligibility.subpackage_eligibility/v2 API
  slug: open-candid-health-subpackage-eligibility-subpackage-eligibility-v2-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_encounter-attachments.subpackage_encounter-attachments/v1 API
  slug: open-candid-health-subpackage-encounter-attachments-subpackage-encounter-attachments-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_encounter-providers.subpackage_encounter-providers/v2 API
  slug: open-candid-health-subpackage-encounter-providers-subpackage-encounter-providers-v2-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_encounter-supplemental-information.subpackage_encounter-supplemental-information/v1 API
  slug: open-candid-health-subpackage-encounter-supplemental-information-subpackage-encounter-supplemental-information-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_encounters.subpackage_encounters/v4 API
  slug: open-candid-health-subpackage-encounters-subpackage-encounters-v4-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_events.subpackage_events/v1 API
  slug: open-candid-health-subpackage-events-subpackage-events-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_exports.subpackage_exports/v3 API
  slug: open-candid-health-subpackage-exports-subpackage-exports-v3-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_external-payment-account-config.subpackage_external-payment-account-config/v1 API
  slug: open-candid-health-subpackage-external-payment-account-config-subpackage-external-payment-account-config-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_fee-schedules.subpackage_fee-schedules/v3 API
  slug: open-candid-health-subpackage-fee-schedules-subpackage-fee-schedules-v3-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_guarantor.subpackage_guarantor/v1 API
  slug: open-candid-health-subpackage-guarantor-subpackage-guarantor-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_health-care-code-information.subpackage_health-care-code-information/v1 API
  slug: open-candid-health-subpackage-health-care-code-information-subpackage-health-care-code-information-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_import-invoice.subpackage_import-invoice/v1 API
  slug: open-candid-health-subpackage-import-invoice-subpackage-import-invoice-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_insurance-adjudications.subpackage_insurance-adjudications/v1 API
  slug: open-candid-health-subpackage-insurance-adjudications-subpackage-insurance-adjudications-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_insurance-refunds.subpackage_insurance-refunds/v1 API
  slug: open-candid-health-subpackage-insurance-refunds-subpackage-insurance-refunds-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_medication-dispense.subpackage_medication-dispense/v1 API
  slug: open-candid-health-subpackage-medication-dispense-subpackage-medication-dispense-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_non-insurance-payer-payments.subpackage_non-insurance-payer-payments/v1 API
  slug: open-candid-health-subpackage-non-insurance-payer-payments-subpackage-non-insurance-payer-payments-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_non-insurance-payer-refunds.subpackage_non-insurance-payer-refunds/v1 API
  slug: open-candid-health-subpackage-non-insurance-payer-refunds-subpackage-non-insurance-payer-refunds-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_non-insurance-payers.subpackage_non-insurance-payers/v1 API
  slug: open-candid-health-subpackage-non-insurance-payers-subpackage-non-insurance-payers-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_organization-providers.subpackage_organization-providers/v3 API
  slug: open-candid-health-subpackage-organization-providers-subpackage-organization-providers-v3-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_organization-service-facilities.subpackage_organization-service-facilities/v2 API
  slug: open-candid-health-subpackage-organization-service-facilities-subpackage-organization-service-facilities-v2-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_patient-ar.subpackage_patient-ar/v1 API
  slug: open-candid-health-subpackage-patient-ar-subpackage-patient-ar-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_patient-payments.subpackage_patient-payments/v4 API
  slug: open-candid-health-subpackage-patient-payments-subpackage-patient-payments-v4-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_patient-refunds.subpackage_patient-refunds/v1 API
  slug: open-candid-health-subpackage-patient-refunds-subpackage-patient-refunds-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_payer-plan-groups.subpackage_payer-plan-groups/v1 API
  slug: open-candid-health-subpackage-payer-plan-groups-subpackage-payer-plan-groups-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_payers.subpackage_payers/v3 API
  slug: open-candid-health-subpackage-payers-subpackage-payers-v3-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_payers.subpackage_payers/v4 API
  slug: open-candid-health-subpackage-payers-subpackage-payers-v4-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_pre-encounter.subpackage_pre-encounter/appointments.subpackage_pre-encounter/appointments/v1 API
  slug: open-candid-health-subpackage-pre-encounter-subpackage-pre-encounter-appointments-subpackage-pre-encounter-appointments-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_pre-encounter.subpackage_pre-encounter/coverages.subpackage_pre-encounter/coverages/v1 API
  slug: open-candid-health-subpackage-pre-encounter-subpackage-pre-encounter-coverages-subpackage-pre-encounter-coverages-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_pre-encounter.subpackage_pre-encounter/eligibilityChecks.subpackage_pre-encounter/eligibilityChecks/v1 API
  slug: open-candid-health-subpackage-pre-encounter-subpackage-pre-encounter-eligibilitychecks-subpackage-pre-encounter-eligibilitychecks-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_pre-encounter.subpackage_pre-encounter/images.subpackage_pre-encounter/images/v1 API
  slug: open-candid-health-subpackage-pre-encounter-subpackage-pre-encounter-images-subpackage-pre-encounter-images-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_pre-encounter.subpackage_pre-encounter/lists.subpackage_pre-encounter/lists/v1 API
  slug: open-candid-health-subpackage-pre-encounter-subpackage-pre-encounter-lists-subpackage-pre-encounter-lists-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_pre-encounter.subpackage_pre-encounter/notes.subpackage_pre-encounter/notes/v1 API
  slug: open-candid-health-subpackage-pre-encounter-subpackage-pre-encounter-notes-subpackage-pre-encounter-notes-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_pre-encounter.subpackage_pre-encounter/organizationExternalProviders.subpackage_pre-encounter/organizationExternalProviders/v1 API
  slug: open-candid-health-subpackage-pre-encounter-subpackage-pre-encounter-organizationexternalproviders-subpackage-pre-encounter-organizationexternalproviders-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_pre-encounter.subpackage_pre-encounter/patients.subpackage_pre-encounter/patients/v1 API
  slug: open-candid-health-subpackage-pre-encounter-subpackage-pre-encounter-patients-subpackage-pre-encounter-patients-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_pre-encounter.subpackage_pre-encounter/tags.subpackage_pre-encounter/tags/v1 API
  slug: open-candid-health-subpackage-pre-encounter-subpackage-pre-encounter-tags-subpackage-pre-encounter-tags-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_service-lines.subpackage_service-lines/v2 API
  slug: open-candid-health-subpackage-service-lines-subpackage-service-lines-v2-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_superbills.subpackage_superbills/v1 API
  slug: open-candid-health-subpackage-superbills-subpackage-superbills-v1-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_tasks.subpackage_tasks/v3 API
  slug: open-candid-health-subpackage-tasks-subpackage-tasks-v3-api
- collection_type: open
  name: API Reference subpackage_auth.subpackage_auth/default subpackage_write-offs.subpackage_write-offs/v1 API
  slug: open-candid-health-subpackage-write-offs-subpackage-write-offs-v1-api
- collection_type: open
  name: Candid Health API
  slug: open-candidhealth
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://candidhealth.com/request-a-demo
- group: other
  href: https://artifacts.apis.io/candid-health/capabilities/candid-health-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/candid-health-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/candid-health/agentic-access/candid-health-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/candid-health-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/candid-health/security/candid-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/candid-health-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/candid-health/authentication/candid-health-authentication.yml
  title: ''
  type: Authentication
  url: authentication/candid-health-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://candidhealth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.joincandidhealth.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/candidhealth
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/candid-health
- group: company
  title: ''
  type: Blog
  url: https://candidhealth.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.joincandidhealth.com
- group: other
  title: ''
  type: X
  url: https://x.com/candid_health
- group: commercial
  href: https://artifacts.apis.io/candid-health/plans/candid-health-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/candid-health-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/candid-health/rate-limits/candid-health-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/candid-health-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/candid-health/finops/candid-health-finops.yml
  title: ''
  type: FinOps
  url: finops/candid-health-finops.yml
- group: docs
  href: https://artifacts.apis.io/candid-health/openapi/_original/candid-health-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/candid-health-openapi.yml
- group: design
  href: https://artifacts.apis.io/candid-health/vocabulary/candid-health-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/candid-health-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/candid-health/json-ld/candid-health-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/candid-health-context.jsonld
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/candidhealth
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/candidhealth
- group: company
  title: ''
  type: Website
  url: https://www.joincandidhealth.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.joincandidhealth.com
- group: build
  href: https://artifacts.apis.io/candid-health/packages/candid-health-packages.yml
  title: ''
  type: Packages
  url: packages/candid-health-packages.yml
- group: build
  href: https://artifacts.apis.io/candid-health/packages/candid-health-packages.yml
  title: ''
  type: SDKs
  url: packages/candid-health-packages.yml
- group: agent
  href: https://artifacts.apis.io/candid-health/well-known/candid-health-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/candid-health-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://docs.joincandidhealth.com/.well-known/api-catalog
- group: agent
  href: https://artifacts.apis.io/candid-health/mcp/candid-health-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/candid-health-mcp.yml
- group: build
  href: https://artifacts.apis.io/candid-health/mcp/candid-health-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/candid-health-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/candid-health/llms/candid-health-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/candid-health-llms.txt
- group: other
  href: https://artifacts.apis.io/candid-health/overlays/candid-health-original-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/candid-health-original-overlay.yaml
- group: design
  href: https://artifacts.apis.io/candid-health/conformance/candid-health-conformance.yml
  title: ''
  type: Conformance
  url: conformance/candid-health-conformance.yml
- group: auth
  href: https://artifacts.apis.io/candid-health/conformance/candid-health-conformance.yml
  title: ''
  type: Compliance
  url: conformance/candid-health-conformance.yml
- group: auth
  href: https://artifacts.apis.io/candid-health/security/candid-health-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/candid-health-trust-center.yml
- group: design
  href: https://artifacts.apis.io/candid-health/errors/candid-health-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/candid-health-problem-types.yml
- group: design
  href: https://artifacts.apis.io/candid-health/lifecycle/candid-health-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/candid-health-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.joincandidhealth.com/api-principles/breaking-changes
- group: design
  href: https://artifacts.apis.io/candid-health/conventions/candid-health-conventions.yml
  title: ''
  type: Conventions
  url: conventions/candid-health-conventions.yml
- group: design
  href: https://artifacts.apis.io/candid-health/data-model/candid-health-data-model.yml
  title: ''
  type: DataModel
  url: data-model/candid-health-data-model.yml
- group: start
  href: https://artifacts.apis.io/candid-health/sandbox/candid-health-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/candid-health-sandbox.yml
- group: design
  href: https://artifacts.apis.io/candid-health/components/candid-health-components.yml
  title: ''
  type: Components
  url: components/candid-health-components.yml
- group: agent
  href: https://artifacts.apis.io/candid-health/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/candid-health/examples/candid-health-encounter-create-example.json
  title: ''
  type: Examples
  url: examples/candid-health-encounter-create-example.json
- group: docs
  href: https://artifacts.apis.io/candid-health/json-schema/candid-health-encounter-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/candid-health-encounter-schema.json
- group: design
  href: https://artifacts.apis.io/candid-health/rules/candid-health-jsonschema-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/candid-health-jsonschema-spectral-rules.yml
- group: start
  title: ''
  type: Portal
  url: https://docs.joincandidhealth.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.joincandidhealth.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.joincandidhealth.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.joincandidhealth.com/introduction/getting-started
- group: operate
  title: ''
  type: Support
  url: https://docs.joincandidhealth.com/additional-resources/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.joincandidhealth.com/hc/en-us
- group: start
  title: ''
  type: Login
  url: https://app.joincandidhealth.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://candidhealth.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://candidhealth.com/privacy-policy
created: 2026-06-12
description: Candid Health is a medical billing automation platform providing REST APIs for submitting claims, checking real-time eligibility, managing encounters, processing remittances, handling prior authorizations, patient collections, credentialing, and full revenue cycle management for healthcare providers.
examples:
- key_count: 3
  name: Candid Health Auth Token Request Example
  slug: candid-health-auth-token-request-example
- key_count: 3
  name: Candid Health Auth Token Response Example
  slug: candid-health-auth-token-response-example
- key_count: 4
  name: Candid Health Eligibility Request Example
  slug: candid-health-eligibility-request-example
- key_count: 10
  name: Candid Health Encounter Create Example
  slug: candid-health-encounter-create-example
finops:
- has_sources: true
  method: derived
  name: Candid Health Finops
  primary_unit: ''
  service_category: ''
  slug: candid-health-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/candid-health.png
json_schemas:
- name: Claim
  property_count: 8
  slug: candid-health-claim
- name: Coverage
  property_count: 18
  slug: candid-health-coverage
- name: EligibilityCheck
  property_count: 6
  slug: candid-health-eligibilitycheck
- name: EligibilityRequest
  property_count: 10
  slug: candid-health-eligibilityrequest
- name: EligibilityResponse
  property_count: 0
  slug: candid-health-eligibilityresponse
- name: Encounter
  property_count: 2
  slug: candid-health-encounter
- name: Patient
  property_count: 52
  slug: candid-health-patient
jsonld:
- class_count: 0
  name: Candid Health Context
  property_count: 51
  slug: candid-health-context
layout: provider
mcp_servers:
- description: 'Candid Health advertises a remote MCP server in its llms.txt and on every documentation page footer. It is live, anonymous and answers tools/list. It is a DOCUMENTATION server, not an API server: the '
  name: Candid Health Documentation MCP Server
  slug: fern-docs-mcp-server
modified: 2026-08-15
name: Candid Health
nav: Providers
network: true
overview: 'Candid Health publishes 53 API contracts indexed on the [APIs.io](https://apis.io/) network, including Exports API, Patients API, Default API, and 50 more. Tagged areas include Medical Billing, Revenue Cycle Management, Healthcare, Claims, and Eligibility.


  The Candid Health catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Candid Health''s developer surface includes pricing, authentication, documentation, GitHub presence, engineering blog, sandbox, code examples, and 46 more developer resources.'
plans:
- name: Candid Health Plans Pricing
  plan_count: 1
  slug: candid-health-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Candid Health Rate Limits
  slug: candid-health-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Candid Health — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: candid-health-jsonschema-spectral-rules
score:
  band: strong
  composite: 65.7
  coverage:
    artifact_dirs: 33
    catalog_earned: 68.8
    catalog_earned_first_party: 16.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.5
  facets:
    access_clarity: 69.7
    contract_governance: 23.5
    contract_quality: 59.2
    developer_ergonomics: 74.4
    discoverability: 85.0
    operational_transparency: 47.4
  previous_composite: 66.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 45.6
      total: 103
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 26.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 38.9
screenshot: https://apis.io/screenshots/candid-health/candid-health-2026-07-25T204340.png
security:
- kind: authentication
  name: Candid Health Authentication
  slug: candid-health-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Candid Health Domain Security
  slug: candid-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Candid Health Trust Center
  slug: candid-health-trust-center
  summary_line: SOC 2 Type 2, SOC 2 Type 1, SOC 1 Type 1, HIPAA (Business Associate)
skill_count: 5
skills:
- name: Authenticate with Candid Health
  slug: candid-health-authenticate
- name: Capture charges in Candid Health
  slug: candid-health-charge-capture
- name: Check patient eligibility with Candid Health
  slug: candid-health-check-eligibility
- name: Track claim status and reconcile remittance in Candid Health
  slug: candid-health-reconcile-remittance
- name: Submit an encounter (claim) to Candid Health
  slug: candid-health-submit-encounter
slug: candid-health
tags:
- Medical Billing
- Revenue Cycle Management
- Healthcare
- Claims
- Eligibility
- Prior Authorization
- Patient Collections
- Credentialing
- Insurance
website: https://candidhealth.com/
---

---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 136
  human_in_the_loop: 0
  name: Candid Health Agentic Access
  operation_count: 238
  slug: candid-health-agentic-access
  summary_line: 238 operations · 136 acting
api_count: 54
apis:
- description: Manage patient invoicing, payments, refunds, and accounts receivable. Automates patient billing workflows and tracks outstanding balances.
  name: Candid Health Patient Collections API
  slug: candid-health-patient-collections-api
- description: Create and manage charge capture claims and bundles for batch claim processing. Enables claim creation from clinical encounters.
  name: Candid Health Charge Capture API
  slug: candid-health-charge-capture-api
- description: Download CSV exports of claim status changes, financial data, and reporting information for revenue cycle analytics and reconciliation.
  name: Candid Health Exports API
  slug: candid-health-exports-api
- description: Core patient management and search capabilities including coverages, appointments, images, notes, lists, and tagging for pre-encounter workflows.
  name: Candid Health Patients API
  slug: candid-health-patients-api
- description: Manage provider and facility credentialing spans, organization providers, service facilities, contracts, payers, and fee schedules.
  name: Candid Health Credentialing API
  slug: candid-health-credentialing-api
- description: OAuth 2.0 client credentials token generation for authenticating API access to all Candid Health REST endpoints.
  name: Candid Health Auth API
  slug: candid-health-auth-api
- description: The subpackage_auth.subpackage_auth/default API from Candid Health — 1 operation(s) for subpackage_auth.subpackage_auth/default.
  name: Candid Health subpackage_auth.subpackage_auth/default API
  slug: candid-health-subpackage-auth-subpackage-auth-default-api
- description: The subpackage_billing-notes.subpackage_billing-notes/v2 API from Candid Health — 2 operation(s) for subpackage_billing-notes.subpackage_billing-notes/v2.
  name: Candid Health subpackage_billing-notes.subpackage_billing-notes/v2 API
  slug: candid-health-subpackage-billing-notes-subpackage-billing-notes-v2-api
- description: The subpackage_charge-capture-bundles.subpackage_charge-capture-bundles/v1 API from Candid Health — 4 operation(s) for subpackage_charge-capture-bundles.subpackage_charge-capture-bundles/v1.
  name: Candid Health subpackage_charge-capture-bundles.subpackage_charge-capture-bundles/v1 API
  slug: candid-health-subpackage-charge-capture-bundles-subpackage-charge-capture-bundles-v1-api
- description: The subpackage_charge-capture.subpackage_charge-capture/v1 API from Candid Health — 5 operation(s) for subpackage_charge-capture.subpackage_charge-capture/v1.
  name: Candid Health subpackage_charge-capture.subpackage_charge-capture/v1 API
  slug: candid-health-subpackage-charge-capture-subpackage-charge-capture-v1-api
- description: The subpackage_contracts.subpackage_contracts/v2 API from Candid Health — 2 operation(s) for subpackage_contracts.subpackage_contracts/v2.
  name: Candid Health subpackage_contracts.subpackage_contracts/v2 API
  slug: candid-health-subpackage-contracts-subpackage-contracts-v2-api
- description: The subpackage_contracts.subpackage_contracts/v3 API from Candid Health — 6 operation(s) for subpackage_contracts.subpackage_contracts/v3.
  name: Candid Health subpackage_contracts.subpackage_contracts/v3 API
  slug: candid-health-subpackage-contracts-subpackage-contracts-v3-api
- description: The subpackage_credentialing.subpackage_credentialing/v2 API from Candid Health — 4 operation(s) for subpackage_credentialing.subpackage_credentialing/v2.
  name: Candid Health subpackage_credentialing.subpackage_credentialing/v2 API
  slug: candid-health-subpackage-credentialing-subpackage-credentialing-v2-api
- description: The subpackage_custom-schemas.subpackage_custom-schemas/v1 API from Candid Health — 2 operation(s) for subpackage_custom-schemas.subpackage_custom-schemas/v1.
  name: Candid Health subpackage_custom-schemas.subpackage_custom-schemas/v1 API
  slug: candid-health-subpackage-custom-schemas-subpackage-custom-schemas-v1-api
- description: The subpackage_diagnoses API from Candid Health — 2 operation(s) for subpackage_diagnoses.
  name: Candid Health subpackage_diagnoses API
  slug: candid-health-subpackage-diagnoses-api
- description: The subpackage_eligibility.subpackage_eligibility/v2 API from Candid Health — 1 operation(s) for subpackage_eligibility.subpackage_eligibility/v2.
  name: Candid Health subpackage_eligibility.subpackage_eligibility/v2 API
  slug: candid-health-subpackage-eligibility-subpackage-eligibility-v2-api
- description: The subpackage_encounter-attachments.subpackage_encounter-attachments/v1 API from Candid Health — 4 operation(s) for subpackage_encounter-attachments.subpackage_encounter-attachments/v1.
  name: Candid Health subpackage_encounter-attachments.subpackage_encounter-attachments/v1 API
  slug: candid-health-subpackage-encounter-attachments-subpackage-encounter-attachments-v1-api
- description: The subpackage_encounter-providers.subpackage_encounter-providers/v2 API from Candid Health — 9 operation(s) for subpackage_encounter-providers.subpackage_encounter-providers/v2.
  name: Candid Health subpackage_encounter-providers.subpackage_encounter-providers/v2 API
  slug: candid-health-subpackage-encounter-providers-subpackage-encounter-providers-v2-api
- description: The subpackage_encounter-supplemental-information.subpackage_encounter-supplemental-information/v1 API from Candid Health — 2 operation(s) for subpackage_encounter-supplemental-information.subpackage_
  name: Candid Health subpackage_encounter-supplemental-information.subpackage_encounter-supplemental-information/v1 API
  slug: candid-health-subpackage-encounter-supplemental-information-subpackage-encounter-supplemental-information-v1-api
- description: The subpackage_encounters.subpackage_encounters/v4 API from Candid Health — 6 operation(s) for subpackage_encounters.subpackage_encounters/v4.
  name: Candid Health subpackage_encounters.subpackage_encounters/v4 API
  slug: candid-health-subpackage-encounters-subpackage-encounters-v4-api
- description: The subpackage_events.subpackage_events/v1 API from Candid Health — 2 operation(s) for subpackage_events.subpackage_events/v1.
  name: Candid Health subpackage_events.subpackage_events/v1 API
  slug: candid-health-subpackage-events-subpackage-events-v1-api
- description: The subpackage_exports.subpackage_exports/v3 API from Candid Health — 1 operation(s) for subpackage_exports.subpackage_exports/v3.
  name: Candid Health subpackage_exports.subpackage_exports/v3 API
  slug: candid-health-subpackage-exports-subpackage-exports-v3-api
- description: The subpackage_external-payment-account-config.subpackage_external-payment-account-config/v1 API from Candid Health — 1 operation(s) for subpackage_external-payment-account-config.subpackage_external-
  name: Candid Health subpackage_external-payment-account-config.subpackage_external-payment-account-config/v1 API
  slug: candid-health-subpackage-external-payment-account-config-subpackage-external-payment-account-config-v1-api
- description: The subpackage_fee-schedules.subpackage_fee-schedules/v3 API from Candid Health — 11 operation(s) for subpackage_fee-schedules.subpackage_fee-schedules/v3.
  name: Candid Health subpackage_fee-schedules.subpackage_fee-schedules/v3 API
  slug: candid-health-subpackage-fee-schedules-subpackage-fee-schedules-v3-api
- description: The subpackage_guarantor.subpackage_guarantor/v1 API from Candid Health — 2 operation(s) for subpackage_guarantor.subpackage_guarantor/v1.
  name: Candid Health subpackage_guarantor.subpackage_guarantor/v1 API
  slug: candid-health-subpackage-guarantor-subpackage-guarantor-v1-api
- description: The subpackage_health-care-code-information.subpackage_health-care-code-information/v1 API from Candid Health — 1 operation(s) for subpackage_health-care-code-information.subpackage_health-care-code-i
  name: Candid Health subpackage_health-care-code-information.subpackage_health-care-code-information/v1 API
  slug: candid-health-subpackage-health-care-code-information-subpackage-health-care-code-information-v1-api
- description: The subpackage_import-invoice.subpackage_import-invoice/v1 API from Candid Health — 2 operation(s) for subpackage_import-invoice.subpackage_import-invoice/v1.
  name: Candid Health subpackage_import-invoice.subpackage_import-invoice/v1 API
  slug: candid-health-subpackage-import-invoice-subpackage-import-invoice-v1-api
- description: The subpackage_insurance-adjudications.subpackage_insurance-adjudications/v1 API from Candid Health — 1 operation(s) for subpackage_insurance-adjudications.subpackage_insurance-adjudications/v1.
  name: Candid Health subpackage_insurance-adjudications.subpackage_insurance-adjudications/v1 API
  slug: candid-health-subpackage-insurance-adjudications-subpackage-insurance-adjudications-v1-api
- description: The subpackage_insurance-refunds.subpackage_insurance-refunds/v1 API from Candid Health — 2 operation(s) for subpackage_insurance-refunds.subpackage_insurance-refunds/v1.
  name: Candid Health subpackage_insurance-refunds.subpackage_insurance-refunds/v1 API
  slug: candid-health-subpackage-insurance-refunds-subpackage-insurance-refunds-v1-api
- description: The subpackage_medication-dispense.subpackage_medication-dispense/v1 API from Candid Health — 1 operation(s) for subpackage_medication-dispense.subpackage_medication-dispense/v1.
  name: Candid Health subpackage_medication-dispense.subpackage_medication-dispense/v1 API
  slug: candid-health-subpackage-medication-dispense-subpackage-medication-dispense-v1-api
- description: The subpackage_non-insurance-payer-payments.subpackage_non-insurance-payer-payments/v1 API from Candid Health — 2 operation(s) for subpackage_non-insurance-payer-payments.subpackage_non-insurance-paye
  name: Candid Health subpackage_non-insurance-payer-payments.subpackage_non-insurance-payer-payments/v1 API
  slug: candid-health-subpackage-non-insurance-payer-payments-subpackage-non-insurance-payer-payments-v1-api
- description: The subpackage_non-insurance-payer-refunds.subpackage_non-insurance-payer-refunds/v1 API from Candid Health — 2 operation(s) for subpackage_non-insurance-payer-refunds.subpackage_non-insurance-payer-r
  name: Candid Health subpackage_non-insurance-payer-refunds.subpackage_non-insurance-payer-refunds/v1 API
  slug: candid-health-subpackage-non-insurance-payer-refunds-subpackage-non-insurance-payer-refunds-v1-api
- description: The subpackage_non-insurance-payers.subpackage_non-insurance-payers/v1 API from Candid Health — 4 operation(s) for subpackage_non-insurance-payers.subpackage_non-insurance-payers/v1.
  name: Candid Health subpackage_non-insurance-payers.subpackage_non-insurance-payers/v1 API
  slug: candid-health-subpackage-non-insurance-payers-subpackage-non-insurance-payers-v1-api
- description: The subpackage_organization-providers.subpackage_organization-providers/v3 API from Candid Health — 2 operation(s) for subpackage_organization-providers.subpackage_organization-providers/v3.
  name: Candid Health subpackage_organization-providers.subpackage_organization-providers/v3 API
  slug: candid-health-subpackage-organization-providers-subpackage-organization-providers-v3-api
- description: The subpackage_organization-service-facilities.subpackage_organization-service-facilities/v2 API from Candid Health — 3 operation(s) for subpackage_organization-service-facilities.subpackage_organizat
  name: Candid Health subpackage_organization-service-facilities.subpackage_organization-service-facilities/v2 API
  slug: candid-health-subpackage-organization-service-facilities-subpackage-organization-service-facilities-v2-api
- description: The subpackage_patient-ar.subpackage_patient-ar/v1 API from Candid Health — 2 operation(s) for subpackage_patient-ar.subpackage_patient-ar/v1.
  name: Candid Health subpackage_patient-ar.subpackage_patient-ar/v1 API
  slug: candid-health-subpackage-patient-ar-subpackage-patient-ar-v1-api
- description: The subpackage_patient-payments.subpackage_patient-payments/v4 API from Candid Health — 2 operation(s) for subpackage_patient-payments.subpackage_patient-payments/v4.
  name: Candid Health subpackage_patient-payments.subpackage_patient-payments/v4 API
  slug: candid-health-subpackage-patient-payments-subpackage-patient-payments-v4-api
- description: The subpackage_patient-refunds.subpackage_patient-refunds/v1 API from Candid Health — 2 operation(s) for subpackage_patient-refunds.subpackage_patient-refunds/v1.
  name: Candid Health subpackage_patient-refunds.subpackage_patient-refunds/v1 API
  slug: candid-health-subpackage-patient-refunds-subpackage-patient-refunds-v1-api
- description: The subpackage_payer-plan-groups.subpackage_payer-plan-groups/v1 API from Candid Health — 2 operation(s) for subpackage_payer-plan-groups.subpackage_payer-plan-groups/v1.
  name: Candid Health subpackage_payer-plan-groups.subpackage_payer-plan-groups/v1 API
  slug: candid-health-subpackage-payer-plan-groups-subpackage-payer-plan-groups-v1-api
- description: The subpackage_payers.subpackage_payers/v3 API from Candid Health — 2 operation(s) for subpackage_payers.subpackage_payers/v3.
  name: Candid Health subpackage_payers.subpackage_payers/v3 API
  slug: candid-health-subpackage-payers-subpackage-payers-v3-api
- description: The subpackage_payers.subpackage_payers/v4 API from Candid Health — 2 operation(s) for subpackage_payers.subpackage_payers/v4.
  name: Candid Health subpackage_payers.subpackage_payers/v4 API
  slug: candid-health-subpackage-payers-subpackage-payers-v4-api
- description: The subpackage_pre-encounter.subpackage_pre-encounter/appointments.subpackage_pre-encounter/appointments/v1 API from Candid Health — 6 operation(s) for subpackage_pre-encounter.subpackage_pre-encounte
  name: Candid Health subpackage_pre-encounter.subpackage_pre-encounter/appointments.subpackage_pre-encounter/appointments/v1 API
  slug: candid-health-subpackage-pre-encounter-subpackage-pre-encounter-appointments-subpackage-pre-encounter-appointments-v1-api
- description: The subpackage_pre-encounter.subpackage_pre-encounter/coverages.subpackage_pre-encounter/coverages/v1 API from Candid Health — 9 operation(s) for subpackage_pre-encounter.subpackage_pre-encounter/cove
  name: Candid Health subpackage_pre-encounter.subpackage_pre-encounter/coverages.subpackage_pre-encounter/coverages/v1 API
  slug: candid-health-subpackage-pre-encounter-subpackage-pre-encounter-coverages-subpackage-pre-encounter-coverages-v1-api
- description: The subpackage_pre-encounter.subpackage_pre-encounter/eligibilityChecks.subpackage_pre-encounter/eligibilityChecks/v1 API from Candid Health — 7 operation(s) for subpackage_pre-encounter.subpackage_pr
  name: Candid Health subpackage_pre-encounter.subpackage_pre-encounter/eligibilityChecks.subpackage_pre-encounter/eligibilityChecks/v1 API
  slug: candid-health-subpackage-pre-encounter-subpackage-pre-encounter-eligibilitychecks-subpackage-pre-encounter-eligibilitychecks-v1-api
- description: The subpackage_pre-encounter.subpackage_pre-encounter/images.subpackage_pre-encounter/images/v1 API from Candid Health — 3 operation(s) for subpackage_pre-encounter.subpackage_pre-encounter/images.sub
  name: Candid Health subpackage_pre-encounter.subpackage_pre-encounter/images.subpackage_pre-encounter/images/v1 API
  slug: candid-health-subpackage-pre-encounter-subpackage-pre-encounter-images-subpackage-pre-encounter-images-v1-api
- description: The subpackage_pre-encounter.subpackage_pre-encounter/lists.subpackage_pre-encounter/lists/v1 API from Candid Health — 2 operation(s) for subpackage_pre-encounter.subpackage_pre-encounter/lists.subpac
  name: Candid Health subpackage_pre-encounter.subpackage_pre-encounter/lists.subpackage_pre-encounter/lists/v1 API
  slug: candid-health-subpackage-pre-encounter-subpackage-pre-encounter-lists-subpackage-pre-encounter-lists-v1-api
- description: The subpackage_pre-encounter.subpackage_pre-encounter/notes.subpackage_pre-encounter/notes/v1 API from Candid Health — 3 operation(s) for subpackage_pre-encounter.subpackage_pre-encounter/notes.subpac
  name: Candid Health subpackage_pre-encounter.subpackage_pre-encounter/notes.subpackage_pre-encounter/notes/v1 API
  slug: candid-health-subpackage-pre-encounter-subpackage-pre-encounter-notes-subpackage-pre-encounter-notes-v1-api
- description: The subpackage_pre-encounter.subpackage_pre-encounter/organizationExternalProviders.subpackage_pre-encounter/organizationExternalProviders/v1 API from Candid Health — 4 operation(s) for subpackage_pre
  name: Candid Health subpackage_pre-encounter.subpackage_pre-encounter/organizationExternalProviders.subpackage_pre-encounter/organizationExternalProviders/v1 API
  slug: candid-health-subpackage-pre-encounter-subpackage-pre-encounter-organizationexternalproviders-subpackage-pre-encounter-organizationexternalproviders-v1-api
- description: The subpackage_pre-encounter.subpackage_pre-encounter/patients.subpackage_pre-encounter/patients/v1 API from Candid Health — 10 operation(s) for subpackage_pre-encounter.subpackage_pre-encounter/patie
  name: Candid Health subpackage_pre-encounter.subpackage_pre-encounter/patients.subpackage_pre-encounter/patients/v1 API
  slug: candid-health-subpackage-pre-encounter-subpackage-pre-encounter-patients-subpackage-pre-encounter-patients-v1-api
- description: The subpackage_pre-encounter.subpackage_pre-encounter/tags.subpackage_pre-encounter/tags/v1 API from Candid Health — 3 operation(s) for subpackage_pre-encounter.subpackage_pre-encounter/tags.subpackag
  name: Candid Health subpackage_pre-encounter.subpackage_pre-encounter/tags.subpackage_pre-encounter/tags/v1 API
  slug: candid-health-subpackage-pre-encounter-subpackage-pre-encounter-tags-subpackage-pre-encounter-tags-v1-api
- description: The subpackage_service-lines.subpackage_service-lines/v2 API from Candid Health — 4 operation(s) for subpackage_service-lines.subpackage_service-lines/v2.
  name: Candid Health subpackage_service-lines.subpackage_service-lines/v2 API
  slug: candid-health-subpackage-service-lines-subpackage-service-lines-v2-api
- description: The subpackage_superbills.subpackage_superbills/v1 API from Candid Health — 1 operation(s) for subpackage_superbills.subpackage_superbills/v1.
  name: Candid Health subpackage_superbills.subpackage_superbills/v1 API
  slug: candid-health-subpackage-superbills-subpackage-superbills-v1-api
- description: The subpackage_tasks.subpackage_tasks/v3 API from Candid Health — 3 operation(s) for subpackage_tasks.subpackage_tasks/v3.
  name: Candid Health subpackage_tasks.subpackage_tasks/v3 API
  slug: candid-health-subpackage-tasks-subpackage-tasks-v3-api
- description: The subpackage_write-offs.subpackage_write-offs/v1 API from Candid Health — 5 operation(s) for subpackage_write-offs.subpackage_write-offs/v1.
  name: Candid Health subpackage_write-offs.subpackage_write-offs/v1 API
  slug: candid-health-subpackage-write-offs-subpackage-write-offs-v1-api
artifact_total: 73
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/candid-health-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/candid-health-domain-security.yml
- group: auth
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
- group: commercial
  title: ''
  type: Pricing
  url: https://candidhealth.com/integrations
- group: operate
  title: ''
  type: StatusPage
  url: https://status.joincandidhealth.com
- group: other
  title: ''
  type: X
  url: https://x.com/candid_health
- group: commercial
  title: ''
  type: Plans
  url: plans/candid-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/candid-health-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/candid-health-finops.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/candid-health-openapi.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/candid-health-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/candid-health-context.jsonld
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
- name: Candid Health Finops
  service_category: ''
  slug: candid-health-finops
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
modified: 2026-06-12
name: Candid Health
nav: Providers
network: true
overview: 'Candid Health publishes 48 APIs on the [APIs.io](https://apis.io/) network, including subpackage_auth.subpackage_auth/default API, subpackage_billing-notes.subpackage_billing-notes/v2 API, subpackage_charge-capture-bundles.subpackage_charge-capture-bundles/v1 API, and 45 more. Tagged areas include Medical Billing, Revenue Cycle Management, Healthcare, Claims, and Eligibility.


  The Candid Health catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Candid Health''s developer surface includes authentication, documentation, GitHub presence, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Candid Health Plans Pricing
  plan_count: 1
  slug: candid-health-plans-pricing
random_paper: 86
rate_limits:
- limit_count: 2
  name: Candid Health Rate Limits
  slug: candid-health-rate-limits
rules:
- name: Candid Health API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: candid-health-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.4
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 42.1
  previous_composite: 44.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 48
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 25.8
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/candid-health/refs/heads/main/screenshots/candid-health-2026-06-20T173925.png
security:
- kind: authentication
  name: Candid Health Authentication
  slug: candid-health-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Candid Health Domain Security
  slug: candid-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: candid-health
tags:
- Medical Billing
- Revenue Cycle Management
- Healthcare
- Claims
- Eligibility
- Prior Authorization
- Remittance
- Patient Collections
- Credentialing
- Insurance
website: https://candidhealth.com/
---

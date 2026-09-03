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
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 39.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 136
  human_in_the_loop: 0
  name: Candid Health Agentic Access
  operation_count: 238
  slug: candid-health-agentic-access
  summary_line: 238 operations · 136 acting
api_count: 1
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
  description: The v1 API from Candid Health — 105 operation(s) for v1.
  name: Candid Health V1 API
  slug: candid-health-v1-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The v2 API from Candid Health — 25 operation(s) for v2.
  name: Candid Health V2 API
  slug: candid-health-v2-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The v3 API from Candid Health — 28 operation(s) for v3.
  name: Candid Health V3 API
  slug: candid-health-v3-api
- baseURL: https://api.joincandidhealth.com
  baseurl_source: declared
  description: The v4 API from Candid Health — 10 operation(s) for v4.
  name: Candid Health V4 API
  slug: candid-health-v4-api
artifact_total: 91
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/candid-health-capability-edges.yml
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
  title: ''
  type: Packages
  url: packages/candid-health-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/candid-health-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/candid-health-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://docs.joincandidhealth.com/.well-known/api-catalog
- group: agent
  title: ''
  type: MCPServer
  url: mcp/candid-health-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/candid-health-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/candid-health-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/candid-health-original-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/candid-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/candid-health-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/candid-health-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/candid-health-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/candid-health-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.joincandidhealth.com/api-principles/breaking-changes
- group: design
  title: ''
  type: Conventions
  url: conventions/candid-health-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/candid-health-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/candid-health-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/candid-health-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/candid-health-encounter-create-example.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/candid-health-encounter-schema.json
- group: design
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
mcp_servers:
- description: 'Candid Health advertises a remote MCP server in its llms.txt and on every documentation page footer. It is live, anonymous and answers tools/list. It is a DOCUMENTATION server, not an API server: the '
  name: Candid Health Documentation MCP Server
  slug: candid-health-documentation-mcp-server
modified: 2026-08-15
name: Candid Health
nav: Providers
network: true
overview: 'Candid Health publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Default API, Diagnoses API, V1 API, and 3 more. Tagged areas include Medical Billing, Revenue Cycle Management, Healthcare, Claims, and Eligibility.


  The Candid Health catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Candid Health''s developer surface includes authentication, documentation, GitHub presence, engineering blog, sandbox, code examples, developer portal, and 45 more developer resources.'
plans:
- name: Candid Health Plans Pricing
  plan_count: 1
  slug: candid-health-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: Candid Health Rate Limits
  slug: candid-health-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Candid Health API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: candid-health-jsonschema-spectral-rules
score:
  band: strong
  composite: 65.6
  coverage:
    artifact_dirs: 29
    catalog_gap: 42.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 72.4
    commercial_clarity: 72.4
    contract_governance: 25.0
    contract_quality: 59.8
    developer_ergonomics: 78.0
    discoverability: 87.0
    governance: 25.0
    operational_transparency: 47.4
  previous_composite: 65.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 62
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/candid-health/refs/heads/main/screenshots/candid-health-2026-07-25T204340.png
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

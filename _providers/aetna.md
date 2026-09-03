---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - finops
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Aetna Agentic Access
  operation_count: 99
  slug: aetna-agentic-access
  summary_line: 99 operations
api_count: 95
apis:
- baseURL: https://apif1.aetna.com/fhir
  baseurl_source: declared
  description: HL7 FHIR R4 Patient Access API giving Aetna members, through an app they authorize, access to their adjudicated claims, encounter data, coverage, clinical records and formulary information. Implements
  name: Aetna Patient Access FHIR API
  slug: aetna-patient-access-fhir-api
- baseURL: https://apif1.aetna.com/fhir
  baseurl_source: declared
  description: HL7 FHIR R4 Provider Directory API implementing the Da Vinci PDex Plan Net Implementation Guide (upgraded to version 1.2.0 on 2026-06-23), covering both Medicare and Commercial networks. Exposes Pract
  name: Aetna Provider Directory FHIR API
  slug: aetna-provider-directory-fhir-api
- baseURL: https://apif1.aetna.com/fhir
  baseurl_source: declared
  description: Da Vinci PDex US Drug Formulary 2.0.0 STU 2 formulary data, delivered as part of the Patient Access API product rather than as a separate base URL. MedicationKnowledge carries covered drugs, tiers, co
  name: Aetna Drug Formulary FHIR API
  slug: aetna-drug-formulary-fhir-api
- description: 'Da Vinci prior-authorization surface built for CMS-0057-F: Coverage Requirements Discovery (STU 2.1) at /coveragerequirementsdiscovery/v1/cds-services/{id} supporting the order-sign, order-dispatch an'
  name: Aetna Prior Authorization FHIR API
  slug: aetna-prior-authorization-fhir-api
- description: Launched in Production on 2026-03-27 under the public-provider-group-fhir product, the Provider Access API lets provider organizations and EHR vendors identify their attributed member groups and reque
  name: Aetna Provider Access FHIR API
  slug: aetna-provider-access-fhir-api
- description: Consumer Real-Time Pharmacy Benefit Check 1.0.0, launched 2024-12-05, letting members and EHR systems retrieve prescription drug cost and coverage information at the point of prescribing. Built to sat
  name: Aetna Realtime Pharmacy Benefit Check API
  slug: aetna-realtime-pharmacy-benefit-check-api
- description: HIPAA X12 electronic data interchange for health care professionals - EDI 837 claims, 270/271 eligibility and benefits, 276/277 claim status and 835 remittance advice. This is not an Aetna-hosted REST
  name: Aetna Provider EDI Connectivity
  slug: aetna-provider-edi-api
artifact_total: 128
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/aetna-patient-access-api-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/aetna-provider-directory-api-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/aetna-patient-access-api-overlay.yaml
- group: other
  title: ''
  type: CapabilityStatement
  url: fhir/aetna-patient-access-capability-statement.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/aetna-vocabulary.yaml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/aetna-allergyintolerance.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/aetna-bundle.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/aetna-careplan.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/aetna-careteam.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/aetna-condition.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/aetna-device.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/aetna-diagnosticreport.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/aetna-documentreference.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/aetna-encounter.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/aetna-explanationofbenefit.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/aetna-goal.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/aetna-healthcareservice.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/aetna-immunization.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/aetna-insuranceplan.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/aetna-location.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/aetna-medicationknowledge.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/aetna-medicationrequest.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/aetna-observation.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/aetna-operationoutcome.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/aetna-organization.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/aetna-organizationaffiliation.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/aetna-patient.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/aetna-practitioner.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/aetna-practitionerrole.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/aetna-procedure.json
- group: build
  title: ''
  type: Examples
  url: examples/aetna-v1-providerdirectory-insuranceplan-200-example.json
- group: build
  title: ''
  type: Examples
  url: examples/aetna-v1-providerdirectory-location-200-example.json
- group: build
  title: ''
  type: Examples
  url: examples/aetna-v1-providerdirectory-location-id-200-example.json
- group: build
  title: ''
  type: Examples
  url: examples/aetna-v1-providerdirectory-organization-200-example.json
- group: build
  title: ''
  type: Examples
  url: examples/aetna-v1-providerdirectory-organization-id-200-example.json
- group: build
  title: ''
  type: Examples
  url: examples/aetna-v1-providerdirectory-organizationaffiliation-200-example.json
- group: build
  title: ''
  type: Examples
  url: examples/aetna-v1-providerdirectory-practitioner-200-example.json
- group: build
  title: ''
  type: Examples
  url: examples/aetna-v1-providerdirectory-practitioner-id-200-example.json
- group: build
  title: ''
  type: Examples
  url: examples/aetna-v1-providerdirectory-practitionerrole-200-example.json
- group: build
  title: ''
  type: Examples
  url: examples/aetna-v1-providerdirectorydata-healthcareservice-200-example.json
- group: build
  title: ''
  type: Examples
  url: examples/aetna-v1-providerdirectorydata-healthcareservice-id-200-example.json
- group: build
  title: ''
  type: Examples
  url: examples/aetna-v1-providerdirectorydata-insuranceplan-200-example.json
- group: build
  title: ''
  type: Examples
  url: examples/aetna-v1-providerdirectorydata-location-200-example.json
- group: build
  title: ''
  type: Examples
  url: examples/aetna-v1-providerdirectorydata-location-id-200-example.json
- group: build
  title: ''
  type: Examples
  url: examples/aetna-v1-providerdirectorydata-organization-200-example.json
- group: build
  title: ''
  type: Examples
  url: examples/aetna-v1-providerdirectorydata-organization-id-200-example.json
- group: build
  title: ''
  type: Examples
  url: examples/aetna-v1-providerdirectorydata-organizationaffiliation-200-example.json
- group: build
  title: ''
  type: Examples
  url: examples/aetna-v1-providerdirectorydata-practitioner-200-example.json
- group: build
  title: ''
  type: Examples
  url: examples/aetna-v1-providerdirectorydata-practitioner-id-200-example.json
- group: build
  title: ''
  type: Examples
  url: examples/aetna-v1-providerdirectorydata-practitionerrole-200-example.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/aetna-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/aetna-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aetna-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/aetna-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aetna-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aetna-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aetna-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developerportal.aetna.com/managedcontent/pdfs/Previous_Releases.pdf
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/aetna-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developerportal.aetna.com/managedcontent/pdfs/Previous_Releases.pdf
- group: operate
  title: ''
  type: Roadmap
  url: https://developerportal.aetna.com/managedcontent/pdfs/Upcoming_Releases.pdf
- group: start
  title: ''
  type: Sandbox
  url: sandbox/aetna-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aetna-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aetna-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aetna-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/aetna-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/aetna-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aetna-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aetna-well-known.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aetna-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aetna-domain-security.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/aetna-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developerportal.aetna.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developerportal.aetna.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developerportal.aetna.com/assets/Data/Fhir.json
- group: start
  title: ''
  type: GettingStarted
  url: https://developerportal.aetna.com/gettingstarted/1000
- group: start
  title: ''
  type: SignUp
  url: https://developerportal.aetna.com/
- group: start
  title: ''
  type: Login
  url: https://member.aetna.com
- group: operate
  title: ''
  type: Support
  url: https://www.aetna.com/individuals-families/contact-aetna.html
- group: company
  title: ''
  type: Website
  url: https://www.aetna.com
- group: start
  title: ''
  type: Portal
  url: https://www.aetna.com/health-care-professionals.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aetnahealth
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aetna
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aetna.com/legal-notices/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developerportal.aetna.com/termsofuse
created: '2026-05-04'
description: 'Aetna, a CVS Health company, is one of the largest U.S. health insurers, offering medical, dental, vision, pharmacy and Medicare/Medicaid plans to individuals, families, employers, health care providers and brokers. Its public API surface is entirely regulatory: Aetna operates an Interoperability API Developer Portal at developerportal.aetna.com that publishes HL7 FHIR R4 interfaces mandated by the CMS Interoperability and Patient Access Final Rule (CMS-9115-F) and the Advancing Interoperability and Improving Prior Authorization Final Rule (CMS-0057-F) - Patient Access, Payer to Payer, Provider Directory, Provider Access, Prior Authorization (Da Vinci CRD, PAS and CDex) and Realtime Pharmacy Benefit Check. Aetna publishes a machine-readable catalog of 139 operations and serves a Swagger 2.0 document for each one, plus live FHIR CapabilityStatements and SMART App Launch discovery documents on its production and sandbox FHIR gateways. Everything is read-only, everything requires
  OAuth 2.0 under SMART App Launch, and everything is free - there is no pricing, no plan and no metered product. Provider EDI connectivity is handled separately through the Availity portal.'
examples:
- key_count: 2
  name: Aetna V1 Providerdirectory Insuranceplan 200 Example
  slug: aetna-v1-providerdirectory-insuranceplan-200-example
- key_count: 2
  name: Aetna V1 Providerdirectory Insuranceplan 400 Example
  slug: aetna-v1-providerdirectory-insuranceplan-400-example
- key_count: 2
  name: Aetna V1 Providerdirectory Insuranceplan 500 Example
  slug: aetna-v1-providerdirectory-insuranceplan-500-example
- key_count: 2
  name: Aetna V1 Providerdirectory Location 200 Example
  slug: aetna-v1-providerdirectory-location-200-example
- key_count: 2
  name: Aetna V1 Providerdirectory Location 400 Example
  slug: aetna-v1-providerdirectory-location-400-example
- key_count: 2
  name: Aetna V1 Providerdirectory Location 500 Example
  slug: aetna-v1-providerdirectory-location-500-example
- key_count: 2
  name: Aetna V1 Providerdirectory Location Id 200 Example
  slug: aetna-v1-providerdirectory-location-id-200-example
- key_count: 2
  name: Aetna V1 Providerdirectory Location Id 400 Example
  slug: aetna-v1-providerdirectory-location-id-400-example
- key_count: 2
  name: Aetna V1 Providerdirectory Location Id 404 Example
  slug: aetna-v1-providerdirectory-location-id-404-example
- key_count: 2
  name: Aetna V1 Providerdirectory Location Id 500 Example
  slug: aetna-v1-providerdirectory-location-id-500-example
- key_count: 2
  name: Aetna V1 Providerdirectory Organization 200 Example
  slug: aetna-v1-providerdirectory-organization-200-example
- key_count: 2
  name: Aetna V1 Providerdirectory Organization 400 Example
  slug: aetna-v1-providerdirectory-organization-400-example
- key_count: 2
  name: Aetna V1 Providerdirectory Organization 500 Example
  slug: aetna-v1-providerdirectory-organization-500-example
- key_count: 2
  name: Aetna V1 Providerdirectory Organization Id 200 Example
  slug: aetna-v1-providerdirectory-organization-id-200-example
- key_count: 2
  name: Aetna V1 Providerdirectory Organization Id 203 Example
  slug: aetna-v1-providerdirectory-organization-id-203-example
- key_count: 2
  name: Aetna V1 Providerdirectory Organization Id 400 Example
  slug: aetna-v1-providerdirectory-organization-id-400-example
- key_count: 2
  name: Aetna V1 Providerdirectory Organization Id 404 Example
  slug: aetna-v1-providerdirectory-organization-id-404-example
- key_count: 2
  name: Aetna V1 Providerdirectory Organization Id 500 Example
  slug: aetna-v1-providerdirectory-organization-id-500-example
- key_count: 2
  name: Aetna V1 Providerdirectory Organizationaffiliation 200 Example
  slug: aetna-v1-providerdirectory-organizationaffiliation-200-example
- key_count: 2
  name: Aetna V1 Providerdirectory Organizationaffiliation 400 Example
  slug: aetna-v1-providerdirectory-organizationaffiliation-400-example
- key_count: 2
  name: Aetna V1 Providerdirectory Organizationaffiliation 500 Example
  slug: aetna-v1-providerdirectory-organizationaffiliation-500-example
- key_count: 2
  name: Aetna V1 Providerdirectory Practitioner 200 Example
  slug: aetna-v1-providerdirectory-practitioner-200-example
- key_count: 2
  name: Aetna V1 Providerdirectory Practitioner 400 Example
  slug: aetna-v1-providerdirectory-practitioner-400-example
- key_count: 2
  name: Aetna V1 Providerdirectory Practitioner 500 Example
  slug: aetna-v1-providerdirectory-practitioner-500-example
- key_count: 2
  name: Aetna V1 Providerdirectory Practitioner Id 200 Example
  slug: aetna-v1-providerdirectory-practitioner-id-200-example
- key_count: 2
  name: Aetna V1 Providerdirectory Practitioner Id 203 Example
  slug: aetna-v1-providerdirectory-practitioner-id-203-example
- key_count: 2
  name: Aetna V1 Providerdirectory Practitionerrole 200 Example
  slug: aetna-v1-providerdirectory-practitionerrole-200-example
- key_count: 2
  name: Aetna V1 Providerdirectorydata Healthcareservice 200 Example
  slug: aetna-v1-providerdirectorydata-healthcareservice-200-example
- key_count: 2
  name: Aetna V1 Providerdirectorydata Healthcareservice Id 200 Example
  slug: aetna-v1-providerdirectorydata-healthcareservice-id-200-example
- key_count: 2
  name: Aetna V1 Providerdirectorydata Insuranceplan 200 Example
  slug: aetna-v1-providerdirectorydata-insuranceplan-200-example
- key_count: 2
  name: Aetna V1 Providerdirectorydata Location 200 Example
  slug: aetna-v1-providerdirectorydata-location-200-example
- key_count: 2
  name: Aetna V1 Providerdirectorydata Location Id 200 Example
  slug: aetna-v1-providerdirectorydata-location-id-200-example
- key_count: 2
  name: Aetna V1 Providerdirectorydata Organization 200 Example
  slug: aetna-v1-providerdirectorydata-organization-200-example
- key_count: 2
  name: Aetna V1 Providerdirectorydata Organization Id 200 Example
  slug: aetna-v1-providerdirectorydata-organization-id-200-example
- key_count: 2
  name: Aetna V1 Providerdirectorydata Organizationaffiliation 200 Example
  slug: aetna-v1-providerdirectorydata-organizationaffiliation-200-example
- key_count: 2
  name: Aetna V1 Providerdirectorydata Practitioner 200 Example
  slug: aetna-v1-providerdirectorydata-practitioner-200-example
- key_count: 2
  name: Aetna V1 Providerdirectorydata Practitioner Id 200 Example
  slug: aetna-v1-providerdirectorydata-practitioner-id-200-example
- key_count: 2
  name: Aetna V1 Providerdirectorydata Practitionerrole 200 Example
  slug: aetna-v1-providerdirectorydata-practitionerrole-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Allergyintolerance 200 Example
  slug: aetna-v2-patientaccess-allergyintolerance-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Allergyintolerance Id 200 Example
  slug: aetna-v2-patientaccess-allergyintolerance-id-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Careplan 200 Example
  slug: aetna-v2-patientaccess-careplan-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Careplan Id 200 Example
  slug: aetna-v2-patientaccess-careplan-id-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Careteam 200 Example
  slug: aetna-v2-patientaccess-careteam-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Condition 200 Example
  slug: aetna-v2-patientaccess-condition-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Condition Id 200 Example
  slug: aetna-v2-patientaccess-condition-id-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Device 200 Example
  slug: aetna-v2-patientaccess-device-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Device Id 200 Example
  slug: aetna-v2-patientaccess-device-id-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Diagnosticreport 200 Example
  slug: aetna-v2-patientaccess-diagnosticreport-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Diagnosticreport Id 200 Example
  slug: aetna-v2-patientaccess-diagnosticreport-id-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Documentreference 200 Example
  slug: aetna-v2-patientaccess-documentreference-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Documentreference Id 200 Example
  slug: aetna-v2-patientaccess-documentreference-id-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Encounter 200 Example
  slug: aetna-v2-patientaccess-encounter-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Encounter Id 200 Example
  slug: aetna-v2-patientaccess-encounter-id-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Explanationofbenefit Id 200 Example
  slug: aetna-v2-patientaccess-explanationofbenefit-id-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Goal 200 Example
  slug: aetna-v2-patientaccess-goal-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Goal Id 200 Example
  slug: aetna-v2-patientaccess-goal-id-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Immunization 200 Example
  slug: aetna-v2-patientaccess-immunization-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Immunization Id 200 Example
  slug: aetna-v2-patientaccess-immunization-id-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Medication Id 200 Example
  slug: aetna-v2-patientaccess-medication-id-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Medicationknowledge 200 Example
  slug: aetna-v2-patientaccess-medicationknowledge-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Medicationknowledge Id 200 Example
  slug: aetna-v2-patientaccess-medicationknowledge-id-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Medicationrequest 200 Example
  slug: aetna-v2-patientaccess-medicationrequest-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Medicationrequest Id 200 Example
  slug: aetna-v2-patientaccess-medicationrequest-id-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Observation 200 Example
  slug: aetna-v2-patientaccess-observation-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Observation Id 200 Example
  slug: aetna-v2-patientaccess-observation-id-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Organization Id 200 Example
  slug: aetna-v2-patientaccess-organization-id-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Practitioner Id 200 Example
  slug: aetna-v2-patientaccess-practitioner-id-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Practitionerrole Id 200 Example
  slug: aetna-v2-patientaccess-practitionerrole-id-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Procedure 200 Example
  slug: aetna-v2-patientaccess-procedure-200-example
- key_count: 2
  name: Aetna V2 Patientaccess Procedure Id 200 Example
  slug: aetna-v2-patientaccess-procedure-id-200-example
features:
- description: All patient-facing APIs implement HL7 FHIR Release 4 standard for interoperability.
  name: FHIR R4 Compliance
- description: Secure OAuth 2.0 authorization framework for patient-authorized third-party app access.
  name: SMART on FHIR Authorization
- description: Full compliance with CMS-9115-F Interoperability and Patient Access Final Rule.
  name: CMS Interoperability Compliance
- description: Complete HIPAA-compliant EDI transaction set for provider administrative workflows.
  name: EDI Transaction Support
- description: Supports member-directed payer-to-payer data exchange for continuity of care.
  name: Payer-to-Payer Data Exchange
- description: Implements HL7 DaVinci Project PDEX, PDex Drug Formulary, and Plan Net guides.
  name: DaVinci Implementation Guides
finops:
- name: Aetna Finops
  service_category: API
  slug: aetna-finops
graphqls:
- description: '> **NOT A PROVIDER CONTRACT — DO NOT PUBLISH, SCORE OR GENERATE CLIENTS FROM THIS FILE.**'
  name: Aetna GraphQL Schema
  slug: aetna-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aetna.png
integrations:
- description: Integrated pharmacy benefit management for prescription drug coverage and mail-order pharmacy.
  name: CVS Caremark
- description: Primary provider portal for EDI transactions, eligibility, claims, and authorization requests.
  name: Availity
- description: EHR integration enabling clinical workflows including prior authorization and care management.
  name: Epic Payer Platform
- description: FHIR-based integration enabling Aetna members to view health data in Apple Health app.
  name: Apple Health
- description: Interoperability network participation for cross-organization health data exchange.
  name: CommonWell Health Alliance
- description: Alignment with CMS Blue Button 2.0 FHIR API patterns for Medicare data access.
  name: CMS Blue Button 2.0
json_schemas:
- name: Aetna FHIR R4 AllergyIntolerance
  property_count: 0
  slug: aetna-allergyintolerance
- name: Aetna FHIR R4 Bundle
  property_count: 0
  slug: aetna-bundle
- name: Aetna FHIR R4 CarePlan
  property_count: 0
  slug: aetna-careplan
- name: Aetna FHIR R4 CareTeam
  property_count: 0
  slug: aetna-careteam
- name: Aetna FHIR R4 Condition
  property_count: 0
  slug: aetna-condition
- name: Aetna FHIR R4 Device
  property_count: 0
  slug: aetna-device
- name: Aetna FHIR R4 DiagnosticReport
  property_count: 0
  slug: aetna-diagnosticreport
- name: Aetna FHIR R4 DocumentReference
  property_count: 0
  slug: aetna-documentreference
- name: Aetna FHIR R4 Encounter
  property_count: 0
  slug: aetna-encounter
- name: Aetna FHIR R4 ExplanationOfBenefit
  property_count: 0
  slug: aetna-explanationofbenefit
- name: Aetna FHIR R4 Goal
  property_count: 0
  slug: aetna-goal
- name: Aetna FHIR R4 HealthcareService
  property_count: 0
  slug: aetna-healthcareservice
- name: Aetna FHIR R4 Immunization
  property_count: 0
  slug: aetna-immunization
- name: Aetna FHIR R4 InsurancePlan
  property_count: 0
  slug: aetna-insuranceplan
- name: Aetna FHIR R4 Location
  property_count: 0
  slug: aetna-location
- name: Aetna FHIR R4 MedicationKnowledge
  property_count: 0
  slug: aetna-medicationknowledge
- name: Aetna FHIR R4 MedicationRequest
  property_count: 0
  slug: aetna-medicationrequest
- name: Aetna FHIR R4 Observation
  property_count: 48
  slug: aetna-observation
- name: Aetna FHIR R4 OperationOutcome
  property_count: 0
  slug: aetna-operationoutcome
- name: Aetna FHIR R4 Organization
  property_count: 0
  slug: aetna-organization
- name: Aetna FHIR R4 OrganizationAffiliation
  property_count: 0
  slug: aetna-organizationaffiliation
- name: Aetna FHIR R4 Patient
  property_count: 0
  slug: aetna-patient
- name: Aetna FHIR R4 Practitioner
  property_count: 0
  slug: aetna-practitioner
- name: Aetna FHIR R4 PractitionerRole
  property_count: 0
  slug: aetna-practitionerrole
- name: Aetna FHIR R4 Procedure
  property_count: 0
  slug: aetna-procedure
layout: provider
modified: '2026-08-30'
name: Aetna
nav: Providers
network: true
overview: 'Aetna publishes 3 APIs on the [APIs.io](https://apis.io/) network: Patient Access FHIR API, Provider Directory FHIR API, and Drug Formulary FHIR API. Tagged areas include Health Insurance, Healthcare, FHIR, Patient Access, and Provider Directory.


  Aetna''s developer surface includes code examples, authentication, changelog, sandbox, documentation, API reference, getting-started guide, and 79 more developer resources.'
plans:
- name: Aetna Plans Pricing
  plan_count: 0
  slug: aetna-plans-pricing
press:
- date: '2026-05-25'
  title: Aetna taps into AI with Care Paths tech
  url: https://www.healthcarefinancenews.com/news/aetna-taps-ai-care-paths-tech
- date: '2026-05-25'
  title: Aetna launches leading edge conversational AI navigation
  url: https://www.cvshealth.com/news/innovation/aetna-launches-leading-edge-conversational-ai-navigation.html
- date: '2026-05-25'
  title: Aetna launches conversational AI for health care navigation
  url: https://www.linkedin.com/posts/nathan-frank-3b00807_aetna-cvshealth-aetnatechnology-activity-7396987415451746304-uAKd
- date: '2026-05-25'
  title: Aetna expands initiatives to simplify experiences for health ...
  url: https://www.prnewswire.com/news-releases/aetna-expands-initiatives-to-simplify-experiences-for-health-care-professionals-and-patients-302632202.html
- date: '2026-05-25'
  title: Aetna Launches New AI and Digital Tools to Improve ...
  url: https://www.cvshealth.com/news/innovation/aetna-launches-new-ai-and-digital-tools-to-improve-access-and-care.html
random_paper: 17
rate_limits:
- limit_count: 0
  name: Aetna Rate Limits
  slug: aetna-rate-limits
scopes:
- name: Aetna Scopes
  scope_count: 54
  slug: aetna-scopes
  summary_line: 54 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 47.5
  coverage:
    artifact_dirs: 30
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 33.3
    contract_quality: 38.2
    developer_ergonomics: 42.3
    discoverability: 74.1
    governance: 33.3
    operational_transparency: 31.6
  previous_composite: 47.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 66.7
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 68.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: authentication
  name: Aetna Authentication
  slug: aetna-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Aetna Domain Security
  slug: aetna-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aetna
tags:
- Health Insurance
- Healthcare
- FHIR
- Patient Access
- Provider Directory
- Drug Formulary
- Prior Authorization
- CMS Interoperability
- SMART on FHIR
- CARIN Blue Button
- Da Vinci
- Payer
- Fortune 100
- CVS Health
use_cases:
- description: Members use SMART on FHIR apps to access their complete health records across providers.
  name: Member Health Record Access
- description: Developers build directory search tools to help patients find in-network providers.
  name: Provider Network Verification
- description: Applications use formulary API to compare medication costs across Aetna plans.
  name: Drug Cost Comparison
- description: Healthcare providers submit claims electronically via EDI 837 transactions through Availity.
  name: Electronic Claims Submission
- description: Providers verify member eligibility and benefits in real time using 270/271 EDI transactions.
  name: Eligibility Verification
- description: Providers receive and process electronic remittance advice via EDI 835 transactions.
  name: Remittance Processing
website: https://www.aetna.com
---

---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  - '{''url'': ''https://www.cerner.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.oracle.com/health/ — a different registrable domain (cerner.com -> oracle.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 41
  human_in_the_loop: 0
  name: Cerner Agentic Access
  operation_count: 135
  slug: cerner-agentic-access
  summary_line: 135 operations · 41 acting
api_count: 50
apis:
- description: The Cerner Millennium DSTU2 FHIR API supports legacy SMART on FHIR applications and integrations with Meaningful Use 2015 CEHRT certification criteria, and remains available alongside the newer R4 imp
  name: Oracle Health Millennium FHIR DSTU2 API
  slug: oracle-health-fhir-dstu2-api
- description: 'The Oracle Health Code Console (formerly Cerner Code) is the developer portal used to register SMART on FHIR and system-level applications, configure redirect URIs and launch parameters, manage OAuth '
  name: Oracle Health Code Console (Developer Portal)
  slug: oracle-health-code-console
- description: Cerner CareAware provides device and third-party application integration APIs for medical device data capture, bi-directional HL7 v2 messaging, and workflow embedding into Millennium, supporting medic
  name: Cerner CareAware Integration APIs
  slug: cerner-careaware
- description: Oracle Health implements the SMART on FHIR App Launch framework (standalone and EHR-launch) with OpenID Connect identity tokens, enabling third-party clinician and patient-facing applications to embed
  name: Oracle Health SMART on FHIR App Launch
  slug: oracle-health-smart-on-fhir
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 Account resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Account API
  slug: oracle-health-account-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 Appointment resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Appointment API
  slug: oracle-health-appointment-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 Basic resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Basic API
  slug: oracle-health-basic-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 Binary resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Binary API
  slug: oracle-health-binary-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR server metadata and capability statements.
  name: Oracle Health (Cerner) Capability API
  slug: oracle-health-capability-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 CareTeam resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Care Team API
  slug: oracle-health-careteam-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 ChargeItem resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Charge Item API
  slug: oracle-health-chargeitem-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 Communication resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Communication API
  slug: oracle-health-communication-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 Condition resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Condition API
  slug: oracle-health-condition-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 Consent resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Consent API
  slug: oracle-health-consent-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 Coverage resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Coverage API
  slug: oracle-health-coverage-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR conformance definitions and operations.
  name: Oracle Health (Cerner) Definitions API
  slug: oracle-health-definitions-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 Device resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Device API
  slug: oracle-health-device-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 DiagnosticReport resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Diagnostic Report API
  slug: oracle-health-diagnosticreport-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 Encounter resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Encounter API
  slug: oracle-health-encounter-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: Kick off a bulk export job.
  name: Oracle Health (Cerner) Export API
  slug: oracle-health-export-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 FamilyMemberHistory resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Family Member History API
  slug: oracle-health-familymemberhistory-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: Retrieve the download URLs for completed export files.
  name: Oracle Health (Cerner) Files API
  slug: oracle-health-files-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: Generic FHIR resource read/write operations.
  name: Oracle Health (Cerner) Generic API
  slug: oracle-health-generic-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 Goal resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Goal API
  slug: oracle-health-goal-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 Immunization resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Immunization API
  slug: oracle-health-immunization-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: Poll and cancel bulk export jobs.
  name: Oracle Health (Cerner) Jobs API
  slug: oracle-health-jobs-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 Location resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Location API
  slug: oracle-health-location-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 Media resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Media API
  slug: oracle-health-media-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 MedicationDispense resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Medication Dispense API
  slug: oracle-health-medicationdispense-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 NutritionOrder resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Nutrition Order API
  slug: oracle-health-nutritionorder-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 Observation resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Observation API
  slug: oracle-health-observation-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 OperationDefinition resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Operation Definition API
  slug: oracle-health-operationdefinition-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 Organization resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Organization API
  slug: oracle-health-organization-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 Patient resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Patient API
  slug: oracle-health-patient-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 Person resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Person API
  slug: oracle-health-person-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 Practitioner resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Practitioner API
  slug: oracle-health-practitioner-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 Procedure resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Procedure API
  slug: oracle-health-procedure-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 Provenance resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Provenance API
  slug: oracle-health-provenance-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 Questionnaire resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Questionnaire API
  slug: oracle-health-questionnaire-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 QuestionnaireResponse resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Questionnaire Response API
  slug: oracle-health-questionnaireresponse-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 RelatedPerson resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Related Person API
  slug: oracle-health-relatedperson-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 Schedule resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Schedule API
  slug: oracle-health-schedule-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 ServiceRequest resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Service Request API
  slug: oracle-health-servicerequest-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 Slot resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Slot API
  slug: oracle-health-slot-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 Specimen resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Specimen API
  slug: oracle-health-specimen-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 StructureDefinition resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Structure Definition API
  slug: oracle-health-structuredefinition-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: 'System-level FHIR interactions: conformance metadata and batch.'
  name: Oracle Health (Cerner) System API
  slug: oracle-health-system-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 AllergyIntolerance resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Allergy Intolerance API
  slug: oracle-health-allergy-intolerance-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 CapabilityStatement resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Capability Statement API
  slug: oracle-health-capability-statement-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 CarePlan resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Care plan API
  slug: oracle-health-care-plan-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 DocumentReference resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Document Reference API
  slug: oracle-health-document-reference-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 InsurancePlan resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Insurance Plan API
  slug: oracle-health-insurance-plan-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 MedicationAdministration resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Medication Administration API
  slug: oracle-health-medication-administration-api
- baseURL: https://fhir-ehr.cerner.com/dstu2/{tenant}
  baseurl_source: declared
  description: FHIR R4 MedicationRequest resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Medication Request API
  slug: oracle-health-medication-request-api
arazzos:
- description: Locate a patient, create a FHIR resource against that patient, then update it by id.
  name: Cerner Oracle Health Clinical Resource Write-Back
  slug: cerner-clinical-resource-write-workflow
- description: Read the server metadata and CapabilityStatement, then enumerate supported operations and structure definitions.
  name: Cerner Oracle Health Conformance Discovery
  slug: cerner-conformance-discovery-workflow
- description: Discover server capabilities, locate a patient, then pull the patient's conditions, encounters, and procedures.
  name: Cerner Oracle Health SMART on FHIR Patient Retrieval
  slug: cerner-smart-on-fhir-patient-data-retrieval-workflow
artifact_total: 78
collections:
- collection_type: open
  name: Oracle Health Millennium Platform FHIR R4 Capability API
  slug: open-cerner-capability-api
- collection_type: open
  name: Oracle Health Millennium Platform FHIR R4 Capability Condition API
  slug: open-cerner-condition-api
- collection_type: open
  name: Oracle Health Millennium Platform FHIR R4 Capability Definitions API
  slug: open-cerner-definitions-api
- collection_type: open
  name: Oracle Health Millennium Platform FHIR R4 Capability Encounter API
  slug: open-cerner-encounter-api
- collection_type: open
  name: Oracle Health Millennium Platform FHIR R4 Capability Generic API
  slug: open-cerner-generic-api
- collection_type: open
  name: Oracle Health Millennium Platform FHIR R4 API
  slug: open-cerner-oracle-health-fhir-r4-api
- collection_type: open
  name: Oracle Health Millennium Platform FHIR R4 Capability Patient API
  slug: open-cerner-patient-api
- collection_type: open
  name: Oracle Health Millennium Platform FHIR R4 Capability Procedure API
  slug: open-cerner-procedure-api
common:
- group: other
  href: https://artifacts.apis.io/oracle-health/capabilities/cerner-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cerner-capability-edges.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/oracle/
- group: agent
  href: https://artifacts.apis.io/oracle-health/agentic-access/cerner-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cerner-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/oracle-health/security/cerner-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cerner-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/oracle-health/security/cerner-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cerner-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/oracle-health/authentication/cerner-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cerner-authentication.yml
- group: auth
  href: https://artifacts.apis.io/oracle-health/scopes/cerner-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cerner-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cerner-corporation
- group: company
  title: ''
  type: Website
  url: https://www.cerner.com
- group: other
  title: ''
  type: Corporate
  url: https://www.oracle.com/health/
- group: other
  title: ''
  type: Developer
  url: https://www.oracle.com/health/developer/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.oracle.com/en/industries/health/millennium-platform-apis/index.html
- group: other
  title: ''
  type: FHIR
  url: https://fhir.cerner.com/
- group: start
  title: ''
  type: CodeConsole
  url: https://code.cerner.com/
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/cerner
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
- group: design
  title: ''
  type: ArazzoWorkflows
  url: ''
- group: docs
  href: https://artifacts.apis.io/oracle-health/openapi/cerner-millennium-fhir-r4-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/cerner-millennium-fhir-r4-openapi.yml
- group: agent
  href: https://artifacts.apis.io/oracle-health/well-known/cerner-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cerner-well-known.yml
- group: build
  href: https://artifacts.apis.io/oracle-health/packages/cerner-packages.yml
  title: ''
  type: Packages
  url: packages/cerner-packages.yml
- group: build
  href: https://artifacts.apis.io/oracle-health/packages/cerner-packages.yml
  title: ''
  type: SDKs
  url: packages/cerner-packages.yml
- group: agent
  href: https://artifacts.apis.io/oracle-health/mcp/cerner-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/cerner-mcp.yml
- group: agent
  href: https://artifacts.apis.io/oracle-health/llms/cerner-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cerner-llms.txt
- group: other
  href: https://artifacts.apis.io/oracle-health/overlays/cerner-millennium-fhir-r4-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cerner-millennium-fhir-r4-overlay.yaml
- group: design
  href: https://artifacts.apis.io/oracle-health/conformance/cerner-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cerner-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.oracle.com/corporate/acquisitions/cerner/security/
- group: design
  href: https://artifacts.apis.io/oracle-health/errors/cerner-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cerner-problem-types.yml
- group: design
  href: https://artifacts.apis.io/oracle-health/lifecycle/cerner-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cerner-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/oracle-health/conventions/cerner-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cerner-conventions.yml
- group: design
  href: https://artifacts.apis.io/oracle-health/data-model/cerner-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cerner-data-model.yml
- group: start
  href: https://artifacts.apis.io/oracle-health/sandbox/cerner-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/cerner-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/oracle-health/changelog/cerner-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cerner-changelog.yml
- group: design
  href: https://artifacts.apis.io/oracle-health/components/cerner-components.yml
  title: ''
  type: Components
  url: components/cerner-components.yml
- group: agent
  href: https://artifacts.apis.io/oracle-health/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/oracle-health/plans/cerner-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cerner-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/oracle-health/rate-limits/cerner-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cerner-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/oracle-health/finops/cerner-finops.yml
  title: ''
  type: FinOps
  url: finops/cerner-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.oracle.com/health/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/en/industries/health/millennium-platform-apis/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oracle.com/en/industries/health/millennium-platform-apis/index.html
- group: operate
  title: ''
  type: Support
  url: https://forums.oracle.com/ords/apexds/domain/open-developer-experience
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cerner
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms/
- group: build
  href: https://artifacts.apis.io/oracle-health/collections/cerner-oracle-health-fhir-r4-api.postman_collection.json
  title: ''
  type: Collections
  url: collections/cerner-oracle-health-fhir-r4-api.postman_collection.json
- group: design
  href: https://artifacts.apis.io/oracle-health/arazzo/_index.yml
  title: ''
  type: Arazzo
  url: arazzo/_index.yml
created: '2026-03-23'
description: 'Oracle Health, formerly Cerner, builds and operates Millennium — one of the two dominant electronic health record platforms in United States hospitals and health systems. Cerner was acquired by Oracle in June 2022 and its developer program now runs as the Oracle Health Developer Program. The public developer surface is HL7 FHIR R4: a multi-tenant, US Core-conformant FHIR server that serves a live CapabilityStatement at /metadata and a live SMART on FHIR discovery document at /.well-known/smart-configuration, advertising 303 OAuth scopes across patient, user and system personas in both SMART v1 and SMART v2 granular forms. It supports SMART App Launch (EHR and standalone), SMART Backend Services with private_key_jwt, FHIR Bulk Data Access export, and — unusually — an open, unauthenticated, read-only endpoint that serves real sandbox data with no registration at all. Alongside FHIR it operates proprietary Millennium EHR APIs, HL7 v2 messaging through Cerner Open Interface, and
  the CareAware device and integration platform. There is no OpenAPI, no GraphQL endpoint, no MCP server, no agent card, no published pricing, no published rate limits, no status page and no first-party SDK for the FHIR API.'
finops:
- has_sources: true
  method: derived
  name: Cerner Finops
  primary_unit: ''
  service_category: ''
  slug: cerner-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cerner.png
layout: provider
modified: '2026-08-21'
name: Oracle Health (Cerner)
nav: Providers
network: true
overview: 'Oracle Health (Cerner) publishes 54 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Appointment API, Basic API, and 51 more. Tagged areas include Bulk FHIR, CapabilityStatement, CareAware, Cerner Millennium, and Clinical Data.


  The Oracle Health (Cerner) catalog on APIs.io includes 1 Spectral governance ruleset.


  Oracle Health (Cerner)''s developer surface includes authentication, API reference, sandbox, changelog, documentation, getting-started guide, support, and 37 more developer resources.'
plans:
- name: Cerner Plans Pricing
  plan_count: 0
  slug: cerner-plans-pricing
press:
- date: ''
  title: Oracle explores Cerner sale to fund AI expansion
  url: https://www.linkedin.com/posts/timlynott_healthtech-healthcareit-ehr-activity-7423118955730493440-4Eci
- date: ''
  title: Oracle Cerner signs AI contract with FDA focused on ...
  url: https://fedscoop.com/oracle-cerner-fda-ai-contract/
- date: ''
  title: Oracle Buys Cerner
  url: https://www.prnewswire.com/news-releases/oracle-buys-cerner-301448252.html
- date: ''
  title: Oracle to launch new AI-backed EHR in 2025
  url: https://www.healthcaredive.com/news/oracle-new-ai-backed-ehr-2025/731398/
- date: ''
  title: Oracle must stop kicking the Cerner can down the road— ...
  url: https://www.hfsresearch.com/research/oracle-kicking-cerner-decisive/
random_paper: 9
rate_limits:
- limit_count: 0
  name: Cerner Rate Limits
  slug: cerner-rate-limits
rules:
- authorship: generated
  effective_rule_count: 117
  extends:
  - spectral:oas
  name: Oracle Health (Cerner) API Rules
  rule_count: 76
  severity_counts:
    error: 57
    hint: 0
    info: 2
    warn: 17
  slug: oracle-health-rules
scopes:
- name: Cerner Scopes
  scope_count: 303
  slug: cerner-scopes
  summary_line: 303 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 45.5
  coverage:
    artifact_dirs: 34
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.8
  facets:
    access_clarity: 36.8
    contract_governance: 31.8
    contract_quality: 20.5
    developer_ergonomics: 68.5
    discoverability: 78.6
    operational_transparency: 18.4
  previous_composite: 46.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 49
      marker_coverage: 92.5
      total: 53
    mcp: derived
    skills: derived
  regulatory:
    applies: true
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
screenshot: https://apis.io/screenshots/oracle-health/cerner-2026-06-20T174140.png
security:
- kind: authentication
  name: Cerner Authentication
  slug: cerner-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Cerner Domain Security
  slug: cerner-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cerner Trust Center
  slug: cerner-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, FIPS 140
skill_count: 4
skills:
- name: cerner-backend-bulk-export
  slug: cerner-backend-bulk-export
- name: cerner-open-sandbox-exploration
  slug: cerner-open-sandbox-exploration
- name: cerner-patient-clinical-summary
  slug: cerner-patient-clinical-summary
- name: cerner-write-back-clinical-resource
  slug: cerner-write-back-clinical-resource
slug: oracle-health
tags:
- Bulk FHIR
- CapabilityStatement
- CareAware
- Cerner Millennium
- Clinical Data
- Code Console
- Electronic Health Records
- FHIR
- Fortune 1000
- HL7
- HL7v2
- Healthcare
- Interoperability
- Millennium Platform
- Multi-Tenant
- OAuth
- Oracle
- Oracle Health
- Patient Access
- Provider Directory
- SMART Backend Services
- SMART on FHIR
- US Core
- Authentication
website: https://www.cerner.com
---

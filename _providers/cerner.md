---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - '{''url'': ''https://www.cerner.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.oracle.com/health/ — a different registrable domain (cerner.com -> oracle.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Cerner Agentic Access
  operation_count: 11
  slug: cerner-agentic-access
  summary_line: 11 operations · 3 acting
api_count: 54
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
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR server metadata and capability statements.
  name: Cerner (Oracle Health) Capability API
  slug: cerner-capability-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: Patient conditions and problem-list entries.
  name: Cerner (Oracle Health) Condition API
  slug: cerner-condition-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR conformance definitions and operations.
  name: Cerner (Oracle Health) Definitions API
  slug: cerner-definitions-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: Patient encounter records.
  name: Cerner (Oracle Health) Encounter API
  slug: cerner-encounter-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: Generic FHIR resource read/write operations.
  name: Cerner (Oracle Health) Generic API
  slug: cerner-generic-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: Patient demographics and identifiers.
  name: Cerner (Oracle Health) Patient API
  slug: cerner-patient-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: Patient procedures.
  name: Cerner (Oracle Health) Procedure API
  slug: cerner-procedure-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 Account resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Account API
  slug: cerner-account-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 AllergyIntolerance resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Allergy Intolerance API
  slug: cerner-allergyintolerance-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 Appointment resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Appointment API
  slug: cerner-appointment-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 Basic resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Basic API
  slug: cerner-basic-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 Binary resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Binary API
  slug: cerner-binary-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 CapabilityStatement resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Capability Statement API
  slug: cerner-capabilitystatement-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 CarePlan resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Care Plan API
  slug: cerner-careplan-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 CareTeam resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Care Team API
  slug: cerner-careteam-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 ChargeItem resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Charge Item API
  slug: cerner-chargeitem-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 Communication resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Communication API
  slug: cerner-communication-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 Consent resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Consent API
  slug: cerner-consent-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 Coverage resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Coverage API
  slug: cerner-coverage-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 Device resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Device API
  slug: cerner-device-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 DiagnosticReport resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Diagnostic Report API
  slug: cerner-diagnosticreport-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 DocumentReference resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Document Reference API
  slug: cerner-documentreference-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: Kick off a bulk export job.
  name: Oracle Health (Cerner) Export API
  slug: cerner-export-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 FamilyMemberHistory resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Family Member History API
  slug: cerner-familymemberhistory-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: Retrieve the download URLs for completed export files.
  name: Oracle Health (Cerner) Files API
  slug: cerner-files-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 Goal resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Goal API
  slug: cerner-goal-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 Immunization resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Immunization API
  slug: cerner-immunization-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 InsurancePlan resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Insurance Plan API
  slug: cerner-insuranceplan-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: Poll and cancel bulk export jobs.
  name: Oracle Health (Cerner) Jobs API
  slug: cerner-jobs-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 Location resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Location API
  slug: cerner-location-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 Media resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Media API
  slug: cerner-media-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 MedicationAdministration resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Medication Administration API
  slug: cerner-medicationadministration-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 MedicationDispense resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Medication Dispense API
  slug: cerner-medicationdispense-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 MedicationRequest resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Medication Request API
  slug: cerner-medicationrequest-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 NutritionOrder resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Nutrition Order API
  slug: cerner-nutritionorder-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 Observation resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Observation API
  slug: cerner-observation-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 OperationDefinition resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Operation Definition API
  slug: cerner-operationdefinition-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 Organization resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Organization API
  slug: cerner-organization-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 Person resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Person API
  slug: cerner-person-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 Practitioner resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Practitioner API
  slug: cerner-practitioner-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 Provenance resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Provenance API
  slug: cerner-provenance-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 Questionnaire resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Questionnaire API
  slug: cerner-questionnaire-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 QuestionnaireResponse resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Questionnaire Response API
  slug: cerner-questionnaireresponse-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 RelatedPerson resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Related Person API
  slug: cerner-relatedperson-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 Schedule resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Schedule API
  slug: cerner-schedule-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 ServiceRequest resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Service Request API
  slug: cerner-servicerequest-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 Slot resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Slot API
  slug: cerner-slot-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 Specimen resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Specimen API
  slug: cerner-specimen-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: FHIR R4 StructureDefinition resource as implemented by Oracle Health Millennium Platform.
  name: Oracle Health (Cerner) Structure Definition API
  slug: cerner-structuredefinition-api
- baseURL: https://fhir-ehr.cerner.com/r4/{tenant}
  baseurl_source: declared
  description: 'System-level FHIR interactions: conformance metadata and batch.'
  name: Oracle Health (Cerner) System API
  slug: cerner-system-api
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
artifact_total: 75
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: CapabilityMap
  url: capabilities/cerner-capability-edges.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/oracle/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cerner-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cerner-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cerner-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cerner-authentication.yml
- group: auth
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
  title: ''
  type: OpenAPI
  url: openapi/cerner-millennium-fhir-r4-openapi.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cerner-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/cerner-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cerner-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/cerner-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cerner-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/cerner-millennium-fhir-r4-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/cerner-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.oracle.com/corporate/acquisitions/cerner/security/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cerner-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cerner-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cerner-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cerner-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cerner-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cerner-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/cerner-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cerner-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cerner-rate-limits.yml
- group: commercial
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
  title: ''
  type: Collections
  url: collections/cerner-oracle-health-fhir-r4-api.postman_collection.json
- group: design
  title: ''
  type: Arazzo
  url: arazzo/_index.yml
created: '2026-03-23'
description: 'Oracle Health, formerly Cerner, builds and operates Millennium — one of the two dominant electronic health record platforms in United States hospitals and health systems. Cerner was acquired by Oracle in June 2022 and its developer program now runs as the Oracle Health Developer Program. The public developer surface is HL7 FHIR R4: a multi-tenant, US Core-conformant FHIR server that serves a live CapabilityStatement at /metadata and a live SMART on FHIR discovery document at /.well-known/smart-configuration, advertising 303 OAuth scopes across patient, user and system personas in both SMART v1 and SMART v2 granular forms. It supports SMART App Launch (EHR and standalone), SMART Backend Services with private_key_jwt, FHIR Bulk Data Access export, and — unusually — an open, unauthenticated, read-only endpoint that serves real sandbox data with no registration at all. Alongside FHIR it operates proprietary Millennium EHR APIs, HL7 v2 messaging through Cerner Open Interface, and
  the CareAware device and integration platform. There is no OpenAPI, no GraphQL endpoint, no MCP server, no agent card, no published pricing, no published rate limits, no status page and no first-party SDK for the FHIR API.'
finops:
- name: Cerner Finops
  service_category: API
  slug: cerner-finops
graphqls:
- description: Cerner Millennium, now operated as Oracle Health, exposes clinical and administrative data through HL7 FHIR R4 REST APIs. There is no native GraphQL endpoint offered by Oracle Health or the Cerner Mil
  name: Cerner (Oracle Health) GraphQL
  slug: cerner-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cerner.png
layout: provider
modified: '2026-08-21'
name: Oracle Health (Cerner)
nav: Providers
network: true
overview: 'Oracle Health (Cerner) publishes 50 APIs on the [APIs.io](https://apis.io/) network, including Cerner (Oracle Health) Capability API, Cerner (Oracle Health) Condition API, Cerner (Oracle Health) Definitions API, and 47 more. Tagged areas include Bulk FHIR, CapabilityStatement, CareAware, Cerner Millennium, and Clinical Data.


  Oracle Health (Cerner)''s developer surface includes authentication, API reference, sandbox, changelog, documentation, getting-started guide, support, and 37 more developer resources.'
plans:
- name: Cerner Plans Pricing
  plan_count: 0
  slug: cerner-plans-pricing
press:
- date: '2026-05-25'
  title: Oracle explores Cerner sale to fund AI expansion
  url: https://www.linkedin.com/posts/timlynott_healthtech-healthcareit-ehr-activity-7423118955730493440-4Eci
- date: '2026-05-25'
  title: Oracle Cerner signs AI contract with FDA focused on ...
  url: https://fedscoop.com/oracle-cerner-fda-ai-contract/
- date: '2026-05-25'
  title: Oracle Buys Cerner
  url: https://www.prnewswire.com/news-releases/oracle-buys-cerner-301448252.html
- date: '2026-05-25'
  title: Oracle to launch new AI-backed EHR in 2025
  url: https://www.healthcaredive.com/news/oracle-new-ai-backed-ehr-2025/731398/
- date: '2026-05-25'
  title: Oracle must stop kicking the Cerner can down the road— ...
  url: https://www.hfsresearch.com/research/oracle-kicking-cerner-decisive/
random_paper: 9
rate_limits:
- limit_count: 0
  name: Cerner Rate Limits
  slug: cerner-rate-limits
scopes:
- name: Cerner Scopes
  scope_count: 303
  slug: cerner-scopes
  summary_line: 303 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 49.2
  coverage:
    artifact_dirs: 30
    catalog_gap: 85.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -1.8
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 26.5
    developer_ergonomics: 68.5
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 51.0
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
    score: 82.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cerner/refs/heads/main/screenshots/cerner-2026-06-20T174140.png
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
slug: cerner
tags:
- Bulk FHIR
- CapabilityStatement
- CareAware
- Cerner Millennium
- Clinical Data
- Code Console
- EHR
- Electronic Health Records
- FHIR
- Fortune 1000
- HL7
- HL7v2
- Healthcare
- Interoperability
- Millennium Platform
- Multi-Tenant
- Authentication
- Oracle
- Oracle Health
- Patient Access
- Provider Directory
- SMART Backend Services
- SMART on FHIR
- US Core
website: https://www.cerner.com
---

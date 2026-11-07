---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
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
  score: 29.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Legacy HL7 FHIR DSTU2 (1.0.2) endpoint operated by Select Medical on the same Epic platform, registered as "Select Medical" in Epic''s public DSTU2 endpoint directory since 2020-06-01 and still listed '
  name: Select Medical FHIR DSTU2 API
  slug: select-medical-holdings-fhir-dstu2
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 Account resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Account API
  slug: select-medical-holdings-account-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 AdverseEvent resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Adverse Event API
  slug: select-medical-holdings-adverseevent-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 Appointment resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Appointment API
  slug: select-medical-holdings-appointment-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 Binary resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Binary API
  slug: select-medical-holdings-binary-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 BodyStructure resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Body Structure API
  slug: select-medical-holdings-bodystructure-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: 'FHIR R4 CareTeam resource as declared by the Select Medical FHIR server CapabilityStatement. Declared US Core profiles: us-core-careteam|6.1.0.'
  name: Select Medical Holdings Care Team API
  slug: select-medical-holdings-careteam-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 Claim resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Claim API
  slug: select-medical-holdings-claim-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 Communication resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Communication API
  slug: select-medical-holdings-communication-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 ConceptMap resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Concept Map API
  slug: select-medical-holdings-conceptmap-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: 'FHIR R4 Condition resource as declared by the Select Medical FHIR server CapabilityStatement. Declared US Core profiles: us-core-condition-encounter-diagnosis|6.1.0, us-core-condition-problems-health-'
  name: Select Medical Holdings Condition API
  slug: select-medical-holdings-condition-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 Consent resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Consent API
  slug: select-medical-holdings-consent-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 Contract resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Contract API
  slug: select-medical-holdings-contract-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: 'FHIR R4 Coverage resource as declared by the Select Medical FHIR server CapabilityStatement. Declared US Core profiles: us-core-coverage|6.1.0.'
  name: Select Medical Holdings Coverage API
  slug: select-medical-holdings-coverage-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: 'FHIR R4 Device resource as declared by the Select Medical FHIR server CapabilityStatement. Declared US Core profiles: us-core-implantable-device|6.1.0.'
  name: Select Medical Holdings Device API
  slug: select-medical-holdings-device-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 DeviceRequest resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Device Request API
  slug: select-medical-holdings-devicerequest-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 DeviceUseStatement resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Device Use Statement API
  slug: select-medical-holdings-deviceusestatement-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: 'FHIR R4 DiagnosticReport resource as declared by the Select Medical FHIR server CapabilityStatement. Declared US Core profiles: us-core-diagnosticreport-lab|6.1.0, us-core-diagnosticreport-note|6.1.0.'
  name: Select Medical Holdings Diagnostic Report API
  slug: select-medical-holdings-diagnosticreport-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: 'FHIR R4 Encounter resource as declared by the Select Medical FHIR server CapabilityStatement. Declared US Core profiles: us-core-encounter|6.1.0.'
  name: Select Medical Holdings Encounter API
  slug: select-medical-holdings-encounter-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 Endpoint resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Endpoint API
  slug: select-medical-holdings-endpoint-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 EpisodeOfCare resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Episode Of Care API
  slug: select-medical-holdings-episodeofcare-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 ExplanationOfBenefit resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Explanation Of Benefit API
  slug: select-medical-holdings-explanationofbenefit-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 FamilyMemberHistory resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Family Member History API
  slug: select-medical-holdings-familymemberhistory-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 Flag resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Flag API
  slug: select-medical-holdings-flag-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: 'FHIR R4 Goal resource as declared by the Select Medical FHIR server CapabilityStatement. Declared US Core profiles: us-core-goal|6.1.0.'
  name: Select Medical Holdings Goal API
  slug: select-medical-holdings-goal-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 Group resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Group API
  slug: select-medical-holdings-group-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 ImagingStudy resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Imaging Study API
  slug: select-medical-holdings-imagingstudy-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: 'FHIR R4 Immunization resource as declared by the Select Medical FHIR server CapabilityStatement. Declared US Core profiles: us-core-immunization|6.1.0.'
  name: Select Medical Holdings Immunization API
  slug: select-medical-holdings-immunization-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 ImmunizationRecommendation resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Immunization Recommendation API
  slug: select-medical-holdings-immunizationrecommendation-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 List resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings List API
  slug: select-medical-holdings-list-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 Location resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Location API
  slug: select-medical-holdings-location-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 Measure resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Measure API
  slug: select-medical-holdings-measure-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 MeasureReport resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Measure Report API
  slug: select-medical-holdings-measurereport-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 Media resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Media API
  slug: select-medical-holdings-media-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: 'FHIR R4 Medication resource as declared by the Select Medical FHIR server CapabilityStatement. Declared US Core profiles: us-core-medication|6.1.0.'
  name: Select Medical Holdings Medication API
  slug: select-medical-holdings-medication-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: 'FHIR R4 MedicationDispense resource as declared by the Select Medical FHIR server CapabilityStatement. Declared US Core profiles: us-core-medicationdispense|6.1.0.'
  name: Select Medical Holdings Medication Dispense API
  slug: select-medical-holdings-medicationdispense-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 NutritionOrder resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Nutrition Order API
  slug: select-medical-holdings-nutritionorder-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: 'FHIR R4 Observation resource as declared by the Select Medical FHIR server CapabilityStatement. Declared US Core profiles: head-occipital-frontal-circumference-percentile|6.1.0, pediatric-bmi-for-age|'
  name: Select Medical Holdings Observation API
  slug: select-medical-holdings-observation-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: 'FHIR R4 Organization resource as declared by the Select Medical FHIR server CapabilityStatement. Declared US Core profiles: us-core-organization|6.1.0.'
  name: Select Medical Holdings Organization API
  slug: select-medical-holdings-organization-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: 'FHIR R4 Patient resource as declared by the Select Medical FHIR server CapabilityStatement. Declared US Core profiles: us-core-patient|6.1.0.'
  name: Select Medical Holdings Patient API
  slug: select-medical-holdings-patient-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: 'FHIR R4 Practitioner resource as declared by the Select Medical FHIR server CapabilityStatement. Declared US Core profiles: us-core-practitioner|6.1.0.'
  name: Select Medical Holdings Practitioner API
  slug: select-medical-holdings-practitioner-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: 'FHIR R4 Procedure resource as declared by the Select Medical FHIR server CapabilityStatement. Declared US Core profiles: us-core-procedure|6.1.0.'
  name: Select Medical Holdings Procedure API
  slug: select-medical-holdings-procedure-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: 'FHIR R4 Provenance resource as declared by the Select Medical FHIR server CapabilityStatement. Declared US Core profiles: us-core-provenance|6.1.0.'
  name: Select Medical Holdings Provenance API
  slug: select-medical-holdings-provenance-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 Questionnaire resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Questionnaire API
  slug: select-medical-holdings-questionnaire-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 QuestionnaireResponse resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Questionnaire Response API
  slug: select-medical-holdings-questionnaireresponse-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: 'FHIR R4 RelatedPerson resource as declared by the Select Medical FHIR server CapabilityStatement. Declared US Core profiles: us-core-relatedperson|6.1.0.'
  name: Select Medical Holdings Related Person API
  slug: select-medical-holdings-relatedperson-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 RequestGroup resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Request Group API
  slug: select-medical-holdings-requestgroup-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 ResearchStudy resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Research Study API
  slug: select-medical-holdings-researchstudy-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 ResearchSubject resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Research Subject API
  slug: select-medical-holdings-researchsubject-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: 'FHIR R4 ServiceRequest resource as declared by the Select Medical FHIR server CapabilityStatement. Declared US Core profiles: us-core-servicerequest|6.1.0.'
  name: Select Medical Holdings Service Request API
  slug: select-medical-holdings-servicerequest-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: 'FHIR R4 Specimen resource as declared by the Select Medical FHIR server CapabilityStatement. Declared US Core profiles: us-core-specimen|6.1.0.'
  name: Select Medical Holdings Specimen API
  slug: select-medical-holdings-specimen-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 Substance resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Substance API
  slug: select-medical-holdings-substance-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 Task resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Task API
  slug: select-medical-holdings-task-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4
  baseurl_source: declared
  description: FHIR R4 ValueSet resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Value Set API
  slug: select-medical-holdings-valueset-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/DSTU2
  baseurl_source: declared
  description: 'FHIR R4 AllergyIntolerance resource as declared by the Select Medical FHIR server CapabilityStatement. Declared US Core profiles: us-core-allergyintolerance|6.1.0.'
  name: Select Medical Holdings Allergy Intolerance API
  slug: select-medical-holdings-allergy-intolerance-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/DSTU2
  baseurl_source: declared
  description: 'FHIR R4 CarePlan resource as declared by the Select Medical FHIR server CapabilityStatement. Declared US Core profiles: us-core-careplan|6.1.0.'
  name: Select Medical Holdings Care plan API
  slug: select-medical-holdings-care-plan-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/DSTU2
  baseurl_source: declared
  description: 'FHIR R4 DocumentReference resource as declared by the Select Medical FHIR server CapabilityStatement. Declared US Core profiles: us-core-documentreference|6.1.0.'
  name: Select Medical Holdings Document Reference API
  slug: select-medical-holdings-document-reference-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/DSTU2
  baseurl_source: declared
  description: FHIR R4 MedicationAdministration resource as declared by the Select Medical FHIR server CapabilityStatement.
  name: Select Medical Holdings Medication Administration API
  slug: select-medical-holdings-medication-administration-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/DSTU2
  baseurl_source: declared
  description: 'FHIR R4 MedicationRequest resource as declared by the Select Medical FHIR server CapabilityStatement. Declared US Core profiles: us-core-medicationrequest|6.1.0.'
  name: Select Medical Holdings Medication Request API
  slug: select-medical-holdings-medication-request-api
- baseURL: https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/DSTU2
  baseurl_source: declared
  description: 'FHIR R4 PractitionerRole resource as declared by the Select Medical FHIR server CapabilityStatement. Declared US Core profiles: us-core-practitionerrole|6.1.0.'
  name: Select Medical Holdings Practitioner Role API
  slug: select-medical-holdings-practitioner-role-api
artifact_total: 69
common:
- group: other
  href: https://artifacts.apis.io/select-medical-holdings/capabilities/select-medical-holdings-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/select-medical-holdings-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.selectmedical.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/select-medical-holdings
- group: start
  title: ''
  type: SignUp
  url: https://mychart.selectmedical.com/MyChart/signup
- group: start
  title: ''
  type: Login
  url: https://mychart.selectmedical.com/MyChart/Authentication/Login
- group: agent
  href: https://artifacts.apis.io/select-medical-holdings/well-known/select-medical-holdings-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/select-medical-holdings-well-known.yml
- group: auth
  href: https://artifacts.apis.io/select-medical-holdings/authentication/select-medical-holdings-authentication.yml
  title: ''
  type: Authentication
  url: authentication/select-medical-holdings-authentication.yml
- group: auth
  href: https://artifacts.apis.io/select-medical-holdings/scopes/select-medical-holdings-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/select-medical-holdings-scopes.yml
- group: design
  href: https://artifacts.apis.io/select-medical-holdings/conformance/select-medical-holdings-conformance.yml
  title: ''
  type: Conformance
  url: conformance/select-medical-holdings-conformance.yml
- group: design
  href: https://artifacts.apis.io/select-medical-holdings/errors/select-medical-holdings-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/select-medical-holdings-problem-types.yml
- group: design
  href: https://artifacts.apis.io/select-medical-holdings/lifecycle/select-medical-holdings-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/select-medical-holdings-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/select-medical-holdings/conventions/select-medical-holdings-conventions.yml
  title: ''
  type: Conventions
  url: conventions/select-medical-holdings-conventions.yml
- group: design
  href: https://artifacts.apis.io/select-medical-holdings/data-model/select-medical-holdings-data-model.yml
  title: ''
  type: DataModel
  url: data-model/select-medical-holdings-data-model.yml
- group: auth
  href: https://artifacts.apis.io/select-medical-holdings/security/select-medical-holdings-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/select-medical-holdings-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/select-medical-holdings/llms/select-medical-holdings-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/select-medical-holdings-llms.txt
- group: commercial
  href: https://artifacts.apis.io/select-medical-holdings/plans/select-medical-holdings-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/select-medical-holdings-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/select-medical-holdings/rate-limits/select-medical-holdings-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/select-medical-holdings-rate-limits.yml
- group: build
  href: https://artifacts.apis.io/select-medical-holdings/packages/select-medical-holdings-packages.yml
  title: ''
  type: Packages
  url: packages/select-medical-holdings-packages.yml
- group: agent
  href: https://artifacts.apis.io/select-medical-holdings/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/select-medical-holdings/overlays/select-medical-holdings-fhir-r4-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/select-medical-holdings-fhir-r4-overlay.yaml
- group: other
  href: https://artifacts.apis.io/select-medical-holdings/fhir/select-medical-holdings-r4-capabilitystatement.json
  title: ''
  type: FHIR
  url: fhir/select-medical-holdings-r4-capabilitystatement.json
created: '2026-03-24'
description: Select Medical Holdings Corporation is one of the largest operators of specialty hospitals and outpatient rehabilitation clinics in the United States, running critical illness recovery hospitals, inpatient rehabilitation hospitals, outpatient rehabilitation clinics and occupational health centers across the country. Select Medical is not a software vendor and publishes no commercial developer program, but as a covered healthcare provider running Epic it operates a live HL7 FHIR R4 patient-access API — registered under "Select Medical" in Epic's public endpoint directory — that exposes 59 FHIR resource types behind SMART-on-FHIR OAuth 2.0, together with an Epic MyChart patient portal. This profile documents that regulated interoperability surface rather than a commercial API product.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/select-medical-holdings.png
layout: provider
modified: '2026-08-28'
name: Select Medical Holdings
nav: Providers
network: true
overview: 'Select Medical Holdings publishes 60 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Adverse Event API, Appointment API, and 57 more. Tagged areas include Healthcare, Hospitals, Rehabilitation, Patient Access, and FHIR.


  The Select Medical Holdings catalog on APIs.io includes 1 Spectral governance ruleset.


  Select Medical Holdings'' developer surface includes signup flow, authentication, and 19 more developer resources.'
plans:
- name: Select Medical Holdings Plans Pricing
  plan_count: 0
  slug: select-medical-holdings-plans-pricing
press:
- date: ''
  title: Select Medical Holdings Corporation (SEM) Q1 2026 ...
  url: https://seekingalpha.com/article/4897429-select-medical-holdings-corporation-sem-q1-2026-earnings-call-transcript
- date: ''
  title: SELECT MEDICAL HOLDINGS CORP SEC 10-K Report
  url: https://www.tradingview.com/news/tradingview:4c841f4ce399c:0-select-medical-holdings-corp-sec-10-k-report/
- date: ''
  title: Select Medical Holdings Corporation to be Acquired by ...
  url: https://www.prnewswire.com/news-releases/select-medical-holdings-corporation-to-be-acquired-by-consortium-led-by-robert-a-ortenzio-martin-f-jackson-and-wcas-302701686.html
- date: ''
  title: Select Medical Holdings Corporation to Announce Second ...
  url: https://www.biospace.com/select-medical-holdings-corporation-to-announce-second-quarter-2019-results-on-thursday-august-1
- date: ''
  title: Select Medical Holdings Corporation Announces ...
  url: https://www.prnewswire.com/news-releases/select-medical-holdings-corporation-announces-expiration-of-hart-scott-rodino-waiting-period-302756311.html
random_paper: 1
rate_limits:
- limit_count: 0
  name: Select Medical Holdings Rate Limits
  slug: select-medical-holdings-rate-limits
rules:
- authorship: generated
  effective_rule_count: 120
  extends:
  - spectral:oas
  name: Select Medical Holdings API Rules
  rule_count: 79
  severity_counts:
    error: 72
    hint: 0
    info: 3
    warn: 4
  slug: select-medical-holdings-rules
scopes:
- name: Select Medical Holdings Scopes
  scope_count: 5
  slug: select-medical-holdings-scopes
  summary_line: 5 scopes
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 26
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    contract_governance: 31.8
    contract_quality: 53.1
    developer_ergonomics: 13.7
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 32.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 59
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/select-medical-holdings/select-medical-holdings-2026-10-11T125655.png
security:
- kind: authentication
  name: Select Medical Holdings Authentication
  slug: select-medical-holdings-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Select Medical Holdings Domain Security
  slug: select-medical-holdings-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: select-medical-clinical-document-retrieval
  slug: select-medical-holdings-clinical-document-retrieval
- name: select-medical-patient-clinical-summary
  slug: select-medical-holdings-patient-clinical-summary
- name: select-medical-write-safety
  slug: select-medical-holdings-write-safety
slug: select-medical-holdings
tags:
- Healthcare
- Hospitals
- Rehabilitation
- Patient Access
- FHIR
- Interoperability
- Electronic Health Records
- Fortune 1000
website: https://www.selectmedical.com
---

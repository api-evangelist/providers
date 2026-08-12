---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.2
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Modernizing Medicine Agentic Access
  operation_count: 125
  slug: modernizing-medicine-agentic-access
  summary_line: 125 operations · 20 acting
api_count: 43
apis:
- description: 'The AllergyIntolerance FHIR resource type<br/>Base profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-allergyintolerance'
  name: ModMed Allergy Intolerance API
  slug: modernizing-medicine-allergyintolerance-api
- description: Appoitments and Slots Details
  name: ModMed Appointments and Slots API
  slug: modernizing-medicine-appointments-and-slots-api
- description: SMART-on-FHIR OAuth 2.0 endpoints.
  name: ModMed Authentication API
  slug: modernizing-medicine-authentication-api
- description: Capability Statement
  name: ModMed Capability Statement API
  slug: modernizing-medicine-capability-statement-api
- description: 'The CarePlan FHIR resource type<br/>Base profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-careplan'
  name: ModMed Care Plan API
  slug: modernizing-medicine-careplan-api
- description: 'The CareTeam FHIR resource type<br/>Base profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-careteam'
  name: ModMed Care Team API
  slug: modernizing-medicine-careteam-api
- description: Charges/Financial details
  name: ModMed Charges/Financial API
  slug: modernizing-medicine-charges-financial-api
- description: Clinical Data/Clipboard details
  name: ModMed Clinical Data/Clipboard API
  slug: modernizing-medicine-clinical-data-clipboard-api
- description: 'The Condition FHIR resource type<br/>Base profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-condition'
  name: ModMed Condition API
  slug: modernizing-medicine-condition-api
- description: 'The Coverage FHIR resource type<br/>Base profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-coverage'
  name: ModMed Coverage API
  slug: modernizing-medicine-coverage-api
- description: 'The Device FHIR resource type<br/>Base profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-implantable-device'
  name: ModMed Device API
  slug: modernizing-medicine-device-api
- description: The DiagnosticReport FHIR resource type
  name: ModMed Diagnostic Report API
  slug: modernizing-medicine-diagnosticreport-api
- description: 'The DocumentReference FHIR resource type<br/>Base profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-documentreference'
  name: ModMed Document Reference API
  slug: modernizing-medicine-documentreference-api
- description: Documents details
  name: ModMed Documents API
  slug: modernizing-medicine-documents-api
- description: 'The Encounter FHIR resource type<br/>Base profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-encounter'
  name: ModMed Encounter API
  slug: modernizing-medicine-encounter-api
- description: Encounters/Visits details
  name: ModMed Encounters/Visits API
  slug: modernizing-medicine-encounters-visits-api
- description: The Endpoint FHIR resource type
  name: ModMed Endpoint API
  slug: modernizing-medicine-endpoint-api
- description: 'The Goal FHIR resource type<br/>Base profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-goal'
  name: ModMed Goal API
  slug: modernizing-medicine-goal-api
- description: The Group FHIR resource type
  name: ModMed Group API
  slug: modernizing-medicine-group-api
- description: 'The Immunization FHIR resource type<br/>Base profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-immunization'
  name: ModMed Immunization API
  slug: modernizing-medicine-immunization-api
- description: Insurance Details
  name: ModMed Insurance API
  slug: modernizing-medicine-insurance-api
- description: 'The Location FHIR resource type<br/>Base profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-location'
  name: ModMed Location API
  slug: modernizing-medicine-location-api
- description: Locations/Facilities details
  name: ModMed Locations/Facilities API
  slug: modernizing-medicine-locations-facilities-api
- description: 'The Medication FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Medication'
  name: ModMed Medication API
  slug: modernizing-medicine-medication-api
- description: The MedicationDispense API from ModMed — 2 operation(s) for medicationdispense.
  name: ModMed Medication Dispense API
  slug: modernizing-medicine-medicationdispense-api
- description: 'The MedicationRequest FHIR resource type<br/>Base profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-medicationrequest'
  name: ModMed Medication Request API
  slug: modernizing-medicine-medicationrequest-api
- description: The Observation FHIR resource type
  name: ModMed Observation API
  slug: modernizing-medicine-observation-api
- description: 'The OperationDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/OperationDefinition'
  name: ModMed Operation Definition API
  slug: modernizing-medicine-operationdefinition-api
- description: 'The Organization FHIR resource type<br/>Base profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-organization'
  name: ModMed Organization API
  slug: modernizing-medicine-organization-api
- description: 'The Patient FHIR resource type<br/>Base profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient'
  name: ModMed Patient API
  slug: modernizing-medicine-patient-api
- description: 'The Practitioner FHIR resource type<br/>Base profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitioner'
  name: ModMed Practitioner API
  slug: modernizing-medicine-practitioner-api
- description: 'The PractitionerRole FHIR resource type<br/>Base profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitionerrole'
  name: ModMed Practitioner Role API
  slug: modernizing-medicine-practitionerrole-api
- description: 'The Procedure FHIR resource type<br/>Base profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-procedure'
  name: ModMed Procedure API
  slug: modernizing-medicine-procedure-api
- description: 'The Provenance FHIR resource type<br/>Base profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-provenance'
  name: ModMed Provenance API
  slug: modernizing-medicine-provenance-api
- description: Providers details
  name: ModMed Providers and Referring Providers API
  slug: modernizing-medicine-providers-and-referring-providers-api
- description: The Questionnaire API from ModMed — 2 operation(s) for questionnaire.
  name: ModMed Questionnaire API
  slug: modernizing-medicine-questionnaire-api
- description: The QuestionnaireResponse API from ModMed — 2 operation(s) for questionnaireresponse.
  name: ModMed Questionnaire Response API
  slug: modernizing-medicine-questionnaireresponse-api
- description: The RelatedPerson API from ModMed — 2 operation(s) for relatedperson.
  name: ModMed Related Person API
  slug: modernizing-medicine-relatedperson-api
- description: 'The ServiceRequest FHIR resource type<br/>Base profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-servicerequest'
  name: ModMed Service Request API
  slug: modernizing-medicine-servicerequest-api
- description: The Specimen API from ModMed — 2 operation(s) for specimen.
  name: ModMed Specimen API
  slug: modernizing-medicine-specimen-api
- description: Tasks/Recalls Details
  name: ModMed Tasks/Recalls API
  slug: modernizing-medicine-tasks-recalls-api
- description: Transcription details
  name: ModMed Transcription API
  slug: modernizing-medicine-transcription-api
- description: The ValueSet FHIR resource type
  name: ModMed Value Set API
  slug: modernizing-medicine-valueset-api
artifact_total: 50
common:
- group: company
  title: ''
  type: Website
  url: https://www.modmed.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.api.modmed.com/
- group: docs
  title: ''
  type: Documentation
  url: https://portal.api.modmed.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://portal.api.modmed.com/reference/getting-started-2
- group: start
  title: ''
  type: GettingStarted
  url: https://portal.api.modmed.com/docs/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://www.modmed.com/synapsys/developers/
- group: operate
  title: ''
  type: Support
  url: https://www.modmed.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.modmed.com/resources/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.modmed.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.modmed.com/privacy-policy/
- group: other
  title: ''
  type: Marketplace
  url: https://modmed.my.site.com/synapsysmarketplace/s/
- group: auth
  title: ''
  type: Authentication
  url: authentication/modernizing-medicine-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/modernizing-medicine-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/modernizing-medicine-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/modernizing-medicine-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/modernizing-medicine-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/modernizing-medicine-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://portal.api.modmed.com/reference/authentication-1
- group: design
  title: ''
  type: Conformance
  url: conformance/modernizing-medicine-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.modmed.com/onc-certification/
- group: design
  title: ''
  type: DataModel
  url: data-model/modernizing-medicine-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/modernizing-medicine-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/modernizing-medicine-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/modernizing-medicine-security.txt
- group: other
  title: ''
  type: APICatalog
  url: https://mm-fhir-endpoint-display.prod.fhir.ema-api.com/
- group: auth
  title: ''
  type: Security
  url: https://www.modmed.com/security/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/modernizing-medicine-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/modernizing-medicine-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/modernizing-medicine-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/modernizing-medicine-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/modernizing-medicine-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/modernizing-medicine-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/modernizing-medicine-ema-proprietary-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/modernizing-medicine-certified-fhir-api-overlay.yaml
created: '2026-08-04'
description: 'ModMed (Modernizing Medicine, Inc., Boca Raton FL) builds specialty-specific cloud healthcare software — the EMA electronic health record, ModMed Practice Management, gGastro for gastroenterology, analytics, revenue cycle management and telehealth — for allergy, dermatology, ENT, gastroenterology, OBGYN, ophthalmology, orthopedics, pain management, plastic surgery, podiatry and urology practices. It publishes two public APIs from one developer portal at portal.api.modmed.com: the EMA Proprietary API, a FHIR R4-style read/write interface under /fhir/v2 covering patients, appointments, slots, coverage, charges, documents and clinical data for synapSYS Marketplace vendors; and the ModMed Certified FHIR API, an ONC-certified HL7 FHIR R4 / US Core read-and-search interface with SMART on FHIR app launch and Bulk FHIR NDJSON export across EMA, ModMed PM, ModMed GI and gGastro. Customer FHIR service base URLs are published publicly as required by the 21st Century Cures Act.'
image: https://www.modmed.com/wp-content/uploads/2024/12/cropped-mm-favicon_512-270x270.png
layout: provider
mcp_servers:
- description: ''
  name: modernizing-medicine-mcp.yml
  slug: modernizing-medicine-mcpyml
modified: '2026-08-04'
name: ModMed
nav: Providers
network: true
overview: 'ModMed publishes 43 APIs on the [APIs.io](https://apis.io/) network, including Allergy Intolerance API, Appointments and Slots API, Authentication API, and 40 more. Tagged areas include Company, Healthcare, Electronic Health Records, Practice Management, and FHIR.


  ModMed''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, authentication, and 28 more developer resources.'
random_paper: 93
rate_limits:
- limit_count: 2
  name: Modernizing Medicine Rate Limits
  slug: modernizing-medicine-rate-limits
scopes:
- name: Modernizing Medicine Scopes
  scope_count: 76
  slug: modernizing-medicine-scopes
  summary_line: 76 scopes · authorizationCode
score:
  band: developing
  composite: 54.5
  delta: -3.9
  facets:
    commercial_clarity: 42.1
    contract_quality: 57.4
    developer_ergonomics: 69.0
    discoverability: 68.5
    governance: 20.8
    operational_transparency: 39.5
  previous_composite: 58.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 43
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 73.8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/modernizing-medicine/refs/heads/main/screenshots/modernizing-medicine-2026-08-07T184015.png
security:
- kind: authentication
  name: Modernizing Medicine Authentication
  slug: modernizing-medicine-authentication
  summary_line: apiKey/http/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Modernizing Medicine Domain Security
  slug: modernizing-medicine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Modernizing Medicine Vulnerability Disclosure
  slug: modernizing-medicine-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: modernizing-medicine
tags:
- Company
- Healthcare
- Electronic Health Records
- Practice Management
- FHIR
- Health IT
- Interoperability
- Medical Billing
- SMART on FHIR
- Telehealth
website: https://www.modmed.com/
---

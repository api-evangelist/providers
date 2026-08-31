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
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Varian Medical Systems Agentic Access
  operation_count: 16
  slug: varian-medical-systems-agentic-access
  summary_line: 16 operations
api_count: 1
apis:
- description: The legacy ARIA Access API provides SOAP and REST access to core ARIA entities including patients, appointments, prescriptions, treatment plans, orders, and administrative data. Deployed on-premise wi
  name: ARIA Access API
  slug: aria-access-api
- description: Patient allergy and intolerance records
  name: Varian Medical Systems AllergyIntolerance API
  slug: varian-medical-systems-allergyintolerance-api
- description: Oncology treatment and care plans
  name: Varian Medical Systems CarePlan API
  slug: varian-medical-systems-careplan-api
- description: Cancer diagnoses and clinical conditions
  name: Varian Medical Systems Condition API
  slug: varian-medical-systems-condition-api
- description: Pathology, imaging, and treatment reports
  name: Varian Medical Systems DiagnosticReport API
  slug: varian-medical-systems-diagnosticreport-api
- description: Clinical document management
  name: Varian Medical Systems DocumentReference API
  slug: varian-medical-systems-documentreference-api
- description: Treatment goals and objectives
  name: Varian Medical Systems Goal API
  slug: varian-medical-systems-goal-api
- description: Chemotherapy and medication prescriptions
  name: Varian Medical Systems MedicationRequest API
  slug: varian-medical-systems-medicationrequest-api
- description: FHIR server capability and metadata
  name: Varian Medical Systems Metadata API
  slug: varian-medical-systems-metadata-api
- description: Labs, vitals, and clinical measurements
  name: Varian Medical Systems Observation API
  slug: varian-medical-systems-observation-api
- description: Oncology patient demographics and identifiers
  name: Varian Medical Systems Patient API
  slug: varian-medical-systems-patient-api
- description: Radiation therapy and other clinical procedures
  name: Varian Medical Systems Procedure API
  slug: varian-medical-systems-procedure-api
artifact_total: 39
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Varian ARIA FHIR API
  slug: open-varian-aria-fhir
- collection_type: open
  name: Varian ARIA FHIR AllergyIntolerance API
  slug: open-varian-medical-systems-allergyintolerance-api
- collection_type: open
  name: Varian ARIA FHIR AllergyIntolerance CarePlan API
  slug: open-varian-medical-systems-careplan-api
- collection_type: open
  name: Varian ARIA FHIR AllergyIntolerance Condition API
  slug: open-varian-medical-systems-condition-api
- collection_type: open
  name: Varian ARIA FHIR AllergyIntolerance DiagnosticReport API
  slug: open-varian-medical-systems-diagnosticreport-api
- collection_type: open
  name: Varian ARIA FHIR AllergyIntolerance DocumentReference API
  slug: open-varian-medical-systems-documentreference-api
- collection_type: open
  name: Varian ARIA FHIR AllergyIntolerance Goal API
  slug: open-varian-medical-systems-goal-api
- collection_type: open
  name: Varian ARIA FHIR AllergyIntolerance MedicationRequest API
  slug: open-varian-medical-systems-medicationrequest-api
- collection_type: open
  name: Varian ARIA FHIR AllergyIntolerance Metadata API
  slug: open-varian-medical-systems-metadata-api
- collection_type: open
  name: Varian ARIA FHIR AllergyIntolerance Observation API
  slug: open-varian-medical-systems-observation-api
- collection_type: open
  name: Varian ARIA FHIR AllergyIntolerance Patient API
  slug: open-varian-medical-systems-patient-api
- collection_type: open
  name: Varian ARIA FHIR AllergyIntolerance Procedure API
  slug: open-varian-medical-systems-procedure-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/varian-medical-systems-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/varian-medical-systems-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/varian-medical-systems-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/varian-medical-systems-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/varian-medical-systems
- group: start
  title: ''
  type: Portal
  url: https://varian.dynamicfhir.com/varian/basepractice/r4
- group: docs
  title: ''
  type: Documentation
  url: https://varian.dynamicfhir.com/varian/basepractice/r4/Home/ApiDocumentation
- group: other
  title: ''
  type: CapabilityStatement
  url: https://varian.dynamicfhir.com/fhir/varian/basepractice/r4/metadata
- group: docs
  title: ''
  type: Documentation
  url: https://www.gatewayscripts.com/post/webinars-revisited-a-review-of-aria-apis
- group: other
  title: ''
  type: Product
  url: https://cancercare.siemens-healthineers.com/products/software/digital-oncology/oncology-management-systems/aria-oncology-information-system
- group: company
  title: ''
  type: Website
  url: https://www.varian.com
- group: company
  title: ''
  type: Website
  url: https://cancercare.siemens-healthineers.com
- group: other
  title: ''
  type: Standards
  url: https://hl7.org/fhir/R4/
- group: other
  title: ''
  type: Standards
  url: https://www.dicomstandard.org
created: '2026-05-03'
description: Varian Medical Systems is a leading manufacturer of medical devices and software for treating cancer with radiotherapy, radiosurgery, proton therapy, and brachytherapy. Acquired by Siemens Healthineers in 2021, Varian provides the ARIA Oncology Information System (OIS) and developer APIs enabling integration with clinical workflows, EHR systems, and the broader healthcare ecosystem using HL7, DICOM, and FHIR standards.
examples:
- key_count: 2
  name: Varian Search Conditions Example
  slug: varian-search-conditions-example
- key_count: 2
  name: Varian Search Patients Example
  slug: varian-search-patients-example
finops:
- name: Varian Medical Systems Finops
  service_category: Healthcare
  slug: varian-medical-systems-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/varian-medical-systems.png
json_schemas:
- name: Varian ARIA Patient
  property_count: 10
  slug: varian-patient
json_structures:
- name: Varian Patient Structure
  property_count: 0
  slug: varian-patient-structure
jsonld:
- class_count: 15
  name: Varian Medical Systems Context
  property_count: 20
  slug: varian-medical-systems-context
layout: provider
modified: '2026-05-19'
name: Varian Medical Systems
nav: Providers
network: true
overview: 'Varian Medical Systems publishes 11 APIs on the [APIs.io](https://apis.io/) network, including AllergyIntolerance API, CarePlan API, Condition API, and 8 more. Tagged areas include Healthcare, Oncology, Medical Devices, FHIR, and Radiation Therapy.


  The Varian Medical Systems catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Varian Medical Systems'' developer surface includes authentication, developer portal, documentation, and 11 more developer resources.'
plans:
- name: Varian Medical Systems Plans Pricing
  plan_count: 1
  slug: varian-medical-systems-plans-pricing
press:
- date: '2026-05-25'
  title: Telix Pharmaceuticals Enters Strategic Collaboration with ...
  url: https://telixpharma.com/news-views/telix-pharmaceuticals-enters-strategic-collaboration-with-varian-medical-systems-for-advanced-prostate-imaging/
- date: '2026-05-25'
  title: Varian Medical Systems Invests in COTA, Inc. to Help Drive ...
  url: https://www.prnewswire.com/news-releases/varian-medical-systems-invests-in-cota-inc-to-help-drive-faster-more-accurate-data-driven-cancer-care-301169528.html
- date: '2026-05-25'
  title: Siemens Healthineers completes acquisition of Varian ...
  url: https://www.siemens-healthineers.com/press/releases/varian-closing
- date: '2026-05-25'
  title: Varian Medical Systems
  url: https://www.itnonline.com/company/varian-medical-systems-0
- date: '2026-05-25'
  title: AI-Enabled Radiation Therapy System & 1,000th Patient
  url: https://siteman.wustl.edu/ai-enabled-radiation-therapy-system-at-siteman/
random_paper: 16
rate_limits:
- limit_count: 1
  name: Varian Medical Systems Rate Limits
  slug: varian-medical-systems-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Varian Medical Systems API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: varian-medical-systems-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Varian Medical Systems API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 5
  slug: varian-rules
scopes:
- name: Varian Medical Systems Scopes
  scope_count: 11
  slug: varian-medical-systems-scopes
  summary_line: 11 scopes · authorizationCode
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 19
    catalog_gap: 60.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 13.6
    contract_quality: 64.4
    developer_ergonomics: 31.0
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 5.3
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 42.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/varian-medical-systems/refs/heads/main/screenshots/varian-medical-systems-2026-06-20T200814.png
security:
- kind: authentication
  name: Varian Medical Systems Authentication
  slug: varian-medical-systems-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Varian Medical Systems Domain Security
  slug: varian-medical-systems-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: varian-medical-systems
tags:
- Healthcare
- Oncology
- Medical Devices
- FHIR
- Radiation Therapy
- Health IT
- Fortune 1000
website: https://www.varian.com
---

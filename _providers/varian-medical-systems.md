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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Varian Medical Systems Agentic Access
  operation_count: 16
  slug: varian-medical-systems-agentic-access
  summary_line: 16 operations
api_count: 12
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
artifact_total: 27
collections:
- collection_type: open
  name: Varian ARIA FHIR API
  slug: open-varian-aria-fhir
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
random_paper: 55
rate_limits:
- limit_count: 1
  name: Varian Medical Systems Rate Limits
  slug: varian-medical-systems-rate-limits
rules:
- name: Varian Medical Systems API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: varian-medical-systems-jsonschema-spectral-rules
- name: Varian Medical Systems API Rules
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
  band: developing
  composite: 45.0
  delta: -5.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 70.9
    developer_ergonomics: 28.3
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 50.6
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
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
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

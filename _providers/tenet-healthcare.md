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
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Tenet Healthcare Agentic Access
  operation_count: 7
  slug: tenet-healthcare-agentic-access
  summary_line: 7 operations
api_count: 8
apis:
- description: Revenue cycle management API from Conifer Health Solutions, a Tenet Healthcare subsidiary providing end-to-end RCM services including patient access, health information management, patient financial s
  name: Conifer Health Solutions Revenue Cycle API
  slug: conifer-health-solutions-revenue-cycle-api
- description: 'United Surgical Partners International (USPI) integration APIs for ambulatory surgery center scheduling, patient registration, procedure management, and clinical data exchange. USPI operates over 600 '
  name: USPI Ambulatory Surgery Center API
  slug: uspi-ambulatory-surgery-center-api
- description: Healthcare appointment scheduling and management (FHIR Appointment resource)
  name: Tenet Healthcare Appointments API
  slug: tenet-healthcare-appointments-api
- description: Patient diagnoses, problems, and health concerns (FHIR Condition resource)
  name: Tenet Healthcare Conditions API
  slug: tenet-healthcare-conditions-api
- description: Clinical document references and summaries (FHIR DocumentReference resource)
  name: Tenet Healthcare Documents API
  slug: tenet-healthcare-documents-api
- description: Medication prescriptions and administration records (FHIR MedicationRequest resource)
  name: Tenet Healthcare Medications API
  slug: tenet-healthcare-medications-api
- description: Clinical observations including vital signs, lab results, and assessments (FHIR Observation resource)
  name: Tenet Healthcare Observations API
  slug: tenet-healthcare-observations-api
- description: Patient demographic and administrative information (FHIR Patient resource)
  name: Tenet Healthcare Patients API
  slug: tenet-healthcare-patients-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tenet Healthcare FHIR R4 Patient Appointments API
  slug: open-tenet-healthcare-appointments-api
- collection_type: open
  name: Tenet Healthcare FHIR R4 Patient Appointments Conditions API
  slug: open-tenet-healthcare-conditions-api
- collection_type: open
  name: Tenet Healthcare FHIR R4 Patient Appointments Documents API
  slug: open-tenet-healthcare-documents-api
- collection_type: open
  name: Tenet Healthcare FHIR R4 Patient API
  slug: open-tenet-healthcare-fhir
- collection_type: open
  name: Tenet Healthcare FHIR R4 Patient Appointments Medications API
  slug: open-tenet-healthcare-medications-api
- collection_type: open
  name: Tenet Healthcare FHIR R4 Patient Appointments Observations API
  slug: open-tenet-healthcare-observations-api
- collection_type: open
  name: Tenet Healthcare FHIR R4 Patient Appointments Patients API
  slug: open-tenet-healthcare-patients-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tenet-healthcare-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tenet-healthcare-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tenet-healthcare-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tenet-healthcare-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tenet-healthcare
- group: company
  title: ''
  type: Website
  url: https://www.tenethealth.com
- group: company
  title: ''
  type: Website
  url: https://www.tenetcorporate.com
- group: company
  title: ''
  type: Investor Relations
  url: https://ir.tenethealth.com
- group: company
  title: ''
  type: Press Room
  url: https://www.tenethealth.com/news
- group: company
  title: ''
  type: Careers
  url: https://careers.tenethealth.com
- group: other
  title: ''
  type: Conifer Health Solutions
  url: https://www.coniferhealth.com
- group: other
  title: ''
  type: USPI
  url: https://www.uspi.com
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tenet-healthcare-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tenet-healthcare-patient-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tenet-healthcare-appointment-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/tenet-healthcare-patient-structure.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/tenet-healthcare-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tenet-healthcare-vocabulary.yml
created: '2026-03-21'
description: Tenet Healthcare is a diversified healthcare services company and Fortune 500 organization operating regionally focused, integrated healthcare delivery networks. The company operates acute care hospitals, ambulatory surgery centers (ASCs), and physician practices across the United States through United Surgical Partners International (USPI) and Tenet Health. Tenet also provides revenue cycle management services through Conifer Health Solutions.
examples:
- key_count: 2
  name: Tenet Healthcare Get Patient Example
  slug: tenet-healthcare-get-patient-example
- key_count: 2
  name: Tenet Healthcare List Appointments Example
  slug: tenet-healthcare-list-appointments-example
finops:
- name: Tenet Healthcare Finops
  service_category: Healthcare
  slug: tenet-healthcare-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tenet-healthcare.png
json_schemas:
- name: Tenet Healthcare Appointment
  property_count: 12
  slug: tenet-healthcare-appointment
- name: Tenet Healthcare Patient
  property_count: 13
  slug: tenet-healthcare-patient
json_structures:
- name: Tenet Healthcare Patient Structure
  property_count: 0
  slug: tenet-healthcare-patient-structure
jsonld:
- class_count: 10
  name: Tenet Healthcare Context
  property_count: 12
  slug: tenet-healthcare-context
layout: provider
modified: '2026-05-19'
name: Tenet Healthcare
nav: Providers
network: true
overview: 'Tenet Healthcare publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Appointments API, Conditions API, Documents API, and 3 more. Tagged areas include Healthcare, Hospitals, Ambulatory Surgery Centers, Revenue Cycle Management, and Fortune 500.


  The Tenet Healthcare catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tenet Healthcare''s developer surface includes authentication and 17 more developer resources.'
plans:
- name: Tenet Healthcare Plans Pricing
  plan_count: 1
  slug: tenet-healthcare-plans-pricing
press:
- date: '2026-05-25'
  title: Tenet to deploy Commure's AI scribe at physician network
  url: https://www.healthcaredive.com/news/tenet-deploys-commure-ai-scribe-physician-network/733663/
- date: '2026-05-25'
  title: Press Release issued on February
  url: https://www.sec.gov/Archives/edgar/data/70318/000007031826000003/thc-20260202exh991.htm
- date: '2026-05-25'
  title: '#WhatsUpTenet Here''s the latest across Tenet Healthcare''s ...'
  url: https://www.facebook.com/tenetglobalbusinesscenter/posts/whatsuptenet-heres-the-latest-across-tenet-healthcares-network-gbcs-mother-compa/905654302216243/
- date: '2026-05-25'
  title: Tenet Announces Accretive Transaction and Previews ...
  url: https://investor.tenethealth.com/press-releases/press-release-details/2026/Tenet-Announces-Accretive-Transaction-and-Previews-Strong-2025-Results/default.aspx
- date: '2026-05-25'
  title: Artificial Intelligence at Tenet Healthcare
  url: https://emerj.com/artificial-intelligence-at-tenet-healthcare/
random_paper: 140
rate_limits:
- limit_count: 1
  name: Tenet Healthcare Rate Limits
  slug: tenet-healthcare-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tenet Healthcare API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tenet-healthcare-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Tenet Healthcare API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 0
    info: 3
    warn: 5
  slug: tenet-healthcare-rules
scopes:
- name: Tenet Healthcare Scopes
  scope_count: 6
  slug: tenet-healthcare-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: thin
  composite: 36.3
  delta: -3.1
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 25.0
    contract_quality: 66.4
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 5.3
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 42.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tenet-healthcare/refs/heads/main/screenshots/tenet-healthcare-2026-06-20T195114.png
security:
- kind: authentication
  name: Tenet Healthcare Authentication
  slug: tenet-healthcare-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Tenet Healthcare Domain Security
  slug: tenet-healthcare-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: tenet-healthcare
tags:
- Healthcare
- Hospitals
- Ambulatory Surgery Centers
- Revenue Cycle Management
- Fortune 500
website: https://www.tenethealth.com
---

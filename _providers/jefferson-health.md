---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Jefferson Health Agentic Access
  operation_count: 21
  slug: jefferson-health-agentic-access
  summary_line: 21 operations
api_count: 19
apis:
- description: The legacy Thomas Jefferson University Hospital DSTU2 FHIR endpoint listed in Epic's public R4 endpoint registry under the organization "Jefferson Health". It remains available for backward compatibil
  name: Thomas Jefferson University Hospital FHIR DSTU2 API
  slug: tjuh-fhir-dstu2-api
- description: 'The Jefferson Health Plans (formerly Health Partners Plans) Patient Access FHIR API exposes adjudicated claims, encounter data from providers, formulary data, and certain clinical data to JHP members '
  name: Jefferson Health Plans Patient Access FHIR API
  slug: jhp-patient-access-fhir-api
- description: MyJeffersonHealth is the patient-facing Epic MyChart deployment used by Jefferson Health patients to view test results, message providers, request prescription renewals, schedule appointments, pay bil
  name: MyJeffersonHealth MyChart Patient Portal
  slug: myjeffersonhealth-mychart
- description: Risk of harmful or undesirable physiological response to a substance.
  name: Jefferson Health Allergy Intolerance API
  slug: jefferson-health-allergy-intolerance-api
- description: HL7 FHIR Bulk Data Access Group-level export.
  name: Jefferson Health Bulk Data API
  slug: jefferson-health-bulk-data-api
- description: Detailed information about conditions, problems, or diagnoses.
  name: Jefferson Health Condition API
  slug: jefferson-health-condition-api
- description: A reference to a document, often a CCDA or clinical note.
  name: Jefferson Health Document Reference API
  slug: jefferson-health-document-reference-api
- description: An interaction between a patient and healthcare provider(s).
  name: Jefferson Health Encounter API
  slug: jefferson-health-encounter-api
- description: The technical details of an endpoint that can be used for electronic services.
  name: Jefferson Health Endpoint API
  slug: jefferson-health-endpoint-api
- description: The details of a healthcare service available at a location.
  name: Jefferson Health Healthcare Service API
  slug: jefferson-health-healthcare-service-api
- description: Details of a Health Insurance product/plan provided by an organization.
  name: Jefferson Health Insurance Plan API
  slug: jefferson-health-insurance-plan-api
- description: Details and position information for a physical place.
  name: Jefferson Health Location API
  slug: jefferson-health-location-api
- description: An order or request for both supply of the medication and the instructions for administration.
  name: Jefferson Health Medication Request API
  slug: jefferson-health-medication-request-api
- description: FHIR conformance discovery.
  name: Jefferson Health Metadata API
  slug: jefferson-health-metadata-api
- description: Measurements and simple assertions made about a patient.
  name: Jefferson Health Observation API
  slug: jefferson-health-observation-api
- description: A formally or informally recognized grouping of people or organizations.
  name: Jefferson Health Organization API
  slug: jefferson-health-organization-api
- description: Demographics and other administrative information about an individual receiving care.
  name: Jefferson Health Patient API
  slug: jefferson-health-patient-api
- description: A person who is directly or indirectly involved in the provisioning of healthcare.
  name: Jefferson Health Practitioner API
  slug: jefferson-health-practitioner-api
- description: A specific set of roles a practitioner may perform at an organization for a period of time.
  name: Jefferson Health Practitioner Role API
  slug: jefferson-health-practitioner-role-api
artifact_total: 41
collections:
- collection_type: open
  name: Jefferson Health Plans Provider Directory FHIR API
  slug: open-jefferson-health-jhp-provider-directory-fhir-api
- collection_type: open
  name: Thomas Jefferson University Hospital FHIR R4 API
  slug: open-jefferson-health-tjuh-fhir-r4-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jefferson-health-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jefferson-health-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jefferson-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/jefferson-health-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.jeffersonhealth.org/
- group: start
  title: ''
  type: PatientPortal
  url: https://my.jeffersonhealth.org/
- group: start
  title: ''
  type: PatientPortal
  url: https://mychart.jefferson.edu/
- group: other
  title: ''
  type: MyChartCentral
  url: https://www.jeffersonhealth.org/your-health/my-jefferson-health/mychart-central
- group: other
  title: ''
  type: Locations
  url: https://www.jeffersonhealth.org/locations
- group: commercial
  title: ''
  type: PriceTransparency
  url: https://www.jeffersonhealth.org/pay-my-bill/charge-description
- group: commercial
  title: ''
  type: PriceEstimator
  url: https://www.jeffersonhealth.org/pay-my-bill/price-estimator
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jeffersonhealth.org/about-us/notice-of-privacy-practices
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jeffersonhealth.org/terms-of-use
- group: other
  title: ''
  type: University
  url: https://www.jefferson.edu/
- group: commercial
  title: ''
  type: HealthPlans
  url: https://www.jeffersonhealthplans.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.cms.gov/Regulations-and-Guidance/Guidance/Interoperability/index
- group: auth
  title: ''
  type: Compliance
  url: https://www.healthit.gov/curesrule/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/jefferson-health-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/jefferson-health-vocabulary.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/jefferson-health-patient-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/jefferson-health-observation-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/jefferson-health-practitioner-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/jefferson-health-fhir-encounter-structure.json
- group: commercial
  title: ''
  type: Plans
  url: plans/jefferson-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jefferson-health-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/jefferson-health-finops.yml
created: '2026-05-23'
description: Jefferson Health is a multi-state nonprofit academic health system based in Philadelphia, Pennsylvania, operating more than 30 hospitals and over 700 care sites across eastern Pennsylvania and southern New Jersey as the clinical arm of the broader Jefferson enterprise that also includes Thomas Jefferson University and Jefferson Health Plans (formerly Health Partners Plans). Its patient-facing electronic health record runs on Epic and is branded as MyJeffersonHealth / MyChart, with a CMS-mandated HL7 FHIR R4 API published at fhir.jefferson.edu/FHIRProxy/api/FHIR/R4 that exposes USCDI-aligned clinical resources to third-party patient-access applications via SMART on FHIR and OAuth 2.0. Jefferson Health Plans separately exposes CARIN-aligned Patient Access and Da Vinci Plan-Net Provider Directory FHIR APIs powered by Smile CDR for its insurance members and the public.
examples:
- key_count: 2
  name: Jhp Provider Directory Organization Search Example
  slug: jhp-provider-directory-organization-search-example
- key_count: 2
  name: Jhp Provider Directory Practitioner Search Example
  slug: jhp-provider-directory-practitioner-search-example
- key_count: 2
  name: Tjuh Fhir R4 Observation Search Example
  slug: tjuh-fhir-r4-observation-search-example
- key_count: 2
  name: Tjuh Fhir R4 Patient Search Example
  slug: tjuh-fhir-r4-patient-search-example
- key_count: 2
  name: Tjuh Fhir R4 Smart Configuration Example
  slug: tjuh-fhir-r4-smart-configuration-example
finops:
- name: Jefferson Health Finops
  service_category: ''
  slug: jefferson-health-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jefferson-health.png
json_schemas:
- name: Jefferson Health FHIR R4 Observation (US Core Subset)
  property_count: 9
  slug: jefferson-health-observation
- name: Jefferson Health FHIR R4 Patient (US Core Subset)
  property_count: 7
  slug: jefferson-health-patient
- name: Jefferson Health Plans Plan-Net Practitioner
  property_count: 7
  slug: jefferson-health-practitioner
json_structures:
- name: Jefferson Health Fhir Encounter Structure
  property_count: 13
  slug: jefferson-health-fhir-encounter-structure
jsonld:
- class_count: 30
  name: Jefferson Health Context
  property_count: 0
  slug: jefferson-health-context
layout: provider
modified: '2026-05-23'
name: Jefferson Health
nav: Providers
network: true
overview: 'Jefferson Health publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Allergy Intolerance API, Bulk Data API, Condition API, and 13 more. Tagged areas include Academic Medical Center, CARIN Blue Button, CMS Interoperability, Cures Act, and Da Vinci Plan-Net.


  The Jefferson Health catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Jefferson Health''s developer surface includes authentication and 25 more developer resources.'
plans:
- name: Jefferson Health Plans Pricing
  plan_count: 4
  slug: jefferson-health-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 0
  name: Jefferson Health Rate Limits
  slug: jefferson-health-rate-limits
rules:
- name: Jefferson Health API Rules
  rule_count: 4
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 1
  slug: jefferson-health-jhp-provider-directory-fhir-rules
- name: Jefferson Health API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: jefferson-health-jsonschema-spectral-rules
- name: Jefferson Health API Rules
  rule_count: 8
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 3
  slug: jefferson-health-tjuh-fhir-r4-rules
scopes:
- name: Jefferson Health Scopes
  scope_count: 13
  slug: jefferson-health-scopes
  summary_line: 13 scopes · authorizationCode
score:
  band: developing
  composite: 44.3
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 60.9
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 31.3
    operational_transparency: 0.0
  previous_composite: 44.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jefferson-health/refs/heads/main/screenshots/jefferson-health-2026-06-20T183715.png
security:
- kind: authentication
  name: Jefferson Health Authentication
  slug: jefferson-health-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Jefferson Health Domain Security
  slug: jefferson-health-domain-security
  summary_line: TLSv1.3 · DMARC
slug: jefferson-health
tags:
- Academic Medical Center
- CARIN Blue Button
- CMS Interoperability
- Cures Act
- Da Vinci Plan-Net
- Epic
- FHIR
- HL7
- Healthcare
- Hospital System
- MyChart
- OAuth 2.0
- Patient Access
- Provider Directory
- SMART on FHIR
- US Core
- USCDI
website: https://www.jeffersonhealth.org/
---

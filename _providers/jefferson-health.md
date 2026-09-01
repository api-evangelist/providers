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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 36.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Jefferson Health Agentic Access
  operation_count: 21
  slug: jefferson-health-agentic-access
  summary_line: 21 operations
api_count: 2
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
artifact_total: 58
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Jefferson Health Plans Provider Directory FHIR Allergy Intolerance API
  slug: open-jefferson-health-allergy-intolerance-api
- collection_type: open
  name: Jefferson Health Plans Provider Directory FHIR Allergy Intolerance Bulk Data API
  slug: open-jefferson-health-bulk-data-api
- collection_type: open
  name: Jefferson Health Plans Provider Directory FHIR Allergy Intolerance Condition API
  slug: open-jefferson-health-condition-api
- collection_type: open
  name: Jefferson Health Plans Provider Directory FHIR Allergy Intolerance Document Reference API
  slug: open-jefferson-health-document-reference-api
- collection_type: open
  name: Jefferson Health Plans Provider Directory FHIR Allergy Intolerance Encounter API
  slug: open-jefferson-health-encounter-api
- collection_type: open
  name: Jefferson Health Plans Provider Directory FHIR Allergy Intolerance Endpoint API
  slug: open-jefferson-health-endpoint-api
- collection_type: open
  name: Jefferson Health Plans Provider Directory FHIR Allergy Intolerance Healthcare Service API
  slug: open-jefferson-health-healthcare-service-api
- collection_type: open
  name: Jefferson Health Plans Provider Directory FHIR Allergy Intolerance Insurance Plan API
  slug: open-jefferson-health-insurance-plan-api
- collection_type: open
  name: Jefferson Health Plans Provider Directory FHIR API
  slug: open-jefferson-health-jhp-provider-directory-fhir-api
- collection_type: open
  name: Jefferson Health Plans Provider Directory FHIR Allergy Intolerance Location API
  slug: open-jefferson-health-location-api
- collection_type: open
  name: Jefferson Health Plans Provider Directory FHIR Allergy Intolerance Medication Request API
  slug: open-jefferson-health-medication-request-api
- collection_type: open
  name: Jefferson Health Plans Provider Directory FHIR Allergy Intolerance Metadata API
  slug: open-jefferson-health-metadata-api
- collection_type: open
  name: Jefferson Health Plans Provider Directory FHIR Allergy Intolerance Observation API
  slug: open-jefferson-health-observation-api
- collection_type: open
  name: Jefferson Health Plans Provider Directory FHIR Allergy Intolerance Organization API
  slug: open-jefferson-health-organization-api
- collection_type: open
  name: Jefferson Health Plans Provider Directory FHIR Allergy Intolerance Patient API
  slug: open-jefferson-health-patient-api
- collection_type: open
  name: Jefferson Health Plans Provider Directory FHIR Allergy Intolerance Practitioner API
  slug: open-jefferson-health-practitioner-api
- collection_type: open
  name: Jefferson Health Plans Provider Directory FHIR Allergy Intolerance Practitioner Role API
  slug: open-jefferson-health-practitioner-role-api
- collection_type: open
  name: Thomas Jefferson University Hospital FHIR R4 API
  slug: open-jefferson-health-tjuh-fhir-r4-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/jefferson-health-capability-edges.yml
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
  url: https://www.jeffersonhealth.org/privacy-practices
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jeffersonhealth.org/privacy-practices/website-terms-of-use
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jeffersonhealth.org/terms-and-conditions
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
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jefferson-health-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/jefferson-health-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jefferson-health-conformance.yml
- group: other
  title: ''
  type: CapabilityStatement
  url: conformance/jefferson-health-tjuh-fhir-r4-capabilitystatement.json
- group: other
  title: ''
  type: CapabilityStatement
  url: conformance/jefferson-health-jhp-provider-directory-capabilitystatement.json
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/jefferson-health-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jefferson-health-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jefferson-health-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/jefferson-health-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/jefferson-health-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/jefferson-health-tjuh-fhir-r4-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/jefferson-health-jhp-provider-directory-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jefferson-health
- group: start
  title: ''
  type: DeveloperPortal
  url: https://appgallery.healthpartnersplans.com/app-gallery/portal/
- group: docs
  title: ''
  type: Documentation
  url: https://www.jeffersonhealthplans.com/home/about-us/interoperability/
- group: docs
  title: ''
  type: APIReference
  url: https://www.jeffersonhealthplans.com/home/about-us/interoperability/developer-resources/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.jeffersonhealthplans.com/home/about-us/interoperability/register-for-api-access.html
- group: start
  title: ''
  type: SignUp
  url: https://www.jeffersonhealthplans.com/home/about-us/interoperability/register-for-the-interoperability-portal.html
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.jeffersonhealthplans.com/home/about-us/interoperability/member-education-faq.html
- group: company
  title: ''
  type: Blog
  url: https://www.jeffersonhealth.org/your-health/living-well
- group: company
  title: ''
  type: News
  url: https://www.jeffersonhealth.org/about-us/news
- group: auth
  title: ''
  type: Compliance
  url: https://www.jeffersonhealth.org/about-us/corporate-compliance
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
modified: '2026-08-15'
name: Jefferson Health
nav: Providers
network: true
overview: 'Jefferson Health publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Allergy Intolerance API, Bulk Data API, Condition API, and 13 more. Tagged areas include Academic Medical Center, CARIN Blue Button, CMS Interoperability, Cures Act, and Da Vinci Plan-Net.


  The Jefferson Health catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Jefferson Health''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, engineering blog, product news, and 44 more developer resources.'
plans:
- name: Jefferson Health Plans Pricing
  plan_count: 4
  slug: jefferson-health-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Jefferson Health Rate Limits
  slug: jefferson-health-rate-limits
rules:
- effective_rule_count: 45
  extends:
  - spectral:oas
  name: Jefferson Health API Rules
  rule_count: 4
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 1
  slug: jefferson-health-jhp-provider-directory-fhir-rules
- effective_rule_count: 5
  extends: []
  name: Jefferson Health API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: jefferson-health-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Jefferson Health API Rules
  rule_count: 8
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 3
  slug: jefferson-health-tjuh-fhir-r4-rules
scopes:
- name: Jefferson Health Scopes
  scope_count: 15
  slug: jefferson-health-scopes
  summary_line: 15 scopes · authorizationCode
score:
  band: exemplar
  composite: 68.0
  coverage:
    artifact_dirs: 29
    catalog_gap: 42.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 81.6
    commercial_clarity: 81.6
    contract_governance: 87.9
    contract_quality: 58.5
    developer_ergonomics: 58.9
    discoverability: 57.4
    governance: 87.9
    operational_transparency: 2.6
  previous_composite: 68.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 76.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jefferson-health/refs/heads/main/screenshots/jefferson-health-2026-06-20T183715.png
security:
- kind: authentication
  name: Jefferson Health Authentication
  slug: jefferson-health-authentication
  summary_line: oauth2/openIdConnect/none · 3 schemes
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
- Authentication
- Patient Access
- Provider Directory
- SMART on FHIR
- US Core
- USCDI
website: https://www.jeffersonhealth.org/
---

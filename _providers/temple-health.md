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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.6
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Temple Health Agentic Access
  operation_count: 11
  slug: temple-health-agentic-access
  summary_line: 11 operations
api_count: 10
apis:
- description: 'The legacy Temple Health DSTU2 FHIR endpoint listed in Epic''s public DSTU2 endpoint registry under the organization "TempleHealth". It remains available for backward compatibility with older SMART on '
  name: Temple Health FHIR DSTU2 API
  slug: temple-health-fhir-dstu2-api
- description: Risk of harmful or undesirable physiological response to a substance.
  name: Temple Health Allergy Intolerance API
  slug: temple-health-allergy-intolerance-api
- description: HL7 FHIR Bulk Data Access Group-level export.
  name: Temple Health Bulk Data API
  slug: temple-health-bulk-data-api
- description: Detailed information about conditions, problems, or diagnoses.
  name: Temple Health Condition API
  slug: temple-health-condition-api
- description: A reference to a document, often a CCDA or clinical note.
  name: Temple Health Document Reference API
  slug: temple-health-document-reference-api
- description: An interaction between a patient and healthcare provider(s).
  name: Temple Health Encounter API
  slug: temple-health-encounter-api
- description: An order or request for both supply of the medication and the instructions for administration.
  name: Temple Health Medication Request API
  slug: temple-health-medication-request-api
- description: FHIR conformance and SMART configuration discovery.
  name: Temple Health Metadata API
  slug: temple-health-metadata-api
- description: Measurements and simple assertions made about a patient.
  name: Temple Health Observation API
  slug: temple-health-observation-api
- description: Demographics and other administrative information about an individual receiving care.
  name: Temple Health Patient API
  slug: temple-health-patient-api
artifact_total: 39
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Temple Health FHIR R4 Allergy Intolerance API
  slug: open-temple-health-allergy-intolerance-api
- collection_type: open
  name: Temple Health FHIR R4 Allergy Intolerance Bulk Data API
  slug: open-temple-health-bulk-data-api
- collection_type: open
  name: Temple Health FHIR R4 Allergy Intolerance Condition API
  slug: open-temple-health-condition-api
- collection_type: open
  name: Temple Health FHIR R4 Allergy Intolerance Document Reference API
  slug: open-temple-health-document-reference-api
- collection_type: open
  name: Temple Health FHIR R4 Allergy Intolerance Encounter API
  slug: open-temple-health-encounter-api
- collection_type: open
  name: Temple Health FHIR R4 Allergy Intolerance Medication Request API
  slug: open-temple-health-medication-request-api
- collection_type: open
  name: Temple Health FHIR R4 Allergy Intolerance Metadata API
  slug: open-temple-health-metadata-api
- collection_type: open
  name: Temple Health FHIR R4 Allergy Intolerance Observation API
  slug: open-temple-health-observation-api
- collection_type: open
  name: Temple Health FHIR R4 Allergy Intolerance Patient API
  slug: open-temple-health-patient-api
- collection_type: open
  name: Temple Health FHIR R4 API
  slug: open-temple-health-temple-health-fhir-r4-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/temple-health-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/temple-health-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/temple-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/temple-health-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.templehealth.org/
- group: start
  title: ''
  type: PatientPortal
  url: https://my.templehealth.org/MyChartPRD/Authentication/Login
- group: other
  title: ''
  type: Locations
  url: https://www.templehealth.org/locations
- group: company
  title: ''
  type: About
  url: https://www.templehealth.org/about
- group: commercial
  title: ''
  type: PriceTransparency
  url: https://www.templehealth.org/pricing-disclaimer
- group: other
  title: ''
  type: FinancialAssistance
  url: https://www.templehealth.org/financial-assistance
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.templehealth.org/web-privacy-policy
- group: other
  title: ''
  type: NonDiscriminationNotice
  url: https://www.templehealth.org/section-1557-notice-non-discrimination
- group: other
  title: ''
  type: University
  url: https://www.temple.edu/
- group: other
  title: ''
  type: MedicalSchool
  url: https://medicine.temple.edu/
- group: other
  title: ''
  type: CancerCenter
  url: https://www.foxchase.org/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Temple-Health
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
  url: json-ld/temple-health-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/temple-health-vocabulary.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/temple-health-patient-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/temple-health-observation-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/temple-health-fhir-encounter-structure.json
- group: commercial
  title: ''
  type: Plans
  url: plans/temple-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/temple-health-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/temple-health-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.templehealth.org/about/news
- group: agent
  title: ''
  type: WellKnown
  url: well-known/temple-health-well-known.yml
- group: other
  title: ''
  type: SMARTConfiguration
  url: well-known/temple-health-smart-configuration.json
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/temple-health-openid-configuration.json
- group: design
  title: ''
  type: Conformance
  url: conformance/temple-health-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/temple-health-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/temple-health-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/temple-health-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/temple-health-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/temple-health-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/temple-health-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/temple-health-fhir-r4-capability-statement-example.json
- group: build
  title: ''
  type: Examples
  url: examples/temple-health-fhir-r4-smart-configuration-example.json
- group: build
  title: ''
  type: Examples
  url: examples/temple-health-fhir-r4-patient-search-example.json
- group: build
  title: ''
  type: Examples
  url: examples/temple-health-fhir-r4-observation-search-example.json
- group: commercial
  title: ''
  type: PriceTransparency
  url: well-known/temple-health-cms-hpt.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hub.templehealth.org/web/guest/disclaimer_termsofuse.html
- group: operate
  title: ''
  type: Support
  url: https://www.templehealth.org/contact-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.templehealth.org/patients-visitors/billing-financial/hospital-pricing-information
- group: other
  title: ''
  type: PatientRights
  url: https://hub.templehealth.org/web/guest/patientrights.html
- group: auth
  title: ''
  type: HIPAANotice
  url: https://hub.templehealth.org/web/guest/privacy-hipaa.html
created: '2026-05-23'
description: Temple University Health System (Temple Health) is the Philadelphia-based academic health system affiliated with the Lewis Katz School of Medicine at Temple University. It operates Temple University Hospital (Main Campus, Jeanes, Episcopal, Northeastern, Women & Families), Temple Health Chestnut Hill Hospital, Fox Chase Cancer Center, and outpatient sites across the Philadelphia region. Its patient-facing electronic health record runs on Epic, branded myTempleHealth (MyChart), with CMS-mandated HL7 FHIR APIs published at epicaccess.templehealth.org/FhirProxyPrd/api/FHIR/R4 (and a legacy DSTU2 endpoint at the same host) that expose USCDI-aligned clinical resources to third-party patient-access applications via SMART on FHIR and OAuth 2.0. Temple Health does not publish a separate commercial developer program; its API surface is regulatory-mandated and free at point of use.
examples:
- key_count: 2
  name: Temple Health Fhir R4 Capability Statement Example
  slug: temple-health-fhir-r4-capability-statement-example
- key_count: 2
  name: Temple Health Fhir R4 Observation Search Example
  slug: temple-health-fhir-r4-observation-search-example
- key_count: 2
  name: Temple Health Fhir R4 Patient Search Example
  slug: temple-health-fhir-r4-patient-search-example
- key_count: 2
  name: Temple Health Fhir R4 Smart Configuration Example
  slug: temple-health-fhir-r4-smart-configuration-example
finops:
- name: Temple Health Finops
  service_category: ''
  slug: temple-health-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/temple-health.png
json_schemas:
- name: Temple Health FHIR R4 Observation (US Core Subset)
  property_count: 9
  slug: temple-health-observation
- name: Temple Health FHIR R4 Patient (US Core Subset)
  property_count: 7
  slug: temple-health-patient
json_structures:
- name: Temple Health Fhir Encounter Structure
  property_count: 13
  slug: temple-health-fhir-encounter-structure
jsonld:
- class_count: 35
  name: Temple Health Context
  property_count: 0
  slug: temple-health-context
layout: provider
mcp_servers:
- description: Temple Health ships no MCP server. This is a CANDIDATE tool surface derived from the operations the FHIR endpoint actually exposes, so that an integrator can see what an MCP wrapper would look like. N
  name: 'Candidate tool surface only — Temple Health hosts no MCP server (deployment mode: none)'
  slug: candidate-tool-surface-only-temple-health-hosts-no-mcp-server-deployment-mode-none
modified: '2026-08-15'
name: Temple Health
nav: Providers
network: true
overview: 'Temple Health publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Allergy Intolerance API, Bulk Data API, Condition API, and 6 more. Tagged areas include Academic Medical Center, CMS Interoperability, Cures Act, DSTU2, and Epic.


  The Temple Health catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Temple Health''s developer surface includes authentication, GitHub presence, engineering blog, code examples, support, pricing, and 42 more developer resources.'
plans:
- name: Temple Health Plans Pricing
  plan_count: 4
  slug: temple-health-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Temple Health Rate Limits
  slug: temple-health-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Temple Health API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: temple-health-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Temple Health API Rules
  rule_count: 8
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 3
  slug: temple-health-temple-health-fhir-r4-rules
scopes:
- name: Temple Health Scopes
  scope_count: 15
  slug: temple-health-scopes
  summary_line: 15 scopes · authorizationCode
score:
  band: strong
  composite: 63.1
  delta: 3.8
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 59.1
    contract_quality: 62.2
    developer_ergonomics: 39.9
    discoverability: 74.1
    governance: 59.1
    operational_transparency: 5.3
  previous_composite: 59.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 76.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/screenshots/temple-health-2026-06-20T195058.png
security:
- kind: authentication
  name: Temple Health Authentication
  slug: temple-health-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Temple Health Domain Security
  slug: temple-health-domain-security
  summary_line: TLSv1.3 · DMARC
slug: temple-health
tags:
- Academic Medical Center
- CMS Interoperability
- Cures Act
- DSTU2
- Epic
- FHIR
- Fox Chase Cancer Center
- HL7
- Healthcare
- Hospital System
- MyChart
- Authentication
- Patient Access
- Price Transparency
- R4
- SMART on FHIR
- Temple University
- US Core
- USCDI
website: https://www.templehealth.org/
---

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
  schema_version: '0.2'
  score: 34.6
  scored_at: '2026-09-15'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Temple Health Agentic Access
  operation_count: 11
  slug: temple-health-agentic-access
  summary_line: 11 operations
api_count: 1
apis:
- description: 'The legacy Temple Health DSTU2 FHIR endpoint listed in Epic''s public DSTU2 endpoint registry under the organization "TempleHealth". It remains available for backward compatibility with older SMART on '
  name: Temple Health FHIR DSTU2 API
  slug: temple-health-fhir-dstu2-api
- baseURL: https://epicaccess.templehealth.org/FhirProxyPrd/api/FHIR/R4
  baseurl_source: declared
  description: Risk of harmful or undesirable physiological response to a substance.
  name: Temple Health Allergy Intolerance API
  slug: temple-health-allergy-intolerance-api
- baseURL: https://epicaccess.templehealth.org/FhirProxyPrd/api/FHIR/R4
  baseurl_source: declared
  description: HL7 FHIR Bulk Data Access Group-level export.
  name: Temple Health Bulk Data API
  slug: temple-health-bulk-data-api
- baseURL: https://epicaccess.templehealth.org/FhirProxyPrd/api/FHIR/R4
  baseurl_source: declared
  description: Detailed information about conditions, problems, or diagnoses.
  name: Temple Health Condition API
  slug: temple-health-condition-api
- baseURL: https://epicaccess.templehealth.org/FhirProxyPrd/api/FHIR/R4
  baseurl_source: declared
  description: A reference to a document, often a CCDA or clinical note.
  name: Temple Health Document Reference API
  slug: temple-health-document-reference-api
- baseURL: https://epicaccess.templehealth.org/FhirProxyPrd/api/FHIR/R4
  baseurl_source: declared
  description: An interaction between a patient and healthcare provider(s).
  name: Temple Health Encounter API
  slug: temple-health-encounter-api
- baseURL: https://epicaccess.templehealth.org/FhirProxyPrd/api/FHIR/R4
  baseurl_source: declared
  description: An order or request for both supply of the medication and the instructions for administration.
  name: Temple Health Medication Request API
  slug: temple-health-medication-request-api
- baseURL: https://epicaccess.templehealth.org/FhirProxyPrd/api/FHIR/R4
  baseurl_source: declared
  description: FHIR conformance and SMART configuration discovery.
  name: Temple Health Metadata API
  slug: temple-health-metadata-api
- baseURL: https://epicaccess.templehealth.org/FhirProxyPrd/api/FHIR/R4
  baseurl_source: declared
  description: Measurements and simple assertions made about a patient.
  name: Temple Health Observation API
  slug: temple-health-observation-api
- baseURL: https://epicaccess.templehealth.org/FhirProxyPrd/api/FHIR/R4
  baseurl_source: declared
  description: Demographics and other administrative information about an individual receiving care.
  name: Temple Health Patient API
  slug: temple-health-patient-api
artifact_total: 38
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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/capabilities/temple-health-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/temple-health-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/agentic-access/temple-health-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/temple-health-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/security/temple-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/temple-health-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/authentication/temple-health-authentication.yml
  title: ''
  type: Authentication
  url: authentication/temple-health-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/scopes/temple-health-scopes.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/json-ld/temple-health-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/temple-health-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/vocabulary/temple-health-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/temple-health-vocabulary.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/json-schema/temple-health-patient-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/temple-health-patient-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/json-schema/temple-health-observation-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/temple-health-observation-schema.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/json-structure/temple-health-fhir-encounter-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/temple-health-fhir-encounter-structure.json
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/plans/temple-health-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/temple-health-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/rate-limits/temple-health-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/temple-health-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/finops/temple-health-finops.yml
  title: ''
  type: FinOps
  url: finops/temple-health-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.templehealth.org/about/news
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/well-known/temple-health-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/temple-health-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/well-known/temple-health-smart-configuration.json
  title: ''
  type: SMARTConfiguration
  url: well-known/temple-health-smart-configuration.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/well-known/temple-health-openid-configuration.json
  title: ''
  type: OpenIDConnect
  url: well-known/temple-health-openid-configuration.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/conformance/temple-health-conformance.yml
  title: ''
  type: Conformance
  url: conformance/temple-health-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/errors/temple-health-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/temple-health-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/lifecycle/temple-health-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/temple-health-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/conventions/temple-health-conventions.yml
  title: ''
  type: Conventions
  url: conventions/temple-health-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/data-model/temple-health-data-model.yml
  title: ''
  type: DataModel
  url: data-model/temple-health-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/llms/temple-health-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/temple-health-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/mcp/temple-health-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/temple-health-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/examples/temple-health-fhir-r4-capability-statement-example.json
  title: ''
  type: Examples
  url: examples/temple-health-fhir-r4-capability-statement-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/examples/temple-health-fhir-r4-smart-configuration-example.json
  title: ''
  type: Examples
  url: examples/temple-health-fhir-r4-smart-configuration-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/examples/temple-health-fhir-r4-patient-search-example.json
  title: ''
  type: Examples
  url: examples/temple-health-fhir-r4-patient-search-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/examples/temple-health-fhir-r4-observation-search-example.json
  title: ''
  type: Examples
  url: examples/temple-health-fhir-r4-observation-search-example.json
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/temple-health/refs/heads/main/well-known/temple-health-cms-hpt.txt
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
modified: '2026-08-15'
name: Temple Health
nav: Providers
network: true
overview: 'Temple Health publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Allergy Intolerance API, Bulk Data API, Condition API, and 6 more. Tagged areas include Academic Medical Center, CMS Interoperability, Cures Act, DSTU2, and Epic.


  The Temple Health catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Temple Health''s developer surface includes authentication, GitHub presence, engineering blog, code examples, support, pricing, and 43 more developer resources.'
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
  composite: 61.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 69.5
    catalog_earned_first_party: 12.0
    catalog_gap: 45.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 78.9
    contract_governance: 47.0
    contract_quality: 62.2
    developer_ergonomics: 39.9
    discoverability: 68.5
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 61.1
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
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
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

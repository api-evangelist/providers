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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
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
  score: 24.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Unitedhealth Agentic Access
  operation_count: 7
  slug: unitedhealth-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- description: FHIR R4 clinical data including conditions, observations, and medications
  name: UnitedHealth Group Clinical Data API
  slug: unitedhealth-clinical-data-api
- description: FHIR R4 Drug Formulary API for prescription drug coverage information
  name: UnitedHealth Group Drug Formulary API
  slug: unitedhealth-drug-formulary-api
- description: FHIR R4 Patient Access API for member health data (CMS-9115-F)
  name: UnitedHealth Group Patient Access API
  slug: unitedhealth-patient-access-api
- description: FHIR R4 Provider Directory API implementing Da Vinci PDex Plan Net IG
  name: UnitedHealth Group Provider Directory API
  slug: unitedhealth-provider-directory-api
artifact_total: 38
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: UnitedHealth Group Optum Clinical Data API
  slug: open-unitedhealth-clinical-data-api
- collection_type: open
  name: UnitedHealth Group Optum Clinical Data Drug Formulary API
  slug: open-unitedhealth-drug-formulary-api
- collection_type: open
  name: UnitedHealth Group Optum API
  slug: open-unitedhealth-optum-api
- collection_type: open
  name: UnitedHealth Group Optum Clinical Data Patient Access API
  slug: open-unitedhealth-patient-access-api
- collection_type: open
  name: UnitedHealth Group Optum Clinical Data Provider Directory API
  slug: open-unitedhealth-provider-directory-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/unitedhealth-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/unitedhealth-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/unitedhealth-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unitedhealth-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unitedhealth-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unitedhealth-group
created: '2026-03-21'
description: UnitedHealth Group is a diversified health care company with two distinct platforms, UnitedHealthcare for health benefits and Optum for health services, serving more than 100 million people worldwide. The company offers FHIR R4-compliant Interoperability APIs through the Optum platform, providing patient access to health records, claims history, provider directory, and drug formulary data in compliance with CMS Interoperability and Patient Access final rule (CMS-9115-F) and HL7 FHIR standards.
examples:
- key_count: 7
  name: Optum Fhir Bundle Example
  slug: optum-fhir-bundle-example
- key_count: 10
  name: Optum Fhir Coverage Example
  slug: optum-fhir-coverage-example
- key_count: 7
  name: Optum Fhir Medication Knowledge Example
  slug: optum-fhir-medication-knowledge-example
- key_count: 10
  name: Optum Fhir Patient Example
  slug: optum-fhir-patient-example
- key_count: 8
  name: Optum Fhir Practitioner Example
  slug: optum-fhir-practitioner-example
finops:
- name: Unitedhealth Finops
  service_category: Healthcare
  slug: unitedhealth-finops
graphqls:
- description: 'UnitedHealth Group operates two primary platforms: UnitedHealthcare for health benefits and Optum for health services. This conceptual GraphQL schema represents the core data models for member eligibi'
  name: UnitedHealth Group GraphQL Schema
  slug: unitedhealth-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unitedhealth.png
json_schemas:
- name: UnitedHealth Group FHIR Bundle
  property_count: 7
  slug: optum-fhir-bundle
- name: UnitedHealth Group FHIR Coverage
  property_count: 11
  slug: optum-fhir-coverage
- name: UnitedHealth Group FHIR ExplanationOfBenefit
  property_count: 11
  slug: optum-fhir-explanation-of-benefit
- name: UnitedHealth Group FHIR MedicationKnowledge
  property_count: 9
  slug: optum-fhir-medication-knowledge
- name: UnitedHealth Group FHIR Patient
  property_count: 8
  slug: optum-fhir-patient
- name: UnitedHealth Group FHIR Practitioner
  property_count: 8
  slug: optum-fhir-practitioner
json_structures:
- name: Optum Fhir Bundle Structure
  property_count: 0
  slug: optum-fhir-bundle-structure
- name: Optum Fhir Coverage Structure
  property_count: 0
  slug: optum-fhir-coverage-structure
- name: Optum Fhir Explanation Of Benefit Structure
  property_count: 0
  slug: optum-fhir-explanation-of-benefit-structure
- name: Optum Fhir Medication Knowledge Structure
  property_count: 0
  slug: optum-fhir-medication-knowledge-structure
- name: Optum Fhir Patient Structure
  property_count: 0
  slug: optum-fhir-patient-structure
- name: Optum Fhir Practitioner Structure
  property_count: 0
  slug: optum-fhir-practitioner-structure
jsonld:
- class_count: 21
  name: Unitedhealth Optum Api Context
  property_count: 1
  slug: unitedhealth-optum-api-context
layout: provider
modified: '2026-05-19'
name: UnitedHealth Group
nav: Providers
network: true
overview: 'UnitedHealth Group publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Clinical Data API, Drug Formulary API, Patient Access API, and 1 more. Tagged areas include Healthcare, Health Insurance, FHIR, Claims, and Interoperability.


  The UnitedHealth Group catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  UnitedHealth Group''s developer surface includes authentication and 5 more developer resources.'
plans:
- name: Unitedhealth Plans Pricing
  plan_count: 1
  slug: unitedhealth-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Unitedhealth Rate Limits
  slug: unitedhealth-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: UnitedHealth Group API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: unitedhealth-jsonschema-spectral-rules
- effective_rule_count: 71
  extends:
  - spectral:oas
  name: UnitedHealth Group API Rules
  rule_count: 30
  severity_counts:
    error: 13
    hint: 0
    info: 4
    warn: 13
  slug: unitedhealth-spectral-rules
score:
  band: thin
  composite: 34.0
  coverage:
    artifact_dirs: 17
    catalog_gap: 58.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 13.6
    contract_quality: 66.9
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 5.3
  previous_composite: 34.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 34.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unitedhealth/refs/heads/main/screenshots/unitedhealth-2026-06-20T200101.png
security:
- kind: authentication
  name: Unitedhealth Authentication
  slug: unitedhealth-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Unitedhealth Domain Security
  slug: unitedhealth-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Unitedhealth Vulnerability Disclosure
  slug: unitedhealth-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: unitedhealth
tags:
- Healthcare
- Health Insurance
- FHIR
- Claims
- Interoperability
- Fortune 100
---

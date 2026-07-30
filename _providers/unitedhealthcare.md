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
- acting_count: 5
  human_in_the_loop: 0
  name: Unitedhealthcare Agentic Access
  operation_count: 12
  slug: unitedhealthcare-agentic-access
  summary_line: 12 operations · 5 acting
api_count: 7
apis:
- description: Claim pre-check, submission, and inquiry
  name: UnitedHealthcare Claims API
  slug: unitedhealthcare-claims-api
- description: Real-time eligibility and benefit verification
  name: UnitedHealthcare Eligibility API
  slug: unitedhealthcare-eligibility-api
- description: Drug formulary and coverage information
  name: UnitedHealthcare Formulary API
  slug: unitedhealthcare-formulary-api
- description: FHIR R4 Patient Access API for member health data
  name: UnitedHealthcare Patient Access API
  slug: unitedhealthcare-patient-access-api
- description: Prior authorization and referral actions
  name: UnitedHealthcare Prior Authorization API
  slug: unitedhealthcare-prior-authorization-api
- description: FHIR R4 Provider Directory API for network information
  name: UnitedHealthcare Provider Directory API
  slug: unitedhealthcare-provider-directory-api
- description: Provider demographics and directory
  name: UnitedHealthcare Providers API
  slug: unitedhealthcare-providers-api
artifact_total: 53
collections:
- collection_type: open
  name: UnitedHealthcare Interoperability API
  slug: open-unitedhealthcare-interoperability-api
- collection_type: open
  name: UnitedHealthcare Provider API
  slug: open-unitedhealthcare-provider-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/unitedhealthcare-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unitedhealthcare-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unitedhealthcare-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UnitedHealthCare
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unitedhealthcare
created: '2025-03-01'
description: UnitedHealthcare is one of the largest health insurance providers in the United States, offering employer-sponsored health benefits, individual and family plans, Medicare and Medicaid plans, and managed care services. UnitedHealthcare provides APIs for healthcare providers through the UHC API Marketplace for eligibility verification, claims management, and prior authorization, and FHIR R4-compliant Interoperability APIs for patient data access and provider directory services per CMS mandates.
examples:
- key_count: 6
  name: Interoperability Fhir Bundle Example
  slug: interoperability-fhir-bundle-example
- key_count: 8
  name: Interoperability Fhir Patient Example
  slug: interoperability-fhir-patient-example
- key_count: 6
  name: Provider Benefit Check Response Example
  slug: provider-benefit-check-response-example
- key_count: 11
  name: Provider Claim Inquiry Response Example
  slug: provider-claim-inquiry-response-example
- key_count: 4
  name: Provider Claim Pre Check Response Example
  slug: provider-claim-pre-check-response-example
- key_count: 14
  name: Provider Eligibility Response Example
  slug: provider-eligibility-response-example
- key_count: 7
  name: Provider Prior Auth Check Response Example
  slug: provider-prior-auth-check-response-example
- key_count: 13
  name: Provider Provider Demographics Example
  slug: provider-provider-demographics-example
finops:
- name: Unitedhealthcare Finops
  service_category: API
  slug: unitedhealthcare-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unitedhealthcare.png
json_schemas:
- name: UnitedHealthcare FHIR Bundle
  property_count: 6
  slug: interoperability-fhir-bundle
- name: UnitedHealthcare FHIR Patient
  property_count: 8
  slug: interoperability-fhir-patient
- name: UnitedHealthcare Benefit Check Request
  property_count: 7
  slug: provider-benefit-check-request
- name: UnitedHealthcare Benefit Check Response
  property_count: 6
  slug: provider-benefit-check-response
- name: UnitedHealthcare Claim Inquiry Request
  property_count: 5
  slug: provider-claim-inquiry-request
- name: UnitedHealthcare Claim Inquiry Response
  property_count: 11
  slug: provider-claim-inquiry-response
- name: UnitedHealthcare Claim Pre-Check Request
  property_count: 7
  slug: provider-claim-pre-check-request
- name: UnitedHealthcare Claim Pre-Check Response
  property_count: 4
  slug: provider-claim-pre-check-response
- name: UnitedHealthcare Eligibility Request
  property_count: 6
  slug: provider-eligibility-request
- name: UnitedHealthcare Eligibility Response
  property_count: 14
  slug: provider-eligibility-response
- name: UnitedHealthcare Prior Auth Check Request
  property_count: 7
  slug: provider-prior-auth-check-request
- name: UnitedHealthcare Prior Auth Check Response
  property_count: 7
  slug: provider-prior-auth-check-response
- name: UnitedHealthcare Provider Demographics
  property_count: 13
  slug: provider-provider-demographics
json_structures:
- name: Interoperability Fhir Bundle Structure
  property_count: 0
  slug: interoperability-fhir-bundle-structure
- name: Interoperability Fhir Patient Structure
  property_count: 0
  slug: interoperability-fhir-patient-structure
- name: Provider Benefit Check Request Structure
  property_count: 0
  slug: provider-benefit-check-request-structure
- name: Provider Benefit Check Response Structure
  property_count: 0
  slug: provider-benefit-check-response-structure
- name: Provider Claim Inquiry Request Structure
  property_count: 0
  slug: provider-claim-inquiry-request-structure
- name: Provider Claim Inquiry Response Structure
  property_count: 0
  slug: provider-claim-inquiry-response-structure
- name: Provider Claim Pre Check Request Structure
  property_count: 0
  slug: provider-claim-pre-check-request-structure
- name: Provider Claim Pre Check Response Structure
  property_count: 0
  slug: provider-claim-pre-check-response-structure
- name: Provider Eligibility Request Structure
  property_count: 0
  slug: provider-eligibility-request-structure
- name: Provider Eligibility Response Structure
  property_count: 0
  slug: provider-eligibility-response-structure
- name: Provider Prior Auth Check Request Structure
  property_count: 0
  slug: provider-prior-auth-check-request-structure
- name: Provider Prior Auth Check Response Structure
  property_count: 0
  slug: provider-prior-auth-check-response-structure
- name: Provider Provider Demographics Structure
  property_count: 0
  slug: provider-provider-demographics-structure
jsonld:
- class_count: 17
  name: Unitedhealthcare Interoperability Api Context
  property_count: 1
  slug: unitedhealthcare-interoperability-api-context
- class_count: 14
  name: Unitedhealthcare Provider Api Context
  property_count: 13
  slug: unitedhealthcare-provider-api-context
layout: provider
modified: '2026-05-19'
name: UnitedHealthcare
nav: Providers
network: true
overview: 'UnitedHealthcare publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Claims API, Eligibility API, Formulary API, and 4 more. Tagged areas include Health Insurance, Healthcare, FHIR, Claims, and Eligibility.


  The UnitedHealthcare catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  UnitedHealthcare''s developer surface includes authentication and 4 more developer resources.'
plans:
- name: Unitedhealthcare Plans Pricing
  plan_count: 3
  slug: unitedhealthcare-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 5
  name: Unitedhealthcare Rate Limits
  slug: unitedhealthcare-rate-limits
rules:
- name: UnitedHealthcare API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: unitedhealthcare-jsonschema-spectral-rules
- name: UnitedHealthcare API Rules
  rule_count: 32
  severity_counts:
    error: 13
    hint: 0
    info: 5
    warn: 14
  slug: unitedhealthcare-spectral-rules
score:
  band: developing
  composite: 43.9
  delta: -5.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 71.2
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 49.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 25.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/unitedhealthcare/refs/heads/main/screenshots/unitedhealthcare-2026-06-20T200108.png
security:
- kind: authentication
  name: Unitedhealthcare Authentication
  slug: unitedhealthcare-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Unitedhealthcare Domain Security
  slug: unitedhealthcare-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: unitedhealthcare
tags:
- Health Insurance
- Healthcare
- FHIR
- Claims
- Eligibility
---

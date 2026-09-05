---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Hl7 Fhir Agentic Access
  operation_count: 11
  slug: hl7-fhir-agentic-access
  summary_line: 11 operations · 3 acting
api_count: 1
apis:
- description: HL7 FHIR R5 (Release 5) is the current published FHIR standard for healthcare data exchange. FHIR R5 REST APIs provide access to patient demographics, observations, conditions, medications, encounters
  name: HL7 FHIR R5 Healthcare API
  slug: hl7-fhir-r5-api
- description: 'SMART on FHIR (v2.2.0) defines OAuth 2.0-based authorization patterns for client applications to authorize, authenticate, and integrate with FHIR-based data systems. It enables EHR launch, standalone '
  name: SMART on FHIR Authentication
  slug: hl7-smart-on-fhir-api
- baseURL: https://fhir-server.example.com/fhir/R5
  baseurl_source: declared
  description: Batch and transaction operations
  name: HL7 FHIR Bundle API
  slug: hl7-fhir-bundle-api
- baseURL: https://fhir-server.example.com/fhir/R5
  baseurl_source: declared
  description: Clinical conditions, diagnoses, and problems
  name: HL7 FHIR Condition API
  slug: hl7-fhir-condition-api
- baseURL: https://fhir-server.example.com/fhir/R5
  baseurl_source: declared
  description: Patient visits and encounters
  name: HL7 FHIR Encounter API
  slug: hl7-fhir-encounter-api
- baseURL: https://fhir-server.example.com/fhir/R5
  baseurl_source: declared
  description: Medication prescriptions and orders
  name: HL7 FHIR MedicationRequest API
  slug: hl7-fhir-medicationrequest-api
- baseURL: https://fhir-server.example.com/fhir/R5
  baseurl_source: declared
  description: Clinical measurements, lab results, vital signs
  name: HL7 FHIR Observation API
  slug: hl7-fhir-observation-api
- baseURL: https://fhir-server.example.com/fhir/R5
  baseurl_source: declared
  description: Patient demographic and identity resources
  name: HL7 FHIR Patient API
  slug: hl7-fhir-patient-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HL7 FHIR R4 Healthcare Bundle API
  slug: open-hl7-fhir-bundle-api
- collection_type: open
  name: HL7 FHIR R4 Healthcare Bundle Condition API
  slug: open-hl7-fhir-condition-api
- collection_type: open
  name: HL7 FHIR R4 Healthcare Bundle Encounter API
  slug: open-hl7-fhir-encounter-api
- collection_type: open
  name: HL7 FHIR R4 Healthcare Bundle MedicationRequest API
  slug: open-hl7-fhir-medicationrequest-api
- collection_type: open
  name: HL7 FHIR R4 Healthcare Bundle Observation API
  slug: open-hl7-fhir-observation-api
- collection_type: open
  name: HL7 FHIR R4 Healthcare Bundle Patient API
  slug: open-hl7-fhir-patient-api
- collection_type: open
  name: HL7 FHIR R4 Healthcare API
  slug: open-hl7-fhir-r4
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/hl7-fhir-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hl7-fhir-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hl7-fhir-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hl7-fhir-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hl7-fhir-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://www.hl7.org/fhir/
- group: docs
  title: ''
  type: Documentation
  url: https://www.hl7.org/fhir/
- group: docs
  title: ''
  type: Reference
  url: https://www.hl7.org/fhir/http.html
- group: auth
  title: ''
  type: Authentication
  url: https://www.hl7.org/fhir/security.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.hl7.org/fhir/history.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.hl7.org/fhir/downloads.html
- group: company
  title: ''
  type: Website
  url: https://www.hl7.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HL7
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/hl7-fhir-r4-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/hl7-fhir-patient-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/hl7-fhir-context.jsonld
created: '2025'
description: HL7 FHIR (Fast Healthcare Interoperability Resources) is the standard API specification for healthcare data exchange, published by Health Level Seven International (HL7). FHIR REST APIs provide access to patient, clinical, financial, and administrative healthcare data in JSON, XML, and RDF formats with a CC0 open license.
finops:
- name: Hl7 Fhir Finops
  service_category: API
  slug: hl7-fhir-finops
json_schemas:
- name: HL7 FHIR R4 Patient
  property_count: 23
  slug: hl7-fhir-patient
jsonld:
- class_count: 13
  name: Hl7 Fhir Context
  property_count: 21
  slug: hl7-fhir-context
layout: provider
modified: '2026-05-19'
name: HL7 FHIR
nav: Providers
network: true
overview: 'HL7 FHIR publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Bundle API, Condition API, Encounter API, and 3 more. Tagged areas include Clinical, FHIR, Healthcare, HL7, and Interoperability.


  The HL7 FHIR catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  HL7 FHIR''s developer surface includes authentication, developer portal, documentation, changelog, getting-started guide, and 11 more developer resources.'
plans:
- name: Hl7 Fhir Plans Pricing
  plan_count: 3
  slug: hl7-fhir-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Hl7 Fhir Rate Limits
  slug: hl7-fhir-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: HL7 FHIR API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: hl7-fhir-jsonschema-spectral-rules
scopes:
- name: Hl7 Fhir Scopes
  scope_count: 7
  slug: hl7-fhir-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 58.3
    catalog_earned_first_party: 0.0
    catalog_gap: 56.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 60.1
    developer_ergonomics: 50.0
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 42.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 42.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hl7-fhir/refs/heads/main/screenshots/hl7-fhir-2026-06-20T182802.png
security:
- kind: authentication
  name: Hl7 Fhir Authentication
  slug: hl7-fhir-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Hl7 Fhir Domain Security
  slug: hl7-fhir-domain-security
  summary_line: TLSv1.3 · DMARC
slug: hl7-fhir
tags:
- Clinical
- FHIR
- Healthcare
- HL7
- Interoperability
website: https://www.hl7.org/
---

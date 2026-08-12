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
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Hl7 Fhir Agentic Access
  operation_count: 11
  slug: hl7-fhir-agentic-access
  summary_line: 11 operations · 3 acting
api_count: 8
apis:
- description: HL7 FHIR R5 (Release 5) is the current published FHIR standard for healthcare data exchange. FHIR R5 REST APIs provide access to patient demographics, observations, conditions, medications, encounters
  name: HL7 FHIR R5 Healthcare API
  slug: hl7-fhir-r5-api
- description: 'SMART on FHIR (v2.2.0) defines OAuth 2.0-based authorization patterns for client applications to authorize, authenticate, and integrate with FHIR-based data systems. It enables EHR launch, standalone '
  name: SMART on FHIR Authentication
  slug: hl7-smart-on-fhir-api
- description: Batch and transaction operations
  name: HL7 FHIR Bundle API
  slug: hl7-fhir-bundle-api
- description: Clinical conditions, diagnoses, and problems
  name: HL7 FHIR Condition API
  slug: hl7-fhir-condition-api
- description: Patient visits and encounters
  name: HL7 FHIR Encounter API
  slug: hl7-fhir-encounter-api
- description: Medication prescriptions and orders
  name: HL7 FHIR MedicationRequest API
  slug: hl7-fhir-medicationrequest-api
- description: Clinical measurements, lab results, vital signs
  name: HL7 FHIR Observation API
  slug: hl7-fhir-observation-api
- description: Patient demographic and identity resources
  name: HL7 FHIR Patient API
  slug: hl7-fhir-patient-api
artifact_total: 19
collections:
- collection_type: open
  name: HL7 FHIR R4 Healthcare API
  slug: open-hl7-fhir-r4
common:
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
image: https://raw.githubusercontent.com/api-evangelist/hl7-fhir/refs/heads/main/image.png
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


  HL7 FHIR''s developer surface includes authentication, developer portal, documentation, changelog, getting-started guide, and 10 more developer resources.'
plans:
- name: Hl7 Fhir Plans Pricing
  plan_count: 3
  slug: hl7-fhir-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 5
  name: Hl7 Fhir Rate Limits
  slug: hl7-fhir-rate-limits
rules:
- name: HL7 FHIR API Rules
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
  composite: 46.1
  delta: -7.2
  facets:
    commercial_clarity: 15.8
    contract_quality: 65.2
    developer_ergonomics: 45.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 28.9
  previous_composite: 53.3
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
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
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

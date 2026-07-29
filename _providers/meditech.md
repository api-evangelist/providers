---
access_model:
  confidence: high
  label: Unknown pricing · Registration request required
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://ehr.meditech.com/ehr-solutions/greenfield-workspace
  - https://greenfield.meditech.com/explorer/topic/welcome
  trial: false
  try_now: false
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
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Meditech Agentic Access
  operation_count: 10
  slug: meditech-agentic-access
  summary_line: 10 operations
api_count: 9
apis:
- description: 'MEDITECH''s FHIR API surface for Expanse, exposed to approved developers through the Greenfield Workspace. US Core FHIR R4 provides view-only access to patient-facing data after the patient authorizes '
  name: MEDITECH Expanse FHIR API
  slug: meditech-api
- description: Allergy and intolerance records
  name: meditech Allergy API
  slug: meditech-allergy-api
- description: FHIR server capability
  name: meditech Capability API
  slug: meditech-capability-api
- description: Problem list and diagnoses
  name: meditech Condition API
  slug: meditech-condition-api
- description: Diagnostic reports (lab, radiology, pathology)
  name: meditech Diagnostic API
  slug: meditech-diagnostic-api
- description: Clinical encounters and visits
  name: meditech Encounter API
  slug: meditech-encounter-api
- description: Medication requests and prescriptions
  name: meditech Medication API
  slug: meditech-medication-api
- description: Vital signs and laboratory results
  name: meditech Observation API
  slug: meditech-observation-api
- description: US Core Patient resources
  name: meditech Patient API
  slug: meditech-patient-api
artifact_total: 17
collections:
- collection_type: open
  name: Meditech Expanse FHIR R4 API
  slug: open-meditech-fhir
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/meditech-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meditech-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/meditech-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/meditech-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/meditech
- group: start
  title: ''
  type: Portal
  url: https://greenfield.meditech.com/
- group: company
  title: ''
  type: Website
  url: https://www.meditech.com/
- group: docs
  title: ''
  type: Documentation
  url: https://greenfield.meditech.com/explorer/topic/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://greenfield.meditech.com/explorer/api
- group: other
  title: ''
  type: Endpoints
  url: https://greenfield.meditech.com/explorer/endpoints
- group: auth
  title: ''
  type: Scopes
  url: https://greenfield.meditech.com/explorer/scope
- group: auth
  title: ''
  type: Authentication
  url: https://greenfield.meditech.com/explorer/authorization
- group: design
  title: ''
  type: Errors
  url: https://greenfield.meditech.com/explorer/status-codes
- group: start
  title: ''
  type: SignUp
  url: https://ehr.meditech.com/ehr-solutions/greenfield-workspace
- group: start
  title: ''
  type: GettingStarted
  url: https://ehr.meditech.com/ehr-solutions/how-to-work-in-the-greenfield-workspace
- group: other
  title: ''
  type: Resources
  url: https://ehr.meditech.com/ehr-solutions/greenfield-workspace-resources
- group: other
  title: ''
  type: HL7Interfaces
  url: https://ehr.meditech.com/hl7-outbound-list-for-greenfield
- group: other
  title: ''
  type: Interoperability
  url: https://ehr.meditech.com/ehr-solutions/meditech-interoperability
- group: company
  title: ''
  type: Blog
  url: https://blog.meditech.com/
- group: operate
  title: ''
  type: Support
  url: https://ehr.meditech.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ehr.meditech.com/privacy-policy
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/meditech/refs/heads/main/openapi/_original/meditech-fhir-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/meditech/refs/heads/main/json-schema/meditech-patient-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/meditech/refs/heads/main/json-ld/meditech-context.jsonld
- group: build
  title: ''
  type: PostmanCollection
  url: collections/meditech-fhir.postman_collection.json
- group: build
  title: ''
  type: OpenCollection
  url: collections/meditech-fhir.opencollection.json
created: '2026-05-04'
description: MEDITECH (Medical Information Technology, Inc.) is an electronic health record vendor serving community hospitals and health systems, primarily through its MEDITECH Expanse platform. Its API program is delivered through the Greenfield Workspace — a registration-gated developer environment where approved app developers get interactive documentation and a sandbox to execute APIs against a real MEDITECH EHR. Published surfaces are US Core FHIR R4 (view-only patient-facing data, USCDI v1, DSTU2/R4 compatible) and FHIR Scheduling APIs. MEDITECH also operates Traverse Exchange, its national data exchange network and TEFCA on-ramp, connecting 700+ facilities across 41 US states plus Canadian deployments.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/meditech.png
json_schemas:
- name: Meditech FHIR R4 Patient
  property_count: 16
  slug: meditech-patient
jsonld:
- class_count: 16
  name: Meditech Context
  property_count: 6
  slug: meditech-context
layout: provider
modified: '2026-07-27'
name: MEDITECH
nav: Providers
network: true
overview: 'MEDITECH publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Allergy API, Capability API, Condition API, and 5 more. Tagged areas include Company, EHR, Healthcare, FHIR, and HL7.


  The MEDITECH catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  MEDITECH''s developer surface includes authentication, developer portal, documentation, API reference, signup flow, getting-started guide, engineering blog, and 19 more developer resources.'
random_paper: 45
rules:
- name: MEDITECH API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: meditech-jsonschema-spectral-rules
scopes:
- name: Meditech Scopes
  scope_count: 5
  slug: meditech-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 45.4
  delta: -8.6
  facets:
    commercial_clarity: 23.7
    contract_quality: 58.1
    developer_ergonomics: 56.5
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 0.0
  previous_composite: 54.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 47.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/meditech/refs/heads/main/screenshots/meditech-2026-06-20T185121.png
security:
- kind: authentication
  name: Meditech Authentication
  slug: meditech-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Meditech Domain Security
  slug: meditech-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: meditech
tags:
- Company
- EHR
- Healthcare
- FHIR
- HL7
- Interoperability
website: https://www.meditech.com/
---

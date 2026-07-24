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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Meditech Agentic Access
  operation_count: 10
  slug: meditech-agentic-access
  summary_line: 10 operations
api_count: 9
apis:
- description: 'Meditech provides electronic health record (EHR) APIs for community hospitals and healthcare organizations. APIs enable access to patient records, lab results, pharmacy orders, radiology reports, and '
  name: Meditech EHR API
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
artifact_total: 20
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
  url: https://ehr.meditech.com/
- group: company
  title: ''
  type: Website
  url: https://ehr.meditech.com/
- group: docs
  title: ''
  type: Documentation
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
  url: https://raw.githubusercontent.com/api-evangelist/meditech/refs/heads/main/openapi/meditech-fhir-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/meditech/refs/heads/main/json-schema/meditech-patient-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/meditech/refs/heads/main/json-ld/meditech-context.jsonld
description: EHR Interoperability benefits everyone in the care network and helps you connect across the continuum of care. MEDITECH supports industry standards.
finops:
- name: Meditech Finops
  service_category: API
  slug: meditech-finops
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
modified: '2026-05-19'
name: meditech
nav: Providers
network: true
overview: 'meditech publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Allergy API, Capability API, Condition API, and 5 more.


  The meditech catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  meditech''s developer surface includes authentication, developer portal, documentation, engineering blog, support, and 9 more developer resources.'
plans:
- name: Meditech Plans Pricing
  plan_count: 3
  slug: meditech-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Meditech Rate Limits
  slug: meditech-rate-limits
rules:
- name: meditech API Rules
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
  composite: 50.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 64.2
    developer_ergonomics: 34.8
    discoverability: 42.5
    governance: 73.7
    operational_transparency: 31.6
  previous_composite: 50.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
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
website: https://ehr.meditech.com/
---

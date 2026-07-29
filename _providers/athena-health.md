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
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
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
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Athena Health Agentic Access
  operation_count: 40
  slug: athena-health-agentic-access
  summary_line: 40 operations · 9 acting
api_count: 22
apis:
- description: The AllergyIntolerance API from athenahealth — 1 operation(s) for allergyintolerance.
  name: athenahealth AllergyIntolerance API
  slug: athena-health-allergyintolerance-api
- description: The Appointment API from athenahealth — 1 operation(s) for appointment.
  name: athenahealth Appointment API
  slug: athena-health-appointment-api
- description: The Appointments API from athenahealth — 6 operation(s) for appointments.
  name: athenahealth Appointments API
  slug: athena-health-appointments-api
- description: The Bulk Data API from athenahealth — 2 operation(s) for bulk data.
  name: athenahealth Bulk Data API
  slug: athena-health-bulk-data-api
- description: The CDS Hooks API from athenahealth — 2 operation(s) for cds hooks.
  name: athenahealth CDS Hooks API
  slug: athena-health-cds-hooks-api
- description: The Claims API from athenahealth — 1 operation(s) for claims.
  name: athenahealth Claims API
  slug: athena-health-claims-api
- description: The Condition API from athenahealth — 1 operation(s) for condition.
  name: athenahealth Condition API
  slug: athena-health-condition-api
- description: The Conformance API from athenahealth — 1 operation(s) for conformance.
  name: athenahealth Conformance API
  slug: athena-health-conformance-api
- description: The Departments API from athenahealth — 1 operation(s) for departments.
  name: athenahealth Departments API
  slug: athena-health-departments-api
- description: The DiagnosticReport API from athenahealth — 1 operation(s) for diagnosticreport.
  name: athenahealth DiagnosticReport API
  slug: athena-health-diagnosticreport-api
- description: The DocumentReference API from athenahealth — 1 operation(s) for documentreference.
  name: athenahealth DocumentReference API
  slug: athena-health-documentreference-api
- description: The Documents API from athenahealth — 1 operation(s) for documents.
  name: athenahealth Documents API
  slug: athena-health-documents-api
- description: The Encounter API from athenahealth — 2 operation(s) for encounter.
  name: athenahealth Encounter API
  slug: athena-health-encounter-api
- description: The Encounters API from athenahealth — 2 operation(s) for encounters.
  name: athenahealth Encounters API
  slug: athena-health-encounters-api
- description: The Immunization API from athenahealth — 1 operation(s) for immunization.
  name: athenahealth Immunization API
  slug: athena-health-immunization-api
- description: The MedicationRequest API from athenahealth — 1 operation(s) for medicationrequest.
  name: athenahealth MedicationRequest API
  slug: athena-health-medicationrequest-api
- description: The Observation API from athenahealth — 1 operation(s) for observation.
  name: athenahealth Observation API
  slug: athena-health-observation-api
- description: The Patient API from athenahealth — 2 operation(s) for patient.
  name: athenahealth Patient API
  slug: athena-health-patient-api
- description: The Patients API from athenahealth — 2 operation(s) for patients.
  name: athenahealth Patients API
  slug: athena-health-patients-api
- description: The Practice API from athenahealth — 1 operation(s) for practice.
  name: athenahealth Practice API
  slug: athena-health-practice-api
- description: The Providers API from athenahealth — 1 operation(s) for providers.
  name: athenahealth Providers API
  slug: athena-health-providers-api
- description: The Subscription API from athenahealth — 3 operation(s) for subscription.
  name: athenahealth Subscription API
  slug: athena-health-subscription-api
artifact_total: 46
asyncapis:
- description: Event-driven notifications from the athenahealth Event Subscription Platform. Delivered as FHIR Bundle notifications (R5 Backport) over rest-hook channel with id-only payloads. Subscriber webhooks mus
  name: athenahealth FHIR Subscriptions Events
  slug: athenahealth-fhir-subscriptions-asyncapi
collections:
- collection_type: open
  name: athenahealth athenaOne REST API
  slug: open-athenahealth-athenaone-rest-api
- collection_type: open
  name: athenahealth CDS Hooks API
  slug: open-athenahealth-cds-hooks-api
- collection_type: open
  name: athenahealth FHIR Bulk Data Access API
  slug: open-athenahealth-fhir-bulk-data-api
- collection_type: open
  name: athenahealth FHIR R4 API
  slug: open-athenahealth-fhir-r4-api
- collection_type: open
  name: athenahealth FHIR Subscriptions API
  slug: open-athenahealth-fhir-subscriptions-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/athena-health-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/athena-health-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/athena-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/athena-health-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/athenahealth
- group: start
  title: ''
  type: Portal
  url: https://www.athenahealth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.athenahealth.com/api/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.athenahealth.com/api/guides/overview
- group: start
  title: ''
  type: Portal
  url: https://mydata.athenahealth.com/access-the-apis
- group: start
  title: ''
  type: Sandbox
  url: https://docs.athenahealth.com/api/sandbox
- group: docs
  title: ''
  type: Documentation
  url: https://docs.athenahealth.com/api/guides/athenaone-environments
- group: docs
  title: ''
  type: Documentation
  url: https://docs.athenahealth.com/api/guides/base-fhir-urls
- group: docs
  title: ''
  type: Documentation
  url: https://docs.athenahealth.com/api/guides/onboarding-overview
- group: operate
  title: ''
  type: Support
  url: https://docs.athenahealth.com/api/support
- group: other
  title: ''
  type: Marketplace
  url: https://www.athenahealth.com/solutions/marketplace
- group: company
  title: ''
  type: Blog
  url: https://www.athenahealth.com/knowledge-hub
- group: other
  title: ''
  type: Source
  url: https://github.com/athenahealth
- group: docs
  title: ''
  type: Documentation
  url: https://fhir.athena.io/athenacoreext/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://mydata.athenahealth.com/fhirapidoc/r4
- group: commercial
  title: ''
  type: Plans
  url: plans/athena-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/athena-health-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/athena-health-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/athena-health-vocabulary.yml
- group: design
  title: ''
  type: Spectral
  url: rules/athena-health-rules.yml
- group: build
  title: ''
  type: Samples
  url: https://github.com/athenahealth/mdp
- group: build
  title: ''
  type: Samples
  url: https://github.com/athenahealth/apiserver-athenaFlex
- group: build
  title: ''
  type: Samples
  url: https://github.com/athenahealth/aone-fhir-subscriptions
- group: build
  title: ''
  type: Tools
  url: https://github.com/athenahealth/vscode-cql-extension
- group: build
  title: ''
  type: SDKs
  url: https://github.com/eleanorhealth/go-athenahealth
description: athenahealth is a cloud-based electronic health record (EHR), revenue cycle management, and practice management platform serving ambulatory practices, hospitals, and health systems across the United States. The athenaOne platform spans patient engagement, scheduling, clinical documentation, ordering, e-prescribing, population health, and billing/claims. The athenahealth API surface exposes both a proprietary REST API and a Cures Act-certified FHIR R4 server with US Core / USCDI conformance, FHIR Subscriptions for event-driven webhooks, FHIR Bulk Data ($export) for population-scale data sharing, and CDS Hooks for embedded clinical decision support. The company is privately held by Veritas Capital and Hellman & Friedman following the 2022 take-private acquisition.
examples:
- key_count: 2
  name: Athenahealth Fhir Read Patient Example
  slug: athenahealth-fhir-read-patient-example
- key_count: 2
  name: Athenahealth Search Patients Example
  slug: athenahealth-search-patients-example
- key_count: 2
  name: Athenahealth Subscription Notification Example
  slug: athenahealth-subscription-notification-example
finops:
- name: Athena Health Finops
  service_category: ''
  slug: athena-health-finops
graphqls:
- description: This conceptual GraphQL schema models the athenahealth athenaOne REST API and FHIR R4 API surface. The athenaOne platform is a cloud-based EHR, revenue cycle management, and practice management system
  name: Athenahealth GraphQL Schema
  slug: athena-health-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/athena-health.png
json_schemas:
- name: athenahealth Appointment
  property_count: 14
  slug: athenahealth-appointment
- name: athenahealth FHIR R4 Patient (US Core profile)
  property_count: 11
  slug: athenahealth-fhir-patient
- name: athenahealth Patient
  property_count: 20
  slug: athenahealth-patient
jsonld:
- class_count: 23
  name: Athena Health Context
  property_count: 2
  slug: athena-health-context
layout: provider
name: athenahealth
nav: Providers
network: true
overview: 'athenahealth publishes 22 APIs on the [APIs.io](https://apis.io/) network, including AllergyIntolerance API, Appointment API, Appointments API, and 19 more. Tagged areas include EHR, Electronic Health Records, Healthcare, HL7, and FHIR.


  The athenahealth catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  athenahealth''s developer surface includes authentication, developer portal, documentation, sandbox, support, engineering blog, tooling, and 22 more developer resources.'
plans:
- name: Athena Health Plans Pricing
  plan_count: 3
  slug: athena-health-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Athena Health Rate Limits
  slug: athena-health-rate-limits
rules:
- name: athenahealth API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: athena-health-asyncapi-spectral-rules
- name: athenahealth API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: athena-health-jsonschema-spectral-rules
- name: athenahealth API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 4
  slug: athena-health-rules
scopes:
- name: Athena Health Scopes
  scope_count: 11
  slug: athena-health-scopes
  summary_line: 11 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 49.4
  delta: -5.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 77.4
    developer_ergonomics: 47.8
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 0.0
  previous_composite: 55.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 42.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/athena-health/refs/heads/main/screenshots/athena-health-2026-06-20T172518.png
security:
- kind: authentication
  name: Athena Health Authentication
  slug: athena-health-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Athena Health Domain Security
  slug: athena-health-domain-security
  summary_line: TLSv1.3 · DMARC
slug: athena-health
tags:
- EHR
- Electronic Health Records
- Healthcare
- HL7
- FHIR
- Interoperability
- Practice Management
- Revenue Cycle Management
- USCDI
- Cures Act
- SMART on FHIR
- CDS Hooks
- Cloud EHR
website: https://www.athenahealth.com/
---

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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
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
  score: 53.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 22
  human_in_the_loop: 3
  name: Orion Agentic Access
  operation_count: 91
  slug: orion-agentic-access
  summary_line: 91 operations · 22 acting · 3 human-in-the-loop
api_count: 32
apis:
- description: Clinical and population health alerts
  name: Orion Health Alerts API
  slug: orion-alerts-api
- description: Operations on AllergyIntolerance resources
  name: Orion Health AllergyIntolerance API
  slug: orion-allergyintolerance-api
- description: Population health analytics and reporting
  name: Orion Health Analytics API
  slug: orion-analytics-api
- description: Audit log access for compliance
  name: Orion Health Audit API
  slug: orion-audit-api
- description: Care program management and enrollment
  name: Orion Health Care Programs API
  slug: orion-care-programs-api
- description: Operations on CarePlan resources
  name: Orion Health CarePlan API
  slug: orion-careplan-api
- description: Patient cohort definition and analysis
  name: Orion Health Cohorts API
  slug: orion-cohorts-api
- description: Communication point configuration and management
  name: Orion Health Communication Points API
  slug: orion-communication-points-api
- description: Operations on Condition resources (diagnoses, problems)
  name: Orion Health Condition API
  slug: orion-condition-api
- description: Engine configuration management
  name: Orion Health Configuration API
  slug: orion-configuration-api
- description: Patient consent management for data sharing
  name: Orion Health Consent API
  slug: orion-consent-api
- description: Operations on DiagnosticReport resources
  name: Orion Health DiagnosticReport API
  slug: orion-diagnosticreport-api
- description: Operations on DocumentReference resources
  name: Orion Health DocumentReference API
  slug: orion-documentreference-api
- description: Clinical document exchange and retrieval
  name: Orion Health Documents API
  slug: orion-documents-api
- description: Operations on Encounter resources
  name: Orion Health Encounter API
  slug: orion-encounter-api
- description: Operations on Immunization resources
  name: Orion Health Immunization API
  slug: orion-immunization-api
- description: Lookup table management for data mapping
  name: Orion Health Lookup Tables API
  slug: orion-lookup-tables-api
- description: Operations on MedicationRequest resources
  name: Orion Health MedicationRequest API
  slug: orion-medicationrequest-api
- description: Message queue monitoring and management
  name: Orion Health Message Queues API
  slug: orion-message-queues-api
- description: Message search, inspection, and reprocessing
  name: Orion Health Messages API
  slug: orion-messages-api
- description: Server capability and metadata operations
  name: Orion Health Metadata API
  slug: orion-metadata-api
- description: System health and performance monitoring
  name: Orion Health Monitoring API
  slug: orion-monitoring-api
- description: Admission, discharge, and transfer notifications
  name: Orion Health Notifications API
  slug: orion-notifications-api
- description: Operations on Observation resources (vitals, labs, etc.)
  name: Orion Health Observation API
  slug: orion-observation-api
- description: Operations on Patient resources
  name: Orion Health Patient API
  slug: orion-patient-api
- description: Patient identity matching and cross-referencing (MPI)
  name: Orion Health Patient Identity API
  slug: orion-patient-identity-api
- description: Operations on Procedure resources
  name: Orion Health Procedure API
  slug: orion-procedure-api
- description: Provider and organization directory lookups
  name: Orion Health Provider Directory API
  slug: orion-provider-directory-api
- description: Healthcare quality measure tracking
  name: Orion Health Quality Measures API
  slug: orion-quality-measures-api
- description: Patient registry management
  name: Orion Health Registries API
  slug: orion-registries-api
- description: Patient risk scoring and stratification
  name: Orion Health Risk Stratification API
  slug: orion-risk-stratification-api
- description: Integration route management
  name: Orion Health Routes API
  slug: orion-routes-api
artifact_total: 50
asyncapis:
- description: 'The Orion Health Rhapsody Integration Engine processes healthcare messages in real-time across connected healthcare systems. This specification describes the event-driven messaging patterns supported '
  name: Orion Health Rhapsody Messaging Events
  slug: orion-rhapsody-messaging-asyncapi
collections:
- collection_type: open
  name: Orion Health FHIR API
  slug: open-orion-fhir
- collection_type: open
  name: Orion Health HIE API
  slug: open-orion-hie
- collection_type: open
  name: Orion Health Population Health API
  slug: open-orion-population-health
- collection_type: open
  name: Orion Health Rhapsody Integration API
  slug: open-orion-rhapsody
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/orion-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orion-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/orion-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/orion-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/orion-health
- group: start
  title: ''
  type: Portal
  url: https://developer.orionhealth.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.orionhealth.com/developers/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://www.orionhealth.com/developers/authentication
- group: operate
  title: ''
  type: Support
  url: https://www.orionhealth.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.orionhealth.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.orionhealth.com/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://www.orionhealth.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.orionhealth.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.orionhealth.com
- group: company
  title: ''
  type: Website
  url: https://www.orionhealth.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/orionhealth
- group: operate
  title: ''
  type: Community
  url: https://community.orionhealth.com
created: '2024'
description: Orion Health is a global healthcare technology company that provides health information technology solutions, including population health management, health information exchange, and clinical workflow tools.
finops:
- name: Orion Finops
  service_category: Healthcare Interoperability
  slug: orion-finops
image: https://www.orionhealth.com/assets/img/orion-health-logo.png
json_schemas:
- name: Orion Health Population Health Care Plan
  property_count: 17
  slug: orion-care-plan
- name: Orion Health FHIR Observation
  property_count: 28
  slug: orion-observation
- name: Orion Health FHIR Patient
  property_count: 20
  slug: orion-patient
jsonld:
- class_count: 5
  name: Orion Healthcare Context
  property_count: 17
  slug: orion-healthcare-context
layout: provider
modified: '2026-05-19'
name: Orion Health
nav: Providers
network: true
overview: 'Orion Health publishes 32 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, AllergyIntolerance API, Analytics API, and 29 more. Tagged areas include EHR, FHIR, Health IT, Healthcare, and HIE.


  The Orion Health catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Orion Health''s developer surface includes authentication, developer portal, getting-started guide, support, engineering blog, and 12 more developer resources.'
plans:
- name: Orion Plans Pricing
  plan_count: 1
  slug: orion-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 4
  name: Orion Rate Limits
  slug: orion-rate-limits
rules:
- name: Orion Health API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: orion-asyncapi-spectral-rules
- name: Orion Health API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: orion-jsonschema-spectral-rules
scopes:
- name: Orion Scopes
  scope_count: 24
  slug: orion-scopes
  summary_line: 24 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 62.4
  delta: 2.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 80.4
    developer_ergonomics: 37.0
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 59.9
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 76.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/orion/refs/heads/main/screenshots/orion-2026-06-20T191207.png
security:
- kind: authentication
  name: Orion Authentication
  slug: orion-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Orion Domain Security
  slug: orion-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: orion
tags:
- EHR
- FHIR
- Health IT
- Healthcare
- HIE
- HL7
- Integration
- Interoperability
- Population Health
website: https://www.orionhealth.com
---

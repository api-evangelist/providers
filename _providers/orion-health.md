---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 22
  human_in_the_loop: 3
  name: Orion Health Agentic Access
  operation_count: 91
  slug: orion-health-agentic-access
  summary_line: 91 operations · 22 acting · 3 human-in-the-loop
api_count: 4
apis:
- description: Medical platform which allows the development of applications for different healthcare scenarios
  name: Orion Health
  slug: orion-health
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
artifact_total: 115
asyncapis:
- description: 'The Orion Health Rhapsody Integration Engine processes healthcare messages in real-time across connected healthcare systems. This specification describes the event-driven messaging patterns supported '
  name: Orion Health Rhapsody Messaging Events
  slug: orion-health-rhapsody-messaging-asyncapi
collections:
- collection_type: postman
  name: Orion Health FHIR Alerts API
  slug: postman-orion-health-alerts-api
- collection_type: postman
  name: Orion Health FHIR Alerts AllergyIntolerance API
  slug: postman-orion-health-allergyintolerance-api
- collection_type: postman
  name: Orion Health FHIR Alerts Analytics API
  slug: postman-orion-health-analytics-api
- collection_type: postman
  name: Orion Health FHIR Alerts Audit API
  slug: postman-orion-health-audit-api
- collection_type: postman
  name: Orion Health FHIR Alerts Care Programs API
  slug: postman-orion-health-care-programs-api
- collection_type: postman
  name: Orion Health FHIR Alerts CarePlan API
  slug: postman-orion-health-careplan-api
- collection_type: postman
  name: Orion Health FHIR Alerts Cohorts API
  slug: postman-orion-health-cohorts-api
- collection_type: postman
  name: Orion Health FHIR Alerts Communication Points API
  slug: postman-orion-health-communication-points-api
- collection_type: postman
  name: Orion Health FHIR Alerts Condition API
  slug: postman-orion-health-condition-api
- collection_type: postman
  name: Orion Health FHIR Alerts Configuration API
  slug: postman-orion-health-configuration-api
- collection_type: postman
  name: Orion Health FHIR Alerts Consent API
  slug: postman-orion-health-consent-api
- collection_type: postman
  name: Orion Health FHIR Alerts DiagnosticReport API
  slug: postman-orion-health-diagnosticreport-api
- collection_type: postman
  name: Orion Health FHIR Alerts DocumentReference API
  slug: postman-orion-health-documentreference-api
- collection_type: postman
  name: Orion Health FHIR Alerts Documents API
  slug: postman-orion-health-documents-api
- collection_type: postman
  name: Orion Health FHIR Alerts Encounter API
  slug: postman-orion-health-encounter-api
- collection_type: postman
  name: Orion Health FHIR Alerts Immunization API
  slug: postman-orion-health-immunization-api
- collection_type: postman
  name: Orion Health FHIR Alerts Lookup Tables API
  slug: postman-orion-health-lookup-tables-api
- collection_type: postman
  name: Orion Health FHIR Alerts MedicationRequest API
  slug: postman-orion-health-medicationrequest-api
- collection_type: postman
  name: Orion Health FHIR Alerts Message Queues API
  slug: postman-orion-health-message-queues-api
- collection_type: postman
  name: Orion Health FHIR Alerts Messages API
  slug: postman-orion-health-messages-api
- collection_type: postman
  name: Orion Health FHIR Alerts Metadata API
  slug: postman-orion-health-metadata-api
- collection_type: postman
  name: Orion Health FHIR Alerts Monitoring API
  slug: postman-orion-health-monitoring-api
- collection_type: postman
  name: Orion Health FHIR Alerts Notifications API
  slug: postman-orion-health-notifications-api
- collection_type: postman
  name: Orion Health FHIR Alerts Observation API
  slug: postman-orion-health-observation-api
- collection_type: postman
  name: Orion Health FHIR Alerts Patient API
  slug: postman-orion-health-patient-api
- collection_type: postman
  name: Orion Health FHIR Alerts Patient Identity API
  slug: postman-orion-health-patient-identity-api
- collection_type: postman
  name: Orion Health FHIR Alerts Procedure API
  slug: postman-orion-health-procedure-api
- collection_type: postman
  name: Orion Health FHIR Alerts Provider Directory API
  slug: postman-orion-health-provider-directory-api
- collection_type: postman
  name: Orion Health FHIR Alerts Quality Measures API
  slug: postman-orion-health-quality-measures-api
- collection_type: postman
  name: Orion Health FHIR Alerts Registries API
  slug: postman-orion-health-registries-api
- collection_type: postman
  name: Orion Health FHIR Alerts Risk Stratification API
  slug: postman-orion-health-risk-stratification-api
- collection_type: postman
  name: Orion Health FHIR Alerts Routes API
  slug: postman-orion-health-routes-api
- collection_type: open
  name: Orion Health FHIR Alerts API
  slug: open-orion-health-alerts-api
- collection_type: open
  name: Orion Health FHIR Alerts AllergyIntolerance API
  slug: open-orion-health-allergyintolerance-api
- collection_type: open
  name: Orion Health FHIR Alerts Analytics API
  slug: open-orion-health-analytics-api
- collection_type: open
  name: Orion Health FHIR Alerts Audit API
  slug: open-orion-health-audit-api
- collection_type: open
  name: Orion Health FHIR Alerts Care Programs API
  slug: open-orion-health-care-programs-api
- collection_type: open
  name: Orion Health FHIR Alerts CarePlan API
  slug: open-orion-health-careplan-api
- collection_type: open
  name: Orion Health FHIR Alerts Cohorts API
  slug: open-orion-health-cohorts-api
- collection_type: open
  name: Orion Health FHIR Alerts Communication Points API
  slug: open-orion-health-communication-points-api
- collection_type: open
  name: Orion Health FHIR Alerts Condition API
  slug: open-orion-health-condition-api
- collection_type: open
  name: Orion Health FHIR Alerts Configuration API
  slug: open-orion-health-configuration-api
- collection_type: open
  name: Orion Health FHIR Alerts Consent API
  slug: open-orion-health-consent-api
- collection_type: open
  name: Orion Health FHIR Alerts DiagnosticReport API
  slug: open-orion-health-diagnosticreport-api
- collection_type: open
  name: Orion Health FHIR Alerts DocumentReference API
  slug: open-orion-health-documentreference-api
- collection_type: open
  name: Orion Health FHIR Alerts Documents API
  slug: open-orion-health-documents-api
- collection_type: open
  name: Orion Health FHIR Alerts Encounter API
  slug: open-orion-health-encounter-api
- collection_type: open
  name: Orion Health FHIR API
  slug: open-orion-health-fhir
- collection_type: open
  name: Orion Health HIE API
  slug: open-orion-health-hie
- collection_type: open
  name: Orion Health FHIR Alerts Immunization API
  slug: open-orion-health-immunization-api
- collection_type: open
  name: Orion Health FHIR Alerts Lookup Tables API
  slug: open-orion-health-lookup-tables-api
- collection_type: open
  name: Orion Health FHIR Alerts MedicationRequest API
  slug: open-orion-health-medicationrequest-api
- collection_type: open
  name: Orion Health FHIR Alerts Message Queues API
  slug: open-orion-health-message-queues-api
- collection_type: open
  name: Orion Health FHIR Alerts Messages API
  slug: open-orion-health-messages-api
- collection_type: open
  name: Orion Health FHIR Alerts Metadata API
  slug: open-orion-health-metadata-api
- collection_type: open
  name: Orion Health FHIR Alerts Monitoring API
  slug: open-orion-health-monitoring-api
- collection_type: open
  name: Orion Health FHIR Alerts Notifications API
  slug: open-orion-health-notifications-api
- collection_type: open
  name: Orion Health FHIR Alerts Observation API
  slug: open-orion-health-observation-api
- collection_type: open
  name: Orion Health FHIR Alerts Patient API
  slug: open-orion-health-patient-api
- collection_type: open
  name: Orion Health FHIR Alerts Patient Identity API
  slug: open-orion-health-patient-identity-api
- collection_type: open
  name: Orion Health Population Health API
  slug: open-orion-health-population-health
- collection_type: open
  name: Orion Health FHIR Alerts Procedure API
  slug: open-orion-health-procedure-api
- collection_type: open
  name: Orion Health FHIR Alerts Provider Directory API
  slug: open-orion-health-provider-directory-api
- collection_type: open
  name: Orion Health FHIR Alerts Quality Measures API
  slug: open-orion-health-quality-measures-api
- collection_type: open
  name: Orion Health FHIR Alerts Registries API
  slug: open-orion-health-registries-api
- collection_type: open
  name: Orion Health Rhapsody Integration API
  slug: open-orion-health-rhapsody
- collection_type: open
  name: Orion Health FHIR Alerts Risk Stratification API
  slug: open-orion-health-risk-stratification-api
- collection_type: open
  name: Orion Health FHIR Alerts Routes API
  slug: open-orion-health-routes-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/orion-health-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orion-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://developer.orionhealth.io/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://www.orionhealth.com/feed/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/orion-health/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/orion-health-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orion-health-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/orion-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/orion-health-scopes.yml
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/orion-health-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orion-health-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/orion-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/orion-health-scopes.yml
created: '2026-05-28'
description: Medical platform which allows the development of applications for different healthcare scenarios
finops:
- name: Orion Health Finops
  service_category: Healthcare Interoperability
  slug: orion-health-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/orion-health.png
json_schemas:
- name: Orion Health Population Health Care Plan
  property_count: 17
  slug: orion-health-care-plan
- name: Orion Health FHIR Observation
  property_count: 28
  slug: orion-health-observation
- name: Orion Health FHIR Patient
  property_count: 20
  slug: orion-health-patient
jsonld:
- class_count: 5
  name: Orion Health Healthcare Context
  property_count: 17
  slug: orion-health-healthcare-context
layout: provider
modified: '2026-05-28'
name: Orion Health
nav: Providers
network: true
overview: 'Orion Health publishes 32 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, AllergyIntolerance API, Analytics API, and 29 more. Tagged areas include Health and Public APIs.


  The Orion Health catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Orion Health''s developer surface includes engineering blog, authentication, developer portal, getting-started guide, support, and 22 more developer resources.'
plans:
- name: Orion Health Plans Pricing
  plan_count: 1
  slug: orion-health-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Orion Health Rate Limits
  slug: orion-health-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Orion Health API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: orion-health-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Orion Health API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: orion-health-jsonschema-spectral-rules
scopes:
- name: Orion Health Scopes
  scope_count: 24
  slug: orion-health-scopes
  summary_line: 24 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 45.2
  coverage:
    artifact_dirs: 17
    catalog_gap: 54.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 13.6
    contract_quality: 77.8
    developer_ergonomics: 34.5
    discoverability: 57.4
    governance: 13.6
    operational_transparency: 18.4
  previous_composite: 45.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 32
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 47.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/orion-health/refs/heads/main/screenshots/orion-health-2026-06-20T191207.png
security:
- kind: authentication
  name: Orion Health Authentication
  slug: orion-health-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Orion Health Domain Security
  slug: orion-health-domain-security
  summary_line: TLSv1.3
slug: orion-health
tags:
- Health
- Public APIs
website: https://developer.orionhealth.io/
---

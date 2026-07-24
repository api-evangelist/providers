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
  name: Charmhealth Agentic Access
  operation_count: 15
  slug: charmhealth-agentic-access
  summary_line: 15 operations
api_count: 14
apis:
- description: Patient allergies and intolerances
  name: CharmHealth AllergyIntolerance API
  slug: charmhealth-allergyintolerance-api
- description: Scheduled appointments
  name: CharmHealth Appointment API
  slug: charmhealth-appointment-api
- description: Server capability statement
  name: CharmHealth Capability API
  slug: charmhealth-capability-api
- description: Care plans
  name: CharmHealth CarePlan API
  slug: charmhealth-careplan-api
- description: Care teams
  name: CharmHealth CareTeam API
  slug: charmhealth-careteam-api
- description: Diagnoses and problems
  name: CharmHealth Condition API
  slug: charmhealth-condition-api
- description: Clinical documents
  name: CharmHealth DocumentReference API
  slug: charmhealth-documentreference-api
- description: Patient encounters and visits
  name: CharmHealth Encounter API
  slug: charmhealth-encounter-api
- description: Immunization records
  name: CharmHealth Immunization API
  slug: charmhealth-immunization-api
- description: Medication orders
  name: CharmHealth MedicationRequest API
  slug: charmhealth-medicationrequest-api
- description: Vital signs, lab results, and clinical observations
  name: CharmHealth Observation API
  slug: charmhealth-observation-api
- description: Provider organizations
  name: CharmHealth Organization API
  slug: charmhealth-organization-api
- description: Patient demographic resource
  name: CharmHealth Patient API
  slug: charmhealth-patient-api
- description: Care providers
  name: CharmHealth Practitioner API
  slug: charmhealth-practitioner-api
artifact_total: 27
collections:
- collection_type: open
  name: CharmHealth FHIR API
  slug: open-charmhealth-fhir-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/charmhealth-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/charmhealth-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/charmhealth-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/charmhealth-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/charmhealth-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CharmHealth
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/charmhealth
- group: company
  title: ''
  type: Website
  url: https://www.charmhealth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.charmhealth.com/resources/fhir/index.html
- group: other
  title: ''
  type: Developer
  url: https://www.charmhealth.com/developer/
- group: company
  title: ''
  type: News
  url: https://www.charmhealth.com/ehr/ehr-trade-shows.html
- group: operate
  title: ''
  type: PressReleases
  url: https://www.charmhealth.com/ehr/press-release.html
- group: other
  title: ''
  type: CaseStudies
  url: https://casestudy.charmhealth.com/charmhealth-case-study-landing-page/
- group: company
  title: ''
  type: Blog
  url: https://www.charmhealth.com/blog/
- group: company
  title: ''
  type: Newsletter
  url: https://www.charmhealth.com/newsletter/
- group: learn
  title: ''
  type: Webinars
  url: https://www.charmhealth.com/ehr/webinar.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.charmhealth.com/ehr/ehr-pricing.html
- group: operate
  title: ''
  type: Support
  url: https://www.charmhealth.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.charmhealth.com/ehr/termsofservice.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.charmhealth.com/privacy-policy.html
- group: design
  title: ''
  type: JSONLD
  url: json-ld/charmhealth-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/charmhealth-patient-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/charmhealth-observation-schema.json
created: '2025-02-21'
description: CharmHealth is a healthcare technology platform offering Electronic Health Records (EHR), Practice Management, Revenue Cycle Management, Patient Engagement, and TeleHealth tooling. CharmHealth exposes an HL7 FHIR R4 API conformant to the US Core Implementation Guide that lets third-party applications query patient medical records, manage clinical resources, and integrate with the EHR using SMART on FHIR OAuth 2.0 authorization.
finops:
- name: Charmhealth Finops
  service_category: API
  slug: charmhealth-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/charmhealth.png
json_schemas:
- name: CharmHealth FHIR Observation
  property_count: 8
  slug: charmhealth-observation
- name: CharmHealth FHIR Patient
  property_count: 8
  slug: charmhealth-patient
jsonld:
- class_count: 0
  name: Charmhealth Context
  property_count: 6
  slug: charmhealth-context
layout: provider
modified: '2026-05-19'
name: CharmHealth
nav: Providers
network: true
overview: 'CharmHealth publishes 14 APIs on the [APIs.io](https://apis.io/) network, including AllergyIntolerance API, Appointment API, Capability API, and 11 more. Tagged areas include EHR, EMR, FHIR, Healthcare, and HL7.


  The CharmHealth catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CharmHealth''s developer surface includes authentication, documentation, product news, engineering blog, pricing, support, and 17 more developer resources.'
plans:
- name: Charmhealth Plans Pricing
  plan_count: 3
  slug: charmhealth-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 5
  name: Charmhealth Rate Limits
  slug: charmhealth-rate-limits
rules:
- name: CharmHealth API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: charmhealth-jsonschema-spectral-rules
scopes:
- name: Charmhealth Scopes
  scope_count: 7
  slug: charmhealth-scopes
  summary_line: 7 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 59.1
  delta: 5.3
  facets:
    commercial_clarity: 71.1
    contract_quality: 55.8
    developer_ergonomics: 26.1
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 36.8
  previous_composite: 53.8
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 89.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/charmhealth/refs/heads/main/screenshots/charmhealth-2026-06-20T174227.png
security:
- kind: authentication
  name: Charmhealth Authentication
  slug: charmhealth-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Charmhealth Domain Security
  slug: charmhealth-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Charmhealth Vulnerability Disclosure
  slug: charmhealth-vulnerability-disclosure
  summary_line: disclosure policy published
slug: charmhealth
tags:
- EHR
- EMR
- FHIR
- Healthcare
- HL7
- Patient Engagement
- Patients
- SMART on FHIR
- US Core
website: https://www.charmhealth.com/
---

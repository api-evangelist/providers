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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Charmhealth Agentic Access
  operation_count: 15
  slug: charmhealth-agentic-access
  summary_line: 15 operations
api_count: 1
apis:
- baseURL: https://ehr2.charmtracker.com/api/ehr/v2/fhir
  baseurl_source: declared
  description: Patient allergies and intolerances
  name: CharmHealth AllergyIntolerance API
  slug: charmhealth-allergyintolerance-api
- baseURL: https://ehr2.charmtracker.com/api/ehr/v2/fhir
  baseurl_source: declared
  description: Scheduled appointments
  name: CharmHealth Appointment API
  slug: charmhealth-appointment-api
- baseURL: https://ehr2.charmtracker.com/api/ehr/v2/fhir
  baseurl_source: declared
  description: Server capability statement
  name: CharmHealth Capability API
  slug: charmhealth-capability-api
- baseURL: https://ehr2.charmtracker.com/api/ehr/v2/fhir
  baseurl_source: declared
  description: Care plans
  name: CharmHealth CarePlan API
  slug: charmhealth-careplan-api
- baseURL: https://ehr2.charmtracker.com/api/ehr/v2/fhir
  baseurl_source: declared
  description: Care teams
  name: CharmHealth CareTeam API
  slug: charmhealth-careteam-api
- baseURL: https://ehr2.charmtracker.com/api/ehr/v2/fhir
  baseurl_source: declared
  description: Diagnoses and problems
  name: CharmHealth Condition API
  slug: charmhealth-condition-api
- baseURL: https://ehr2.charmtracker.com/api/ehr/v2/fhir
  baseurl_source: declared
  description: Clinical documents
  name: CharmHealth DocumentReference API
  slug: charmhealth-documentreference-api
- baseURL: https://ehr2.charmtracker.com/api/ehr/v2/fhir
  baseurl_source: declared
  description: Patient encounters and visits
  name: CharmHealth Encounter API
  slug: charmhealth-encounter-api
- baseURL: https://ehr2.charmtracker.com/api/ehr/v2/fhir
  baseurl_source: declared
  description: Immunization records
  name: CharmHealth Immunization API
  slug: charmhealth-immunization-api
- baseURL: https://ehr2.charmtracker.com/api/ehr/v2/fhir
  baseurl_source: declared
  description: Medication orders
  name: CharmHealth MedicationRequest API
  slug: charmhealth-medicationrequest-api
- baseURL: https://ehr2.charmtracker.com/api/ehr/v2/fhir
  baseurl_source: declared
  description: Vital signs, lab results, and clinical observations
  name: CharmHealth Observation API
  slug: charmhealth-observation-api
- baseURL: https://ehr2.charmtracker.com/api/ehr/v2/fhir
  baseurl_source: declared
  description: Provider organizations
  name: CharmHealth Organization API
  slug: charmhealth-organization-api
- baseURL: https://ehr2.charmtracker.com/api/ehr/v2/fhir
  baseurl_source: declared
  description: Patient demographic resource
  name: CharmHealth Patient API
  slug: charmhealth-patient-api
- baseURL: https://ehr2.charmtracker.com/api/ehr/v2/fhir
  baseurl_source: declared
  description: Care providers
  name: CharmHealth Practitioner API
  slug: charmhealth-practitioner-api
artifact_total: 56
collections:
- collection_type: postman
  name: CharmHealth FHIR AllergyIntolerance API
  slug: postman-charmhealth-allergyintolerance-api
- collection_type: postman
  name: CharmHealth FHIR AllergyIntolerance Appointment API
  slug: postman-charmhealth-appointment-api
- collection_type: postman
  name: CharmHealth FHIR AllergyIntolerance Capability API
  slug: postman-charmhealth-capability-api
- collection_type: postman
  name: CharmHealth FHIR AllergyIntolerance CarePlan API
  slug: postman-charmhealth-careplan-api
- collection_type: postman
  name: CharmHealth FHIR AllergyIntolerance CareTeam API
  slug: postman-charmhealth-careteam-api
- collection_type: postman
  name: CharmHealth FHIR AllergyIntolerance Condition API
  slug: postman-charmhealth-condition-api
- collection_type: postman
  name: CharmHealth FHIR AllergyIntolerance DocumentReference API
  slug: postman-charmhealth-documentreference-api
- collection_type: postman
  name: CharmHealth FHIR AllergyIntolerance Encounter API
  slug: postman-charmhealth-encounter-api
- collection_type: postman
  name: CharmHealth FHIR AllergyIntolerance Immunization API
  slug: postman-charmhealth-immunization-api
- collection_type: postman
  name: CharmHealth FHIR AllergyIntolerance MedicationRequest API
  slug: postman-charmhealth-medicationrequest-api
- collection_type: postman
  name: CharmHealth FHIR AllergyIntolerance Observation API
  slug: postman-charmhealth-observation-api
- collection_type: postman
  name: CharmHealth FHIR AllergyIntolerance Organization API
  slug: postman-charmhealth-organization-api
- collection_type: postman
  name: CharmHealth FHIR AllergyIntolerance Patient API
  slug: postman-charmhealth-patient-api
- collection_type: postman
  name: CharmHealth FHIR AllergyIntolerance Practitioner API
  slug: postman-charmhealth-practitioner-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CharmHealth FHIR AllergyIntolerance API
  slug: open-charmhealth-allergyintolerance-api
- collection_type: open
  name: CharmHealth FHIR AllergyIntolerance Appointment API
  slug: open-charmhealth-appointment-api
- collection_type: open
  name: CharmHealth FHIR AllergyIntolerance Capability API
  slug: open-charmhealth-capability-api
- collection_type: open
  name: CharmHealth FHIR AllergyIntolerance CarePlan API
  slug: open-charmhealth-careplan-api
- collection_type: open
  name: CharmHealth FHIR AllergyIntolerance CareTeam API
  slug: open-charmhealth-careteam-api
- collection_type: open
  name: CharmHealth FHIR AllergyIntolerance Condition API
  slug: open-charmhealth-condition-api
- collection_type: open
  name: CharmHealth FHIR AllergyIntolerance DocumentReference API
  slug: open-charmhealth-documentreference-api
- collection_type: open
  name: CharmHealth FHIR AllergyIntolerance Encounter API
  slug: open-charmhealth-encounter-api
- collection_type: open
  name: CharmHealth FHIR API
  slug: open-charmhealth-fhir-api
- collection_type: open
  name: CharmHealth FHIR AllergyIntolerance Immunization API
  slug: open-charmhealth-immunization-api
- collection_type: open
  name: CharmHealth FHIR AllergyIntolerance MedicationRequest API
  slug: open-charmhealth-medicationrequest-api
- collection_type: open
  name: CharmHealth FHIR AllergyIntolerance Observation API
  slug: open-charmhealth-observation-api
- collection_type: open
  name: CharmHealth FHIR AllergyIntolerance Organization API
  slug: open-charmhealth-organization-api
- collection_type: open
  name: CharmHealth FHIR AllergyIntolerance Patient API
  slug: open-charmhealth-patient-api
- collection_type: open
  name: CharmHealth FHIR AllergyIntolerance Practitioner API
  slug: open-charmhealth-practitioner-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/charmhealth-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/charmhealth/overview
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


  CharmHealth''s developer surface includes authentication, documentation, product news, engineering blog, pricing, support, and 19 more developer resources.'
plans:
- name: Charmhealth Plans Pricing
  plan_count: 3
  slug: charmhealth-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Charmhealth Rate Limits
  slug: charmhealth-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: CharmHealth API Rules
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
  composite: 40.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 54.3
    catalog_earned_first_party: 0.0
    catalog_gap: 60.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.8
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 53.7
    developer_ergonomics: 10.7
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 41.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 60.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
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

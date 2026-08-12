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
- acting_count: 0
  human_in_the_loop: 0
  name: Penn Medicine Agentic Access
  operation_count: 22
  slug: penn-medicine-agentic-access
  summary_line: 22 operations
api_count: 7
apis:
- description: MyChart-based patient portal that gives Penn Medicine patients access to medical records, lab results, secure messaging with their care team, telehealth visits, medication refills, prescription manage
  name: MyPennMedicine Patient Portal
  slug: mypennmedicine-patient-portal
- description: 'EpicLink-based portal for community and referring physicians that provides secure access to Penn Medicine patient records: clinical notes, lab and imaging results, medication lists, and the ability to'
  name: PhysicianLink Referring Physician Portal
  slug: physicianlink-referring-physician-portal
- description: 'Penn Medicine and the Perelman School of Medicine publish open-source health-informatics software across several GitHub organizations: Penn Medicine Center for Health Care Innovation (Penn-Medicine-CH'
  name: Penn Medicine Open Source Health Informatics
  slug: penn-medicine-open-source-health-informatics
- description: HL7 FHIR Bulk Data Access (Flat FHIR) Group-level export.
  name: Penn Medicine Bulk Data API
  slug: penn-medicine-bulk-data-api
- description: Patient-mediated clinical and claims data resources required under CMS-9115-F.
  name: Penn Medicine Patient Access API
  slug: penn-medicine-patient-access-api
- description: Public provider, organization, location, and endpoint resources required under CMS-9115-F.
  name: Penn Medicine Provider Directory API
  slug: penn-medicine-provider-directory-api
- description: SMART on FHIR launch and discovery endpoints.
  name: Penn Medicine SMART API
  slug: penn-medicine-smart-api
artifact_total: 50
collections:
- collection_type: open
  name: Penn Medicine FHIR R4 API
  slug: open-penn-medicine-fhir-r4
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/penn-medicine-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/penn-medicine-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/penn-medicine-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/penn-medicine-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://www.pennmedicine.org
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fhir.epic.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Penn-Medicine-CHCI
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pennsignals
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PMACS
- group: company
  title: ''
  type: Blog
  url: https://www.pennmedicine.org/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pennmedicine.org/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pennmedicine.org/terms-of-use
- group: auth
  title: ''
  type: Compliance
  url: https://www.pennmedicine.org/for-health-care-professionals/for-physicians/electronic-medical-records
- group: operate
  title: ''
  type: Support
  url: https://www.pennmedicine.org/contact-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/penn-medicine
- group: design
  title: ''
  type: SpectralRules
  url: rules/penn-medicine-fhir-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/penn-medicine-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/penn-medicine-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/penn-medicine-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/penn-medicine-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/penn-medicine-finops.yml
created: '2026-05-23'
description: Penn Medicine is the University of Pennsylvania Health System (UPHS) plus the Perelman School of Medicine. It is an $11.9 billion enterprise powered by nearly 49,000 faculty and staff, operating six hospitals (Hospital of the University of Pennsylvania, Penn Presbyterian Medical Center, Chester County Hospital, Lancaster General Health, Princeton Health, and Pennsylvania Hospital — the first hospital in the United States, chartered in 1751) plus Penn Medicine at Home, Good Shepherd Penn Partners Rehabilitation, Lancaster Behavioral Health Hospital, and Princeton House Behavioral Health. The Perelman School of Medicine was awarded $580 million in NIH funding in fiscal year 2023. From an API perspective, Penn Medicine runs a production Epic-backed HL7 FHIR R4 endpoint at `https://ssproxy.pennhealth.com/PRD-FHIR/api/FHIR/R4` (Epic Organization ID 346, implementation description "University of Pennsylvania Health Systems FHIR Server"). The CapabilityStatement instantiates `us-core-server|6.1.0`
  and the HL7 Bulk Data Access IG, exposes 59 FHIR resource types covering Patient Access (clinical + claims) and Provider Directory per CMS-9115-F, and protects them with OAuth 2.0 / SMART-on-FHIR. Penn Medicine also operates the MyPennMedicine MyChart patient portal and the PhysicianLink referring-provider portal, and publishes open-source informatics work through several Perelman School of Medicine GitHub orgs (Penn-Medicine-CHCI, pennsignals, PMACS, pennbiobank).
examples:
- key_count: 5
  name: Penn Medicine Fhir Bulk Export Example
  slug: penn-medicine-fhir-bulk-export-example
- key_count: 9
  name: Penn Medicine Fhir Observation Example
  slug: penn-medicine-fhir-observation-example
- key_count: 10
  name: Penn Medicine Fhir Organization Example
  slug: penn-medicine-fhir-organization-example
- key_count: 11
  name: Penn Medicine Fhir Patient Example
  slug: penn-medicine-fhir-patient-example
- key_count: 8
  name: Penn Medicine Fhir Practitioner Example
  slug: penn-medicine-fhir-practitioner-example
features:
- description: HL7 FHIR R4 server with US Core 6.1.0 conformance and SMART on FHIR authorization, fulfilling CMS-9115-F Patient Access requirements.
  name: CMS-Compliant Patient Access FHIR API
- description: Unauthenticated FHIR resources for Practitioner, PractitionerRole, Organization, Location, and Endpoint.
  name: Public Provider Directory
- description: Group-level $export per the HL7 Bulk Data IG; supports backend services (client_credentials) authentication.
  name: HL7 Bulk Data Access
- description: CapabilityStatement advertises 59 resource types covering clinical, administrative, and financial data including AllergyIntolerance, Condition, Observation, MedicationRequest, Immunization, Procedure, Encounter, DiagnosticReport, DocumentReference, Coverage, ExplanationOfBenefit, and Claim.
  name: 59 FHIR Resource Types
- description: MyChart-based portal that fronts the FHIR surface for patients and their authorized apps.
  name: MyPennMedicine Patient Portal
- description: EpicLink portal for community physicians referring patients into UPHS.
  name: PhysicianLink for Referring Providers
finops:
- name: Penn Medicine Finops
  service_category: API
  slug: penn-medicine-finops
image: https://www.pennmedicine.org/-/media/global/global-logo.svg
integrations:
- description: UPHS's underlying EHR; the FHIR endpoint is served by Epic November 2025.
  name: Epic EHR
- description: Third-party app developers register apps at fhir.epic.com and target Penn Medicine (Organization ID 346).
  name: Epic on FHIR
- description: SMART on FHIR launch protocols for EHR-integrated and standalone apps.
  name: SMART App Launch
- description: Backend-services authentication and Group-level export.
  name: HL7 FHIR Bulk Data IG
- description: CapabilityStatement instantiates us-core-server profile.
  name: HL7 US Core 6.1.0
- description: Penn Medicine participated in Apple's 2018 launch of Health Records on iPhone, allowing patients to view FHIR-formatted records.
  name: Apple Health
- description: National interoperability framework Penn Medicine participates in for record retrieval across networks.
  name: Carequality
- description: Epic-to-Epic record exchange for connecting providers.
  name: Care Everywhere
json_schemas:
- name: Penn Medicine FHIR Observation
  property_count: 9
  slug: penn-medicine-fhir-observation
- name: Penn Medicine FHIR Organization
  property_count: 9
  slug: penn-medicine-fhir-organization
- name: Penn Medicine FHIR Patient
  property_count: 10
  slug: penn-medicine-fhir-patient
- name: Penn Medicine FHIR Practitioner
  property_count: 7
  slug: penn-medicine-fhir-practitioner
jsonld:
- class_count: 25
  name: Penn Medicine Context
  property_count: 0
  slug: penn-medicine-context
layout: provider
modified: '2026-05-23'
name: Penn Medicine
nav: Providers
network: true
overview: 'Penn Medicine publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Bulk Data API, Patient Access API, Provider Directory API, and 1 more. Tagged areas include Healthcare, Hospital, Academic Medical Center, FHIR, and SMART On FHIR.


  The Penn Medicine catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Penn Medicine''s developer surface includes authentication, developer portal, engineering blog, support, and 17 more developer resources.'
plans:
- name: Penn Medicine Plans Pricing
  plan_count: 3
  slug: penn-medicine-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 3
  name: Penn Medicine Rate Limits
  slug: penn-medicine-rate-limits
rules:
- name: Penn Medicine API Rules
  rule_count: 4
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 2
  slug: penn-medicine-fhir-rules
- name: Penn Medicine API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: penn-medicine-jsonschema-spectral-rules
scopes:
- name: Penn Medicine Scopes
  scope_count: 6
  slug: penn-medicine-scopes
  summary_line: 6 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 52.7
  delta: -0.6
  facets:
    commercial_clarity: 68.4
    contract_quality: 70.9
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 31.3
    operational_transparency: 36.8
  previous_composite: 53.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/penn-medicine/refs/heads/main/screenshots/penn-medicine-2026-06-20T191538.png
security:
- kind: authentication
  name: Penn Medicine Authentication
  slug: penn-medicine-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Penn Medicine Domain Security
  slug: penn-medicine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: penn-medicine
solutions:
- description: CMS-mandated patient-mediated data access surface for UPHS patients.
  name: Patient Access
- description: CMS-mandated public provider directory surface.
  name: Provider Directory
- description: Population-scale FHIR data extraction for approved partners.
  name: Bulk Data Analytics
- description: Open-source Cobalt platform from Penn Medicine CHCI delivering employee mental health and well-being services.
  name: Connected Mental Health (Cobalt)
tags:
- Healthcare
- Hospital
- Academic Medical Center
- FHIR
- SMART On FHIR
- Patient Access
- Provider Directory
- CMS Interoperability
- US Core
- Bulk Data
- Epic
use_cases:
- description: Patients authorize third-party PHR and care-coordination apps to pull their complete clinical and claims history from Penn Medicine via SMART on FHIR.
  name: Patient-Mediated Data Download
- description: Approved EHR-launched and standalone SMART apps surface Penn Medicine clinical data inside referring-provider, payer, and longitudinal-care tools.
  name: Care-Coordination Apps
- description: Approved system-level clients run Group-level $export to extract de-identified cohorts for quality measurement, research, and risk modeling.
  name: Population Analytics
- description: Payers, referral platforms, and health information exchanges consume the public Provider Directory bundle without authentication.
  name: Provider Directory Distribution
- description: PhysicianLink gives credentialed community physicians read access to UPHS records for shared patients.
  name: Referring Provider EMR Access
website: https://fhir.epic.com
---

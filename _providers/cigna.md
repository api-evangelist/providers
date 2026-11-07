---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cigna Agentic Access
  operation_count: 22
  slug: cigna-agentic-access
  summary_line: 22 operations
api_count: 4
apis:
- baseURL: https://fhir.cigna.com/PatientAccess/v1
  baseurl_source: declared
  description: The Bulk Data API from Cigna — 1 operation(s) for bulk data.
  name: Cigna Bulk Data API
  slug: cigna-bulk-data-api
- baseURL: https://fhir.cigna.com/PatientAccess/v1
  baseurl_source: declared
  description: The Condition API from Cigna — 1 operation(s) for condition.
  name: Cigna Condition API
  slug: cigna-condition-api
- baseURL: https://fhir.cigna.com/PatientAccess/v1
  baseurl_source: declared
  description: The Coverage API from Cigna — 1 operation(s) for coverage.
  name: Cigna Coverage API
  slug: cigna-coverage-api
- baseURL: https://fhir.cigna.com/PatientAccess/v1
  baseurl_source: declared
  description: The Encounter API from Cigna — 1 operation(s) for encounter.
  name: Cigna Encounter API
  slug: cigna-encounter-api
- baseURL: https://fhir.cigna.com/PatientAccess/v1
  baseurl_source: declared
  description: The ExplanationOfBenefit API from Cigna — 1 operation(s) for explanationofbenefit.
  name: Cigna ExplanationOfBenefit API
  slug: cigna-explanationofbenefit-api
- baseURL: https://fhir.cigna.com/PatientAccess/v1
  baseurl_source: declared
  description: The Location API from Cigna — 1 operation(s) for location.
  name: Cigna Location API
  slug: cigna-location-api
- baseURL: https://fhir.cigna.com/PatientAccess/v1
  baseurl_source: declared
  description: The MedicationKnowledge API from Cigna — 1 operation(s) for medicationknowledge.
  name: Cigna MedicationKnowledge API
  slug: cigna-medicationknowledge-api
- baseURL: https://fhir.cigna.com/PatientAccess/v1
  baseurl_source: declared
  description: The Observation API from Cigna — 1 operation(s) for observation.
  name: Cigna Observation API
  slug: cigna-observation-api
- baseURL: https://fhir.cigna.com/PatientAccess/v1
  baseurl_source: declared
  description: The Organization API from Cigna — 1 operation(s) for organization.
  name: Cigna Organization API
  slug: cigna-organization-api
- baseURL: https://fhir.cigna.com/PatientAccess/v1
  baseurl_source: declared
  description: The Patient API from Cigna — 4 operation(s) for patient.
  name: Cigna Patient API
  slug: cigna-patient-api
- baseURL: https://fhir.cigna.com/PatientAccess/v1
  baseurl_source: declared
  description: The Practitioner API from Cigna — 2 operation(s) for practitioner.
  name: Cigna Practitioner API
  slug: cigna-practitioner-api
- baseURL: https://fhir.cigna.com/PatientAccess/v1
  baseurl_source: declared
  description: The Healthcare Service API from Cigna — 1 operation(s) for healthcare service.
  name: Cigna Healthcare Service API
  slug: cigna-healthcare-service-api
- baseURL: https://fhir.cigna.com/PatientAccess/v1
  baseurl_source: declared
  description: The Insurance Plan API from Cigna — 2 operation(s) for insurance plan.
  name: Cigna Insurance Plan API
  slug: cigna-insurance-plan-api
- baseURL: https://fhir.cigna.com/PatientAccess/v1
  baseurl_source: declared
  description: The Medication Request API from Cigna — 1 operation(s) for medication request.
  name: Cigna Medication Request API
  slug: cigna-medication-request-api
- baseURL: https://fhir.cigna.com/PatientAccess/v1
  baseurl_source: declared
  description: The Practitioner Role API from Cigna — 1 operation(s) for practitioner role.
  name: Cigna Practitioner Role API
  slug: cigna-practitioner-role-api
artifact_total: 61
collections:
- collection_type: postman
  name: Cigna Drug Formulary Bulk Data API
  slug: postman-cigna-bulk-data-api
- collection_type: postman
  name: Cigna Drug Formulary Bulk Data Condition API
  slug: postman-cigna-condition-api
- collection_type: postman
  name: Cigna Drug Formulary Bulk Data Coverage API
  slug: postman-cigna-coverage-api
- collection_type: postman
  name: Cigna Drug Formulary Bulk Data Encounter API
  slug: postman-cigna-encounter-api
- collection_type: postman
  name: Cigna Drug Formulary Bulk Data ExplanationOfBenefit API
  slug: postman-cigna-explanationofbenefit-api
- collection_type: postman
  name: Cigna Drug Formulary Bulk Data HealthcareService API
  slug: postman-cigna-healthcareservice-api
- collection_type: postman
  name: Cigna Drug Formulary Bulk Data InsurancePlan API
  slug: postman-cigna-insuranceplan-api
- collection_type: postman
  name: Cigna Drug Formulary Bulk Data Location API
  slug: postman-cigna-location-api
- collection_type: postman
  name: Cigna Drug Formulary Bulk Data MedicationKnowledge API
  slug: postman-cigna-medicationknowledge-api
- collection_type: postman
  name: Cigna Drug Formulary Bulk Data MedicationRequest API
  slug: postman-cigna-medicationrequest-api
- collection_type: postman
  name: Cigna Drug Formulary Bulk Data Observation API
  slug: postman-cigna-observation-api
- collection_type: postman
  name: Cigna Drug Formulary Bulk Data Organization API
  slug: postman-cigna-organization-api
- collection_type: postman
  name: Cigna Drug Formulary Bulk Data Patient API
  slug: postman-cigna-patient-api
- collection_type: postman
  name: Cigna Drug Formulary Bulk Data Practitioner API
  slug: postman-cigna-practitioner-api
- collection_type: postman
  name: Cigna Drug Formulary Bulk Data PractitionerRole API
  slug: postman-cigna-practitionerrole-api
- collection_type: open
  name: Cigna Drug Formulary Bulk Data API
  slug: open-cigna-bulk-data-api
- collection_type: open
  name: Cigna Drug Formulary Bulk Data Condition API
  slug: open-cigna-condition-api
- collection_type: open
  name: Cigna Drug Formulary Bulk Data Coverage API
  slug: open-cigna-coverage-api
- collection_type: open
  name: Cigna Drug Formulary API
  slug: open-cigna-drug-formulary-api
- collection_type: open
  name: Cigna Drug Formulary Bulk Data Encounter API
  slug: open-cigna-encounter-api
- collection_type: open
  name: Cigna Drug Formulary Bulk Data ExplanationOfBenefit API
  slug: open-cigna-explanationofbenefit-api
- collection_type: open
  name: Cigna Drug Formulary Bulk Data HealthcareService API
  slug: open-cigna-healthcareservice-api
- collection_type: open
  name: Cigna Drug Formulary Bulk Data InsurancePlan API
  slug: open-cigna-insuranceplan-api
- collection_type: open
  name: Cigna Drug Formulary Bulk Data Location API
  slug: open-cigna-location-api
- collection_type: open
  name: Cigna Drug Formulary Bulk Data MedicationKnowledge API
  slug: open-cigna-medicationknowledge-api
- collection_type: open
  name: Cigna Drug Formulary Bulk Data MedicationRequest API
  slug: open-cigna-medicationrequest-api
- collection_type: open
  name: Cigna Drug Formulary Bulk Data Observation API
  slug: open-cigna-observation-api
- collection_type: open
  name: Cigna Drug Formulary Bulk Data Organization API
  slug: open-cigna-organization-api
- collection_type: open
  name: Cigna Patient Access API
  slug: open-cigna-patient-access-api
- collection_type: open
  name: Cigna Drug Formulary Bulk Data Patient API
  slug: open-cigna-patient-api
- collection_type: open
  name: Cigna Drug Formulary Bulk Data Practitioner API
  slug: open-cigna-practitioner-api
- collection_type: open
  name: Cigna Drug Formulary Bulk Data PractitionerRole API
  slug: open-cigna-practitionerrole-api
- collection_type: open
  name: Cigna Provider Access API
  slug: open-cigna-provider-access-api
- collection_type: open
  name: Cigna Provider Directory API
  slug: open-cigna-provider-directory-api
common:
- group: commercial
  href: https://artifacts.apis.io/cigna/plans/cigna-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cigna-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cigna/rate-limits/cigna-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cigna-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cigna/finops/cigna-finops.yml
  title: ''
  type: FinOps
  url: finops/cigna-finops.yml
- group: other
  href: https://artifacts.apis.io/cigna/capabilities/cigna-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cigna-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/cigna/overview
- group: agent
  href: https://artifacts.apis.io/cigna/agentic-access/cigna-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cigna-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cigna/security/cigna-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cigna-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cigna/security/cigna-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cigna-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cigna/security/cigna-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cigna-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cigna/authentication/cigna-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cigna-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cigna/scopes/cigna-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cigna-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cigna
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-cigna-group
- group: company
  title: ''
  type: Website
  url: https://www.cigna.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cigna.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.cigna.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.cigna.com/docs/service-apis
- group: operate
  title: ''
  type: Support
  url: https://developer.cigna.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cigna.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cigna.com/legal/privacy
- group: design
  href: https://artifacts.apis.io/cigna/json-ld/cigna-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/cigna-context.jsonld
- group: docs
  href: https://artifacts.apis.io/cigna/json-schema/cigna-patient-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/cigna-patient-schema.json
- group: design
  href: https://artifacts.apis.io/cigna/spectral/cigna-spectral.yml
  title: ''
  type: Spectral
  url: spectral/cigna-spectral.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.cigna.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://newsroom.cigna.com/
created: '2025-02-21'
description: Cigna Healthcare is a leading global health services company offering medical, dental, behavioral, and pharmacy plans for individuals, families, and employers. The Cigna Developer Portal exposes CMS-mandated FHIR APIs for Patient Access, Provider Directory, Drug Formulary, and Provider Access, along with member and provider service APIs that enable third-party applications, electronic health record systems, and partners to access member health data with consent and look up Cigna network providers and formulary information.
finops:
- has_sources: true
  method: generated
  name: Cigna Finops
  primary_unit: ''
  service_category: Healthcare / Health Insurance
  slug: cigna-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cigna.png
json_schemas:
- name: CignaPatient
  property_count: 10
  slug: cigna-patient
jsonld:
- class_count: 0
  name: Cigna Context
  property_count: 8
  slug: cigna-context
layout: provider
modified: '2026-05-19'
name: Cigna
nav: Providers
network: true
overview: 'Cigna publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bulk Data API, Condition API, Coverage API, and 12 more. Tagged areas include CMS Interoperability, Da Vinci, Drug Formulary, FHIR, and Health Insurance.


  The Cigna catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cigna''s developer surface includes authentication, developer portal, documentation, support, engineering blog, and 20 more developer resources.'
plans:
- name: Cigna Plans Pricing
  plan_count: 3
  slug: cigna-plans-pricing
press:
- date: ''
  title: Cigna Corporation's Second Quarter 2020 Earnings Release Details
  url: https://www.cigna.com/newsroom/news-releases/2020/cigna-corporations-second-quarter-2020-earnings-release-details.html
- date: ''
  title: Cigna Names Noelle Eder, Global Chief Information Officer
  url: https://www.cigna.com/newsroom/news-releases/2020/cigna-names-noelle-eder-global-chief-information-officer.html
- date: ''
  title: Cigna Launches Evernorth To Accelerate Delivery Of Innovative And Flexible Health Service Solutions
  url: https://www.cigna.com/newsroom/news-releases/2020/cigna-launches-evernorth-to-accelerate-delivery-of-innovative-and-flexible-health-service-solutions.html
- date: ''
  title: Cigna Affordable Care Act Health Plans to Expand into 63 New Counties Across North Carolina for 2021
  url: https://www.cigna.com/newsroom/news-releases/2020/cigna-affordable-care-act-health-plans-to-expand-into-63-new-counties-across-north-carolina-for-2021.html
- date: ''
  title: Cigna launches new generative AI assistant for members
  url: https://www.healthcaredive.com/news/cigna-launches-generative-ai-member-assistant/750480/
- date: ''
  title: Cigna Healthcare Unveils Industry-Leading AI-Powered ...
  url: https://www.prnewswire.com/news-releases/cigna-healthcare-unveils-industry-leading-ai-powered-digital-tools-for-a-simple-and-reliable-customer-experience-302479742.html
- date: ''
  title: Cigna and Earvin "Magic" Johnson Join Forces to Combat Health Disparities and Support Minority and Women-Owned Businesses
  url: https://www.cigna.com/newsroom/news-releases/2020/cigna-and-earvin-magic-johnson-join-forces-to-combat-health-disparities-and-support-minority-and-women-owned-businesses.html
- date: ''
  title: Cigna Corporation Announces Appearance at the Credit Suisse 29th Annual Healthcare Conference
  url: https://www.cigna.com/newsroom/news-releases/2020/cigna-corporation-announces-appearance-at-the-credit-suisse-29th-annual-healthcare-conference.html
random_paper: 10
rate_limits:
- limit_count: 2
  name: Cigna Rate Limits
  slug: cigna-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Cigna — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cigna-jsonschema-spectral-rules
scopes:
- name: Cigna Scopes
  scope_count: 6
  slug: cigna-scopes
  summary_line: 6 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 32.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 53.3
    catalog_earned_first_party: 0.0
    catalog_gap: 61.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 46.7
    developer_ergonomics: 15.5
    discoverability: 78.6
    operational_transparency: 18.4
  previous_composite: 32.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 35.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/cigna/cigna-2026-06-20T174340.png
security:
- kind: authentication
  name: Cigna Authentication
  slug: cigna-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Cigna Domain Security
  slug: cigna-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cigna Vulnerability Disclosure
  slug: cigna-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Cigna Trust Center
  slug: cigna-trust-center
  summary_line: SOC 2, HIPAA
slug: cigna
tags:
- CMS Interoperability
- Da Vinci
- Drug Formulary
- FHIR
- Health Insurance
- Healthcare
- Patient Access
- Provider Directory
- SMART on FHIR
- Fortune 100
website: https://www.cigna.com/
---

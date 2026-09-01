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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.2
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Wellcare Health Plans Agentic Access
  operation_count: 15
  slug: wellcare-health-plans-agentic-access
  summary_line: 15 operations
api_count: 2
apis:
- description: Member diagnosed conditions and clinical data.
  name: wellcare-health-plans Condition API
  slug: wellcare-health-plans-condition-api
- description: Member insurance coverage and enrollment information.
  name: wellcare-health-plans Coverage API
  slug: wellcare-health-plans-coverage-api
- description: Member care encounters and visits.
  name: wellcare-health-plans Encounter API
  slug: wellcare-health-plans-encounter-api
- description: Claims and EOB data for medical, pharmacy, dental, and vision.
  name: wellcare-health-plans Explanation of Benefits API
  slug: wellcare-health-plans-explanation-of-benefits-api
- description: Immunization records and history.
  name: wellcare-health-plans Immunization API
  slug: wellcare-health-plans-immunization-api
- description: Insurance plan details including networks and coverage areas.
  name: wellcare-health-plans Insurance Plan API
  slug: wellcare-health-plans-insurance-plan-api
- description: Physical care delivery locations and addresses.
  name: wellcare-health-plans Location API
  slug: wellcare-health-plans-location-api
- description: Prescribed medications and medication orders.
  name: wellcare-health-plans Medication Request API
  slug: wellcare-health-plans-medication-request-api
- description: Clinical observations, lab results, and vital signs.
  name: wellcare-health-plans Observation API
  slug: wellcare-health-plans-observation-api
- description: Healthcare organizations, hospitals, and facilities.
  name: wellcare-health-plans Organization API
  slug: wellcare-health-plans-organization-api
- description: Patient demographic and identity resources.
  name: wellcare-health-plans Patient API
  slug: wellcare-health-plans-patient-api
- description: Individual healthcare practitioners and clinicians.
  name: wellcare-health-plans Practitioner API
  slug: wellcare-health-plans-practitioner-api
- description: A practitioner's role within an organization and network.
  name: wellcare-health-plans Practitioner Role API
  slug: wellcare-health-plans-practitioner-role-api
artifact_total: 45
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: WellCare FHIR Patient Access API
  slug: open-wellcare-fhir-patient-access-api
- collection_type: open
  name: WellCare FHIR Provider Directory API
  slug: open-wellcare-fhir-provider-directory-api
- collection_type: open
  name: WellCare FHIR Patient Access Condition API
  slug: open-wellcare-health-plans-condition-api
- collection_type: open
  name: WellCare FHIR Patient Access Condition Coverage API
  slug: open-wellcare-health-plans-coverage-api
- collection_type: open
  name: WellCare FHIR Patient Access Condition Encounter API
  slug: open-wellcare-health-plans-encounter-api
- collection_type: open
  name: WellCare FHIR Patient Access Condition Explanation of Benefits API
  slug: open-wellcare-health-plans-explanation-of-benefits-api
- collection_type: open
  name: WellCare FHIR Patient Access Condition Immunization API
  slug: open-wellcare-health-plans-immunization-api
- collection_type: open
  name: WellCare FHIR Patient Access Condition Insurance Plan API
  slug: open-wellcare-health-plans-insurance-plan-api
- collection_type: open
  name: WellCare FHIR Patient Access Condition Location API
  slug: open-wellcare-health-plans-location-api
- collection_type: open
  name: WellCare FHIR Patient Access Condition Medication Request API
  slug: open-wellcare-health-plans-medication-request-api
- collection_type: open
  name: WellCare FHIR Patient Access Condition Observation API
  slug: open-wellcare-health-plans-observation-api
- collection_type: open
  name: WellCare FHIR Patient Access Condition Organization API
  slug: open-wellcare-health-plans-organization-api
- collection_type: open
  name: WellCare FHIR Access Condition Patient API
  slug: open-wellcare-health-plans-patient-api
- collection_type: open
  name: WellCare FHIR Patient Access Condition Practitioner API
  slug: open-wellcare-health-plans-practitioner-api
- collection_type: open
  name: WellCare FHIR Patient Access Condition Practitioner Role API
  slug: open-wellcare-health-plans-practitioner-role-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/centene-corporation/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wellcare-health-plans-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wellcare-health-plans-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wellcare-health-plans-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/wellcare-health-plans-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wellcare
- group: company
  title: ''
  type: Website
  url: https://www.wellcare.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://partners.centene.com/apis
- group: start
  title: ''
  type: InteroperabilityPortal
  url: https://www.wellcare.com/en/interoperability-and-patient-access
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/wellcare-health-plans
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/wellcare-health-plans-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/wellcare-health-plans-vocabulary.yml
description: WellCare Health Plans was a managed care company that focused exclusively on government-sponsored managed care services through Medicaid, Medicare Advantage, and Medicare Prescription Drug Plans before being acquired by Centene Corporation. Now operating under Centene, WellCare provides FHIR- compliant APIs for interoperability and patient access as required by CMS Interoperability and Patient Access final rules (CMS-9115-F). The Centene Developer Partner Portal at partners.centene.com/apis provides access to WellCare FHIR APIs.
examples:
- key_count: 2
  name: Wellcare Fhir Patient Access Api Getpatient Example
  slug: wellcare-fhir-patient-access-api-getPatient-example
- key_count: 2
  name: Wellcare Fhir Patient Access Api Listexplanationofbenefit Example
  slug: wellcare-fhir-patient-access-api-listExplanationOfBenefit-example
- key_count: 2
  name: Wellcare Fhir Provider Directory Api Searchpractitioners Example
  slug: wellcare-fhir-provider-directory-api-searchPractitioners-example
finops:
- name: Wellcare Health Plans Finops
  service_category: API
  slug: wellcare-health-plans-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wellcare-health-plans.png
json_schemas:
- name: WellCare FHIR Explanation of Benefit
  property_count: 9
  slug: wellcare-fhir-eob
- name: WellCare FHIR Patient
  property_count: 9
  slug: wellcare-fhir-patient
json_structures:
- name: Wellcare Fhir Patient Structure
  property_count: 0
  slug: wellcare-fhir-patient-structure
jsonld:
- class_count: 7
  name: Wellcare Health Plans Context
  property_count: 27
  slug: wellcare-health-plans-context
layout: provider
modified: '2026-05-19'
name: WellCare Health Plans
nav: Providers
network: true
overview: 'WellCare Health Plans publishes 13 APIs on the [APIs.io](https://apis.io/) network, including wellcare-health-plans Condition API, wellcare-health-plans Coverage API, wellcare-health-plans Encounter API, and 10 more. Tagged areas include Fortune 500.


  The WellCare Health Plans catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  WellCare Health Plans'' developer surface includes authentication and 11 more developer resources.'
plans:
- name: Wellcare Health Plans Plans Pricing
  plan_count: 3
  slug: wellcare-health-plans-plans-pricing
press:
- date: '2026-05-25'
  title: Centene Completes Acquisition of Apixio - Dec 8, 2020
  url: https://investors.centene.com/2020-12-08-Centene-Completes-Acquisition-of-Apixio
- date: '2026-05-25'
  title: Cohere Health Adds Dr. Mark Leenay to Board of Directors ...
  url: https://www.prnewswire.com/news-releases/cohere-health-adds-dr-mark-leenay-to-board-of-directors-to-advance-clinical-ai-leadership-and-health-plan-collaborations-302694925.html
- date: '2026-05-25'
  title: WellCare Health Plans, Inc.
  url: https://www.sec.gov/enforcement-litigation/litigation-releases/lr-21044
- date: '2026-05-25'
  title: Wellcare Enhances Offering of Affordable, Quality ...
  url: https://www.prnewswire.com/news-releases/wellcare-enhances-offering-of-affordable-quality-medicare-advantage-and-medicare-prescription-drug-plans-in-2026-302582597.html
- date: '2026-05-25'
  title: Wellcare Announces Refreshed Brand in Effort to Better ...
  url: https://www.prnewswire.com/news-releases/wellcare-announces-refreshed-brand-in-effort-to-better-serve-medicare-members-301366933.html
random_paper: 9
rate_limits:
- limit_count: 5
  name: Wellcare Health Plans Rate Limits
  slug: wellcare-health-plans-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: WellCare Health Plans API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: wellcare-health-plans-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: WellCare Health Plans API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 1
    info: 0
    warn: 5
  slug: wellcare-health-plans-rules
scopes:
- name: Wellcare Health Plans Scopes
  scope_count: 8
  slug: wellcare-health-plans-scopes
  summary_line: 8 scopes · authorizationCode
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 19
    catalog_gap: 46.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 74.2
    developer_ergonomics: 21.4
    discoverability: 53.7
    governance: 28.8
    operational_transparency: 13.2
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wellcare-health-plans/refs/heads/main/screenshots/wellcare-health-plans-2026-08-17T082908.png
security:
- kind: authentication
  name: Wellcare Health Plans Authentication
  slug: wellcare-health-plans-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Wellcare Health Plans Domain Security
  slug: wellcare-health-plans-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wellcare-health-plans
tags:
- Fortune 500
website: https://www.wellcare.com
---

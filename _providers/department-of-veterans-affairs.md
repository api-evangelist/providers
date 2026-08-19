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
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Department Of Veterans Affairs Agentic Access
  operation_count: 21
  slug: department-of-veterans-affairs-agentic-access
  summary_line: 21 operations · 5 acting
api_count: 30
apis:
- description: Verify and standardize U.S. and international addresses for Veterans and their families.
  name: VA Address Validation API
  slug: va-address-validation-api
- description: Retrieve VA-generated benefit documents (decision letters, award letters, certifications) for Veterans.
  name: VA Benefits Documents API
  slug: va-benefits-documents-api
- description: Reference data lookups for benefits-claim form fields (countries, states, disabilities, treatment centers, etc.).
  name: VA Benefits Reference Data API
  slug: va-benefits-reference-data-api
- description: Determine whether a Veteran is eligible for community-care services under VA referral programs.
  name: VA Community Care Eligibility API
  slug: va-community-care-eligibility-api
- description: Submit supplemental claims, higher-level reviews, and Notices of Disagreement under appeals modernization.
  name: VA Decision Reviews API
  slug: va-decision-reviews-api
- description: Read and update a Veteran's direct-deposit information for benefit payments.
  name: VA Direct Deposit Management API
  slug: va-direct-deposit-management-api
- description: Submit and track GI Bill and VA education benefit applications and entitlement data.
  name: VA Education Benefits API
  slug: va-education-benefits-api
- description: Access VA-guaranteed home-loan eligibility, certificates of eligibility (COE), and loan data.
  name: VA Loan Guaranty API
  slug: va-loan-guaranty-api
- description: Lender-facing API for review, conditions, and modification of VA-guaranteed home loans.
  name: VA Loan Review API
  slug: va-loan-review-api
- description: Submit and track guaranty remittance payments for VA-guaranteed loans.
  name: VA Guaranty Remittance API
  slug: va-guaranty-remittance-api
- description: Generate official VA letters (e.g. service verification, benefit summary) on demand.
  name: VA Letter Generator API
  slug: va-letter-generator-api
- description: Veteran-authorized SMART-on-FHIR API exposing the patient's own health record.
  name: VA Patient Health API (FHIR)
  slug: va-patient-health-fhir-api
- description: Retrieve a Veteran's service history and eligibility for VA programs.
  name: VA Veteran Service History and Eligibility API
  slug: va-veteran-service-history-and-eligibility-api
- description: The AllergyIntolerance API from Department of Veterans Affairs (VA) — 1 operation(s) for allergyintolerance.
  name: Department of Veterans Affairs (VA) AllergyIntolerance API
  slug: department-of-veterans-affairs-allergyintolerance-api
- description: Appeals status and history
  name: Department of Veterans Affairs (VA) Appeals API
  slug: department-of-veterans-affairs-appeals-api
- description: Veteran benefits claims operations
  name: Department of Veterans Affairs (VA) Claims API
  slug: department-of-veterans-affairs-claims-api
- description: The Condition API from Department of Veterans Affairs (VA) — 1 operation(s) for condition.
  name: Department of Veterans Affairs (VA) Condition API
  slug: department-of-veterans-affairs-condition-api
- description: Veteran status confirmation
  name: Department of Veterans Affairs (VA) Confirmation API
  slug: department-of-veterans-affairs-confirmation-api
- description: Search and retrieve VA facilities
  name: Department of Veterans Affairs (VA) Facilities API
  slug: department-of-veterans-affairs-facilities-api
- description: Search and retrieve VA forms
  name: Department of Veterans Affairs (VA) Forms API
  slug: department-of-veterans-affairs-forms-api
- description: Intent to File operations
  name: Department of Veterans Affairs (VA) Intent To File API
  slug: department-of-veterans-affairs-intent-to-file-api
- description: The MedicationRequest API from Department of Veterans Affairs (VA) — 1 operation(s) for medicationrequest.
  name: Department of Veterans Affairs (VA) MedicationRequest API
  slug: department-of-veterans-affairs-medicationrequest-api
- description: Locate facilities near a given address or coordinates
  name: Department of Veterans Affairs (VA) NearbyFacilities API
  slug: department-of-veterans-affairs-nearbyfacilities-api
- description: The Observation API from Department of Veterans Affairs (VA) — 1 operation(s) for observation.
  name: Department of Veterans Affairs (VA) Observation API
  slug: department-of-veterans-affairs-observation-api
- description: The Patient API from Department of Veterans Affairs (VA) — 1 operation(s) for patient.
  name: Department of Veterans Affairs (VA) Patient API
  slug: department-of-veterans-affairs-patient-api
- description: Representation requests and POA management
  name: Department of Veterans Affairs (VA) Power of Attorney API
  slug: department-of-veterans-affairs-power-of-attorney-api
- description: Health, benefits, and other services offered at facilities
  name: Department of Veterans Affairs (VA) Services API
  slug: department-of-veterans-affairs-services-api
- description: Request upload locations
  name: Department of Veterans Affairs (VA) UploadLocation API
  slug: department-of-veterans-affairs-uploadlocation-api
- description: Submission status retrieval
  name: Department of Veterans Affairs (VA) UploadStatus API
  slug: department-of-veterans-affairs-uploadstatus-api
- description: The Veterans API from Department of Veterans Affairs (VA) — 1 operation(s) for veterans.
  name: Department of Veterans Affairs (VA) Veterans API
  slug: department-of-veterans-affairs-veterans-api
artifact_total: 74
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: VA Appeals Status AllergyIntolerance API
  slug: open-department-of-veterans-affairs-allergyintolerance-api
- collection_type: open
  name: VA Status AllergyIntolerance Appeals API
  slug: open-department-of-veterans-affairs-appeals-api
- collection_type: open
  name: VA Appeals Status AllergyIntolerance Claims API
  slug: open-department-of-veterans-affairs-claims-api
- collection_type: open
  name: VA Appeals Status AllergyIntolerance Condition API
  slug: open-department-of-veterans-affairs-condition-api
- collection_type: open
  name: VA Appeals Status AllergyIntolerance Confirmation API
  slug: open-department-of-veterans-affairs-confirmation-api
- collection_type: open
  name: VA Appeals Status AllergyIntolerance Facilities API
  slug: open-department-of-veterans-affairs-facilities-api
- collection_type: open
  name: VA Appeals Status AllergyIntolerance Forms API
  slug: open-department-of-veterans-affairs-forms-api
- collection_type: open
  name: VA Appeals Status AllergyIntolerance Intent To File API
  slug: open-department-of-veterans-affairs-intent-to-file-api
- collection_type: open
  name: VA Appeals Status AllergyIntolerance MedicationRequest API
  slug: open-department-of-veterans-affairs-medicationrequest-api
- collection_type: open
  name: VA Appeals Status AllergyIntolerance NearbyFacilities API
  slug: open-department-of-veterans-affairs-nearbyfacilities-api
- collection_type: open
  name: VA Appeals Status AllergyIntolerance Observation API
  slug: open-department-of-veterans-affairs-observation-api
- collection_type: open
  name: VA Appeals Status AllergyIntolerance Patient API
  slug: open-department-of-veterans-affairs-patient-api
- collection_type: open
  name: VA Appeals Status AllergyIntolerance Power of Attorney API
  slug: open-department-of-veterans-affairs-power-of-attorney-api
- collection_type: open
  name: VA Appeals Status AllergyIntolerance Services API
  slug: open-department-of-veterans-affairs-services-api
- collection_type: open
  name: VA Appeals Status AllergyIntolerance UploadLocation API
  slug: open-department-of-veterans-affairs-uploadlocation-api
- collection_type: open
  name: VA Appeals Status AllergyIntolerance UploadStatus API
  slug: open-department-of-veterans-affairs-uploadstatus-api
- collection_type: open
  name: VA Appeals Status AllergyIntolerance Veterans API
  slug: open-department-of-veterans-affairs-veterans-api
- collection_type: open
  name: VA Appeals Status API
  slug: open-va-appeals-status-api
- collection_type: open
  name: VA Benefits Claims API
  slug: open-va-benefits-claims-api
- collection_type: open
  name: VA Benefits Intake API
  slug: open-va-benefits-intake-api
- collection_type: open
  name: VA Clinical Health API (FHIR)
  slug: open-va-clinical-health-fhir-api
- collection_type: open
  name: VA Facilities API
  slug: open-va-facilities-api
- collection_type: open
  name: VA Forms API
  slug: open-va-forms-api
- collection_type: open
  name: VA Veteran Confirmation API
  slug: open-va-veteran-confirmation-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/department-of-veterans-affairs-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/department-of-veterans-affairs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/department-of-veterans-affairs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/department-of-veterans-affairs-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/department-of-veterans-affairs-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/department-of-veterans-affairs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/department-of-veterans-affairs
- group: start
  title: ''
  type: Portal
  url: https://developer.va.gov/
- group: operate
  title: ''
  type: FAQ
  url: https://developer.va.gov/support/faq
- group: operate
  title: ''
  type: Support
  url: https://developer.va.gov/support/contact-us
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.va.gov/onboarding
- group: company
  title: ''
  type: Blog
  url: https://news.va.gov/feed/
created: '2024-01-01'
description: The Department of Veterans Affairs (VA) provides health care, benefits, and memorial services to U.S. military Veterans and their families. The VA API Platform at developer.va.gov publishes a structured catalog of APIs spanning Veteran identity confirmation, benefits claims, appeals, document intake, education, loan guaranty, facilities, forms, and HL7 FHIR clinical health data.
examples:
- key_count: 1
  name: Claim Example
  slug: claim-example
- key_count: 1
  name: Facility Example
  slug: facility-example
- key_count: 1
  name: Form Example
  slug: form-example
finops:
- name: Department Of Veterans Affairs Finops
  service_category: Public-Sector / Government API
  slug: department-of-veterans-affairs-finops
image: https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/apis-json.png
json_schemas:
- name: VA Appeal
  property_count: 3
  slug: va-appeal
- name: VA Benefits Claim
  property_count: 3
  slug: va-claim
- name: VA Facility
  property_count: 3
  slug: va-facility
- name: VA Form
  property_count: 3
  slug: va-form
- name: Veteran Confirmation
  property_count: 1
  slug: va-veteran-confirmation
jsonld:
- class_count: 0
  name: Va Context
  property_count: 7
  slug: va-context
layout: provider
modified: '2026-05-19'
name: Department of Veterans Affairs (VA)
nav: Providers
network: true
overview: 'Department of Veterans Affairs (VA) publishes 17 APIs on the [APIs.io](https://apis.io/) network, including AllergyIntolerance API, Appeals API, Claims API, and 14 more. Tagged areas include Federal Government, Healthcare, and Veterans.


  The Department of Veterans Affairs (VA) catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Department of Veterans Affairs (VA)''s developer surface includes authentication, developer portal, FAQ, support, getting-started guide, engineering blog, and 6 more developer resources.'
plans:
- name: Department Of Veterans Affairs Plans Pricing
  plan_count: 2
  slug: department-of-veterans-affairs-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 2
  name: Department Of Veterans Affairs Rate Limits
  slug: department-of-veterans-affairs-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Department of Veterans Affairs (VA) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: department-of-veterans-affairs-jsonschema-spectral-rules
- effective_rule_count: 0
  extends: []
  name: Department of Veterans Affairs (VA) API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: va-rules
scopes:
- name: Department Of Veterans Affairs Scopes
  scope_count: 3
  slug: department-of-veterans-affairs-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 36.0
  delta: -5.6
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 9.8
    contract_quality: 62.9
    developer_ergonomics: 28.6
    discoverability: 50.0
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 41.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 50.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/department-of-veterans-affairs/refs/heads/main/screenshots/department-of-veterans-affairs-2026-06-20T175926.png
security:
- kind: authentication
  name: Department Of Veterans Affairs Authentication
  slug: department-of-veterans-affairs-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Department Of Veterans Affairs Domain Security
  slug: department-of-veterans-affairs-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Department Of Veterans Affairs Vulnerability Disclosure
  slug: department-of-veterans-affairs-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: department-of-veterans-affairs
tags:
- Federal Government
- Healthcare
- Veterans
website: https://developer.va.gov/
---

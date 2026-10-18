---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.0
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Spliceforms Agentic Access
  operation_count: 39
  slug: spliceforms-agentic-access
  summary_line: 39 operations · 19 acting
api_count: 5
apis:
- baseURL: https://api.stitch.spliceforms.com/auth
  baseurl_source: declared
  description: Endpoints to inquire customer accounts information
  name: Spliceforms account data inquiry API
  slug: spliceforms-account-data-inquiry-api
- baseURL: https://api.stitch.spliceforms.com/auth
  baseurl_source: declared
  description: Endpoints for retrieving and managing bank branch information.
  name: Spliceforms Branches API
  slug: spliceforms-branches-api
- baseURL: https://api.stitch.spliceforms.com/auth
  baseurl_source: declared
  description: Endpoints to fetch calculator results
  name: Spliceforms Calculators API
  slug: spliceforms-calculators-api
- baseURL: https://api.stitch.spliceforms.com/auth
  baseurl_source: declared
  description: Endpoints to retrieve codesets information
  name: Spliceforms Codesets API
  slug: spliceforms-codesets-api
- baseURL: https://api.stitch.spliceforms.com/auth
  baseurl_source: declared
  description: Endpoints dealing with consent management and definitions.
  name: Spliceforms Consents API
  slug: spliceforms-consents-api
- baseURL: https://api.stitch.spliceforms.com/auth
  baseurl_source: declared
  description: Endpoints to verify customer information
  name: Spliceforms data validations API
  slug: spliceforms-data-validations-api
- baseURL: https://api.stitch.spliceforms.com/auth
  baseurl_source: declared
  description: API endpoints for filling the application form information and submit for processing
  name: Spliceforms Form Capture API
  slug: spliceforms-form-capture-api
- baseURL: https://api.stitch.spliceforms.com/auth
  baseurl_source: declared
  description: Endpoints related to geographical locations, including states and cities.
  name: Spliceforms Location API
  slug: spliceforms-location-api
- baseURL: https://api.stitch.spliceforms.com/auth
  baseurl_source: declared
  description: API endpoints for token issuance on successful OTP authentication
  name: Spliceforms OTP Auth API
  slug: spliceforms-otp-auth-api
- baseURL: https://api.stitch.spliceforms.com/auth
  baseurl_source: declared
  description: API endpoints for tracking the status of application processing
  name: Spliceforms Status Tracking API
  slug: spliceforms-status-tracking-api
- baseURL: https://api.stitch.spliceforms.com/auth
  baseurl_source: declared
  description: API endpoints to initiate the application processing
  name: Spliceforms Submission API
  slug: spliceforms-submission-api
artifact_total: 43
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/spliceforms/refs/heads/main/agentic-access/spliceforms-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/spliceforms-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/spliceforms/refs/heads/main/rules/spliceforms-stoplight-projects-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/spliceforms-stoplight-projects-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/spliceforms/refs/heads/main/rules/spliceforms-rules.yml
  title: ''
  type: Spectral
  url: rules/spliceforms-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/spliceforms/refs/heads/main/json-ld/spliceforms-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/spliceforms-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/spliceforms/refs/heads/main/vocabulary/spliceforms-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/spliceforms-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/spliceforms/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/spliceforms/refs/heads/main/data-model/spliceforms-data-model.yml
  title: ''
  type: DataModel
  url: data-model/spliceforms-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/spliceforms/refs/heads/main/conventions/spliceforms-conventions.yml
  title: ''
  type: Conventions
  url: conventions/spliceforms-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/spliceforms/refs/heads/main/errors/spliceforms-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/spliceforms-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/spliceforms/refs/heads/main/conformance/spliceforms-conformance.yml
  title: ''
  type: Conformance
  url: conformance/spliceforms-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/spliceforms/refs/heads/main/overlays/spliceforms-auth-services-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/spliceforms-auth-services-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/spliceforms/refs/heads/main/hosts/spliceforms-hosts.yml
  title: ''
  type: Hosts
  url: hosts/spliceforms-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/spliceforms/refs/heads/main/vendors/spliceforms-vendors.yml
  title: ''
  type: Vendors
  url: vendors/spliceforms-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/spliceforms/refs/heads/main/security/spliceforms-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/spliceforms-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spliceforms.com/
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/spliceforms/stoplight-projects/blob/efa3a9d27fea181247794c461dccb33010a2e51d/sf-style-guide/.spectral.json
- group: company
  title: ''
  type: ProductWebsite
  url: https://apibanking.com/
- group: company
  title: ''
  type: Blog
  url: https://apibanking.substack.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spliceforms
- group: operate
  title: ''
  type: Support
  url: https://apibanking.com/contact-us/
- group: company
  title: ''
  type: About
  url: https://apibanking.com/about-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apibanking/
created: '2026-10-09'
description: Spliceforms Enterprise Solutions (CIN U72200MH2022PTC395237) is a private limited company incorporated in India on 13 December 2022 that operates apibanking.com, an API and embedded-banking platform for financial institutions. It provides an API factory, a docs content platform and developer portal, and a partner management portal with SDKs, sandboxes and sample apps, to help banks, fintechs and corporates build partner integrations. It also publishes a Spectral API style guide on GitHub.
image: https://apibanking.com/wp-content/uploads/2023/02/logo.svg
json_schemas:
- name: ApplicationStatus92828
  property_count: 2
  slug: spliceforms-application-status92828
- name: BankAccountOwnershipCheckRequest
  property_count: 5
  slug: spliceforms-bank-account-ownership-check-request
- name: Branch
  property_count: 6
  slug: spliceforms-branch
- name: City
  property_count: 6
  slug: spliceforms-city
- name: ConsentDefinition
  property_count: 4
  slug: spliceforms-consent-definition
- name: ETBFDApplicationForm
  property_count: 3
  slug: spliceforms-etbfdapplication-form
- name: FDAccountWithOptionalPayout
  property_count: 7
  slug: spliceforms-fdaccount-with-optional-payout
- name: FDMaturityCalculationRequest
  property_count: 8
  slug: spliceforms-fdmaturity-calculation-request
- name: FDMaturity
  property_count: 4
  slug: spliceforms-fdmaturity
- name: Form92828
  property_count: 3
  slug: spliceforms-form92828
- name: NomineeInquiryRequest
  property_count: 1
  slug: spliceforms-nominee-inquiry-request
- name: Nominee
  property_count: 6
  slug: spliceforms-nominee
- name: OtherBankBranch
  property_count: 4
  slug: spliceforms-other-bank-branch
- name: OTPAuthResponse
  property_count: 2
  slug: spliceforms-otpauth-response
- name: OTPChallengeAnswer
  property_count: 2
  slug: spliceforms-otpchallenge-answer
- name: OTPChallengeRequest
  property_count: 2
  slug: spliceforms-otpchallenge-request
- name: OTPChallengeResponse
  property_count: 3
  slug: spliceforms-otpchallenge-response
- name: OTPResendRequest
  property_count: 1
  slug: spliceforms-otpresend-request
- name: PaginatedResponse
  property_count: 4
  slug: spliceforms-paginated-response
- name: PayinRequest
  property_count: 4
  slug: spliceforms-payin-request
- name: PayinSourcePreference
  property_count: 2
  slug: spliceforms-payin-source-preference
- name: Staff
  property_count: 3
  slug: spliceforms-staff
- name: State
  property_count: 4
  slug: spliceforms-state
- name: VPAOwnershipCheckRequest
  property_count: 2
  slug: spliceforms-vpaownership-check-request
jsonld:
- class_count: 92
  name: Spliceforms Context
  property_count: 130
  slug: spliceforms-context
layout: provider
modified: '2026-10-09'
name: Spliceforms
nav: Providers
network: true
overview: 'Spliceforms publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including account data inquiry API, Branches API, Calculators API, and 8 more. Tagged areas include Company, API Banking, Open Banking, Embedded Banking, and Fintech.


  The Spliceforms catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Spliceforms'' developer surface includes engineering blog, support, and 20 more developer resources.'
plans:
- name: Spliceforms Plans Pricing
  plan_count: 0
  slug: spliceforms-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Spliceforms Rate Limits
  slug: spliceforms-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Spliceforms API Rules
  rule_count: 17
  severity_counts:
    error: 14
    hint: 0
    info: 2
    warn: 1
  slug: spliceforms-rules
- authorship: provider
  effective_rule_count: 81
  extends: []
  name: Spliceforms — stoplight projects rules
  rule_count: 81
  severity_counts:
    error: 46
    hint: 0
    info: 0
    'off': 2
    warn: 33
  slug: spliceforms-stoplight-projects-spectral-rules
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 79.3
    catalog_earned_first_party: 18.0
    catalog_gap: 35.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.3
  facets:
    access_clarity: 0.0
    contract_governance: 62.9
    contract_quality: 64.7
    developer_ergonomics: 8.9
    discoverability: 71.4
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 26.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 8.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/spliceforms/refs/heads/main/screenshots/spliceforms-2026-10-11T130212.png
security:
- kind: authentication
  name: Spliceforms Authentication
  slug: spliceforms-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Spliceforms Domain Security
  slug: spliceforms-domain-security
  summary_line: TLSv1.3 · HSTS
slug: spliceforms
tags:
- Company
- API Banking
- Open Banking
- Embedded Banking
- Fintech
- Developer Portal
- Banking
- India
website: https://spliceforms.com/
---

---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 53
  human_in_the_loop: 0
  name: Va Gov Agentic Access
  operation_count: 116
  slug: va-gov-agentic-access
  summary_line: 116 operations · 53 acting
api_count: 22
apis:
- description: Composite of the three AMA decision-review filing endpoints — Higher-Level Review (HLR), Supplemental Claim (SC), and Notice of Disagreement (Board Appeal / NOD) — for submitting and tracking decision
  name: Decision Reviews API
  slug: decision-reviews-api
- description: School Certifying Officials (SCOs) and education benefit administrators read and submit GI Bill / Post-9/11 education benefit enrollment data — VA Form 22-1999 enrollment certifications — on behalf of
  name: Education Benefits API
  slug: education-benefits-api
- description: Provides lenders and servicers the digital surface for the VA Home Loan Guaranty program — eligibility, appraisals, loan setup, and certificate-of-eligibility (COE) operations. Companion APIs handle L
  name: Loan Guaranty API
  slug: loan-guaranty-api
- description: Lets VA Loan Guaranty servicers remit funding-fee, late, and other Loan Guaranty payments to VA electronically instead of through legacy paper-based remittance. Client credentials only; sandbox availa
  name: Guaranty Remittance API
  slug: guaranty-remittance-api
- description: Insurance-coordination API for VA's Consolidated Patient Account Center (CPAC) — submit and update third-party health insurance coverage on a Veteran's record so VA can correctly bill private insurers
  name: Health Care Costs Coverage API
  slug: health-care-costs-coverage-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: Allows authenticated and authorized users to file a 5103 Notice Response on a claim.
  name: VA Lighthouse 5103 Waiver API
  slug: va-gov-5103-waiver-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: The ACA Coverage API from VA Lighthouse — 1 operation(s) for aca coverage.
  name: VA Lighthouse ACA Coverage API
  slug: va-gov-aca-coverage-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: Address Standardization and Validation endpoints
  name: VA Lighthouse AddressValidation-v3 API
  slug: va-gov-addressvalidation-v3-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: The Appealable Issues API from VA Lighthouse — 1 operation(s) for appealable issues.
  name: VA Lighthouse Appealable Issues API
  slug: va-gov-appealable-issues-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: Caseflow appeals status API
  name: VA Lighthouse Appeals Status API
  slug: va-gov-appeals-status-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: Allows authenticated and authorized users to access claims data for a single claim by ID, or for all claims based on claimant data. No data is returned if the user is not authenticated and authorized.
  name: VA Lighthouse Claims API
  slug: va-gov-claims-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: The DirectDeposit API from VA Lighthouse — 1 operation(s) for directdeposit.
  name: VA Lighthouse DirectDeposit API
  slug: va-gov-directdeposit-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: Used for 526 claims.
  name: VA Lighthouse Disability API
  slug: va-gov-disability-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: Allows authenticated and authorized users to automatically establish a Disability Compensation Claim (21-526EZ) in VBMS
  name: VA Lighthouse Disability Compensation Claims API
  slug: va-gov-disability-compensation-claims-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: The Disability Rating API from VA Lighthouse — 4 operation(s) for disability rating.
  name: VA Lighthouse Disability Rating API
  slug: va-gov-disability-rating-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: The Documents Service API from VA Lighthouse — 9 operation(s) for documents service.
  name: VA Lighthouse Documents Service API
  slug: va-gov-documents-service-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: The Enrolled Benefits API from VA Lighthouse — 1 operation(s) for enrolled benefits.
  name: VA Lighthouse Enrolled Benefits API
  slug: va-gov-enrolled-benefits-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: VA Facilities API
  name: VA Lighthouse facilities API
  slug: va-gov-facilities-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: The Flashes API from VA Lighthouse — 1 operation(s) for flashes.
  name: VA Lighthouse Flashes API
  slug: va-gov-flashes-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: The Forms API from VA Lighthouse — 2 operation(s) for forms.
  name: VA Lighthouse Forms API
  slug: va-gov-forms-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: Used for 0966 submissions.
  name: VA Lighthouse Intent to File API
  slug: va-gov-intent-to-file-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: The JWS Validation API from VA Lighthouse — 1 operation(s) for jws validation.
  name: VA Lighthouse JWS Validation API
  slug: va-gov-jws-validation-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: The Legacy Appeals API from VA Lighthouse — 1 operation(s) for legacy appeals.
  name: VA Lighthouse Legacy Appeals API
  slug: va-gov-legacy-appeals-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: The Letters API from VA Lighthouse — 3 operation(s) for letters.
  name: VA Lighthouse Letters API
  slug: va-gov-letters-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: Loan Review Public Resource
  name: VA Lighthouse loanReviewPublic API
  slug: va-gov-loanreviewpublic-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: The Path API from VA Lighthouse — 1 operation(s) for path.
  name: VA Lighthouse Path API
  slug: va-gov-path-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: The Permanent And Total Disability API from VA Lighthouse — 2 operation(s) for permanent and total disability.
  name: VA Lighthouse Permanent And Total Disability API
  slug: va-gov-permanent-and-total-disability-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: Used for 21-22 and 21-22a form submissions.
  name: VA Lighthouse Power of Attorney API
  slug: va-gov-power-of-attorney-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: The Reference Data API from VA Lighthouse — 9 operation(s) for reference data.
  name: VA Lighthouse Reference Data API
  slug: va-gov-reference-data-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: The Search API from VA Lighthouse — 1 operation(s) for search.
  name: VA Lighthouse Search API
  slug: va-gov-search-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: The Service History API from VA Lighthouse — 1 operation(s) for service history.
  name: VA Lighthouse Service History API
  slug: va-gov-service-history-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: The Status API from VA Lighthouse — 2 operation(s) for status.
  name: VA Lighthouse Status API
  slug: va-gov-status-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: The Uploads API from VA Lighthouse — 5 operation(s) for uploads.
  name: VA Lighthouse Uploads API
  slug: va-gov-uploads-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: Veteran Confirmation - Veteran Status
  name: VA Lighthouse veteran_confirmation_status API
  slug: va-gov-veteran-confirmation-status-api
- baseURL: https://api.va.gov/services/va_facilities/v1
  baseurl_source: declared
  description: The Veteran Verification API from VA Lighthouse — 3 operation(s) for veteran verification.
  name: VA Lighthouse Veteran Verification API
  slug: va-gov-veteran-verification-api
artifact_total: 115
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Address Validation 5103 Waiver API
  slug: open-va-gov-5103-waiver-api
- collection_type: open
  name: Address Validation 5103 Waiver ACA Coverage API
  slug: open-va-gov-aca-coverage-api
- collection_type: open
  name: Address Validation
  slug: open-va-gov-address-validation-v3
- collection_type: open
  name: Address Validation 5103 Waiver AddressValidation-v3 API
  slug: open-va-gov-addressvalidation-v3-api
- collection_type: open
  name: Address Validation 5103 Waiver Appealable Issues API
  slug: open-va-gov-appealable-issues-api
- collection_type: open
  name: Appealable Issues
  slug: open-va-gov-appealable-issues-v0
- collection_type: open
  name: Address Validation 5103 Waiver Appeals Status API
  slug: open-va-gov-appeals-status-api
- collection_type: open
  name: Appeals
  slug: open-va-gov-appeals-status-v0
- collection_type: open
  name: Appeals Status
  slug: open-va-gov-appeals-status-v1
- collection_type: open
  name: Benefits Claims
  slug: open-va-gov-benefits-claims-v1
- collection_type: open
  name: Benefits Claims
  slug: open-va-gov-benefits-claims-v2
- collection_type: open
  name: Benefits Documents Service API
  slug: open-va-gov-benefits-documents-v1
- collection_type: open
  name: Benefits Intake
  slug: open-va-gov-benefits-intake-v1
- collection_type: open
  name: Benefits Data Lookup API
  slug: open-va-gov-benefits-reference-data-v1
- collection_type: open
  name: Address Validation 5103 Waiver Claims API
  slug: open-va-gov-claims-api
- collection_type: open
  name: Community Care Eligibility
  slug: open-va-gov-community-care-eligibility-v0
- collection_type: open
  name: Direct Deposit Management API
  slug: open-va-gov-direct-deposit-management-v1
- collection_type: open
  name: Address Validation 5103 Waiver DirectDeposit API
  slug: open-va-gov-directdeposit-api
- collection_type: open
  name: Address Validation 5103 Waiver Disability API
  slug: open-va-gov-disability-api
- collection_type: open
  name: Address Validation 5103 Waiver Disability Compensation Claims API
  slug: open-va-gov-disability-compensation-claims-api
- collection_type: open
  name: Address Validation 5103 Waiver Disability Rating API
  slug: open-va-gov-disability-rating-api
- collection_type: open
  name: Address Validation 5103 Waiver Documents Service API
  slug: open-va-gov-documents-service-api
- collection_type: open
  name: Address Validation 5103 Waiver Enrolled Benefits API
  slug: open-va-gov-enrolled-benefits-api
- collection_type: open
  name: Address Validation 5103 Waiver facilities API
  slug: open-va-gov-facilities-api
- collection_type: open
  name: VA Facilities
  slug: open-va-gov-facilities-v0
- collection_type: open
  name: VA Facilities
  slug: open-va-gov-facilities-v1
- collection_type: open
  name: Address Validation 5103 Waiver Flashes API
  slug: open-va-gov-flashes-api
- collection_type: open
  name: Address Validation 5103 Waiver Forms API
  slug: open-va-gov-forms-api
- collection_type: open
  name: VA Forms
  slug: open-va-gov-forms-v0
- collection_type: open
  name: Address Validation 5103 Waiver Intent to File API
  slug: open-va-gov-intent-to-file-api
- collection_type: open
  name: Address Validation 5103 Waiver JWS Validation API
  slug: open-va-gov-jws-validation-api
- collection_type: open
  name: Address Validation 5103 Waiver Legacy Appeals API
  slug: open-va-gov-legacy-appeals-api
- collection_type: open
  name: Legacy Appeals
  slug: open-va-gov-legacy-appeals-v0
- collection_type: open
  name: Address Validation 5103 Waiver Letters API
  slug: open-va-gov-letters-api
- collection_type: open
  name: VA Loan Guaranty - Loan Review REST API
  slug: open-va-gov-loan-review-v1
- collection_type: open
  name: Address Validation 5103 Waiver Path API
  slug: open-va-gov-path-api
- collection_type: open
  name: API Collection
  slug: open-va-gov-patient-health-fhir-r4-capability
- collection_type: open
  name: Address Validation 5103 Waiver Permanent And Total Disability API
  slug: open-va-gov-permanent-and-total-disability-api
- collection_type: open
  name: Address Validation 5103 Waiver Power of Attorney API
  slug: open-va-gov-power-of-attorney-api
- collection_type: open
  name: Address Validation 5103 Waiver Reference Data API
  slug: open-va-gov-reference-data-api
- collection_type: open
  name: Address Validation 5103 Waiver Search API
  slug: open-va-gov-search-api
- collection_type: open
  name: Address Validation 5103 Waiver Service History API
  slug: open-va-gov-service-history-api
- collection_type: open
  name: Address Validation 5103 Waiver Status API
  slug: open-va-gov-status-api
- collection_type: open
  name: Address Validation 5103 Waiver Uploads API
  slug: open-va-gov-uploads-api
- collection_type: open
  name: VA Letter Generator API
  slug: open-va-gov-va-letter-generator-v1
- collection_type: open
  name: Address Validation 5103 Waiver veteran_confirmation_status API
  slug: open-va-gov-veteran-confirmation-status-api
- collection_type: open
  name: Veteran Confirmation
  slug: open-va-gov-veteran-confirmation-v0
- collection_type: open
  name: Veteran Confirmation
  slug: open-va-gov-veteran-confirmation-v1
- collection_type: open
  name: Address Validation 5103 Waiver Veteran Verification API
  slug: open-va-gov-veteran-verification-api
- collection_type: open
  name: Veteran Verification
  slug: open-va-gov-veteran-verification-v0
- collection_type: open
  name: Veteran Verification
  slug: open-va-gov-veteran-verification-v1
- collection_type: open
  name: Veteran Service History and Eligibility API
  slug: open-va-gov-veteran-verification-v2
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/va-gov-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/va-gov-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/va-gov-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/va-gov-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/va-gov-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/va-gov-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.va.gov
- group: start
  title: ''
  type: Portal
  url: https://api.va.gov
- group: docs
  title: ''
  type: Documentation
  url: https://developer.va.gov/explore
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.va.gov/onboarding
- group: start
  title: ''
  type: Signup
  url: https://developer.va.gov/onboarding/request-sandbox-access
- group: auth
  title: ''
  type: Authentication
  url: https://developer.va.gov/explore/api/authorization-code
- group: auth
  title: ''
  type: Authentication
  url: https://developer.va.gov/explore/api/client-credentials
- group: docs
  title: ''
  type: Documentation
  url: https://developer.va.gov/onboarding/request-production-access
- group: docs
  title: ''
  type: Documentation
  url: https://developer.va.gov/api-publishing
- group: operate
  title: ''
  type: Support
  url: https://developer.va.gov/support
- group: operate
  title: ''
  type: ContactEmail
  url: mailto:api@va.gov
- group: operate
  title: ''
  type: StatusPage
  url: https://valighthouse.statuspage.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.va.gov/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.va.gov/privacy-policy/
- group: docs
  title: ''
  type: Documentation
  url: https://www.va.gov/accessibility/
- group: company
  title: ''
  type: Blog
  url: https://news.va.gov/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/department-of-veterans-affairs
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/department-of-veterans-affairs/vets-api
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/department-of-veterans-affairs/vets-website
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/department-of-veterans-affairs/vets-api-clients
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/department-of-veterans-affairs/lighthouse-fhir-apis-consumer-docs
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/department-of-veterans-affairs/health-apis-bulk-fhir
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/department-of-veterans-affairs/health-apis-clinical-fhir
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/department-of-veterans-affairs/lighthouse-oas-tests
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/department-of-veterans-affairs/VHA-Facilities
- group: docs
  title: ''
  type: Documentation
  url: https://developer.va.gov/api-publishing/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developer.va.gov/onboarding/working-with-lighthouse-apis
- group: start
  title: ''
  type: Sandbox
  url: https://sandbox-api.va.gov
- group: auth
  title: ''
  type: Authentication
  url: https://api.va.gov/oauth2/authorization
- group: auth
  title: ''
  type: Authentication
  url: https://api.va.gov/oauth2/token
- group: auth
  title: ''
  type: Authentication
  url: https://api.va.gov/oauth2/revoke
- group: docs
  title: ''
  type: Documentation
  url: http://docs.smarthealthit.org/
- group: docs
  title: ''
  type: Documentation
  url: https://hl7.org/fhir/us/core/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/us-veteransaffairs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.va.gov/policy-and-compliance/notice-of-privacy-practices/
created: '2026-05-25T00:00:00.000Z'
description: VA Lighthouse is the US Department of Veterans Affairs' developer API platform. Published at developer.va.gov with production endpoints at api.va.gov, Lighthouse exposes 22+ APIs covering Benefits (claims, documents, reference data, intake), Health (HL7 FHIR R4 Patient Health and Clinical Health, Community Care Eligibility), Facilities, Forms, Veteran Verification and Confirmation, Appeals and Decision Reviews under the Appeals Modernization Act (AMA), Address Validation, Direct Deposit Management, VA Letter Generation, Education Benefits, and the full VA Home Loan Guaranty stack (Loan Guaranty, Loan Review, Guaranty Remittance, Health-Care-Costs Coverage). All authenticated APIs use OAuth 2.0 with both Authorization Code (Veteran consent) and Client Credentials (system) flows; the health APIs additionally support SMART-on-FHIR. The platform is operated by the VA Office of the CTO with open-source backend code in github.com/department-of-veterans-affairs/vets-api and reference
  clients in vets-api-clients.
features:
- 22+ Lighthouse APIs spanning Benefits, Health, Facilities, Verification, Forms, Appeals, and Loan Guaranty
- HL7 FHIR R4 + US Core conformant Patient Health and Clinical Health APIs with SMART-on-FHIR launch
- OAuth 2.0 with both Authorization Code (Veteran consent) and Client Credentials (system) flows
- Full sandbox at sandbox-api.va.gov with documented synthetic Veteran test accounts (vets-api-clients/test_accounts)
- Open-data facilities, forms, and reference-data APIs (no auth required for read endpoints)
- VA address canonicalization and geocoding via Address Validation API v3
- Direct integration with VBMS (Benefits Documents) and Centralized Mail Portal (Benefits Intake) for claims documentation
- AMA-era decision review filing — HLR, SC, Notice of Disagreement — plus legacy appeal status
- Programmatic VA letter generation (Benefit Summary, Service Verification, COE, etc.) as on-demand PDFs
- VA Home Loan Guaranty digital surface — Loan Guaranty, Loan Review, Guaranty Remittance, Health-Care-Costs Coverage
- Veteran Confirmation and Veteran Verification APIs for retail/lender Veteran-status checks
- GI Bill / Post-9/11 education benefit submission for School Certifying Officials
- Path-to-Production process documented in developer-portal-backend / Path-to-Production.md
- Lighthouse OAS contract testing via the public lighthouse-oas-tests repository
- Public reference implementations and sample apps in vets-api-clients (Ruby, Node, samples)
- vets-api (Ruby/Rails) — primary open-source backend powering VA.gov and many Lighthouse endpoints
- vets-website — public open-source frontend for VA.gov
- FHIR Bulk Data (Flat FHIR) endpoints via health-apis-bulk-fhir
- StatusPage at valighthouse.statuspage.io
- VA Lighthouse OAuth flow supports PKCE and SMART-on-FHIR scopes (patient/*, user/*, system/*)
- Free at point of use for accredited consumers — no per-call pricing for approved third parties
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/va-gov.png
jsonld:
- class_count: 2
  name: Va Gov Context
  property_count: 15
  slug: va-gov-context
layout: provider
modified: '2026-05-25'
name: VA Lighthouse
nav: Providers
network: true
overview: 'VA Lighthouse publishes 30 APIs on the [APIs.io](https://apis.io/) network, including 5103 Waiver API, ACA Coverage API, AddressValidation-v3 API, and 27 more. Tagged areas include Government, Veterans Affairs, Veterans, Healthcare, and Benefits.


  The VA Lighthouse catalog on APIs.io includes 1 JSON-LD context.


  VA Lighthouse''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, support, engineering blog, and 34 more developer resources.'
random_paper: 4
scopes:
- name: Va Gov Scopes
  scope_count: 35
  slug: va-gov-scopes
  summary_line: 35 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 41.6
  coverage:
    artifact_dirs: 10
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 64.9
    developer_ergonomics: 31.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 41.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 30
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 68.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/va-gov/refs/heads/main/screenshots/va-gov-2026-06-20T200737.png
security:
- kind: authentication
  name: Va Gov Authentication
  slug: va-gov-authentication
  summary_line: apiKey/http/oauth2 · 6 schemes
- kind: domain-security
  name: Va Gov Domain Security
  slug: va-gov-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Va Gov Vulnerability Disclosure
  slug: va-gov-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: va-gov
tags:
- Government
- Veterans Affairs
- Veterans
- Healthcare
- Benefits
- FHIR
- Open Data
- Federal
website: https://developer.va.gov
---

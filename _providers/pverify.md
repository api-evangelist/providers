---
access_model:
  confidence: high
  label: Tiered subscription · Sales-led onboarding · API is an Enterprise-tier entitlement
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - pricing-page
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Pverify Agentic Access
  operation_count: 10
  slug: pverify-agentic-access
  summary_line: 10 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api.pverify.com
  baseurl_source: declared
  description: OAuth2 client-credentials token endpoint. POST /Token exchanges Client_Id + Client_Secret for a bearer access_token used on every other pVerify call, alongside the case-sensitive Client-API-Id header.
  name: pVerify Authentication API
  slug: pverify-authentication-api
- baseURL: https://api.pverify.com
  baseurl_source: declared
  description: Real-time X12 270/271 insurance eligibility verification. Submit an EligibilitySummary inquiry, poll the pending queue, retrieve the parsed benefit summary or the raw 271, pull a PDF report, and cance
  name: pVerify Eligibility API
  slug: pverify-eligibility-api
- baseURL: https://api.pverify.com
  baseurl_source: declared
  description: Dental insurance eligibility and benefit verification, including the only version-prefixed path in the pVerify surface (/api/v2/DentalEligibilitySummary) alongside the unversioned v1 endpoints.
  name: pVerify Dental Eligibility API
  slug: pverify-dental-eligibility-api
- baseURL: https://api.pverify.com
  baseurl_source: declared
  description: Find unknown or unreported active insurance coverage for a patient presenting as self-pay, returning candidate payers and member IDs plus a hosted details URL and PDF report.
  name: pVerify Insurance Discovery API
  slug: pverify-insurance-discovery-api
- baseURL: https://api.pverify.com
  baseurl_source: declared
  description: Look up a Medicare Beneficiary Identifier for a patient from demographic data, for providers who need the MBI before they can run Medicare eligibility.
  name: pVerify MBI Lookup API
  slug: pverify-mbi-lookup-api
- baseURL: https://api.pverify.com
  baseurl_source: declared
  description: Validate and complete patient demographic data (pDV) — name, date of birth, gender and address — so that downstream eligibility and discovery inquiries match on identity.
  name: pVerify Patient Demographic Validator API
  slug: pverify-patient-demographic-validator-api
- baseURL: https://api.pverify.com
  baseurl_source: declared
  description: X12 276/277 claim status inquiry. Ask a payer what happened to a submitted claim and retrieve the 277 response by RequestID. Not every payer supports 276/277 electronically.
  name: pVerify Claim Status API
  slug: pverify-claim-status-api
- baseURL: https://api.pverify.com
  baseurl_source: declared
  description: Estimate patient financial responsibility for a planned service from the payer benefit data, for point-of-service collection.
  name: pVerify Patient Cost Estimator API
  slug: pverify-estimation-api
- baseURL: https://api.pverify.com
  baseurl_source: declared
  description: 'The payer network surface: the full supported-payer catalog, live per-payer up/down status (the only pVerify operation requiring no authentication), and recent per-payer rejection statistics.'
  name: pVerify Payers API
  slug: pverify-payers-api
- baseURL: https://api.pverify.com
  baseurl_source: declared
  description: Provision and drive the embeddable eligibility-and-estimates widget. Setup runs against the premium portal host; CGXInquiry returns a combined estimate plus eligibility result for the widget to render
  name: pVerify CGX Widget API
  slug: pverify-cgx-widget-api
- baseURL: https://api.pverify.com
  baseurl_source: declared
  description: Medicare same-or-similar DME history check. pVerify labels this product "(Discontinued)" in its own documentation while continuing to document it in full; every operation is marked deprecated in the s
  name: pVerify Same or Similar API (discontinued)
  slug: pverify-same-or-similar-api
- baseURL: https://api.pverify.com
  baseurl_source: declared
  description: Certificate of Medical Necessity lookup. Labelled "(Discontinued)" by pVerify; every operation is marked deprecated in the spec.
  name: pVerify CMN API (discontinued)
  slug: pverify-cmn-api
- baseURL: https://api.pverify.com
  baseurl_source: declared
  description: Skilled Nursing Facility stay verification. Labelled "(Discontinued)" by pVerify; every operation is marked deprecated in the spec.
  name: pVerify SNF API (discontinued)
  slug: pverify-snf-api
artifact_total: 29
asyncapis:
- description: ''
  name: Pverify Callbacks
  slug: pverify-callbacks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: pVerify Authentication API
  slug: open-pverify-authentication-api
- collection_type: open
  name: pVerify Authentication Batch API
  slug: open-pverify-batch-api
- collection_type: open
  name: pVerify Authentication Claim Status API
  slug: open-pverify-claim-status-api
- collection_type: open
  name: pVerify Authentication Eligibility API
  slug: open-pverify-eligibility-api
- collection_type: open
  name: pVerify Authentication Estimation API
  slug: open-pverify-estimation-api
- collection_type: open
  name: pVerify Authentication Payers API
  slug: open-pverify-payers-api
- collection_type: open
  name: pVerify API
  slug: open-pverify
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/pverify-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.pverify.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://pverify.com/api-developers/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pverify.io/
- group: docs
  title: ''
  type: APIReference
  url: https://postman.pverify.com/
- group: build
  title: ''
  type: Postman
  url: https://postman.pverify.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://pverify.com/templates/
- group: operate
  title: ''
  type: Support
  url: https://pverify.com/contact-support/
- group: company
  title: ''
  type: Blog
  url: https://pverify.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pVerify
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pverify
- group: start
  title: ''
  type: Login
  url: https://apimgmt.pverify.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://pverify.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pverify.com/pverify-legal-documentation/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pverify.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dosespot.com/posts/dashboard
- group: auth
  title: ''
  type: TrustCenter
  url: security/pverify-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.dosespot.com/
- group: operate
  title: ''
  type: SLA
  url: https://pverify.com/wp-content/uploads/2025/04/Exhibit-B-SLA.docx
- group: auth
  title: ''
  type: Authentication
  url: authentication/pverify-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pverify-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pverify-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pverify-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pverify-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pverify-data-model.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/pverify-vocabulary.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/pverify-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/pverify-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/pverify-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pverify-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pverify-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pverify-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pverify-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pverify-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pverify-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pverify-finops.yml
- group: build
  title: ''
  type: PostmanCollection
  url: collections/pverify-published-postman-collection.json
created: '2026-06-21'
description: pVerify is a US healthcare insurance eligibility and revenue-cycle API company, part of DoseSpot (now Interra Health). Its REST API at https://api.pverify.com exchanges X12 270/271 eligibility transactions and returns parsed, practice-type-specific benefit summaries; runs 276/277 claim status inquiries; discovers unknown active coverage for self-pay patients; looks up Medicare Beneficiary Identifiers; validates patient demographics; publishes a supported-payer catalog with live per-payer up/down status; and estimates patient financial responsibility at the point of service. Authentication is an OAuth2 client-credentials bearer token plus a case-sensitive Client-API-Id header. pVerify publishes no OpenAPI — its machine-readable contract is a public Postman Collection v2.0.0 at https://postman.pverify.com/, from which the OpenAPI documents in this repository were derived operation-for-operation.
finops:
- name: Pverify Finops
  service_category: Healthcare and Insurance
  slug: pverify-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pverify.png
layout: provider
modified: '2026-08-15'
name: pVerify
nav: Providers
network: true
overview: 'pVerify publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Eligibility API, Dental Eligibility API, and 10 more. Tagged areas include Healthcare, Insurance, Eligibility, Claims, and EDI.


  The pVerify catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  pVerify''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 31 more developer resources.'
plans:
- name: Pverify Plans Pricing
  plan_count: 8
  slug: pverify-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 4
  name: Pverify Rate Limits
  slug: pverify-rate-limits
score:
  band: strong
  composite: 55.0
  coverage:
    artifact_dirs: 26
    catalog_gap: 46.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 33.3
    contract_quality: 61.8
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 33.3
    operational_transparency: 34.2
  previous_composite: 55.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 27.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pverify/refs/heads/main/screenshots/pverify-2026-08-17T080414.png
security:
- kind: authentication
  name: Pverify Authentication
  slug: pverify-authentication
  summary_line: http/apiKey · 3 schemes
- kind: domain-security
  name: Pverify Domain Security
  slug: pverify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Pverify Trust Center
  slug: pverify-trust-center
  summary_line: SOC 2 Type II, HIPAA
slug: pverify
tags:
- Healthcare
- Insurance
- Eligibility
- Claims
- EDI
- 270/271
- 276/277
- Revenue Cycle
- Medicare
- Payers
- Insurance Discovery
- Patient Estimation
- HIPAA
- Dental
website: https://www.pverify.com
---

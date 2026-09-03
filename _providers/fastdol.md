---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 17
  human_in_the_loop: 2
  name: Fastdol Agentic Access
  operation_count: 48
  slug: fastdol-agentic-access
  summary_line: 48 operations · 17 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.fastdol.com
  baseurl_source: declared
  description: The Auth API from FastDOL — 7 operation(s) for auth.
  name: FastDOL Auth API
  slug: fastdol-auth-api
- baseURL: https://api.fastdol.com
  baseurl_source: declared
  description: The Dashboard API from FastDOL — 5 operation(s) for dashboard.
  name: FastDOL Dashboard API
  slug: fastdol-dashboard-api
- baseURL: https://api.fastdol.com
  baseurl_source: declared
  description: The Employers API from FastDOL — 14 operation(s) for employers.
  name: FastDOL Employers API
  slug: fastdol-employers-api
- baseURL: https://api.fastdol.com
  baseurl_source: declared
  description: The Export API from FastDOL — 3 operation(s) for export.
  name: FastDOL Export API
  slug: fastdol-export-api
- baseURL: https://api.fastdol.com
  baseurl_source: declared
  description: The Health API from FastDOL — 2 operation(s) for health.
  name: FastDOL Health API
  slug: fastdol-health-api
- baseURL: https://api.fastdol.com
  baseurl_source: declared
  description: The Industries API from FastDOL — 2 operation(s) for industries.
  name: FastDOL Industries API
  slug: fastdol-industries-api
- baseURL: https://api.fastdol.com
  baseurl_source: declared
  description: The Inspections API from FastDOL — 1 operation(s) for inspections.
  name: FastDOL Inspections API
  slug: fastdol-inspections-api
- baseURL: https://api.fastdol.com
  baseurl_source: declared
  description: The Sitemap API from FastDOL — 1 operation(s) for sitemap.
  name: FastDOL Sitemap API
  slug: fastdol-sitemap-api
- baseURL: https://api.fastdol.com
  baseurl_source: declared
  description: The Stats API from FastDOL — 7 operation(s) for stats.
  name: FastDOL Stats API
  slug: fastdol-stats-api
- baseURL: https://api.fastdol.com
  baseurl_source: declared
  description: The Usage API from FastDOL — 3 operation(s) for usage.
  name: FastDOL Usage API
  slug: fastdol-usage-api
- baseURL: https://api.fastdol.com
  baseurl_source: declared
  description: The Webhooks API from FastDOL — 1 operation(s) for webhooks.
  name: FastDOL Webhooks API
  slug: fastdol-webhooks-api
artifact_total: 137
collections:
- collection_type: postman
  name: FastDOL Auth API
  slug: postman-fastdol-auth-api
- collection_type: postman
  name: FastDOL Auth Dashboard API
  slug: postman-fastdol-dashboard-api
- collection_type: postman
  name: FastDOL Auth Employers API
  slug: postman-fastdol-employers-api
- collection_type: postman
  name: FastDOL Auth Export API
  slug: postman-fastdol-export-api
- collection_type: postman
  name: FastDOL Auth Health API
  slug: postman-fastdol-health-api
- collection_type: postman
  name: FastDOL Auth Industries API
  slug: postman-fastdol-industries-api
- collection_type: postman
  name: FastDOL Auth Inspections API
  slug: postman-fastdol-inspections-api
- collection_type: postman
  name: FastDOL Auth Sitemap API
  slug: postman-fastdol-sitemap-api
- collection_type: postman
  name: FastDOL Auth Stats API
  slug: postman-fastdol-stats-api
- collection_type: postman
  name: FastDOL Auth Usage API
  slug: postman-fastdol-usage-api
- collection_type: postman
  name: FastDOL Auth Webhooks API
  slug: postman-fastdol-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FastDOL Auth API
  slug: open-fastdol-auth-api
- collection_type: open
  name: FastDOL Auth Dashboard API
  slug: open-fastdol-dashboard-api
- collection_type: open
  name: FastDOL Auth Employers API
  slug: open-fastdol-employers-api
- collection_type: open
  name: FastDOL Auth Export API
  slug: open-fastdol-export-api
- collection_type: open
  name: FastDOL Auth Health API
  slug: open-fastdol-health-api
- collection_type: open
  name: FastDOL Auth Industries API
  slug: open-fastdol-industries-api
- collection_type: open
  name: FastDOL Auth Inspections API
  slug: open-fastdol-inspections-api
- collection_type: open
  name: FastDOL Auth Sitemap API
  slug: open-fastdol-sitemap-api
- collection_type: open
  name: FastDOL Auth Stats API
  slug: open-fastdol-stats-api
- collection_type: open
  name: FastDOL Auth Usage API
  slug: open-fastdol-usage-api
- collection_type: open
  name: FastDOL Auth Webhooks API
  slug: open-fastdol-webhooks-api
- collection_type: open
  name: FastDOL API
  slug: open-fastdol
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/fastdol/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fastdol-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fastdol-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fastdol.com/
- group: docs
  title: ''
  type: Documentation
  url: https://fastdol.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://fastdol.com/docs
- group: start
  title: ''
  type: Sandbox
  url: https://fastdol.com/playground
- group: start
  title: ''
  type: Signup
  url: https://fastdol.com/signup
- group: start
  title: ''
  type: Login
  url: https://fastdol.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://fastdol.com/enterprise
- group: commercial
  title: ''
  type: Plans
  url: plans/fastdol-plans-pricing.yml
- group: commercial
  title: ''
  type: PricingPage
  url: https://fastdol.com/enterprise
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fastdol-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fastdol-finops.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/fastdol-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/fastdol-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://fastdol.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fastdol.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fastdol.com/privacy
- group: operate
  title: ''
  type: Contact
  url: https://fastdol.com/enterprise
- group: operate
  title: ''
  type: Support
  url: mailto:ben@fastdol.com
- group: auth
  title: ''
  type: Authentication
  url: https://fastdol.com/docs
- group: other
  title: ''
  type: Methodology
  url: https://fastdol.com/methodology
- group: other
  title: ''
  type: Datasets
  url: https://fastdol.com/datasets
- group: other
  title: ''
  type: HuggingFace
  url: https://huggingface.co/FastDOLz
- group: other
  title: ''
  type: APIsJSON
  url: https://api.fastdol.com/v1/openapi.json
created: '2026-05-16'
description: Federal workplace enforcement records on 2.3M US employers across 16 federal agencies — OSHA, WHD, MSHA, EPA ECHO, NLRB, FMCSA, OFLC, BLS SOII, SAM.gov, CMS, USAspending, CPSC, NHTSA, SEC, and the UVA Corporate Prosecution Registry — exposed as a single normalized JSON API. Query inspections, violations, penalties, wage theft cases, severe injury reports, federal contract awards, and recalls.
examples:
- key_count: 6
  name: Fastdol Batch Lookup Item Example
  slug: fastdol-batch-lookup-item-example
- key_count: 1
  name: Fastdol Batch Lookup Request Example
  slug: fastdol-batch-lookup-request-example
- key_count: 1
  name: Fastdol Batch Lookup V1 Employers Batch Post Request Example
  slug: fastdol-batch-lookup-v1-employers-batch-post-request-example
- key_count: 1
  name: Fastdol Body Upload Csv V1 Employers Upload Csv Post Example
  slug: fastdol-body-upload-csv-v1-employers-upload-csv-post-example
- key_count: 5
  name: Fastdol Create Export V1 Export Post Request Example
  slug: fastdol-create-export-v1-export-post-request-example
- key_count: 2
  name: Fastdol Create Key Dashboard Keys Post Request Example
  slug: fastdol-create-key-dashboard-keys-post-request-example
- key_count: 2
  name: Fastdol Create Key Request Example
  slug: fastdol-create-key-request-example
- key_count: 2
  name: Fastdol Delete Account Dashboard Account Delete Request Example
  slug: fastdol-delete-account-dashboard-account-delete-request-example
- key_count: 2
  name: Fastdol Delete Account Request Example
  slug: fastdol-delete-account-request-example
- key_count: 17
  name: Fastdol Export Filters Example
  slug: fastdol-export-filters-example
- key_count: 5
  name: Fastdol Export Request Example
  slug: fastdol-export-request-example
- key_count: 3
  name: Fastdol Feedback Request Example
  slug: fastdol-feedback-request-example
- key_count: 1
  name: Fastdol Forgot Password Auth Forgot Password Post Request Example
  slug: fastdol-forgot-password-auth-forgot-password-post-request-example
- key_count: 1
  name: Fastdol Forgot Password Request Example
  slug: fastdol-forgot-password-request-example
- key_count: 2
  name: Fastdol Login Auth Login Post Request Example
  slug: fastdol-login-auth-login-post-request-example
- key_count: 2
  name: Fastdol Login Request Example
  slug: fastdol-login-request-example
- key_count: 2
  name: Fastdol Reset Password Auth Reset Password Post Request Example
  slug: fastdol-reset-password-auth-reset-password-post-request-example
- key_count: 2
  name: Fastdol Reset Password Request Example
  slug: fastdol-reset-password-request-example
- key_count: 3
  name: Fastdol Signup Auth Signup Post Request Example
  slug: fastdol-signup-auth-signup-post-request-example
- key_count: 3
  name: Fastdol Signup Request Example
  slug: fastdol-signup-request-example
- key_count: 3
  name: Fastdol Submit Feedback V1 Employers Employer Id Feedback Post Request Example
  slug: fastdol-submit-feedback-v1-employers-employer-id-feedback-post-request-example
- key_count: 1
  name: Fastdol Verify Email Auth Verify Post Request Example
  slug: fastdol-verify-email-auth-verify-post-request-example
- key_count: 1
  name: Fastdol Verify Email Request Example
  slug: fastdol-verify-email-request-example
features:
- description: Fuzzy search across 2.3M US employers by name, EIN, ZIP, state, or NAICS code with risk-ranked results.
  name: Unified Employer Search
- description: Single employer profile aggregating OSHA inspections and violations, WHD wage theft, MSHA mine safety, EPA ECHO, NLRB labor practice, FMCSA, OFLC, BLS SOII, SAM.gov debarment, CMS, USAspending, CPSC, NHTSA, SEC enforcement, and federal prosecutions.
  name: Cross-Agency Enforcement Profile
- description: Composite per-employer risk score with risk-history endpoint exposing month-over-month changes.
  name: Risk Scoring
- description: Aggregate enforcement across all locations of a parent company via parent-name lookup.
  name: Parent Company Rollup
- description: Compare an employer against industry peers within the same NAICS code and state.
  name: Peer Comparison
- description: Submit up to 100 employer queries in one POST for high-throughput backfills.
  name: Batch Lookup
- description: Upload up to 500 rows / 5MB for bulk match against the employer index.
  name: CSV Upload
- description: Enterprise-only export job pipeline returning downloadable CSV/JSON of up to 100,000 rows.
  name: Async Bulk Export
- description: Drill into individual OSHA inspection activity numbers for citation-level violations.
  name: Inspection Violations Detail
- description: OSHA Form 300A and severe-injury report data per employer.
  name: Severe Injuries Reporting
- description: SEC enforcement actions joined to publicly traded parent companies.
  name: SEC Enforcement Linkage
- description: Lookup NAICS-4 industry codes and BLS SOII industry injury rate benchmarks.
  name: NAICS Industry Metadata
- description: Pre-aggregated stats by US state and NAICS code, plus a dedicated nursing-home (CMS CCN) statistics index.
  name: State and Industry Statistics
- description: Dashboard endpoints to create, list, rotate (48-hour grace), and revoke API keys (up to 5 active per account).
  name: API Key Self-Service
- description: Self-reported lookup logging and PDF report claim endpoints with retrievable usage history.
  name: Usage Telemetry
- description: Crawler-friendly employer sitemap endpoint for SEO and search-index ingestion.
  name: Sitemap Feed
- description: Per-employer feedback submission for data corrections.
  name: Feedback Submission
finops:
- name: Fastdol Finops
  service_category: Public Records / Compliance Data
  slug: fastdol-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fastdol.png
integrations:
- description: Inspections, violations, penalties, fatalities, and severity classifications.
  name: OSHA Enforcement Data
- description: Self-reported DART and TRIR injury rates by establishment.
  name: OSHA ITA Form 300A
- description: Wage violations, back wages, and affected-employee counts.
  name: WHD (Wage and Hour Division)
- description: Mine safety violations and penalties.
  name: MSHA
- description: Environmental compliance covering air, water, waste, and drinking water.
  name: EPA ECHO
- description: Labor practice charges and union representation cases.
  name: NLRB
- description: Motor carrier safety data.
  name: FMCSA
- description: Foreign labor certifications including H-1B, H-2A, and H-2B.
  name: OFLC
- description: Bureau of Labor Statistics industry injury rate benchmarks.
  name: BLS SOII
- description: Federal debarment and suspension exclusions.
  name: SAM.gov
- description: Nursing home ratings and deficiencies indexed by CCN.
  name: CMS
- description: 25-year history of federal contract awards.
  name: USAspending.gov
- description: Product recall data.
  name: CPSC
- description: Vehicle recall and defect complaint data.
  name: NHTSA
- description: SEC enforcement actions and public-company filings.
  name: SEC EDGAR
- description: Federal prosecutions and plea agreement records.
  name: UVA Corporate Prosecution Registry
- description: Billing webhook intake is wired into the API for subscription lifecycle events.
  name: Stripe
- description: Several FastDOL datasets are mirrored on the FastDOLz Hugging Face organization for ML and bulk research workflows.
  name: Hugging Face Datasets
json_schemas:
- name: BatchLookupItem
  property_count: 6
  slug: fastdol-batch-lookup-item
- name: BatchLookupRequest
  property_count: 1
  slug: fastdol-batch-lookup-request
- name: Body_upload_csv_v1_employers_upload_csv_post
  property_count: 1
  slug: fastdol-body-upload-csv-v1-employers-upload-csv-post
- name: CreateKeyRequest
  property_count: 2
  slug: fastdol-create-key-request
- name: DeleteAccountRequest
  property_count: 2
  slug: fastdol-delete-account-request
- name: ExportFilters
  property_count: 17
  slug: fastdol-export-filters
- name: ExportRequest
  property_count: 5
  slug: fastdol-export-request
- name: FeedbackRequest
  property_count: 3
  slug: fastdol-feedback-request
- name: ForgotPasswordRequest
  property_count: 1
  slug: fastdol-forgot-password-request
- name: LoginRequest
  property_count: 2
  slug: fastdol-login-request
- name: ResetPasswordRequest
  property_count: 2
  slug: fastdol-reset-password-request
- name: SignupRequest
  property_count: 3
  slug: fastdol-signup-request
- name: VerifyEmailRequest
  property_count: 1
  slug: fastdol-verify-email-request
json_structures:
- name: Fastdol Batch Lookup Item Structure
  property_count: 6
  slug: fastdol-batch-lookup-item-structure
- name: Fastdol Batch Lookup Request Structure
  property_count: 1
  slug: fastdol-batch-lookup-request-structure
- name: Fastdol Body Upload Csv V1 Employers Upload Csv Post Structure
  property_count: 1
  slug: fastdol-body-upload-csv-v1-employers-upload-csv-post-structure
- name: Fastdol Create Key Request Structure
  property_count: 2
  slug: fastdol-create-key-request-structure
- name: Fastdol Delete Account Request Structure
  property_count: 2
  slug: fastdol-delete-account-request-structure
- name: Fastdol Export Filters Structure
  property_count: 17
  slug: fastdol-export-filters-structure
- name: Fastdol Export Request Structure
  property_count: 5
  slug: fastdol-export-request-structure
- name: Fastdol Feedback Request Structure
  property_count: 3
  slug: fastdol-feedback-request-structure
- name: Fastdol Forgot Password Request Structure
  property_count: 1
  slug: fastdol-forgot-password-request-structure
- name: Fastdol Login Request Structure
  property_count: 2
  slug: fastdol-login-request-structure
- name: Fastdol Reset Password Request Structure
  property_count: 2
  slug: fastdol-reset-password-request-structure
- name: Fastdol Signup Request Structure
  property_count: 3
  slug: fastdol-signup-request-structure
- name: Fastdol Verify Email Request Structure
  property_count: 1
  slug: fastdol-verify-email-request-structure
jsonld:
- class_count: 21
  name: Fastdol Context
  property_count: 17
  slug: fastdol-context
layout: provider
modified: '2026-05-19'
name: FastDOL
nav: Providers
network: true
overview: 'FastDOL publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Dashboard API, Employers API, and 8 more. Tagged areas include OSHA, Compliance, Workplace Safety, Public Records, and Federal Enforcement.


  The FastDOL catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  FastDOL''s developer surface includes documentation, API reference, sandbox, signup flow, pricing, engineering blog, support, and 19 more developer resources.'
plans:
- name: Fastdol Plans Pricing
  plan_count: 2
  slug: fastdol-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 10
  name: Fastdol Rate Limits
  slug: fastdol-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: FastDOL API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: fastdol-jsonschema-spectral-rules
- effective_rule_count: 73
  extends:
  - spectral:oas
  name: FastDOL API Rules
  rule_count: 32
  severity_counts:
    error: 8
    hint: 0
    info: 6
    warn: 18
  slug: fastdol-rules
score:
  band: developing
  composite: 49.8
  coverage:
    artifact_dirs: 16
    catalog_gap: 28.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 28.8
    contract_quality: 67.4
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 31.6
  previous_composite: 49.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 38.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fastdol/refs/heads/main/screenshots/fastdol-2026-06-20T181047.png
security:
- kind: domain-security
  name: Fastdol Domain Security
  slug: fastdol-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fastdol
solutions:
- description: 50 monthly API lookups per key, no credit card required, for evaluation and light research use.
  name: Free Tier
- description: Custom-quota API access, bulk export, dataset licensing, and custom integrations contracted directly with FastDOL.
  name: Enterprise Data Licensing
tags:
- OSHA
- Compliance
- Workplace Safety
- Public Records
- Federal Enforcement
- Labor
use_cases:
- description: Reporters investigating workplace safety, wage theft, or environmental violations at specific employers or industries.
  name: Journalism and Investigations
- description: Investment funds screening portfolio companies for material labor, safety, and compliance liabilities.
  name: ESG and Responsible Investment
- description: Workers compensation and commercial casualty underwriters pricing risk based on federal enforcement history.
  name: Insurance Underwriting
- description: Procurement teams vetting suppliers and contractors against federal debarment, OSHA, and EPA records.
  name: Procurement and Vendor Risk
- description: Unions and worker advocates identifying chronic violators and industry-wide enforcement patterns.
  name: Labor Organizing and Worker Advocacy
- description: Labor economists, public health researchers, and policy analysts studying enforcement effectiveness and worker safety outcomes.
  name: Academic Research
- description: Plaintiffs counsel and defense firms researching defendant enforcement history.
  name: Legal Discovery and Litigation Support
- description: Corporate compliance teams benchmarking their own facilities against industry peers.
  name: Compliance and Audit Functions
website: https://fastdol.com/
---

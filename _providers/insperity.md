---
access_model:
  confidence: high
  label: Customer-only; key issued by an Insperity Integration Specialist behind an IP allow-list
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://developer.insperity.com/get-started
  - https://developer.insperity.com/api/swagger/payroll_tax
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-09-16'
api_count: 4
apis:
- description: Use your own applicant tracking or HR application to send candidate hire information to Insperity Premier Onboarding. One published operation, POST /public/Employee/Onboarding/v2, which accepts a call
  name: Insperity Onboarding API
  slug: insperity-onboarding-api
- description: Update an employee's compensation and retrieve general ledger information post payroll. Three published operations covering billing group changes, remuneration changes and the payroll ledger read.
  name: Insperity Payroll & Tax API
  slug: insperity-payroll-tax-api
- description: Transfer employee information to and from Insperity Premier. Twenty-six published operations — fifteen named employee change events written as POSTs (address, email, phone, department, location, super
  name: Insperity HRIS API
  slug: insperity-hris-api
- description: Company-scoped reference data. Some Insperity API fields require specific values as defined in Insperity Premier, and the Core APIs return the list of accepted options — benefit classes, billing group
  name: Insperity Core API
  slug: insperity-core-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.insperity.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/insperity
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.insperity.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.insperity.com/developer-resources
- group: docs
  title: ''
  type: APIReference
  url: https://developer.insperity.com/categories
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.insperity.com/get-started
- group: operate
  title: ''
  type: Support
  url: https://developer.insperity.com/faq
- group: company
  title: ''
  type: Blog
  url: https://www.insperity.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.insperity.com/privacy-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/insperity/refs/heads/main/authentication/insperity-authentication.yml
  title: ''
  type: Authentication
  url: authentication/insperity-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/insperity/refs/heads/main/conventions/insperity-conventions.yml
  title: ''
  type: Conventions
  url: conventions/insperity-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/insperity/refs/heads/main/errors/insperity-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/insperity-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/insperity/refs/heads/main/rate-limits/insperity-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/insperity-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/insperity/refs/heads/main/plans/insperity-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/insperity-plans-pricing.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/insperity/refs/heads/main/sandbox/insperity-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/insperity-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/insperity/refs/heads/main/lifecycle/insperity-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/insperity-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/insperity/refs/heads/main/conformance/insperity-conformance.yml
  title: ''
  type: Conformance
  url: conformance/insperity-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/insperity/refs/heads/main/data-model/insperity-data-model.yml
  title: ''
  type: DataModel
  url: data-model/insperity-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/insperity/refs/heads/main/packages/insperity-packages.yml
  title: ''
  type: Packages
  url: packages/insperity-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/insperity/refs/heads/main/llms/insperity-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/insperity-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/insperity/refs/heads/main/security/insperity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/insperity-domain-security.yml
created: '2026-04-28'
description: 'Insperity is a professional employer organization (PEO) headquartered in Kingwood, Texas that provides human resources and business performance solutions to small and medium-sized businesses, including payroll processing, employee benefits, workers'' compensation, HR compliance and the Insperity Premier HR technology platform. Insperity Premier exposes a REST Public API at https://api.insperity.com/public organized into four categories — Onboarding, Payroll & Tax, HRIS and Core — covering 45 publicly listed operations that let a client''s applicant tracking system, HRIS or payroll application send new-hire records, submit employee change events, retrieve post-payroll general ledger data, and read the company-scoped reference code lists those writes must resolve against. Access is not self-service: a key is issued per customer by an Insperity Integration Specialist after an API Terms of Use Agreement is signed, requests must originate from allow-listed IP addresses, and the
  developer portal''s Swagger documents require a Premier account.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/insperity.png
layout: provider
modified: '2026-09-13'
name: Insperity
nav: Providers
network: true
overview: 'Insperity publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 1000, Human Resources, Payroll, Benefits, and HRIS.


  Insperity''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 14 more developer resources.'
plans:
- name: Insperity Plans Pricing
  plan_count: 0
  slug: insperity-plans-pricing
press:
- date: '2026-05-25'
  title: 'Artificial Intelligence (AI) At Work: What You Need To Know'
  url: https://www.insperity.com/blog/artificial-intelligence-ai-at-work-what-you-need-to-know/
- date: '2026-05-25'
  title: Insperity Archives - NSCA
  url: https://www.nsca.org/tag/insperity/
- date: '2026-05-25'
  title: 'Earnings call transcript: Insperity Q1 2026 earnings miss ...'
  url: https://www.investing.com/news/transcripts/earnings-call-transcript-insperity-q1-2026-earnings-miss-forecast-stock-dips-93CH-4651652
- date: '2026-05-25'
  title: Business Outlook Report 2024
  url: https://www.insperity.com/resources/guide/business-outlook-report/
- date: '2026-05-25'
  title: Workday and Insperity Announce Exclusive Strategic ...
  url: https://newsroom.workday.com/2024-02-08-Workday-and-Insperity-Announce-Exclusive-Strategic-Partnership-to-Provide-Best-in-Class-HR-Service-and-Technology-to-Small-and-Midsize-Businesses
random_paper: 9
rate_limits:
- limit_count: 0
  name: Insperity Rate Limits
  slug: insperity-rate-limits
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 74.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 22.9
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/insperity/refs/heads/main/screenshots/insperity-2026-06-20T183405.png
security:
- kind: authentication
  name: Insperity Authentication
  slug: insperity-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Insperity Domain Security
  slug: insperity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: insperity
tags:
- Fortune 1000
- Human Resources
- Payroll
- Benefits
- HRIS
- Onboarding
- Professional Employer Organization
- Workforce Management
- Employer of Record
website: https://www.insperity.com
---

---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 27
  human_in_the_loop: 1
  name: Kolayik Agentic Access
  operation_count: 46
  slug: kolayik-agentic-access
  summary_line: 46 operations · 27 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.kolayik.com
  baseurl_source: declared
  description: The Approval Process API from KolayIK — 1 operation(s) for approval process.
  name: KolayIK Approval Process API
  slug: kolayik-approval-process-api
- baseURL: https://api.kolayik.com
  baseurl_source: declared
  description: The Calendar API from KolayIK — 5 operation(s) for calendar.
  name: KolayIK Calendar API
  slug: kolayik-calendar-api
- baseURL: https://api.kolayik.com
  baseurl_source: declared
  description: The Expense API from KolayIK — 1 operation(s) for expense.
  name: KolayIK Expense API
  slug: kolayik-expense-api
- baseURL: https://api.kolayik.com
  baseurl_source: declared
  description: The Leave API from KolayIK — 3 operation(s) for leave.
  name: KolayIK Leave API
  slug: kolayik-leave-api
- baseURL: https://api.kolayik.com
  baseurl_source: declared
  description: The Payroll API from KolayIK — 2 operation(s) for payroll.
  name: KolayIK Payroll API
  slug: kolayik-payroll-api
- baseURL: https://api.kolayik.com
  baseurl_source: declared
  description: The Person API from KolayIK — 18 operation(s) for person.
  name: KolayIK Person API
  slug: kolayik-person-api
- baseURL: https://api.kolayik.com
  baseurl_source: declared
  description: The Profile API from KolayIK — 1 operation(s) for profile.
  name: KolayIK Profile API
  slug: kolayik-profile-api
- baseURL: https://api.kolayik.com
  baseurl_source: declared
  description: The Timelog API from KolayIK — 4 operation(s) for timelog.
  name: KolayIK Timelog API
  slug: kolayik-timelog-api
- baseURL: https://api.kolayik.com
  baseurl_source: declared
  description: The Training API from KolayIK — 5 operation(s) for training.
  name: KolayIK Training API
  slug: kolayik-training-api
- baseURL: https://api.kolayik.com
  baseurl_source: declared
  description: The Transaction API from KolayIK — 4 operation(s) for transaction.
  name: KolayIK Transaction API
  slug: kolayik-transaction-api
- baseURL: https://api.kolayik.com
  baseurl_source: declared
  description: The Unit API from KolayIK — 2 operation(s) for unit.
  name: KolayIK Unit API
  slug: kolayik-unit-api
arazzos:
- description: Resolve an employee, read their leave balances, check for overlapping leave in the window, create the leave record, and verify it.
  name: Check balances and book leave in Kolay İK
  slug: kolayik-book-leave
- description: Discover the tenant's custom person fields and org tree, create the person, verify the stored record, and assign onboarding training.
  name: Onboard an employee in Kolay İK
  slug: kolayik-onboard-employee
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kolay Public Approval Process API
  slug: open-kolayik-approval-process-api
- collection_type: open
  name: Kolay Public Approval Process Calendar API
  slug: open-kolayik-calendar-api
- collection_type: open
  name: Kolay Public Approval Process Expense API
  slug: open-kolayik-expense-api
- collection_type: open
  name: Kolay Public Approval Process Leave API
  slug: open-kolayik-leave-api
- collection_type: open
  name: Kolay Public Approval Process Payroll API
  slug: open-kolayik-payroll-api
- collection_type: open
  name: Kolay Public Approval Process Person API
  slug: open-kolayik-person-api
- collection_type: open
  name: Kolay Public Approval Process Profile API
  slug: open-kolayik-profile-api
- collection_type: open
  name: Kolay Public Approval Process Timelog API
  slug: open-kolayik-timelog-api
- collection_type: open
  name: Kolay Public Approval Process Training API
  slug: open-kolayik-training-api
- collection_type: open
  name: Kolay Public Approval Process Transaction API
  slug: open-kolayik-transaction-api
- collection_type: open
  name: Kolay Public Approval Process Unit API
  slug: open-kolayik-unit-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/kolayik-public-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kolayik-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kolayik-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://kolayik.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.kolayik.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.kolayik.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.kolayik.com/
- group: build
  title: ''
  type: Postman
  url: https://apidocs.kolayik.com/
- group: start
  title: ''
  type: SignUp
  url: https://kolayik.com/kayit-ol
- group: start
  title: ''
  type: Login
  url: https://app.kolayik.com/home
- group: commercial
  title: ''
  type: Pricing
  url: https://kolayik.com/insan-kaynaklari-yazilimi-fiyatlari
- group: operate
  title: ''
  type: Support
  url: https://destek.kolayik.com/tr/
- group: operate
  title: ''
  type: HelpCenter
  url: https://destek.kolayik.com/tr/
- group: company
  title: ''
  type: Blog
  url: https://kolayik.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kolayik
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kolayik.com/kullanici-sozlesmesi
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kolayik.com/internet-sitesi-kvkk
- group: auth
  title: ''
  type: Security
  url: https://kolayik.com/bilgi-guvenligi-politikasi
- group: auth
  title: ''
  type: Compliance
  url: https://kolayik.com/bilgi-guvenligi-politikasi
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kolayik.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://updates.kolayik.com/tr
- group: operate
  title: ''
  type: Contact
  url: https://kolayik.com/iletisim
- group: company
  title: ''
  type: About
  url: https://kolayik.com/hakkimizda
- group: learn
  title: ''
  type: Academy
  url: https://akademi.kolayik.com/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/kolayik
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kolayik/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCR3rklQaddzZsppuFM4YxHw
- group: auth
  title: ''
  type: Authentication
  url: authentication/kolayik-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kolayik-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kolayik-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kolayik-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kolayik-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kolayik-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/kolayik-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kolayik-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/kolayik-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kolayik-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/kolayik-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kolayik-onboard-employee.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kolayik-book-leave.yml
created: '2026-07-17'
description: Kolay İK (Kolay Yazılım A.Ş.) is an Istanbul-based cloud human-resources and human-capital-management SaaS platform serving more than 4,500 companies and 300,000+ employees, predominantly in Türkiye. The product covers employee/personnel records (özlük), payroll (bordro), performance evaluation, shift management (vardiya), compensation review, applicant tracking, HR analytics, time and attendance (PDKS), leave management, expense and asset tracking, and training. Kolay publishes an official public REST API — the "Kolay Public API" (v2, https://api.kolayik.com) — documented as a public Postman collection at apidocs.kolayik.com, covering person, unit, leave, timelog, transaction, approval, calendar, training, expense and payroll resources, authenticated with a bearer API token created from the in-product developer settings.
image: https://cdn.prod.website-files.com/6113889e45c6e62ebf4ca212/616f325923c82836146d34aa_kolay-ik-logo-tr.svg
layout: provider
modified: '2026-07-19'
name: KolayIK
nav: Providers
network: true
overview: 'KolayIK publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Approval Process API, Calendar API, Expense API, and 8 more. Tagged areas include Company, Human Resources, HR, Payroll, and HCM.


  KolayIK''s developer surface includes documentation, API reference, signup flow, pricing, support, engineering blog, changelog, and 34 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 49.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 54.4
    developer_ergonomics: 51.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - turkey
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 48.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kolayik/refs/heads/main/screenshots/kolayik-2026-07-25T224126.png
security:
- kind: authentication
  name: Kolayik Authentication
  slug: kolayik-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kolayik Domain Security
  slug: kolayik-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kolayik Vulnerability Disclosure
  slug: kolayik-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: kolayik
tags:
- Company
- Human Resources
- HR
- Payroll
- HCM
- Employee Management
- Time and Attendance
- Applicant Tracking
- Software-as-a-Service
- Turkey
website: https://kolayik.com
---

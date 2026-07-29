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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 27
  human_in_the_loop: 1
  name: Kolayik Agentic Access
  operation_count: 46
  slug: kolayik-agentic-access
  summary_line: 46 operations · 27 acting · 1 human-in-the-loop
api_count: 11
apis:
- description: The Approval Process API from KolayIK — 1 operation(s) for approval process.
  name: KolayIK Approval Process API
  slug: kolayik-approval-process-api
- description: The Calendar API from KolayIK — 5 operation(s) for calendar.
  name: KolayIK Calendar API
  slug: kolayik-calendar-api
- description: The Expense API from KolayIK — 1 operation(s) for expense.
  name: KolayIK Expense API
  slug: kolayik-expense-api
- description: The Leave API from KolayIK — 3 operation(s) for leave.
  name: KolayIK Leave API
  slug: kolayik-leave-api
- description: The Payroll API from KolayIK — 2 operation(s) for payroll.
  name: KolayIK Payroll API
  slug: kolayik-payroll-api
- description: The Person API from KolayIK — 18 operation(s) for person.
  name: KolayIK Person API
  slug: kolayik-person-api
- description: The Profile API from KolayIK — 1 operation(s) for profile.
  name: KolayIK Profile API
  slug: kolayik-profile-api
- description: The Timelog API from KolayIK — 4 operation(s) for timelog.
  name: KolayIK Timelog API
  slug: kolayik-timelog-api
- description: The Training API from KolayIK — 5 operation(s) for training.
  name: KolayIK Training API
  slug: kolayik-training-api
- description: The Transaction API from KolayIK — 4 operation(s) for transaction.
  name: KolayIK Transaction API
  slug: kolayik-transaction-api
- description: The Unit API from KolayIK — 2 operation(s) for unit.
  name: KolayIK Unit API
  slug: kolayik-unit-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Resolve an employee, read their leave balances, check for overlapping leave in the window, create the leave record, and verify it.
  name: Check balances and book leave in Kolay İK
  slug: kolayik-book-leave
- description: Discover the tenant's custom person fields and org tree, create the person, verify the stored record, and assign onboarding training.
  name: Onboard an employee in Kolay İK
  slug: kolayik-onboard-employee
artifact_total: 19
common:
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
  type: MCPServer
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
mcp_servers:
- description: ''
  name: kolayik-mcp.yml
  slug: kolayik-mcpyml
modified: '2026-07-19'
name: KolayIK
nav: Providers
network: true
overview: 'KolayIK publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Approval Process API, Calendar API, Expense API, and 8 more. Tagged areas include Company, Human Resources, HR, Payroll, and Human Capital Management.


  KolayIK''s developer surface includes documentation, API reference, signup flow, pricing, support, engineering blog, changelog, and 33 more developer resources.'
random_paper: 63
score:
  band: developing
  composite: 52.8
  delta: -0.1
  facets:
    commercial_clarity: 52.6
    contract_quality: 57.8
    developer_ergonomics: 49.5
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 47.4
  previous_composite: 52.9
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
  schema_version: 0.6
  scored_at: '2026-07-28'
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
- Human Capital Management
- Employee Management
- Time and Attendance
- Applicant Tracking
- SaaS
- Turkey
website: https://kolayik.com
---

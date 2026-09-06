---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'Miter exposes a REST API used to build custom integrations between the Miter HCM platform and construction ERPs, accounting, and workforce systems — syncing projects, cost codes, accounts, employees, '
  name: Miter REST API
  slug: miter-rest-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/miter-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/miter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.miter.com/
- group: operate
  title: ''
  type: Support
  url: https://support.miter.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.miter.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/miter-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/miter-llms.txt
- group: auth
  title: ''
  type: Compliance
  url: https://www.miter.com/compliance/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.miter.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.miter.com/terms-of-service
- group: start
  title: ''
  type: Login
  url: https://dashboard.miter.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.miter.com/resources/
created: '2026-07-17'
description: Miter is a Human Capital Management (HCM) platform purpose-built for construction contractors, consolidating payroll, HR, benefits, field operations, and expense management into a single connected system. Its construction payroll automates prevailing-wage, certified-payroll, and union compliance, multi-state tax handling, and fully-burdened job-cost tracking in real time, while its HRIS covers recruiting, benefits, performance, and learning. Field Operations adds time tracking, scheduling, daily reports, production tracking, and safety, and Expense Management handles reimbursements, per diems, and corporate cards. Miter connects to construction ERPs and accounting systems (Sage Intacct, NetSuite, Acumatica, QuickBooks, Procore, Viewpoint, and more) through off-the-shelf integrations or a custom REST API. Backed by Bessemer Venture Partners.
image: https://www.miter.com/wp-content/uploads/2025/03/OpenGraph-Homepage.jpg
layout: provider
modified: '2026-07-20'
name: Miter
nav: Providers
network: true
overview: 'Miter publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Vertical Software, Construction, Payroll, and HCM.


  Miter''s developer surface includes support, engineering blog, and 10 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 18.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/miter/refs/heads/main/screenshots/miter-2026-08-07T183806.png
security:
- kind: domain-security
  name: Miter Domain Security
  slug: miter-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Miter Trust Center
  slug: miter-trust-center
  summary_line: SOC 2 Type II
slug: miter
tags:
- Company
- Vertical Software
- Construction
- Payroll
- HCM
- HR
- Field Operations
- Expense Management
- Workforce Management
- Fintech
website: https://www.miter.com/
---

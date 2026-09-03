---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  - rate-limits
  - security
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jirav-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jirav.com/
- group: company
  title: ''
  type: Blog
  url: https://www.jirav.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.jirav.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.jirav.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jirav.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jirav.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://help.jirav.com/support-portal
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://help.jirav.com/release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/jirav-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/jirav-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jirav-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jirav-llms.txt
coverage:
  checked: '2026-08-23'
  detail: Jirav ships FP&A software as an end-user web app only — every host was probed and the company publishes no developer portal, no API reference and no contract of any kind; the only REST surface, a /v1/* Spring Boot API, is the private backend of its own AngularJS app at https://app.jirav.com/-/ and it is documented nowhere.
  evidence:
  - status: 404
    url: https://www.jirav.com/openapi.json
  - status: 404
    url: https://app.jirav.com/v3/api-docs
  - status: 404
    url: https://app.jirav.com/graphql
  - status: 0
    url: https://api.jirav.com/
  - status: 200
    url: https://help.jirav.com/integrations
  reason: no-developer-program
  state: none
created: '2026-08-23'
description: Jirav is a financial planning and analysis (FP&A) platform for growth companies and for accounting and CFO advisory firms, combining reporting, dashboards, budgeting, forecasting, scenario modeling and workforce planning in a single hosted web application. It imports actuals from accounting systems (QuickBooks Online, QuickBooks Desktop, Xero, Oracle NetSuite, Sage Intacct) and from payroll and HR systems (Gusto, Paychex Flex, ADP RUN, BambooHR, Paylocity, TriNet, Justworks, UKG Ready), plus Excel and Google Sheets uploads, then drives three-way pro forma financials, budget-versus-actual analysis, KPI libraries and board-ready report packages from that data. Jirav sells direct to finance teams and wholesale through an accounting partner program. The integrations are one-way inbound connectors that Jirav operates against other vendors' APIs; as of this profile Jirav publishes no developer program, no public REST or GraphQL API, no SDK, and no webhook surface of its own.
image: https://www.jirav.com/hubfs/header-logo.png
layout: provider
modified: '2026-08-23'
name: Jirav
nav: Providers
network: true
overview: 'Jirav is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Planning, FP&A, Budgeting, and Forecasting.


  Jirav''s developer surface includes engineering blog, pricing, support, release notes, changelog, and 8 more developer resources.'
plans:
- name: Jirav Plans Pricing
  plan_count: 5
  slug: jirav-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Jirav Rate Limits
  slug: jirav-rate-limits
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 11
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 23.2
  provenance:
    mcp: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jirav/refs/heads/main/screenshots/jirav-2026-09-02T145943.png
security:
- kind: domain-security
  name: Jirav Domain Security
  slug: jirav-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jirav
tags:
- Company
- Financial Planning
- FP&A
- Budgeting
- Forecasting
- Accounting
- Reporting
- Dashboards
- Business Intelligence
- Software-as-a-Service
website: https://www.jirav.com/
---

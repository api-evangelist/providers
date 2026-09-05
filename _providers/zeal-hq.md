---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Zeal Hq Agentic Access
  operation_count: 36
  slug: zeal-hq-agentic-access
  summary_line: 36 operations · 19 acting
api_count: 1
apis:
- baseURL: https://api.zeal.com
  baseurl_source: declared
  description: The Companies API from Zeal — 3 operation(s) for companies.
  name: Zeal Companies API
  slug: zeal-hq-companies-api
- baseURL: https://api.zeal.com
  baseurl_source: declared
  description: The Contractor Payments API from Zeal — 2 operation(s) for contractor payments.
  name: Zeal Contractor Payments API
  slug: zeal-hq-contractor-payments-api
- baseURL: https://api.zeal.com
  baseurl_source: declared
  description: The Contractors API from Zeal — 2 operation(s) for contractors.
  name: Zeal Contractors API
  slug: zeal-hq-contractors-api
- baseURL: https://api.zeal.com
  baseurl_source: declared
  description: The Employee Check API from Zeal — 3 operation(s) for employee check.
  name: Zeal Employee Check API
  slug: zeal-hq-employee-check-api
- baseURL: https://api.zeal.com
  baseurl_source: declared
  description: The Employees API from Zeal — 4 operation(s) for employees.
  name: Zeal Employees API
  slug: zeal-hq-employees-api
- baseURL: https://api.zeal.com
  baseurl_source: declared
  description: The Funding API from Zeal — 1 operation(s) for funding.
  name: Zeal Funding API
  slug: zeal-hq-funding-api
- baseURL: https://api.zeal.com
  baseurl_source: declared
  description: The Onboarding API from Zeal — 3 operation(s) for onboarding.
  name: Zeal Onboarding API
  slug: zeal-hq-onboarding-api
- baseURL: https://api.zeal.com
  baseurl_source: declared
  description: The Pay Schedules API from Zeal — 3 operation(s) for pay schedules.
  name: Zeal Pay Schedules API
  slug: zeal-hq-pay-schedules-api
- baseURL: https://api.zeal.com
  baseurl_source: declared
  description: The Reports API from Zeal — 4 operation(s) for reports.
  name: Zeal Reports API
  slug: zeal-hq-reports-api
- baseURL: https://api.zeal.com
  baseurl_source: declared
  description: The Tax API from Zeal — 4 operation(s) for tax.
  name: Zeal Tax API
  slug: zeal-hq-tax-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zeal Companies API
  slug: open-zeal-hq-companies-api
- collection_type: open
  name: Zeal Companies Contractor Payments API
  slug: open-zeal-hq-contractor-payments-api
- collection_type: open
  name: Zeal Companies Contractors API
  slug: open-zeal-hq-contractors-api
- collection_type: open
  name: Zeal Companies Employee Check API
  slug: open-zeal-hq-employee-check-api
- collection_type: open
  name: Zeal Companies Employees API
  slug: open-zeal-hq-employees-api
- collection_type: open
  name: Zeal Companies Funding API
  slug: open-zeal-hq-funding-api
- collection_type: open
  name: Zeal Companies Onboarding API
  slug: open-zeal-hq-onboarding-api
- collection_type: open
  name: Zeal Companies Pay Schedules API
  slug: open-zeal-hq-pay-schedules-api
- collection_type: open
  name: Zeal Companies Reports API
  slug: open-zeal-hq-reports-api
- collection_type: open
  name: Zeal Companies Tax API
  slug: open-zeal-hq-tax-api
- collection_type: open
  name: Zeal API
  slug: open-zeal-hq
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zeal-hq-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zeal-hq-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zeal-hq-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zeal-holdings
- group: company
  title: ''
  type: Website
  url: https://www.zeal.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zeal.com
- group: commercial
  title: ''
  type: Plans
  url: plans/zeal-hq-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zeal-hq-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zeal-hq-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.zeal.com/blog/rss.xml
created: '2026-07-01'
description: Zeal is an embedded, payroll-as-a-service platform. Its API lets software companies build their own payroll products - onboarding companies, employees, and 1099 contractors, running pay runs, disbursing pay, and handling tax calculation, filing, and compliance across all US jurisdictions - without becoming a payroll company themselves.
finops:
- name: Zeal Hq Finops
  service_category: Payroll and Human Resources
  slug: zeal-hq-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zeal-hq.png
layout: provider
modified: '2026-07-01'
name: Zeal
nav: Providers
network: true
overview: 'Zeal publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Companies API, Contractor Payments API, Contractors API, and 7 more. Tagged areas include Payroll, Embedded Finance, Fintech, Tax Compliance, and Contractors.


  Zeal''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Zeal Hq Plans Pricing
  plan_count: 4
  slug: zeal-hq-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Zeal Hq Rate Limits
  slug: zeal-hq-rate-limits
score:
  band: thin
  composite: 38.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 50.9
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zeal-hq/refs/heads/main/screenshots/zeal-hq-2026-09-02T171511.png
security:
- kind: authentication
  name: Zeal Hq Authentication
  slug: zeal-hq-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zeal Hq Domain Security
  slug: zeal-hq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zeal-hq
tags:
- Payroll
- Embedded Finance
- Fintech
- Tax Compliance
- Contractors
- Human Resources
website: https://www.zeal.com
---

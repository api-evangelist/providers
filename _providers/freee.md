---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Freee Agentic Access
  operation_count: 42
  slug: freee-agentic-access
  summary_line: 42 operations · 18 acting
api_count: 12
apis:
- description: Accounting account items / chart of accounts (勘定科目).
  name: freee Account Items API
  slug: freee-account-items-api
- description: Time clocks (打刻) and work records (勤怠).
  name: freee Attendance API
  slug: freee-attendance-api
- description: freee companies (事業所) the authenticated user can access.
  name: freee Companies API
  slug: freee-companies-api
- description: Accounting deals / transactions (取引) - income and expense records.
  name: freee Deals API
  slug: freee-deals-api
- description: HR employees (従業員).
  name: freee Employees API
  slug: freee-employees-api
- description: Authenticated HR user context.
  name: freee HR Users API
  slug: freee-hr-users-api
- description: Issued invoices and quotations (請求書・見積書).
  name: freee Invoices API
  slug: freee-invoices-api
- description: Journals (仕訳帳), manual journals, and trial-balance reports.
  name: freee Journals API
  slug: freee-journals-api
- description: Trading partners / counterparties (取引先).
  name: freee Partners API
  slug: freee-partners-api
- description: Employee payroll statements (給与明細) and bonuses.
  name: freee Payroll API
  slug: freee-payroll-api
- description: Tax codes (税区分) available to a company.
  name: freee Taxes API
  slug: freee-taxes-api
- description: Wallet transactions / statement lines (明細) and walletables (口座).
  name: freee Wallet Transactions API
  slug: freee-wallet-transactions-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: freee API (Accounting and HR/Payroll) Account Items API
  slug: open-freee-account-items-api
- collection_type: open
  name: freee API (Accounting and HR/Payroll) Account Items Attendance API
  slug: open-freee-attendance-api
- collection_type: open
  name: freee API (Accounting and HR/Payroll) Account Items Companies API
  slug: open-freee-companies-api
- collection_type: open
  name: freee API (Accounting and HR/Payroll) Account Items Deals API
  slug: open-freee-deals-api
- collection_type: open
  name: freee API (Accounting and HR/Payroll) Account Items Employees API
  slug: open-freee-employees-api
- collection_type: open
  name: freee API (Accounting and HR/Payroll) Account Items HR Users API
  slug: open-freee-hr-users-api
- collection_type: open
  name: freee API (Accounting and HR/Payroll) Account Items Invoices API
  slug: open-freee-invoices-api
- collection_type: open
  name: freee API (Accounting and HR/Payroll) Account Items Journals API
  slug: open-freee-journals-api
- collection_type: open
  name: freee API (Accounting and HR/Payroll) Account Items Partners API
  slug: open-freee-partners-api
- collection_type: open
  name: freee API (Accounting and HR/) Account Items Payroll API
  slug: open-freee-payroll-api
- collection_type: open
  name: freee API (Accounting and HR/Payroll) Account Items Taxes API
  slug: open-freee-taxes-api
- collection_type: open
  name: freee API (Accounting and HR/Payroll) Account Items Wallet Transactions API
  slug: open-freee-wallet-transactions-api
- collection_type: open
  name: freee API (Accounting and HR/Payroll)
  slug: open-freee
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/freee-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freee-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/freee-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/freee
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/freeekk
- group: company
  title: ''
  type: Website
  url: https://www.freee.co.jp/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.freee.co.jp/
- group: commercial
  title: ''
  type: Plans
  url: plans/freee-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/freee-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/freee-finops.yml
created: '2026-07-12'
description: freee K.K. (freee株式会社) is a Japanese cloud business-management SaaS company. Its core products are freee Accounting (会計freee) - cloud accounting and bookkeeping - and freee HR & Payroll (人事労務freee) - HR, attendance, and payroll - plus invoicing (freee請求書) and sales management. freee exposes well-documented public REST APIs for both accounting and HR, authenticated with OAuth 2.0 (authorization code). Accounting endpoints live under https://api.freee.co.jp/api/1 and HR / payroll endpoints under https://api.freee.co.jp/hr/api/v1, and freee publishes machine-readable OpenAPI schemas for its platform.
finops:
- name: Freee Finops
  service_category: Business Applications
  slug: freee-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/freee.png
layout: provider
modified: '2026-07-12'
name: freee
nav: Providers
network: true
overview: 'freee publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Account Items API, Attendance API, Companies API, and 9 more. Tagged areas include Accounting, Bookkeeping, HR, Payroll, and Invoicing.


  freee''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Freee Plans Pricing
  plan_count: 5
  slug: freee-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Freee Rate Limits
  slug: freee-rate-limits
score:
  band: thin
  composite: 37.2
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 58.0
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/freee/refs/heads/main/screenshots/freee-2026-07-25T215132.png
security:
- kind: authentication
  name: Freee Authentication
  slug: freee-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Freee Domain Security
  slug: freee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: freee
tags:
- Accounting
- Bookkeeping
- HR
- Payroll
- Invoicing
- Finance
- Software-as-a-Service
- Japan
website: https://www.freee.co.jp/
---

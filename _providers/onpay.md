---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Onpay Agentic Access
  operation_count: 58
  slug: onpay-agentic-access
  summary_line: 58 operations · 28 acting
api_count: 6
apis:
- description: The Company API from OnPay — 17 operation(s) for company.
  name: OnPay Company API
  slug: onpay-company-api
- description: The Deductions API from OnPay — 7 operation(s) for deductions.
  name: OnPay Deductions API
  slug: onpay-deductions-api
- description: The Employees API from OnPay — 14 operation(s) for employees.
  name: OnPay Employees API
  slug: onpay-employees-api
- description: The Pay-runs API from OnPay — 2 operation(s) for pay-runs.
  name: OnPay Pay Runs API
  slug: onpay-pay-runs-api
- description: The Reports API from OnPay — 2 operation(s) for reports.
  name: OnPay Reports API
  slug: onpay-reports-api
- description: The User API from OnPay — 1 operation(s) for user.
  name: OnPay User API
  slug: onpay-user-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onpay-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/onpay-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://onpay.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://onpay.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://onpay.readme.io/
- group: docs
  title: ''
  type: APIReference
  url: https://onpay.readme.io/reference/authorization
- group: start
  title: ''
  type: GettingStarted
  url: https://onpay.readme.io/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.onpay.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://onpay.com/insights/
- group: commercial
  title: ''
  type: Pricing
  url: https://onpay.com/payroll/software/costs-pricing/
- group: start
  title: ''
  type: SignUp
  url: https://onpay.com/get-started/
- group: start
  title: ''
  type: Login
  url: https://app.onpay.com/app/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://onpay.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://onpay.com/privacy/
- group: auth
  title: ''
  type: Security
  url: https://onpay.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://onpay.com/security/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/onpay-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/onpay-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/onpay-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/onpay-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/onpay-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/onpay-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/onpay-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/onpay-data-model.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/onpay-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-04'
description: OnPay is an Atlanta, Georgia based provider of full-service online payroll, HR, and employee benefits software for small and mid-size US businesses, founded in 2011 and funded by Carrick Capital Partners. The platform runs payroll and direct deposit, files federal, state, and local payroll taxes, and handles onboarding, PTO, org charts, health insurance, 401(k), and workers' compensation. For developers, OnPay publishes a partner-only REST API (v2) documented on a public ReadMe hub, covering employees, employee deductions, wages, leave, tax fields, bank accounts, terminations and rehires, company worksites, locations, departments and positions, pay schedules, and payroll reporting. Access is limited to approved partners, authorized with OAuth 2.0 authorization-code grants against app.onpay.com and role-scoped bearer tokens.
image: https://onpay.com/wp-content/uploads/2017/08/d9fo84j1zi.jpg
layout: provider
modified: '2026-08-04'
name: OnPay
nav: Providers
network: true
overview: 'OnPay publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Company API, Deductions API, Employees API, and 3 more. Tagged areas include payroll, human-resources, employee-benefits, payroll-tax, and small-business.


  OnPay''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 19 more developer resources.'
random_paper: 87
scopes:
- name: Onpay Scopes
  scope_count: 6
  slug: onpay-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: developing
  composite: 43.2
  delta: 0.2
  facets:
    commercial_clarity: 52.6
    contract_quality: 39.5
    developer_ergonomics: 53.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 10.5
  previous_composite: 43.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/onpay/refs/heads/main/screenshots/onpay-2026-08-07T190403.png
security:
- kind: authentication
  name: Onpay Authentication
  slug: onpay-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Onpay Domain Security
  slug: onpay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Onpay Vulnerability Disclosure
  slug: onpay-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: onpay
tags:
- payroll
- human-resources
- employee-benefits
- payroll-tax
- small-business
- workforce-management
- fintech
- hr-tech
- time-and-attendance
- retirement-401k
website: https://onpay.com/
---

---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Onpay Agentic Access
  operation_count: 58
  slug: onpay-agentic-access
  summary_line: 58 operations · 28 acting
api_count: 1
apis:
- baseURL: https://api.onpay.com/v2
  baseurl_source: declared
  description: The Company API from OnPay — 17 operation(s) for company.
  name: OnPay Company API
  slug: onpay-company-api
- baseURL: https://api.onpay.com/v2
  baseurl_source: declared
  description: The Deductions API from OnPay — 7 operation(s) for deductions.
  name: OnPay Deductions API
  slug: onpay-deductions-api
- baseURL: https://api.onpay.com/v2
  baseurl_source: declared
  description: The Employees API from OnPay — 14 operation(s) for employees.
  name: OnPay Employees API
  slug: onpay-employees-api
- baseURL: https://api.onpay.com/v2
  baseurl_source: declared
  description: The Pay-runs API from OnPay — 2 operation(s) for pay-runs.
  name: OnPay Pay Runs API
  slug: onpay-pay-runs-api
- baseURL: https://api.onpay.com/v2
  baseurl_source: declared
  description: The Reports API from OnPay — 2 operation(s) for reports.
  name: OnPay Reports API
  slug: onpay-reports-api
- baseURL: https://api.onpay.com/v2
  baseurl_source: declared
  description: The User API from OnPay — 1 operation(s) for user.
  name: OnPay User API
  slug: onpay-user-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OnPay Company API
  slug: open-onpay-company-api
- collection_type: open
  name: OnPay Deductions API
  slug: open-onpay-deductions-api
- collection_type: open
  name: OnPay Employees API
  slug: open-onpay-employees-api
- collection_type: open
  name: OnPay Pay Runs API
  slug: open-onpay-pay-runs-api
- collection_type: open
  name: OnPay Reports API
  slug: open-onpay-reports-api
- collection_type: open
  name: OnPay User API
  slug: open-onpay-user-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/onpay-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/onpay-api-overlay.yaml
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
mcp_servers:
- description: ''
  name: OnPay MCP Server
  slug: onpay-mcp-server
modified: '2026-08-04'
name: OnPay
nav: Providers
network: true
overview: 'OnPay publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Company API, Deductions API, Employees API, and 3 more. Tagged areas include Payroll, Human Resources, Employee Benefits, payroll-tax, and Small Business.


  OnPay''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
random_paper: 5
scopes:
- name: Onpay Scopes
  scope_count: 6
  slug: onpay-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 4.5
    contract_quality: 43.0
    developer_ergonomics: 39.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
- Payroll
- Human Resources
- Employee Benefits
- payroll-tax
- Small Business
- Workforce Management
- Fintech
- HR Tech
- Time and Attendance
- retirement-401k
website: https://onpay.com/
---

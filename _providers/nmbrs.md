---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
  score: 24.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Nmbrs Agentic Access
  operation_count: 10
  slug: nmbrs-agentic-access
  summary_line: 10 operations · 2 acting
api_count: 1
apis:
- description: Legacy SOAP v3 EmployeeService (300+ operations, e.g. Employee_GetCurrent, Contract_GetAll, Salary_GetCurrent, Absence2_Insert, WageComponentFixed_Insert) authenticated with a username + API token. De
  name: Nmbrs SOAP EmployeeService (Legacy)
  slug: nmbrs-soap-employee-service
- description: Legacy SOAP v3 CompanyService (120+ operations, e.g. Company_GetCurrentPeriod, Run_GetList, RunRequest_Insert, SalaryDocuments_GetAllPayslipsPDFByRunCompany, Journals_GetByRunCompany, WageTax_GetList)
  name: Nmbrs SOAP CompanyService (Legacy)
  slug: nmbrs-soap-company-service
- description: Legacy SOAP v3 DebtorService for the accountant/debtor tier that owns companies (e.g. AccountantContact_GetList, Debtor_GetList). Deprecated - retiring 1 March 2027 in favor of the REST API.
  name: Nmbrs SOAP DebtorService (Legacy)
  slug: nmbrs-soap-debtor-service
- baseURL: https://api.nmbrsapp.com
  baseurl_source: declared
  description: Employee absence, leave, and sickness registrations.
  name: Nmbrs Absences API
  slug: nmbrs-absences-api
- baseURL: https://api.nmbrsapp.com
  baseurl_source: declared
  description: Company (employer) records within a Nmbrs environment.
  name: Nmbrs Companies API
  slug: nmbrs-companies-api
- baseURL: https://api.nmbrsapp.com
  baseurl_source: declared
  description: Employee records and their personal / HR information.
  name: Nmbrs Employees API
  slug: nmbrs-employees-api
- baseURL: https://api.nmbrsapp.com
  baseurl_source: declared
  description: Employment contracts and employment history for an employee.
  name: Nmbrs Employments API
  slug: nmbrs-employments-api
- baseURL: https://api.nmbrsapp.com
  baseurl_source: declared
  description: Payroll runs (payruns) and their results for a company.
  name: Nmbrs Payruns API
  slug: nmbrs-payruns-api
- baseURL: https://api.nmbrsapp.com
  baseurl_source: declared
  description: Salary and wage information for an employee.
  name: Nmbrs Salaries API
  slug: nmbrs-salaries-api
- baseURL: https://api.nmbrsapp.com
  baseurl_source: declared
  description: Fixed and variable wage components used in payroll.
  name: Nmbrs Wage Components API
  slug: nmbrs-wage-components-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nmbrs Public REST API (HR & Payroll) Absences API
  slug: open-nmbrs-absences-api
- collection_type: open
  name: Nmbrs Public REST API (HR & Payroll) Absences Companies API
  slug: open-nmbrs-companies-api
- collection_type: open
  name: Nmbrs Public REST API (HR & Payroll) Absences Employees API
  slug: open-nmbrs-employees-api
- collection_type: open
  name: Nmbrs Public REST API (HR & Payroll) Absences Employments API
  slug: open-nmbrs-employments-api
- collection_type: open
  name: Nmbrs Public REST API (HR & Payroll) Absences Payruns API
  slug: open-nmbrs-payruns-api
- collection_type: open
  name: Nmbrs Public REST API (HR & Payroll) Absences Salaries API
  slug: open-nmbrs-salaries-api
- collection_type: open
  name: Nmbrs Public REST API (HR & Payroll) Absences Wage Components API
  slug: open-nmbrs-wage-components-api
- collection_type: open
  name: Nmbrs Public REST API (HR & Payroll)
  slug: open-nmbrs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nmbrs-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nmbrs-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nmbrs-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nmbrs
- group: company
  title: ''
  type: Website
  url: https://www.nmbrs.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.nmbrs.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://nmbrs.stoplight.io/docs/nmbrs-restapi
- group: start
  title: ''
  type: SignUp
  url: https://developer.nmbrs.com
- group: commercial
  title: ''
  type: Plans
  url: plans/nmbrs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nmbrs-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nmbrs-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.nmbrs.com/blog
created: '2026-07-11'
description: Nmbrs (Visma Nmbrs) is cloud HR and payroll software for the Netherlands and Sweden, widely used by employers, accountants, and payroll service providers. Nmbrs exposes its HRIS and payroll data through a public API in two generations. The current, forward-looking interface is a REST API served from https://api.nmbrsapp.com, authenticated with OAuth 2.0 (Authorization Code flow via identityservice.nmbrs.com) plus a per-product subscription key, with granular scopes over companies, employees, employments, salaries, wage components, payruns, and absences. The older SOAP API (api.nmbrs.nl/soap/v3 - EmployeeService, CompanyService, DebtorService) remains available for existing integrations but is deprecated and scheduled to be retired on 1 March 2027, after which REST is the only supported API.
finops:
- name: Nmbrs Finops
  service_category: HR and Payroll Software
  slug: nmbrs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nmbrs.png
layout: provider
modified: '2026-07-11'
name: Nmbrs
nav: Providers
network: true
overview: 'Nmbrs publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Absences API, Companies API, Employees API, and 4 more. Tagged areas include Human Resources, HRIS, Payroll, Employee Management, and HR.


  Nmbrs'' developer surface includes authentication, documentation, API reference, signup flow, engineering blog, and 7 more developer resources.'
plans:
- name: Nmbrs Plans Pricing
  plan_count: 4
  slug: nmbrs-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Nmbrs Rate Limits
  slug: nmbrs-rate-limits
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 10
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 13.9
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 30.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nmbrs/refs/heads/main/screenshots/nmbrs-2026-08-07T185352.png
security:
- kind: authentication
  name: Nmbrs Authentication
  slug: nmbrs-authentication
  summary_line: oauth2/apiKey/soap-token · 3 schemes
- kind: domain-security
  name: Nmbrs Domain Security
  slug: nmbrs-domain-security
  summary_line: HSTS · DMARC
slug: nmbrs
tags:
- Human Resources
- HRIS
- Payroll
- Employee Management
- HR
- Absence Management
- Netherlands
- Sweden
- SOAP
- REST
website: https://www.nmbrs.com
---

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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.7
  scored_at: '2026-11-06'
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
  description: Salary and wage information for an employee.
  name: Nmbrs Salaries API
  slug: nmbrs-salaries-api
- baseURL: https://api.nmbrsapp.com
  baseurl_source: declared
  description: Fixed and variable wage components used in payroll.
  name: Nmbrs Wage Components API
  slug: nmbrs-wage-components-api
- baseURL: https://api.nmbrs.nl/soap/v3
  baseurl_source: declared
  description: Payroll runs (payruns) and their results for a company.
  name: Nmbrs Pay Runs API
  slug: nmbrs-pay-runs-api
artifact_total: 25
collections:
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
- group: other
  href: https://artifacts.apis.io/nmbrs/capabilities/nmbrs-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/nmbrs-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/nmbrs/agentic-access/nmbrs-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/nmbrs-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/nmbrs/authentication/nmbrs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nmbrs-authentication.yml
- group: auth
  href: https://artifacts.apis.io/nmbrs/security/nmbrs-domain-security.yml
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
  href: https://artifacts.apis.io/nmbrs/plans/nmbrs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nmbrs-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/nmbrs/rate-limits/nmbrs-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/nmbrs-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/nmbrs/finops/nmbrs-finops.yml
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
- has_sources: true
  method: generated
  name: Nmbrs Finops
  primary_unit: ''
  service_category: HR and Payroll Software
  slug: nmbrs-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nmbrs.png
layout: provider
modified: '2026-07-11'
name: Nmbrs
nav: Providers
network: true
overview: 'Nmbrs publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Absences API, Companies API, Employees API, and 7 more. Tagged areas include Human Resources, HRIS, Payroll, Employee Management, and Absence Management.


  The Nmbrs catalog on APIs.io includes 1 Spectral governance ruleset.


  Nmbrs'' developer surface includes authentication, documentation, API reference, signup flow, engineering blog, and 8 more developer resources.'
plans:
- name: Nmbrs Plans Pricing
  plan_count: 4
  slug: nmbrs-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Nmbrs Rate Limits
  slug: nmbrs-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Nmbrs API Rules
  rule_count: 61
  severity_counts:
    error: 59
    hint: 0
    info: 1
    warn: 1
  slug: nmbrs-rules
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 13.6
    contract_quality: 50.2
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
    - nordics
  previous_composite: 30.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/nmbrs/nmbrs-2026-08-07T185352.png
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
- Absence Management
- Netherlands
- Sweden
- SOAP
- REST
website: https://www.nmbrs.com
---

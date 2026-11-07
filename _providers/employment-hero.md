---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Employment Hero Agentic Access
  operation_count: 24
  slug: employment-hero-agentic-access
  summary_line: 24 operations · 9 acting
api_count: 6
apis:
- description: Versioned REST API (v1) for accessing Employment Hero HR, payroll, and employee data including organisations, employees, teams, leave, pay runs, and onboarding. Apps register through the Developer Por
  name: Employment Hero REST API
  slug: rest-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: The Bank Accounts API from Employment Hero — 1 operation(s) for bank accounts.
  name: Employment Hero Bank Accounts API
  slug: employment-hero-bank-accounts-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: The Certifications API from Employment Hero — 5 operation(s) for certifications.
  name: Employment Hero Certifications API
  slug: employment-hero-certifications-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: The Cost Centres API from Employment Hero — 1 operation(s) for cost centres.
  name: Employment Hero Cost Centres API
  slug: employment-hero-cost-centres-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: The Custom Fields API from Employment Hero — 1 operation(s) for custom fields.
  name: Employment Hero Custom Fields API
  slug: employment-hero-custom-fields-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: The Departments API from Employment Hero — 2 operation(s) for departments.
  name: Employment Hero Departments API
  slug: employment-hero-departments-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: The Documents API from Employment Hero — 1 operation(s) for documents.
  name: Employment Hero Documents API
  slug: employment-hero-documents-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: The Emergency Contacts API from Employment Hero — 1 operation(s) for emergency contacts.
  name: Employment Hero Emergency Contacts API
  slug: employment-hero-emergency-contacts-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: The Employees API from Employment Hero — 3 operation(s) for employees.
  name: Employment Hero Employees API
  slug: employment-hero-employees-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: The Forms API from Employment Hero — 4 operation(s) for forms.
  name: Employment Hero Forms API
  slug: employment-hero-forms-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: The Job Histories API from Employment Hero — 1 operation(s) for job histories.
  name: Employment Hero Job Histories API
  slug: employment-hero-job-histories-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: ABA Settings
  name: Employment Hero Aba Settings API
  slug: employment-hero-abasettings-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Authentication
  name: Employment Hero Authentication API
  slug: employment-hero-authentication-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Award
  name: Employment Hero Award API
  slug: employment-hero-award-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Benefit Categories
  name: Employment Hero Benefit Category API
  slug: employment-hero-benefitcategory-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Brand
  name: Employment Hero Brand API
  slug: employment-hero-brand-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Business
  name: Employment Hero Business API
  slug: employment-hero-business-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Contractor
  name: Employment Hero Contractor API
  slug: employment-hero-contractor-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Deduction Categories
  name: Employment Hero Deduction Categories API
  slug: employment-hero-deductioncategories-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Employee
  name: Employment Hero Employee API
  slug: employment-hero-employee-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Employee Access
  name: Employment Hero Employee Access API
  slug: employment-hero-employeeaccess-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Employee Bank Accounts
  name: Employment Hero Employee Bank Account API
  slug: employment-hero-employeebankaccount-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Employee Benefit Categories
  name: Employment Hero Employee Benefit Category API
  slug: employment-hero-employeebenefitcategory-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Employee Benefits In Kind
  name: Employment Hero Employee Benefits In Kind API
  slug: employment-hero-employeebenefitsinkind-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Employee Documents
  name: Employment Hero Employee Document API
  slug: employment-hero-employeedocument-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Employee Earnings Line Split
  name: Employment Hero Employee Earnings Line Split API
  slug: employment-hero-employeeearningslinesplit-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Employee Expense Categories
  name: Employment Hero Employee Expense Categories API
  slug: employment-hero-employeeexpensecategories-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Employee Expense Requests
  name: Employment Hero Employee Expense Request API
  slug: employment-hero-employeeexpenserequest-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Employee Gains Or Profits Employee Share Plan
  name: Employment Hero Employee Gains Or Profits Employee Share Plan API
  slug: employment-hero-employeegainsorprofitsemployeeshareplan-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Employee Groups
  name: Employment Hero Employee Groups API
  slug: employment-hero-employeegroups-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Employee Income From Overseas Subject To Tax Remission
  name: Employment Hero Employee Income From Overseas Subject To Tax Remission API
  slug: employment-hero-employeeincomefromoverseassubjecttotaxremission-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Employee Income Tax Borne By Employer
  name: Employment Hero Employee Income Tax Borne By Employer API
  slug: employment-hero-employeeincometaxbornebyemployer-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Employee Iras Lump Sum
  name: Employment Hero Employee Iras Lump Sum API
  slug: employment-hero-employeeiraslumpsum-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Employee Leave Allowances
  name: Employment Hero Employee Leave Allowances API
  slug: employment-hero-employeeleaveallowances-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Employee Onboarding
  name: Employment Hero Employee Onboarding API
  slug: employment-hero-employeeonboarding-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Employee Pay Rate Schedule
  name: Employment Hero Employee Pay Rate Schedule API
  slug: employment-hero-employeepayrateschedule-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Employee Qualifications
  name: Employment Hero Employee Qualifications API
  slug: employment-hero-employeequalifications-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Pay Run Inclusions
  name: Employment Hero Employee Recurring Transactions API
  slug: employment-hero-employeerecurringtransactions-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Employee Reporting Dimension Earnings Line Split
  name: Employment Hero Employee Reporting Dimension Earnings Line Split API
  slug: employment-hero-employeereportingdimensionearningslinesplit-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Employee Self Managed Super Funds
  name: Employment Hero Employee Self Managed Super Fund API
  slug: employment-hero-employeeselfmanagedsuperfund-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Employee Super Funds
  name: Employment Hero Employee Super Fund API
  slug: employment-hero-employeesuperfund-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Employer Liability Categories
  name: Employment Hero Employer Liability Categories API
  slug: employment-hero-employerliabilitycategories-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Employing Entities
  name: Employment Hero Employing Entities API
  slug: employment-hero-employingentities-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Employment Agreement
  name: Employment Hero Employment Agreement API
  slug: employment-hero-employmentagreement-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Employee Self Setup
  name: Employment Hero Ess API
  slug: employment-hero-ess-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Invoices
  name: Employment Hero Invoices API
  slug: employment-hero-invoices-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Leave Allowances
  name: Employment Hero Leave Allowance API
  slug: employment-hero-leaveallowance-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Leave Categories
  name: Employment Hero Leave Categories API
  slug: employment-hero-leavecategories-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Leave Requests
  name: Employment Hero Leave Requests API
  slug: employment-hero-leaverequests-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Location
  name: Employment Hero Location API
  slug: employment-hero-location-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Lookup Data
  name: Employment Hero Lookup Data API
  slug: employment-hero-lookupdata-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Manager
  name: Employment Hero Manager API
  slug: employment-hero-manager-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: The Other API from Employment Hero — 8 operation(s) for other.
  name: Employment Hero Other API
  slug: employment-hero-other-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Pay Category
  name: Employment Hero Pay Category API
  slug: employment-hero-paycategory-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Pay Condition
  name: Employment Hero Pay Condition API
  slug: employment-hero-paycondition-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Pay Conditions Comparison
  name: Employment Hero Pay Condition Comparison API
  slug: employment-hero-payconditioncomparison-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: PayeScheme
  name: Employment Hero Paye Scheme API
  slug: employment-hero-payescheme-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Payment Summaries
  name: Employment Hero Payment Summary API
  slug: employment-hero-paymentsummary-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Pay Rate Templates
  name: Employment Hero Pay Rate Template API
  slug: employment-hero-payratetemplate-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Pay Run
  name: Employment Hero Pay Run API
  slug: employment-hero-payrun-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Pay Schedules
  name: Employment Hero Pay Schedule API
  slug: employment-hero-payschedule-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Pension Settings
  name: Employment Hero Pension Settings API
  slug: employment-hero-pensionsettings-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Public Holiday
  name: Employment Hero Public Holiday API
  slug: employment-hero-publicholiday-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Qualifications
  name: Employment Hero Qualifications API
  slug: employment-hero-qualifications-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Reporting
  name: Employment Hero Reporting API
  slug: employment-hero-reporting-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Dimensions
  name: Employment Hero Reporting Dimensions API
  slug: employment-hero-reportingdimensions-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Reseller
  name: Employment Hero Reseller API
  slug: employment-hero-reseller-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Roster Shifts
  name: Employment Hero Roster Shift API
  slug: employment-hero-rostershift-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Subcontractor
  name: Employment Hero Subcontractor API
  slug: employment-hero-subcontractor-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Super Funds
  name: Employment Hero Super Fund API
  slug: employment-hero-superfund-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Tiered Leave Allowances
  name: Employment Hero Tiered Leave Allowance API
  slug: employment-hero-tieredleaveallowance-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Time and Attendance
  name: Employment Hero Time And Attendance API
  slug: employment-hero-timeandattendance-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Timesheets
  name: Employment Hero Timesheets API
  slug: employment-hero-timesheets-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Unavailability
  name: Employment Hero Unavailability API
  slug: employment-hero-unavailability-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: User
  name: Employment Hero User API
  slug: employment-hero-user-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Webhook
  name: Employment Hero Webhook API
  slug: employment-hero-webhook-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: White Label
  name: Employment Hero White Label API
  slug: employment-hero-whitelabel-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Work Types
  name: Employment Hero Work Type API
  slug: employment-hero-worktype-api
- baseURL: https://api.employmenthero.com/api/v1
  baseurl_source: declared
  description: Chart of Accounts
  name: Employment Hero Chart Of Accounts API
  slug: employment-hero-chart-of-accounts-api
artifact_total: 102
collections:
- collection_type: open
  name: Employment Hero REST Bank Accounts API
  slug: open-employment-hero-bank-accounts-api
- collection_type: open
  name: Employment Hero REST Bank Accounts Certifications API
  slug: open-employment-hero-certifications-api
- collection_type: open
  name: Employment Hero REST Bank Accounts Cost Centres API
  slug: open-employment-hero-cost-centres-api
- collection_type: open
  name: Employment Hero REST Bank Accounts Custom Fields API
  slug: open-employment-hero-custom-fields-api
- collection_type: open
  name: Employment Hero REST Bank Accounts Departments API
  slug: open-employment-hero-departments-api
- collection_type: open
  name: Employment Hero REST Bank Accounts Documents API
  slug: open-employment-hero-documents-api
- collection_type: open
  name: Employment Hero REST Bank Accounts Emergency Contacts API
  slug: open-employment-hero-emergency-contacts-api
- collection_type: open
  name: Employment Hero REST Bank Accounts Employees API
  slug: open-employment-hero-employees-api
- collection_type: open
  name: Employment Hero REST Bank Accounts Forms API
  slug: open-employment-hero-forms-api
- collection_type: open
  name: Employment Hero REST Bank Accounts Job Histories API
  slug: open-employment-hero-job-histories-api
- collection_type: open
  name: Employment Hero REST API
  slug: open-employment-hero
common:
- group: operate
  href: https://artifacts.apis.io/employment-hero/rate-limits/employment-hero-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/employment-hero-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/employment-hero/plans/employment-hero-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/employment-hero-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/employment-hero/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/employment-hero/data-model/employment-hero-data-model.yml
  title: ''
  type: DataModel
  url: data-model/employment-hero-data-model.yml
- group: design
  href: https://artifacts.apis.io/employment-hero/conventions/employment-hero-conventions.yml
  title: ''
  type: Conventions
  url: conventions/employment-hero-conventions.yml
- group: start
  href: https://artifacts.apis.io/employment-hero/sandbox/employment-hero-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/employment-hero-sandbox.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.google.com/document/d/10JdrewYyHzmB5C9qxqFDr-2Ya5g0cShWwz8ZeEukXnk
- group: operate
  href: https://artifacts.apis.io/employment-hero/lifecycle/employment-hero-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/employment-hero-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/employment-hero/lifecycle/employment-hero-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/employment-hero-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/employment-hero/errors/employment-hero-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/employment-hero-problem-types.yml
- group: design
  href: https://artifacts.apis.io/employment-hero/conformance/employment-hero-conformance.yml
  title: ''
  type: Conformance
  url: conformance/employment-hero-conformance.yml
- group: other
  href: https://artifacts.apis.io/employment-hero/overlays/employment-hero-bank-accounts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/employment-hero-bank-accounts-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/employment-hero/llms/employment-hero-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/employment-hero-llms.txt
- group: auth
  href: https://artifacts.apis.io/employment-hero/well-known/employment-hero-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/employment-hero-security.txt
- group: agent
  href: https://artifacts.apis.io/employment-hero/well-known/employment-hero-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/employment-hero-well-known.yml
- group: other
  href: https://artifacts.apis.io/employment-hero/hosts/employment-hero-hosts.yml
  title: ''
  type: Hosts
  url: hosts/employment-hero-hosts.yml
- group: build
  href: https://artifacts.apis.io/employment-hero/integrations/employment-hero-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/employment-hero-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/employment-hero/vendors/employment-hero-vendors.yml
  title: ''
  type: Vendors
  url: vendors/employment-hero-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://employmenthero.com/work/management/
- group: start
  title: ''
  type: GettingStarted
  url: https://employmenthero.com/solutions/onboarding-software/
- group: other
  href: https://artifacts.apis.io/employment-hero/capabilities/employment-hero-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/employment-hero-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/employment-hero/agentic-access/employment-hero-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/employment-hero-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/employment-hero/security/employment-hero-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/employment-hero-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/employment-hero/security/employment-hero-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/employment-hero-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/employment-hero/authentication/employment-hero-authentication.yml
  title: ''
  type: Authentication
  url: authentication/employment-hero-authentication.yml
- group: auth
  href: https://artifacts.apis.io/employment-hero/scopes/employment-hero-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/employment-hero-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Thinkei
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/employment-hero
- group: company
  title: ''
  type: Website
  url: https://employmenthero.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.employmenthero.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.employmenthero.com/api-references
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.employmenthero.com
- group: commercial
  title: ''
  type: Pricing
  url: https://employmenthero.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://secure.employmenthero.com/users/sign_in
- group: company
  title: ''
  type: Blog
  url: https://employmenthero.com/blog/
- group: company
  title: ''
  type: BlogFeed
  url: https://employmenthero.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://help.employmenthero.com/hc/en-au
- group: operate
  title: ''
  type: Contact
  url: https://employmenthero.com/contact/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.employmenthero.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.employmenthero.com/
- group: company
  title: ''
  type: Newsroom
  url: https://employmenthero.com/news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://employmenthero.com/legals/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://employmenthero.com/legals/privacy-policy
- group: docs
  title: ''
  type: PartnerGuides
  url: https://developer.employmenthero.com/partner-guides
created: '2026-05-11'
description: Employment Hero is an AI-powered Employment Operating System for Australian and international businesses combining HR, payroll, recruitment, onboarding, learning, and employee benefits into a single platform. The product covers policy management, automated workflows, AI-assisted hiring, an employee mobile app, and the HeroForce managed employment service. The Employment Hero API is a versioned REST API authenticated via OAuth 2.0 with short- lived (15-minute) access tokens and refresh tokens.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/employment-hero.png
layout: provider
modified: '2026-10-20'
name: Employment Hero
nav: Providers
network: true
overview: 'Employment Hero publishes 79 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bank Accounts API, Certifications API, Cost Centres API, and 76 more. Tagged areas include Human Resources, HRIS, Payroll, Recruiting, and Employee Benefits.


  The Employment Hero catalog on APIs.io includes 1 Spectral governance ruleset.


  Employment Hero''s developer surface includes sandbox, getting-started guide, authentication, documentation, API reference, pricing, engineering blog, and 37 more developer resources.'
plans:
- name: Employment Hero Plans Pricing
  plan_count: 5
  slug: employment-hero-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Employment Hero Rate Limits
  slug: employment-hero-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Employment Hero API Rules
  rule_count: 62
  severity_counts:
    error: 46
    hint: 0
    info: 5
    warn: 11
  slug: employment-hero-rules
scopes:
- name: Employment Hero Scopes
  scope_count: 2
  slug: employment-hero-scopes
  summary_line: 2 scopes
score:
  band: strong
  composite: 59.4
  coverage:
    artifact_dirs: 32
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.0
  facets:
    access_clarity: 57.9
    contract_governance: 31.8
    contract_quality: 41.7
    developer_ergonomics: 56.5
    discoverability: 80.4
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 69.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 13.0
      derived: 0
      marker_coverage: 0.0
      total: 78
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 38.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/employment-hero/employment-hero-2026-06-20T180642.png
security:
- kind: authentication
  name: Employment Hero Authentication
  slug: employment-hero-authentication
  summary_line: oauth2/http-basic/apiKey · 3 schemes
- kind: domain-security
  name: Employment Hero Domain Security
  slug: employment-hero-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Employment Hero Vulnerability Disclosure
  slug: employment-hero-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: employment-hero-collect-form-responses
  slug: employment-hero-collect-form-responses
- name: employment-hero-employee-profile-lookup
  slug: employment-hero-employee-profile-lookup
- name: employment-hero-manage-certifications
  slug: employment-hero-manage-certifications
- name: employment-hero-onboard-employee
  slug: employment-hero-onboard-employee
slug: employment-hero
tags:
- Human Resources
- HRIS
- Payroll
- Recruiting
- Employee Benefits
- Workforce Management
- Australia
website: https://employmenthero.com
---

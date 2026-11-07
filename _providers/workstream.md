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
    agentic_access: false
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://public-api.workstream.us
  baseurl_source: declared
  description: Applicants represent people who have applied for positions within your company.
  name: Workstream Applicants API
  slug: workstream-applicants-api
- baseURL: https://public-api.workstream.us
  baseurl_source: declared
  description: The Workstream API uses OAuth 2.0 Bearer access tokens to authenticate requests. You can view and manage your access tokens in the [Workstream Dashboard](https://hr.workstream.us/#/company?currentPane
  name: Workstream Authorization API
  slug: workstream-authorization-api
- baseURL: https://public-api.workstream.us
  baseurl_source: declared
  description: Company Roles represent roles within your company.
  name: Workstream Company Roles API
  slug: workstream-company-roles-api
- baseURL: https://public-api.workstream.us
  baseurl_source: declared
  description: Company Users represent people who are system users within your company.
  name: Workstream Company Users API
  slug: workstream-company-users-api
- baseURL: https://public-api.workstream.us
  baseurl_source: declared
  description: Custom field config for location, department, job posting and employee within your company.
  name: Workstream Custom Field API
  slug: workstream-custom-field-api
- baseURL: https://public-api.workstream.us
  baseurl_source: declared
  description: Departments represent departments within your company.
  name: Workstream Departments API
  slug: workstream-departments-api
- baseURL: https://public-api.workstream.us
  baseurl_source: declared
  description: Employee Documents represent documents that are associated with employees within your company.
  name: Workstream Employee Documents API
  slug: workstream-employee-documents-api
- baseURL: https://public-api.workstream.us
  baseurl_source: declared
  description: Employees represent applicants who have been accepted into a new position, or people who are already working for your company.
  name: Workstream Employees API
  slug: workstream-employees-api
- baseURL: https://public-api.workstream.us
  baseurl_source: declared
  description: Imported Employee Infos represent imported employee information that is associated with employees within your company.
  name: Workstream Imported Employee Infos API
  slug: workstream-imported-employee-infos-api
- baseURL: https://public-api.workstream.us
  baseurl_source: declared
  description: Locations represent store locations within your company.
  name: Workstream Locations API
  slug: workstream-locations-api
- baseURL: https://public-api.workstream.us
  baseurl_source: declared
  description: Positions represent open job requisitions within your company that are looking to be filled.
  name: Workstream Positions API
  slug: workstream-positions-api
- baseURL: https://public-api.workstream.us
  baseurl_source: declared
  description: Team Members represent team members that are managed within your company.
  name: Workstream Team Members API
  slug: workstream-team-members-api
artifact_total: 30
collections:
- collection_type: open
  name: Workstream Public Applicants API
  slug: open-workstream-applicants-api
- collection_type: open
  name: Workstream Public Applicants Authorization API
  slug: open-workstream-authorization-api
- collection_type: open
  name: Workstream Public Applicants Company Roles API
  slug: open-workstream-company-roles-api
- collection_type: open
  name: Workstream Public Applicants Company Users API
  slug: open-workstream-company-users-api
- collection_type: open
  name: Workstream Public Applicants Custom Field API
  slug: open-workstream-custom-field-api
- collection_type: open
  name: Workstream Public Applicants Departments API
  slug: open-workstream-departments-api
- collection_type: open
  name: Workstream Public Applicants Employee Documents API
  slug: open-workstream-employee-documents-api
- collection_type: open
  name: Workstream Public Applicants Employees API
  slug: open-workstream-employees-api
- collection_type: open
  name: Workstream Public Applicants Imported Employee Infos API
  slug: open-workstream-imported-employee-infos-api
- collection_type: open
  name: Workstream Public Applicants Locations API
  slug: open-workstream-locations-api
- collection_type: open
  name: Workstream Public Applicants Positions API
  slug: open-workstream-positions-api
- collection_type: open
  name: Workstream Public Applicants Team Members API
  slug: open-workstream-team-members-api
common:
- group: commercial
  href: https://artifacts.apis.io/workstream/plans/workstream-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/workstream-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/workstream/capabilities/workstream-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/workstream-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/workstream/security/workstream-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/workstream-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/workstream/authentication/workstream-authentication.yml
  title: ''
  type: Authentication
  url: authentication/workstream-authentication.yml
- group: auth
  href: https://artifacts.apis.io/workstream/scopes/workstream-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/workstream-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://workstream.us
- group: docs
  title: ''
  type: Documentation
  url: https://docs.workstream.us/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.workstream.us/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.workstream.us/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.workstream.us/en/articles/12278786-set-up-workstream-apis
- group: operate
  title: ''
  type: Support
  url: https://help.workstream.us/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.workstream.us/en/
- group: company
  title: ''
  type: Blog
  url: https://www.workstream.us/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.workstream.us/pricing
- group: start
  title: ''
  type: Login
  url: https://hr.workstream.us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://workstream.us/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workstream.us/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://workstream-status.statuspage.io/
created: '2026-07-17'
description: Workstream is an all-in-one HR, hiring, and payroll platform built for hourly businesses, particularly multi-location restaurants, serving 46 of the top 50 restaurant brands including Taco Bell, Jimmy John's, and Culver's. The platform covers applicant tracking and sourcing, Voice AI screening, onboarding, team management, time and scheduling, compliance, and full-service payroll. Workstream publishes a public REST API (OAuth 2.0 access tokens scoped to positions, applicants, employees, locations, departments, and custom fields) documented at docs.workstream.us.
finops:
- has_sources: true
  method: derived
  name: Workstream Finops
  primary_unit: ''
  service_category: ''
  slug: workstream-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/workstream.png
layout: provider
modified: '2026-07-21'
name: Workstream
nav: Providers
network: true
overview: 'Workstream publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Applicants API, Authorization API, Company Roles API, and 9 more. Tagged areas include Company, Human Resources, Hiring, Payroll, and Onboarding.


  The Workstream catalog on APIs.io includes 1 Spectral governance ruleset.


  Workstream''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Workstream Plans Pricing
  plan_count: 7
  slug: workstream-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 117
  extends:
  - spectral:oas
  name: Workstream API Rules
  rule_count: 76
  severity_counts:
    error: 58
    hint: 0
    info: 7
    warn: 11
  slug: workstream-rules
scopes:
- name: Workstream Scopes
  scope_count: 10
  slug: workstream-scopes
  summary_line: 10 scopes · implicit
score:
  band: developing
  composite: 52.0
  coverage:
    artifact_dirs: 29
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 69.7
    contract_governance: 13.6
    contract_quality: 44.8
    developer_ergonomics: 57.1
    discoverability: 73.2
    operational_transparency: 26.3
  previous_composite: 52.0
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/workstream/workstream-2026-08-17T082948.png
security:
- kind: authentication
  name: Workstream Authentication
  slug: workstream-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Workstream Domain Security
  slug: workstream-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: workstream
tags:
- Company
- Human Resources
- Hiring
- Payroll
- Onboarding
- Applicant Tracking
- Hourly Workforce
- Restaurant
website: https://workstream.us
---

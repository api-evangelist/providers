---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.4
  scored_at: '2026-08-12'
api_count: 12
apis:
- description: Applicants represent people who have applied for positions within your company.
  name: Workstream Applicants API
  slug: workstream-applicants-api
- description: The Workstream API uses OAuth 2.0 Bearer access tokens to authenticate requests. You can view and manage your access tokens in the [Workstream Dashboard](https://hr.workstream.us/#/company?currentPane
  name: Workstream Authorization API
  slug: workstream-authorization-api
- description: Company Roles represent roles within your company.
  name: Workstream Company Roles API
  slug: workstream-company-roles-api
- description: Company Users represent people who are system users within your company.
  name: Workstream Company Users API
  slug: workstream-company-users-api
- description: Custom field config for location, department, job posting and employee within your company.
  name: Workstream Custom Field API
  slug: workstream-custom-field-api
- description: Departments represent departments within your company.
  name: Workstream Departments API
  slug: workstream-departments-api
- description: Employee Documents represent documents that are associated with employees within your company.
  name: Workstream Employee Documents API
  slug: workstream-employee-documents-api
- description: Employees represent applicants who have been accepted into a new position, or people who are already working for your company.
  name: Workstream Employees API
  slug: workstream-employees-api
- description: Imported Employee Infos represent imported employee information that is associated with employees within your company.
  name: Workstream Imported Employee Infos API
  slug: workstream-imported-employee-infos-api
- description: Locations represent store locations within your company.
  name: Workstream Locations API
  slug: workstream-locations-api
- description: Positions represent open job requisitions within your company that are looking to be filled.
  name: Workstream Positions API
  slug: workstream-positions-api
- description: Team Members represent team members that are managed within your company.
  name: Workstream Team Members API
  slug: workstream-team-members-api
artifact_total: 15
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/workstream-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/workstream-authentication.yml
- group: auth
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
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/workstream.png
layout: provider
modified: '2026-07-21'
name: Workstream
nav: Providers
network: true
overview: 'Workstream publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Applicants API, Authorization API, Company Roles API, and 9 more. Tagged areas include Company, Hr Tech, Hiring, Payroll, and Onboarding.


  Workstream''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 9 more developer resources.'
random_paper: 23
scopes:
- name: Workstream Scopes
  scope_count: 10
  slug: workstream-scopes
  summary_line: 10 scopes · implicit
score:
  band: developing
  composite: 43.3
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 54.9
    developer_ergonomics: 52.2
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 43.3
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
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
- Hr Tech
- Hiring
- Payroll
- Onboarding
- Applicant Tracking
- Hourly Workforce
- Restaurants
website: https://workstream.us
---

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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: 7Shifts Agentic Access
  operation_count: 33
  slug: 7shifts-agentic-access
  summary_line: 33 operations · 14 acting
api_count: 15
apis:
- description: Employee availability records.
  name: 7shifts Availability API
  slug: 7shifts-availability-api
- description: Company resources for 7shifts accounts.
  name: 7shifts Companies API
  slug: 7shifts-companies-api
- description: Departments within a location.
  name: 7shifts Departments API
  slug: 7shifts-departments-api
- description: Identity introspection for the authenticated token.
  name: 7shifts Identity API
  slug: 7shifts-identity-api
- description: Physical restaurant locations within a company.
  name: 7shifts Locations API
  slug: 7shifts-locations-api
- description: Token issuance for Partner OAuth applications.
  name: 7shifts OAuth API
  slug: 7shifts-oauth-api
- description: Sales, labor, and worked-hours reporting.
  name: 7shifts Reporting API
  slug: 7shifts-reporting-api
- description: Job roles within a department.
  name: 7shifts Roles API
  slug: 7shifts-roles-api
- description: Sales receipts and POS-integrated sales data.
  name: 7shifts Sales API
  slug: 7shifts-sales-api
- description: Scheduled shifts assigned to users.
  name: 7shifts Shifts API
  slug: 7shifts-shifts-api
- description: Time off requests and approvals.
  name: 7shifts Time Off API
  slug: 7shifts-time-off-api
- description: Clock-in and clock-out time tracking records.
  name: 7shifts Time Punches API
  slug: 7shifts-time-punches-api
- description: Users (employees) scoped to a company.
  name: 7shifts Users API
  slug: 7shifts-users-api
- description: Hourly and salary wage records for users.
  name: 7shifts Wages API
  slug: 7shifts-wages-api
- description: Company-level webhook subscriptions.
  name: 7shifts Webhooks API
  slug: 7shifts-webhooks-api
artifact_total: 63
collections:
- collection_type: open
  name: 7shifts API
  slug: open-7shifts
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/7shifts-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/7shifts-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/7shifts-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/7shifts-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/7shifts-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/7shifts
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/7shifts
- group: company
  title: ''
  type: Website
  url: https://www.7shifts.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.7shifts.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.7shifts.com/reference/introduction
- group: commercial
  title: ''
  type: Pricing
  url: https://www.7shifts.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.7shifts.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.7shifts.com/login
- group: operate
  title: ''
  type: Support
  url: https://support.7shifts.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.7shifts.com/llms.txt
- group: design
  title: ''
  type: Rules
  url: rules/7shifts-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/7shifts-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/7shifts-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/7shifts-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/7shifts-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/7shifts-finops.yml
created: '2026-05-11'
description: 7shifts is a restaurant employee scheduling, time-tracking, and team management platform that helps restaurant operators forecast labor, build schedules, manage shift trades, run payroll integrations, and communicate with hourly staff. The platform integrates with major POS systems for sales data and labor forecasting and supports multi-location operations across quick-service, full-service, and franchise concepts. The 7shifts API v2 is a REST API authenticated via long-lived access tokens (Bearer) for internal use or OAuth 2.0 client credentials for technology partners, exposing employees, schedules, shifts, time punches, departments, locations, and wages.
examples:
- key_count: 7
  name: 7Shifts Availability Example
  slug: 7shifts-availability-example
- key_count: 7
  name: 7Shifts Company Example
  slug: 7shifts-company-example
- key_count: 5
  name: 7Shifts Department Example
  slug: 7shifts-department-example
- key_count: 11
  name: 7Shifts Location Example
  slug: 7shifts-location-example
- key_count: 8
  name: 7Shifts Receipt Example
  slug: 7shifts-receipt-example
- key_count: 8
  name: 7Shifts Role Example
  slug: 7shifts-role-example
- key_count: 15
  name: 7Shifts Shift Example
  slug: 7shifts-shift-example
- key_count: 10
  name: 7Shifts Timeoff Example
  slug: 7shifts-timeoff-example
- key_count: 15
  name: 7Shifts Timepunch Example
  slug: 7shifts-timepunch-example
- key_count: 13
  name: 7Shifts User Example
  slug: 7shifts-user-example
- key_count: 8
  name: 7Shifts Wage Example
  slug: 7shifts-wage-example
- key_count: 6
  name: 7Shifts Webhook Example
  slug: 7shifts-webhook-example
finops:
- name: 7Shifts Finops
  service_category: Workforce Management
  slug: 7shifts-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/7shifts.png
json_schemas:
- name: Availability
  property_count: 7
  slug: 7shifts-availability
- name: Company
  property_count: 7
  slug: 7shifts-company
- name: Department
  property_count: 5
  slug: 7shifts-department
- name: Location
  property_count: 11
  slug: 7shifts-location
- name: Receipt
  property_count: 8
  slug: 7shifts-receipt
- name: Role
  property_count: 8
  slug: 7shifts-role
- name: Shift
  property_count: 15
  slug: 7shifts-shift
- name: Time Off
  property_count: 10
  slug: 7shifts-timeoff
- name: Time Punch
  property_count: 15
  slug: 7shifts-timepunch
- name: User
  property_count: 13
  slug: 7shifts-user
- name: Wage
  property_count: 8
  slug: 7shifts-wage
- name: Webhook
  property_count: 6
  slug: 7shifts-webhook
json_structures:
- name: 7Shifts Availability Structure
  property_count: 7
  slug: 7shifts-availability-structure
- name: 7Shifts Company Structure
  property_count: 7
  slug: 7shifts-company-structure
- name: 7Shifts Department Structure
  property_count: 5
  slug: 7shifts-department-structure
- name: 7Shifts Location Structure
  property_count: 11
  slug: 7shifts-location-structure
- name: 7Shifts Receipt Structure
  property_count: 8
  slug: 7shifts-receipt-structure
- name: 7Shifts Role Structure
  property_count: 8
  slug: 7shifts-role-structure
- name: 7Shifts Shift Structure
  property_count: 15
  slug: 7shifts-shift-structure
- name: 7Shifts Timeoff Structure
  property_count: 10
  slug: 7shifts-timeoff-structure
- name: 7Shifts Timepunch Structure
  property_count: 15
  slug: 7shifts-timepunch-structure
- name: 7Shifts User Structure
  property_count: 13
  slug: 7shifts-user-structure
- name: 7Shifts Wage Structure
  property_count: 8
  slug: 7shifts-wage-structure
- name: 7Shifts Webhook Structure
  property_count: 6
  slug: 7shifts-webhook-structure
jsonld:
- class_count: 33
  name: 7Shifts Context
  property_count: 12
  slug: 7shifts-context
layout: provider
modified: '2026-06-02'
name: 7shifts
nav: Providers
network: true
overview: '7shifts publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Availability API, Companies API, Departments API, and 12 more. Tagged areas include Restaurant, Scheduling, Workforce Management, Employee Scheduling, and Time Tracking.


  The 7shifts catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  7shifts'' developer surface includes authentication, documentation, API reference, pricing, signup flow, support, and 15 more developer resources.'
plans:
- name: 7Shifts Plans Pricing
  plan_count: 4
  slug: 7shifts-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 1
  name: 7Shifts Rate Limits
  slug: 7shifts-rate-limits
rules:
- name: 7shifts API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: 7shifts-jsonschema-spectral-rules
- name: 7shifts API Rules
  rule_count: 41
  severity_counts:
    error: 10
    hint: 0
    info: 10
    warn: 21
  slug: 7shifts-spectral-rules
scopes:
- name: 7Shifts Scopes
  scope_count: 18
  slug: 7shifts-scopes
  summary_line: 18 scopes · clientCredentials
score:
  band: developing
  composite: 54.1
  delta: -4.3
  facets:
    commercial_clarity: 63.2
    contract_quality: 65.0
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 58.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/7shifts/refs/heads/main/screenshots/7shifts-2026-06-20T162818.png
security:
- kind: authentication
  name: 7Shifts Authentication
  slug: 7shifts-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: 7Shifts Domain Security
  slug: 7shifts-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: 7Shifts Vulnerability Disclosure
  slug: 7shifts-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: 7shifts
tags:
- Restaurant
- Scheduling
- Workforce Management
- Employee Scheduling
- Time Tracking
- HRIS
- Labor
website: https://www.7shifts.com
---

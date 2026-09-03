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
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Absence Io Agentic Access
  operation_count: 12
  slug: absence-io-agentic-access
  summary_line: 12 operations · 10 acting
api_count: 7
apis:
- baseURL: https://app.absence.io/api/v2
  baseurl_source: spec
  description: Operations for managing employee absence records.
  name: Absence.io Absences API
  slug: absence-io-absences-api
- baseURL: https://app.absence.io/api/v2
  baseurl_source: spec
  description: Operations for managing employee leave allowances and balances.
  name: Absence.io Allowances API
  slug: absence-io-allowances-api
- baseURL: https://app.absence.io/api/v2
  baseurl_source: spec
  description: Operations for retrieving organizational department information.
  name: Absence.io Departments API
  slug: absence-io-departments-api
- baseURL: https://app.absence.io/api/v2
  baseurl_source: spec
  description: Operations for retrieving office location information.
  name: Absence.io Locations API
  slug: absence-io-locations-api
- baseURL: https://app.absence.io/api/v2
  baseurl_source: spec
  description: Operations for retrieving absence reason type definitions.
  name: Absence.io Reason Types API
  slug: absence-io-reason-types-api
- baseURL: https://app.absence.io/api/v2
  baseurl_source: spec
  description: Operations for retrieving working time configurations.
  name: Absence.io Timespans API
  slug: absence-io-timespans-api
- baseURL: https://app.absence.io/api/v2
  baseurl_source: spec
  description: Operations for retrieving user/employee information.
  name: Absence.io Users API
  slug: absence-io-users-api
artifact_total: 71
collections:
- collection_type: postman
  name: Absence.io Absences API
  slug: postman-absence-io-absences-api
- collection_type: postman
  name: Absence.io Absences Allowances API
  slug: postman-absence-io-allowances-api
- collection_type: postman
  name: Absence.io Absences Departments API
  slug: postman-absence-io-departments-api
- collection_type: postman
  name: Absence.io Absences Locations API
  slug: postman-absence-io-locations-api
- collection_type: postman
  name: Absence.io Absences Reason Types API
  slug: postman-absence-io-reason-types-api
- collection_type: postman
  name: Absence.io Absences Timespans API
  slug: postman-absence-io-timespans-api
- collection_type: postman
  name: Absence.io Absences Users API
  slug: postman-absence-io-users-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Absence.io Absences API
  slug: open-absence-io-absences-api
- collection_type: open
  name: Absence.io Absences Allowances API
  slug: open-absence-io-allowances-api
- collection_type: open
  name: Absence.io Absences Departments API
  slug: open-absence-io-departments-api
- collection_type: open
  name: Absence.io Absences Locations API
  slug: open-absence-io-locations-api
- collection_type: open
  name: Absence.io Absences Reason Types API
  slug: open-absence-io-reason-types-api
- collection_type: open
  name: Absence.io Absences Timespans API
  slug: open-absence-io-timespans-api
- collection_type: open
  name: Absence.io Absences Users API
  slug: open-absence-io-users-api
- collection_type: open
  name: Absence.io API
  slug: open-absence-io
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/absenceio/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/absence-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/absence-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/absence-io-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/absenceio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/absence-io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.absence.io/pricing/pricing-packages/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.absence.io/#authentication
- group: company
  title: ''
  type: Blog
  url: https://blog.absence.io/en/
- group: company
  title: ''
  type: Partners
  url: https://promo.absence.io/partner-program
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.absence.io/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.absence.io/privacy-notice/
- group: design
  title: ''
  type: SpectralRules
  url: rules/absence-io-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/absence-io-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/absence-io-context.jsonld
created: '2025-02-17'
description: Absence.io is an innovative and efficient leave management software that simplifies the process of tracking and managing employee absences. It provides a centralized platform for both employees and managers to easily request, approve, and track time-off requests. Absence.io helps streamline communication and ensure transparency within an organization by providing real-time updates on employee availability and leave balances. The REST API v2 allows integration with absences, users, allowances, departments, locations, reason types, and timespans using Hawk authentication.
examples:
- key_count: 9
  name: Absence Example
  slug: absence-example
- key_count: 8
  name: Allowance Example
  slug: allowance-example
- key_count: 4
  name: Department Example
  slug: department-example
- key_count: 4
  name: Location Example
  slug: location-example
- key_count: 5
  name: Reason Type Example
  slug: reason-type-example
- key_count: 4
  name: Timespan Example
  slug: timespan-example
- key_count: 8
  name: User Example
  slug: user-example
features:
- description: Create, approve, and track employee vacation, sick leave, and other absence types through a centralized platform.
  name: Absence Management
- description: Configure and track annual leave allowances per employee, including carryover management.
  name: Leave Allowances
- description: Configurable approval workflows for absence requests with manager notifications and audit trail.
  name: Approval Workflows
- description: Support for departments, locations, and teams to reflect your organization's hierarchy.
  name: Organizational Structure
- description: Customizable absence reason types (vacation, sick leave, parental leave, etc.) with color coding.
  name: Reason Types
- description: Define timespans with hours per day and days per week for accurate absence calculation.
  name: Working Time Configurations
- description: Full REST API for integrating absence management with ERP, HRIS, and other business systems using Hawk authentication.
  name: REST API v2
finops:
- name: Absence Io Finops
  service_category: API
  slug: absence-io-finops
image: /assets/icons/absence-io.png
integrations:
- description: Integration with Slack for absence request notifications and team visibility.
  name: Slack
- description: Integration with Jira for project planning with awareness of team availability.
  name: Atlassian Jira
- description: Integration with SharePoint for absence calendar sharing and team visibility.
  name: SharePoint
- description: Sync absence records to Google Calendar for team scheduling visibility.
  name: Google Calendar
- description: Integration with Redmine project management for resource planning.
  name: Redmine
json_schemas:
- name: Absence
  property_count: 9
  slug: absence
- name: Allowance
  property_count: 8
  slug: allowance
- name: Department
  property_count: 4
  slug: department
- name: Location
  property_count: 4
  slug: location
- name: ReasonType
  property_count: 5
  slug: reason-type
- name: Timespan
  property_count: 4
  slug: timespan
- name: User
  property_count: 8
  slug: user
json_structures:
- name: Absence Structure
  property_count: 9
  slug: absence-structure
- name: Allowance Structure
  property_count: 8
  slug: allowance-structure
- name: Department Structure
  property_count: 4
  slug: department-structure
- name: Location Structure
  property_count: 4
  slug: location-structure
- name: Reason Type Structure
  property_count: 5
  slug: reason-type-structure
- name: Timespan Structure
  property_count: 4
  slug: timespan-structure
- name: User Structure
  property_count: 8
  slug: user-structure
jsonld:
- class_count: 9
  name: Absence Io Context
  property_count: 28
  slug: absence-io-context
layout: provider
modified: '2026-05-19'
name: Absence.io
nav: Providers
network: true
overview: 'Absence.io publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Absences API, Allowances API, Departments API, and 4 more. Tagged areas include Absences, Employees, Leave Management, and HR.


  The Absence.io catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Absence.io''s developer surface includes authentication, pricing, engineering blog, and 12 more developer resources.'
plans:
- name: Absence Io Plans Pricing
  plan_count: 3
  slug: absence-io-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Absence Io Rate Limits
  slug: absence-io-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Absence.io API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: absence-io-jsonschema-spectral-rules
- effective_rule_count: 77
  extends:
  - spectral:oas
  name: Absence.io API Rules
  rule_count: 36
  severity_counts:
    error: 14
    hint: 0
    info: 6
    warn: 16
  slug: absence-io-spectral-rules
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 17
    catalog_gap: 45.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 28.8
    contract_quality: 30.6
    developer_ergonomics: 29.8
    discoverability: 55.6
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 33.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/absence-io/refs/heads/main/screenshots/absence-io-2026-06-20T163343.png
security:
- kind: authentication
  name: Absence Io Authentication
  slug: absence-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Absence Io Domain Security
  slug: absence-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: absence-io
tags:
- Absences
- Employees
- Leave Management
- HR
use_cases:
- description: Integrate absence data with ERP systems to automatically reflect employee availability and costs.
  name: ERP Integration
- description: Sync employee records between Absence.io and HR information systems to maintain a single source of truth.
  name: HRIS Sync
- description: Use absence and allowance data to calculate accurate payroll deductions and entitlements.
  name: Payroll Processing
- description: Query team absence data to plan project staffing and identify scheduling conflicts.
  name: Capacity Planning
- description: Generate custom reports on absence patterns, allowance usage, and team availability.
  name: Absence Reporting
- description: Pull absence and allowance data into custom HR dashboards and analytics tools.
  name: Custom Dashboards
---

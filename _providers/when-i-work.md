---
access_model:
  confidence: high
  label: Paid (free trial) · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 71
  human_in_the_loop: 0
  name: When I Work Agentic Access
  operation_count: 119
  slug: when-i-work-agentic-access
  summary_line: 119 operations · 71 acting
api_count: 1
apis:
- description: 'Accounts (aka Workplaces) are objects that define a business account with When I Work. Each user is associated with an account enabling them to access Shifts or other data. For more information about '
  name: When I Work Accounts API
  slug: when-i-work-accounts-api
- description: 'Annotations convey important information to all staff for the given schedules (locations) and date range. Any or none of the following tags may apply to an Annotation: * Time Off Not Allowed * Busines'
  name: When I Work Annotations API
  slug: when-i-work-annotations-api
- description: Set your availability preferences to let your employer know when you prefer to work and when you prefer not to work. For more information about using Availabilities, visit the [Help Center](https://he
  name: When I Work Availabilities API
  slug: when-i-work-availabilities-api
- description: 'The import API is used to import a variety of When I Work resources from user-provided CSV or Excel files. ### Import Types All available import types and their columns are listed here. Where possible'
  name: When I Work Import API
  slug: when-i-work-import-api
- description: Shift Bidding, also called “OpenShift Requests”, is an option within an OpenShift that allows employees to express interest in the shift. Management can then view who has requested to pick up the Open
  name: When I Work OpenShift Requests API
  slug: when-i-work-openshift-requests-api
- description: 'Payrolls allows you to select a pay period date range and hours worked within that range. Default range if not supplied is today + 3 days. > Please note that payrolls cannot be created or deleted via '
  name: When I Work Payrolls API
  slug: when-i-work-payrolls-api
- description: Positions (aka, job or duty) are used to define labor allocation. Users can be tagged (associated) with one or more Positions. When I Work uses this association for shift eligibility, Alert notificati
  name: When I Work Positions API
  slug: when-i-work-positions-api
- description: A punch is an event where a user clocks in or clocks out. Punches can be managed to restrict where an employee can clock in/out and from what devices. If a user forgets to clock out, they will be allo
  name: When I Work Punch API
  slug: when-i-work-punch-api
- description: Types of time off that can be selected when submitting a time off request. For more information about using Time Off Requests, visit the [Help Center](https://help.wheniwork.com/articles/requesting-ti
  name: When I Work Request Type API
  slug: when-i-work-request-type-api
- description: Schedule templates allow you to create a daily or weekly schedule that is reusable. If your schedules are very similar from day to day or week to week, use a template to save time and avoid creating s
  name: When I Work Schedule Templates API
  slug: when-i-work-schedule-templates-api
- description: Schedules are logical groupings of users that are working together. Schedules can be physical offices with addresses or logical groups like departments. Users can be tagged (associated) to one or more
  name: When I Work Schedules (Locations) API
  slug: when-i-work-schedules-locations-api
- description: 'When the Attendance setting is enabled to Ask Employees About Paid Rest Breaks the feedback on whether or not breaks were taken is provided here. Note: This endpoint requires the request header for w-'
  name: When I Work Shift Break - Paid Rest API
  slug: when-i-work-shift-break-paid-rest-api
- description: Two types of breaks are provided. First; Scheduled Shift Breaks are break records associated with scheduled shifts. Second; Shift Breaks are break records associated with time worked. For Shift Breaks
  name: When I Work Shift Breaks API
  slug: when-i-work-shift-breaks-api
- description: 'If you’re unable to work one of your shifts, you can give it to one of your coworkers (drop the shift) or trade shifts with one of your coworkers (swap shifts). For more information about using Shift '
  name: When I Work Shift Requests API
  slug: when-i-work-shift-requests-api
- description: 'Shift templates save you time when you need to schedule shifts that have a consistent start and end time. Instead of manually entering in custom shift details one-by-one, shift templates allow you to '
  name: When I Work Shift Templates (Blocks) API
  slug: when-i-work-shift-templates-blocks-api
- description: Shifts provide the basis for scheduling. Many other objects, including Schedules (aka Locations), Positions, Sites, Users, Tasks, and Tags all link through Shifts. For more information about how to us
  name: When I Work Shifts API
  slug: when-i-work-shifts-api
- description: 'Sites communicate additional information about a given shift to the recipient. Typical usage is when you schedule employees for shifts that are at different physical sites (addresses) compared to the '
  name: When I Work Sites API
  slug: when-i-work-sites-api
- description: The Swaps API from When I Work — 1 operation(s) for swaps.
  name: When I Work Swaps API
  slug: when-i-work-swaps-api
- description: When you need to take time off from work, use When I Work to send the request to your manager for approval. Time off can be submitted as unpaid, paid (PTO), sick, or holiday. For more information abou
  name: When I Work Time Off Requests API
  slug: when-i-work-time-off-requests-api
- description: Time records are a listing of the worked hours and can be select by date range. Records are sourced from timeclock terminal, web clock In/Out, mobile clock In/Out, timesheet edits, and API record crea
  name: When I Work Times API
  slug: when-i-work-times-api
- description: Timezones for When I work workplaces including Olson ID
  name: When I Work Timezones API
  slug: when-i-work-timezones-api
- description: A person on the When I Work platform is associated with a two tier record. The persons email/password is associated to a person_id. For each Workplace the person belongs to a user_id record exists. Th
  name: When I Work Users API
  slug: when-i-work-users-api
artifact_total: 63
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: When I Work API Documentation Accounts API
  slug: open-when-i-work-accounts-api
- collection_type: open
  name: When I Work API Documentation Accounts Annotations API
  slug: open-when-i-work-annotations-api
- collection_type: open
  name: When I Work API Documentation Accounts Availabilities API
  slug: open-when-i-work-availabilities-api
- collection_type: open
  name: When I Work API Documentation Accounts Import API
  slug: open-when-i-work-import-api
- collection_type: open
  name: When I Work API Documentation Accounts OpenShift Requests API
  slug: open-when-i-work-openshift-requests-api
- collection_type: open
  name: When I Work API Documentation Accounts Payrolls API
  slug: open-when-i-work-payrolls-api
- collection_type: open
  name: When I Work API Documentation Accounts Positions API
  slug: open-when-i-work-positions-api
- collection_type: open
  name: When I Work API Documentation Accounts Punch API
  slug: open-when-i-work-punch-api
- collection_type: open
  name: When I Work API Documentation Accounts Request Type API
  slug: open-when-i-work-request-type-api
- collection_type: open
  name: When I Work API Documentation Accounts Schedule Templates API
  slug: open-when-i-work-schedule-templates-api
- collection_type: open
  name: When I Work API Documentation Accounts Schedules (Locations) API
  slug: open-when-i-work-schedules-locations-api
- collection_type: open
  name: When I Work API Documentation Accounts Shift Break - Paid Rest API
  slug: open-when-i-work-shift-break-paid-rest-api
- collection_type: open
  name: When I Work API Documentation Accounts Shift Breaks API
  slug: open-when-i-work-shift-breaks-api
- collection_type: open
  name: When I Work API Documentation Accounts Shift Requests API
  slug: open-when-i-work-shift-requests-api
- collection_type: open
  name: When I Work API Documentation Accounts Shift Templates (Blocks) API
  slug: open-when-i-work-shift-templates-blocks-api
- collection_type: open
  name: When I Work API Documentation Accounts Shifts API
  slug: open-when-i-work-shifts-api
- collection_type: open
  name: When I Work API Documentation Accounts Sites API
  slug: open-when-i-work-sites-api
- collection_type: open
  name: When I Work API Documentation Accounts Swaps API
  slug: open-when-i-work-swaps-api
- collection_type: open
  name: When I Work API Documentation Accounts Time Off Requests API
  slug: open-when-i-work-time-off-requests-api
- collection_type: open
  name: When I Work API Documentation Accounts Times API
  slug: open-when-i-work-times-api
- collection_type: open
  name: When I Work API Documentation Accounts Timezones API
  slug: open-when-i-work-timezones-api
- collection_type: open
  name: When I Work API Documentation Accounts Users API
  slug: open-when-i-work-users-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/when-i-work-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/when-i-work-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/when-i-work-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/when-i-work-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://wheniwork.com
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.wheniwork.com/external/index.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wheniwork
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wheniwork
- group: company
  title: ''
  type: Blog
  url: https://wheniwork.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://wheniwork.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.wheniwork.com
- group: other
  title: ''
  type: X
  url: https://x.com/wheniwork
- group: commercial
  title: ''
  type: Plans
  url: plans/when-i-work-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/when-i-work-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/when-i-work-finops.yml
created: 2026-06-12
description: When I Work is an employee scheduling and workforce management platform serving over 200,000 workplaces in industries such as restaurants, retail, healthcare, and hospitality. The platform provides a REST API that enables developers and integration partners to manage shifts, schedules, users, time clock records, attendance, and team communication programmatically. API access is restricted to the Premium plan tier, which also includes webhook support and SAML/SSO capabilities. Authentication follows a token-based model where a private developer key and user credentials are exchanged for a bearer token used in subsequent requests. When I Work also publishes webhooks for real-time event notifications, making it suitable for building payroll, HR, and operations integrations.
examples:
- key_count: 1
  name: When I Work Examples
  slug: when-i-work-examples
finops:
- name: When I Work Finops
  service_category: ''
  slug: when-i-work-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/when-i-work.png
json_schemas:
- name: Position
  property_count: 8
  slug: when-i-work-position
- name: Request
  property_count: 16
  slug: when-i-work-request
- name: Schedule
  property_count: 19
  slug: when-i-work-schedule
- name: Shift
  property_count: 30
  slug: when-i-work-shift
- name: ShiftTemplate
  property_count: 12
  slug: when-i-work-shifttemplate
- name: Site
  property_count: 16
  slug: when-i-work-site
- name: Time
  property_count: 27
  slug: when-i-work-time
- name: User
  property_count: 23
  slug: when-i-work-user
jsonld:
- class_count: 9
  name: When I Work Context
  property_count: 4
  slug: when-i-work-context
layout: provider
modified: 2026-06-12
name: When I Work
nav: Providers
network: true
overview: 'When I Work publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Annotations API, Availabilities API, and 19 more. Tagged areas include Employee Scheduling, Workforce Management, Time Tracking, Time Clock, and Shift Management.


  The When I Work catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  When I Work''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: When I Work Plans Pricing
  plan_count: 3
  slug: when-i-work-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: When I Work Rate Limits
  slug: when-i-work-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: When I Work API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: when-i-work-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.1
  coverage:
    artifact_dirs: 15
    catalog_gap: 51.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 25.0
    contract_quality: 60.4
    developer_ergonomics: 14.3
    discoverability: 44.4
    governance: 25.0
    operational_transparency: 39.5
  previous_composite: 42.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/when-i-work/refs/heads/main/screenshots/when-i-work-2026-06-20T201428.png
security:
- kind: authentication
  name: When I Work Authentication
  slug: when-i-work-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: When I Work Domain Security
  slug: when-i-work-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: When I Work Trust Center
  slug: when-i-work-trust-center
  summary_line: SOC 2
slug: when-i-work
tags:
- Employee Scheduling
- Workforce Management
- Time Tracking
- Time Clock
- Shift Management
- Attendance
- Team Messaging
- Hourly Workers
- Labor Forecasting
- HR
website: https://wheniwork.com
---

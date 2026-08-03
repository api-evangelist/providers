---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 18
  human_in_the_loop: 1
  name: Workday Tracking System Agentic Access
  operation_count: 35
  slug: workday-tracking-system-agentic-access
  summary_line: 35 operations · 18 acting · 1 human-in-the-loop
api_count: 13
apis:
- description: Operations for managing accrual overrides and balances
  name: Workday Tracking System Accruals API
  slug: workday-tracking-system-accruals-api
- description: Operations for managing time off plan balances and overrides
  name: Workday Tracking System Balances API
  slug: workday-tracking-system-balances-api
- description: Operations for managing labor demand data
  name: Workday Tracking System Labor Demand API
  slug: workday-tracking-system-labor-demand-api
- description: Operations for managing leave of absence requests
  name: Workday Tracking System Leave of Absence API
  slug: workday-tracking-system-leave-of-absence-api
- description: Operations for managing scheduling organizations and settings
  name: Workday Tracking System Scheduling Organizations API
  slug: workday-tracking-system-scheduling-organizations-api
- description: Operations for managing schedule shifts
  name: Workday Tracking System Shifts API
  slug: workday-tracking-system-shifts-api
- description: Operations for managing reported and calculated time blocks
  name: Workday Tracking System Time Blocks API
  slug: workday-tracking-system-time-blocks-api
- description: Operations for importing and managing time clock events
  name: Workday Tracking System Time Clock Events API
  slug: workday-tracking-system-time-clock-events-api
- description: Operations for managing employee time off requests
  name: Workday Tracking System Time Off API
  slug: workday-tracking-system-time-off-api
- description: Operations for creating and retrieving time requests
  name: Workday Tracking System Time Requests API
  slug: workday-tracking-system-time-requests-api
- description: Operations for managing employee timesheets
  name: Workday Tracking System Timesheets API
  slug: workday-tracking-system-timesheets-api
- description: Operations for assigning and managing work schedules
  name: Workday Tracking System Work Schedules API
  slug: workday-tracking-system-work-schedules-api
- description: Operations for managing worker scheduling preferences
  name: Workday Tracking System Worker Preferences API
  slug: workday-tracking-system-worker-preferences-api
arazzos:
- description: Read a worker's current work schedule, assign a new schedule, and confirm the assignment took effect.
  name: Workday Assign Work Schedule
  slug: workday-tracking-system-assign-work-schedule-workflow
- description: Ingest a time clock event, poll for the resulting calculated time blocks, then submit the worker's timesheet.
  name: Workday Clock Event to Timesheet Submission
  slug: workday-tracking-system-clock-event-to-timesheet-workflow
- description: Create a scheduling organization, schedule a worker's shift within it, and confirm the shift.
  name: Workday Create Scheduling Organization and Shift
  slug: workday-tracking-system-create-scheduling-org-and-shift-workflow
- description: Request a leave of absence for a worker, verify it appears in the list, and process the return from leave.
  name: Workday Leave of Absence Lifecycle
  slug: workday-tracking-system-leave-of-absence-lifecycle-workflow
- description: Verify a worker has enough time off balance, then submit a time off request and confirm it.
  name: Workday Request Time Off With Balance Check
  slug: workday-tracking-system-request-time-off-with-balance-check-workflow
- description: Read labor demand for an organization, check existing coverage, and schedule a shift only when demand exists.
  name: Workday Staff Against Labor Demand
  slug: workday-tracking-system-staff-against-labor-demand-workflow
- description: Create a reported time block for a worker, fetch it back, and correct it with updated hours.
  name: Workday Time Block Lifecycle
  slug: workday-tracking-system-time-block-lifecycle-workflow
- description: Read a worker's scheduling preferences, update them, and schedule a shift aligned to the preferred times.
  name: Workday Update Scheduling Preferences and Shift
  slug: workday-tracking-system-update-scheduling-preferences-and-shift-workflow
artifact_total: 149
collections:
- collection_type: postman
  name: Workday Absence Management Accruals API
  slug: postman-workday-tracking-system-accruals-api
- collection_type: postman
  name: Workday Absence Management Accruals Balances API
  slug: postman-workday-tracking-system-balances-api
- collection_type: postman
  name: Workday Absence Management Accruals Labor Demand API
  slug: postman-workday-tracking-system-labor-demand-api
- collection_type: postman
  name: Workday Absence Management Accruals Leave of Absence API
  slug: postman-workday-tracking-system-leave-of-absence-api
- collection_type: postman
  name: Workday Absence Management Accruals Scheduling Organizations API
  slug: postman-workday-tracking-system-scheduling-organizations-api
- collection_type: postman
  name: Workday Absence Management Accruals Shifts API
  slug: postman-workday-tracking-system-shifts-api
- collection_type: postman
  name: Workday Absence Management Accruals Time Blocks API
  slug: postman-workday-tracking-system-time-blocks-api
- collection_type: postman
  name: Workday Absence Management Accruals Time Clock Events API
  slug: postman-workday-tracking-system-time-clock-events-api
- collection_type: postman
  name: Workday Absence Management Accruals Time Off API
  slug: postman-workday-tracking-system-time-off-api
- collection_type: postman
  name: Workday Absence Management Accruals Time Requests API
  slug: postman-workday-tracking-system-time-requests-api
- collection_type: postman
  name: Workday Absence Management Accruals Timesheets API
  slug: postman-workday-tracking-system-timesheets-api
- collection_type: postman
  name: Workday Absence Management Accruals Work Schedules API
  slug: postman-workday-tracking-system-work-schedules-api
- collection_type: postman
  name: Workday Absence Management Accruals Worker Preferences API
  slug: postman-workday-tracking-system-worker-preferences-api
- collection_type: open
  name: Workday Absence Management API
  slug: open-workday-tracking-system-absence-management
- collection_type: open
  name: Workday Scheduling API
  slug: open-workday-tracking-system-scheduling
- collection_type: open
  name: Workday Time Tracking API
  slug: open-workday-tracking-system-time-tracking
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/workday-tracking-system/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/workday-tracking-system-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/workday-tracking-system-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/workday-tracking-system-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/workday-tracking-system-authentication.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-tracking-system-assign-work-schedule-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-tracking-system-clock-event-to-timesheet-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-tracking-system-create-scheduling-org-and-shift-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-tracking-system-leave-of-absence-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-tracking-system-request-time-off-with-balance-check-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-tracking-system-staff-against-labor-demand-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-tracking-system-time-block-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-tracking-system-update-scheduling-preferences-and-shift-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.workday.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.workday.com/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.workday.com
- group: auth
  title: ''
  type: Authentication
  url: https://docs.workday.com/authentication/oauth2
- group: start
  title: ''
  type: Signup
  url: https://www.workday.com/en-us/forms/contact-sales.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.workday.com/en-us/pricing.html
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.workday.com/rate-limits
- group: operate
  title: ''
  type: StatusPage
  url: https://status.workday.com
- group: operate
  title: ''
  type: Support
  url: https://www.workday.com/en-us/company/latest/customer-support.html
- group: operate
  title: ''
  type: Community
  url: https://community.workday.com
- group: company
  title: ''
  type: Blog
  url: https://blog.workday.com
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.workday.com/release-notes
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workday.com/en-us/terms-of-service.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workday.com/en-us/privacy.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Workday
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/workday-tracking-system/refs/heads/main/json-ld/workday-tracking-system-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/workday-tracking-system/refs/heads/main/json-schema/workday-tracking-system-leave-of-absence-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/workday-tracking-system/refs/heads/main/json-schema/workday-tracking-system-time-block-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/workday-tracking-system/refs/heads/main/json-schema/workday-tracking-system-timesheet-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/workday-tracking-system/refs/heads/main/json-structure/workday-tracking-system-leave-of-absence-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/workday-tracking-system/refs/heads/main/json-structure/workday-tracking-system-time-block-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/workday-tracking-system/refs/heads/main/json-structure/workday-tracking-system-timesheet-structure.json
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/workday-tracking-system/refs/heads/main/rules/workday-tracking-system-spectral-rules.yml
created: '2024-01-15'
description: APIs for managing employee time tracking, absence management, and workforce scheduling in the Workday platform. Covers time blocks, time clock events, timesheets, time off, leaves of absence, accruals, schedule shifts, scheduling organizations, labor demand, and worker scheduling preferences.
features:
- description: Capture, calculate, and report worker time blocks with batch import support for high-volume time entry workflows.
  name: Time Block Management
- description: Import time clock events from third-party clocks and devices into Workday for centralized time tracking.
  name: Time Clock Integration
- description: Retrieve, submit, approve, and report on timesheets covering configurable pay periods.
  name: Timesheet Lifecycle
- description: Enter time off entries, request leaves of absence, and process return-from-leave events through the Absence Management API.
  name: Time Off and Leave
- description: Inspect time off balances and apply accrual overrides to align worker plan balances with payroll requirements.
  name: Accrual Balances and Overrides
- description: Create, update, and import schedule shifts and assign them to workers within scheduling organizations.
  name: Schedule Shift Management
- description: Configure labor demand by scheduling organization to drive shift creation and workforce planning.
  name: Labor Demand Planning
- description: Capture worker availability and scheduling preferences to inform shift assignment decisions.
  name: Worker Scheduling Preferences
finops:
- name: Workday Tracking System Finops
  service_category: HR / Workforce SaaS
  slug: workday-tracking-system-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/workday-tracking-system.png
integrations:
- description: Calculated time blocks and approved timesheets feed Workday Payroll for gross-to-net processing.
  name: Workday Payroll
- description: Worker, organization, and position data from Workday HCM are referenced across time, absence, and scheduling APIs.
  name: Workday HCM
- description: Third-party time clock vendors integrate with the Time Tracking API via the time clock events endpoints.
  name: Time Clock Hardware
- description: Scheduling and labor optimization partners exchange shifts, labor demand, and preferences with the Scheduling API.
  name: Workforce Management Partners
- description: OAuth 2.0 integration with enterprise identity providers authenticates API clients and workers.
  name: Identity Providers
json_schemas:
- name: AccrualOverrideInput
  property_count: 6
  slug: absence-management-accrual-override-input
- name: AccrualOverride
  property_count: 8
  slug: absence-management-accrual-override
- name: AccrualOverridesResponse
  property_count: 2
  slug: absence-management-accrual-overrides-response
- name: LeaveOfAbsenceInput
  property_count: 5
  slug: absence-management-leave-of-absence-input
- name: LeaveOfAbsence
  property_count: 9
  slug: absence-management-leave-of-absence
- name: LeavesOfAbsenceResponse
  property_count: 2
  slug: absence-management-leaves-of-absence-response
- name: ReturnFromLeaveInput
  property_count: 2
  slug: absence-management-return-from-leave-input
- name: TimeOffBalance
  property_count: 8
  slug: absence-management-time-off-balance
- name: TimeOffBalancesResponse
  property_count: 2
  slug: absence-management-time-off-balances-response
- name: TimeOffEntry
  property_count: 11
  slug: absence-management-time-off-entry
- name: TimeOffInput
  property_count: 4
  slug: absence-management-time-off-input
- name: TimeOffResponse
  property_count: 4
  slug: absence-management-time-off-response
- name: LaborDemandInput
  property_count: 5
  slug: scheduling-labor-demand-input
- name: LaborDemandResponse
  property_count: 2
  slug: scheduling-labor-demand-response
- name: LaborDemand
  property_count: 7
  slug: scheduling-labor-demand
- name: ScheduleShiftInput
  property_count: 7
  slug: scheduling-schedule-shift-input
- name: ScheduleShift
  property_count: 10
  slug: scheduling-schedule-shift
- name: ScheduleShiftsResponse
  property_count: 4
  slug: scheduling-schedule-shifts-response
- name: SchedulingOrganizationInput
  property_count: 4
  slug: scheduling-scheduling-organization-input
- name: SchedulingOrganization
  property_count: 6
  slug: scheduling-scheduling-organization
- name: SchedulingOrganizationsResponse
  property_count: 4
  slug: scheduling-scheduling-organizations-response
- name: WorkerSchedulingPreferencesInput
  property_count: 5
  slug: scheduling-worker-scheduling-preferences-input
- name: WorkerSchedulingPreferences
  property_count: 7
  slug: scheduling-worker-scheduling-preferences
- name: Shift
  property_count: 4
  slug: time-tracking-shift
- name: TimeBlockInput
  property_count: 8
  slug: time-tracking-time-block-input
- name: TimeBlock
  property_count: 13
  slug: time-tracking-time-block
- name: TimeBlocksResponse
  property_count: 4
  slug: time-tracking-time-blocks-response
- name: TimeClockEventInput
  property_count: 4
  slug: time-tracking-time-clock-event-input
- name: TimeClockEvent
  property_count: 7
  slug: time-tracking-time-clock-event
- name: TimeClockEventsResponse
  property_count: 2
  slug: time-tracking-time-clock-events-response
- name: TimeRequestInput
  property_count: 3
  slug: time-tracking-time-request-input
- name: TimeRequest
  property_count: 8
  slug: time-tracking-time-request
- name: TimeRequestsResponse
  property_count: 2
  slug: time-tracking-time-requests-response
- name: Timesheet
  property_count: 9
  slug: time-tracking-timesheet
- name: TimesheetsResponse
  property_count: 2
  slug: time-tracking-timesheets-response
- name: WorkScheduleAssignment
  property_count: 3
  slug: time-tracking-work-schedule-assignment
- name: WorkSchedule
  property_count: 8
  slug: time-tracking-work-schedule
- name: LeaveOfAbsence
  property_count: 9
  slug: workday-tracking-system-leave-of-absence
- name: TimeBlock
  property_count: 13
  slug: workday-tracking-system-time-block
- name: Timesheet
  property_count: 9
  slug: workday-tracking-system-timesheet
json_structures:
- name: Absence Management Accrual Override Input Structure
  property_count: 6
  slug: absence-management-accrual-override-input-structure
- name: Absence Management Accrual Override Structure
  property_count: 8
  slug: absence-management-accrual-override-structure
- name: Absence Management Accrual Overrides Response Structure
  property_count: 2
  slug: absence-management-accrual-overrides-response-structure
- name: Absence Management Leave Of Absence Input Structure
  property_count: 5
  slug: absence-management-leave-of-absence-input-structure
- name: Absence Management Leave Of Absence Structure
  property_count: 9
  slug: absence-management-leave-of-absence-structure
- name: Absence Management Leaves Of Absence Response Structure
  property_count: 2
  slug: absence-management-leaves-of-absence-response-structure
- name: Absence Management Return From Leave Input Structure
  property_count: 2
  slug: absence-management-return-from-leave-input-structure
- name: Absence Management Time Off Balance Structure
  property_count: 8
  slug: absence-management-time-off-balance-structure
- name: Absence Management Time Off Balances Response Structure
  property_count: 2
  slug: absence-management-time-off-balances-response-structure
- name: Absence Management Time Off Entry Structure
  property_count: 11
  slug: absence-management-time-off-entry-structure
- name: Absence Management Time Off Input Structure
  property_count: 4
  slug: absence-management-time-off-input-structure
- name: Absence Management Time Off Response Structure
  property_count: 4
  slug: absence-management-time-off-response-structure
- name: Scheduling Labor Demand Input Structure
  property_count: 5
  slug: scheduling-labor-demand-input-structure
- name: Scheduling Labor Demand Response Structure
  property_count: 2
  slug: scheduling-labor-demand-response-structure
- name: Scheduling Labor Demand Structure
  property_count: 7
  slug: scheduling-labor-demand-structure
- name: Scheduling Schedule Shift Input Structure
  property_count: 7
  slug: scheduling-schedule-shift-input-structure
- name: Scheduling Schedule Shift Structure
  property_count: 10
  slug: scheduling-schedule-shift-structure
- name: Scheduling Schedule Shifts Response Structure
  property_count: 4
  slug: scheduling-schedule-shifts-response-structure
- name: Scheduling Scheduling Organization Input Structure
  property_count: 4
  slug: scheduling-scheduling-organization-input-structure
- name: Scheduling Scheduling Organization Structure
  property_count: 6
  slug: scheduling-scheduling-organization-structure
- name: Scheduling Scheduling Organizations Response Structure
  property_count: 4
  slug: scheduling-scheduling-organizations-response-structure
- name: Scheduling Worker Scheduling Preferences Input Structure
  property_count: 5
  slug: scheduling-worker-scheduling-preferences-input-structure
- name: Scheduling Worker Scheduling Preferences Structure
  property_count: 7
  slug: scheduling-worker-scheduling-preferences-structure
- name: Time Tracking Shift Structure
  property_count: 4
  slug: time-tracking-shift-structure
- name: Time Tracking Time Block Input Structure
  property_count: 8
  slug: time-tracking-time-block-input-structure
- name: Time Tracking Time Block Structure
  property_count: 13
  slug: time-tracking-time-block-structure
- name: Time Tracking Time Blocks Response Structure
  property_count: 4
  slug: time-tracking-time-blocks-response-structure
- name: Time Tracking Time Clock Event Input Structure
  property_count: 4
  slug: time-tracking-time-clock-event-input-structure
- name: Time Tracking Time Clock Event Structure
  property_count: 7
  slug: time-tracking-time-clock-event-structure
- name: Time Tracking Time Clock Events Response Structure
  property_count: 2
  slug: time-tracking-time-clock-events-response-structure
- name: Time Tracking Time Request Input Structure
  property_count: 3
  slug: time-tracking-time-request-input-structure
- name: Time Tracking Time Request Structure
  property_count: 8
  slug: time-tracking-time-request-structure
- name: Time Tracking Time Requests Response Structure
  property_count: 2
  slug: time-tracking-time-requests-response-structure
- name: Time Tracking Timesheet Structure
  property_count: 9
  slug: time-tracking-timesheet-structure
- name: Time Tracking Timesheets Response Structure
  property_count: 2
  slug: time-tracking-timesheets-response-structure
- name: Time Tracking Work Schedule Assignment Structure
  property_count: 3
  slug: time-tracking-work-schedule-assignment-structure
- name: Time Tracking Work Schedule Structure
  property_count: 8
  slug: time-tracking-work-schedule-structure
- name: Workday Tracking System Leave Of Absence Structure
  property_count: 9
  slug: workday-tracking-system-leave-of-absence-structure
- name: Workday Tracking System Time Block Structure
  property_count: 13
  slug: workday-tracking-system-time-block-structure
- name: Workday Tracking System Timesheet Structure
  property_count: 9
  slug: workday-tracking-system-timesheet-structure
jsonld:
- class_count: 1
  name: Workday Tracking System Context
  property_count: 36
  slug: workday-tracking-system-context
layout: provider
modified: '2026-05-19'
name: Workday Tracking System
nav: Providers
network: true
overview: 'Workday Tracking System publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Accruals API, Balances API, Labor Demand API, and 10 more. Tagged areas include Absence Management, Attendance, Enterprise, HCM, and Human Capital Management.


  The Workday Tracking System catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Workday Tracking System''s developer surface includes authentication, developer portal, getting-started guide, documentation, signup flow, pricing, support, and 29 more developer resources.'
plans:
- name: Workday Tracking System Plans Pricing
  plan_count: 1
  slug: workday-tracking-system-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Workday Tracking System Rate Limits
  slug: workday-tracking-system-rate-limits
rules:
- name: Workday Tracking System API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: workday-tracking-system-jsonschema-spectral-rules
- name: Workday Tracking System API Rules
  rule_count: 74
  severity_counts:
    error: 18
    hint: 0
    info: 12
    warn: 44
  slug: workday-tracking-system-spectral-rules
score:
  band: developing
  composite: 52.5
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 29.8
    developer_ergonomics: 50.0
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 57.9
  previous_composite: 52.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 13
      marker_coverage: 100.0
      total: 13
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/workday-tracking-system/refs/heads/main/screenshots/workday-tracking-system-2026-06-20T201611.png
security:
- kind: authentication
  name: Workday Tracking System Authentication
  slug: workday-tracking-system-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Workday Tracking System Domain Security
  slug: workday-tracking-system-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Workday Tracking System Trust Center
  slug: workday-tracking-system-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR
slug: workday-tracking-system
solutions:
- description: Core HCM suite that includes Time Tracking, Absence Management, and Scheduling as integrated workforce capabilities.
  name: Workday Human Capital Management
- description: Native payroll solution that consumes time and absence data for accurate pay calculation.
  name: Workday Payroll
- description: Scheduling, labor optimization, and time tracking solution tailored to shift-based workforces.
  name: Workday Workforce Management
tags:
- Absence Management
- Attendance
- Enterprise
- HCM
- Human Capital Management
- Payroll
- Scheduling
- Time Tracking
- Timesheets
- Workforce Management
use_cases:
- description: Aggregate calculated time blocks and approved timesheets to feed downstream payroll runs.
  name: Payroll Time Capture
- description: Push punch-in and punch-out events from physical or mobile time clocks into Workday in near real time.
  name: Time Clock Device Integration
- description: Manage employee time off requests and leave of absence cases across HR, payroll, and benefits.
  name: Absence and Leave Tracking
- description: Plan and publish weekly shift schedules across scheduling organizations based on labor demand.
  name: Workforce Scheduling
- description: Produce auditable records of worked hours, breaks, and leaves for labor law and contractual compliance.
  name: Compliance Reporting
- description: Apply targeted accrual overrides to correct worker balances following payroll or eligibility changes.
  name: Accrual Adjustment Workflows
website: https://developer.workday.com
---

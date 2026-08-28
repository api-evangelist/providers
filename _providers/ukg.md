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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Ukg Agentic Access
  operation_count: 18
  slug: ukg-agentic-access
  summary_line: 18 operations · 2 acting
api_count: 9
apis:
- description: 'The UKG HR Service Delivery API (formerly People Doc) provides access to employee request management, knowledge portal content, process automation, document storage, and compliance workflows. Enables '
  name: UKG HR Service Delivery API
  slug: ukg-hr-service-delivery-api
- description: Accrual balances and transactions
  name: UKG Accruals API
  slug: ukg-accruals-api
- description: Benefits enrollment and plan information
  name: UKG Benefits API
  slug: ukg-benefits-api
- description: Employee records and demographic data
  name: UKG Employees API
  slug: ukg-employees-api
- description: Departments, locations, and cost centers
  name: UKG Organization API
  slug: ukg-organization-api
- description: Payroll data and check history
  name: UKG Payroll API
  slug: ukg-payroll-api
- description: Job changes, status changes, and employment actions
  name: UKG Personnel Actions API
  slug: ukg-personnel-actions-api
- description: Shifts, schedules, and schedule management
  name: UKG Scheduling API
  slug: ukg-scheduling-api
- description: Punches, time entries, and timecards
  name: UKG Timekeeping API
  slug: ukg-timekeeping-api
arazzos:
- description: Locate an employee and audit their active benefits elections.
  name: UKG Pro HCM Benefits Enrollment Audit
  slug: ukg-benefits-enrollment-audit-workflow
- description: Resolve a WFM employee, submit a clock punch, and verify it landed.
  name: UKG Pro WFM Clock In and Verify
  slug: ukg-clock-in-and-verify-workflow
- description: Match an HCM employee record against the WFM roster for the same person.
  name: UKG Cross-System Employee Reconcile
  slug: ukg-cross-system-employee-reconcile-workflow
- description: Compare a day's scheduled shifts to actual punches for an employee.
  name: UKG Pro WFM Daily Attendance Reconcile
  slug: ukg-daily-attendance-reconcile-workflow
- description: Resolve an employee from the directory and assemble their core HCM profile.
  name: UKG Pro HCM Employee 360 Profile
  slug: ukg-employee-360-profile-workflow
- description: Page the employee ID list, then hydrate one employee into a full record.
  name: UKG Pro HCM Employee Roster Bootstrap
  slug: ukg-employee-roster-bootstrap-workflow
- description: Validate org references then submit a department transfer for an employee.
  name: UKG Pro HCM New Hire Org Placement
  slug: ukg-new-hire-org-placement-workflow
- description: Assemble an employee's pay rate, statement history, and deposit accounts.
  name: UKG Pro HCM Payroll Statement Review
  slug: ukg-payroll-statement-review-workflow
- description: Read an employee's accrual balances and branch on available PTO.
  name: UKG Pro WFM PTO Balance and Schedule Check
  slug: ukg-pto-balance-and-schedule-workflow
- description: Pull a location schedule, drill into one employee, and check their accruals.
  name: UKG Pro WFM Schedule Coverage Check
  slug: ukg-schedule-coverage-check-workflow
- description: Validate an employee, submit a personnel action, and branch on its status.
  name: UKG Pro HCM Submit Personnel Change
  slug: ukg-submit-personnel-change-workflow
- description: Resolve an employee, pull their timecards, and branch on approval status.
  name: UKG Pro WFM Timecard Period Review
  slug: ukg-timecard-period-review-workflow
artifact_total: 122
collections:
- collection_type: postman
  name: UKG Pro HCM API
  slug: postman-ukg-pro-hcm
- collection_type: postman
  name: UKG Pro Workforce Management API
  slug: postman-ukg-pro-wfm
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: UKG Pro HCM Accruals API
  slug: open-ukg-accruals-api
- collection_type: open
  name: UKG Pro HCM Accruals Benefits API
  slug: open-ukg-benefits-api
- collection_type: open
  name: UKG Pro HCM Accruals Employees API
  slug: open-ukg-employees-api
- collection_type: open
  name: UKG Pro HCM Accruals Organization API
  slug: open-ukg-organization-api
- collection_type: open
  name: UKG Pro HCM Accruals Payroll API
  slug: open-ukg-payroll-api
- collection_type: open
  name: UKG Pro HCM Accruals Personnel Actions API
  slug: open-ukg-personnel-actions-api
- collection_type: open
  name: UKG Pro HCM API
  slug: open-ukg-pro-hcm
- collection_type: open
  name: UKG Pro Workforce Management API
  slug: open-ukg-pro-wfm
- collection_type: open
  name: UKG Pro HCM Accruals Scheduling API
  slug: open-ukg-scheduling-api
- collection_type: open
  name: UKG Pro HCM Accruals Timekeeping API
  slug: open-ukg-timekeeping-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ukg-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ukg-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ukg-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/ukg/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ukg-benefits-enrollment-audit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ukg-clock-in-and-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ukg-cross-system-employee-reconcile-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ukg-daily-attendance-reconcile-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ukg-employee-360-profile-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ukg-employee-roster-bootstrap-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ukg-new-hire-org-placement-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ukg-payroll-statement-review-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ukg-pto-balance-and-schedule-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ukg-schedule-coverage-check-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ukg-submit-personnel-change-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ukg-timecard-period-review-workflow.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ultimatesoftware
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ukg
- group: company
  title: ''
  type: Website
  url: https://www.ukg.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ukg.com
- group: start
  title: ''
  type: Portal
  url: https://developer.ukg.com
- group: company
  title: ''
  type: Blog
  url: https://www.ukg.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ukg.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ukg.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ukg.com/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://support.ukg.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.ukg.com/general/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developer.ukg.com/hcm/docs/authentication
- group: start
  title: ''
  type: Signup
  url: https://www.ukg.com/contact-us
- group: design
  title: ''
  type: SpectralRules
  url: rules/ukg-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ukg-vocabulary.yaml
created: '2025-02-08'
description: UKG (Ultimate Kronos Group) is an enterprise human capital management (HCM) and workforce management platform serving over 80,000 organizations worldwide. The UKG Pro suite includes HCM APIs for employee data, payroll, benefits, and personnel actions, plus WFM APIs for time and labor management, scheduling, accruals, and attendance. The UKG Developer Hub provides REST APIs, webhook subscriptions, and People Fabric APIs for building HR integrations, payroll connectors, and workforce analytics applications.
examples:
- key_count: 8
  name: Pro Hcm Benefits Election Example
  slug: pro-hcm-benefits-election-example
- key_count: 5
  name: Pro Hcm Department Example
  slug: pro-hcm-department-example
- key_count: 6
  name: Pro Hcm Direct Deposit Example
  slug: pro-hcm-direct-deposit-example
- key_count: 10
  name: Pro Hcm Employee Example
  slug: pro-hcm-employee-example
- key_count: 3
  name: Pro Hcm Employee Id List Example
  slug: pro-hcm-employee-id-list-example
- key_count: 8
  name: Pro Hcm Employee Job Example
  slug: pro-hcm-employee-job-example
- key_count: 3
  name: Pro Hcm Employee List Example
  slug: pro-hcm-employee-list-example
- key_count: 7
  name: Pro Hcm Location Example
  slug: pro-hcm-location-example
- key_count: 6
  name: Pro Hcm Pay Rate Example
  slug: pro-hcm-pay-rate-example
- key_count: 12
  name: Pro Hcm Pay Statement Example
  slug: pro-hcm-pay-statement-example
- key_count: 7
  name: Pro Hcm Personnel Change Request Example
  slug: pro-hcm-personnel-change-request-example
- key_count: 3
  name: Pro Hcm Personnel Change Response Example
  slug: pro-hcm-personnel-change-response-example
- key_count: 6
  name: Pro Wfm Accrual Balance Example
  slug: pro-wfm-accrual-balance-example
- key_count: 6
  name: Pro Wfm Punch Example
  slug: pro-wfm-punch-example
- key_count: 4
  name: Pro Wfm Punch Request Example
  slug: pro-wfm-punch-request-example
- key_count: 9
  name: Pro Wfm Shift Example
  slug: pro-wfm-shift-example
- key_count: 8
  name: Pro Wfm Timecard Example
  slug: pro-wfm-timecard-example
- key_count: 8
  name: Pro Wfm Wfm Employee Example
  slug: pro-wfm-wfm-employee-example
features:
- description: Comprehensive HCM covering employee records, org management, talent, and compliance for enterprise organizations.
  name: Human Capital Management
- description: Full-service payroll with tax compliance, direct deposit, pay statements, and multi-state support.
  name: Payroll Processing
- description: Benefits enrollment, plan management, life event processing, and ACA compliance tracking.
  name: Benefits Administration
- description: Automated timekeeping with punch clocks, mobile entry, approval workflows, and FLSA compliance.
  name: Time and Attendance
- description: AI-powered scheduling with demand forecasting, shift management, and coverage optimization.
  name: Workforce Scheduling
- description: Configurable vacation, sick, and PTO accrual policies with automated balance tracking.
  name: Accrual Management
- description: Employee case management, knowledge portal, HR document management, and process automation.
  name: HR Service Delivery
- description: Unified data platform connecting HCM and WFM data across all UKG products via modern APIs.
  name: People Fabric
finops:
- name: Ukg Finops
  service_category: HCM / Workforce Management
  slug: ukg-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ukg.png
integrations:
- description: Sync employee data between UKG and Salesforce for HR-CRM alignment.
  name: Salesforce
- description: Integrate with SAP ERP for GL posting, cost center management, and financial reconciliation.
  name: SAP
- description: Single sign-on and user provisioning integration with Microsoft Entra ID.
  name: Microsoft Azure AD
- description: Employee data exchange for organizations using both platforms during migration or hybrid scenarios.
  name: Workday
- description: Payroll data exchange with ADP for organizations using both HCM and payroll platforms.
  name: ADP
- description: Applicant tracking system integration for recruiting and onboarding handoff.
  name: Greenhouse
json_schemas:
- name: BenefitsElection
  property_count: 8
  slug: pro-hcm-benefits-election
- name: Department
  property_count: 5
  slug: pro-hcm-department
- name: DirectDeposit
  property_count: 6
  slug: pro-hcm-direct-deposit
- name: EmployeeIdList
  property_count: 3
  slug: pro-hcm-employee-id-list
- name: EmployeeJob
  property_count: 8
  slug: pro-hcm-employee-job
- name: EmployeeList
  property_count: 3
  slug: pro-hcm-employee-list
- name: Employee
  property_count: 10
  slug: pro-hcm-employee
- name: Location
  property_count: 7
  slug: pro-hcm-location
- name: PayRate
  property_count: 6
  slug: pro-hcm-pay-rate
- name: PayStatement
  property_count: 12
  slug: pro-hcm-pay-statement
- name: PersonnelChangeRequest
  property_count: 7
  slug: pro-hcm-personnel-change-request
- name: PersonnelChangeResponse
  property_count: 3
  slug: pro-hcm-personnel-change-response
- name: AccrualBalance
  property_count: 6
  slug: pro-wfm-accrual-balance
- name: PunchRequest
  property_count: 4
  slug: pro-wfm-punch-request
- name: Punch
  property_count: 6
  slug: pro-wfm-punch
- name: Shift
  property_count: 9
  slug: pro-wfm-shift
- name: Timecard
  property_count: 8
  slug: pro-wfm-timecard
- name: WfmEmployee
  property_count: 8
  slug: pro-wfm-wfm-employee
json_structures:
- name: Pro Hcm Benefits Election Structure
  property_count: 8
  slug: pro-hcm-benefits-election-structure
- name: Pro Hcm Department Structure
  property_count: 5
  slug: pro-hcm-department-structure
- name: Pro Hcm Direct Deposit Structure
  property_count: 6
  slug: pro-hcm-direct-deposit-structure
- name: Pro Hcm Employee Id List Structure
  property_count: 3
  slug: pro-hcm-employee-id-list-structure
- name: Pro Hcm Employee Job Structure
  property_count: 8
  slug: pro-hcm-employee-job-structure
- name: Pro Hcm Employee List Structure
  property_count: 3
  slug: pro-hcm-employee-list-structure
- name: Pro Hcm Employee Structure
  property_count: 10
  slug: pro-hcm-employee-structure
- name: Pro Hcm Location Structure
  property_count: 7
  slug: pro-hcm-location-structure
- name: Pro Hcm Pay Rate Structure
  property_count: 6
  slug: pro-hcm-pay-rate-structure
- name: Pro Hcm Pay Statement Structure
  property_count: 12
  slug: pro-hcm-pay-statement-structure
- name: Pro Hcm Personnel Change Request Structure
  property_count: 7
  slug: pro-hcm-personnel-change-request-structure
- name: Pro Hcm Personnel Change Response Structure
  property_count: 3
  slug: pro-hcm-personnel-change-response-structure
- name: Pro Wfm Accrual Balance Structure
  property_count: 6
  slug: pro-wfm-accrual-balance-structure
- name: Pro Wfm Punch Request Structure
  property_count: 4
  slug: pro-wfm-punch-request-structure
- name: Pro Wfm Punch Structure
  property_count: 6
  slug: pro-wfm-punch-structure
- name: Pro Wfm Shift Structure
  property_count: 9
  slug: pro-wfm-shift-structure
- name: Pro Wfm Timecard Structure
  property_count: 8
  slug: pro-wfm-timecard-structure
- name: Pro Wfm Wfm Employee Structure
  property_count: 8
  slug: pro-wfm-wfm-employee-structure
jsonld:
- class_count: 13
  name: Ukg Pro Hcm Context
  property_count: 62
  slug: ukg-pro-hcm-context
- class_count: 6
  name: Ukg Pro Wfm Context
  property_count: 28
  slug: ukg-pro-wfm-context
layout: provider
modified: '2026-05-19'
name: UKG
nav: Providers
network: true
overview: 'UKG publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Accruals API, Benefits API, Employees API, and 5 more. Tagged areas include HCM, Workforce Management, HR, Payroll, and Time and Attendance.


  The UKG catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  UKG''s developer surface includes authentication, documentation, developer portal, engineering blog, pricing, support, getting-started guide, and 24 more developer resources.'
plans:
- name: Ukg Plans Pricing
  plan_count: 1
  slug: ukg-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Ukg Rate Limits
  slug: ukg-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: UKG API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ukg-jsonschema-spectral-rules
- effective_rule_count: 75
  extends:
  - spectral:oas
  name: UKG API Rules
  rule_count: 34
  severity_counts:
    error: 14
    hint: 0
    info: 5
    warn: 15
  slug: ukg-spectral-rules
score:
  band: thin
  composite: 33.8
  delta: 1.9
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 28.8
    contract_quality: 30.8
    developer_ergonomics: 47.6
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 31.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 8
      marker_coverage: 100.0
      total: 8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ukg/refs/heads/main/screenshots/ukg-2026-06-20T200004.png
security:
- kind: authentication
  name: Ukg Authentication
  slug: ukg-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Ukg Domain Security
  slug: ukg-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ukg
solutions:
- description: Enterprise HCM platform for mid-market and enterprise organizations with full HR, payroll, and talent capabilities.
  name: UKG Pro
- description: Workforce management platform for hourly and complex workforce scheduling, timekeeping, and compliance.
  name: UKG Pro WFM
- description: Simplified HCM solution for small and medium businesses with combined HR, payroll, and time management.
  name: UKG Ready
- description: Employee experience platform for HR case management, knowledge delivery, and document compliance.
  name: UKG HR Service Delivery
tags:
- HCM
- Workforce Management
- HR
- Payroll
- Time and Attendance
- Benefits
- Scheduling
use_cases:
- description: Sync employee pay data, deductions, and tax information with third-party payroll processors and ERP systems.
  name: Payroll Integration
- description: Exchange enrollment data and eligibility with benefits carriers, insurance providers, and benefits administration systems.
  name: Benefits Connector
- description: Import punch data, approved timecards, and schedule information into payroll and workforce analytics platforms.
  name: Time and Labor Integration
- description: Keep employee demographic, job, and organizational data synchronized between UKG and downstream business systems.
  name: HRIS Data Sync
- description: Export workforce data to business intelligence tools and data warehouses for advanced analytics and reporting.
  name: Analytics and Reporting
- description: Automate new hire provisioning by triggering downstream system access and equipment setup from UKG hire events.
  name: Onboarding Automation
website: https://www.ukg.com
---

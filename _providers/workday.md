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
  band: agent-ready
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
    error_semantics: documented
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
  score: 32.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Workday Agentic Access
  operation_count: 104
  slug: workday-agentic-access
  summary_line: 104 operations · 17 acting · 1 human-in-the-loop
api_count: 16
apis:
- description: Strategic Sourcing API for managing sourcing events, awards, contracts, suppliers, spend categories, and procurement workflows.
  name: Workday Strategic Sourcing API
  slug: strategic-sourcing-api
- description: Standards-based SOAP API providing programmatic access to Workday business management services with WSDL and XML Schema definitions. Covers 55 service areas including Human Resources, Payroll, Benefit
  name: Workday SOAP Web Services API
  slug: soap-web-services-api
- description: Workday Extend platform for building custom applications that integrate with Workday. Provides low-code and no-code developer tools for creating business solutions.
  name: Workday Extend API
  slug: extend-api
- description: Adaptive Planning REST and XML APIs for managing planning data, accounts, dimensions, and custom reports. Supports integration with enterprise planning and budgeting workflows.
  name: Workday Adaptive Planning API
  slug: adaptive-planning-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing absence types.
  name: Workday Absence Types API
  slug: workday-absence-types-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing accounting journals.
  name: Workday Accounting API
  slug: workday-accounting-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing benefit elections.
  name: Workday Benefit Elections API
  slug: workday-benefit-elections-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing benefit plans.
  name: Workday Benefit Plans API
  slug: workday-benefit-plans-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing candidates.
  name: Workday Candidates API
  slug: workday-candidates-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing compensation plans and grades.
  name: Workday Compensation Plans API
  slug: workday-compensation-plans-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing contact information.
  name: Workday Contact Information API
  slug: workday-contact-information-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing data loading tasks.
  name: Workday Data Change Tasks API
  slug: workday-data-change-tasks-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for discovering available data sources and fields.
  name: Workday Data Sources API
  slug: workday-data-sources-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing Prism Analytics datasets.
  name: Workday Datasets API
  slug: workday-datasets-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing worker dependents.
  name: Workday Dependents API
  slug: workday-dependents-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing expense reports.
  name: Workday Expenses API
  slug: workday-expenses-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing feedback and feedback badges.
  name: Workday Feedback API
  slug: workday-feedback-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for file upload containers.
  name: Workday File Containers API
  slug: workday-file-containers-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing worker goals.
  name: Workday Goals API
  slug: workday-goals-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing job applications.
  name: Workday Job Applications API
  slug: workday-job-applications-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing job postings.
  name: Workday Job Postings API
  slug: workday-job-postings-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing job profiles.
  name: Workday Job Profiles API
  slug: workday-job-profiles-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing job requisitions.
  name: Workday Job Requisitions API
  slug: workday-job-requisitions-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing leaves of absence.
  name: Workday Leave of Absence API
  slug: workday-leave-of-absence-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing location data.
  name: Workday Locations API
  slug: workday-locations-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing mentorship relationships.
  name: Workday Mentorships API
  slug: workday-mentorships-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for one-time payment requests.
  name: Workday One-Time Payments API
  slug: workday-one-time-payments-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing organizational data.
  name: Workday Organizations API
  slug: workday-organizations-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing pay groups and pay periods.
  name: Workday Pay Groups API
  slug: workday-pay-groups-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for accessing pay slips.
  name: Workday Pay Slips API
  slug: workday-pay-slips-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing payroll inputs.
  name: Workday Payroll Inputs API
  slug: workday-payroll-inputs-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing person data.
  name: Workday People API
  slug: workday-people-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing performance reviews.
  name: Workday Performance Reviews API
  slug: workday-performance-reviews-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing positions.
  name: Workday Positions API
  slug: workday-positions-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing suppliers and purchase orders.
  name: Workday Procurement API
  slug: workday-procurement-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing recruiting prospects.
  name: Workday Prospects API
  slug: workday-prospects-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for executing WQL queries.
  name: Workday Query API
  slug: workday-query-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for accessing common reference data and lookup values.
  name: Workday Reference Data API
  slug: workday-reference-data-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for accessing custom report data via RaaS.
  name: Workday Reports API
  slug: workday-reports-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing customer invoices.
  name: Workday Revenue API
  slug: workday-revenue-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing compensation scorecards and results.
  name: Workday Scorecards API
  slug: workday-scorecards-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for staffing events and organization assignments.
  name: Workday Staffing API
  slug: workday-staffing-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing succession plans.
  name: Workday Succession Planning API
  slug: workday-succession-planning-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing Prism Analytics tables.
  name: Workday Tables API
  slug: workday-tables-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing talent profiles and skills.
  name: Workday Talent Profiles API
  slug: workday-talent-profiles-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing time clock events.
  name: Workday Time Clock API
  slug: workday-time-clock-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing time entries.
  name: Workday Time Entries API
  slug: workday-time-entries-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing time-off requests and entries.
  name: Workday Time Off API
  slug: workday-time-off-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing timesheets.
  name: Workday Timesheets API
  slug: workday-timesheets-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/
  baseurl_source: declared
  description: Endpoints for managing worker data.
  name: Workday Workers API
  slug: workday-workers-api
arazzos:
- description: Read a worker's current benefit elections and eligible plans, then initiate a benefit change event.
  name: Workday Change Benefits
  slug: workday-change-benefits-workflow
- description: Confirm a worker, look up the target job profile and position, then initiate a job change.
  name: Workday Change Worker Job
  slug: workday-change-worker-job-workflow
- description: Confirm a worker and read their recent clock events, then record a new clock in/out event.
  name: Workday Clock Time Event
  slug: workday-clock-time-event-workflow
- description: Search supervisory organizations, load the first match's detail, and list its workers.
  name: Workday Explore Supervisory Organization
  slug: workday-explore-supervisory-org-workflow
- description: Search workers by name, then load the matched worker's full detail and recent history.
  name: Workday Find Worker and Load Detail
  slug: workday-find-worker-detail-workflow
- description: Confirm a worker and review their existing badges, then give a new feedback badge.
  name: Workday Give Feedback Badge
  slug: workday-give-feedback-badge-workflow
- description: Confirm a worker and read their timesheets, then log a new time entry.
  name: Workday Log Time Entry
  slug: workday-log-time-entry-workflow
- description: Search people, load the first match's detail, then gather home and work contact information.
  name: Workday Person Contact 360
  slug: workday-person-contact-360-workflow
- description: Create a Prism dataset, stage a file container, create a data change task, and confirm its status.
  name: Workday Prism Load Dataset
  slug: workday-prism-load-dataset-workflow
- description: Read a worker's current compensation and available grades, then request a compensation change.
  name: Workday Request Compensation Change
  slug: workday-request-compensation-change-workflow
- description: Read a worker's goals and reviews, then request feedback from respondents.
  name: Workday Request Feedback
  slug: workday-request-feedback-workflow
- description: Confirm a worker, review existing leaves, then submit a new leave of absence request.
  name: Workday Request Leave of Absence
  slug: workday-request-leave-of-absence-workflow
- description: Confirm a worker and read their pay slips, then submit a one-time payment request.
  name: Workday Request One-Time Payment
  slug: workday-request-one-time-payment-workflow
- description: List expense reports, load the first report's detail, and cross-reference accounting journals.
  name: Workday Review Expense Reports
  slug: workday-review-expense-reports-workflow
- description: List job requisitions, load a requisition's detail and its posting, then review job applications.
  name: Workday Review Recruiting Pipeline
  slug: workday-review-recruiting-pipeline-workflow
- description: List suppliers, load the first supplier's detail, then review purchase orders and customer invoices.
  name: Workday Review Supplier Spend
  slug: workday-review-supplier-spend-workflow
- description: Confirm a worker, then assemble their talent profile, skills, and certifications.
  name: Workday Review Talent Profile
  slug: workday-review-talent-profile-workflow
- description: Confirm a worker, check eligible absence types and balances, then submit a time-off request.
  name: Workday Submit Time Off
  slug: workday-submit-time-off-workflow
- description: Confirm a worker and review their organization assignments, then initiate a termination event.
  name: Workday Terminate Worker
  slug: workday-terminate-worker-workflow
- description: Discover a WQL data source and its fields, then execute a WQL query against it.
  name: Workday WQL Discover and Query
  slug: workday-wql-discover-and-query-workflow
artifact_total: 739
collections:
- collection_type: postman
  name: Workday Absence Management API
  slug: postman-absenceManagement
- collection_type: postman
  name: Workday Benefits API
  slug: postman-benefits
- collection_type: postman
  name: Workday Compensation API
  slug: postman-compensation
- collection_type: postman
  name: Workday Financial Management API
  slug: postman-financialManagement
- collection_type: postman
  name: Workday HCM API
  slug: postman-hcm
- collection_type: postman
  name: Workday Payroll API
  slug: postman-payroll
- collection_type: postman
  name: Workday Performance Management API
  slug: postman-performanceManagement
- collection_type: postman
  name: Workday Person API
  slug: postman-person
- collection_type: postman
  name: Workday Prism Analytics API
  slug: postman-prismAnalytics
- collection_type: postman
  name: Workday Report-as-a-Service API
  slug: postman-raas
- collection_type: postman
  name: Workday Recruiting API
  slug: postman-recruiting
- collection_type: postman
  name: Workday Staffing API
  slug: postman-staffing
- collection_type: postman
  name: Workday Talent Management API
  slug: postman-talent
- collection_type: postman
  name: Workday Time Tracking API
  slug: postman-timeTracking
- collection_type: postman
  name: Workday WQL API
  slug: postman-wql
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Workday Absence Management API
  slug: open-absenceManagement
- collection_type: open
  name: Workday Benefits API
  slug: open-benefits
- collection_type: open
  name: Workday Common API
  slug: open-common
- collection_type: open
  name: Workday Compensation API
  slug: open-compensation
- collection_type: open
  name: Workday Financial Management API
  slug: open-financialManagement
- collection_type: open
  name: Workday HCM API
  slug: open-hcm
- collection_type: open
  name: Workday Payroll API
  slug: open-payroll
- collection_type: open
  name: Workday Performance Management API
  slug: open-performanceManagement
- collection_type: open
  name: Workday Person API
  slug: open-person
- collection_type: open
  name: Workday Prism Analytics API
  slug: open-prismAnalytics
- collection_type: open
  name: Workday Report-as-a-Service API
  slug: open-raas
- collection_type: open
  name: Workday Recruiting API
  slug: open-recruiting
- collection_type: open
  name: Workday Staffing API
  slug: open-staffing
- collection_type: open
  name: Workday Talent Management API
  slug: open-talent
- collection_type: open
  name: Workday Time Tracking API
  slug: open-timeTracking
- collection_type: open
  name: Workday Absence Management Absence Types API
  slug: open-workday-absence-types-api
- collection_type: open
  name: Workday Financial Management Accounting API
  slug: open-workday-accounting-api
- collection_type: open
  name: Workday Benefits Benefit Elections API
  slug: open-workday-benefit-elections-api
- collection_type: open
  name: Workday Benefits Benefit Plans API
  slug: open-workday-benefit-plans-api
- collection_type: open
  name: Workday Recruiting Candidates API
  slug: open-workday-candidates-api
- collection_type: open
  name: Workday Compensation Compensation Plans API
  slug: open-workday-compensation-plans-api
- collection_type: open
  name: Workday Person Contact Information API
  slug: open-workday-contact-information-api
- collection_type: open
  name: Workday Prism Analytics Data Change Tasks API
  slug: open-workday-data-change-tasks-api
- collection_type: open
  name: Workday WQL Data Sources API
  slug: open-workday-data-sources-api
- collection_type: open
  name: Workday Prism Analytics Datasets API
  slug: open-workday-datasets-api
- collection_type: open
  name: Workday Benefits Dependents API
  slug: open-workday-dependents-api
- collection_type: open
  name: Workday Financial Management Expenses API
  slug: open-workday-expenses-api
- collection_type: open
  name: Workday Performance Management Feedback API
  slug: open-workday-feedback-api
- collection_type: open
  name: Workday Prism Analytics File Containers API
  slug: open-workday-file-containers-api
- collection_type: open
  name: Workday Performance Management Goals API
  slug: open-workday-goals-api
- collection_type: open
  name: Workday Recruiting Job Applications API
  slug: open-workday-job-applications-api
- collection_type: open
  name: Workday Recruiting Job Postings API
  slug: open-workday-job-postings-api
- collection_type: open
  name: Workday Staffing Job Profiles API
  slug: open-workday-job-profiles-api
- collection_type: open
  name: Workday Recruiting Job Requisitions API
  slug: open-workday-job-requisitions-api
- collection_type: open
  name: Workday Absence Management Leave of Absence API
  slug: open-workday-leave-of-absence-api
- collection_type: open
  name: Workday HCM Locations API
  slug: open-workday-locations-api
- collection_type: open
  name: Workday Talent Management Mentorships API
  slug: open-workday-mentorships-api
- collection_type: open
  name: Workday Compensation One-Time Payments API
  slug: open-workday-one-time-payments-api
- collection_type: open
  name: Workday HCM Organizations API
  slug: open-workday-organizations-api
- collection_type: open
  name: Workday Payroll Pay Groups API
  slug: open-workday-pay-groups-api
- collection_type: open
  name: Workday Payroll Pay Slips API
  slug: open-workday-pay-slips-api
- collection_type: open
  name: Workday Payroll Payroll Inputs API
  slug: open-workday-payroll-inputs-api
- collection_type: open
  name: Workday Person People API
  slug: open-workday-people-api
- collection_type: open
  name: Workday Staffing Positions API
  slug: open-workday-positions-api
- collection_type: open
  name: Workday Financial Management Procurement API
  slug: open-workday-procurement-api
- collection_type: open
  name: Workday Recruiting Prospects API
  slug: open-workday-prospects-api
- collection_type: open
  name: Workday WQL Query API
  slug: open-workday-query-api
- collection_type: open
  name: Workday Common Reference Data API
  slug: open-workday-reference-data-api
- collection_type: open
  name: Workday Report-as-a-Service Reports API
  slug: open-workday-reports-api
- collection_type: open
  name: Workday Financial Management Revenue API
  slug: open-workday-revenue-api
- collection_type: open
  name: Workday Compensation Scorecards API
  slug: open-workday-scorecards-api
- collection_type: open
  name: Workday Staffing API
  slug: open-workday-staffing-api
- collection_type: open
  name: Workday Talent Management Succession Planning API
  slug: open-workday-succession-planning-api
- collection_type: open
  name: Workday Prism Analytics Tables API
  slug: open-workday-tables-api
- collection_type: open
  name: Workday Talent Management Talent Profiles API
  slug: open-workday-talent-profiles-api
- collection_type: open
  name: Workday Time Tracking Time Clock API
  slug: open-workday-time-clock-api
- collection_type: open
  name: Workday Time Tracking Time Entries API
  slug: open-workday-time-entries-api
- collection_type: open
  name: Workday Absence Management Time Off API
  slug: open-workday-time-off-api
- collection_type: open
  name: Workday Time Tracking Timesheets API
  slug: open-workday-timesheets-api
- collection_type: open
  name: Workday HCM Workers API
  slug: open-workday-workers-api
- collection_type: open
  name: Workday WQL API
  slug: open-wql
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/workday-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/workday-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/workday-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/workday-cli.yml
- group: design
  title: ''
  type: Components
  url: components/workday-components.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/workday-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/workday-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/workday-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/workday-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/workday-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/workday-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/workday-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/workday-changelog.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/workday-well-known.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/workday-hcm-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/workday-financialManagement-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/workday-recruiting-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/workday-timeTracking-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/workday-benefits-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/workday-absenceManagement-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/workday-compensation-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/workday-payroll-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/workday-person-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/workday-performanceManagement-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/workday-talent-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/workday-staffing-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/workday-common-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/workday-prismAnalytics-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/workday-raas-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/workday-wql-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/workday-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/workday-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/workday-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/workday-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/workday/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-change-benefits-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-change-worker-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-clock-time-event-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-explore-supervisory-org-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-find-worker-detail-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-give-feedback-badge-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-log-time-entry-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-person-contact-360-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-prism-load-dataset-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-request-compensation-change-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-request-feedback-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-request-leave-of-absence-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-request-one-time-payment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-review-expense-reports-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-review-recruiting-pipeline-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-review-supplier-spend-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-review-talent-profile-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-submit-time-off-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-terminate-worker-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-wql-discover-and-query-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/workday
- group: start
  title: ''
  type: GettingStarted
  url: https://community.workday.com/api-start
- group: auth
  title: ''
  type: Authentication
  url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html#authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://community.workday.com/articles/16827
- group: operate
  title: ''
  type: StatusPage
  url: https://community.workday.com/trust/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workday.com/en-us/legal.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workday.com/en-us/privacy.html
- group: docs
  title: ''
  type: Documentation
  url: https://community.workday.com/api
- group: start
  title: ''
  type: Console
  url: https://developer.workday.com/about
- group: company
  title: ''
  type: Blog
  url: https://blog.workday.com/en-us/application-development.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/workday
- group: start
  title: ''
  type: Signup
  url: https://resourcecenter.workday.com/
- group: operate
  title: ''
  type: Support
  url: https://www.workday.com/en-us/services/support.html
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.workday.com/en-US/home
- group: company
  title: ''
  type: Partners
  url: https://www.workday.com/en-us/company/partners/overview.html
- group: docs
  title: ''
  type: APIReference
  url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
- group: other
  title: ''
  type: WSDL
  url: soap/workday-wsdl-index.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/workday-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/workday-vocabulary.yaml
created: '2024-01-15'
description: Collection of Workday REST and SOAP APIs for human capital management, financial management, enterprise planning, analytics, and platform extensibility.
examples:
- key_count: 4
  name: Absencemanagement Absence Type Example
  slug: absenceManagement-absence-type-example
- key_count: 2
  name: Absencemanagement Error Response Example
  slug: absenceManagement-error-response-example
- key_count: 8
  name: Absencemanagement Leave Of Absence Example
  slug: absenceManagement-leave-of-absence-example
- key_count: 5
  name: Absencemanagement Leave Of Absence Request Example
  slug: absenceManagement-leave-of-absence-request-example
- key_count: 3
  name: Absencemanagement Resource Reference Example
  slug: absenceManagement-resource-reference-example
- key_count: 5
  name: Absencemanagement Time Off Balance Example
  slug: absenceManagement-time-off-balance-example
- key_count: 5
  name: Absencemanagement Time Off Entry Example
  slug: absenceManagement-time-off-entry-example
- key_count: 1
  name: Absencemanagement Time Off Request Example
  slug: absenceManagement-time-off-request-example
- key_count: 1
  name: Benefits Benefit Change Request Example
  slug: benefits-benefit-change-request-example
- key_count: 9
  name: Benefits Benefit Election Example
  slug: benefits-benefit-election-example
- key_count: 5
  name: Benefits Benefit Plan Example
  slug: benefits-benefit-plan-example
- key_count: 4
  name: Benefits Dependent Example
  slug: benefits-dependent-example
- key_count: 2
  name: Benefits Error Response Example
  slug: benefits-error-response-example
- key_count: 3
  name: Benefits Resource Reference Example
  slug: benefits-resource-reference-example
- key_count: 5
  name: Common Country Example
  slug: common-country-example
- key_count: 5
  name: Common Currency Example
  slug: common-currency-example
- key_count: 2
  name: Common Error Response Example
  slug: common-error-response-example
- key_count: 4
  name: Common Language Example
  slug: common-language-example
- key_count: 2
  name: Common Reference Value Example
  slug: common-reference-value-example
- key_count: 3
  name: Common Resource Reference Example
  slug: common-resource-reference-example
- key_count: 2
  name: Compensation Compensation Change Request Example
  slug: compensation-compensation-change-request-example
- key_count: 7
  name: Compensation Compensation Grade Example
  slug: compensation-compensation-grade-example
- key_count: 5
  name: Compensation Compensation Plan Example
  slug: compensation-compensation-plan-example
- key_count: 5
  name: Compensation Compensation Scorecard Example
  slug: compensation-compensation-scorecard-example
- key_count: 2
  name: Compensation Error Response Example
  slug: compensation-error-response-example
- key_count: 2
  name: Compensation One Time Payment Request Example
  slug: compensation-one-time-payment-request-example
- key_count: 3
  name: Compensation Resource Reference Example
  slug: compensation-resource-reference-example
- key_count: 7
  name: Compensation Scorecard Result Example
  slug: compensation-scorecard-result-example
- key_count: 7
  name: Financialmanagement Accounting Journal Example
  slug: financialManagement-accounting-journal-example
- key_count: 7
  name: Financialmanagement Customer Invoice Example
  slug: financialManagement-customer-invoice-example
- key_count: 2
  name: Financialmanagement Error Response Example
  slug: financialManagement-error-response-example
- key_count: 6
  name: Financialmanagement Expense Report Example
  slug: financialManagement-expense-report-example
- key_count: 6
  name: Financialmanagement Purchase Order Example
  slug: financialManagement-purchase-order-example
- key_count: 3
  name: Financialmanagement Resource Reference Example
  slug: financialManagement-resource-reference-example
- key_count: 7
  name: Financialmanagement Supplier Example
  slug: financialManagement-supplier-example
- key_count: 4
  name: Hcm Business Title Change Example
  slug: hcm-business-title-change-example
- key_count: 2
  name: Hcm Error Response Example
  slug: hcm-error-response-example
- key_count: 5
  name: Hcm Inbox Task Example
  slug: hcm-inbox-task-example
- key_count: 6
  name: Hcm Location Example
  slug: hcm-location-example
- key_count: 3
  name: Hcm Resource Reference Example
  slug: hcm-resource-reference-example
- key_count: 6
  name: Hcm Supervisory Organization Example
  slug: hcm-supervisory-organization-example
- key_count: 10
  name: Hcm Worker Example
  slug: hcm-worker-example
- key_count: 3
  name: Hcm Worker History Entry Example
  slug: hcm-worker-history-entry-example
- key_count: 7
  name: Hcm Worker Summary Example
  slug: hcm-worker-summary-example
- key_count: 2
  name: Payroll Error Response Example
  slug: payroll-error-response-example
- key_count: 6
  name: Payroll Pay Group Detail Example
  slug: payroll-pay-group-detail-example
- key_count: 4
  name: Payroll Pay Group Example
  slug: payroll-pay-group-example
- key_count: 9
  name: Payroll Pay Slip Example
  slug: payroll-pay-slip-example
- key_count: 7
  name: Payroll Payroll Input Example
  slug: payroll-payroll-input-example
- key_count: 3
  name: Payroll Resource Reference Example
  slug: payroll-resource-reference-example
- key_count: 2
  name: Performancemanagement Error Response Example
  slug: performanceManagement-error-response-example
- key_count: 4
  name: Performancemanagement Feedback Badge Example
  slug: performanceManagement-feedback-badge-example
- key_count: 1
  name: Performancemanagement Feedback Badge Request Example
  slug: performanceManagement-feedback-badge-request-example
- key_count: 3
  name: Performancemanagement Feedback Request Example
  slug: performanceManagement-feedback-request-example
- key_count: 8
  name: Performancemanagement Goal Example
  slug: performanceManagement-goal-example
- key_count: 4
  name: Performancemanagement Performance Review Example
  slug: performanceManagement-performance-review-example
- key_count: 3
  name: Performancemanagement Resource Reference Example
  slug: performanceManagement-resource-reference-example
- key_count: 3
  name: Person Contact Information Example
  slug: person-contact-information-example
- key_count: 2
  name: Person Error Response Example
  slug: person-error-response-example
- key_count: 4
  name: Person Person Example
  slug: person-person-example
- key_count: 6
  name: Person Person Name Example
  slug: person-person-name-example
- key_count: 3
  name: Person Person Summary Example
  slug: person-person-summary-example
- key_count: 3
  name: Person Personal Information Example
  slug: person-personal-information-example
- key_count: 3
  name: Person Resource Reference Example
  slug: person-resource-reference-example
- key_count: 8
  name: Prismanalytics Data Change Task Activity Example
  slug: prismAnalytics-data-change-task-activity-example
- key_count: 2
  name: Prismanalytics Data Change Task Create Request Example
  slug: prismAnalytics-data-change-task-create-request-example
- key_count: 7
  name: Prismanalytics Data Change Task Example
  slug: prismAnalytics-data-change-task-example
- key_count: 5
  name: Prismanalytics Dataset Create Request Example
  slug: prismAnalytics-dataset-create-request-example
- key_count: 10
  name: Prismanalytics Dataset Example
  slug: prismAnalytics-dataset-example
- key_count: 6
  name: Prismanalytics Dataset Field Example
  slug: prismAnalytics-dataset-field-example
- key_count: 4
  name: Prismanalytics Dataset Update Request Example
  slug: prismAnalytics-dataset-update-request-example
- key_count: 2
  name: Prismanalytics Error Response Example
  slug: prismAnalytics-error-response-example
- key_count: 3
  name: Prismanalytics File Container Example
  slug: prismAnalytics-file-container-example
- key_count: 3
  name: Prismanalytics Resource Reference Example
  slug: prismAnalytics-resource-reference-example
- key_count: 8
  name: Prismanalytics Table Example
  slug: prismAnalytics-table-example
- key_count: 2
  name: Raas Error Response Example
  slug: raas-error-response-example
- key_count: 1
  name: Raas Report Response Example
  slug: raas-report-response-example
- key_count: 3
  name: Raas Resource Reference Example
  slug: raas-resource-reference-example
- key_count: 6
  name: Recruiting Candidate Example
  slug: recruiting-candidate-example
- key_count: 2
  name: Recruiting Error Response Example
  slug: recruiting-error-response-example
- key_count: 5
  name: Recruiting Job Application Example
  slug: recruiting-job-application-example
- key_count: 9
  name: Recruiting Job Posting Example
  slug: recruiting-job-posting-example
- key_count: 8
  name: Recruiting Job Requisition Example
  slug: recruiting-job-requisition-example
- key_count: 5
  name: Recruiting Prospect Example
  slug: recruiting-prospect-example
- key_count: 3
  name: Recruiting Resource Reference Example
  slug: recruiting-resource-reference-example
- key_count: 2
  name: Staffing Error Response Example
  slug: staffing-error-response-example
- key_count: 3
  name: Staffing Job Change Example
  slug: staffing-job-change-example
- key_count: 2
  name: Staffing Job Change Request Example
  slug: staffing-job-change-request-example
- key_count: 6
  name: Staffing Job Profile Example
  slug: staffing-job-profile-example
- key_count: 2
  name: Staffing One Time Payment Request Example
  slug: staffing-one-time-payment-request-example
- key_count: 3
  name: Staffing Organization Assignment Example
  slug: staffing-organization-assignment-example
- key_count: 6
  name: Staffing Position Example
  slug: staffing-position-example
- key_count: 3
  name: Staffing Resource Reference Example
  slug: staffing-resource-reference-example
- key_count: 4
  name: Staffing Termination Request Example
  slug: staffing-termination-request-example
- key_count: 6
  name: Talent Certification Example
  slug: talent-certification-example
- key_count: 5
  name: Talent Education Entry Example
  slug: talent-education-entry-example
- key_count: 2
  name: Talent Error Response Example
  slug: talent-error-response-example
- key_count: 6
  name: Talent Job History Entry Example
  slug: talent-job-history-entry-example
- key_count: 3
  name: Talent Language Example
  slug: talent-language-example
- key_count: 5
  name: Talent Mentorship Example
  slug: talent-mentorship-example
- key_count: 3
  name: Talent Resource Reference Example
  slug: talent-resource-reference-example
- key_count: 3
  name: Talent Skill Example
  slug: talent-skill-example
- key_count: 5
  name: Talent Succession Plan Example
  slug: talent-succession-plan-example
- key_count: 8
  name: Talent Talent Profile Example
  slug: talent-talent-profile-example
- key_count: 2
  name: Timetracking Error Response Example
  slug: timeTracking-error-response-example
- key_count: 3
  name: Timetracking Resource Reference Example
  slug: timeTracking-resource-reference-example
- key_count: 5
  name: Timetracking Time Clock Event Example
  slug: timeTracking-time-clock-event-example
- key_count: 2
  name: Timetracking Time Clock Event Request Example
  slug: timeTracking-time-clock-event-request-example
- key_count: 6
  name: Timetracking Time Entry Example
  slug: timeTracking-time-entry-example
- key_count: 3
  name: Timetracking Time Entry Request Example
  slug: timeTracking-time-entry-request-example
- key_count: 7
  name: Timetracking Timesheet Example
  slug: timeTracking-timesheet-example
- key_count: 6
  name: Workday Changebenefits Example
  slug: workday-changebenefits-example
- key_count: 6
  name: Workday Createdatachangetask Example
  slug: workday-createdatachangetask-example
- key_count: 6
  name: Workday Createdataset Example
  slug: workday-createdataset-example
- key_count: 6
  name: Workday Createfilecontainer Example
  slug: workday-createfilecontainer-example
- key_count: 6
  name: Workday Createjobchange Example
  slug: workday-createjobchange-example
- key_count: 6
  name: Workday Createtimeclockevent Example
  slug: workday-createtimeclockevent-example
- key_count: 6
  name: Workday Executewqlquery Example
  slug: workday-executewqlquery-example
- key_count: 6
  name: Workday Getaccountingjournalbyid Example
  slug: workday-getaccountingjournalbyid-example
- key_count: 6
  name: Workday Getaccountingjournals Example
  slug: workday-getaccountingjournals-example
- key_count: 6
  name: Workday Getbenefitelections Example
  slug: workday-getbenefitelections-example
- key_count: 6
  name: Workday Getbenefitplans Example
  slug: workday-getbenefitplans-example
- key_count: 6
  name: Workday Getcandidatebyid Example
  slug: workday-getcandidatebyid-example
- key_count: 6
  name: Workday Getcandidates Example
  slug: workday-getcandidates-example
- key_count: 6
  name: Workday Getcompensationgrades Example
  slug: workday-getcompensationgrades-example
- key_count: 6
  name: Workday Getcompensationplans Example
  slug: workday-getcompensationplans-example
- key_count: 6
  name: Workday Getcompensationscorecardbyid Example
  slug: workday-getcompensationscorecardbyid-example
- key_count: 6
  name: Workday Getcompensationscorecardresults Example
  slug: workday-getcompensationscorecardresults-example
- key_count: 6
  name: Workday Getcompensationscorecards Example
  slug: workday-getcompensationscorecards-example
- key_count: 6
  name: Workday Getcountries Example
  slug: workday-getcountries-example
- key_count: 6
  name: Workday Getcountrybyid Example
  slug: workday-getcountrybyid-example
- key_count: 6
  name: Workday Getcurrencies Example
  slug: workday-getcurrencies-example
- key_count: 6
  name: Workday Getcurrencybyid Example
  slug: workday-getcurrencybyid-example
- key_count: 6
  name: Workday Getcustomerinvoices Example
  slug: workday-getcustomerinvoices-example
- key_count: 6
  name: Workday Getcustomreport Example
  slug: workday-getcustomreport-example
- key_count: 6
  name: Workday Getdatachangetaskactivities Example
  slug: workday-getdatachangetaskactivities-example
- key_count: 6
  name: Workday Getdatachangetaskbyid Example
  slug: workday-getdatachangetaskbyid-example
- key_count: 6
  name: Workday Getdatachangetasks Example
  slug: workday-getdatachangetasks-example
- key_count: 6
  name: Workday Getdatasetbyid Example
  slug: workday-getdatasetbyid-example
- key_count: 6
  name: Workday Getdatasets Example
  slug: workday-getdatasets-example
- key_count: 6
  name: Workday Getdatasourcebyid Example
  slug: workday-getdatasourcebyid-example
- key_count: 6
  name: Workday Getdatasourcefields Example
  slug: workday-getdatasourcefields-example
- key_count: 6
  name: Workday Getdatasources Example
  slug: workday-getdatasources-example
- key_count: 6
  name: Workday Getdependents Example
  slug: workday-getdependents-example
- key_count: 6
  name: Workday Geteligibleabsencetypes Example
  slug: workday-geteligibleabsencetypes-example
- key_count: 6
  name: Workday Geteligiblebenefitplans Example
  slug: workday-geteligiblebenefitplans-example
- key_count: 6
  name: Workday Getexpensereportbyid Example
  slug: workday-getexpensereportbyid-example
- key_count: 6
  name: Workday Getexpensereports Example
  slug: workday-getexpensereports-example
- key_count: 6
  name: Workday Getfeedbackbadges Example
  slug: workday-getfeedbackbadges-example
- key_count: 6
  name: Workday Getfilecontainerbyid Example
  slug: workday-getfilecontainerbyid-example
- key_count: 6
  name: Workday Getgenders Example
  slug: workday-getgenders-example
- key_count: 6
  name: Workday Gethomecontactinformation Example
  slug: workday-gethomecontactinformation-example
- key_count: 6
  name: Workday Getjobapplicationbyid Example
  slug: workday-getjobapplicationbyid-example
- key_count: 6
  name: Workday Getjobapplications Example
  slug: workday-getjobapplications-example
- key_count: 6
  name: Workday Getjobpostingbyid Example
  slug: workday-getjobpostingbyid-example
- key_count: 6
  name: Workday Getjobpostings Example
  slug: workday-getjobpostings-example
- key_count: 6
  name: Workday Getjobprofilebyid Example
  slug: workday-getjobprofilebyid-example
- key_count: 6
  name: Workday Getjobprofiles Example
  slug: workday-getjobprofiles-example
- key_count: 6
  name: Workday Getjobrequisitionbyid Example
  slug: workday-getjobrequisitionbyid-example
- key_count: 6
  name: Workday Getjobrequisitions Example
  slug: workday-getjobrequisitions-example
- key_count: 6
  name: Workday Getlanguages Example
  slug: workday-getlanguages-example
- key_count: 6
  name: Workday Getleavesofabsence Example
  slug: workday-getleavesofabsence-example
- key_count: 6
  name: Workday Getlocationbyid Example
  slug: workday-getlocationbyid-example
- key_count: 6
  name: Workday Getlocations Example
  slug: workday-getlocations-example
- key_count: 6
  name: Workday Getmaritalstatuses Example
  slug: workday-getmaritalstatuses-example
- key_count: 6
  name: Workday Getmentorships Example
  slug: workday-getmentorships-example
- key_count: 6
  name: Workday Getorganizationassignments Example
  slug: workday-getorganizationassignments-example
- key_count: 6
  name: Workday Getpaygroupbyid Example
  slug: workday-getpaygroupbyid-example
- key_count: 6
  name: Workday Getpaygroupdetails Example
  slug: workday-getpaygroupdetails-example
- key_count: 6
  name: Workday Getpaygroups Example
  slug: workday-getpaygroups-example
- key_count: 6
  name: Workday Getpayrollinputs Example
  slug: workday-getpayrollinputs-example
- key_count: 6
  name: Workday Getpayslips Example
  slug: workday-getpayslips-example
- key_count: 6
  name: Workday Getpeople Example
  slug: workday-getpeople-example
- key_count: 6
  name: Workday Getperformancereviews Example
  slug: workday-getperformancereviews-example
- key_count: 6
  name: Workday Getpersonalinformation Example
  slug: workday-getpersonalinformation-example
- key_count: 6
  name: Workday Getpersonbyid Example
  slug: workday-getpersonbyid-example
- key_count: 6
  name: Workday Getpositionbyid Example
  slug: workday-getpositionbyid-example
- key_count: 6
  name: Workday Getpositions Example
  slug: workday-getpositions-example
- key_count: 6
  name: Workday Getprospects Example
  slug: workday-getprospects-example
- key_count: 6
  name: Workday Getpurchaseorders Example
  slug: workday-getpurchaseorders-example
- key_count: 6
  name: Workday Getsuccessionplanbyid Example
  slug: workday-getsuccessionplanbyid-example
- key_count: 6
  name: Workday Getsuccessionplans Example
  slug: workday-getsuccessionplans-example
- key_count: 6
  name: Workday Getsupervisoryorganizationbyid Example
  slug: workday-getsupervisoryorganizationbyid-example
- key_count: 6
  name: Workday Getsupervisoryorganizations Example
  slug: workday-getsupervisoryorganizations-example
- key_count: 6
  name: Workday Getsupplierbyid Example
  slug: workday-getsupplierbyid-example
- key_count: 6
  name: Workday Getsuppliers Example
  slug: workday-getsuppliers-example
- key_count: 6
  name: Workday Gettablebyid Example
  slug: workday-gettablebyid-example
- key_count: 6
  name: Workday Gettables Example
  slug: workday-gettables-example
- key_count: 6
  name: Workday Gettalentprofile Example
  slug: workday-gettalentprofile-example
- key_count: 6
  name: Workday Gettimeclockevents Example
  slug: workday-gettimeclockevents-example
- key_count: 6
  name: Workday Gettimeentries Example
  slug: workday-gettimeentries-example
- key_count: 6
  name: Workday Gettimeoffbalances Example
  slug: workday-gettimeoffbalances-example
- key_count: 6
  name: Workday Gettimeoffentries Example
  slug: workday-gettimeoffentries-example
- key_count: 6
  name: Workday Gettimesheets Example
  slug: workday-gettimesheets-example
- key_count: 6
  name: Workday Getworkcontactinformation Example
  slug: workday-getworkcontactinformation-example
- key_count: 6
  name: Workday Getworkerbusinesstitlechanges Example
  slug: workday-getworkerbusinesstitlechanges-example
- key_count: 6
  name: Workday Getworkerbyid Example
  slug: workday-getworkerbyid-example
- key_count: 6
  name: Workday Getworkercertifications Example
  slug: workday-getworkercertifications-example
- key_count: 6
  name: Workday Getworkergoals Example
  slug: workday-getworkergoals-example
- key_count: 6
  name: Workday Getworkerhistory Example
  slug: workday-getworkerhistory-example
- key_count: 6
  name: Workday Getworkerinboxtasks Example
  slug: workday-getworkerinboxtasks-example
- key_count: 6
  name: Workday Getworkerphoto Example
  slug: workday-getworkerphoto-example
- key_count: 6
  name: Workday Getworkers Example
  slug: workday-getworkers-example
- key_count: 6
  name: Workday Getworkerskills Example
  slug: workday-getworkerskills-example
- key_count: 6
  name: Workday Givefeedbackbadge Example
  slug: workday-givefeedbackbadge-example
- key_count: 6
  name: Workday Requestcompensationchange Example
  slug: workday-requestcompensationchange-example
- key_count: 6
  name: Workday Requestfeedback Example
  slug: workday-requestfeedback-example
- key_count: 6
  name: Workday Requestleaveofabsence Example
  slug: workday-requestleaveofabsence-example
- key_count: 6
  name: Workday Requestonetimepayment Example
  slug: workday-requestonetimepayment-example
- key_count: 6
  name: Workday Requesttimeentry Example
  slug: workday-requesttimeentry-example
- key_count: 6
  name: Workday Requesttimeoff Example
  slug: workday-requesttimeoff-example
- key_count: 6
  name: Workday Terminateworker Example
  slug: workday-terminateworker-example
- key_count: 6
  name: Workday Updatedataset Example
  slug: workday-updatedataset-example
- key_count: 5
  name: Wql Data Source Example
  slug: wql-data-source-example
- key_count: 8
  name: Wql Data Source Field Example
  slug: wql-data-source-field-example
- key_count: 2
  name: Wql Error Response Example
  slug: wql-error-response-example
- key_count: 3
  name: Wql Resource Reference Example
  slug: wql-resource-reference-example
- key_count: 2
  name: Wql Wql Query Result Example
  slug: wql-wql-query-result-example
features:
- description: Comprehensive HCM suite for managing the entire employee lifecycle from hiring to retirement with global compliance.
  name: Human Capital Management
- description: Cloud-native financial management with real-time accounting, procurement, expenses, and revenue management.
  name: Financial Management
- description: Enterprise planning and budgeting with collaborative forecasting, scenario modeling, and rolling forecasts.
  name: Adaptive Planning
- description: Augmented analytics platform combining Workday and third-party data for actionable business intelligence.
  name: Prism Analytics
- description: End-to-end recruiting solution with job requisitions, candidate management, and interview scheduling.
  name: Recruiting
- description: Skills-based talent optimization with performance reviews, succession planning, and career development.
  name: Talent Management
- description: Global payroll processing with automated calculations, tax compliance, and pay slip generation.
  name: Payroll
- description: Automated time entry, timesheet management, leave balances, and absence request workflows.
  name: Time and Absence Tracking
- description: Low-code platform for building custom applications that integrate natively with the Workday ecosystem.
  name: Workday Extend
- description: Expose custom Workday reports as RESTful web services for programmatic data access and integration.
  name: Report-as-a-Service
finops:
- name: Workday Finops
  service_category: Enterprise SaaS
  slug: workday-finops
graphqls:
- description: Workday is a cloud-based HCM and Financial Management platform delivering REST and SOAP APIs across human capital management, payroll, benefits, recruiting, talent, time tracking, and financial manage
  name: Workday GraphQL Schema
  slug: workday-graphql
image: /assets/icons/workday.png
integrations:
- description: Sync workforce and customer data between Workday HCM and Salesforce CRM for unified employee and customer insights.
  name: Salesforce
- description: Integrate Workday with Microsoft Teams, Outlook, and Azure AD for single sign-on and productivity workflows.
  name: Microsoft 365
- description: Connect Workday HR processes with ServiceNow ITSM for automated employee service delivery and ticket management.
  name: ServiceNow
- description: Enable Workday notifications, approvals, and time-off requests directly within Slack channels and DMs.
  name: Slack
- description: Integrate Workday payroll with ADP for third-party payroll processing and tax filing services.
  name: ADP
- description: Connect Workday financial management with SAP ERP for cross-system accounting and procurement workflows.
  name: SAP
- description: Integrate Workday with Greenhouse recruiting for seamless candidate pipeline management and hiring workflows.
  name: Greenhouse
- description: Connect Workday with Okta for identity management, single sign-on, and automated user provisioning.
  name: Okta
json_schemas:
- name: AbsenceType
  property_count: 4
  slug: absenceManagement-absence-type
- name: ErrorResponse
  property_count: 2
  slug: absenceManagement-error-response
- name: LeaveOfAbsenceRequest
  property_count: 5
  slug: absenceManagement-leave-of-absence-request
- name: LeaveOfAbsence
  property_count: 8
  slug: absenceManagement-leave-of-absence
- name: ResourceReference
  property_count: 3
  slug: absenceManagement-resource-reference
- name: TimeOffBalance
  property_count: 5
  slug: absenceManagement-time-off-balance
- name: TimeOffEntry
  property_count: 5
  slug: absenceManagement-time-off-entry
- name: TimeOffRequest
  property_count: 1
  slug: absenceManagement-time-off-request
- name: BenefitChangeRequest
  property_count: 1
  slug: benefits-benefit-change-request
- name: BenefitElection
  property_count: 9
  slug: benefits-benefit-election
- name: BenefitPlan
  property_count: 5
  slug: benefits-benefit-plan
- name: Dependent
  property_count: 4
  slug: benefits-dependent
- name: ErrorResponse
  property_count: 2
  slug: benefits-error-response
- name: ResourceReference
  property_count: 3
  slug: benefits-resource-reference
- name: Country
  property_count: 5
  slug: common-country
- name: Currency
  property_count: 5
  slug: common-currency
- name: ErrorResponse
  property_count: 2
  slug: common-error-response
- name: Language
  property_count: 4
  slug: common-language
- name: ReferenceValue
  property_count: 2
  slug: common-reference-value
- name: ResourceReference
  property_count: 3
  slug: common-resource-reference
- name: CompensationChangeRequest
  property_count: 2
  slug: compensation-compensation-change-request
- name: CompensationGrade
  property_count: 7
  slug: compensation-compensation-grade
- name: CompensationPlan
  property_count: 5
  slug: compensation-compensation-plan
- name: CompensationScorecard
  property_count: 5
  slug: compensation-compensation-scorecard
- name: ErrorResponse
  property_count: 2
  slug: compensation-error-response
- name: OneTimePaymentRequest
  property_count: 2
  slug: compensation-one-time-payment-request
- name: ResourceReference
  property_count: 3
  slug: compensation-resource-reference
- name: ScorecardResult
  property_count: 7
  slug: compensation-scorecard-result
- name: Compensation
  property_count: 18
  slug: compensation
- name: AccountingJournal
  property_count: 7
  slug: financialManagement-accounting-journal
- name: CustomerInvoice
  property_count: 7
  slug: financialManagement-customer-invoice
- name: ErrorResponse
  property_count: 2
  slug: financialManagement-error-response
- name: ExpenseReport
  property_count: 6
  slug: financialManagement-expense-report
- name: PurchaseOrder
  property_count: 6
  slug: financialManagement-purchase-order
- name: ResourceReference
  property_count: 3
  slug: financialManagement-resource-reference
- name: Supplier
  property_count: 7
  slug: financialManagement-supplier
- name: BusinessTitleChange
  property_count: 4
  slug: hcm-business-title-change
- name: ErrorResponse
  property_count: 2
  slug: hcm-error-response
- name: InboxTask
  property_count: 5
  slug: hcm-inbox-task
- name: Location
  property_count: 6
  slug: hcm-location
- name: ResourceReference
  property_count: 3
  slug: hcm-resource-reference
- name: SupervisoryOrganization
  property_count: 6
  slug: hcm-supervisory-organization
- name: WorkerHistoryEntry
  property_count: 3
  slug: hcm-worker-history-entry
- name: Worker
  property_count: 10
  slug: hcm-worker
- name: WorkerSummary
  property_count: 7
  slug: hcm-worker-summary
- name: Organization
  property_count: 20
  slug: organization
- name: ErrorResponse
  property_count: 2
  slug: payroll-error-response
- name: PayGroupDetail
  property_count: 6
  slug: payroll-pay-group-detail
- name: PayGroup
  property_count: 4
  slug: payroll-pay-group
- name: PaySlip
  property_count: 9
  slug: payroll-pay-slip
- name: PayrollInput
  property_count: 7
  slug: payroll-payroll-input
- name: ResourceReference
  property_count: 3
  slug: payroll-resource-reference
- name: ErrorResponse
  property_count: 2
  slug: performanceManagement-error-response
- name: FeedbackBadgeRequest
  property_count: 1
  slug: performanceManagement-feedback-badge-request
- name: FeedbackBadge
  property_count: 4
  slug: performanceManagement-feedback-badge
- name: FeedbackRequest
  property_count: 3
  slug: performanceManagement-feedback-request
- name: Goal
  property_count: 8
  slug: performanceManagement-goal
- name: PerformanceReview
  property_count: 4
  slug: performanceManagement-performance-review
- name: ResourceReference
  property_count: 3
  slug: performanceManagement-resource-reference
- name: ContactInformation
  property_count: 3
  slug: person-contact-information
- name: ErrorResponse
  property_count: 2
  slug: person-error-response
- name: PersonName
  property_count: 6
  slug: person-person-name
- name: Person
  property_count: 4
  slug: person-person
- name: PersonSummary
  property_count: 3
  slug: person-person-summary
- name: PersonalInformation
  property_count: 3
  slug: person-personal-information
- name: ResourceReference
  property_count: 3
  slug: person-resource-reference
- name: Position
  property_count: 22
  slug: position
- name: DataChangeTaskActivity
  property_count: 8
  slug: prismAnalytics-data-change-task-activity
- name: DataChangeTaskCreateRequest
  property_count: 2
  slug: prismAnalytics-data-change-task-create-request
- name: DataChangeTask
  property_count: 7
  slug: prismAnalytics-data-change-task
- name: DatasetCreateRequest
  property_count: 5
  slug: prismAnalytics-dataset-create-request
- name: DatasetField
  property_count: 6
  slug: prismAnalytics-dataset-field
- name: Dataset
  property_count: 10
  slug: prismAnalytics-dataset
- name: DatasetUpdateRequest
  property_count: 4
  slug: prismAnalytics-dataset-update-request
- name: ErrorResponse
  property_count: 2
  slug: prismAnalytics-error-response
- name: FileContainer
  property_count: 3
  slug: prismAnalytics-file-container
- name: ResourceReference
  property_count: 3
  slug: prismAnalytics-resource-reference
- name: Table
  property_count: 8
  slug: prismAnalytics-table
- name: ErrorResponse
  property_count: 2
  slug: raas-error-response
- name: ReportResponse
  property_count: 1
  slug: raas-report-response
- name: ResourceReference
  property_count: 3
  slug: raas-resource-reference
- name: Candidate
  property_count: 6
  slug: recruiting-candidate
- name: ErrorResponse
  property_count: 2
  slug: recruiting-error-response
- name: JobApplication
  property_count: 5
  slug: recruiting-job-application
- name: JobPosting
  property_count: 9
  slug: recruiting-job-posting
- name: JobRequisition
  property_count: 8
  slug: recruiting-job-requisition
- name: Prospect
  property_count: 5
  slug: recruiting-prospect
- name: ResourceReference
  property_count: 3
  slug: recruiting-resource-reference
- name: ErrorResponse
  property_count: 2
  slug: staffing-error-response
- name: JobChangeRequest
  property_count: 2
  slug: staffing-job-change-request
- name: JobChange
  property_count: 3
  slug: staffing-job-change
- name: JobProfile
  property_count: 6
  slug: staffing-job-profile
- name: OneTimePaymentRequest
  property_count: 2
  slug: staffing-one-time-payment-request
- name: OrganizationAssignment
  property_count: 3
  slug: staffing-organization-assignment
- name: Position
  property_count: 6
  slug: staffing-position
- name: ResourceReference
  property_count: 3
  slug: staffing-resource-reference
- name: TerminationRequest
  property_count: 4
  slug: staffing-termination-request
- name: Certification
  property_count: 6
  slug: talent-certification
- name: EducationEntry
  property_count: 5
  slug: talent-education-entry
- name: ErrorResponse
  property_count: 2
  slug: talent-error-response
- name: JobHistoryEntry
  property_count: 6
  slug: talent-job-history-entry
- name: Language
  property_count: 3
  slug: talent-language
- name: Mentorship
  property_count: 5
  slug: talent-mentorship
- name: ResourceReference
  property_count: 3
  slug: talent-resource-reference
- name: Skill
  property_count: 3
  slug: talent-skill
- name: SuccessionPlan
  property_count: 5
  slug: talent-succession-plan
- name: TalentProfile
  property_count: 8
  slug: talent-talent-profile
- name: Time Off
  property_count: 13
  slug: time-off
- name: ErrorResponse
  property_count: 2
  slug: timeTracking-error-response
- name: ResourceReference
  property_count: 3
  slug: timeTracking-resource-reference
- name: TimeClockEventRequest
  property_count: 2
  slug: timeTracking-time-clock-event-request
- name: TimeClockEvent
  property_count: 5
  slug: timeTracking-time-clock-event
- name: TimeEntryRequest
  property_count: 3
  slug: timeTracking-time-entry-request
- name: TimeEntry
  property_count: 6
  slug: timeTracking-time-entry
- name: Timesheet
  property_count: 7
  slug: timeTracking-timesheet
- name: AbsenceType
  property_count: 4
  slug: workday-absencetype
- name: AccountingJournal
  property_count: 10
  slug: workday-accountingjournal
- name: BenefitChangeRequest
  property_count: 3
  slug: workday-benefitchangerequest
- name: BenefitElection
  property_count: 12
  slug: workday-benefitelection
- name: BenefitPlan
  property_count: 6
  slug: workday-benefitplan
- name: BusinessTitleChange
  property_count: 4
  slug: workday-businesstitlechange
- name: Candidate
  property_count: 8
  slug: workday-candidate
- name: Certification
  property_count: 6
  slug: workday-certification
- name: CompensationChangeRequest
  property_count: 3
  slug: workday-compensationchangerequest
- name: CompensationGrade
  property_count: 9
  slug: workday-compensationgrade
- name: CompensationPlan
  property_count: 10
  slug: workday-compensationplan
- name: CompensationScorecard
  property_count: 6
  slug: workday-compensationscorecard
- name: ContactInformation
  property_count: 3
  slug: workday-contactinformation
- name: Country
  property_count: 5
  slug: workday-country
- name: Currency
  property_count: 5
  slug: workday-currency
- name: CustomerInvoice
  property_count: 9
  slug: workday-customerinvoice
- name: DataChangeTask
  property_count: 9
  slug: workday-datachangetask
- name: DataChangeTaskActivity
  property_count: 8
  slug: workday-datachangetaskactivity
- name: DataChangeTaskCreateRequest
  property_count: 4
  slug: workday-datachangetaskcreaterequest
- name: Dataset
  property_count: 10
  slug: workday-dataset
- name: DatasetCreateRequest
  property_count: 5
  slug: workday-datasetcreaterequest
- name: DatasetField
  property_count: 6
  slug: workday-datasetfield
- name: DatasetUpdateRequest
  property_count: 4
  slug: workday-datasetupdaterequest
- name: DataSource
  property_count: 5
  slug: workday-datasource
- name: DataSourceField
  property_count: 8
  slug: workday-datasourcefield
- name: Dependent
  property_count: 6
  slug: workday-dependent
- name: EducationEntry
  property_count: 6
  slug: workday-educationentry
- name: ErrorResponse
  property_count: 2
  slug: workday-errorresponse
- name: ExpenseReport
  property_count: 8
  slug: workday-expensereport
- name: FeedbackBadge
  property_count: 6
  slug: workday-feedbackbadge
- name: FeedbackBadgeRequest
  property_count: 2
  slug: workday-feedbackbadgerequest
- name: FeedbackRequest
  property_count: 3
  slug: workday-feedbackrequest
- name: FileContainer
  property_count: 3
  slug: workday-filecontainer
- name: Goal
  property_count: 9
  slug: workday-goal
- name: InboxTask
  property_count: 7
  slug: workday-inboxtask
- name: JobApplication
  property_count: 8
  slug: workday-jobapplication
- name: JobChange
  property_count: 5
  slug: workday-jobchange
- name: JobChangeRequest
  property_count: 6
  slug: workday-jobchangerequest
- name: JobHistoryEntry
  property_count: 6
  slug: workday-jobhistoryentry
- name: JobPosting
  property_count: 11
  slug: workday-jobposting
- name: JobProfile
  property_count: 9
  slug: workday-jobprofile
- name: JobRequisition
  property_count: 13
  slug: workday-jobrequisition
- name: Language
  property_count: 4
  slug: workday-language
- name: LeaveOfAbsence
  property_count: 9
  slug: workday-leaveofabsence
- name: LeaveOfAbsenceRequest
  property_count: 7
  slug: workday-leaveofabsencerequest
- name: Location
  property_count: 8
  slug: workday-location
- name: Mentorship
  property_count: 8
  slug: workday-mentorship
- name: OneTimePaymentRequest
  property_count: 5
  slug: workday-onetimepaymentrequest
- name: OrganizationAssignment
  property_count: 5
  slug: workday-organizationassignment
- name: PayGroup
  property_count: 7
  slug: workday-paygroup
- name: PayGroupDetail
  property_count: 6
  slug: workday-paygroupdetail
- name: PayrollInput
  property_count: 9
  slug: workday-payrollinput
- name: PaySlip
  property_count: 11
  slug: workday-payslip
- name: PerformanceReview
  property_count: 8
  slug: workday-performancereview
- name: Person
  property_count: 9
  slug: workday-person
- name: PersonalInformation
  property_count: 9
  slug: workday-personalinformation
- name: PersonName
  property_count: 6
  slug: workday-personname
- name: PersonSummary
  property_count: 3
  slug: workday-personsummary
- name: Position
  property_count: 12
  slug: workday-position
- name: Prospect
  property_count: 7
  slug: workday-prospect
- name: PurchaseOrder
  property_count: 8
  slug: workday-purchaseorder
- name: ReferenceValue
  property_count: 2
  slug: workday-referencevalue
- name: ReportResponse
  property_count: 1
  slug: workday-reportresponse
- name: ResourceReference
  property_count: 3
  slug: workday-resourcereference
- name: ScorecardResult
  property_count: 9
  slug: workday-scorecardresult
- name: Skill
  property_count: 5
  slug: workday-skill
- name: SuccessionPlan
  property_count: 7
  slug: workday-successionplan
- name: SupervisoryOrganization
  property_count: 9
  slug: workday-supervisoryorganization
- name: Supplier
  property_count: 9
  slug: workday-supplier
- name: Table
  property_count: 8
  slug: workday-table
- name: TalentProfile
  property_count: 9
  slug: workday-talentprofile
- name: TerminationRequest
  property_count: 6
  slug: workday-terminationrequest
- name: TimeClockEvent
  property_count: 6
  slug: workday-timeclockevent
- name: TimeClockEventRequest
  property_count: 3
  slug: workday-timeclockeventrequest
- name: TimeEntry
  property_count: 8
  slug: workday-timeentry
- name: TimeEntryRequest
  property_count: 5
  slug: workday-timeentryrequest
- name: TimeOffBalance
  property_count: 6
  slug: workday-timeoffbalance
- name: TimeOffEntry
  property_count: 7
  slug: workday-timeoffentry
- name: TimeOffRequest
  property_count: 1
  slug: workday-timeoffrequest
- name: Timesheet
  property_count: 7
  slug: workday-timesheet
- name: Worker
  property_count: 13
  slug: workday-worker
- name: WorkerHistoryEntry
  property_count: 4
  slug: workday-workerhistoryentry
- name: WorkerSummary
  property_count: 8
  slug: workday-workersummary
- name: WqlQueryResult
  property_count: 2
  slug: workday-wqlqueryresult
- name: Worker
  property_count: 15
  slug: worker
- name: DataSourceField
  property_count: 8
  slug: wql-data-source-field
- name: DataSource
  property_count: 5
  slug: wql-data-source
- name: ErrorResponse
  property_count: 2
  slug: wql-error-response
- name: ResourceReference
  property_count: 3
  slug: wql-resource-reference
- name: WqlQueryResult
  property_count: 2
  slug: wql-wql-query-result
json_structures:
- name: Absencemanagement Absence Type Structure
  property_count: 4
  slug: absenceManagement-absence-type-structure
- name: Absencemanagement Error Response Structure
  property_count: 2
  slug: absenceManagement-error-response-structure
- name: Absencemanagement Leave Of Absence Request Structure
  property_count: 5
  slug: absenceManagement-leave-of-absence-request-structure
- name: Absencemanagement Leave Of Absence Structure
  property_count: 8
  slug: absenceManagement-leave-of-absence-structure
- name: Absencemanagement Resource Reference Structure
  property_count: 3
  slug: absenceManagement-resource-reference-structure
- name: Absencemanagement Time Off Balance Structure
  property_count: 5
  slug: absenceManagement-time-off-balance-structure
- name: Absencemanagement Time Off Entry Structure
  property_count: 5
  slug: absenceManagement-time-off-entry-structure
- name: Absencemanagement Time Off Request Structure
  property_count: 1
  slug: absenceManagement-time-off-request-structure
- name: Benefits Benefit Change Request Structure
  property_count: 1
  slug: benefits-benefit-change-request-structure
- name: Benefits Benefit Election Structure
  property_count: 9
  slug: benefits-benefit-election-structure
- name: Benefits Benefit Plan Structure
  property_count: 5
  slug: benefits-benefit-plan-structure
- name: Benefits Dependent Structure
  property_count: 4
  slug: benefits-dependent-structure
- name: Benefits Error Response Structure
  property_count: 2
  slug: benefits-error-response-structure
- name: Benefits Resource Reference Structure
  property_count: 3
  slug: benefits-resource-reference-structure
- name: Common Country Structure
  property_count: 5
  slug: common-country-structure
- name: Common Currency Structure
  property_count: 5
  slug: common-currency-structure
- name: Common Error Response Structure
  property_count: 2
  slug: common-error-response-structure
- name: Common Language Structure
  property_count: 4
  slug: common-language-structure
- name: Common Reference Value Structure
  property_count: 2
  slug: common-reference-value-structure
- name: Common Resource Reference Structure
  property_count: 3
  slug: common-resource-reference-structure
- name: Compensation Compensation Change Request Structure
  property_count: 2
  slug: compensation-compensation-change-request-structure
- name: Compensation Compensation Grade Structure
  property_count: 7
  slug: compensation-compensation-grade-structure
- name: Compensation Compensation Plan Structure
  property_count: 5
  slug: compensation-compensation-plan-structure
- name: Compensation Compensation Scorecard Structure
  property_count: 5
  slug: compensation-compensation-scorecard-structure
- name: Compensation Error Response Structure
  property_count: 2
  slug: compensation-error-response-structure
- name: Compensation One Time Payment Request Structure
  property_count: 2
  slug: compensation-one-time-payment-request-structure
- name: Compensation Resource Reference Structure
  property_count: 3
  slug: compensation-resource-reference-structure
- name: Compensation Scorecard Result Structure
  property_count: 7
  slug: compensation-scorecard-result-structure
- name: Financialmanagement Accounting Journal Structure
  property_count: 7
  slug: financialManagement-accounting-journal-structure
- name: Financialmanagement Customer Invoice Structure
  property_count: 7
  slug: financialManagement-customer-invoice-structure
- name: Financialmanagement Error Response Structure
  property_count: 2
  slug: financialManagement-error-response-structure
- name: Financialmanagement Expense Report Structure
  property_count: 6
  slug: financialManagement-expense-report-structure
- name: Financialmanagement Purchase Order Structure
  property_count: 6
  slug: financialManagement-purchase-order-structure
- name: Financialmanagement Resource Reference Structure
  property_count: 3
  slug: financialManagement-resource-reference-structure
- name: Financialmanagement Supplier Structure
  property_count: 7
  slug: financialManagement-supplier-structure
- name: Hcm Business Title Change Structure
  property_count: 4
  slug: hcm-business-title-change-structure
- name: Hcm Error Response Structure
  property_count: 2
  slug: hcm-error-response-structure
- name: Hcm Inbox Task Structure
  property_count: 5
  slug: hcm-inbox-task-structure
- name: Hcm Location Structure
  property_count: 6
  slug: hcm-location-structure
- name: Hcm Resource Reference Structure
  property_count: 3
  slug: hcm-resource-reference-structure
- name: Hcm Supervisory Organization Structure
  property_count: 6
  slug: hcm-supervisory-organization-structure
- name: Hcm Worker History Entry Structure
  property_count: 3
  slug: hcm-worker-history-entry-structure
- name: Hcm Worker Structure
  property_count: 10
  slug: hcm-worker-structure
- name: Hcm Worker Summary Structure
  property_count: 7
  slug: hcm-worker-summary-structure
- name: Payroll Error Response Structure
  property_count: 2
  slug: payroll-error-response-structure
- name: Payroll Pay Group Detail Structure
  property_count: 6
  slug: payroll-pay-group-detail-structure
- name: Payroll Pay Group Structure
  property_count: 4
  slug: payroll-pay-group-structure
- name: Payroll Pay Slip Structure
  property_count: 9
  slug: payroll-pay-slip-structure
- name: Payroll Payroll Input Structure
  property_count: 7
  slug: payroll-payroll-input-structure
- name: Payroll Resource Reference Structure
  property_count: 3
  slug: payroll-resource-reference-structure
- name: Performancemanagement Error Response Structure
  property_count: 2
  slug: performanceManagement-error-response-structure
- name: Performancemanagement Feedback Badge Request Structure
  property_count: 1
  slug: performanceManagement-feedback-badge-request-structure
- name: Performancemanagement Feedback Badge Structure
  property_count: 4
  slug: performanceManagement-feedback-badge-structure
- name: Performancemanagement Feedback Request Structure
  property_count: 3
  slug: performanceManagement-feedback-request-structure
- name: Performancemanagement Goal Structure
  property_count: 8
  slug: performanceManagement-goal-structure
- name: Performancemanagement Performance Review Structure
  property_count: 4
  slug: performanceManagement-performance-review-structure
- name: Performancemanagement Resource Reference Structure
  property_count: 3
  slug: performanceManagement-resource-reference-structure
- name: Person Contact Information Structure
  property_count: 3
  slug: person-contact-information-structure
- name: Person Error Response Structure
  property_count: 2
  slug: person-error-response-structure
- name: Person Person Name Structure
  property_count: 6
  slug: person-person-name-structure
- name: Person Person Structure
  property_count: 4
  slug: person-person-structure
- name: Person Person Summary Structure
  property_count: 3
  slug: person-person-summary-structure
- name: Person Personal Information Structure
  property_count: 3
  slug: person-personal-information-structure
- name: Person Resource Reference Structure
  property_count: 3
  slug: person-resource-reference-structure
- name: Prismanalytics Data Change Task Activity Structure
  property_count: 8
  slug: prismAnalytics-data-change-task-activity-structure
- name: Prismanalytics Data Change Task Create Request Structure
  property_count: 2
  slug: prismAnalytics-data-change-task-create-request-structure
- name: Prismanalytics Data Change Task Structure
  property_count: 7
  slug: prismAnalytics-data-change-task-structure
- name: Prismanalytics Dataset Create Request Structure
  property_count: 5
  slug: prismAnalytics-dataset-create-request-structure
- name: Prismanalytics Dataset Field Structure
  property_count: 6
  slug: prismAnalytics-dataset-field-structure
- name: Prismanalytics Dataset Structure
  property_count: 10
  slug: prismAnalytics-dataset-structure
- name: Prismanalytics Dataset Update Request Structure
  property_count: 4
  slug: prismAnalytics-dataset-update-request-structure
- name: Prismanalytics Error Response Structure
  property_count: 2
  slug: prismAnalytics-error-response-structure
- name: Prismanalytics File Container Structure
  property_count: 3
  slug: prismAnalytics-file-container-structure
- name: Prismanalytics Resource Reference Structure
  property_count: 3
  slug: prismAnalytics-resource-reference-structure
- name: Prismanalytics Table Structure
  property_count: 8
  slug: prismAnalytics-table-structure
- name: Raas Error Response Structure
  property_count: 2
  slug: raas-error-response-structure
- name: Raas Report Response Structure
  property_count: 1
  slug: raas-report-response-structure
- name: Raas Resource Reference Structure
  property_count: 3
  slug: raas-resource-reference-structure
- name: Recruiting Candidate Structure
  property_count: 6
  slug: recruiting-candidate-structure
- name: Recruiting Error Response Structure
  property_count: 2
  slug: recruiting-error-response-structure
- name: Recruiting Job Application Structure
  property_count: 5
  slug: recruiting-job-application-structure
- name: Recruiting Job Posting Structure
  property_count: 9
  slug: recruiting-job-posting-structure
- name: Recruiting Job Requisition Structure
  property_count: 8
  slug: recruiting-job-requisition-structure
- name: Recruiting Prospect Structure
  property_count: 5
  slug: recruiting-prospect-structure
- name: Recruiting Resource Reference Structure
  property_count: 3
  slug: recruiting-resource-reference-structure
- name: Staffing Error Response Structure
  property_count: 2
  slug: staffing-error-response-structure
- name: Staffing Job Change Request Structure
  property_count: 2
  slug: staffing-job-change-request-structure
- name: Staffing Job Change Structure
  property_count: 3
  slug: staffing-job-change-structure
- name: Staffing Job Profile Structure
  property_count: 6
  slug: staffing-job-profile-structure
- name: Staffing One Time Payment Request Structure
  property_count: 2
  slug: staffing-one-time-payment-request-structure
- name: Staffing Organization Assignment Structure
  property_count: 3
  slug: staffing-organization-assignment-structure
- name: Staffing Position Structure
  property_count: 6
  slug: staffing-position-structure
- name: Staffing Resource Reference Structure
  property_count: 3
  slug: staffing-resource-reference-structure
- name: Staffing Termination Request Structure
  property_count: 4
  slug: staffing-termination-request-structure
- name: Talent Certification Structure
  property_count: 6
  slug: talent-certification-structure
- name: Talent Education Entry Structure
  property_count: 5
  slug: talent-education-entry-structure
- name: Talent Error Response Structure
  property_count: 2
  slug: talent-error-response-structure
- name: Talent Job History Entry Structure
  property_count: 6
  slug: talent-job-history-entry-structure
- name: Talent Language Structure
  property_count: 3
  slug: talent-language-structure
- name: Talent Mentorship Structure
  property_count: 5
  slug: talent-mentorship-structure
- name: Talent Resource Reference Structure
  property_count: 3
  slug: talent-resource-reference-structure
- name: Talent Skill Structure
  property_count: 3
  slug: talent-skill-structure
- name: Talent Succession Plan Structure
  property_count: 5
  slug: talent-succession-plan-structure
- name: Talent Talent Profile Structure
  property_count: 8
  slug: talent-talent-profile-structure
- name: Timetracking Error Response Structure
  property_count: 2
  slug: timeTracking-error-response-structure
- name: Timetracking Resource Reference Structure
  property_count: 3
  slug: timeTracking-resource-reference-structure
- name: Timetracking Time Clock Event Request Structure
  property_count: 2
  slug: timeTracking-time-clock-event-request-structure
- name: Timetracking Time Clock Event Structure
  property_count: 5
  slug: timeTracking-time-clock-event-structure
- name: Timetracking Time Entry Request Structure
  property_count: 3
  slug: timeTracking-time-entry-request-structure
- name: Timetracking Time Entry Structure
  property_count: 6
  slug: timeTracking-time-entry-structure
- name: Timetracking Timesheet Structure
  property_count: 7
  slug: timeTracking-timesheet-structure
- name: Workday Structure
  property_count: 0
  slug: workday-structure
- name: Wql Data Source Field Structure
  property_count: 8
  slug: wql-data-source-field-structure
- name: Wql Data Source Structure
  property_count: 5
  slug: wql-data-source-structure
- name: Wql Error Response Structure
  property_count: 2
  slug: wql-error-response-structure
- name: Wql Resource Reference Structure
  property_count: 3
  slug: wql-resource-reference-structure
- name: Wql Wql Query Result Structure
  property_count: 2
  slug: wql-wql-query-result-structure
jsonld:
- class_count: 0
  name: Absencemanagement Context
  property_count: 0
  slug: absenceManagement-context
- class_count: 0
  name: Benefits Context
  property_count: 0
  slug: benefits-context
- class_count: 0
  name: Common Context
  property_count: 0
  slug: common-context
- class_count: 0
  name: Compensation Context
  property_count: 0
  slug: compensation-context
- class_count: 3
  name: context Context
  property_count: 19
  slug: context
- class_count: 0
  name: Financialmanagement Context
  property_count: 0
  slug: financialManagement-context
- class_count: 0
  name: Hcm Context
  property_count: 0
  slug: hcm-context
- class_count: 0
  name: Payroll Context
  property_count: 0
  slug: payroll-context
- class_count: 0
  name: Performancemanagement Context
  property_count: 0
  slug: performanceManagement-context
- class_count: 0
  name: Person Context
  property_count: 0
  slug: person-context
- class_count: 0
  name: Prismanalytics Context
  property_count: 0
  slug: prismAnalytics-context
- class_count: 0
  name: Raas Context
  property_count: 0
  slug: raas-context
- class_count: 0
  name: Recruiting Context
  property_count: 0
  slug: recruiting-context
- class_count: 0
  name: Staffing Context
  property_count: 0
  slug: staffing-context
- class_count: 0
  name: Talent Context
  property_count: 0
  slug: talent-context
- class_count: 0
  name: Timetracking Context
  property_count: 0
  slug: timeTracking-context
- class_count: 0
  name: Wql Context
  property_count: 0
  slug: wql-context
layout: provider
modified: '2026-06-20'
name: Workday
nav: Providers
network: true
overview: 'Workday publishes 46 APIs on the [APIs.io](https://apis.io/) network, including Absence Types API, Accounting API, Benefit Elections API, and 43 more. Tagged areas include Cloud Computing, Enterprise Software, Financial Management, HCM, and Software-as-a-Service.


  The Workday catalog on APIs.io includes 17 JSON-LD contexts and 2 Spectral governance rulesets.


  Workday''s developer surface includes CLI, changelog, authentication, getting-started guide, documentation, developer console, engineering blog, and 68 more developer resources.'
plans:
- name: Workday Plans Pricing
  plan_count: 1
  slug: workday-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Workday Rate Limits
  slug: workday-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Workday API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: workday-jsonschema-spectral-rules
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: Workday API Rules
  rule_count: 17
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 8
  slug: workday-spectral-rules
scopes:
- name: Workday Scopes
  scope_count: 29
  slug: workday-scopes
  summary_line: 29 scopes · authorizationCode
score:
  band: developing
  composite: 51.2
  coverage:
    artifact_dirs: 36
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 33.3
    contract_quality: 72.7
    developer_ergonomics: 44.0
    discoverability: 40.7
    governance: 33.3
    operational_transparency: 39.5
  previous_composite: 51.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 46
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/workday/refs/heads/main/screenshots/workday-2026-06-20T201559.png
security:
- kind: authentication
  name: Workday Authentication
  slug: workday-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Workday Domain Security
  slug: workday-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Workday Trust Center
  slug: workday-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR
slug: workday
tags:
- Cloud Computing
- Enterprise Software
- Financial Management
- HCM
- Software-as-a-Service
use_cases:
- description: Automate new hire onboarding workflows including position assignment, benefits enrollment, and system provisioning.
  name: Employee Onboarding
- description: Model headcount scenarios, track open positions, and align workforce supply with business demand.
  name: Workforce Planning
- description: Streamline employee expense reporting with automated policy enforcement, approval workflows, and reimbursement.
  name: Expense Management
- description: Generate regulatory compliance reports for labor laws, tax requirements, and industry-specific mandates.
  name: Compliance Reporting
- description: Conduct structured performance evaluations with goal tracking, feedback collection, and calibration.
  name: Performance Reviews
- description: Integrate payroll data with third-party systems for tax filing, benefits administration, and general ledger posting.
  name: Payroll Integration
---

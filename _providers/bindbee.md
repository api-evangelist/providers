---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: platform
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.1
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 35
  human_in_the_loop: 0
  name: Bindbee Agentic Access
  operation_count: 151
  slug: bindbee-agentic-access
  summary_line: 151 operations · 35 acting
api_count: 1
apis:
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: Job candidates from connected ATS systems, normalized across Greenhouse, Lever, Workable, Ashby and every other connected ATS.
  name: Bindbee Candidates API
  phrasing_intents:
  - id: listCandidates
    intent: List candidates, optionally for one job
    question: Which candidates are in the connected ATS for a particular job?
  - id: getCandidate
    intent: Get a single candidate record
    question: What does one candidate record look like from the ATS?
  phrasing_ops: 2
  slug: bindbee-candidates-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: Organizational departments from connected HRIS and ATS systems.
  name: Bindbee Departments API
  phrasing_intents:
  - id: listDepartments
    intent: List departments from the HR system
    question: Which departments exist in the connected HRIS?
  phrasing_ops: 1
  slug: bindbee-departments-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: Normalized employee records from connected HRIS systems, including employment, compensation, benefits, groups and reporting hierarchy.
  name: Bindbee Employees API
  phrasing_intents:
  - id: listEmployees
    intent: Page through employees on the short route
    question: Can I page through all employees using the simple /hris/employees route?
  - id: getEmployee
    intent: Get an employee on the short route
    question: Can I look up one employee by id on the simple HRIS employees route?
  phrasing_ops: 2
  slug: bindbee-employees-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: Job listings and requisitions from connected ATS systems.
  name: Bindbee Jobs API
  phrasing_intents:
  - id: listJobs
    intent: List job postings by status
    question: Which job postings are in the connected ATS?
  phrasing_ops: 1
  slug: bindbee-jobs-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: Employee time-off requests and accrued balances from connected HRIS systems.
  name: Bindbee Time Off API
  phrasing_intents:
  - id: get_time_off_list_api_hris_v1_time_off_get
    intent: List time-off requests
    question: Which vacation or leave requests has an employee submitted?
  - id: create_time_off_api_hris_v1_time_off_post
    intent: Submit a time-off request
    question: How do I file a leave request for an employee in the HR system?
  - id: get_create_time_off_meta_api_hris_v1_time_off_meta_post_get
    intent: Get the time-off request schema
    question: What fields does creating a time-off request need for this HRIS?
  - id: get_time_off_by_id_api_hris_v1_time_off__id__get
    intent: Get one time-off request
    question: What are the dates and status of one leave request?
  - id: listTimeOff
    intent: List time off and balances on the short route
    question: Can I get both time-off requests and balances in one call from the simple route?
  phrasing_ops: 5
  slug: bindbee-time-off-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Activity API from Bindbee — 2 operation(s) for activity.
  name: Bindbee Activity API
  phrasing_intents:
  - id: get_activities_api_ats_v1_activities_get
    intent: List candidate activities in the ATS
    question: Which notes, emails and other activities are logged against a candidate in our ATS?
  - id: create_activity_api_ats_v1_activities_post
    intent: Log a new activity on a candidate
    question: How do I add a note or email record to a candidate's history in the ATS?
  - id: get_activity_by_id_api_ats_v1_activities__id__get
    intent: Get one candidate activity by id
    question: What does a single logged ATS activity record contain?
  phrasing_ops: 3
  slug: bindbee-activity-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Application API from Bindbee — 2 operation(s) for application.
  name: Bindbee Application API
  phrasing_intents:
  - id: get_applications_api_ats_v1_applications_get
    intent: List job applications in the ATS
    question: Which applications have been submitted for a given job opening?
  - id: create_application_api_ats_v1_applications_post
    intent: Submit a new job application
    question: How do I push a new application for a candidate into the connected ATS?
  - id: get_application_by_id_api_ats_v1_applications__id__get
    intent: Get one job application by id
    question: What stage is a particular application in right now?
  phrasing_ops: 3
  slug: bindbee-application-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Attachment API from Bindbee — 2 operation(s) for attachment.
  name: Bindbee Attachment API
  phrasing_intents:
  - id: get_attachments_api_ats_v1_attachments_get
    intent: List candidate attachments
    question: Which resumes and files are stored across our ATS?
  - id: create_attachment_api_ats_v1_attachments_post
    intent: Create an attachment record
    question: How do I add a new attachment object through the generic attachments endpoint?
  - id: get_attachment_by_id_api_ats_v1_attachments__id__get
    intent: Get one attachment by id
    question: What metadata comes back for a single attachment?
  phrasing_ops: 3
  slug: bindbee-attachment-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Bank Info API from Bindbee — 2 operation(s) for bank info.
  name: Bindbee Bank Info API
  phrasing_intents:
  - id: get_bank_info_list_api_hris_v1_bank_info_get
    intent: List employee bank account details
    question: Where can I read employees' direct deposit bank accounts from the HRIS?
  - id: get_bank_info_by_id_api_hris_v1_bank_info__id__get
    intent: Get one bank account record
    question: What fields does a single bank info record expose?
  phrasing_ops: 2
  slug: bindbee-bank-info-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Benefit Coverages API from Bindbee — 2 operation(s) for benefit coverages.
  name: Bindbee Benefit Coverages API
  phrasing_intents:
  - id: get_benefit_coverages_api_hris_v1_benefit_coverages_get
    intent: List benefit coverage levels
    question: What coverage options exist under a given benefit?
  - id: get_benefit_coverage_by_id_api_hris_v1_benefit_coverages__id__get
    intent: Get one benefit coverage record
    question: What does one benefit coverage entry include?
  phrasing_ops: 2
  slug: bindbee-benefit-coverages-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Benefits API from Bindbee — 2 operation(s) for benefits.
  name: Bindbee Benefits API
  phrasing_intents:
  - id: get_benefits_api_hris_v1_benefits_get
    intent: List employee benefit enrollments
    question: Which benefits is a given employee enrolled in?
  - id: get_benefit_by_id_api_hris_v1_benefits__id__get
    intent: Get one employee benefit by id
    question: What are the details of one employee's benefit enrollment?
  phrasing_ops: 2
  slug: bindbee-benefits-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Candidate API from Bindbee — 4 operation(s) for candidate.
  name: Bindbee Candidate API
  phrasing_intents:
  - id: get_candidates_api_ats_v1_candidates_get
    intent: Search candidates in the ATS
    question: Can I find a candidate in our ATS by email address?
  - id: create_candidate_api_ats_v1_candidates_post
    intent: Add a new candidate to the ATS
    question: How do I create a candidate profile in the connected ATS?
  - id: get_create_candidate_request_body_api_ats_v1_candidates_create_meta_get
    intent: Get fields required to create a candidate
    question: Which fields does this ATS require before I can create a candidate?
  - id: get_candidate_by_id_api_ats_v1_candidates__id__get
    intent: Get one candidate by id
    question: What profile details are stored for one candidate?
  - id: create_candidate_attachment_api_ats_v1_candidates__candidate_id__attachments_post
    intent: Upload a file to a candidate
    question: How do I upload a resume to a specific candidate?
  phrasing_ops: 5
  slug: bindbee-candidate-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Categories API from Bindbee — 2 operation(s) for categories.
  name: Bindbee Categories API
  phrasing_intents:
  - id: get_lms_categories_api_lms_v1_categories_get
    intent: List learning course categories
    question: What course categories exist in our learning platform?
  - id: get_lms_category_by_id_api_lms_v1_categories__id__get
    intent: Get one learning category
    question: What details are stored for one LMS category?
  phrasing_ops: 2
  slug: bindbee-categories-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Company API from Bindbee — 2 operation(s) for company.
  name: Bindbee Company API
  phrasing_intents:
  - id: get_companies_api_hris_v1_companies_get
    intent: List companies in the HRIS
    question: Which legal entities or companies are set up in the connected HRIS?
  - id: get_company_by_id_api_hris_v1_companies__id__get
    intent: Get one company by id
    question: What information is held for a single company entity?
  phrasing_ops: 2
  slug: bindbee-company-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Compensation API from Bindbee — 2 operation(s) for compensation.
  name: Bindbee Compensation API
  phrasing_intents:
  - id: get_compensations_api_hris_v1_compensations_get
    intent: List employee compensation records
    question: What is a given employee's pay rate history?
  - id: get_compensation_by_id_api_hris_v1_compensations__id__get
    intent: Get one compensation record
    question: What does a single compensation entry include?
  phrasing_ops: 2
  slug: bindbee-compensation-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Completions API from Bindbee — 2 operation(s) for completions.
  name: Bindbee Completions API
  phrasing_intents:
  - id: get_lms_completions_api_lms_v1_completions_get
    intent: List course completions
    question: Who has completed a given training course?
  - id: get_lms_completion_by_id_api_lms_v1_completions__id__get
    intent: Get one course completion
    question: What details are recorded for one course completion?
  phrasing_ops: 2
  slug: bindbee-completions-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Connector API from Bindbee — 8 operation(s) for connector.
  name: Bindbee Connector API
  phrasing_intents:
  - id: get_hris_connectors_api_hris_v1_connectors_get
    intent: List HRIS connectors
    question: Which HR system connections have my customers linked?
  - id: delete_hris_connector_api_hris_v1_connectors__connector_id__delete_delete
    intent: Delete an HRIS connector
    question: How do I disconnect a customer's linked HR system?
  - id: get_ats_connectors_api_ats_v1_connectors_get
    intent: List ATS connectors
    question: Which applicant tracking system connections are linked to my account?
  - id: delete_ats_connector_api_ats_v1_connectors__connector_id__delete_delete
    intent: Delete an ATS connector
    question: How do I unlink a customer's applicant tracking system?
  - id: get_lms_connectors_api_lms_v1_connectors_get
    intent: List LMS connectors
    question: Which learning management system connections are active?
  - id: delete_lms_connector_api_lms_v1_connectors__connector_id__delete_delete
    intent: Delete an LMS connector
    question: How do I remove a linked learning platform connection?
  - id: get_connector_token_api_embedded_v1_connectors_connector_token__temporary_token__get
    intent: Exchange a temporary token for a connector token
    question: After a user finishes the embedded link flow, how do I get the permanent connector token?
  - id: force_resync_connector_api_embedded_v1_connectors_resync_post
    intent: Force a connector to resync
    question: How do I trigger a fresh data sync for a linked account right now?
  phrasing_ops: 8
  slug: bindbee-connector-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Contents API from Bindbee — 2 operation(s) for contents.
  name: Bindbee Contents API
  phrasing_intents:
  - id: get_lms_contents_api_lms_v1_contents_get
    intent: List learning content items
    question: What learning content items belong to a given course?
  - id: get_lms_content_by_id_api_lms_v1_contents__id__get
    intent: Get one learning content item
    question: What details are available for one piece of LMS content?
  phrasing_ops: 2
  slug: bindbee-contents-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Courses API from Bindbee — 2 operation(s) for courses.
  name: Bindbee Courses API
  phrasing_intents:
  - id: get_lms_courses_api_lms_v1_courses_get
    intent: List training courses
    question: Which courses are available in our learning platform?
  - id: get_lms_course_by_id_api_lms_v1_courses__id__get
    intent: Get one training course
    question: What does a single course record include?
  phrasing_ops: 2
  slug: bindbee-courses-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Custom Fields API from Bindbee — 7 operation(s) for custom fields.
  name: Bindbee Custom Fields API
  phrasing_intents:
  - id: create_custom_field_api_v1_custom_fields_post
    intent: Define a new custom field
    question: How do I define a new custom field on a unified model?
  - id: list_custom_fields_api_v1_custom_fields_get
    intent: List custom field definitions
    question: Which custom fields has my organization defined?
  - id: create_custom_field_mapping_api_v1_custom_fields_mapping_post
    intent: Map a custom field to source data
    question: How do I tell a custom field where to read its value from in the source system?
  - id: list_custom_field_mappings_api_v1_custom_fields_mapping_get
    intent: List custom field mappings
    question: Which JMESPath mappings are set up for an integration?
  - id: update_custom_field_mapping_api_v1_custom_fields_mapping__custom_field_mapping_id__patch
    intent: Change a mapping's JMESPath
    question: How do I fix the JMESPath expression on an existing mapping?
  - id: delete_custom_field_mapping_api_v1_custom_fields_mapping__custom_field_mapping_id__delete
    intent: Delete a custom field mapping
    question: How do I remove a mapping without deleting the custom field itself?
  - id: get_raw_data_api_v1_custom_fields_raw_data_get
    intent: Inspect raw upstream data for a model
    question: What does the raw payload from the source system look like before I write a JMESPath?
  - id: preview_custom_field_api_v1_custom_fields_preview_post
    intent: Test a JMESPath before saving a mapping
    question: Can I dry-run a JMESPath expression against real connector data first?
  phrasing_ops: 12
  slug: bindbee-custom-fields-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Department API from Bindbee — 2 operation(s) for department.
  name: Bindbee Department API
  phrasing_intents:
  - id: get_departments_api_ats_v1_departments_get
    intent: List recruiting departments in the ATS
    question: Which departments are set up in our applicant tracking system?
  - id: create_department_api_ats_v1_departments_post
    intent: Create a department in the ATS
    question: How do I add a new department to the recruiting system?
  - id: get_department_by_id_api_ats_v1_departments__id__get
    intent: Get one ATS department
    question: What details are held for one recruiting department?
  phrasing_ops: 3
  slug: bindbee-department-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Dependent Benefits API from Bindbee — 2 operation(s) for dependent benefits.
  name: Bindbee Dependent Benefits API
  phrasing_intents:
  - id: get_dependent_benefits_api_hris_v1_dependent_benefits_get
    intent: List benefits covering dependents
    question: Which benefits cover a particular dependent?
  - id: get_dependent_benefit_by_id_api_hris_v1_dependent_benefits__id__get
    intent: Get one dependent benefit
    question: What details are recorded for one dependent's benefit?
  phrasing_ops: 2
  slug: bindbee-dependent-benefits-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Dependents API from Bindbee — 2 operation(s) for dependents.
  name: Bindbee Dependents API
  phrasing_intents:
  - id: get_dependents_api_hris_v1_dependents_get
    intent: List employees' dependents
    question: Who are the dependents listed for an employee?
  - id: get_dependent_by_id_api_hris_v1_dependents__id__get
    intent: Get one dependent
    question: What information is kept about one dependent?
  phrasing_ops: 2
  slug: bindbee-dependents-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The EEOC API from Bindbee — 2 operation(s) for eeoc.
  name: Bindbee EEOC API
  phrasing_intents:
  - id: get_eeocs_api_ats_v1_eeocs_get
    intent: List EEOC demographic records
    question: Where do I read candidates' EEOC self-identification data?
  - id: create_eeoc_api_ats_v1_eeocs_post
    intent: Create an EEOC record
    question: How do I submit a candidate's EEOC self-identification to the ATS?
  - id: get_eeoc_by_id_api_ats_v1_eeocs__id__get
    intent: Get one EEOC record
    question: What fields are in a single EEOC record?
  phrasing_ops: 3
  slug: bindbee-eeoc-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Employee API from Bindbee — 4 operation(s) for employee.
  name: Bindbee Employee API
  phrasing_intents:
  - id: get_employees_api_hris_v1_employees_get
    intent: Search employees in the HRIS
    question: Who reports to a given manager according to the HR system?
  - id: create_employee_api_hris_v1_employees_post
    intent: Add a new employee to the HRIS
    question: How do I create a new hire record in the connected HR system?
  - id: get_create_employee_request_body_api_hris_v1_employees_create_meta_get
    intent: Get data points needed to add an employee
    question: Which data points does this HR system need before I can add a new employee?
  - id: get_create_employee_meta_api_hris_v1_employees_meta_post_get
    intent: Get the POST employee request schema
    question: What is the exact request schema for the POST employee call?
  - id: get_employee_by_id_api_hris_v1_employees__id__get
    intent: Get one employee by id
    question: What does the HR system hold for one specific employee?
  phrasing_ops: 5
  slug: bindbee-employee-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Employee Payroll Runs API from Bindbee — 3 operation(s) for employee payroll runs.
  name: Bindbee Employee Payroll Runs API
  phrasing_intents:
  - id: get_employee_payroll_runs_api_hris_v1_employee_payroll_runs_get
    intent: List employees' payroll results
    question: What did a specific employee get paid in each payroll run?
  - id: create_employee_payroll_run_api_hris_v1_employee_payroll_runs_post
    intent: Create an employee payroll run record
    question: How do I write an employee's payroll result into the connected system?
  - id: get_create_employee_payroll_run_meta_api_hris_v1_employee_payroll_runs_meta_post_get
    intent: Get the employee payroll run request schema
    question: What request body does creating an employee payroll run expect?
  - id: get_employee_payroll_runs_by_id_api_hris_v1_employee_payroll_runs__id__get
    intent: Get one employee payroll run
    question: What earnings, deductions and taxes are in one employee's payroll run?
  phrasing_ops: 4
  slug: bindbee-employee-payroll-runs-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Employer Benefits API from Bindbee — 2 operation(s) for employer benefits.
  name: Bindbee Employer Benefits API
  phrasing_intents:
  - id: get_employer_benefits_api_hris_v1_employer_benefits_get
    intent: List employer benefit plans
    question: Which benefit plans does the company offer?
  - id: get_employer_benefit_by_id_api_hris_v1_employer_benefits__id__get
    intent: Get one employer benefit plan
    question: What are the details of one employer-offered benefit plan?
  phrasing_ops: 2
  slug: bindbee-employer-benefits-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Employments API from Bindbee — 2 operation(s) for employments.
  name: Bindbee Employments API
  phrasing_intents:
  - id: get_employments_api_hris_v1_employments_get
    intent: List employment records
    question: What job titles and employment history does an employee have?
  - id: get_employment_by_id_api_hris_v1_employments__id__get
    intent: Get one employment record
    question: What does one employment record contain?
  phrasing_ops: 2
  slug: bindbee-employments-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Enrollments API from Bindbee — 2 operation(s) for enrollments.
  name: Bindbee Enrollments API
  phrasing_intents:
  - id: get_lms_enrollments_api_lms_v1_enrollments_get
    intent: List course enrollments
    question: Which learners are enrolled in a given course?
  - id: get_lms_enrollment_by_id_api_lms_v1_enrollments__id__get
    intent: Get one course enrollment
    question: What does one LMS enrollment record include?
  phrasing_ops: 2
  slug: bindbee-enrollments-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Group API from Bindbee — 2 operation(s) for group.
  name: Bindbee Group API
  phrasing_intents:
  - id: get_groups_api_hris_v1_groups_get
    intent: List HRIS groups and teams
    question: Which teams, divisions or cost centers exist in the HR system?
  - id: get_group_by_id_api_hris_v1_groups__id__get
    intent: Get one HRIS group
    question: What details are held for one team or group?
  phrasing_ops: 2
  slug: bindbee-group-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Health Check API from Bindbee — 1 operation(s) for health check.
  name: Bindbee Health Check API
  phrasing_intents:
  - id: org_health_check_api_v1_org_check_post
    intent: Run an organization health check
    question: Is my organization's setup healthy and reachable?
  phrasing_ops: 1
  slug: bindbee-health-check-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Integration API from Bindbee — 3 operation(s) for integration.
  name: Bindbee Integration API
  phrasing_intents:
  - id: get_org_integrations_api_hris_v1_integrations_get
    intent: List enabled HRIS integrations
    question: Which HR system integrations are enabled for my organization?
  - id: get_org_integrations_api_ats_v1_integrations_get
    intent: List enabled ATS integrations
    question: Which applicant tracking system integrations can my customers connect?
  - id: get_org_integrations_api_lms_v1_integrations_get
    intent: List enabled LMS integrations
    question: Which learning management platforms are available as integrations?
  phrasing_ops: 3
  slug: bindbee-integration-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Job API from Bindbee — 2 operation(s) for job.
  name: Bindbee Job API
  phrasing_intents:
  - id: get_jobs_api_ats_v1_jobs_get
    intent: Search job openings in the ATS
    question: Which job openings are currently open in our ATS?
  - id: create_job_api_ats_v1_jobs_post
    intent: Open a new job requisition
    question: How do I create a new job opening in the ATS?
  - id: get_job_by_id_api_ats_v1_jobs__id__get
    intent: Get one job opening by id
    question: What details are stored for one job requisition?
  phrasing_ops: 3
  slug: bindbee-job-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Job Interview Stage API from Bindbee — 2 operation(s) for job interview stage.
  name: Bindbee Job Interview Stage API
  phrasing_intents:
  - id: get_job_interview_stages_api_ats_v1_job_interview_stages_get
    intent: List interview stages for jobs
    question: What interview stages does a job's hiring pipeline have?
  - id: create_job_interview_stage_api_ats_v1_job_interview_stages_post
    intent: Add an interview stage to a pipeline
    question: How do I add a new interview stage to a hiring pipeline?
  - id: get_job_interview_stage_by_id_api_ats_v1_job_interview_stages__id__get
    intent: Get one interview stage
    question: What does a single interview stage record hold?
  phrasing_ops: 3
  slug: bindbee-job-interview-stage-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Link API from Bindbee — 1 operation(s) for link.
  name: Bindbee Link API
  phrasing_intents:
  - id: create_link_token_api_embedded_v1_link_create_link_token_post
    intent: Create a link token for the embedded flow
    question: How do I start the embedded flow so a customer can connect their HR or ATS system?
  phrasing_ops: 1
  slug: bindbee-link-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Location API from Bindbee — 2 operation(s) for location.
  name: Bindbee Location API
  phrasing_intents:
  - id: get_locations_api_hris_v1_locations_get
    intent: List work locations
    question: Which office and work locations are set up in the HR system?
  - id: get_location_by_id_api_hris_v1_locations__id__get
    intent: Get one work location
    question: What address details does one location have?
  phrasing_ops: 2
  slug: bindbee-location-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Lookup API from Bindbee — 2 operation(s) for lookup.
  name: Bindbee Lookup API
  phrasing_intents:
  - id: list_integrations_api_v1_lookup_integrations_get
    intent: Look up integration slugs
    question: Which integration slugs can I use when creating custom field mappings?
  - id: list_models_api_v1_lookup_models_get
    intent: Look up unified model slugs
    question: Which unified models can a custom field be attached to?
  phrasing_ops: 2
  slug: bindbee-lookup-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Offer API from Bindbee — 2 operation(s) for offer.
  name: Bindbee Offer API
  phrasing_intents:
  - id: get_offers_api_ats_v1_offers_get
    intent: List job offers
    question: Which offers have been extended for a given application?
  - id: create_offer_api_ats_v1_offers_post
    intent: Create a job offer
    question: How do I record a new offer for a candidate in the ATS?
  - id: get_offer_by_id_api_ats_v1_offers__id__get
    intent: Get one job offer
    question: What are the details and status of one offer?
  phrasing_ops: 3
  slug: bindbee-offer-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Office API from Bindbee — 2 operation(s) for office.
  name: Bindbee Office API
  phrasing_intents:
  - id: get_offices_api_ats_v1_offices_get
    intent: List recruiting offices
    question: Which offices are set up in the applicant tracking system?
  - id: create_office_api_ats_v1_offices_post
    intent: Create an office in the ATS
    question: How do I add a new office location to the recruiting system?
  - id: get_office_by_id_api_ats_v1_offices__id__get
    intent: Get one ATS office
    question: What details does the ATS keep for one office?
  phrasing_ops: 3
  slug: bindbee-office-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Passthrough API from Bindbee — 1 operation(s) for passthrough.
  name: Bindbee Passthrough API
  phrasing_intents:
  - id: make_passthrough_request_api_v1_passthrough_post
    intent: Send a raw request to the underlying system
    question: How do I call an endpoint of the underlying HR or ATS system that the unified model does not cover?
  phrasing_ops: 1
  slug: bindbee-passthrough-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Pay Groups API from Bindbee — 2 operation(s) for pay groups.
  name: Bindbee Pay Groups API
  phrasing_intents:
  - id: get_pay_groups_api_hris_v1_pay_groups_get
    intent: List pay groups
    question: Which pay groups or pay schedules exist in the HR system?
  - id: get_pay_group_by_id_api_hris_v1_pay_groups__id__get
    intent: Get one pay group
    question: What details are stored for one pay group?
  phrasing_ops: 2
  slug: bindbee-pay-groups-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Payroll Codes API from Bindbee — 2 operation(s) for payroll codes.
  name: Bindbee Payroll Codes API
  phrasing_intents:
  - id: get_payroll_codes_api_hris_v1_payroll_codes_get
    intent: List payroll earning and deduction codes
    question: Which earning, deduction and tax codes are configured in payroll?
  - id: get_payroll_code_by_id_api_hris_v1_payroll_codes__id__get
    intent: Get one payroll code
    question: What does one payroll code represent?
  phrasing_ops: 2
  slug: bindbee-payroll-codes-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Payroll Run Calendars API from Bindbee — 2 operation(s) for payroll run calendars.
  name: Bindbee Payroll Run Calendars API
  phrasing_intents:
  - id: get_payroll_run_calendars_api_hris_v1_payroll_run_calendars_get
    intent: List payroll run calendars
    question: When are upcoming payroll runs scheduled?
  - id: get_payroll_calendar_run_by_id_api_hris_v1_payroll_run_calendars__id__get
    intent: Get one payroll run calendar
    question: What dates does a single payroll calendar entry hold?
  phrasing_ops: 2
  slug: bindbee-payroll-run-calendars-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Payroll Runs API from Bindbee — 2 operation(s) for payroll runs.
  name: Bindbee Payroll Runs API
  phrasing_intents:
  - id: get_payroll_runs_api_hris_v1_payroll_runs_get
    intent: List company payroll runs
    question: Which payroll runs were processed for a pay group?
  - id: get_payroll_run_by_id_api_hris_v1_payroll_runs__id__get
    intent: Get one payroll run
    question: What are the dates and status of one payroll run?
  phrasing_ops: 2
  slug: bindbee-payroll-runs-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Reject Reason API from Bindbee — 2 operation(s) for reject reason.
  name: Bindbee Reject Reason API
  phrasing_intents:
  - id: get_reject_reasons_api_ats_v1_reject_reasons_get
    intent: List candidate rejection reasons
    question: What rejection reasons are configured in the ATS?
  - id: create_reject_reason_api_ats_v1_reject_reasons_post
    intent: Add a rejection reason
    question: How do I add a new rejection reason to the ATS?
  - id: get_reject_reason_by_id_api_ats_v1_reject_reasons__id__get
    intent: Get one rejection reason
    question: What does a single reject reason record contain?
  phrasing_ops: 3
  slug: bindbee-reject-reason-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Remote User API from Bindbee — 2 operation(s) for remote user.
  name: Bindbee Remote User API
  phrasing_intents:
  - id: get_remote_users_api_ats_v1_remote_users_get
    intent: List ATS users such as recruiters
    question: Which recruiters and hiring team members have ATS accounts?
  - id: create_remote_user_api_ats_v1_remote_users_post
    intent: Create an ATS user
    question: How do I add a new recruiter or interviewer account to the ATS?
  - id: get_remote_user_by_id_api_ats_v1_remote_users__id__get
    intent: Get one ATS user
    question: What details does the ATS store for one user?
  phrasing_ops: 3
  slug: bindbee-remote-user-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Scheduled Interview API from Bindbee — 2 operation(s) for scheduled interview.
  name: Bindbee Scheduled Interview API
  phrasing_intents:
  - id: get_scheduled_interviews_api_ats_v1_scheduled_interviews_get
    intent: List scheduled interviews
    question: Which interviews are scheduled for a given application?
  - id: create_scheduled_interview_api_ats_v1_scheduled_interviews_post
    intent: Schedule an interview
    question: How do I put a new interview on the calendar in the ATS?
  - id: get_scheduled_interview_by_id_api_ats_v1_scheduled_interviews__id__get
    intent: Get one scheduled interview
    question: When and with whom is a specific interview scheduled?
  phrasing_ops: 3
  slug: bindbee-scheduled-interview-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Scorecard API from Bindbee — 2 operation(s) for scorecard.
  name: Bindbee Scorecard API
  phrasing_intents:
  - id: get_scorecards_api_ats_v1_scorecards_get
    intent: List interview scorecards
    question: What feedback scorecards were submitted for an application?
  - id: create_scorecard_api_ats_v1_scorecards_post
    intent: Submit an interview scorecard
    question: How do I submit interview feedback as a scorecard?
  - id: get_scorecard_by_id_api_ats_v1_scorecards__id__get
    intent: Get one interview scorecard
    question: What rating and notes are on one scorecard?
  phrasing_ops: 3
  slug: bindbee-scorecard-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Screening Question API from Bindbee — 2 operation(s) for screening question.
  name: Bindbee Screening Question API
  phrasing_intents:
  - id: get_screening_questions_api_ats_v1_screening_questions_get
    intent: List a job's screening questions
    question: What screening questions do applicants answer for a given job?
  - id: create_screening_question_api_ats_v1_screening_questions_post
    intent: Add a screening question
    question: How do I add a screening question to an application form?
  - id: get_screening_question_by_id_api_ats_v1_screening_questions__id__get
    intent: Get one screening question
    question: What options and type does one screening question have?
  phrasing_ops: 3
  slug: bindbee-screening-question-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Skills API from Bindbee — 2 operation(s) for skills.
  name: Bindbee Skills API
  phrasing_intents:
  - id: get_lms_skills_api_lms_v1_skills_get
    intent: List skills in the learning platform
    question: Which skills are tracked in our learning platform?
  - id: get_lms_skill_by_id_api_lms_v1_skills__id__get
    intent: Get one learning skill
    question: What details are stored for one LMS skill?
  phrasing_ops: 2
  slug: bindbee-skills-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Tag API from Bindbee — 2 operation(s) for tag.
  name: Bindbee Tag API
  phrasing_intents:
  - id: get_tags_api_ats_v1_tags_get
    intent: List candidate tags in the ATS
    question: What tags are available for labeling candidates?
  - id: create_tag_api_ats_v1_tags_post
    intent: Create a candidate tag
    question: How do I create a new tag for labeling candidates?
  - id: get_tag_by_id_api_ats_v1_tags__id__get
    intent: Get one ATS tag
    question: What does a single tag record contain?
  phrasing_ops: 3
  slug: bindbee-tag-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Time Off Balance API from Bindbee — 2 operation(s) for time off balance.
  name: Bindbee Time Off Balance API
  phrasing_intents:
  - id: get_time_off_balances_list_api_hris_v1_time_off_balances_get
    intent: List time-off balances
    question: How much vacation or sick leave does an employee have left?
  - id: get_time_off_balance_by_id_api_hris_v1_time_off_balances__id__get
    intent: Get one time-off balance
    question: What does a single leave balance record contain?
  phrasing_ops: 2
  slug: bindbee-time-off-balance-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Timesheet Entry API from Bindbee — 3 operation(s) for timesheet entry.
  name: Bindbee Timesheet Entry API
  phrasing_intents:
  - id: get_timesheet_list_api_hris_v1_timesheet_entry_get
    intent: List timesheet entries
    question: What hours has an employee logged on their timesheet?
  - id: create_timesheet_api_hris_v1_timesheet_entry_post
    intent: Log a timesheet entry
    question: How do I record hours worked for an employee?
  - id: get_create_timesheet_meta_api_hris_v1_timesheet_entry_meta_post_get
    intent: Get the timesheet entry request schema
    question: What fields are required to create a timesheet entry in this HRIS?
  - id: get_timesheet_by_id_api_hris_v1_timesheet_entry__id__get
    intent: Get one timesheet entry
    question: What start and end times are on one timesheet entry?
  phrasing_ops: 4
  slug: bindbee-timesheet-entry-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Users API from Bindbee — 2 operation(s) for users.
  name: Bindbee Users API
  phrasing_intents:
  - id: get_lms_users_api_lms_v1_users_get
    intent: List learners in the LMS
    question: Which learners have accounts in our learning platform?
  - id: get_lms_user_by_id_api_lms_v1_users__id__get
    intent: Get one LMS learner
    question: What profile details does the LMS hold for one learner?
  phrasing_ops: 2
  slug: bindbee-users-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The Webhooks API from Bindbee — 3 operation(s) for webhooks.
  name: Bindbee Webhooks API
  phrasing_intents:
  - id: list_webhooks_api_v1_webhooks_get
    intent: List configured webhooks
    question: Which webhooks are configured for my organization?
  - id: list_webhook_logs_api_v1_webhooks_logs_get
    intent: List webhook delivery attempts
    question: Which webhook deliveries failed recently?
  - id: get_webhook_log_detail_api_v1_webhooks_logs__log_id__get
    intent: Get one webhook delivery's detail
    question: What exact request and response did one webhook delivery produce?
  phrasing_ops: 3
  slug: bindbee-webhooks-api
artifact_total: 114
asyncapis:
- description: ''
  name: Bindbee Webhooks
  slug: bindbee-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bindbee Candidates API
  slug: open-bindbee-candidates-api
- collection_type: open
  name: Bindbee Candidates Departments API
  slug: open-bindbee-departments-api
- collection_type: open
  name: Bindbee Candidates Employees API
  slug: open-bindbee-employees-api
- collection_type: open
  name: Bindbee Candidates Jobs API
  slug: open-bindbee-jobs-api
- collection_type: open
  name: Bindbee Candidates Time Off API
  slug: open-bindbee-time-off-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.bindbee.dev/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/agentic-access/bindbee-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bindbee-agentic-access.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/a2a/bindbee-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/bindbee-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/mcp/bindbee-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bindbee-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/mcp/bindbee-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/bindbee-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/well-known/bindbee-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bindbee-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/conventions/bindbee-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bindbee-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/conventions/bindbee-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/bindbee-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/errors/bindbee-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bindbee-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/data-model/bindbee-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bindbee-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/lifecycle/bindbee-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bindbee-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bindbee.dev/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/conformance/bindbee-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bindbee-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/conformance/bindbee-conformance.yml
  title: ''
  type: Compliance
  url: conformance/bindbee-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/security/bindbee-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bindbee-trust-center.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/packages/bindbee-packages.yml
  title: ''
  type: Packages
  url: packages/bindbee-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/packages/bindbee-packages.yml
  title: ''
  type: SDKs
  url: packages/bindbee-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/components/bindbee-components.yml
  title: ''
  type: Components
  url: components/bindbee-components.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/sandbox/bindbee-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/bindbee-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/asyncapi/bindbee-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bindbee-webhooks.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/overlays/bindbee-unified-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bindbee-unified-api-overlay.yaml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/plans/bindbee-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bindbee-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/rate-limits/bindbee-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bindbee-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/llms/bindbee-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bindbee-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/examples/bindbee-employees-response-example.json
  title: ''
  type: Examples
  url: examples/bindbee-employees-response-example.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/json-schema/bindbee-employees-response-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/bindbee-employees-response-schema.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.bindbee.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bindbee.dev/api-reference/basics/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bindbee.dev/features/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://bindbee.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.bindbee.dev/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bindbee.dev/policies/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bindbee.dev/policies/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:support@bindbee.dev
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unifyXX
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/security/bindbee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bindbee-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/authentication/bindbee-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bindbee-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bindbee
- group: start
  title: ''
  type: Portal
  url: https://bindbee.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bindbee.dev/
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/rules/bindbee-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/vocabulary/bindbee-vocabulary.yaml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.bindbee.dev/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://bindbee.dev/blog/rss.xml
created: '2026-03-16'
description: Bindbee is a unified API for HRIS, Payroll, ATS and LMS integrations. One integration against Bindbee reaches 67+ third-party HR systems — BambooHR, Workday, ADP, Greenhouse, Lever, Personio, Hibob and the rest — through normalized employee, candidate, job, payroll, time-off and course models, so a B2B software company never builds a one-to-one connector again. Each of its customers' end users authorizes their own system through an embedded link flow and is addressed by a connector token; reads are served from Bindbee's synced copy of the upstream system, refreshed every 24 hours by default, with webhooks for sync and data-change events and a passthrough endpoint for anything the unified model does not cover.
examples:
- key_count: 2
  name: Bindbee Candidate Example
  slug: bindbee-candidate-example
- key_count: 2
  name: Bindbee Candidates Response Example
  slug: bindbee-candidates-response-example
- key_count: 2
  name: Bindbee Department Example
  slug: bindbee-department-example
- key_count: 2
  name: Bindbee Departments Response Example
  slug: bindbee-departments-response-example
- key_count: 2
  name: Bindbee Employee Example
  slug: bindbee-employee-example
- key_count: 2
  name: Bindbee Employees Response Example
  slug: bindbee-employees-response-example
- key_count: 2
  name: Bindbee Job Example
  slug: bindbee-job-example
- key_count: 2
  name: Bindbee Jobs Response Example
  slug: bindbee-jobs-response-example
- key_count: 2
  name: Bindbee Time Off Request Example
  slug: bindbee-time-off-request-example
- key_count: 2
  name: Bindbee Time Off Response Example
  slug: bindbee-time-off-response-example
features:
- description: Access employee data from BambooHR, Workday, ADP, and 50+ HRIS systems through one API.
  name: Unified HRIS API
- description: Access job listings and candidates from Greenhouse, Lever, Workable, and other ATS systems.
  name: Unified ATS API
- description: Consistent normalized schema across all connected HR systems.
  name: Data Normalization
- description: Efficient cursor-based pagination for large employee datasets.
  name: Cursor Pagination
- description: Secure per-integration connector tokens for multi-tenant HR data access.
  name: Connector Tokens
- description: Webhooks and polling for real-time HR data synchronization.
  name: Real-Time Sync
finops:
- name: Bindbee Finops
  service_category: API
  slug: bindbee-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bindbee.png
json_schemas:
- name: AtsCandidate
  property_count: 22
  slug: bindbee-candidate
- name: PaginatedResponse[AtsCandidate]
  property_count: 3
  slug: bindbee-candidates-response
- name: AtsDepartment
  property_count: 6
  slug: bindbee-department
- name: PaginatedResponse[AtsDepartment]
  property_count: 3
  slug: bindbee-departments-response
- name: HrisEmployeeResponse
  property_count: 40
  slug: bindbee-employee
- name: PaginatedResponse[HrisEmployeeResponse]
  property_count: 3
  slug: bindbee-employees-response
- name: AtsJob
  property_count: 17
  slug: bindbee-job
- name: PaginatedResponse[AtsJob]
  property_count: 3
  slug: bindbee-jobs-response
- name: HrisTimeOff
  property_count: 14
  slug: bindbee-time-off-request
- name: PaginatedResponse[HrisTimeOff]
  property_count: 3
  slug: bindbee-time-off-response
json_structures:
- name: Bindbee Candidate Structure
  property_count: 7
  slug: bindbee-candidate-structure
- name: Bindbee Candidates Response Structure
  property_count: 1
  slug: bindbee-candidates-response-structure
- name: Bindbee Department Structure
  property_count: 3
  slug: bindbee-department-structure
- name: Bindbee Departments Response Structure
  property_count: 1
  slug: bindbee-departments-response-structure
- name: Bindbee Employee Structure
  property_count: 8
  slug: bindbee-employee-structure
- name: Bindbee Employees Response Structure
  property_count: 3
  slug: bindbee-employees-response-structure
- name: Bindbee Job Structure
  property_count: 6
  slug: bindbee-job-structure
- name: Bindbee Jobs Response Structure
  property_count: 1
  slug: bindbee-jobs-response-structure
- name: Bindbee Time Off Request Structure
  property_count: 6
  slug: bindbee-time-off-request-structure
- name: Bindbee Time Off Response Structure
  property_count: 1
  slug: bindbee-time-off-response-structure
jsonld:
- class_count: 10
  name: Bindbee Context
  property_count: 12
  slug: bindbee-context
layout: provider
mcp_servers:
- description: Bindbee serves a remote MCP server on its own documentation host. It was probed anonymously with a JSON-RPC tools/list call on 2026-09-04 and returned three tools with full inputSchemas. It is a DOCUM
  name: Bindbee Docs
  slug: bindbee-docs
modified: '2026-09-04'
name: Bindbee
nav: Providers
network: true
overview: 'Bindbee publishes 55 APIs on the [APIs.io](https://apis.io/) network, including Candidates API, Departments API, Employees API, and 52 more. Tagged areas include Applicant Tracking, HR Integration, HRIS, Workforce, and Unified API.


  The Bindbee catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Bindbee''s developer surface includes sandbox, code examples, API reference, getting-started guide, pricing, signup flow, support, and 38 more developer resources.'
plans:
- name: Bindbee Plans Pricing
  plan_count: 3
  slug: bindbee-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Bindbee Rate Limits
  slug: bindbee-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Bindbee API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: bindbee-jsonschema-spectral-rules
- effective_rule_count: 71
  extends:
  - spectral:oas
  name: Bindbee API Rules
  rule_count: 30
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 22
  slug: bindbee-spectral-rules
score:
  band: exemplar
  composite: 70.9
  coverage:
    artifact_dirs: 32
    catalog_earned: 80.0
    catalog_earned_first_party: 20.0
    catalog_gap: 35.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 100.0
    contract_governance: 45.5
    contract_quality: 60.7
    developer_ergonomics: 78.6
    discoverability: 75.0
    operational_transparency: 47.4
  previous_composite: 70.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 18.3
      derived: 10
      marker_coverage: 16.4
      total: 61
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 29.4
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/screenshots/bindbee-2026-06-20T173245.png
security:
- kind: authentication
  name: Bindbee Authentication
  slug: bindbee-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Bindbee Domain Security
  slug: bindbee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bindbee Trust Center
  slug: bindbee-trust-center
  summary_line: SOC 2 Type II, ISO 27001, HIPAA, GDPR
slug: bindbee
tags:
- Applicant Tracking
- HR Integration
- HRIS
- Workforce
- Unified API
- Payroll
- LMS
- Employee Data
- Integration
- A2A
use_cases:
- description: Sync employee records from any HRIS into internal apps and directories.
  name: Employee Directory Integration
- description: Trigger onboarding workflows when new employees are added in the HRIS.
  name: Onboarding Automation
- description: Track candidates across ATS stages in unified dashboards.
  name: Recruiting Pipeline Visibility
- description: Move between HRIS providers without rewriting integrations.
  name: HRIS Migration
- description: Aggregate people data from multiple HR systems for workforce analytics.
  name: HR Analytics
website: https://www.bindbee.dev/
---

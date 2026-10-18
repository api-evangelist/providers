---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 785
  human_in_the_loop: 230
  name: Deputy Agentic Access
  operation_count: 1500
  slug: deputy-agentic-access
  summary_line: 1500 operations · 785 acting · 230 human-in-the-loop
api_count: 8
apis:
- description: REST API for managing employees, schedules, timesheets, locations, leave, tasks, and sales metrics in the Deputy workforce management platform. Authentication is handled via OAuth 2.0 or a permanent a
  name: Deputy Public API
  slug: public-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Access Management Employee API from Deputy — 1 operation(s) for access management employee.
  name: Deputy Access Management Employee API
  slug: deputy-access-management-employee-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Access Management Employee Role API from Deputy — 1 operation(s) for access management employee role.
  name: Deputy Access Management Employee Role API
  slug: deputy-access-management-employee-role-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Access Management Employee Role History API from Deputy — 1 operation(s) for access management employee role history.
  name: Deputy Access Management Employee Role History API
  slug: deputy-access-management-employee-role-history-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Access Management Privilege Hierarchy API from Deputy — 1 operation(s) for access management privilege hierarchy.
  name: Deputy Access Management Privilege Hierarchy API
  slug: deputy-access-management-privilege-hierarchy-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Access Management Role API from Deputy — 2 operation(s) for access management role.
  name: Deputy Access Management Role API
  slug: deputy-access-management-role-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Account Stats API from Deputy — 2 operation(s) for account stats.
  name: Deputy Account Stats API
  slug: deputy-account-stats-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Add Entitlement To Employees API from Deputy — 1 operation(s) for add entitlement to employees.
  name: Deputy Add Entitlement To Employees API
  slug: deputy-add-entitlement-to-employees-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the Address resource
  name: Deputy Address API
  slug: deputy-address-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Agreed Hour API from Deputy — 17 operation(s) for agreed hour.
  name: Deputy Agreed Hour API
  slug: deputy-agreed-hour-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The AI Assistant API from Deputy — 1 operation(s) for ai assistant.
  name: Deputy AI Assistant API
  slug: deputy-ai-assistant-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Area Management API from Deputy — 1 operation(s) for area management.
  name: Deputy Area Management API
  slug: deputy-area-management-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Area Profile API from Deputy — 4 operation(s) for area profile.
  name: Deputy Area Profile API
  slug: deputy-area-profile-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Area Rate API from Deputy — 2 operation(s) for area rate.
  name: Deputy Area Rate API
  slug: deputy-area-rate-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Audit Pay Recalculation API from Deputy — 1 operation(s) for audit pay recalculation.
  name: Deputy Audit Pay Recalculation API
  slug: deputy-audit-pay-recalculation-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Availability API from Deputy — 2 operation(s) for availability.
  name: Deputy Availability API
  slug: deputy-availability-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The BidApprove API from Deputy — 1 operation(s) for bidapprove.
  name: Deputy Bid Approve API
  slug: deputy-bidapprove-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Business Details API from Deputy — 1 operation(s) for business details.
  name: Deputy Business Details API
  slug: deputy-business-details-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the Category resource
  name: Deputy Category API
  slug: deputy-category-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: V1 /my/colleague/* endpoints
  name: Deputy Colleague API
  slug: deputy-colleague-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the Comment resource
  name: Deputy Comment API
  slug: deputy-comment-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Communication API from Deputy — 1 operation(s) for communication.
  name: Deputy Communication API
  slug: deputy-communication-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the Company resource
  name: Deputy Company API
  slug: deputy-company-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the CompanyPeriod resource
  name: Deputy Company Period API
  slug: deputy-companyperiod-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Compliance API from Deputy — 21 operation(s) for compliance.
  name: Deputy Compliance API
  slug: deputy-compliance-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Concurrent Leave Cap Config API from Deputy — 1 operation(s) for concurrent leave cap config.
  name: Deputy Concurrent Leave Cap Config API
  slug: deputy-concurrent-leave-cap-config-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: V1 /supervise/config/* endpoints
  name: Deputy Config API
  slug: deputy-config-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the Contact resource
  name: Deputy Contact API
  slug: deputy-contact-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: V1 /my/contactaddress/* endpoints
  name: Deputy Contactaddress API
  slug: deputy-contactaddress-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: V1 /supervise/cost/* endpoints
  name: Deputy Cost API
  slug: deputy-cost-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the Country resource
  name: Deputy Country API
  slug: deputy-country-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Custom Fields API from Deputy — 2 operation(s) for custom fields.
  name: Deputy Custom Fields API
  slug: deputy-custom-fields-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the CustomAppData resource
  name: Deputy Custom App Data API
  slug: deputy-customappdata-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the CustomFieldData resource
  name: Deputy Custom Field Data API
  slug: deputy-customfielddata-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: V1 /my/department/* endpoints
  name: Deputy Department API
  slug: deputy-department-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Departments API from Deputy — 5 operation(s) for departments.
  name: Deputy Departments API
  slug: deputy-departments-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Deputy Reports API from Deputy — 4 operation(s) for deputy reports.
  name: Deputy Deputy Reports API
  slug: deputy-deputy-reports-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Embedded Reports API from Deputy — 16 operation(s) for embedded reports.
  name: Deputy Embedded Reports API
  slug: deputy-embedded-reports-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Employee Agreement API from Deputy — 2 operation(s) for employee agreement.
  name: Deputy Employee Agreement API
  slug: deputy-employee-agreement-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the Employee resource
  name: Deputy Employee API
  slug: deputy-employee-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Employee Data Fix API from Deputy — 4 operation(s) for employee data fix.
  name: Deputy Employee Data Fix API
  slug: deputy-employee-data-fix-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Employee Entitlements API from Deputy — 1 operation(s) for employee entitlements.
  name: Deputy Employee Entitlements API
  slug: deputy-employee-entitlements-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Employee Onboarding API from Deputy — 4 operation(s) for employee onboarding.
  name: Deputy Employee Onboarding API
  slug: deputy-employee-onboarding-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Employee Onboarding Usage API from Deputy — 1 operation(s) for employee onboarding usage.
  name: Deputy Employee Onboarding Usage API
  slug: deputy-employee-onboarding-usage-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Employee Preferences API from Deputy — 1 operation(s) for employee preferences.
  name: Deputy Employee Preferences API
  slug: deputy-employee-preferences-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Employee Profile API from Deputy — 3 operation(s) for employee profile.
  name: Deputy Employee Profile API
  slug: deputy-employee-profile-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Employee Profile History API from Deputy — 1 operation(s) for employee profile history.
  name: Deputy Employee Profile History API
  slug: deputy-employee-profile-history-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Employee Sentiment API from Deputy — 7 operation(s) for employee sentiment.
  name: Deputy Employee Sentiment API
  slug: deputy-employee-sentiment-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Employee Standard Day API from Deputy — 1 operation(s) for employee standard day.
  name: Deputy Employee Standard Day API
  slug: deputy-employee-standard-day-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the EmployeeAgreement resource
  name: Deputy Employee Agreement API
  slug: deputy-employeeagreement-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the EmployeeAgreementAreaRate resource
  name: Deputy Employee Agreement Area Rate API
  slug: deputy-employeeagreementarearate-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the EmployeeAgreementHistory resource
  name: Deputy Employee Agreement History API
  slug: deputy-employeeagreementhistory-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the EmployeeAppraisal resource
  name: Deputy Employee Appraisal API
  slug: deputy-employeeappraisal-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the EmployeeAvailability resource
  name: Deputy Employee Availability API
  slug: deputy-employeeavailability-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the EmployeeContractedHours resource
  name: Deputy Employee Contracted Hours API
  slug: deputy-employeecontractedhours-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the EmployeeContractedHoursShift resource
  name: Deputy Employee Contracted Hours Shift API
  slug: deputy-employeecontractedhoursshift-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the EmployeeHistory resource
  name: Deputy Employee History API
  slug: deputy-employeehistory-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the EmployeePaycycle resource
  name: Deputy Employee Paycycle API
  slug: deputy-employeepaycycle-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the EmployeePaycycleReturn resource
  name: Deputy Employee Paycycle Return API
  slug: deputy-employeepaycyclereturn-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the EmployeeRole resource
  name: Deputy Employee Role API
  slug: deputy-employeerole-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Employees API from Deputy — 14 operation(s) for employees.
  name: Deputy Employees API
  slug: deputy-employees-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the EmployeeSalaryOpunitCosting resource
  name: Deputy Employee Salary Opunit Costing API
  slug: deputy-employeesalaryopunitcosting-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the EmployeeWorkplace resource
  name: Deputy Employee Workplace API
  slug: deputy-employeeworkplace-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Employment Condition API from Deputy — 2 operation(s) for employment condition.
  name: Deputy Employment Condition API
  slug: deputy-employment-condition-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Employment contract level API from Deputy — 4 operation(s) for employment contract level.
  name: Deputy Employment contract level API
  slug: deputy-employment-contract-level-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Employment Contracts API from Deputy — 2 operation(s) for employment contracts.
  name: Deputy Employment Contracts API
  slug: deputy-employment-contracts-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the EmploymentCondition resource
  name: Deputy Employment Condition API
  slug: deputy-employmentcondition-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the EmploymentContract resource
  name: Deputy Employment Contract API
  slug: deputy-employmentcontract-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the EmploymentContractConfig resource
  name: Deputy Employment Contract Config API
  slug: deputy-employmentcontractconfig-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the EmploymentContractLeaveRules resource
  name: Deputy Employment Contract Leave Rules API
  slug: deputy-employmentcontractleaverules-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: V1 /supervise/empshiftinfo/* endpoints
  name: Deputy Empshiftinfo API
  slug: deputy-empshiftinfo-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Entitlement Remediation API from Deputy — 3 operation(s) for entitlement remediation.
  name: Deputy Entitlement Remediation API
  slug: deputy-entitlement-remediation-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the Event resource
  name: Deputy Event API
  slug: deputy-event-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: V1 /my/feed/* endpoints
  name: Deputy Feed API
  slug: deputy-feed-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The File API from Deputy — 1 operation(s) for file.
  name: Deputy File API
  slug: deputy-file-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the Geo resource
  name: Deputy Geo API
  slug: deputy-geo-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Get a Flag Record API from Deputy — 1 operation(s) for get a flag record.
  name: Deputy Get a Flag Record API
  slug: deputy-get-a-flag-record-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Get all visible employee roles API from Deputy — 1 operation(s) for get all visible employee roles.
  name: Deputy Get all visible employee roles API
  slug: deputy-get-all-visible-employee-roles-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Get all visible employee roles include advisor API from Deputy — 1 operation(s) for get all visible employee roles include advisor.
  name: Deputy Get all visible employee roles include advisor API
  slug: deputy-get-all-visible-employee-roles-include-advisor-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Get Business Setting API from Deputy — 1 operation(s) for get business setting.
  name: Deputy Get Business Setting API
  slug: deputy-get-business-setting-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Get Business Setting Template API from Deputy — 1 operation(s) for get business setting template.
  name: Deputy Get Business Setting Template API
  slug: deputy-get-business-setting-template-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Get Employee Role Ids For Privilege Names API from Deputy — 1 operation(s) for get employee role ids for privilege names.
  name: Deputy Get Employee Role Ids For Privilege Names API
  slug: deputy-get-employee-role-ids-for-privilege-names-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Get Employee Role Ids with 2FA Enforced API from Deputy — 1 operation(s) for get employee role ids with 2fa enforced.
  name: Deputy Get Employee Role Ids with 2FA Enforced API
  slug: deputy-get-employee-role-ids-with-2fa-enforced-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Get Employees Entitled To Leave rule API from Deputy — 1 operation(s) for get employees entitled to leave rule.
  name: Deputy Get Employees Entitled To Leave rule API
  slug: deputy-get-employees-entitled-to-leave-rule-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: V1 /supervise/get-roster-timesheet/* endpoints
  name: Deputy Get Roster Timesheet API
  slug: deputy-get-roster-timesheet-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: V1 /my/getrecommendation/* endpoints
  name: Deputy Getrecommendation API
  slug: deputy-getrecommendation-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Hr API from Deputy — 4 operation(s) for hr.
  name: Deputy Hr API
  slug: deputy-hr-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Internal - Do not use API from Deputy — 2 operation(s) for internal - do not use.
  name: Deputy Internal - Do not use API
  slug: deputy-internal-do-not-use-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the Journal resource
  name: Deputy Journal API
  slug: deputy-journal-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the Kiosk resource
  name: Deputy Kiosk API
  slug: deputy-kiosk-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Labor Model Rule API from Deputy — 6 operation(s) for labor model rule.
  name: Deputy Labor Model Rule API
  slug: deputy-labor-model-rule-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Leave Absence API from Deputy — 1 operation(s) for leave absence.
  name: Deputy Leave Absence API
  slug: deputy-leave-absence-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Leave Accrual API from Deputy — 2 operation(s) for leave accrual.
  name: Deputy Leave Accrual API
  slug: deputy-leave-accrual-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: V1 /my/leave/* endpoints
  name: Deputy Leave API
  slug: deputy-leave-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Leave Audit Log API from Deputy — 1 operation(s) for leave audit log.
  name: Deputy Leave Audit Log API
  slug: deputy-leave-audit-log-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Leave Balance API from Deputy — 3 operation(s) for leave balance.
  name: Deputy Leave Balance API
  slug: deputy-leave-balance-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Leave Config API from Deputy — 1 operation(s) for leave config.
  name: Deputy Leave Config API
  slug: deputy-leave-config-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Leave Entitlements API from Deputy — 4 operation(s) for leave entitlements.
  name: Deputy Leave Entitlements API
  slug: deputy-leave-entitlements-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Leave Extension API from Deputy — 1 operation(s) for leave extension.
  name: Deputy Leave Extension API
  slug: deputy-leave-extension-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Leave Feature Set API from Deputy — 3 operation(s) for leave feature set.
  name: Deputy Leave Feature Set API
  slug: deputy-leave-feature-set-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Leave Location Settings API from Deputy — 1 operation(s) for leave location settings.
  name: Deputy Leave Location Settings API
  slug: deputy-leave-location-settings-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Leave Migration API from Deputy — 6 operation(s) for leave migration.
  name: Deputy Leave Migration API
  slug: deputy-leave-migration-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Leave Non Working Days API from Deputy — 1 operation(s) for leave non working days.
  name: Deputy Leave Non Working Days API
  slug: deputy-leave-non-working-days-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Leave Pay Rules API from Deputy — 1 operation(s) for leave pay rules.
  name: Deputy Leave Pay Rules API
  slug: deputy-leave-pay-rules-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Leave Reference Period API from Deputy — 1 operation(s) for leave reference period.
  name: Deputy Leave Reference Period API
  slug: deputy-leave-reference-period-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Leave Request API from Deputy — 5 operation(s) for leave request.
  name: Deputy Leave Request API
  slug: deputy-leave-request-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Leave Rules API from Deputy — 1 operation(s) for leave rules.
  name: Deputy Leave Rules API
  slug: deputy-leave-rules-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the LeaveAccrual resource
  name: Deputy Leave Accrual API
  slug: deputy-leaveaccrual-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the LeavePayLine resource
  name: Deputy Leave Pay Line API
  slug: deputy-leavepayline-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the LeaveRules resource
  name: Deputy Leave Rules API
  slug: deputy-leaverules-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The List Flag Records API from Deputy — 1 operation(s) for list flag records.
  name: Deputy List Flag Records API
  slug: deputy-list-flag-records-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: V1 /my/location/* endpoints
  name: Deputy Location API
  slug: deputy-location-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Location Profile API from Deputy — 5 operation(s) for location profile.
  name: Deputy Location Profile API
  slug: deputy-location-profile-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Location Setting API from Deputy — 2 operation(s) for location setting.
  name: Deputy Location Setting API
  slug: deputy-location-setting-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Locations API from Deputy — 8 operation(s) for locations.
  name: Deputy Locations API
  slug: deputy-locations-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: '# All about "Me" This set of API endpoints allow you to retrieve data about the authenticated user the API token relates too. You can find information out such as locations the user is able to work, t'
  name: Deputy Logged in User Details API
  slug: deputy-logged-in-user-details-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Management API from Deputy — 10 operation(s) for management.
  name: Deputy Management API
  slug: deputy-management-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Me Tab API from Deputy — 1 operation(s) for me tab.
  name: Deputy Me Tab API
  slug: deputy-me-tab-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: V1 /my/memo/* endpoints
  name: Deputy Memo API
  slug: deputy-memo-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: V1 /supervise/metric/* endpoints
  name: Deputy Metric API
  slug: deputy-metric-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Metrics API from Deputy — 4 operation(s) for metrics.
  name: Deputy Metrics API
  slug: deputy-metrics-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The NEW - Shift Suggestions API from Deputy — 1 operation(s) for new - shift suggestions.
  name: Deputy NEW - Shift Suggestions API
  slug: deputy-new-shift-suggestions-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: V1 /my/notification/* endpoints
  name: Deputy Notification API
  slug: deputy-notification-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: V1 /my/nps/* endpoints
  name: Deputy Nps API
  slug: deputy-nps-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Onboarding Dashboard API from Deputy — 2 operation(s) for onboarding dashboard.
  name: Deputy Onboarding Dashboard API
  slug: deputy-onboarding-dashboard-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Onboarding Embed API from Deputy — 2 operation(s) for onboarding embed.
  name: Deputy Onboarding Embed API
  slug: deputy-onboarding-embed-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Onboarding Gamification API from Deputy — 2 operation(s) for onboarding gamification.
  name: Deputy Onboarding Gamification API
  slug: deputy-onboarding-gamification-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Onboarding Route API from Deputy — 1 operation(s) for onboarding route.
  name: Deputy Onboarding Route API
  slug: deputy-onboarding-route-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the OperationalUnit resource
  name: Deputy Operational Unit API
  slug: deputy-operationalunit-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Partner Employees API from Deputy — 2 operation(s) for partner employees.
  name: Deputy Partner Employees API
  slug: deputy-partner-employees-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Pay Calendars API from Deputy — 7 operation(s) for pay calendars.
  name: Deputy Pay Calendars API
  slug: deputy-pay-calendars-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Pay Comparison API from Deputy — 7 operation(s) for pay comparison.
  name: Deputy Pay Comparison API
  slug: deputy-pay-comparison-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Pay Rates API from Deputy — 2 operation(s) for pay rates.
  name: Deputy Pay Rates API
  slug: deputy-pay-rates-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the PayPeriod resource
  name: Deputy Pay Period API
  slug: deputy-payperiod-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Payroll Export Template API from Deputy — 2 operation(s) for payroll export template.
  name: Deputy Payroll Export Template API
  slug: deputy-payroll-export-template-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Payroll Mobile API from Deputy — 1 operation(s) for payroll mobile.
  name: Deputy Payroll Mobile API
  slug: deputy-payroll-mobile-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Payroll User Authorization Code API from Deputy — 1 operation(s) for payroll user authorization code.
  name: Deputy Payroll User Authorization Code API
  slug: deputy-payroll-user-authorization-code-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the PayRules resource
  name: Deputy Pay Rules API
  slug: deputy-payrules-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The People API from Deputy — 2 operation(s) for people.
  name: Deputy People API
  slug: deputy-people-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Permission API from Deputy — 3 operation(s) for permission.
  name: Deputy Permission API
  slug: deputy-permission-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: V1 /my/photo/* endpoints
  name: Deputy Photo API
  slug: deputy-photo-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Plan Downgrade Job API from Deputy — 1 operation(s) for plan downgrade job.
  name: Deputy Plan Downgrade Job API
  slug: deputy-plan-downgrade-job-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: V1 /my/pref/* endpoints
  name: Deputy Pref API
  slug: deputy-pref-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Product Subscription API from Deputy — 1 operation(s) for product subscription.
  name: Deputy Product Subscription API
  slug: deputy-product-subscription-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The ProductAddOns API from Deputy — 1 operation(s) for productaddons.
  name: Deputy Product Add Ons API
  slug: deputy-productaddons-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the PublicHoliday resource
  name: Deputy Public Holiday API
  slug: deputy-publicholiday-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The PublishShifts API from Deputy — 3 operation(s) for publishshifts.
  name: Deputy Publish Shifts API
  slug: deputy-publishshifts-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Reaction API from Deputy — 2 operation(s) for reaction.
  name: Deputy Reaction API
  slug: deputy-reaction-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Remediation API from Deputy — 1 operation(s) for remediation.
  name: Deputy Remediation API
  slug: deputy-remediation-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Resource API API from Deputy — 56 operation(s) for resource api.
  name: Deputy Resource API
  slug: deputy-resource-api-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: V1 /my/roster/* endpoints
  name: Deputy Roster API
  slug: deputy-roster-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the RosterOpen resource
  name: Deputy Roster Open API
  slug: deputy-rosteropen-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Rosters API from Deputy — 5 operation(s) for rosters.
  name: Deputy Rosters API
  slug: deputy-rosters-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the RosterSwap resource
  name: Deputy Roster Swap API
  slug: deputy-rosterswap-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the RosterTemplate resource
  name: Deputy Roster Template API
  slug: deputy-rostertemplate-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Sales API from Deputy — 2 operation(s) for sales.
  name: Deputy Sales API
  slug: deputy-sales-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the SalesData resource
  name: Deputy Sales Data API
  slug: deputy-salesdata-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Save Business Setting Config API from Deputy — 1 operation(s) for save business setting config.
  name: Deputy Save Business Setting Config API
  slug: deputy-save-business-setting-config-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Schedule Agent API from Deputy — 2 operation(s) for schedule agent.
  name: Deputy Schedule Agent API
  slug: deputy-schedule-agent-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the Schedule resource
  name: Deputy Schedule API
  slug: deputy-schedule-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The ScheduleConsent API from Deputy — 1 operation(s) for scheduleconsent.
  name: Deputy Schedule Consent API
  slug: deputy-scheduleconsent-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The ScheduleFilters API from Deputy — 1 operation(s) for schedulefilters.
  name: Deputy Schedule Filters API
  slug: deputy-schedulefilters-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The ScheduleTemplate API from Deputy — 3 operation(s) for scheduletemplate.
  name: Deputy Schedule Template API
  slug: deputy-scheduletemplate-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: V1 /supervise/sendpushermessage/* endpoints
  name: Deputy Sendpushermessage API
  slug: deputy-sendpushermessage-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: V1 /supervise/sendsms/* endpoints
  name: Deputy Sendsms API
  slug: deputy-sendsms-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the Session resource
  name: Deputy Session API
  slug: deputy-session-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Session History API from Deputy — 1 operation(s) for session history.
  name: Deputy Session History API
  slug: deputy-session-history-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: V1 /my/setup/* endpoints
  name: Deputy Setup API
  slug: deputy-setup-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Shift Offers API from Deputy — 3 operation(s) for shift offers.
  name: Deputy Shift Offers API
  slug: deputy-shift-offers-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Shifts API from Deputy — 34 operation(s) for shifts.
  name: Deputy Shifts API
  slug: deputy-shifts-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Shifts consent check API from Deputy — 1 operation(s) for shifts consent check.
  name: Deputy Shifts consent check API
  slug: deputy-shifts-consent-check-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the ShiftTemplate resource
  name: Deputy Shift Template API
  slug: deputy-shifttemplate-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the SmsLog resource
  name: Deputy Sms Log API
  slug: deputy-smslog-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the State resource
  name: Deputy State API
  slug: deputy-state-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the StressProfile resource
  name: Deputy Stress Profile API
  slug: deputy-stressprofile-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Swaps API from Deputy — 6 operation(s) for swaps.
  name: Deputy Swaps API
  slug: deputy-swaps-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the SystemUsageBalance resource
  name: Deputy System Usage Balance API
  slug: deputy-systemusagebalance-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the SystemUsageTracking resource
  name: Deputy System Usage Tracking API
  slug: deputy-systemusagetracking-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: V1 /my/task/* endpoints
  name: Deputy Task API
  slug: deputy-task-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the TaskGroup resource
  name: Deputy Task Group API
  slug: deputy-taskgroup-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the TaskGroupSetup resource
  name: Deputy Task Group Setup API
  slug: deputy-taskgroupsetup-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the TaskOpunitConfig resource
  name: Deputy Task Opunit Config API
  slug: deputy-taskopunitconfig-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the TaskSetup resource
  name: Deputy Task Setup API
  slug: deputy-tasksetup-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the Team resource
  name: Deputy Team API
  slug: deputy-team-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Tenant User Referral API API from Deputy — 1 operation(s) for tenant user referral api.
  name: Deputy Tenant User Referral API
  slug: deputy-tenant-user-referral-api-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: V1 /my/timesheet/* endpoints
  name: Deputy Timesheet API
  slug: deputy-timesheet-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Timesheet Approval API from Deputy — 31 operation(s) for timesheet approval.
  name: Deputy Timesheet Approval API
  slug: deputy-timesheet-approval-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Timesheet Attestation API from Deputy — 4 operation(s) for timesheet attestation.
  name: Deputy Timesheet Attestation API
  slug: deputy-timesheet-attestation-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Timesheet Batch Forecast API from Deputy — 1 operation(s) for timesheet batch forecast.
  name: Deputy Timesheet Batch Forecast API
  slug: deputy-timesheet-batch-forecast-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Timesheet Export API from Deputy — 4 operation(s) for timesheet export.
  name: Deputy Timesheet Export API
  slug: deputy-timesheet-export-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Timesheet Export List Timesheets API from Deputy — 1 operation(s) for timesheet export list timesheets.
  name: Deputy Timesheet Export List Timesheets API
  slug: deputy-timesheet-export-list-timesheets-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Timesheet Get Pay Return Rates API from Deputy — 1 operation(s) for timesheet get pay return rates.
  name: Deputy Timesheet Get Pay Return Rates API
  slug: deputy-timesheet-get-pay-return-rates-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Timesheet Get Pay Suggestion API from Deputy — 1 operation(s) for timesheet get pay suggestion.
  name: Deputy Timesheet Get Pay Suggestion API
  slug: deputy-timesheet-get-pay-suggestion-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the TimesheetExport resource
  name: Deputy Timesheet Export API
  slug: deputy-timesheetexport-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the TimesheetPayForecast resource
  name: Deputy Timesheet Pay Forecast API
  slug: deputy-timesheetpayforecast-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the TimesheetPayReturn resource
  name: Deputy Timesheet Pay Return API
  slug: deputy-timesheetpayreturn-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the TimesheetPayReturnDetail resource
  name: Deputy Timesheet Pay Return Detail API
  slug: deputy-timesheetpayreturndetail-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The TimesheetQuestionRemediation API from Deputy — 3 operation(s) for timesheetquestionremediation.
  name: Deputy Timesheet Question Remediation API
  slug: deputy-timesheetquestionremediation-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Timesheets API from Deputy — 12 operation(s) for timesheets.
  name: Deputy Timesheets API
  slug: deputy-timesheets-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Timesheets Export API from Deputy — 1 operation(s) for timesheets export.
  name: Deputy Timesheets Export API
  slug: deputy-timesheets-export-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: V1 /my/todo/* endpoints
  name: Deputy Todo API
  slug: deputy-todo-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: V1 /my/token/* endpoints
  name: Deputy Token API
  slug: deputy-token-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: V1 /my/training/* endpoints
  name: Deputy Training API
  slug: deputy-training-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the TrainingModule resource
  name: Deputy Training Module API
  slug: deputy-trainingmodule-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the TrainingRecord resource
  name: Deputy Training Record API
  slug: deputy-trainingrecord-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: V1 /my/unavail/* endpoints
  name: Deputy Unavail API
  slug: deputy-unavail-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Update a Flag Record API from Deputy — 1 operation(s) for update a flag record.
  name: Deputy Update a Flag Record API
  slug: deputy-update-a-flag-record-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The User API from Deputy — 1 operation(s) for user.
  name: Deputy User API
  slug: deputy-user-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The User info API from Deputy — 1 operation(s) for user info.
  name: Deputy User info API
  slug: deputy-user-info-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The User SSO Link API from Deputy — 1 operation(s) for user sso link.
  name: Deputy User SSO Link API
  slug: deputy-user-sso-link-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Utility request API from Deputy — 2 operation(s) for utility request.
  name: Deputy Utility request API
  slug: deputy-utility-request-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Weather API from Deputy — 1 operation(s) for weather.
  name: Deputy Weather API
  slug: deputy-weather-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the Webhook resource
  name: Deputy Webhook API
  slug: deputy-webhook-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Webhook Triggers API from Deputy — 2 operation(s) for webhook triggers.
  name: Deputy Webhook Triggers API
  slug: deputy-webhook-triggers-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: The Webhooks API from Deputy — 1 operation(s) for webhooks.
  name: Deputy Webhooks API
  slug: deputy-webhooks-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: V1 /my/widget/* endpoints
  name: Deputy Widget API
  slug: deputy-widget-api
- baseURL: https://{install}.{geo}.deputy.com/api/v1
  baseurl_source: declared
  description: Operations on the CustomField resource
  name: Deputy Custom Field API
  slug: deputy-custom-field-api
artifact_total: 253
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deputy/refs/heads/main/capabilities/deputy-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/deputy-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/deputy/refs/heads/main/agentic-access/deputy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/deputy-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/deputy/refs/heads/main/rules/deputy-rules.yml
  title: ''
  type: Spectral
  url: rules/deputy-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/deputy/refs/heads/main/json-ld/deputy-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/deputy-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/deputy/refs/heads/main/vocabulary/deputy-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/deputy-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/deputy/refs/heads/main/data-model/deputy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/deputy-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.deputy.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/deputy/refs/heads/main/errors/deputy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/deputy-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/deputy/refs/heads/main/conformance/deputy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/deputy-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/deputy/refs/heads/main/llms/deputy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deputy-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/deputy/refs/heads/main/well-known/deputy-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/deputy-status-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/deputy/refs/heads/main/well-known/deputy-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/deputy-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/deputy/refs/heads/main/well-known/deputy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deputy-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deputy/refs/heads/main/hosts/deputy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deputy-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/deputy/refs/heads/main/integrations/deputy-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/deputy-integration-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deputy/refs/heads/main/vendors/deputy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deputy-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.deputy.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.deputy.com/press
- group: other
  title: ''
  type: Leadership
  url: https://www.deputy.com/about/leadership
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/deputy/refs/heads/main/scopes/deputy-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/deputy-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/deputy/refs/heads/main/authentication/deputy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/deputy-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/deputy/refs/heads/main/security/deputy-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/deputy-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/deputy/refs/heads/main/security/deputy-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/deputy-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/deputy/refs/heads/main/security/deputy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deputy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.deputy.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.deputy.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.deputy.com/docs/getting-started-with-the-deputy-api
- group: auth
  title: ''
  type: Authentication
  url: https://developer.deputy.com/docs/using-oauth-20
- group: commercial
  title: ''
  type: Pricing
  url: https://www.deputy.com/pricing
- group: start
  title: ''
  type: Login
  url: https://once.deputy.com/login/
- group: operate
  title: ''
  type: Support
  url: https://help.deputy.com/
- group: company
  title: ''
  type: Blog
  url: https://www.deputy.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.deputy.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.deputy.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.deputy.com/terms-of-service
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deputydev
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/deputyapp
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.deputy.com/llms.txt
created: '2026-05-11'
description: Deputy is an API-first workforce management platform that handles employee scheduling, time and attendance tracking, timesheets, leave management, task delegation, and team communications for businesses with hourly workers. The platform integrates with payroll, HR, and point of sale systems and exposes most of its product surface area via a public REST API. The Deputy API uses OAuth 2.0 or permanent token authentication and provides JSON endpoints for employees, schedules, timesheets, locations, sales metrics, and more.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deputy.png
json_schemas:
- name: AddNewWorkplaceRequest
  property_count: 11
  slug: deputy-add-new-workplace-request
- name: AddanemployeeRequest
  property_count: 10
  slug: deputy-addanemployee-request
- name: AddleaveforaemployeeRequest
  property_count: 6
  slug: deputy-addleaveforaemployee-request
- name: CopyRequestCopyRequestData
  property_count: 7
  slug: deputy-copy-request-copy-request-data
- name: CreateaDepartmentRequest
  property_count: 7
  slug: deputy-createa-department-request
- name: CreateamemoRequest
  property_count: 5
  slug: deputy-createamemo-request
- name: CustomFieldData
  property_count: 133
  slug: deputy-custom-field-data
- name: EmployeeAgreement
  property_count: 32
  slug: deputy-employee-agreement
- name: Employee
  property_count: 49
  slug: deputy-employee
- name: HrExportExportHrBulkDataResponse
  property_count: 3
  slug: deputy-hr-export-export-hr-bulk-data-response
- name: HrExportExportHrDataResponse
  property_count: 2
  slug: deputy-hr-export-export-hr-data-response
- name: HrExportExportHrPayDetailsDataResponse
  property_count: 2
  slug: deputy-hr-export-export-hr-pay-details-data-response
- name: PayComparisonSubmitReportRequest
  property_count: 14
  slug: deputy-pay-comparison-submit-report-request
- name: PayRules
  property_count: 38
  slug: deputy-pay-rules
- name: Roster
  property_count: 39
  slug: deputy-roster
- name: SearchforEmploymentContractLeaveRulesRequest
  property_count: 1
  slug: deputy-searchfor-employment-contract-leave-rules-request
- name: SearchforacustomfielddataentryRequest
  property_count: 1
  slug: deputy-searchforacustomfielddataentry-request
- name: SearchforanEmployeeAgreementHistoryRequest
  property_count: 1
  slug: deputy-searchforan-employee-agreement-history-request
- name: SearchforanEmployeeAvailabilityRequest
  property_count: 1
  slug: deputy-searchforan-employee-availability-request
- name: SearchforanEmploymentConditionRequest
  property_count: 1
  slug: deputy-searchforan-employment-condition-request
- name: SearchforanEmploymentContractRequest
  property_count: 1
  slug: deputy-searchforan-employment-contract-request
- name: SetawardforemployeeRequest
  property_count: 3
  slug: deputy-setawardforemployee-request
- name: Timesheet model
  property_count: 50
  slug: deputy-tenanttimesheetv2model-timesheet
- name: Timesheet
  property_count: 63
  slug: deputy-timesheet
- name: UserInfoGetResponse
  property_count: 2
  slug: deputy-user-info-get-response
- name: Area profile
  property_count: 18
  slug: deputy-v2model-area-profile
- name: Employment Contracts
  property_count: 16
  slug: deputy-v2model-employment-contracts
- name: Leave Request
  property_count: 19
  slug: deputy-v2model-leave-request
jsonld:
- class_count: 120
  name: Deputy Context
  property_count: 670
  slug: deputy-context
layout: provider
modified: '2026-05-11'
name: Deputy
nav: Providers
network: true
overview: 'Deputy publishes 217 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access Management Employee API, Access Management Employee Role API, Access Management Employee Role History API, and 214 more. Tagged areas include Workforce Management, Employee Scheduling, Time and Attendance, Timesheets, and Human Resources.


  The Deputy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Deputy''s developer surface includes authentication, getting-started guide, pricing, support, engineering blog, and 33 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Deputy API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 2
  slug: deputy-rules
scopes:
- name: Deputy Scopes
  scope_count: 1
  slug: deputy-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 56.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 33.0
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 60.0
    developer_ergonomics: 28.6
    discoverability: 82.1
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 23.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 216
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 41.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 100.0
screenshot: https://raw.githubusercontent.com/api-evangelist/deputy/refs/heads/main/screenshots/deputy-2026-06-20T180004.png
security:
- kind: authentication
  name: Deputy Authentication
  slug: deputy-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Deputy Domain Security
  slug: deputy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Deputy Vulnerability Disclosure
  slug: deputy-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Deputy Trust Center
  slug: deputy-trust-center
  summary_line: SOC 2, ISO 27001
slug: deputy
tags:
- Workforce Management
- Employee Scheduling
- Time and Attendance
- Timesheets
- Human Resources
- Shift Planning
- Australia
- Scheduling
website: https://www.deputy.com
---

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
  band: agent-native
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
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 225
  human_in_the_loop: 5
  name: Deel Com Agentic Access
  operation_count: 484
  slug: deel-com-agentic-access
  summary_line: 484 operations · 225 acting · 5 human-in-the-loop
api_count: 9
apis:
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Gross-to-net payroll adjustments — bonuses, deductions, one-time payments
  name: Deel Adjustments API
  slug: deel-com-adjustments-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Candidate records and resume attachments
  name: Deel Candidates API
  slug: deel-com-candidates-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: IC and EOR contract list and detail
  name: Deel Contracts API
  slug: deel-com-contracts-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Device provisioning and equipment lifecycle
  name: Deel IT API
  slug: deel-com-deel-it-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Payroll cycles and events for Global Payroll legal entities
  name: Deel Global Payroll API
  slug: deel-com-global-payroll-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Global Payroll employee hiring
  name: Deel GP Hiring API
  slug: deel-com-gp-hiring-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Visas, work permits, immigration case management
  name: Deel Immigration API
  slug: deel-com-immigration-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Countries, currencies, job titles, seniority levels, time-off types
  name: Deel Lookups API
  slug: deel-com-lookups-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Manager directory for the organization
  name: Deel Managers API
  slug: deel-com-managers-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Milestone-based contract deliverables
  name: Deel Milestones API
  slug: deel-com-milestones-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Organization profile, child organizations, structure, departments, groups
  name: Deel Organizations API
  slug: deel-com-organizations-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Employee payslips
  name: Deel Payslips API
  slug: deel-com-payslips-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: US paystubs
  name: Deel Paystubs API
  slug: deel-com-paystubs-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Unified directory across IC, EOR, and direct employees
  name: Deel People API
  slug: deel-com-people-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: KYC and AML background screenings
  name: Deel Screenings API
  slug: deel-com-screenings-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Time tracking shifts for Global Payroll employees
  name: Deel Time Tracking API
  slug: deel-com-time-tracking-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Submit, approve, and manage contractor timesheets
  name: Deel Timesheets API
  slug: deel-com-timesheets-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Create, list, update, and delete webhook subscriptions
  name: Deel Webhooks API
  slug: deel-com-webhooks-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The subpackage_employees API from Deel — 1 operation(s) for subpackage_employees.
  name: Deel Subpackage Employees API
  slug: deel-com-subpackage-employees-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The subpackage_enrollments API from Deel — 1 operation(s) for subpackage_enrollments.
  name: Deel Subpackage Enrollments API
  slug: deel-com-subpackage-enrollments-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The subpackage_payroll API from Deel — 2 operation(s) for subpackage_payroll.
  name: Deel Subpackage Payroll API
  slug: deel-com-subpackage-payroll-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The subpackage_paystubs API from Deel — 1 operation(s) for subpackage_paystubs.
  name: Deel Subpackage Paystubs API
  slug: deel-com-subpackage-paystubs-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The subpackage_plans401K API from Deel — 5 operation(s) for subpackage_plans401k.
  name: Deel Subpackage Plans401 K API
  slug: deel-com-subpackage-plans401k-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The subpackage_serviceProviderConfig API from Deel — 1 operation(s) for subpackage_serviceproviderconfig.
  name: Deel Subpackage Service Provider Config API
  slug: deel-com-subpackage-serviceproviderconfig-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The accounting API from Deel — 7 operation(s) for accounting.
  name: Deel Accounting API
  slug: deel-com-accounting-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to ATS.
  name: Deel Ats API
  slug: deel-com-ats-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The atsApplications API from Deel — 4 operation(s) for atsapplications.
  name: Deel Ats Applications API
  slug: deel-com-atsapplications-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The atsApplicationSources API from Deel — 1 operation(s) for atsapplicationsources.
  name: Deel Ats Application Sources API
  slug: deel-com-atsapplicationsources-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The atsAttachments API from Deel — 1 operation(s) for atsattachments.
  name: Deel Ats Attachments API
  slug: deel-com-atsattachments-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The atsCandidates API from Deel — 2 operation(s) for atscandidates.
  name: Deel Ats Candidates API
  slug: deel-com-atscandidates-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The atsDepartments API from Deel — 1 operation(s) for atsdepartments.
  name: Deel Ats Departments API
  slug: deel-com-atsdepartments-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The atsEmailTemplates API from Deel — 1 operation(s) for atsemailtemplates.
  name: Deel Ats Email Templates API
  slug: deel-com-atsemailtemplates-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The atsEmploymentTypes API from Deel — 1 operation(s) for atsemploymenttypes.
  name: Deel Ats Employment Types API
  slug: deel-com-atsemploymenttypes-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The atsHiringMembers API from Deel — 1 operation(s) for atshiringmembers.
  name: Deel Ats Hiring Members API
  slug: deel-com-atshiringmembers-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The atsJobPostings API from Deel — 3 operation(s) for atsjobpostings.
  name: Deel Ats Job Postings API
  slug: deel-com-atsjobpostings-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The atsJobs API from Deel — 1 operation(s) for atsjobs.
  name: Deel Ats Jobs API
  slug: deel-com-atsjobs-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The atsLocations API from Deel — 1 operation(s) for atslocations.
  name: Deel Ats Locations API
  slug: deel-com-atslocations-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The atsOffers API from Deel — 1 operation(s) for atsoffers.
  name: Deel Ats Offers API
  slug: deel-com-atsoffers-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The atsReasons API from Deel — 1 operation(s) for atsreasons.
  name: Deel Ats Reasons API
  slug: deel-com-atsreasons-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The atsTags API from Deel — 1 operation(s) for atstags.
  name: Deel Ats Tags API
  slug: deel-com-atstags-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Clearance requests.
  name: Deel Clearance Requests API
  slug: deel-com-clearancerequests-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Consent.
  name: Deel Consent API
  slug: deel-com-consent-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The contractorAmendments API from Deel — 1 operation(s) for contractoramendments.
  name: Deel Contractor Amendments API
  slug: deel-com-contractoramendments-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The contractorHiring API from Deel — 6 operation(s) for contractorhiring.
  name: Deel Contractor Hiring API
  slug: deel-com-contractorhiring-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The costCalculator API from Deel — 1 operation(s) for costcalculator.
  name: Deel Cost Calculator API
  slug: deel-com-costcalculator-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Cost Centers.
  name: Deel Cost Centers API
  slug: deel-com-costcenters-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The customFieldsContracts API from Deel — 4 operation(s) for customfieldscontracts.
  name: Deel Custom Fields Contracts API
  slug: deel-com-customfieldscontracts-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The customFieldsPeople API from Deel — 4 operation(s) for customfieldspeople.
  name: Deel Custom Fields People API
  slug: deel-com-customfieldspeople-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The deelAsAService API from Deel — 2 operation(s) for deelasaservice.
  name: Deel Deel As A Service API
  slug: deel-com-deelasaservice-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Documents.
  name: Deel Documents API
  slug: deel-com-documents-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Employee Information.
  name: Deel Employee Information API
  slug: deel-com-employeeinformation-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The Endpoints API from Deel — 0 operation(s) for endpoints.
  name: Deel Endpoints API
  slug: deel-com-endpoints-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The eor API from Deel — 6 operation(s) for eor.
  name: Deel Eor API
  slug: deel-com-eor-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The eorAmendments API from Deel — 9 operation(s) for eoramendments.
  name: Deel Eor Amendments API
  slug: deel-com-eoramendments-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The eorBenefits API from Deel — 1 operation(s) for eorbenefits.
  name: Deel Eor Benefits API
  slug: deel-com-eorbenefits-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The eorContract API from Deel — 3 operation(s) for eorcontract.
  name: Deel Eor Contract API
  slug: deel-com-eorcontract-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The eorContractDocuments API from Deel — 2 operation(s) for eorcontractdocuments.
  name: Deel Eor Contract Documents API
  slug: deel-com-eorcontractdocuments-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The eorHiring API from Deel — 9 operation(s) for eorhiring.
  name: Deel Eor Hiring API
  slug: deel-com-eorhiring-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The eorJobScopes API from Deel — 2 operation(s) for eorjobscopes.
  name: Deel Eor Job Scopes API
  slug: deel-com-eorjobscopes-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The eorOffboarding API from Deel — 8 operation(s) for eoroffboarding.
  name: Deel Eor Offboarding API
  slug: deel-com-eoroffboarding-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The eorPayslips API from Deel — 1 operation(s) for eorpayslips.
  name: Deel Eor Payslips API
  slug: deel-com-eorpayslips-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The eorProjectAssignment API from Deel — 3 operation(s) for eorprojectassignment.
  name: Deel Eor Project Assignment API
  slug: deel-com-eorprojectassignment-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The eorTerminations API from Deel — 4 operation(s) for eorterminations.
  name: Deel Eor Terminations API
  slug: deel-com-eorterminations-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The eorWorkerAccounts API from Deel — 1 operation(s) for eorworkeraccounts.
  name: Deel Eor Worker Accounts API
  slug: deel-com-eorworkeraccounts-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The eorWorkerAgreements API from Deel — 3 operation(s) for eorworkeragreements.
  name: Deel Eor Worker Agreements API
  slug: deel-com-eorworkeragreements-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The eorWorkerBanks API from Deel — 2 operation(s) for eorworkerbanks.
  name: Deel Eor Worker Banks API
  slug: deel-com-eorworkerbanks-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The eorWorkerBenefits API from Deel — 1 operation(s) for eorworkerbenefits.
  name: Deel Eor Worker Benefits API
  slug: deel-com-eorworkerbenefits-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The eorWorkerCompliance API from Deel — 5 operation(s) for eorworkercompliance.
  name: Deel Eor Worker Compliance API
  slug: deel-com-eorworkercompliance-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The eorWorkerDocuments API from Deel — 1 operation(s) for eorworkerdocuments.
  name: Deel Eor Worker Documents API
  slug: deel-com-eorworkerdocuments-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The eorWorkerInformation API from Deel — 3 operation(s) for eorworkerinformation.
  name: Deel Eor Worker Information API
  slug: deel-com-eorworkerinformation-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The eorWorkerMailboxes API from Deel — 1 operation(s) for eorworkermailboxes.
  name: Deel Eor Worker Mailboxes API
  slug: deel-com-eorworkermailboxes-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The eorWorkerOffboarding API from Deel — 5 operation(s) for eorworkeroffboarding.
  name: Deel Eor Worker Offboarding API
  slug: deel-com-eorworkeroffboarding-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The eorWorkerPayslips API from Deel — 1 operation(s) for eorworkerpayslips.
  name: Deel Eor Worker Payslips API
  slug: deel-com-eorworkerpayslips-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Equity Tokens.
  name: Deel Equity Tokens API
  slug: deel-com-equitytokens-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Files.
  name: Deel Files API
  slug: deel-com-files-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Forms.
  name: Deel Forms API
  slug: deel-com-forms-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The globalPayroll API from Deel — 17 operation(s) for globalpayroll.
  name: Deel Global Payroll API
  slug: deel-com-globalpayroll-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The gpHiring API from Deel — 2 operation(s) for gphiring.
  name: Deel Gp Hiring API
  slug: deel-com-gphiring-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Groups.
  name: Deel Groups API
  slug: deel-com-groups-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to HRX Documents.
  name: Deel Hrx Documents API
  slug: deel-com-hrxdocuments-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to IC invoicing taxes.
  name: Deel Ic Invoicing Taxes API
  slug: deel-com-icinvoicingtaxes-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Integrations.
  name: Deel Integrations API
  slug: deel-com-integrations-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The invoiceAdjustments API from Deel — 4 operation(s) for invoiceadjustments.
  name: Deel Invoice Adjustments API
  slug: deel-com-invoiceadjustments-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to IT agreements.
  name: Deel It Agreements API
  slug: deel-com-itagreements-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The itAssets API from Deel — 9 operation(s) for itassets.
  name: Deel It Assets API
  slug: deel-com-itassets-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to IT orders.
  name: Deel It Orders API
  slug: deel-com-itorders-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to IT policies.
  name: Deel It Policies API
  slug: deel-com-itpolicies-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to IT products.
  name: Deel It Products API
  slug: deel-com-itproducts-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to IT seats.
  name: Deel It Seats API
  slug: deel-com-itseats-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to IT warehouses.
  name: Deel It Warehouses API
  slug: deel-com-itwarehouses-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Knowledge Hub.
  name: Deel Knowledge Hub API
  slug: deel-com-knowledgehub-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Learning.
  name: Deel Learning API
  slug: deel-com-learning-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to List Cycles.
  name: Deel List Cycles API
  slug: deel-com-listcycles-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The offboarding API from Deel — 3 operation(s) for offboarding.
  name: Deel Offboarding API
  slug: deel-com-offboarding-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The offCycle API from Deel — 2 operation(s) for offcycle.
  name: Deel Off Cycle API
  slug: deel-com-offcycle-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Off-cycle Payments.
  name: Deel Off Cycle Payments API
  slug: deel-com-offcyclepayments-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Onboarding.
  name: Deel Onboarding API
  slug: deel-com-onboarding-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to On-Demand Payroll.
  name: Deel On Demand Payroll API
  slug: deel-com-ondemandpayroll-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Organization structure.
  name: Deel Organization Structure API
  slug: deel-com-organizationstructure-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Organization Tasks.
  name: Deel Organization Tasks API
  slug: deel-com-organizationtasks-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Payments.
  name: Deel Payments API
  slug: deel-com-payments-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The payouts API from Deel — 12 operation(s) for payouts.
  name: Deel Payouts API
  slug: deel-com-payouts-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The personalInformation API from Deel — 3 operation(s) for personalinformation.
  name: Deel Personal Information API
  slug: deel-com-personalinformation-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Positions.
  name: Deel Positions API
  slug: deel-com-positions-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The projects API from Deel — 5 operation(s) for projects.
  name: Deel Projects API
  slug: deel-com-projects-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Refund Statements.
  name: Deel Refund Statements API
  slug: deel-com-refundstatements-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Reports.
  name: Deel Reports API
  slug: deel-com-reports-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Talent.
  name: Deel Talent API
  slug: deel-com-talent-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Tasks.
  name: Deel Tasks API
  slug: deel-com-tasks-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Terminations.
  name: Deel Terminations API
  slug: deel-com-terminations-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Time Off.
  name: Deel Time Off API
  slug: deel-com-timeoff-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Time Tracking Shifts.
  name: Deel Time Tracking Shifts API
  slug: deel-com-timetrackingshifts-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Treasury.
  name: Deel Treasury API
  slug: deel-com-treasury-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The users API from Deel — 2 operation(s) for users.
  name: Deel Users API
  slug: deel-com-users-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Worker HR.
  name: Deel Worker Hr API
  slug: deel-com-workerhr-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The workerInformation API from Deel — 8 operation(s) for workerinformation.
  name: Deel Worker Information API
  slug: deel-com-workerinformation-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Worker Relations.
  name: Deel Worker Relations API
  slug: deel-com-workerrelations-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The workers API from Deel — 10 operation(s) for workers.
  name: Deel Workers API
  slug: deel-com-workers-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: API endpoints related to Worker Session.
  name: Deel Worker Session API
  slug: deel-com-workersession-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The Legal Entities API from Deel — 10 operation(s) for legal entities.
  name: Deel Legal Entities API
  slug: deel-com-legal-entities-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: The Magic Link API from Deel — 1 operation(s) for magic link.
  name: Deel Magic Link API
  slug: deel-com-magic-link-api
artifact_total: 208
asyncapis:
- description: AsyncAPI definition for Deel's webhook surface. Deel webhooks are HTTP POST deliveries from Deel to a subscriber-controlled `url` registered via the Deel Webhooks API (`POST /rest/v2/webhooks`). A sub
  name: Deel Webhooks
  slug: deel-webhooks-asyncapi
collections:
- collection_type: open
  name: Deel ATS API
  slug: open-deel-ats-api
- collection_type: open
  name: Deel ATS Adjustments API
  slug: open-deel-com-adjustments-api
- collection_type: open
  name: Deel ATS Adjustments Applications API
  slug: open-deel-com-applications-api
- collection_type: open
  name: Deel ATS Adjustments Candidates API
  slug: open-deel-com-candidates-api
- collection_type: open
  name: Deel ATS Adjustments Contractor Amendments API
  slug: open-deel-com-contractor-amendments-api
- collection_type: open
  name: Deel ATS Adjustments Contractor Hiring API
  slug: open-deel-com-contractor-hiring-api
- collection_type: open
  name: Deel ATS Adjustments Contracts API
  slug: open-deel-com-contracts-api
- collection_type: open
  name: Deel ATS Adjustments Custom Fields API
  slug: open-deel-com-custom-fields-api
- collection_type: open
  name: Deel ATS Adjustments Deel IT API
  slug: open-deel-com-deel-it-api
- collection_type: open
  name: Deel ATS Adjustments EOR Amendments API
  slug: open-deel-com-eor-amendments-api
- collection_type: open
  name: Deel ATS Adjustments EOR Benefits API
  slug: open-deel-com-eor-benefits-api
- collection_type: open
  name: Deel ATS Adjustments EOR Cost Calculator API
  slug: open-deel-com-eor-cost-calculator-api
- collection_type: open
  name: Deel ATS Adjustments EOR Hiring API
  slug: open-deel-com-eor-hiring-api
- collection_type: open
  name: Deel ATS Adjustments EOR Terminations API
  slug: open-deel-com-eor-terminations-api
- collection_type: open
  name: Deel ATS Adjustments EOR Worker Information API
  slug: open-deel-com-eor-worker-information-api
- collection_type: open
  name: Deel ATS Adjustments Global Payroll API
  slug: open-deel-com-global-payroll-api
- collection_type: open
  name: Deel ATS Adjustments GP Hiring API
  slug: open-deel-com-gp-hiring-api
- collection_type: open
  name: Deel ATS Adjustments IC Invoicing Taxes API
  slug: open-deel-com-ic-invoicing-taxes-api
- collection_type: open
  name: Deel ATS Adjustments Immigration API
  slug: open-deel-com-immigration-api
- collection_type: open
  name: Deel ATS Adjustments Invoice Adjustments API
  slug: open-deel-com-invoice-adjustments-api
- collection_type: open
  name: Deel ATS Adjustments Jobs API
  slug: open-deel-com-jobs-api
- collection_type: open
  name: Deel ATS Adjustments Legal Entities API
  slug: open-deel-com-legal-entities-api
- collection_type: open
  name: Deel ATS Adjustments Lookups API
  slug: open-deel-com-lookups-api
- collection_type: open
  name: Deel ATS Adjustments Magic Link API
  slug: open-deel-com-magic-link-api
- collection_type: open
  name: Deel ATS Adjustments Managers API
  slug: open-deel-com-managers-api
- collection_type: open
  name: Deel ATS Adjustments Milestones API
  slug: open-deel-com-milestones-api
- collection_type: open
  name: Deel ATS Adjustments Off Cycle API
  slug: open-deel-com-off-cycle-api
- collection_type: open
  name: Deel ATS Adjustments Offers API
  slug: open-deel-com-offers-api
- collection_type: open
  name: Deel ATS Adjustments Organizations API
  slug: open-deel-com-organizations-api
- collection_type: open
  name: Deel ATS Adjustments Payslips API
  slug: open-deel-com-payslips-api
- collection_type: open
  name: Deel ATS Adjustments Paystubs API
  slug: open-deel-com-paystubs-api
- collection_type: open
  name: Deel ATS Adjustments People API
  slug: open-deel-com-people-api
- collection_type: open
  name: Deel ATS Adjustments Reference Data API
  slug: open-deel-com-reference-data-api
- collection_type: open
  name: Deel ATS Adjustments SCIM API
  slug: open-deel-com-scim-api
- collection_type: open
  name: Deel ATS Adjustments Screenings API
  slug: open-deel-com-screenings-api
- collection_type: open
  name: Deel ATS Adjustments Time Off API
  slug: open-deel-com-time-off-api
- collection_type: open
  name: Deel ATS Adjustments Time Tracking API
  slug: open-deel-com-time-tracking-api
- collection_type: open
  name: Deel ATS Adjustments Timesheets API
  slug: open-deel-com-timesheets-api
- collection_type: open
  name: Deel ATS Adjustments Webhook Events API
  slug: open-deel-com-webhook-events-api
- collection_type: open
  name: Deel ATS Adjustments Webhooks API
  slug: open-deel-com-webhooks-api
- collection_type: open
  name: Deel Contractors API
  slug: open-deel-contractors-api
- collection_type: open
  name: Deel Core API
  slug: open-deel-core-api
- collection_type: open
  name: Deel Employer of Record (EOR) API
  slug: open-deel-eor-api
- collection_type: open
  name: Deel Global Payroll API
  slug: open-deel-global-payroll-api
- collection_type: open
  name: Deel HRIS API
  slug: open-deel-hris-api
- collection_type: open
  name: Deel Platform Extensions API
  slug: open-deel-platform-extensions-api
- collection_type: open
  name: Deel Webhooks API
  slug: open-deel-webhooks-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.deel.com/
- group: other
  href: https://artifacts.apis.io/deel-com/capabilities/deel-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/deel-com-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/deel-com/agentic-access/deel-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/deel-com-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/deel-com/security/deel-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deel-com-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/deel-com/authentication/deel-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/deel-com-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.deel.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.deel.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.deel.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.deel.com/api/quickstart
- group: auth
  title: ''
  type: Authentication
  url: https://developer.deel.com/api/authentication
- group: auth
  title: ''
  type: Authentication
  url: https://developer.deel.com/api/oauth
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.deel.com/api/rate-limits
- group: docs
  title: ''
  type: Documentation
  url: https://developer.deel.com/api/idempotency
- group: other
  title: ''
  type: BestPractices
  url: https://developer.deel.com/api/best-practices
- group: design
  title: ''
  type: Versioning
  url: https://developer.deel.com/api/api-versioning
- group: start
  title: ''
  type: Sandbox
  url: https://developer.deel.com/api/sandbox
- group: design
  title: ''
  type: Webhooks
  url: https://developer.deel.com/api/webhooks/introduction
- group: design
  title: ''
  type: Webhooks
  url: https://developer.deel.com/api/webhooks/events
- group: company
  title: ''
  type: Partner
  url: https://developer.deel.com/api/partners/introduction
- group: other
  title: ''
  type: Embedded
  url: https://developer.deel.com/api/embedded/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://developer.deel.com/mcp/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://developer.deel.com/mcp/connecting-clients
- group: docs
  title: ''
  type: Documentation
  url: https://developer.deel.com/mcp/reference/tools-reference
- group: operate
  title: ''
  type: Community
  url: https://stack.deel.com
- group: company
  title: ''
  type: Blog
  url: https://www.deel.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.deel.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.deel.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.letsdeel.com/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.deel.com/contact-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deel/
- group: other
  title: ''
  type: X
  url: https://x.com/deel
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deel
- group: commercial
  href: https://artifacts.apis.io/deel-com/plans/deel-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deel-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/deel-com/rate-limits/deel-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/deel-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/deel-com/finops/deel-com-finops.yml
  title: ''
  type: FinOps
  url: finops/deel-com-finops.yml
created: '2026-05-25'
description: Deel is a global workforce platform combining payroll, Employer of Record (EOR), independent contractor management, HRIS, ATS, IT/device management, immigration, and background screenings across 150+ countries. The Deel Public API and SCIM API expose the full worker lifecycle — hire, onboard, pay, manage time off, run payroll, terminate — through a REST surface at api.letsdeel.com/rest/v2 with bearer-token and OAuth2 authentication, a sandbox at api-sandbox.demo.deel.com, HMAC-signed webhooks, a Deel App Store for partner apps, an Embedded "Deel as a Service" model, and a public MCP server for AI agent integration. Deel has compliantly processed over $20B in global payroll for 40,000+ companies.
features:
- Global payroll in 120+ countries with local compliance and tax handling
- Employer of Record (EOR) in 100+ countries via Deel-owned local entities
- Contractor management with IC, Pay-As-You-Go, milestone, and COR contract types
- Pay workers in 150+ currencies including crypto (Bitcoin, Ethereum, USDC)
- Unified HRIS across all worker types (employee, contractor, EOR)
- Time off, time tracking, and work schedule management
- SCIM 2.0 user provisioning for Okta, Azure AD, and other identity providers
- ATS (Applicant Tracking System) with jobs, candidates, applications, offers, and pipeline tracking
- Deel IT — device provisioning, MDM, and equipment lifecycle for distributed teams
- Deel Mobility — in-house visa and immigration case management
- Deel Engage — performance, learning, and 1:1 management
- Background checks (KYC and AML screenings)
- Bearer-token authentication with Organization and Personal token types and granular scopes
- OAuth2 authentication for Deel App Store partner integrations
- Date-based API versioning with documented endpoint lifecycle states
- Rate limiting at 5 requests per second per organization (shared across tokens)
- Idempotency keys on POST/PATCH via UUID v4 with 24-hour response cache
- Webhooks with HMAC-SHA256 signatures and a no-code subscription manager
- Webhook simulation in sandbox without affecting production data
- Sandbox environment at api-sandbox.demo.deel.com with pre-populated test workers
- Deel as a Service (Embedded) — partners embed EOR/IC workflows directly into their own products
- Deel MCP Server for AI agent integration with Claude Code, Cursor, and other MCP clients
- LLM-ready docs via .md page suffix and llms-full.txt aggregated documentation
- Postman collection, Insomnia collection, and inline OpenAPI per endpoint
- 2,000+ in-country experts plus AI-driven compliance logic
finops:
- has_sources: true
  method: derived
  name: Deel Com Finops
  primary_unit: worker
  service_category: ''
  slug: deel-com-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deel-com.png
json_schemas:
- name: Deel Contract
  property_count: 15
  slug: deel-contract
- name: Deel EOR Contract
  property_count: 15
  slug: deel-eor-contract
- name: Deel Payroll Event
  property_count: 12
  slug: deel-payroll-event
- name: Deel Person
  property_count: 15
  slug: deel-person
- name: Deel Time Off Request
  property_count: 13
  slug: deel-time-off
jsonld:
- class_count: 1
  name: Deel Com Context
  property_count: 9
  slug: deel-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.deel.com over HTTP.
  name: Deel MCP Server
  slug: deel-com
modified: '2026-09-16'
name: Deel
nav: Providers
network: true
overview: 'Deel publishes 121 API contracts indexed on the [APIs.io](https://apis.io/) network, including Adjustments API, Candidates API, Contracts API, and 118 more. Tagged areas include Human Resources, Payroll, Global Payroll, Employer of Record, and Contractors.


  The Deel catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Deel''s developer surface includes authentication, developer portal, documentation, getting-started guide, sandbox, engineering blog, pricing, and 28 more developer resources.'
plans:
- name: Deel Com Plans Pricing
  plan_count: 5
  slug: deel-com-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Deel Com Rate Limits
  slug: deel-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Deel — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: deel-com-jsonschema-spectral-rules
score:
  band: strong
  composite: 63.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 74.3
    catalog_earned_first_party: 12.0
    catalog_gap: 40.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 76.2
    developer_ergonomics: 64.3
    discoverability: 73.3
    operational_transparency: 47.4
  previous_composite: 62.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 32.3
      total: 325
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 77.8
screenshot: https://apis.io/screenshots/deel-com/deel-com-2026-06-20T175806.png
security:
- kind: authentication
  name: Deel Com Authentication
  slug: deel-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Deel Com Domain Security
  slug: deel-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: deel-com
tags:
- Human Resources
- Payroll
- Global Payroll
- Employer of Record
- Contractors
- HRIS
- Applicant Tracking
- Workforce
- Compliance
- Immigration
- Background Checks
- Webhook
- IT
website: https://www.deel.com/
---

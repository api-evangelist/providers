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
    event_surface_described: derived
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 40
  human_in_the_loop: 0
  name: Deel Com Agentic Access
  operation_count: 93
  slug: deel-com-agentic-access
  summary_line: 93 operations · 40 acting
api_count: 8
apis:
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Gross-to-net payroll adjustments — bonuses, deductions, one-time payments
  name: Deel Adjustments API
  slug: deel-com-adjustments-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Application lifecycle and pipeline stages
  name: Deel Applications API
  slug: deel-com-applications-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Candidate records and resume attachments
  name: Deel Candidates API
  slug: deel-com-candidates-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Amend active contractor contracts
  name: Deel Contractor Amendments API
  slug: deel-com-contractor-amendments-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Create and onboard IC, PAYG, milestone, and COR contracts
  name: Deel Contractor Hiring API
  slug: deel-com-contractor-hiring-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: IC and EOR contract list and detail
  name: Deel Contracts API
  slug: deel-com-contracts-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Custom fields on contracts and people
  name: Deel Custom Fields API
  slug: deel-com-custom-fields-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Device provisioning and equipment lifecycle
  name: Deel Deel IT API
  slug: deel-com-deel-it-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Amend active EOR contracts with structured approval flow
  name: Deel EOR Amendments API
  slug: deel-com-eor-amendments-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Country-specific benefit plans and worker enrollment
  name: Deel EOR Benefits API
  slug: deel-com-eor-benefits-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Employment cost calculator including salary, benefits, and Deel fees
  name: Deel EOR Cost Calculator API
  slug: deel-com-eor-cost-calculator-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Hiring guides, contract creation, three-party quote signing
  name: Deel EOR Hiring API
  slug: deel-com-eor-hiring-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Terminate EOR contracts with cause and offboarding workflow
  name: Deel EOR Terminations API
  slug: deel-com-eor-terminations-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Worker-side accounts, banks, documents, payslips, compliance
  name: Deel EOR Worker Information API
  slug: deel-com-eor-worker-information-api
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
  description: Contractor invoicing and tax handling
  name: Deel IC Invoicing Taxes API
  slug: deel-com-ic-invoicing-taxes-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Visas, work permits, immigration case management
  name: Deel Immigration API
  slug: deel-com-immigration-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Add, update, delete, and review invoice line items
  name: Deel Invoice Adjustments API
  slug: deel-com-invoice-adjustments-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Job and job-posting management
  name: Deel Jobs API
  slug: deel-com-jobs-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Client legal entities, industries
  name: Deel Legal Entities API
  slug: deel-com-legal-entities-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Countries, currencies, job titles, seniority levels, time-off types
  name: Deel Lookups API
  slug: deel-com-lookups-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Generate single-use deep links into the Deel app
  name: Deel Magic Link API
  slug: deel-com-magic-link-api
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
  description: One-off payments outside the normal cycle
  name: Deel Off Cycle API
  slug: deel-com-off-cycle-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Offer creation and acceptance
  name: Deel Offers API
  slug: deel-com-offers-api
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
  description: Departments, locations, employment types, sources, tags, reasons
  name: Deel Reference Data API
  slug: deel-com-reference-data-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: SCIM 2.0 user provisioning per RFC 7643/7644
  name: Deel SCIM API
  slug: deel-com-scim-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: KYC and AML background screenings
  name: Deel Screenings API
  slug: deel-com-screenings-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Time-off policies, requests, entitlements, events, work schedules
  name: Deel Time Off API
  slug: deel-com-time-off-api
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
  description: Discover available webhook event types
  name: Deel Webhook Events API
  slug: deel-com-webhook-events-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: declared
  description: Create, list, update, and delete webhook subscriptions
  name: Deel Webhooks API
  slug: deel-com-webhooks-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The Default API from Deel — 1 operation(s) for default.
  name: Deel Default API
  slug: deel-default-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_accounting API from Deel — 6 operation(s) for subpackage_accounting.
  name: Deel subpackage_accounting API
  slug: deel-subpackage-accounting-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_adjustments API from Deel — 4 operation(s) for subpackage_adjustments.
  name: Deel subpackage_adjustments API
  slug: deel-subpackage-adjustments-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_assets API from Deel — 2 operation(s) for subpackage_assets.
  name: Deel subpackage_assets API
  slug: deel-subpackage-assets-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_ats API from Deel — 20 operation(s) for subpackage_ats.
  name: Deel subpackage_ats API
  slug: deel-subpackage-ats-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_candidates API from Deel — 1 operation(s) for subpackage_candidates.
  name: Deel subpackage_candidates API
  slug: deel-subpackage-candidates-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_consent API from Deel — 1 operation(s) for subpackage_consent.
  name: Deel subpackage_consent API
  slug: deel-subpackage-consent-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_contractorAmendments API from Deel — 1 operation(s) for subpackage_contractoramendments.
  name: Deel subpackage_contractorAmendments API
  slug: deel-subpackage-contractoramendments-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_contractorHiring API from Deel — 6 operation(s) for subpackage_contractorhiring.
  name: Deel subpackage_contractorHiring API
  slug: deel-subpackage-contractorhiring-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_contracts API from Deel — 10 operation(s) for subpackage_contracts.
  name: Deel subpackage_contracts API
  slug: deel-subpackage-contracts-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_costCalculator API from Deel — 1 operation(s) for subpackage_costcalculator.
  name: Deel subpackage_costCalculator API
  slug: deel-subpackage-costcalculator-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_costCenters API from Deel — 3 operation(s) for subpackage_costcenters.
  name: Deel subpackage_costCenters API
  slug: deel-subpackage-costcenters-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_customFieldsContracts API from Deel — 4 operation(s) for subpackage_customfieldscontracts.
  name: Deel subpackage_customFieldsContracts API
  slug: deel-subpackage-customfieldscontracts-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_customFieldsPeople API from Deel — 4 operation(s) for subpackage_customfieldspeople.
  name: Deel subpackage_customFieldsPeople API
  slug: deel-subpackage-customfieldspeople-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_deelAsAService API from Deel — 2 operation(s) for subpackage_deelasaservice.
  name: Deel subpackage_deelAsAService API
  slug: deel-subpackage-deelasaservice-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_employeeInformation API from Deel — 1 operation(s) for subpackage_employeeinformation.
  name: Deel subpackage_employeeInformation API
  slug: deel-subpackage-employeeinformation-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_employees API from Deel — 1 operation(s) for subpackage_employees.
  name: Deel subpackage_employees API
  slug: deel-subpackage-employees-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_enrollments API from Deel — 1 operation(s) for subpackage_enrollments.
  name: Deel subpackage_enrollments API
  slug: deel-subpackage-enrollments-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_eorAmendments API from Deel — 9 operation(s) for subpackage_eoramendments.
  name: Deel subpackage_eorAmendments API
  slug: deel-subpackage-eoramendments-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_eorBenefits API from Deel — 1 operation(s) for subpackage_eorbenefits.
  name: Deel subpackage_eorBenefits API
  slug: deel-subpackage-eorbenefits-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_eorContract API from Deel — 3 operation(s) for subpackage_eorcontract.
  name: Deel subpackage_eorContract API
  slug: deel-subpackage-eorcontract-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_eorContractDocuments API from Deel — 1 operation(s) for subpackage_eorcontractdocuments.
  name: Deel subpackage_eorContractDocuments API
  slug: deel-subpackage-eorcontractdocuments-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_eorHiring API from Deel — 9 operation(s) for subpackage_eorhiring.
  name: Deel subpackage_eorHiring API
  slug: deel-subpackage-eorhiring-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_eorJobScopes API from Deel — 2 operation(s) for subpackage_eorjobscopes.
  name: Deel subpackage_eorJobScopes API
  slug: deel-subpackage-eorjobscopes-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_eorOffboarding API from Deel — 8 operation(s) for subpackage_eoroffboarding.
  name: Deel subpackage_eorOffboarding API
  slug: deel-subpackage-eoroffboarding-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_eorPayslips API from Deel — 1 operation(s) for subpackage_eorpayslips.
  name: Deel subpackage_eorPayslips API
  slug: deel-subpackage-eorpayslips-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_eorProjectAssignment API from Deel — 3 operation(s) for subpackage_eorprojectassignment.
  name: Deel subpackage_eorProjectAssignment API
  slug: deel-subpackage-eorprojectassignment-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_eorTerminations API from Deel — 4 operation(s) for subpackage_eorterminations.
  name: Deel subpackage_eorTerminations API
  slug: deel-subpackage-eorterminations-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_eorWorkerAccounts API from Deel — 1 operation(s) for subpackage_eorworkeraccounts.
  name: Deel subpackage_eorWorkerAccounts API
  slug: deel-subpackage-eorworkeraccounts-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_eorWorkerAgreements API from Deel — 3 operation(s) for subpackage_eorworkeragreements.
  name: Deel subpackage_eorWorkerAgreements API
  slug: deel-subpackage-eorworkeragreements-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_eorWorkerBanks API from Deel — 2 operation(s) for subpackage_eorworkerbanks.
  name: Deel subpackage_eorWorkerBanks API
  slug: deel-subpackage-eorworkerbanks-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_eorWorkerBenefits API from Deel — 1 operation(s) for subpackage_eorworkerbenefits.
  name: Deel subpackage_eorWorkerBenefits API
  slug: deel-subpackage-eorworkerbenefits-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_eorWorkerCompliance API from Deel — 5 operation(s) for subpackage_eorworkercompliance.
  name: Deel subpackage_eorWorkerCompliance API
  slug: deel-subpackage-eorworkercompliance-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_eorWorkerDocuments API from Deel — 1 operation(s) for subpackage_eorworkerdocuments.
  name: Deel subpackage_eorWorkerDocuments API
  slug: deel-subpackage-eorworkerdocuments-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_eorWorkerInformation API from Deel — 3 operation(s) for subpackage_eorworkerinformation.
  name: Deel subpackage_eorWorkerInformation API
  slug: deel-subpackage-eorworkerinformation-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_eorWorkerMailboxes API from Deel — 1 operation(s) for subpackage_eorworkermailboxes.
  name: Deel subpackage_eorWorkerMailboxes API
  slug: deel-subpackage-eorworkermailboxes-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_eorWorkerOffboarding API from Deel — 5 operation(s) for subpackage_eorworkeroffboarding.
  name: Deel subpackage_eorWorkerOffboarding API
  slug: deel-subpackage-eorworkeroffboarding-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_eorWorkerPayslips API from Deel — 1 operation(s) for subpackage_eorworkerpayslips.
  name: Deel subpackage_eorWorkerPayslips API
  slug: deel-subpackage-eorworkerpayslips-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_equityTokens API from Deel — 1 operation(s) for subpackage_equitytokens.
  name: Deel subpackage_equityTokens API
  slug: deel-subpackage-equitytokens-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_forms API from Deel — 2 operation(s) for subpackage_forms.
  name: Deel subpackage_forms API
  slug: deel-subpackage-forms-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_globalPayroll API from Deel — 3 operation(s) for subpackage_globalpayroll.
  name: Deel subpackage_globalPayroll API
  slug: deel-subpackage-globalpayroll-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_gpHiring API from Deel — 2 operation(s) for subpackage_gphiring.
  name: Deel subpackage_gpHiring API
  slug: deel-subpackage-gphiring-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_groups API from Deel — 3 operation(s) for subpackage_groups.
  name: Deel subpackage_groups API
  slug: deel-subpackage-groups-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_hrxDocuments API from Deel — 2 operation(s) for subpackage_hrxdocuments.
  name: Deel subpackage_hrxDocuments API
  slug: deel-subpackage-hrxdocuments-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_icInvoicingTaxes API from Deel — 2 operation(s) for subpackage_icinvoicingtaxes.
  name: Deel subpackage_icInvoicingTaxes API
  slug: deel-subpackage-icinvoicingtaxes-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_immigration API from Deel — 10 operation(s) for subpackage_immigration.
  name: Deel subpackage_immigration API
  slug: deel-subpackage-immigration-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_integrations API from Deel — 1 operation(s) for subpackage_integrations.
  name: Deel subpackage_integrations API
  slug: deel-subpackage-integrations-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_invoiceAdjustments API from Deel — 4 operation(s) for subpackage_invoiceadjustments.
  name: Deel subpackage_invoiceAdjustments API
  slug: deel-subpackage-invoiceadjustments-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_knowledgeHub API from Deel — 1 operation(s) for subpackage_knowledgehub.
  name: Deel subpackage_knowledgeHub API
  slug: deel-subpackage-knowledgehub-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_learning API from Deel — 1 operation(s) for subpackage_learning.
  name: Deel subpackage_learning API
  slug: deel-subpackage-learning-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_legalEntities API from Deel — 4 operation(s) for subpackage_legalentities.
  name: Deel subpackage_legalEntities API
  slug: deel-subpackage-legalentities-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_listCycles API from Deel — 1 operation(s) for subpackage_listcycles.
  name: Deel subpackage_listCycles API
  slug: deel-subpackage-listcycles-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_lookups API from Deel — 6 operation(s) for subpackage_lookups.
  name: Deel subpackage_lookups API
  slug: deel-subpackage-lookups-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_magicLink API from Deel — 1 operation(s) for subpackage_magiclink.
  name: Deel subpackage_magicLink API
  slug: deel-subpackage-magiclink-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_managers API from Deel — 2 operation(s) for subpackage_managers.
  name: Deel subpackage_managers API
  slug: deel-subpackage-managers-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_milestones API from Deel — 2 operation(s) for subpackage_milestones.
  name: Deel subpackage_milestones API
  slug: deel-subpackage-milestones-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_offboarding API from Deel — 3 operation(s) for subpackage_offboarding.
  name: Deel subpackage_offboarding API
  slug: deel-subpackage-offboarding-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_offCycle API from Deel — 2 operation(s) for subpackage_offcycle.
  name: Deel subpackage_offCycle API
  slug: deel-subpackage-offcycle-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_onboarding API from Deel — 3 operation(s) for subpackage_onboarding.
  name: Deel subpackage_onboarding API
  slug: deel-subpackage-onboarding-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_orders API from Deel — 2 operation(s) for subpackage_orders.
  name: Deel subpackage_orders API
  slug: deel-subpackage-orders-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_organizations API from Deel — 7 operation(s) for subpackage_organizations.
  name: Deel subpackage_organizations API
  slug: deel-subpackage-organizations-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_organizationStructure API from Deel — 6 operation(s) for subpackage_organizationstructure.
  name: Deel subpackage_organizationStructure API
  slug: deel-subpackage-organizationstructure-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_organizationTasks API from Deel — 1 operation(s) for subpackage_organizationtasks.
  name: Deel subpackage_organizationTasks API
  slug: deel-subpackage-organizationtasks-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_payouts API from Deel — 11 operation(s) for subpackage_payouts.
  name: Deel subpackage_payouts API
  slug: deel-subpackage-payouts-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_payroll API from Deel — 2 operation(s) for subpackage_payroll.
  name: Deel subpackage_payroll API
  slug: deel-subpackage-payroll-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_payslips API from Deel — 1 operation(s) for subpackage_payslips.
  name: Deel subpackage_payslips API
  slug: deel-subpackage-payslips-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_paystubs API from Deel — 1 operation(s) for subpackage_paystubs.
  name: Deel subpackage_paystubs API
  slug: deel-subpackage-paystubs-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_people API from Deel — 5 operation(s) for subpackage_people.
  name: Deel subpackage_people API
  slug: deel-subpackage-people-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_personalInformation API from Deel — 2 operation(s) for subpackage_personalinformation.
  name: Deel subpackage_personalInformation API
  slug: deel-subpackage-personalinformation-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_plans401K API from Deel — 5 operation(s) for subpackage_plans401k.
  name: Deel subpackage_plans401K API
  slug: deel-subpackage-plans401k-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_policies API from Deel — 1 operation(s) for subpackage_policies.
  name: Deel subpackage_policies API
  slug: deel-subpackage-policies-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_positions API from Deel — 3 operation(s) for subpackage_positions.
  name: Deel subpackage_positions API
  slug: deel-subpackage-positions-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_projects API from Deel — 5 operation(s) for subpackage_projects.
  name: Deel subpackage_projects API
  slug: deel-subpackage-projects-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_reports API from Deel — 4 operation(s) for subpackage_reports.
  name: Deel subpackage_reports API
  slug: deel-subpackage-reports-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_screenings API from Deel — 6 operation(s) for subpackage_screenings.
  name: Deel subpackage_screenings API
  slug: deel-subpackage-screenings-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_serviceProviderConfig API from Deel — 1 operation(s) for subpackage_serviceproviderconfig.
  name: Deel subpackage_serviceProviderConfig API
  slug: deel-subpackage-serviceproviderconfig-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_tasks API from Deel — 5 operation(s) for subpackage_tasks.
  name: Deel subpackage_tasks API
  slug: deel-subpackage-tasks-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_terminations API from Deel — 1 operation(s) for subpackage_terminations.
  name: Deel subpackage_terminations API
  slug: deel-subpackage-terminations-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_timeOff API from Deel — 11 operation(s) for subpackage_timeoff.
  name: Deel subpackage_timeOff API
  slug: deel-subpackage-timeoff-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_timesheets API from Deel — 4 operation(s) for subpackage_timesheets.
  name: Deel subpackage_timesheets API
  slug: deel-subpackage-timesheets-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_timeTracking API from Deel — 5 operation(s) for subpackage_timetracking.
  name: Deel subpackage_timeTracking API
  slug: deel-subpackage-timetracking-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_timeTrackingShifts API from Deel — 4 operation(s) for subpackage_timetrackingshifts.
  name: Deel subpackage_timeTrackingShifts API
  slug: deel-subpackage-timetrackingshifts-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_treasury API from Deel — 2 operation(s) for subpackage_treasury.
  name: Deel subpackage_treasury API
  slug: deel-subpackage-treasury-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_user API from Deel — 1 operation(s) for subpackage_user.
  name: Deel subpackage_user API
  slug: deel-subpackage-user-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_users API from Deel — 3 operation(s) for subpackage_users.
  name: Deel subpackage_users API
  slug: deel-subpackage-users-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_webhooks API from Deel — 3 operation(s) for subpackage_webhooks.
  name: Deel subpackage_webhooks API
  slug: deel-subpackage-webhooks-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_workerHr API from Deel — 1 operation(s) for subpackage_workerhr.
  name: Deel subpackage_workerHr API
  slug: deel-subpackage-workerhr-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_workerInformation API from Deel — 8 operation(s) for subpackage_workerinformation.
  name: Deel subpackage_workerInformation API
  slug: deel-subpackage-workerinformation-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_workerRelations API from Deel — 15 operation(s) for subpackage_workerrelations.
  name: Deel subpackage_workerRelations API
  slug: deel-subpackage-workerrelations-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_workers API from Deel — 5 operation(s) for subpackage_workers.
  name: Deel subpackage_workers API
  slug: deel-subpackage-workers-api
- baseURL: https://api.letsdeel.com/rest/v2
  baseurl_source: spec
  description: The subpackage_workerSession API from Deel — 2 operation(s) for subpackage_workersession.
  name: Deel subpackage_workerSession API
  slug: deel-subpackage-workersession-api
artifact_total: 219
asyncapis:
- description: AsyncAPI definition for Deel's webhook surface. Deel webhooks are HTTP POST deliveries from Deel to a subscriber-controlled `url` registered via the Deel Webhooks API (`POST /rest/v2/webhooks`). A sub
  name: Deel Webhooks
  slug: deel-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/deel-com-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/deel-com-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deel-com-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/deel-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/deel-com-rate-limits.yml
- group: commercial
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
- name: Deel Com Finops
  service_category: Business Applications — Human Resources
  slug: deel-com-finops
graphqls:
- description: 'Deel is a global workforce platform combining payroll, Employer of Record (EOR), independent contractor management, HRIS, ATS, IT/device management, immigration, and background screenings across 150+ '
  name: Deel GraphQL Schema
  slug: deel-com-graphql
- description: This conceptual GraphQL schema covers the Deel global payroll, HR, and contractor management platform. Deel supports workers and contractors in 150+ countries through a unified API surface spanning co
  name: Deel GraphQL Schema
  slug: deel-graphql
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
modified: '2026-05-25'
name: Deel
nav: Providers
network: true
overview: 'Deel publishes 130 APIs on the [APIs.io](https://apis.io/) network, including Adjustments API, Applications API, Candidates API, and 127 more. Tagged areas include HR, Payroll, Global Payroll, EOR, and Employer of Record.


  The Deel catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Deel''s developer surface includes authentication, developer portal, documentation, getting-started guide, sandbox, engineering blog, pricing, and 27 more developer resources.'
plans:
- name: Deel Com Plans Pricing
  plan_count: 15
  slug: deel-com-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Deel Com Rate Limits
  slug: deel-com-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Deel API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: deel-com-jsonschema-spectral-rules
score:
  band: strong
  composite: 58.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 78.3
    catalog_earned_first_party: 0.0
    catalog_gap: 36.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.9
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 78.2
    developer_ergonomics: 64.3
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 63.2
  previous_composite: 54.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 130
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/deel-com/refs/heads/main/screenshots/deel-com-2026-06-20T175806.png
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
- HR
- Payroll
- Global Payroll
- EOR
- Employer of Record
- Contractors
- HRIS
- ATS
- Workforce
- Compliance
- Immigration
- Background Checks
- Webhook
- IT
website: https://www.deel.com
---

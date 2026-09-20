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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.5
  scored_at: '2026-09-19'
agentic_access:
- acting_count: 42
  human_in_the_loop: 0
  name: Microsoft Azure Cost Management Agentic Access
  operation_count: 75
  slug: microsoft-azure-cost-management-agentic-access
  summary_line: 75 operations · 42 acting
api_count: 1
apis:
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Create, schedule, run and delete recurring Cost Management exports that write cost and usage data — including FOCUS-format datasets — to a storage account you own.
  name: Azure Cost Management Exports API
  slug: microsoft-azure-cost-management-exports-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: List every REST operation the Microsoft.CostManagement resource provider exposes.
  name: Azure Cost Management Operations API
  slug: microsoft-azure-cost-management-operations-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: List, read and dismiss the cost alerts raised by budgets and anomaly detection at a scope.
  name: Azure Cost Management Alerts API
  slug: microsoft-azure-cost-management-alerts-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Create, read, update and delete cost and reservation-utilization budgets, with their notification thresholds.
  name: Azure Cost Management Budgets API
  slug: microsoft-azure-cost-management-budgets-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Manage rules that redistribute shared cost between scopes within a billing account.
  name: Azure Cost Management Cost Allocation Rule Definitions API
  slug: microsoft-azure-cost-management-costallocationruledefinitions-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Poll the asynchronous cost details report operation and retrieve the download link for the generated file.
  name: Azure Cost Management Generate Cost Details Report API
  slug: microsoft-azure-cost-management-generatecostdetailsreport-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Retrieve the result of a long-running detailed cost report operation.
  name: Azure Cost Management Generate Detailed Cost Report Operation Results API
  slug: microsoft-azure-cost-management-generatedetailedcostreportoperationresults-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Retrieve the status of a long-running detailed cost report operation.
  name: Azure Cost Management Generate Detailed Cost Report Operation Status API
  slug: microsoft-azure-cost-management-generatedetailedcostreportoperationstatus-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Manage partner markup rules applied at a billing profile.
  name: Azure Cost Management Markup Rules API
  slug: microsoft-azure-cost-management-markuprules-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: 'The tenant- and scope-level Cost Management surface that is not a managed resource: Query, Forecast, Dimensions, cost details and detailed cost report generation, price sheet downloads, benefit recomm'
  name: Azure Cost Management Providers API
  slug: microsoft-azure-cost-management-providers-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Manage scope-scoped scheduled actions that email a saved view on a recurrence, and run them on demand.
  name: Azure Cost Management Scheduled Action Operation Group API
  slug: microsoft-azure-cost-management-scheduledactionoperationgroup-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Manage scheduled actions that email a saved Cost Analysis view on a recurrence, and run them on demand.
  name: Azure Cost Management Scheduled Actions API
  slug: microsoft-azure-cost-management-scheduledactions-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Read and write Cost Management settings at a scope.
  name: Azure Cost Management Settings API
  slug: microsoft-azure-cost-management-settings-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Manage saved Cost Analysis views scoped to a subscription, resource group, management group or billing account.
  name: Azure Cost Management View Operation Group API
  slug: microsoft-azure-cost-management-viewoperationgroup-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Manage saved Cost Analysis views — the persisted form of a cost query — at a scope or at the tenant.
  name: Azure Cost Management Views API
  slug: microsoft-azure-cost-management-views-api
artifact_total: 188
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Cost Management REST Exports API
  slug: open-microsoft-azure-cost-management-exports-api
- collection_type: open
  name: Azure Cost Management REST Exports Operations API
  slug: open-microsoft-azure-cost-management-operations-api
- collection_type: open
  name: Azure Cost Management REST API
  slug: open-microsoft-azure-cost-management
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/security/microsoft-azure-cost-management-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-azure-cost-management-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/security/microsoft-azure-cost-management-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-azure-cost-management-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/agentic-access/microsoft-azure-cost-management-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-cost-management-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/security/microsoft-azure-cost-management-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-cost-management-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/authentication/microsoft-azure-cost-management-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-cost-management-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/scopes/microsoft-azure-cost-management-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-cost-management-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/cost-management/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.microsoft.com/en-us/privacy/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/rest/api/cost-management/
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/rest/api/cost-management/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/manage-automation
- group: start
  title: ''
  type: SignUp
  url: https://azure.microsoft.com/en-us/free/
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/
- group: operate
  title: ''
  type: Roadmap
  url: https://azure.microsoft.com/en-us/updates/?updateType=in-development
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/packages/microsoft-azure-cost-management-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-azure-cost-management-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/packages/microsoft-azure-cost-management-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-azure-cost-management-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/cli/microsoft-azure-cost-management-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-azure-cost-management-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/well-known/microsoft-azure-cost-management-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-azure-cost-management-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/well-known/microsoft-azure-cost-management-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-azure-cost-management-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/llms/microsoft-azure-cost-management-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-azure-cost-management-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/conventions/microsoft-azure-cost-management-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-azure-cost-management-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/conventions/microsoft-azure-cost-management-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/microsoft-azure-cost-management-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/errors/microsoft-azure-cost-management-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-azure-cost-management-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/lifecycle/microsoft-azure-cost-management-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-azure-cost-management-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.status.microsoft/en-us/status
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/lifecycle/policies/modern
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/changelog/microsoft-azure-cost-management-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/microsoft-azure-cost-management-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/conformance/microsoft-azure-cost-management-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-azure-cost-management-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/conformance/microsoft-azure-cost-management-conformance.yml
  title: ''
  type: Compliance
  url: conformance/microsoft-azure-cost-management-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/data-model/microsoft-azure-cost-management-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-azure-cost-management-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/security/microsoft-azure-cost-management-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/microsoft-azure-cost-management-vulnerability-disclosure.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/rate-limits/microsoft-azure-cost-management-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-cost-management-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/plans/microsoft-azure-cost-management-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-cost-management-plans-pricing.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/finops/microsoft-azure-cost-management-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-azure-cost-management-finops.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/examples/_index.yml
  title: ''
  type: Examples
  url: examples/_index.yml
created: '2026-05-04'
description: Microsoft Cost Management is the Azure Resource Manager resource provider (Microsoft.CostManagement) for understanding and controlling cloud spend. Its REST API covers multidimensional cost and usage queries, forecasting, budgets and their alert thresholds, saved Cost Analysis views, scheduled actions that email those views, recurring data exports to customer-owned storage, cost allocation and partner markup rules, reservation and savings-plan benefit recommendations, and asynchronous cost detail and price sheet report generation. Exports can emit the FinOps Foundation's FOCUS schema, so Azure cost data lands in the same shape as other clouds. The service is included with Azure at no additional cost; what is rationed is throughput, through a per-tenant Query Processing Unit budget.
examples:
- key_count: 4
  name: Benefitrecommendationsbybillingaccount
  slug: BenefitRecommendationsByBillingAccount
- key_count: 4
  name: Benefitrecommendationsbybillingaccountformanagementgroup
  slug: BenefitRecommendationsByBillingAccountForManagementGroup
- key_count: 4
  name: Billingaccountalerts
  slug: BillingAccountAlerts
- key_count: 4
  name: Billingaccountdimensionslist
  slug: BillingAccountDimensionsList
- key_count: 4
  name: Billingaccountdimensionslistexpandandtop
  slug: BillingAccountDimensionsListExpandAndTop
- key_count: 4
  name: Billingaccountdimensionslistwithfilter
  slug: BillingAccountDimensionsListWithFilter
- key_count: 4
  name: Billingaccountforecast
  slug: BillingAccountForecast
- key_count: 4
  name: Billingaccountquery
  slug: BillingAccountQuery
- key_count: 4
  name: Billingaccountquerygrouping
  slug: BillingAccountQueryGrouping
- key_count: 4
  name: Billingprofilealerts
  slug: BillingProfileAlerts
- key_count: 4
  name: Billingprofileforecast
  slug: BillingProfileForecast
- key_count: 4
  name: Costallocationrulechecknameavailability
  slug: CostAllocationRuleCheckNameAvailability
- key_count: 4
  name: Costallocationrulecreate
  slug: CostAllocationRuleCreate
- key_count: 4
  name: Costallocationrulecreatetag
  slug: CostAllocationRuleCreateTag
- key_count: 4
  name: Costallocationruledelete
  slug: CostAllocationRuleDelete
- key_count: 4
  name: Costallocationruleget
  slug: CostAllocationRuleGet
- key_count: 4
  name: Costallocationruleslist
  slug: CostAllocationRulesList
- key_count: 4
  name: Costdetailsoperationresultsbysubscriptionscope
  slug: CostDetailsOperationResultsBySubscriptionScope
- key_count: 4
  name: Departmentalerts
  slug: DepartmentAlerts
- key_count: 4
  name: Departmentdimensionslist
  slug: DepartmentDimensionsList
- key_count: 4
  name: Departmentdimensionslistexpandandtop
  slug: DepartmentDimensionsListExpandAndTop
- key_count: 4
  name: Departmentdimensionslistwithfilter
  slug: DepartmentDimensionsListWithFilter
- key_count: 4
  name: Departmentforecast
  slug: DepartmentForecast
- key_count: 4
  name: Departmentquery
  slug: DepartmentQuery
- key_count: 4
  name: Departmentquerygrouping
  slug: DepartmentQueryGrouping
- key_count: 4
  name: Dismissresourcegroupalerts
  slug: DismissResourceGroupAlerts
- key_count: 4
  name: Dismisssubscriptionalerts
  slug: DismissSubscriptionAlerts
- key_count: 4
  name: Eapricesheetforbillingperiod
  slug: EAPriceSheetForBillingPeriod
- key_count: 4
  name: Enrollmentaccountalerts
  slug: EnrollmentAccountAlerts
- key_count: 4
  name: Enrollmentaccountdimensionslist
  slug: EnrollmentAccountDimensionsList
- key_count: 4
  name: Enrollmentaccountdimensionslistexpandandtop
  slug: EnrollmentAccountDimensionsListExpandAndTop
- key_count: 4
  name: Enrollmentaccountdimensionslistwithfilter
  slug: EnrollmentAccountDimensionsListWithFilter
- key_count: 4
  name: Enrollmentaccountforecast
  slug: EnrollmentAccountForecast
- key_count: 4
  name: Enrollmentaccountquery
  slug: EnrollmentAccountQuery
- key_count: 4
  name: Enrollmentaccountquerygrouping
  slug: EnrollmentAccountQueryGrouping
- key_count: 4
  name: Exportcreateorupdatebybillingaccount
  slug: ExportCreateOrUpdateByBillingAccount
- key_count: 4
  name: Exportcreateorupdatebybillingaccountcustom
  slug: ExportCreateOrUpdateByBillingAccountCustom
- key_count: 4
  name: Exportcreateorupdatebybillingaccountmonthly
  slug: ExportCreateOrUpdateByBillingAccountMonthly
- key_count: 4
  name: Exportcreateorupdatebybillingaccountpricesheet
  slug: ExportCreateOrUpdateByBillingAccountPricesheet
- key_count: 4
  name: Exportcreateorupdatebybillingaccountreservationdetails
  slug: ExportCreateOrUpdateByBillingAccountReservationDetails
- key_count: 4
  name: Exportcreateorupdatebybillingaccountreservationrecommendation
  slug: ExportCreateOrUpdateByBillingAccountReservationRecommendation
- key_count: 4
  name: Exportcreateorupdatebybillingaccountreservationtransactions
  slug: ExportCreateOrUpdateByBillingAccountReservationTransactions
- key_count: 4
  name: Exportcreateorupdatebydepartment
  slug: ExportCreateOrUpdateByDepartment
- key_count: 4
  name: Exportcreateorupdatebyenrollmentaccount
  slug: ExportCreateOrUpdateByEnrollmentAccount
- key_count: 4
  name: Exportcreateorupdatebymanagementgroup
  slug: ExportCreateOrUpdateByManagementGroup
- key_count: 4
  name: Exportcreateorupdatebyresourcegroup
  slug: ExportCreateOrUpdateByResourceGroup
- key_count: 4
  name: Exportcreateorupdatebysubscription
  slug: ExportCreateOrUpdateBySubscription
- key_count: 4
  name: Exportdeletebybillingaccount
  slug: ExportDeleteByBillingAccount
- key_count: 4
  name: Exportdeletebydepartment
  slug: ExportDeleteByDepartment
- key_count: 4
  name: Exportdeletebyenrollmentaccount
  slug: ExportDeleteByEnrollmentAccount
- key_count: 4
  name: Exportdeletebymanagementgroup
  slug: ExportDeleteByManagementGroup
- key_count: 4
  name: Exportdeletebyresourcegroup
  slug: ExportDeleteByResourceGroup
- key_count: 4
  name: Exportdeletebysubscription
  slug: ExportDeleteBySubscription
- key_count: 4
  name: Exportgetbybillingaccount
  slug: ExportGetByBillingAccount
- key_count: 4
  name: Exportgetbydepartment
  slug: ExportGetByDepartment
- key_count: 4
  name: Exportgetbyenrollmentaccount
  slug: ExportGetByEnrollmentAccount
- key_count: 4
  name: Exportgetbymanagementgroup
  slug: ExportGetByManagementGroup
- key_count: 4
  name: Exportgetbyresourcegroup
  slug: ExportGetByResourceGroup
- key_count: 4
  name: Exportgetbysubscription
  slug: ExportGetBySubscription
- key_count: 4
  name: Exportrunbybillingaccount
  slug: ExportRunByBillingAccount
- key_count: 4
  name: Exportrunbybillingaccountwithoptionalrequestbody
  slug: ExportRunByBillingAccountWithOptionalRequestBody
- key_count: 4
  name: Exportrunbydepartment
  slug: ExportRunByDepartment
- key_count: 4
  name: Exportrunbyenrollmentaccount
  slug: ExportRunByEnrollmentAccount
- key_count: 4
  name: Exportrunbymanagementgroup
  slug: ExportRunByManagementGroup
- key_count: 4
  name: Exportrunbyresourcegroup
  slug: ExportRunByResourceGroup
- key_count: 4
  name: Exportrunbysubscription
  slug: ExportRunBySubscription
- key_count: 4
  name: Exportrunhistorygetbybillingaccount
  slug: ExportRunHistoryGetByBillingAccount
- key_count: 4
  name: Exportrunhistorygetbydepartment
  slug: ExportRunHistoryGetByDepartment
- key_count: 4
  name: Exportrunhistorygetbyenrollmentaccount
  slug: ExportRunHistoryGetByEnrollmentAccount
- key_count: 4
  name: Exportrunhistorygetbymanagementgroup
  slug: ExportRunHistoryGetByManagementGroup
- key_count: 4
  name: Exportrunhistorygetbyresourcegroup
  slug: ExportRunHistoryGetByResourceGroup
- key_count: 4
  name: Exportrunhistorygetbysubscription
  slug: ExportRunHistoryGetBySubscription
- key_count: 4
  name: Exportsgetbybillingaccount
  slug: ExportsGetByBillingAccount
- key_count: 4
  name: Exportsgetbydepartment
  slug: ExportsGetByDepartment
- key_count: 4
  name: Exportsgetbyenrollmentaccount
  slug: ExportsGetByEnrollmentAccount
- key_count: 4
  name: Exportsgetbymanagementgroup
  slug: ExportsGetByManagementGroup
- key_count: 4
  name: Exportsgetbyresourcegroup
  slug: ExportsGetByResourceGroup
- key_count: 4
  name: Exportsgetbysubscription
  slug: ExportsGetBySubscription
- key_count: 4
  name: Externalbillingaccountalerts
  slug: ExternalBillingAccountAlerts
- key_count: 4
  name: Externalbillingaccountforecast
  slug: ExternalBillingAccountForecast
- key_count: 4
  name: Externalbillingaccountsdimensions
  slug: ExternalBillingAccountsDimensions
- key_count: 4
  name: Externalbillingaccountsquery
  slug: ExternalBillingAccountsQuery
- key_count: 4
  name: Externalsubscriptionalerts
  slug: ExternalSubscriptionAlerts
- key_count: 4
  name: Externalsubscriptionforecast
  slug: ExternalSubscriptionForecast
- key_count: 4
  name: Externalsubscriptionsdimensions
  slug: ExternalSubscriptionsDimensions
- key_count: 4
  name: Externalsubscriptionsquery
  slug: ExternalSubscriptionsQuery
- key_count: 4
  name: Generatecostdetailsreportbybillingaccountenterpriseagreementcustomerandbillingperiod
  slug: GenerateCostDetailsReportByBillingAccountEnterpriseAgreementCustomerAndBillingPeriod
- key_count: 4
  name: Generatecostdetailsreportbybillingprofileandinvoiceid
  slug: GenerateCostDetailsReportByBillingProfileAndInvoiceId
- key_count: 4
  name: Generatecostdetailsreportbybillingprofileandinvoiceidandcustomerid
  slug: GenerateCostDetailsReportByBillingProfileAndInvoiceIdAndCustomerId
- key_count: 4
  name: Generatecostdetailsreportbycustomerandtimeperiod
  slug: GenerateCostDetailsReportByCustomerAndTimePeriod
- key_count: 4
  name: Generatecostdetailsreportbydepartmentsandtimeperiod
  slug: GenerateCostDetailsReportByDepartmentsAndTimePeriod
- key_count: 4
  name: Generatecostdetailsreportbyenrollmentaccountsandtimeperiod
  slug: GenerateCostDetailsReportByEnrollmentAccountsAndTimePeriod
- key_count: 4
  name: Generatecostdetailsreportbysubscriptionandtimeperiod
  slug: GenerateCostDetailsReportBySubscriptionAndTimePeriod
- key_count: 4
  name: Generatedetailedcostreportbybillingaccountlegacyandbillingperiod
  slug: GenerateDetailedCostReportByBillingAccountLegacyAndBillingPeriod
- key_count: 4
  name: Generatedetailedcostreportbybillingprofileandinvoiceid
  slug: GenerateDetailedCostReportByBillingProfileAndInvoiceId
- key_count: 4
  name: Generatedetailedcostreportbybillingprofileandinvoiceidandcustomerid
  slug: GenerateDetailedCostReportByBillingProfileAndInvoiceIdAndCustomerId
- key_count: 4
  name: Generatedetailedcostreportbycustomerandtimeperiod
  slug: GenerateDetailedCostReportByCustomerAndTimePeriod
- key_count: 4
  name: Generatedetailedcostreportbysubscriptionandtimeperiod
  slug: GenerateDetailedCostReportBySubscriptionAndTimePeriod
- key_count: 4
  name: Generatedetailedcostreportoperationresultsbysubscriptionscope
  slug: GenerateDetailedCostReportOperationResultsBySubscriptionScope
- key_count: 4
  name: Generatedetailedcostreportoperationstatusbysubscriptionscope
  slug: GenerateDetailedCostReportOperationStatusBySubscriptionScope
- key_count: 4
  name: Generatereservationdetailsreportbybillingaccount
  slug: GenerateReservationDetailsReportByBillingAccount
- key_count: 4
  name: Generatereservationdetailsreportbybillingprofile
  slug: GenerateReservationDetailsReportByBillingProfile
- key_count: 4
  name: Invoicesectionalerts
  slug: InvoiceSectionAlerts
- key_count: 4
  name: Invoicesectionforecast
  slug: InvoiceSectionForecast
- key_count: 4
  name: Mcabillingaccountdimensionslist
  slug: MCABillingAccountDimensionsList
- key_count: 4
  name: Mcabillingaccountdimensionslistexpandandtop
  slug: MCABillingAccountDimensionsListExpandAndTop
- key_count: 4
  name: Mcabillingaccountdimensionslistwithfilter
  slug: MCABillingAccountDimensionsListWithFilter
- key_count: 4
  name: Mcabillingaccountquery
  slug: MCABillingAccountQuery
- key_count: 4
  name: Mcabillingaccountquerygrouping
  slug: MCABillingAccountQueryGrouping
- key_count: 4
  name: Mcabillingprofiledimensionslist
  slug: MCABillingProfileDimensionsList
- key_count: 4
  name: Mcabillingprofiledimensionslistexpandandtop
  slug: MCABillingProfileDimensionsListExpandAndTop
- key_count: 4
  name: Mcabillingprofiledimensionslistwithfilter
  slug: MCABillingProfileDimensionsListWithFilter
- key_count: 4
  name: Mcabillingprofilequery
  slug: MCABillingProfileQuery
- key_count: 4
  name: Mcabillingprofilequerygrouping
  slug: MCABillingProfileQueryGrouping
- key_count: 4
  name: Mcacustomerdimensionslist
  slug: MCACustomerDimensionsList
- key_count: 4
  name: Mcacustomerdimensionslistexpandandtop
  slug: MCACustomerDimensionsListExpandAndTop
- key_count: 4
  name: Mcacustomerdimensionslistwithfilter
  slug: MCACustomerDimensionsListWithFilter
- key_count: 4
  name: Mcacustomerquery
  slug: MCACustomerQuery
- key_count: 4
  name: Mcacustomerquerygrouping
  slug: MCACustomerQueryGrouping
- key_count: 4
  name: Mcainvoicesectiondimensionslist
  slug: MCAInvoiceSectionDimensionsList
- key_count: 4
  name: Mcainvoicesectiondimensionslistexpandandtop
  slug: MCAInvoiceSectionDimensionsListExpandAndTop
- key_count: 4
  name: Mcainvoicesectiondimensionslistwithfilter
  slug: MCAInvoiceSectionDimensionsListWithFilter
- key_count: 4
  name: Mcainvoicesectionquery
  slug: MCAInvoiceSectionQuery
- key_count: 4
  name: Mcainvoicesectionquerygrouping
  slug: MCAInvoiceSectionQueryGrouping
- key_count: 4
  name: Managementgroupdimensionslist
  slug: ManagementGroupDimensionsList
- key_count: 4
  name: Managementgroupdimensionslistexpandandtop
  slug: ManagementGroupDimensionsListExpandAndTop
- key_count: 4
  name: Managementgroupdimensionslistwithfilter
  slug: ManagementGroupDimensionsListWithFilter
- key_count: 4
  name: Managementgroupquery
  slug: ManagementGroupQuery
- key_count: 4
  name: Managementgroupquerygrouping
  slug: ManagementGroupQueryGrouping
- key_count: 4
  name: Markuprulescreateorupdate
  slug: MarkupRulesCreateOrUpdate
- key_count: 4
  name: Markuprulesdelete
  slug: MarkupRulesDelete
- key_count: 4
  name: Markuprulesget
  slug: MarkupRulesGet
- key_count: 4
  name: Markupruleslist
  slug: MarkupRulesList
- key_count: 4
  name: Operationlist
  slug: OperationList
- key_count: 4
  name: Pricesheetdownload
  slug: PricesheetDownload
- key_count: 4
  name: Pricesheetdownloadbybillingprofile
  slug: PricesheetDownloadByBillingProfile
- key_count: 4
  name: Privateview
  slug: PrivateView
- key_count: 4
  name: Privateviewcreateorupdate
  slug: PrivateViewCreateOrUpdate
- key_count: 4
  name: Privateviewdelete
  slug: PrivateViewDelete
- key_count: 4
  name: Privateviewlist
  slug: PrivateViewList
- key_count: 4
  name: Resourcegroupalerts
  slug: ResourceGroupAlerts
- key_count: 4
  name: Resourcegroupdimensionslist
  slug: ResourceGroupDimensionsList
- key_count: 4
  name: Resourcegroupforecast
  slug: ResourceGroupForecast
- key_count: 4
  name: Resourcegroupquery
  slug: ResourceGroupQuery
- key_count: 4
  name: Resourcegroupquerygrouping
  slug: ResourceGroupQueryGrouping
- key_count: 4
  name: Singleresourcegroupalert
  slug: SingleResourceGroupAlert
- key_count: 4
  name: Singlesubscriptionalert
  slug: SingleSubscriptionAlert
- key_count: 4
  name: Subscriptionalerts
  slug: SubscriptionAlerts
- key_count: 4
  name: Subscriptiondimensionslist
  slug: SubscriptionDimensionsList
- key_count: 4
  name: Subscriptionforecast
  slug: SubscriptionForecast
- key_count: 4
  name: Subscriptionquery
  slug: SubscriptionQuery
- key_count: 4
  name: Subscriptionquerygrouping
  slug: SubscriptionQueryGrouping
- key_count: 4
  name: Viewbyresourcegroup
  slug: ViewByResourceGroup
- key_count: 4
  name: Viewcreateorupdatebyresourcegroup
  slug: ViewCreateOrUpdateByResourceGroup
- key_count: 4
  name: Viewdeletebyresourcegroup
  slug: ViewDeleteByResourceGroup
- key_count: 4
  name: Viewlistbyresourcegroup
  slug: ViewListByResourceGroup
- key_count: 4
  name: Setting Delete
  slug: setting-delete
- key_count: 4
  name: Setting Get
  slug: setting-get
- key_count: 4
  name: Settings Createorupdate
  slug: settings-createOrUpdate
- key_count: 4
  name: Settingslist
  slug: settingsList
finops:
- name: Microsoft Azure Cost Management Finops
  service_category: API
  slug: microsoft-azure-cost-management-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-cost-management.png
layout: provider
modified: '2026-09-17'
name: Azure Cost Management
nav: Providers
network: true
overview: 'Azure Cost Management publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Exports API, Operations API, Alerts API, and 12 more. Tagged areas include Cost Management, FinOps, Cloud Cost, Billing, and Budgets.


  Azure Cost Management''s developer surface includes authentication, developer portal, pricing, support, documentation, API reference, getting-started guide, and 34 more developer resources.'
plans:
- name: Microsoft Azure Cost Management Plans Pricing
  plan_count: 1
  slug: microsoft-azure-cost-management-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Microsoft Azure Cost Management Rate Limits
  slug: microsoft-azure-cost-management-rate-limits
scopes:
- name: Microsoft Azure Cost Management Scopes
  scope_count: 1
  slug: microsoft-azure-cost-management-scopes
  summary_line: 1 scope · implicit
score:
  band: strong
  composite: 65.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 89.5
    contract_governance: 0.0
    contract_quality: 46.9
    developer_ergonomics: 73.2
    discoverability: 75.9
    operational_transparency: 89.5
  previous_composite: 65.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/screenshots/microsoft-azure-cost-management-2026-06-20T185407.png
security:
- kind: authentication
  name: Microsoft Azure Cost Management Authentication
  slug: microsoft-azure-cost-management-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Cost Management Domain Security
  slug: microsoft-azure-cost-management-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Azure Cost Management Vulnerability Disclosure
  slug: microsoft-azure-cost-management-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Azure Cost Management Trust Center
  slug: microsoft-azure-cost-management-trust-center
  summary_line: GDPR
slug: microsoft-azure-cost-management
tags:
- Cost Management
- FinOps
- Cloud Cost
- Billing
- Budgets
- Export
- Cost Analysis
- Forecasting
- Chargebacks
- Focus
- Azure
- Reservations
website: https://www.microsoft.com/
---

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
    error_semantics: derived
    event_surface_described: false
    idempotency: derived
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.9
  scored_at: '2026-10-04'
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
  phrasing_intents:
  - id: Exports_List
    intent: List cost exports at any scope
    question: What scheduled cost data exports are configured at my billing scope?
  - id: Exports_Get
    intent: Get a cost export at a scope by name
    question: Where does a particular cost export write its files and on what schedule?
  - id: Exports_CreateOrUpdate
    intent: Create or update a scheduled cost export
    question: How do I set up a daily export of cost data to a storage account at a billing scope?
  - id: Exports_Delete
    intent: Delete a cost export at a scope
    question: How do I stop and remove a cost export at my billing account scope?
  - id: Exports_Execute
    intent: Run a cost export now
    question: Can I trigger a cost export immediately instead of waiting for its schedule?
  - id: Exports_GetExecutionHistory
    intent: Get an export's run history
    question: Did my cost export succeed the last few times it ran?
  - id: listExportsBySubscription
    intent: List export resources in a subscription
    question: Which export resources exist across a whole subscription, by subscription ID?
  - id: listExportsByResourceGroup
    intent: List export resources in a resource group
    question: What export resources are deployed in a specific resource group?
  phrasing_ops: 12
  slug: microsoft-azure-cost-management-exports-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: List every REST operation the Microsoft.CostManagement resource provider exposes.
  name: Azure Cost Management Operations API
  phrasing_intents:
  - id: Operations_List
    intent: List available Cost Management operations
    question: What operations does the Azure Cost Management resource provider support?
  phrasing_ops: 1
  slug: microsoft-azure-cost-management-operations-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: List, read and dismiss the cost alerts raised by budgets and anomaly detection at a scope.
  name: Azure Cost Management Alerts API
  phrasing_intents:
  - id: Alerts_List
    intent: List cost alerts for a scope
    question: How do I see all the cost alerts raised for my Azure subscription?
  - id: Alerts_Get
    intent: Get one cost alert by ID
    question: What are the details of a specific cost alert I was notified about?
  - id: Alerts_Dismiss
    intent: Dismiss a cost alert
    question: How do I dismiss a cost alert I've already dealt with?
  phrasing_ops: 3
  slug: microsoft-azure-cost-management-alerts-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Create, read, update and delete cost and reservation-utilization budgets, with their notification thresholds.
  name: Azure Cost Management Budgets API
  phrasing_intents:
  - id: Budgets_List
    intent: List budgets for a scope
    question: What budgets are set up on my Azure subscription?
  - id: Budgets_Get
    intent: Get a budget by name
    question: How much is left in a particular budget and what are its thresholds?
  - id: Budgets_CreateOrUpdate
    intent: Create or update a budget
    question: How do I set a monthly spending budget with alert thresholds on a subscription?
  - id: Budgets_Delete
    intent: Delete a budget
    question: How do I remove a budget I no longer need?
  phrasing_ops: 4
  slug: microsoft-azure-cost-management-budgets-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Manage rules that redistribute shared cost between scopes within a billing account.
  name: Azure Cost Management Cost Allocation Rule Definitions API
  phrasing_intents:
  - id: CostAllocationRules_List
    intent: List cost allocation rules for a billing account
    question: What cost allocation rules exist on my billing account or enterprise enrollment?
  - id: CostAllocationRules_Get
    intent: Get a cost allocation rule by name
    question: Which sources and targets does a specific cost allocation rule use?
  - id: CostAllocationRules_CreateOrUpdate
    intent: Create or update a cost allocation rule
    question: How do I reallocate shared platform costs from one subscription to several others?
  - id: CostAllocationRules_Delete
    intent: Delete a cost allocation rule
    question: How do I stop a cost allocation rule from redistributing costs?
  phrasing_ops: 4
  slug: microsoft-azure-cost-management-costallocationruledefinitions-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Poll the asynchronous cost details report operation and retrieve the download link for the generated file.
  name: Azure Cost Management Generate Cost Details Report API
  phrasing_intents:
  - id: GenerateCostDetailsReport_GetOperationResults
    intent: Get the result of a cost details report
    question: Is my cost details report ready to download yet?
  phrasing_ops: 1
  slug: microsoft-azure-cost-management-generatecostdetailsreport-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Retrieve the result of a long-running detailed cost report operation.
  name: Azure Cost Management Generate Detailed Cost Report Operation Results API
  phrasing_intents:
  - id: GenerateDetailedCostReportOperationResults_Get
    intent: Get the result of a detailed cost report
    question: How do I retrieve the finished detailed cost report after requesting it?
  phrasing_ops: 1
  slug: microsoft-azure-cost-management-generatedetailedcostreportoperationresults-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Retrieve the status of a long-running detailed cost report operation.
  name: Azure Cost Management Generate Detailed Cost Report Operation Status API
  phrasing_intents:
  - id: GenerateDetailedCostReportOperationStatus_Get
    intent: Check a detailed cost report's status
    question: Is my detailed cost report still running or has it completed?
  phrasing_ops: 1
  slug: microsoft-azure-cost-management-generatedetailedcostreportoperationstatus-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Manage partner markup rules applied at a billing profile.
  name: Azure Cost Management Markup Rules API
  phrasing_intents:
  - id: MarkupRules_List
    intent: List markup rules for a billing profile
    question: What markup rules are applied to customer prices on my billing profile?
  - id: MarkupRules_Get
    intent: Get a markup rule by name
    question: What percentage and date range does a specific markup rule use?
  - id: MarkupRules_CreateOrUpdate
    intent: Create or update a markup rule
    question: How do I add a markup on top of Azure costs for a customer's billing profile?
  - id: MarkupRules_Delete
    intent: Delete a markup rule
    question: How do I stop applying a markup to a billing profile's costs?
  phrasing_ops: 4
  slug: microsoft-azure-cost-management-markuprules-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: 'The tenant- and scope-level Cost Management surface that is not a managed resource: Query, Forecast, Dimensions, cost details and detailed cost report generation, price sheet downloads, benefit recomm'
  name: Azure Cost Management Providers API
  phrasing_intents:
  - id: BenefitRecommendations_List
    intent: List savings plan purchase recommendations
    question: Should I buy an Azure savings plan, and how much commitment is recommended for my subscription?
  - id: ScheduledActions_CheckNameAvailabilityByScope
    intent: Check a shared scheduled action name at a scope
    question: Is a name already taken for a shared scheduled action on my subscription?
  - id: Dimensions_List
    intent: List cost dimensions for an Azure scope
    question: Which dimensions, like resource group or meter category, can I group my Azure costs by?
  - id: Forecast_Usage
    intent: Forecast Azure costs for a scope
    question: What will my Azure subscription spend by the end of the month?
  - id: GenerateCostDetailsReport_CreateOperation
    intent: Request a cost details report
    question: What's the current way to get line-item usage details for my subscription now that the older usage APIs are replaced?
  - id: GenerateDetailedCostReport_CreateOperation
    intent: Request a detailed cost report
    question: Can I request a detailed cost report for one customer under my billing account?
  - id: Query_Usage
    intent: Query Azure cost and usage data for a scope
    question: How much did each resource group cost me last month?
  - id: Alerts_ListExternal
    intent: List cost alerts for an external cloud account
    question: What cost alerts exist for my connected external cloud billing account?
  phrasing_ops: 28
  slug: microsoft-azure-cost-management-providers-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Manage scope-scoped scheduled actions that email a saved view on a recurrence, and run them on demand.
  name: Azure Cost Management Scheduled Action Operation Group API
  phrasing_intents:
  - id: ScheduledActions_ListByScope
    intent: List shared scheduled actions at a scope
    question: Which shared scheduled cost emails and alerts are set up on my subscription?
  - id: ScheduledActions_GetByScope
    intent: Get a shared scheduled action by name
    question: Who receives a particular shared scheduled cost email and how often?
  - id: ScheduledActions_CreateOrUpdateByScope
    intent: Create or update a shared scheduled action
    question: How do I email a cost view to my team every week from a subscription scope?
  - id: ScheduledActions_DeleteByScope
    intent: Delete a shared scheduled action
    question: How do I stop a shared scheduled cost email at a subscription scope?
  - id: ScheduledActions_RunByScope
    intent: Run a shared scheduled action now
    question: Can I send a shared scheduled cost email right now instead of waiting?
  phrasing_ops: 5
  slug: microsoft-azure-cost-management-scheduledactionoperationgroup-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Manage scheduled actions that email a saved Cost Analysis view on a recurrence, and run them on demand.
  name: Azure Cost Management Scheduled Actions API
  phrasing_intents:
  - id: ScheduledActions_List
    intent: List my private scheduled actions
    question: What private scheduled cost emails have I set up for myself?
  - id: ScheduledActions_Get
    intent: Get a private scheduled action by name
    question: When does my private scheduled cost email next run?
  - id: ScheduledActions_CreateOrUpdate
    intent: Create or update a private scheduled action
    question: How do I schedule a private cost report email just for myself?
  - id: ScheduledActions_Delete
    intent: Delete a private scheduled action
    question: How do I cancel a private scheduled cost email I created?
  - id: ScheduledActions_Run
    intent: Run a private scheduled action now
    question: Can I send my private scheduled cost email immediately?
  phrasing_ops: 5
  slug: microsoft-azure-cost-management-scheduledactions-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Read and write Cost Management settings at a scope.
  name: Azure Cost Management Settings API
  phrasing_intents:
  - id: Settings_List
    intent: List Cost Management settings for a scope
    question: What Cost Management settings are configured at my scope?
  - id: Settings_GetByScope
    intent: Get one Cost Management setting
    question: Is a specific cost setting such as tag inheritance turned on for my scope?
  - id: Settings_CreateOrUpdateByScope
    intent: Create or update a Cost Management setting
    question: How do I turn on tag inheritance for cost data at a billing scope?
  - id: Settings_DeleteByScope
    intent: Delete a Cost Management setting
    question: How do I remove a cost setting and go back to the default behavior?
  phrasing_ops: 4
  slug: microsoft-azure-cost-management-settings-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Manage saved Cost Analysis views scoped to a subscription, resource group, management group or billing account.
  name: Azure Cost Management View Operation Group API
  phrasing_intents:
  - id: Views_ListByScope
    intent: List saved cost views at a scope
    question: What saved cost analysis views are shared on my subscription?
  - id: Views_GetByScope
    intent: Get a saved cost view at a scope
    question: How is a saved cost view at my scope grouped and filtered?
  - id: Views_CreateOrUpdateByScope
    intent: Create or update a saved cost view at a scope
    question: How do I save a cost analysis view that everyone on a subscription can use?
  - id: Views_DeleteByScope
    intent: Delete a saved cost view at a scope
    question: How do I remove a shared cost view from a subscription?
  phrasing_ops: 4
  slug: microsoft-azure-cost-management-viewoperationgroup-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Manage saved Cost Analysis views — the persisted form of a cost query — at a scope or at the tenant.
  name: Azure Cost Management Views API
  phrasing_intents:
  - id: Views_List
    intent: List my private cost views
    question: What private cost analysis views have I saved?
  - id: Views_Get
    intent: Get one of my private cost views
    question: How is my private cost view configured?
  - id: Views_CreateOrUpdate
    intent: Create or update a private cost view
    question: How do I save a personal cost analysis view only I can see?
  - id: Views_Delete
    intent: Delete a private cost view
    question: How do I delete a personal cost view I no longer use?
  phrasing_ops: 4
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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/capabilities/microsoft-azure-cost-management-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-azure-cost-management-capability-edges.yml
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


  Azure Cost Management''s developer surface includes authentication, developer portal, pricing, support, documentation, API reference, getting-started guide, and 35 more developer resources.'
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
  band: exemplar
  composite: 69.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.0
  facets:
    access_clarity: 89.5
    contract_governance: 0.0
    contract_quality: 46.1
    developer_ergonomics: 73.2
    discoverability: 73.2
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
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
- Reserved Instances
website: https://www.microsoft.com/
---

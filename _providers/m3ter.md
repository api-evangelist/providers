---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 175
  human_in_the_loop: 0
  name: M3Ter Agentic Access
  operation_count: 323
  slug: m3ter-agentic-access
  summary_line: 323 operations · 175 acting
api_count: 1
apis:
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for Account related operations such as creation, update, list and delete. An Account represents one of your end-customer accounts. Accounts do not belong to a Product to allow for cases wher
  name: M3ter Account API
  slug: m3ter-account-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for AccountPlan and AccountPlanGroup related operations such as creation, update, list and delete. **AccountPlans** An Account represents one of your end-customer accounts. To create an Acco
  name: M3ter AccountPlan API
  slug: m3ter-accountplan-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for listing, creating, updating, retrieving, or deleting Aggregations. An Aggregation links to a Meter and targets a Data Field or Derived Field on the Meter. You define the method of aggreg
  name: M3ter Aggregation API
  slug: m3ter-aggregation-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoint for retrieving a JSON Web Token (JWT) bearer token for a ServiceUser using the Client Credentials Grant flow. A ServiceUser represents the automated process you want to grant access to your O
  name: M3ter Auth API
  slug: m3ter-auth-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for creating/updating/deleting BalanceChargeSchedules. **NOTE!** The BalanceChargeSchedule feature is available in Beta release version. See [Feature Release Stages](https://www.m3ter.com/do
  name: M3ter BalanceChargeSchedule API
  slug: m3ter-balancechargeschedule-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: 'Endpoints for creating/retrieving/updating/deleting Balances on Accounts. When you have created a Balance for an Account, you can create a positive or negative Transaction amounts for the Balance. To '
  name: M3ter Balances API
  slug: m3ter-balances-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for creating/updating/deleting BalanceTransactionSchedules. **NOTE!** The BalanceTransactionSchedule feature is available in Beta release version. See [Feature Release Stages](https://www.m3
  name: M3ter BalanceTransactionSchedule API
  slug: m3ter-balancetransactionschedule-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: 'Endpoints for billing operations such as creating, updating, listing,downloading, and deleting Bills. Bills are generated for an Account, and are calculated in accordance with the usage-based pricing '
  name: M3ter Bill API
  slug: m3ter-bill-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for updating and retreiving the Bill Configuration for an Organization. The Organization represents your company as a direct customer of the m3ter service. You can use the **Update BillConfi
  name: M3ter BillConfig API
  slug: m3ter-billconfig-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for Bill Grouping Key operations such as creation, update, list, and delete. Bill Grouping Keys are stored for your Organization, and you can use them to control billing operations. For exam
  name: M3ter BillGroupingKey API
  slug: m3ter-billgroupingkey-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for creating, retrieving, listing, and cancelling Bill Jobs. Bill Jobs are critical components in billing management, providing asynchronous mechanisms to calculate and handle bills. Bill Jo
  name: M3ter BillJob API
  slug: m3ter-billjob-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: 'Endpoints for creating/updating/deleting Charges. Create Charges for your end-customer Accounts to create ad-hoc line items for Account billing. Charges are: * Created for either debit or credit amoun'
  name: M3ter Charge API
  slug: m3ter-charge-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints that manage Commitments *(also known as Prepayments)* in the context of usage-based pricing and billing. A Commitment represents an agreement where the end-customer has agreed to pay a fixed
  name: M3ter Commitments API
  slug: m3ter-commitments-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for Compound Aggregation related operations such as creation, update, list and delete. Use Compound Aggregations to create numerical measures from usage data by applying a calculation to one
  name: M3ter CompoundAggregation API
  slug: m3ter-compoundaggregation-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: 'Endpoints for Contract related operations such as creation, update, list and delete. Contracts are created for Accounts, which are your end-user customers. Contracts can be used for: * **Accounts Repo'
  name: M3ter Contract API
  slug: m3ter-contract-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for listing, creating, retrieving, updating, or deleting Counters. You can create Counters for your m3ter Organization, which can then be used as pricing metrics to apply a unit-based [Count
  name: M3ter Counter API
  slug: m3ter-counter-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for listing, creating, updating, retrieving, or deleting CounterAdjustments. If you attach a Plan to an Account which is priced using a Counter to apply unit-based pricing, you can then crea
  name: M3ter CounterAdjustments API
  slug: m3ter-counteradjustments-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for listing, creating, updating, retrieving, or deleting CounterPricing. Create the CounterPricing for a Plan/PlanTemplate using a Counter, and define a unit-based pricing structure for char
  name: M3ter CounterPricing API
  slug: m3ter-counterpricing-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for CreditReason operations such as creation, update, list, and delete. You can create CreditReasons for your Organization, and then use them when creating a credit line item on a bill, or a
  name: M3ter CreditReason API
  slug: m3ter-creditreason-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: 'Endpoints for Credit line item related operations such as creation, update, list and delete. These are line items on Bills that are specifically related to Credits. You use the Credit Reasons created '
  name: M3ter Credits API
  slug: m3ter-credits-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for Currency operations such as creation, update, list, and delete. Currencies are stored for your Organization, and can then be used to specify currencies on various entities such as plan g
  name: M3ter Currency API
  slug: m3ter-currency-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: 'Endpoints for querying and filtering Usage data collected for your Organization. **IMPORTANT: Request Rate Limits for Data Explorer v2!** As part of the Config API, requests made to the Data Explorer '
  name: M3ter DataExplorerV2 API
  slug: m3ter-dataexplorerv2-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for DebitReason operations such as creation, update, list, and delete. You can create DebitReasons for your Organization, and then use them when creating a debit line item on a bill, or appl
  name: M3ter DebitReason API
  slug: m3ter-debitreason-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for Debit line item related operations such as creation, update, list and delete. These are line items on Bills that are specifically related to Debits. You use the Debit Reasons created for
  name: M3ter Debits API
  slug: m3ter-debits-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: This section provides Endpoints for operations that allow you to retrieve detailed information about individual Events, list all Events or specific Event Types, and explore dynamic fields available fo
  name: M3ter Events API
  slug: m3ter-events-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: 'Endpoints for triggering one-off, ad-hoc Data Exports. You can set up and run ad-hoc Exports to export two kinds of data from your m3ter Organization: * Usage data. * Operational data for entities. **'
  name: M3ter ExportAdHoc API
  slug: m3ter-exportadhoc-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for creating, updating, retrieving, or deleting Data Export Destinations. Before you can configure and run either [Export Schedules](https://www.m3ter.com/docs/api#tag/ExportSchedule) or [Ad
  name: M3ter ExportDestination API
  slug: m3ter-exportdestination-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for creating, updating, retrieving, or deleting Data Export schedules. You can set up an Export Schedule to export one of two types of data from your m3ter Organization - either *Usage data*
  name: M3ter ExportSchedule API
  slug: m3ter-exportschedule-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for managing External Mapping related operations such as creation, update, list and delete. When you integrate your 3rd-party systems with the m3ter platform, a mapping between entities in t
  name: M3ter External Mapping API
  slug: m3ter-external-mapping-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for creating and retrieving user invitations. Use invitations to invite other people to join your m3ter Organization. An invitation sends an email inviting someone to join your Organization.
  name: M3ter Invitations API
  slug: m3ter-invitations-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoint for retrieving a list of line items for Bills in an Organization.
  name: M3ter Line Item API
  slug: m3ter-line-item-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for creating/updating/deleting Lookup Table Revisions. Lookup Tables utilize a "Table and Revision" model, which lets you update data cleanly, and extend the schema without modifying existin
  name: M3ter LookupTableRevision API
  slug: m3ter-lookuptablerevision-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for creating/updating/deleting Data for specific Lookup Table Revisions. When you've added fields to create a data schema for a Lookup Table Revision, you can use upsert operations to create
  name: M3ter LookupTableRevisionData API
  slug: m3ter-lookuptablerevisiondata-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for retrieving reporting data on Marketplace Integration runs
  name: M3ter Marketplace Integrations API
  slug: m3ter-marketplace-integrations-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: 'Endpoints for submitting usage data measurements to the m3ter platform: - **Directly:** You can use the **Submit Measurements** call to submit raw data measurements directly using the **Ingest API**. '
  name: M3ter Measurements API
  slug: m3ter-measurements-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for listing, creating, updating, retrieving, or deleting Meters. Use Meters to submit usage data for the consumption of your products and services by end customers. This usage data then beco
  name: M3ter Meter API
  slug: m3ter-meter-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: 'This section provides endpoints for managing Event Notifications. You can create Notifications based on system Events generated by the platform. When you base a Notification on a specific Event type, '
  name: M3ter Notifications API
  slug: m3ter-notifications-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for retrieving or updating the Organization Config. Organization represents your company as a direct customer of m3ter. Use Organization configuration to define *Organization-wide* settings.
  name: M3ter OrganizationConfig API
  slug: m3ter-organizationconfig-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: This section contains the endpoints for managing users within an Organization *(OrgUsers)*. These endpoints allow you to retrieve, update, and analyze user data, as well as their associated permission
  name: M3ter OrgUsers API
  slug: m3ter-orgusers-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for Permission Policy related operations such as creation, update, add and retrieve. Permission Policies can restrict or grant access to specific resources for both Users *(people)* and Serv
  name: M3ter PermissionPolicy API
  slug: m3ter-permissionpolicy-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for listing, creating, updating, retrieving, or deleting Plans. A Plan is based on a PlanTemplate and represents a specific pricing plan for one of your products or services. Each Plan inher
  name: M3ter Plan API
  slug: m3ter-plan-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for PlanGroup related operations such as creation, update, retrieve, list and delete. PlanGroups are constructs that group multiple plans together. This enables a unified approach to efficie
  name: M3ter PlanGroup API
  slug: m3ter-plangroup-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for PlanGroupLink related operations such as creation, update, list and delete. PlanGroupLinks are the intersection table between a PlanGroup and its associated Plans. A PlanGroupLink is onl
  name: M3ter PlanGroupLink API
  slug: m3ter-plangrouplink-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for listing, creating, updating, retrieving, or deleting PlanTemplates. Use PlanTemplates to define default values for Plans. These default values control the billing operations you want app
  name: M3ter PlanTemplate API
  slug: m3ter-plantemplate-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for listing, creating, updating, retrieving, or deleting Pricing. Create the Pricing for a Plan/PlanTemplate with usage data Aggregations, and define a usage-based pricing structure for char
  name: M3ter Pricing API
  slug: m3ter-pricing-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for listing, creating, updating, retrieving, or deleting Products. A Product represents the products and services you offer to your end customers. Products act as a container for the Meters,
  name: M3ter Product API
  slug: m3ter-product-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for ResourceGroup related operations such as creation, update, list and delete. ResourceGroups are used in the context of Permission Policies, which controls what a User who has been given a
  name: M3ter ResourceGroup API
  slug: m3ter-resourcegroup-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: 'Endpoints for retrieving and managing scheduled Events'' configurations. Scheduled Event Configurations define custom Event types that reference Date/Time fields belonging to configuration and billing '
  name: M3ter ScheduledEventConfigurations API
  slug: m3ter-scheduledeventconfigurations-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for listing, creating, updating, retrieving, or deleting Statement Definitions. Bill statements are informative backing sheets to invoices. They provide a breakdown of the usage charges that
  name: M3ter StatementDefinition API
  slug: m3ter-statementdefinition-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for creating, retrieving, listing, and cancelling statement jobs. StatementJobs are tasks to asynchronously calculate and generate a bill statement. Bill statements are informative backing s
  name: M3ter StatementJob API
  slug: m3ter-statementjob-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for requesting support and managing m3ter Support users. For troubleshooting purposes, you can grant m3ter Support access to your Organization. m3ter Support only has access for a limited ti
  name: M3ter Support API
  slug: m3ter-support-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: 'Endpoints for TransactionType operations such as creation, update, list, retrieve, and delete. You can create TransactionTypes for your Organization, which can then be used when creating and updating '
  name: M3ter TransactionType API
  slug: m3ter-transactiontype-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for creating/updating Users
  name: M3ter User API
  slug: m3ter-user-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for creating/updating/deleting External Mappings
  name: M3ter External Mappings API
  slug: m3ter-externalmappings-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for configuring integrations
  name: M3ter Integration Configs API
  slug: m3ter-integrationconfigs-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for configuring credentials
  name: M3ter Integration Credentials API
  slug: m3ter-integrationcredentials-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: The IntegrationDestinations API from M3ter — 15 operation(s) for integrationdestinations.
  name: M3ter Integration Destinations API
  slug: m3ter-integrationdestinations-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for integration runs
  name: M3ter Integration Runs API
  slug: m3ter-integrationruns-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for configuring transformations
  name: M3ter Integration Transformations API
  slug: m3ter-integrationtransformations-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: 'Endpoints for creating/updating/deleting MeterGroups. MeterGroups represent a logical grouping of Meters. They are not required for billing, but mainly for Analytics purposes. For example: "show me th'
  name: M3ter Meter Group API
  slug: m3ter-metergroup-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for creating/updating/deleting service users
  name: M3ter Service User API
  slug: m3ter-serviceuser-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for creating/activating/deactivating/deleting service user credentials
  name: M3ter Service User Credentials API
  slug: m3ter-serviceusercredentials-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: 'Endpoints for retrieving and updating Custom Fields at the Organization level for all entities that support them. Custom Fields in m3ter allow you to store custom data in the form of number or string '
  name: M3ter Custom Field API
  slug: m3ter-custom-field-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for querying the Data Explorer and saving query selections. The Data Explorer is a m3ter analytics tool, enabling you to query the Usage, Billing, and Prepayments data collected for your Org
  name: M3ter Data Explorer API
  slug: m3ter-data-explorer-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: 'Endpoints for retrieving/querying Data Export jobs. **Preview Version!** The Data Export feature is currently available only in Preview release version. See Feature Release Stages for Preview release '
  name: M3ter Export Job API
  slug: m3ter-export-job-api
- baseURL: https://api.m3ter.com
  baseurl_source: declared
  description: Endpoints for creating/updating/deleting Lookup Tables. Lookup Tables enable you to manage dynamic data mappings that your calculations reference. Use them for currency conversion, pricing tiers, disc
  name: M3ter Lookup Table API
  slug: m3ter-lookup-table-api
artifact_total: 135
collections:
- collection_type: open
  name: m3ter Account API
  slug: open-m3ter-account-api
- collection_type: open
  name: m3ter Account AccountPlan API
  slug: open-m3ter-accountplan-api
- collection_type: open
  name: m3ter Account Aggregation API
  slug: open-m3ter-aggregation-api
- collection_type: open
  name: m3ter Account Auth API
  slug: open-m3ter-auth-api
- collection_type: open
  name: m3ter Account BalanceChargeSchedule API
  slug: open-m3ter-balancechargeschedule-api
- collection_type: open
  name: m3ter Account Balances API
  slug: open-m3ter-balances-api
- collection_type: open
  name: m3ter Account BalanceTransactionSchedule API
  slug: open-m3ter-balancetransactionschedule-api
- collection_type: open
  name: m3ter Account Bill API
  slug: open-m3ter-bill-api
- collection_type: open
  name: m3ter Account BillConfig API
  slug: open-m3ter-billconfig-api
- collection_type: open
  name: m3ter Account BillGroupingKey API
  slug: open-m3ter-billgroupingkey-api
- collection_type: open
  name: m3ter Account BillJob API
  slug: open-m3ter-billjob-api
- collection_type: open
  name: m3ter Account Charge API
  slug: open-m3ter-charge-api
- collection_type: open
  name: m3ter Account Commitments API
  slug: open-m3ter-commitments-api
- collection_type: open
  name: m3ter Account CompoundAggregation API
  slug: open-m3ter-compoundaggregation-api
- collection_type: open
  name: m3ter Account Contract API
  slug: open-m3ter-contract-api
- collection_type: open
  name: m3ter Account Counter API
  slug: open-m3ter-counter-api
- collection_type: open
  name: m3ter Account CounterAdjustments API
  slug: open-m3ter-counteradjustments-api
- collection_type: open
  name: m3ter Account CounterPricing API
  slug: open-m3ter-counterpricing-api
- collection_type: open
  name: m3ter Account CreditReason API
  slug: open-m3ter-creditreason-api
- collection_type: open
  name: m3ter Account Credits API
  slug: open-m3ter-credits-api
- collection_type: open
  name: m3ter Account Currency API
  slug: open-m3ter-currency-api
- collection_type: open
  name: m3ter Account CustomField API
  slug: open-m3ter-customfield-api
- collection_type: open
  name: m3ter Account DataExplorer API
  slug: open-m3ter-dataexplorer-api
- collection_type: open
  name: m3ter Account DataExplorerV2 API
  slug: open-m3ter-dataexplorerv2-api
- collection_type: open
  name: m3ter Account DebitReason API
  slug: open-m3ter-debitreason-api
- collection_type: open
  name: m3ter Account Debits API
  slug: open-m3ter-debits-api
- collection_type: open
  name: m3ter Account Events API
  slug: open-m3ter-events-api
- collection_type: open
  name: m3ter Account ExportAdHoc API
  slug: open-m3ter-exportadhoc-api
- collection_type: open
  name: m3ter Account ExportDestination API
  slug: open-m3ter-exportdestination-api
- collection_type: open
  name: m3ter Account ExportJob API
  slug: open-m3ter-exportjob-api
- collection_type: open
  name: m3ter Account ExportSchedule API
  slug: open-m3ter-exportschedule-api
- collection_type: open
  name: m3ter Account External Mapping API
  slug: open-m3ter-external-mapping-api
- collection_type: open
  name: m3ter Account Integrations API
  slug: open-m3ter-integrations-api
- collection_type: open
  name: m3ter Account Invitations API
  slug: open-m3ter-invitations-api
- collection_type: open
  name: m3ter Account Line Item API
  slug: open-m3ter-line-item-api
- collection_type: open
  name: m3ter Account LookupTable API
  slug: open-m3ter-lookuptable-api
- collection_type: open
  name: m3ter Account LookupTableRevision API
  slug: open-m3ter-lookuptablerevision-api
- collection_type: open
  name: m3ter Account LookupTableRevisionData API
  slug: open-m3ter-lookuptablerevisiondata-api
- collection_type: open
  name: m3ter Account Marketplace Integrations API
  slug: open-m3ter-marketplace-integrations-api
- collection_type: open
  name: m3ter Account Measurements API
  slug: open-m3ter-measurements-api
- collection_type: open
  name: m3ter Account Meter API
  slug: open-m3ter-meter-api
- collection_type: open
  name: m3ter Account Notifications API
  slug: open-m3ter-notifications-api
- collection_type: open
  name: m3ter Account OrganizationConfig API
  slug: open-m3ter-organizationconfig-api
- collection_type: open
  name: m3ter Account OrgUsers API
  slug: open-m3ter-orgusers-api
- collection_type: open
  name: m3ter Account PermissionPolicy API
  slug: open-m3ter-permissionpolicy-api
- collection_type: open
  name: m3ter Account Plan API
  slug: open-m3ter-plan-api
- collection_type: open
  name: m3ter Account PlanGroup API
  slug: open-m3ter-plangroup-api
- collection_type: open
  name: m3ter Account PlanGroupLink API
  slug: open-m3ter-plangrouplink-api
- collection_type: open
  name: m3ter Account PlanTemplate API
  slug: open-m3ter-plantemplate-api
- collection_type: open
  name: m3ter Account Pricing API
  slug: open-m3ter-pricing-api
- collection_type: open
  name: m3ter Account Product API
  slug: open-m3ter-product-api
- collection_type: open
  name: m3ter Account ResourceGroup API
  slug: open-m3ter-resourcegroup-api
- collection_type: open
  name: m3ter Account ScheduledEventConfigurations API
  slug: open-m3ter-scheduledeventconfigurations-api
- collection_type: open
  name: m3ter Account StatementDefinition API
  slug: open-m3ter-statementdefinition-api
- collection_type: open
  name: m3ter Account StatementJob API
  slug: open-m3ter-statementjob-api
- collection_type: open
  name: m3ter Account Support API
  slug: open-m3ter-support-api
- collection_type: open
  name: m3ter Account TransactionType API
  slug: open-m3ter-transactiontype-api
- collection_type: open
  name: m3ter Account User API
  slug: open-m3ter-user-api
- collection_type: open
  name: m3ter API
  slug: open-m3ter
common:
- group: commercial
  href: https://artifacts.apis.io/m3ter/plans/m3ter-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/m3ter-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/m3ter/rate-limits/m3ter-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/m3ter-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/m3ter/finops/m3ter-finops.yml
  title: ''
  type: FinOps
  url: finops/m3ter-finops.yml
- group: other
  href: https://artifacts.apis.io/m3ter/capabilities/m3ter-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/m3ter-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/m3ter/agentic-access/m3ter-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/m3ter-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/m3ter/security/m3ter-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/m3ter-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/m3ter/security/m3ter-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/m3ter-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/m3ter/security/m3ter-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/m3ter-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/m3ter/authentication/m3ter-authentication.yml
  title: ''
  type: Authentication
  url: authentication/m3ter-authentication.yml
- group: auth
  href: https://artifacts.apis.io/m3ter/scopes/m3ter-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/m3ter-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/m3ter
- group: company
  title: ''
  type: Website
  url: https://www.m3ter.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.m3ter.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.m3ter.com/api
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.m3ter.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.m3ter.com/blog/feed/
created: '2026-03-27'
description: 'm3ter is a usage-based billing and metering engine providing real-time usage data ingestion, pricing logic, and billing automation for API and SaaS products. The m3ter platform exposes two HTTP-based REST APIs returning JSON responses: an Ingest API for submitting raw usage measurements and a Config API for configuration and billing management. Authentication uses OAuth 2.0 Client Credentials with a Service User Access Key id and Api Secret exchanged for a Bearer Token at https://api.m3ter.com/oauth/token.'
finops:
- has_sources: false
  method: generated
  name: M3Ter Finops
  primary_unit: request
  service_category: API
  slug: m3ter-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/m3ter.png
layout: provider
modified: '2026-05-19'
name: M3ter
nav: Providers
network: true
overview: 'M3ter publishes 66 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, AccountPlan API, Aggregation API, and 63 more. Tagged areas include FinOps, Usage-Based Billing, Metering, Billing, and Pricing.


  The M3ter catalog on APIs.io includes 1 Spectral governance ruleset.


  M3ter''s developer surface includes authentication, documentation, API reference, engineering blog, and 12 more developer resources.'
plans:
- name: M3Ter Plans Pricing
  plan_count: 3
  slug: m3ter-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: M3Ter Rate Limits
  slug: m3ter-rate-limits
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: M3ter API Rules
  rule_count: 64
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 17
  slug: m3ter-rules
scopes:
- name: M3Ter Scopes
  scope_count: 6
  slug: m3ter-scopes
  summary_line: 6 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 46.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 52.2
    developer_ergonomics: 59.5
    discoverability: 73.2
    operational_transparency: 18.4
  previous_composite: 45.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 99.2
      derived: 0
      marker_coverage: 52.8
      total: 125
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://apis.io/screenshots/m3ter/m3ter-2026-06-20T184823.png
security:
- kind: authentication
  name: M3Ter Authentication
  slug: m3ter-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: M3Ter Domain Security
  slug: m3ter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: M3Ter Vulnerability Disclosure
  slug: m3ter-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: M3Ter Trust Center
  slug: m3ter-trust-center
  summary_line: SOC 2
slug: m3ter
tags:
- FinOps
- Usage-Based Billing
- Metering
- Billing
- Pricing
- Software-as-a-Service
website: https://www.m3ter.com/
---

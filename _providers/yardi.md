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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Yardi Agentic Access
  operation_count: 13
  slug: yardi-agentic-access
  summary_line: 13 operations · 13 acting
api_count: 12
apis:
- description: Web service interface that provides the ability to export commercial data from Yardi Voyager databases, including property, unit, lease, and rent roll information. Built on the OSCRE standard with Yar
  name: Yardi Voyager Commercial Data API
  slug: yardi-voyager-commercial-data-api
- description: API for online rental applications, payments, and resident portal functionality for multifamily properties. RENTCafe APIv2 provides transaction-based pricing with an annual price cap, enabling vendors
  name: Yardi RENTCafe API
  slug: yardi-rentcafe-api
- description: Maintenance and work order management API enabling integration with maintenance operations, service requests, and vendor management. Part of the Voyager Standard Interface Partnership Program, this AP
  name: Yardi Maintenance IQ API
  slug: yardi-maintenance-iq-api
- description: API for investment and asset management functions including deal tracking, investor reporting, and portfolio analytics. Provides programmatic access to investment management data within the Yardi Voya
  name: Yardi Investment Manager API
  slug: yardi-investment-manager-api
- description: SOAP-based API for Yardi's self-storage management platform, formerly known as CenterShift. The SWS2 API provides tokenized authentication and access to store management methods for creating custom ap
  name: Yardi Store Web Services API
  slug: yardi-store-web-services-api
- description: 'API and webhook integration for Yardi Kube, the coworking and flexible workspace management platform. Enables connecting third-party applications with Yardi Kube for member management, billing, space '
  name: Yardi Kube API
  slug: yardi-kube-api
- description: Interface API for Yardi's Electronic Health Records platform designed for senior living communities. Supports secure data exchange with pharmacy networks, laboratory systems, and other healthcare part
  name: Yardi Senior Living EHR API
  slug: yardi-senior-living-ehr-api
- description: Operations for managing resident transactions, charges, payments, credits, and billing data. Accessed via the ItfResidentTransactions20 web service interface.
  name: Yardi Billing and Payments API
  slug: yardi-billing-and-payments-api
- description: Operations for retrieving shared property management data including properties, units, tenants, and chart of accounts. Accessed via the ItfCommonData web service interface.
  name: Yardi Common Data API
  slug: yardi-common-data-api
- description: Operations for managing job cost tracking, budgets, and construction project financials. Accessed via the ItfJobCost web service interface.
  name: Yardi Job Cost API
  slug: yardi-job-cost-api
- description: Operations for creating and managing maintenance work orders and service requests. Accessed via the ItfServiceRequests web service interface.
  name: Yardi Service Requests API
  slug: yardi-service-requests-api
- description: Operations for managing vendor invoices, purchase orders, and accounts payable transactions. Accessed via the ItfVendorInvoice web service interface.
  name: Yardi Vendor Invoicing API
  slug: yardi-vendor-invoicing-api
artifact_total: 51
collections:
- collection_type: open
  name: Yardi Voyager API
  slug: open-yardi-voyager-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/yardi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yardi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/yardi-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/yardi-systems
- group: start
  title: ''
  type: Portal
  url: https://www.yardi.com/platform/
- group: other
  title: ''
  type: Developer Resources
  url: https://www.yardi.com/platform/api/
- group: operate
  title: ''
  type: Support
  url: https://www.yardi.com/support/
- group: operate
  title: ''
  type: Contact
  url: https://www.yardi.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://resources.yardi.com/legal/privacy-statement/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.yardi.com/about-us/legal/terms-of-use/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.yardi.com
- group: company
  title: ''
  type: Website
  url: https://www.yardi.com
- group: company
  title: ''
  type: Blog
  url: https://www.yardi.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.yardi.com/company/become-an-interface-partner/
- group: start
  title: ''
  type: Signup
  url: https://www.yardi.com/company/become-an-interface-partner/
- group: docs
  title: ''
  type: Documentation
  url: https://www.yardi.com/services/interfaces/standard-interface-options/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/YardiSystems
- group: learn
  title: ''
  type: Training
  url: https://www.yardi.com/company/training/
- group: start
  title: ''
  type: Login
  url: https://www.yardi.com/company/technical-support/
created: '2025-01-01'
description: Yardi develops and supports industry-leading investment and property management software for all types and sizes of real estate companies. The platform includes solutions for residential, commercial, public housing, affordable housing, and military housing management.
examples:
- key_count: 2
  name: Yardi Get Tenants Example
  slug: yardi-get-tenants-example
finops:
- name: Yardi Finops
  service_category: Property Management / PropTech
  slug: yardi-finops
graphqls:
- description: Yardi is a property management and real estate investment platform. The API covers property records, lease management, resident/tenant data, financial transactions, maintenance orders, commercial prop
  name: Yardi GraphQL API
  slug: yardi-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yardi.png
json_schemas:
- name: BudgetDataResponse
  property_count: 1
  slug: yardi-budgetdataresponse
- name: ChartOfAccountsResponse
  property_count: 1
  slug: yardi-chartofaccountsresponse
- name: GetBudgetDataRequest
  property_count: 10
  slug: yardi-getbudgetdatarequest
- name: GetChartOfAccountsRequest
  property_count: 8
  slug: yardi-getchartofaccountsrequest
- name: GetJobCostDataRequest
  property_count: 9
  slug: yardi-getjobcostdatarequest
- name: GetPropertyConfigurationsRequest
  property_count: 8
  slug: yardi-getpropertyconfigurationsrequest
- name: GetResidentTransactionsByChargeDateRequest
  property_count: 10
  slug: yardi-getresidenttransactionsbychargedaterequest
- name: GetResidentTransactionsRequest
  property_count: 10
  slug: yardi-getresidenttransactionsrequest
- name: GetServiceRequestsRequest
  property_count: 10
  slug: yardi-getservicerequestsrequest
- name: GetTenantsRequest
  property_count: 8
  slug: yardi-gettenantsrequest
- name: GetUnitInformationRequest
  property_count: 8
  slug: yardi-getunitinformationrequest
- name: GetVendorInvoicesRequest
  property_count: 10
  slug: yardi-getvendorinvoicesrequest
- name: ImportResidentTransactionsRequest
  property_count: 9
  slug: yardi-importresidenttransactionsrequest
- name: ImportResponse
  property_count: 2
  slug: yardi-importresponse
- name: ImportServiceRequestsRequest
  property_count: 9
  slug: yardi-importservicerequestsrequest
- name: ImportVendorInvoicesRequest
  property_count: 9
  slug: yardi-importvendorinvoicesrequest
- name: JobCostDataResponse
  property_count: 1
  slug: yardi-jobcostdataresponse
- name: PropertyConfigurationsResponse
  property_count: 1
  slug: yardi-propertyconfigurationsresponse
- name: ServiceRequestsResponse
  property_count: 1
  slug: yardi-servicerequestsresponse
- name: Yardi Tenant
  property_count: 14
  slug: yardi-tenant
- name: TenantsResponse
  property_count: 1
  slug: yardi-tenantsresponse
- name: Yardi Resident Transaction
  property_count: 12
  slug: yardi-transaction
- name: TransactionResponse
  property_count: 1
  slug: yardi-transactionresponse
- name: UnitInformationResponse
  property_count: 1
  slug: yardi-unitinformationresponse
- name: VendorInvoicesResponse
  property_count: 1
  slug: yardi-vendorinvoicesresponse
json_structures:
- name: Yardi Structure
  property_count: 0
  slug: yardi-structure
- name: Yardi Tenant Structure
  property_count: 0
  slug: yardi-tenant-structure
jsonld:
- class_count: 0
  name: Yardi Context
  property_count: 28
  slug: yardi-context
layout: provider
modified: '2026-05-19'
name: Yardi
nav: Providers
network: true
overview: 'Yardi publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Billing and Payments API, Common Data API, Job Cost API, and 2 more. Tagged areas include Accounting, Commercial Real Estate, Coworking, Investment Management, and Multifamily.


  The Yardi catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Yardi''s developer surface includes authentication, developer portal, support, engineering blog, getting-started guide, signup flow, documentation, and 12 more developer resources.'
plans:
- name: Yardi Plans Pricing
  plan_count: 1
  slug: yardi-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 1
  name: Yardi Rate Limits
  slug: yardi-rate-limits
rules:
- name: Yardi API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: yardi-jsonschema-spectral-rules
- name: Yardi API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 8
  slug: yardi-rules
score:
  band: strong
  composite: 62.9
  delta: 3.2
  facets:
    commercial_clarity: 63.2
    contract_quality: 67.3
    developer_ergonomics: 45.7
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 42.1
  previous_composite: 59.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yardi/refs/heads/main/screenshots/yardi-2026-06-20T201730.png
security:
- kind: authentication
  name: Yardi Authentication
  slug: yardi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Yardi Domain Security
  slug: yardi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: yardi
tags:
- Accounting
- Commercial Real Estate
- Coworking
- Investment Management
- Multifamily
- Property Management
- Real Estate
- Residential
- Self Storage
- Senior Living
website: https://www.yardi.com
---

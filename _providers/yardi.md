---
access_model:
  confidence: high
  label: Enterprise · Partner-gated (SIPP application, Data Exchange Agreement per interface, annual per-interface fee, 3+ active Voyager clients required)
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - https://www.yardi.com/company/become-an-interface-partner/
  - https://www.yardi.com/company/find-an-interface-partner/
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Yardi Agentic Access
  operation_count: 13
  slug: yardi-agentic-access
  summary_line: 13 operations · 13 acting
api_count: 1
apis:
- description: 'Yardi''s first-party Model Context Protocol server, announced in early access on 2025-09-10 and described as generally available in Virtuoso Enterprise on 2026-06-16. Listed on the Anthropic connector '
  name: Yardi Virtuoso Connector (MCP)
  slug: yardi-virtuoso-connector-mcp
- description: SOAP-based API for Yardi's self-storage management platform, formerly CenterShift. SWS2 provides tokenized authentication and store management methods for building custom applications and websites aga
  name: Yardi Store Web Services API (SWS2)
  slug: yardi-store-web-services-api
- description: API and webhook integration for Yardi Kube, the coworking and flexible workspace management platform, covering member management, billing, space booking, access control and CRM integrations. The integ
  name: Yardi Kube API
  slug: yardi-kube-api
- description: Voyager Standard Interface that exports commercial data from Yardi Voyager databases — property, unit, lease and rent roll information — built on the OSCRE standard with Yardi-specific extensions. Ann
  name: Yardi Voyager Commercial Data Interface
  slug: yardi-voyager-commercial-data-api
- description: The RentCafe marketing, leasing and resident-services API. Yardi's published RentCafe API Terms of Use names concrete operations in its Schedule A — getapartmentavailability, getfloorplans, getunitpri
  name: RentCafe API
  slug: yardi-rentcafe-api
- description: Voyager Standard Interface for Yardi's Electronic Health Records platform for senior living communities, supporting data exchange with pharmacy networks, laboratory systems and other healthcare partne
  name: Yardi Senior Living EHR Interface
  slug: yardi-senior-living-ehr-api
- baseURL_template: https://{server}.yardi.com/{clientUrl}/webservices
  baseurl_source: spec_template
  description: Operations for managing resident transactions, charges, payments, credits and billing data, accessed via the ItfResidentTransactions20 Voyager web service interface. Yardi publishes no specification f
  name: Yardi Billing and Payments Interface
  slug: yardi-billing-and-payments-api
- baseURL_template: https://{server}.yardi.com/{clientUrl}/webservices
  baseurl_source: spec_template
  description: Operations for retrieving shared property management data including properties, units, tenants and chart of accounts, accessed via the ItfCommonData Voyager web service interface. Yardi publishes no s
  name: Yardi Common Data Interface
  slug: yardi-common-data-api
- baseURL_template: https://{server}.yardi.com/{clientUrl}/webservices
  baseurl_source: spec_template
  description: Operations for job cost tracking, budgets and construction project financials, accessed via the ItfJobCost Voyager web service interface. Corresponds to the "Construction API" interface category on Ya
  name: Yardi Job Cost Interface
  slug: yardi-job-cost-api
- baseURL_template: https://{server}.yardi.com/{clientUrl}/webservices
  baseurl_source: spec_template
  description: Operations for creating and managing maintenance work orders and service requests, accessed via the ItfServiceRequests Voyager web service interface. Corresponds to the "Maintenance API" interface cat
  name: Yardi Service Requests Interface
  slug: yardi-service-requests-api
- baseURL_template: https://{server}.yardi.com/{clientUrl}/webservices
  baseurl_source: spec_template
  description: Operations for vendor invoices, purchase orders and accounts payable transactions, accessed via the ItfVendorInvoice Voyager web service interface. Corresponds to the "Payables API" interface category
  name: Yardi Vendor Invoicing Interface
  slug: yardi-vendor-invoicing-api
artifact_total: 62
collections:
- collection_type: postman
  name: Yardi Voyager Billing and Payments API
  slug: postman-yardi-billing-and-payments-api
- collection_type: postman
  name: Yardi Voyager Billing and Payments Common Data API
  slug: postman-yardi-common-data-api
- collection_type: postman
  name: Yardi Voyager Billing and Payments Job Cost API
  slug: postman-yardi-job-cost-api
- collection_type: postman
  name: Yardi Voyager Billing and Payments Service Requests API
  slug: postman-yardi-service-requests-api
- collection_type: postman
  name: Yardi Voyager Billing and Payments Vendor Invoicing API
  slug: postman-yardi-vendor-invoicing-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Yardi Voyager Billing and Payments API
  slug: open-yardi-billing-and-payments-api
- collection_type: open
  name: Yardi Voyager Billing and Payments Common Data API
  slug: open-yardi-common-data-api
- collection_type: open
  name: Yardi Voyager Billing and Payments Job Cost API
  slug: open-yardi-job-cost-api
- collection_type: open
  name: Yardi Voyager Billing and Payments Service Requests API
  slug: open-yardi-service-requests-api
- collection_type: open
  name: Yardi Voyager Billing and Payments Vendor Invoicing API
  slug: open-yardi-vendor-invoicing-api
- collection_type: open
  name: Yardi Voyager API
  slug: open-yardi-voyager-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.yardi.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.yardi.com/company/find-an-interface-partner/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.yardi.com/company/become-an-interface-partner/
- group: company
  title: ''
  type: Partners
  url: https://www.yardi.com/company/find-an-interface-partner/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.yardi.com/
- group: operate
  title: ''
  type: StatusAPI
  url: https://status.yardi.com/api
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.virtuoso.ai
- group: agent
  title: ''
  type: WellKnown
  url: https://mcp.virtuoso.ai/.well-known/oauth-protected-resource
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
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/yardi/overview
- group: auth
  title: ''
  type: Compliance
  url: https://www.yardi.com/company/cloud-security/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/yardi-systems
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/YardiSystems
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://resources.yardi.com/legal/privacy-statement/
- group: commercial
  title: ''
  type: Legal
  url: https://www.yardi.com/company/legal/
- group: operate
  title: ''
  type: Support
  url: https://www.yardi.com/company/technical-support/
- group: start
  title: ''
  type: Login
  url: https://clientcentral.yardi.com/
- group: learn
  title: ''
  type: Training
  url: https://www.yardi.com/company/training/
- group: company
  title: ''
  type: Blog
  url: https://www.yardi.com/blog/
- group: company
  title: ''
  type: News
  url: https://www.yardi.com/news/
created: '2025-01-01'
description: 'Yardi Systems, Inc. (Goleta, California) builds the investment and property management software that residential, commercial, affordable housing, public housing, military housing, self-storage, coworking and senior living operators run as their system of record — Voyager, Breeze, RentCafe, Elevate, Investment Suite, Matrix, Kube and Virtuoso. It sits on the systems-of-record rung of the real estate value chain: the ledger and operating platform a landlord or asset manager runs on, not a listing portal and not a registry operator. Its API posture, stated honestly, is licensed-access-only and partner-gated. There is no public developer portal — developer., developers., api. and docs. hosts do not resolve on yardi.com, and the /platform/ and /platform/api/ paths previously catalogued here return HTTP 404. Real interfaces exist in volume, but only behind the Voyager Standard Interface Partnership Program (SIPP): an application, a signed Data Exchange Agreement per interface type,
  a company at least two years old with three or more active Voyager clients, and an annual license fee per interface that is in some cases charged per transaction. A development sandbox is provided only after acceptance. The public "find an interface partner" page is a directory of 450+ already-accepted vendors across twelve interface categories, not documentation — its only calls to action are "Talk to sales" and "Contact us". Three public, machine-readable or anonymously readable surfaces do exist, and none of them is the Voyager API. Yardi ships a first-party MCP server, the Virtuoso Connector, whose OAuth 2.1 authorization contract is published anonymously on mcp.virtuoso.ai even though its tool list is not. status.yardi.com runs a full Atlassian Statuspage with an unauthenticated JSON API across 134 components in 16 product groups. And centershiftdevx.com, the legacy CenterShift developer site carried forward into Yardi Store, still serves genuine SWS2 endpoint documentation to anonymous
  readers — the only Yardi property that does. Every OpenAPI, JSON Schema, GraphQL schema, Postman collection and derived governance artifact in this repository was written by API Evangelist from Yardi''s own interface naming and public partner documentation. Yardi publishes no OpenAPI, no WSDL, no OData $metadata and no machine-readable contract of any kind.'
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
mcp_servers:
- description: ''
  name: Yardi MCP Server
  slug: yardi-mcp-server
modified: '2026-07-28'
name: Yardi
nav: Providers
network: true
overview: 'Yardi publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Billing and Payments Interface, Common Data Interface, Job Cost Interface, and 2 more. Tagged areas include Accounting, Commercial Real Estate, Co-Working, Investment Management, and MCP.


  The Yardi catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Yardi''s developer surface includes documentation, getting-started guide, authentication, legal docs, support, training material, engineering blog, and 15 more developer resources.'
plans:
- name: Yardi Plans Pricing
  plan_count: 1
  slug: yardi-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Yardi Rate Limits
  slug: yardi-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Yardi API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: yardi-jsonschema-spectral-rules
- effective_rule_count: 10
  extends: []
  name: Yardi API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 8
  slug: yardi-rules
score:
  band: thin
  composite: 37.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 50.3
    catalog_earned_first_party: 0.0
    catalog_gap: 64.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 48.7
    commercial_clarity: 48.7
    contract_governance: 9.8
    contract_quality: 26.7
    developer_ergonomics: 48.8
    discoverability: 70.4
    governance: 9.8
    operational_transparency: 23.7
  previous_composite: 38.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Co-Working
- Investment Management
- MCP
- Multifamily
- Property Management
- PropTech
- Real-Estate
- Residential
- Self Storage
- Senior Living
website: https://www.yardi.com
---

---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 42.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Rutter Agentic Access
  operation_count: 26
  slug: rutter-agentic-access
  summary_line: 26 operations · 9 acting
api_count: 2
apis:
- description: The Rutter Commerce API enables reading and writing data to all major commerce platforms through a unified API, supporting platforms like Shopify, WooCommerce, Amazon, and more.
  name: Rutter Commerce API
  slug: commerce-api
- description: The Rutter Accounting API provides a unified interface to read and write data to all major accounting platforms including QuickBooks, Xero, Freshbooks, and Zoho Books.
  name: Rutter Accounting API
  slug: accounting-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: 'Unified accounting/ERP API: accounts, bills, invoices, payments, journal entries, items, vendors, customers, financial statements, attachments and Bank Feeds across QuickBooks, Xero, NetSuite, Sage In'
  name: Rutter Accounting API
  slug: rutter-accounting-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: 'Unified ads API: ad accounts and campaigns across Facebook, Google and TikTok (5 operations under /ads).'
  name: Rutter Ads API
  slug: rutter-ads-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: 'Unified banking API: bank accounts, bank statements and bank transactions for connected banking platforms (8 operations under /banking).'
  name: Rutter Banking API
  slug: rutter-banking-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: 'Unified commerce API: orders, fulfilments, products, collections, customers, customer groups, inventory events, stores and commerce metrics, plus Agentic Commerce (ACP) and Universal Commerce Protocol'
  name: Rutter Commerce API
  slug: rutter-commerce-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: 'Connections and platform access: create connections and Rutter Link URLs, exchange public tokens for access tokens, read connection status, schedule backfills and incremental syncs, verify credentials'
  name: Rutter Connections API
  slug: rutter-connections-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: 'Unified HRIS API: organizations, employees, departments, locations and employee payroll runs from connected HR platforms such as Workday (10 operations under /hris).'
  name: Rutter HRIS API
  slug: rutter-hris-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: 'Supplier Enablement API for commercial-card programs: enrich merchants and suppliers, score card acceptance, and create and track card activations and activation jobs (10 operations under /supplier_en'
  name: Rutter Supplier Enablement API
  slug: rutter-supplier-enablement-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: The Acp API from Rutter — 4 operation(s) for acp.
  name: Rutter Acp API
  slug: rutter-acp-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: The Auth API from Rutter — 1 operation(s) for auth.
  name: Rutter Auth API
  slug: rutter-auth-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: The Balance API from Rutter — 1 operation(s) for balance.
  name: Rutter Balance API
  slug: rutter-balance-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: The Collections API from Rutter — 2 operation(s) for collections.
  name: Rutter Collections API
  slug: rutter-collections-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: The Configs API from Rutter — 5 operation(s) for configs.
  name: Rutter Configs API
  slug: rutter-configs-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: The Customer Groups API from Rutter — 2 operation(s) for customer groups.
  name: Rutter Customer Groups API
  slug: rutter-customer-groups-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: The Customers API from Rutter — 2 operation(s) for customers.
  name: Rutter Customers API
  slug: rutter-customers-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: The Events API from Rutter — 1 operation(s) for events.
  name: Rutter Events API
  slug: rutter-events-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: The Inventory Events API from Rutter — 2 operation(s) for inventory events.
  name: Rutter Inventory Events API
  slug: rutter-inventory-events-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: The Item API from Rutter — 1 operation(s) for item.
  name: Rutter Item API
  slug: rutter-item-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: The Jobs API from Rutter — 1 operation(s) for jobs.
  name: Rutter Jobs API
  slug: rutter-jobs-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: The Logs API from Rutter — 3 operation(s) for logs.
  name: Rutter Logs API
  slug: rutter-logs-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: The Orders API from Rutter — 3 operation(s) for orders.
  name: Rutter Orders API
  slug: rutter-orders-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: The Payouts API from Rutter — 2 operation(s) for payouts.
  name: Rutter Payouts API
  slug: rutter-payouts-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: The Products API from Rutter — 5 operation(s) for products.
  name: Rutter Products API
  slug: rutter-products-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: The Store API from Rutter — 1 operation(s) for store.
  name: Rutter Store API
  slug: rutter-store-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: The Subscriptions API from Rutter — 1 operation(s) for subscriptions.
  name: Rutter Subscriptions API
  slug: rutter-subscriptions-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: The Supplier Enablement Enrichments API from Rutter — 1 operation(s) for supplier enablement enrichments.
  name: Rutter Supplier Enablement Enrichments API
  slug: rutter-supplier-enablement-enrichments-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: The Transactions API from Rutter — 2 operation(s) for transactions.
  name: Rutter Transactions API
  slug: rutter-transactions-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: The Ucp API from Rutter — 4 operation(s) for ucp.
  name: Rutter Ucp API
  slug: rutter-ucp-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: Webhook configuration and management
  name: Rutter Webhooks API
  slug: rutter-webhooks-api
artifact_total: 115
asyncapis:
- description: ''
  name: Rutter Webhooks
  slug: rutter-webhooks
collections:
- collection_type: open
  name: Rutter Unified Accounting API
  slug: open-rutter-accounting-api
- collection_type: open
  name: Rutter Unified Accounting Ads API
  slug: open-rutter-ads-api
- collection_type: open
  name: Rutter Unified Accounting Banking API
  slug: open-rutter-banking-api
- collection_type: open
  name: Rutter Unified Accounting Commerce API
  slug: open-rutter-commerce-api
- collection_type: open
  name: Rutter Unified Accounting Connections API
  slug: open-rutter-connections-api
- collection_type: open
  name: Rutter Unified API
  slug: open-rutter-unified-api
- collection_type: open
  name: Rutter Unified Accounting Webhooks API
  slug: open-rutter-webhooks-api
common:
- group: auth
  href: https://artifacts.apis.io/rutter/well-known/rutter-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/rutter-status-security.txt
- group: agent
  href: https://artifacts.apis.io/rutter/well-known/rutter-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rutter-well-known.yml
- group: design
  href: https://artifacts.apis.io/rutter/rules/rutter-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/rutter-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/rutter/rules/rutter-rules.yml
  title: ''
  type: Spectral
  url: rules/rutter-rules.yml
- group: design
  href: https://artifacts.apis.io/rutter/rules/rutter-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/rutter-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/rutter/json-ld/rutter-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/rutter-context.jsonld
- group: design
  href: https://artifacts.apis.io/rutter/vocabulary/rutter-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/rutter-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/rutter/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/rutter/asyncapi/rutter-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/rutter-webhooks.yml
- group: design
  href: https://artifacts.apis.io/rutter/data-model/rutter-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rutter-data-model.yml
- group: design
  href: https://artifacts.apis.io/rutter/components/rutter-components.yml
  title: ''
  type: Components
  url: components/rutter-components.yml
- group: operate
  href: https://artifacts.apis.io/rutter/changelog/rutter-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/rutter-changelog.yml
- group: design
  href: https://artifacts.apis.io/rutter/conventions/rutter-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/rutter-conventions.yml
- group: design
  href: https://artifacts.apis.io/rutter/conventions/rutter-conventions.yml
  title: ''
  type: Conventions
  url: conventions/rutter-conventions.yml
- group: start
  href: https://artifacts.apis.io/rutter/sandbox/rutter-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/rutter-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.rutter.com/
- group: auth
  href: https://artifacts.apis.io/rutter/security/rutter-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/rutter-trust-center.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.rutter.com/api-upgrades
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rutterapi.com
- group: design
  href: https://artifacts.apis.io/rutter/lifecycle/rutter-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/rutter-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/rutter/errors/rutter-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rutter-problem-types.yml
- group: design
  href: https://artifacts.apis.io/rutter/conformance/rutter-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rutter-conformance.yml
- group: other
  href: https://artifacts.apis.io/rutter/overlays/rutter-accounting-api-authentication-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/rutter-accounting-api-authentication-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/rutter/llms/rutter-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rutter-llms.txt
- group: other
  href: https://artifacts.apis.io/rutter/hosts/rutter-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rutter-hosts.yml
- group: build
  href: https://artifacts.apis.io/rutter/integrations/rutter-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/rutter-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/rutter/vendors/rutter-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rutter-vendors.yml
- group: build
  href: https://artifacts.apis.io/rutter/packages/rutter-packages.yml
  title: ''
  type: Packages
  url: packages/rutter-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.rutter.com/
- group: commercial
  href: https://artifacts.apis.io/rutter/plans/rutter-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rutter-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/rutter/rate-limits/rutter-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rutter-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/rutter/finops/rutter-finops.yml
  title: ''
  type: FinOps
  url: finops/rutter-finops.yml
- group: other
  href: https://artifacts.apis.io/rutter/capabilities/rutter-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/rutter-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/rutter/agentic-access/rutter-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/rutter-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/rutter/security/rutter-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rutter-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/rutter/authentication/rutter-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rutter-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rutterapi
- group: company
  title: ''
  type: Website
  url: https://www.rutter.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rutter.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rutter.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.rutter.com/blog
- group: other
  title: ''
  type: APIs
  url: https://www.rutter.com/our-features/apis
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.rutterapi.com/sign-up
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rutter
- group: build
  title: ''
  type: SDKs
  url: https://github.com/rutter/react-rutter-link
- group: docs
  title: ''
  type: APIReference
  url: https://docs.rutter.com/rest/2024-08-31/basics
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.rutter.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.rutter.com/try-us-out
- group: operate
  title: ''
  type: Support
  url: https://help.rutter.com/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/langapi/workspace/rutter-s-public-workspace
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rutterdocs.s3.us-east-2.amazonaws.com/FW_15501597_4_Rutter+Global+Privacy+Notice.pdf
- group: start
  title: ''
  type: Login
  url: https://dashboard.rutterapi.com/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/RutterAPI
created: '2026-03-16'
description: Rutter is the leading unified RESTful API for B2B financial products that connects to over 60 commerce, payments, accounting, and ads platforms through a single API. Trusted by companies like Airwallex, Mercury, and Ramp, Rutter enables developers to read, update, write, and remove data across major business platforms with a unified data model and idempotency guarantees for financial data. The API supports OAuth2 and Basic authentication, versioning via the X-Rutter-Version header, cursor-based pagination, and asynchronous request processing.
examples:
- key_count: 2
  name: Rutter List Connections Example
  slug: rutter-list-connections-example
- key_count: 2
  name: Rutter List Invoices Example
  slug: rutter-list-invoices-example
- key_count: 2
  name: Rutter List Orders Example
  slug: rutter-list-orders-example
finops:
- has_sources: true
  method: generated
  name: Rutter Finops
  primary_unit: ''
  service_category: Unified API / Commerce + Accounting Integration
  slug: rutter-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rutter.png
json_schemas:
- name: ACPCheckoutSession
  property_count: 12
  slug: rutter-acpcheckout-session
- name: ACPCompleteCheckoutSessionResponse
  property_count: 13
  slug: rutter-acpcomplete-checkout-session-response
- name: AdsAccountResponseWithConnection
  property_count: 2
  slug: rutter-ads-account-response-with-connection
- name: AggregateAccountingMetricResponse
  property_count: 35
  slug: rutter-aggregate-accounting-metric-response
- name: BankAccountBalanceResponseWithConnection
  property_count: 2
  slug: rutter-bank-account-balance-response-with-connection
- name: BankAccountDetailsResponseWithConnection
  property_count: 2
  slug: rutter-bank-account-details-response-with-connection
- name: BankTransactionResponseWithConnection
  property_count: 2
  slug: rutter-bank-transaction-response-with-connection
- name: CampaignResponseWithConnection
  property_count: 2
  slug: rutter-campaign-response-with-connection
- name: Rutter Connection
  property_count: 5
  slug: rutter-connection
- name: CreateConnectionBackfillBody
  property_count: 7
  slug: rutter-create-connection-backfill-body
- name: CreateConnectionBody
  property_count: 5
  slug: rutter-create-connection-body
- name: CreateCreateBillCreditUnapplicationRequest
  property_count: 2
  slug: rutter-create-create-bill-credit-unapplication-request
- name: CreateCreateInvoiceCreditApplicationRequest
  property_count: 2
  slug: rutter-create-create-invoice-credit-application-request
- name: CreateCreateInvoiceCreditUnapplicationRequest
  property_count: 2
  slug: rutter-create-create-invoice-credit-unapplication-request
- name: CreateEntityWithCustomFieldsPageResponse
  property_count: 3
  slug: rutter-create-entity-with-custom-fields-page-response
- name: CreateEntityWithCustomFieldsPage
  property_count: 3
  slug: rutter-create-entity-with-custom-fields-page
- name: CreateSupplierEnablementMerchantCardActivationRequest
  property_count: 1
  slug: rutter-create-supplier-enablement-merchant-card-activation-request
- name: GetBalanceResponse
  property_count: 2
  slug: rutter-get-balance-response
- name: GetConnectionStatusResponse
  property_count: 2
  slug: rutter-get-connection-status-response
- name: GetJsonPathConfigResponse
  property_count: 1
  slug: rutter-get-json-path-config-response
- name: GetPayoutsResponse
  property_count: 2
  slug: rutter-get-payouts-response
- name: GetRequestResponse
  property_count: 1
  slug: rutter-get-request-response
- name: GetSupplierEnablementEnrichmentsResponse
  property_count: 8
  slug: rutter-get-supplier-enablement-enrichments-response
- name: GetSupplierEnablementMerchantEnrichmentResponse
  property_count: 0
  slug: rutter-get-supplier-enablement-merchant-enrichment-response
- name: GetTransactionsResponse
  property_count: 2
  slug: rutter-get-transactions-response
- name: GetWebhookLogResponse
  property_count: 1
  slug: rutter-get-webhook-log-response
- name: HrisEmployeePayrollRunResponseWithConnection
  property_count: 2
  slug: rutter-hris-employee-payroll-run-response-with-connection
- name: Rutter Invoice
  property_count: 7
  slug: rutter-invoice
- name: ListAdsAccountResponseWithConnection
  property_count: 3
  slug: rutter-list-ads-account-response-with-connection
- name: ListBankAccountResponseWithConnection
  property_count: 3
  slug: rutter-list-bank-account-response-with-connection
- name: ListBankStatementResponseWithConnection
  property_count: 3
  slug: rutter-list-bank-statement-response-with-connection
- name: ListBankTransactionResponseWithConnection
  property_count: 3
  slug: rutter-list-bank-transaction-response-with-connection
- name: ListCampaignDailyResponseWithConnection
  property_count: 3
  slug: rutter-list-campaign-daily-response-with-connection
- name: ListCampaignResponseWithConnection
  property_count: 3
  slug: rutter-list-campaign-response-with-connection
- name: ListHrisDepartmentResponseWithConnection
  property_count: 3
  slug: rutter-list-hris-department-response-with-connection
- name: ListHrisEmployeePayrollRunResponseWithConnection
  property_count: 3
  slug: rutter-list-hris-employee-payroll-run-response-with-connection
- name: ListHrisEmployeeResponseWithConnection
  property_count: 3
  slug: rutter-list-hris-employee-response-with-connection
- name: ListHrisLocationResponseWithConnection
  property_count: 3
  slug: rutter-list-hris-location-response-with-connection
- name: ListHrisOrganizationResponseWithConnection
  property_count: 3
  slug: rutter-list-hris-organization-response-with-connection
- name: ListPayoutsResponse
  property_count: 3
  slug: rutter-list-payouts-response
- name: ListSubscriptionsResponse
  property_count: 3
  slug: rutter-list-subscriptions-response
- name: ListSupplierEnablementCardActivationResponse
  property_count: 1
  slug: rutter-list-supplier-enablement-card-activation-response
- name: ListSupplierEnablementEnrichmentsResponse
  property_count: 0
  slug: rutter-list-supplier-enablement-enrichments-response
- name: ListTransactionsResponse
  property_count: 3
  slug: rutter-list-transactions-response
- name: ListWebhookLogsResponse
  property_count: 5
  slug: rutter-list-webhook-logs-response
- name: Rutter Order
  property_count: 8
  slug: rutter-order
- name: PatchConnectionSyncConfigRequest
  property_count: 2
  slug: rutter-patch-connection-sync-config-request
- name: PatchPlatformSyncConfigRequest
  property_count: 2
  slug: rutter-patch-platform-sync-config-request
- name: PostPlatformSyncConfigRequest
  property_count: 2
  slug: rutter-post-platform-sync-config-request
- name: SupplierEnablementCardActivationResponse
  property_count: 1
  slug: rutter-supplier-enablement-card-activation-response
- name: UCPCancelCheckoutSessionResponse
  property_count: 10
  slug: rutter-ucpcancel-checkout-session-response
- name: UCPCompleteCheckoutSessionResponse
  property_count: 10
  slug: rutter-ucpcomplete-checkout-session-response
- name: UCPCreateCheckoutSessionResponse
  property_count: 10
  slug: rutter-ucpcreate-checkout-session-response
- name: UpdateJsonPathConfigResponse
  property_count: 1
  slug: rutter-update-json-path-config-response
- name: VariantResponse
  property_count: 1
  slug: rutter-variant-response
- name: WebhookConfigResponse
  property_count: 8
  slug: rutter-webhook-config-response
json_structures:
- name: Rutter Connection Structure
  property_count: 0
  slug: rutter-connection-structure
- name: Rutter Invoice Structure
  property_count: 0
  slug: rutter-invoice-structure
- name: Rutter Order Structure
  property_count: 0
  slug: rutter-order-structure
jsonld:
- class_count: 1
  name: Rutter Context
  property_count: 24
  slug: rutter-context
layout: provider
modified: '2026-11-05'
name: Rutter
nav: Providers
network: true
overview: 'Rutter publishes 30 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounting API, Ads API, Banking API, and 27 more. Tagged areas include Accounting, B2B, Commerce, Financial Data, and Payments.


  The Rutter catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Rutter''s developer surface includes changelog, sandbox, authentication, documentation, pricing, engineering blog, signup flow, and 46 more developer resources.'
plans:
- name: Rutter Plans Pricing
  plan_count: 2
  slug: rutter-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Rutter Rate Limits
  slug: rutter-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Rutter — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: rutter-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Rutter API Rules
  rule_count: 44
  severity_counts:
    error: 31
    hint: 0
    info: 2
    warn: 11
  slug: rutter-rules
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Rutter API Rules
  rule_count: 15
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 10
  slug: rutter-spectral-rules
score:
  band: strong
  composite: 64.8
  coverage:
    artifact_dirs: 40
    catalog_earned: 70.8
    catalog_earned_first_party: 16.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 29.2
  facets:
    access_clarity: 71.1
    contract_governance: 35.6
    contract_quality: 61.7
    developer_ergonomics: 68.5
    discoverability: 64.3
    operational_transparency: 84.2
  previous_composite: 35.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 28
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 23.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/rutter/rutter-2026-06-20T193303.png
security:
- kind: authentication
  name: Rutter Authentication
  slug: rutter-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Rutter Domain Security
  slug: rutter-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Rutter Trust Center
  slug: rutter-trust-center
  summary_line: SOC 2 Type II, ISO 27001:2022, GDPR
skill_count: 4
skills:
- name: rutter-connect-a-business
  slug: rutter-connect-a-business
- name: rutter-create-accounting-invoice
  slug: rutter-create-accounting-invoice
- name: rutter-read-commerce-orders
  slug: rutter-read-commerce-orders
- name: rutter-sync-bank-feed-transactions
  slug: rutter-sync-bank-feed-transactions
slug: rutter
tags:
- Accounting
- B2B
- Commerce
- Financial Data
- Payments
- Unified API
- HRIS
website: https://www.rutter.com/
---

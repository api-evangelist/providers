---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 60.7
  scored_at: '2026-08-24'
api_count: 90
apis:
- description: Account configurations
  name: Xentral Account API
  slug: xentral-account-api
- description: Accounting Export endpoints
  name: Xentral Accounting Export API
  slug: xentral-accounting-export-api
- description: AuthPlatform represents the oauth login for Xentral
  name: Xentral AuthPlatform API
  slug: xentral-authplatform-api
- description: Create and manage collections for your reports.
  name: Xentral Collection API
  slug: xentral-collection-api
- description: Create collective bills
  name: Xentral Collective Bill API
  slug: xentral-collective-bill-api
- description: Get information about your current current and monthly credits regarding Report usage.
  name: Xentral Credit API
  slug: xentral-credit-api
- description: A credit note is a document you send to your customer to correct a mistake on an order or an invoice, or to refund an amount paid for products or services.
  name: Xentral Credit Note API
  slug: xentral-credit-note-api
- description: Credit Note resource tags management.
  name: Xentral Credit Note Tag API
  slug: xentral-credit-note-tag-api
- description: CreditNote
  name: Xentral CreditNote API
  slug: xentral-creditnote-api
- description: Represents the address associated with a specific customer, including details such as location, contact information, and address type.
  name: Xentral Customer Address API
  slug: xentral-customer-address-api
- description: Customer represents an information related to company, or individual person.
  name: Xentral Customer API
  slug: xentral-customer-api
- description: Contact person information related to a specific customer
  name: Xentral Customer - Contact Person API
  slug: xentral-customer-contact-person-api
- description: Customer Delivery Address
  name: Xentral Customer Delivery Address API
  slug: xentral-customer-delivery-address-api
- description: Delivery information.
  name: Xentral Delivery API
  slug: xentral-delivery-api
- description: Delivery notes.
  name: Xentral Delivery Note API
  slug: xentral-delivery-note-api
- description: Delivery notes tags.
  name: Xentral Delivery Note Tag API
  slug: xentral-delivery-note-tag-api
- description: Delivery Terms
  name: Xentral Delivery Terms API
  slug: xentral-delivery-terms-api
- description: DeliveryNote
  name: Xentral DeliveryNote API
  slug: xentral-deliverynote-api
- description: Get documentation about our data catalog, tables and columns.
  name: Xentral Documentation API
  slug: xentral-documentation-api
- description: EmailAccount
  name: Xentral EmailAccount API
  slug: xentral-emailaccount-api
- description: Employees
  name: Xentral Employee API
  slug: xentral-employee-api
- description: External shop references that are linked to a product.
  name: Xentral External Reference API
  slug: xentral-external-reference-api
- description: All external shops that exists within Xentral
  name: Xentral External Reference Target API
  slug: xentral-external-reference-target-api
- description: Get a business document file and its metadata.
  name: Xentral File API
  slug: xentral-file-api
- description: General Ledger transactions
  name: Xentral General Ledger API
  slug: xentral-general-ledger-api
- description: Goods Receipt for physical incoming goods.
  name: Xentral Goods Receipt API
  slug: xentral-goods-receipt-api
- description: An invoice is a commercial document issued by a seller to a buyer relating to a sale transaction and indicating the products, quantities, and agreed-upon prices for products or services the seller had
  name: Xentral Invoice API
  slug: xentral-invoice-api
- description: Invoice resource tags management.
  name: Xentral Invoice Tag API
  slug: xentral-invoice-tag-api
- description: Returns a collection with all liabilities.
  name: Xentral Liability API
  slug: xentral-liability-api
- description: Manage options for products.
  name: Xentral Matrixproduct API
  slug: xentral-matrixproduct-api
- description: Offer
  name: Xentral Offer API
  slug: xentral-offer-api
- description: Payment Methods resource
  name: Xentral Payment Methods API
  slug: xentral-payment-methods-api
- description: Payment Service Provider endpoints
  name: Xentral Payment Service Provider API
  slug: xentral-payment-service-provider-api
- description: PaymentTermsGroups can be used to group customers with identical payment terms such as different discounts, payment targets, and free postage options.
  name: Xentral Payment Terms Group API
  slug: xentral-payment-terms-group-api
- description: Payment Transaction resource
  name: Xentral Payment Transaction API
  slug: xentral-payment-transaction-api
- description: Point Of Sale (POS) endpoints.
  name: Xentral Point Of Sale API
  slug: xentral-point-of-sale-api
- description: PriceInquiry
  name: Xentral PriceInquiry API
  slug: xentral-priceinquiry-api
- description: Print Jobs represent the jobs that are sent to the printer.
  name: Xentral Print Jobs API
  slug: xentral-print-jobs-api
- description: Product represents the services or things given company sells in the business.
  name: Xentral Product API
  slug: xentral-product-api
- description: Product Category represents the Product Category Tree that can be used to categorise products.
  name: Xentral Product Category API
  slug: xentral-product-category-api
- description: 40 product free fields can be used and individually labeled.
  name: Xentral Product Free Field API
  slug: xentral-product-free-field-api
- description: Product labels management.
  name: Xentral Product Label API
  slug: xentral-product-label-api
- description: Images of a product
  name: Xentral Product Media API
  slug: xentral-product-media-api
- description: Product merchandise groups.
  name: Xentral Product Merchandise Group API
  slug: xentral-product-merchandise-group-api
- description: Product properties describe its physical traits.
  name: Xentral Product Property API
  slug: xentral-product-property-api
- description: Product resource tags management.
  name: Xentral Product Tag API
  slug: xentral-product-tag-api
- description: ProductCalculation
  name: Xentral ProductCalculation API
  slug: xentral-productcalculation-api
- description: ProductDeliveryThreshold
  name: Xentral ProductDeliveryThreshold API
  slug: xentral-productdeliverythreshold-api
- description: Production resource management
  name: Xentral Production API
  slug: xentral-production-api
- description: ProformaInvoice
  name: Xentral ProformaInvoice API
  slug: xentral-proformainvoice-api
- description: Project resource.
  name: Xentral Project API
  slug: xentral-project-api
- description: Provisional Return resource.
  name: Xentral Provisional Return API
  slug: xentral-provisional-return-api
- description: Purchase Orders made at a supplier.
  name: Xentral Purchase Order API
  slug: xentral-purchase-order-api
- description: PurchasePrices determine the prices used for the purchasing of products.
  name: Xentral Purchase Price API
  slug: xentral-purchase-price-api
- description: PurchaseOrder
  name: Xentral PurchaseOrder API
  slug: xentral-purchaseorder-api
- description: Create, manage and export reports and report results based on SQL queries against your data.
  name: Xentral Query API
  slug: xentral-query-api
- description: Create, manage and export reports and report results based on SQL queries against your data.
  name: Xentral Report API
  slug: xentral-report-api
- description: Provide information about your usage in terms of credits spent.
  name: Xentral Report Usage API
  slug: xentral-report-usage-api
- description: Settings for analytics reporting platform
  name: Xentral Reporting Settings API
  slug: xentral-reporting-settings-api
- description: Return represents incoming shipments from customer to supplier
  name: Xentral Return API
  slug: xentral-return-api
- description: Return reason describes why an item is being returned
  name: Xentral Return Reason API
  slug: xentral-return-reason-api
- description: ReturnOrder
  name: Xentral ReturnOrder API
  slug: xentral-returnorder-api
- description: Revenue Account Mapping configurations
  name: Xentral Revenue Account Mapping API
  slug: xentral-revenue-account-mapping-api
- description: SalesChannel are the configured Shops/Marketplaces.
  name: Xentral Sales Channel API
  slug: xentral-sales-channel-api
- description: Sales Channel Settings inside a product.
  name: Xentral Sales Channels Product Settings API
  slug: xentral-sales-channels-product-settings-api
- description: SalesOrders are an outbound orders, meaning that someone has bought from you.
  name: Xentral Sales Order API
  slug: xentral-sales-order-api
- description: SalesPrices determine the prices used in sales to customers.
  name: Xentral Sales Price API
  slug: xentral-sales-price-api
- description: SalesOrder
  name: Xentral SalesOrder API
  slug: xentral-salesorder-api
- description: SalesPrice
  name: Xentral SalesPrice API
  slug: xentral-salesprice-api
- description: ServiceOrder
  name: Xentral ServiceOrder API
  slug: xentral-serviceorder-api
- description: Settings represents the application's configurations.
  name: Xentral Setting API
  slug: xentral-setting-api
- description: Shipments
  name: Xentral Shipments API
  slug: xentral-shipments-api
- description: Shipping methods
  name: Xentral Shipping Methods API
  slug: xentral-shipping-methods-api
- description: Stock movement type
  name: Xentral Stock Movement Types API
  slug: xentral-stock-movement-types-api
- description: Represent a storage item in a storage location
  name: Xentral Storage Item API
  slug: xentral-storage-item-api
- description: Represents the spaces within a warehouse
  name: Xentral Storage Location API
  slug: xentral-storage-location-api
- description: Suppliers represents an information related to providers of goods the company is managing.
  name: Xentral Supplier API
  slug: xentral-supplier-api
- description: Supplier Delivery Address
  name: Xentral Supplier Delivery Address API
  slug: xentral-supplier-delivery-address-api
- description: Supplier resource tags management.
  name: Xentral Supplier Tag API
  slug: xentral-supplier-tag-api
- description: SupplierInvoice
  name: Xentral SupplierInvoice API
  slug: xentral-supplierinvoice-api
- description: Resource tags.
  name: Xentral Tag API
  slug: xentral-tag-api
- description: Tax Account Mapping configurations
  name: Xentral Tax Account Mapping API
  slug: xentral-tax-account-mapping-api
- description: Tax resource
  name: Xentral Tax API
  slug: xentral-tax-api
- description: Tax Obligation resource
  name: Xentral Tax Obligation API
  slug: xentral-tax-obligation-api
- description: Represents a tax rate for a product on given day and for given country
  name: Xentral Tax Rate API
  slug: xentral-tax-rate-api
- description: Tax Type configurations
  name: Xentral Tax Type API
  slug: xentral-tax-type-api
- description: Tax Type Mapping configurations
  name: Xentral Tax Type Mapping API
  slug: xentral-tax-type-mapping-api
- description: User represents a Xentral account used to access other parts of the system.
  name: Xentral User API
  slug: xentral-user-api
- description: Represents a location with storage space
  name: Xentral Warehouse API
  slug: xentral-warehouse-api
- description: Manage webhooks.
  name: Xentral Webhook API
  slug: xentral-webhook-api
artifact_total: 186
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Xentral Account API
  slug: open-xentral-account-api
- collection_type: open
  name: Xentral Account Accounting Export API
  slug: open-xentral-accounting-export-api
- collection_type: open
  name: Xentral Account AuthPlatform API
  slug: open-xentral-authplatform-api
- collection_type: open
  name: Xentral Account Collection API
  slug: open-xentral-collection-api
- collection_type: open
  name: Xentral Account Collective Bill API
  slug: open-xentral-collective-bill-api
- collection_type: open
  name: Xentral Account Credit API
  slug: open-xentral-credit-api
- collection_type: open
  name: Xentral Account Credit Note API
  slug: open-xentral-credit-note-api
- collection_type: open
  name: Xentral Account Credit Note Tag API
  slug: open-xentral-credit-note-tag-api
- collection_type: open
  name: Xentral Account CreditNote API
  slug: open-xentral-creditnote-api
- collection_type: open
  name: Xentral Account Customer Address API
  slug: open-xentral-customer-address-api
- collection_type: open
  name: Xentral Account Customer API
  slug: open-xentral-customer-api
- collection_type: open
  name: Xentral Account Customer - Contact Person API
  slug: open-xentral-customer-contact-person-api
- collection_type: open
  name: Xentral Account Customer Delivery Address API
  slug: open-xentral-customer-delivery-address-api
- collection_type: open
  name: Xentral Account Delivery API
  slug: open-xentral-delivery-api
- collection_type: open
  name: Xentral Account Delivery Note API
  slug: open-xentral-delivery-note-api
- collection_type: open
  name: Xentral Account Delivery Note Tag API
  slug: open-xentral-delivery-note-tag-api
- collection_type: open
  name: Xentral Account Delivery Terms API
  slug: open-xentral-delivery-terms-api
- collection_type: open
  name: Xentral Account DeliveryNote API
  slug: open-xentral-deliverynote-api
- collection_type: open
  name: Xentral Account Documentation API
  slug: open-xentral-documentation-api
- collection_type: open
  name: Xentral Account EmailAccount API
  slug: open-xentral-emailaccount-api
- collection_type: open
  name: Xentral Account Employee API
  slug: open-xentral-employee-api
- collection_type: open
  name: Xentral Account External Reference API
  slug: open-xentral-external-reference-api
- collection_type: open
  name: Xentral Account External Reference Target API
  slug: open-xentral-external-reference-target-api
- collection_type: open
  name: Xentral Account File API
  slug: open-xentral-file-api
- collection_type: open
  name: Xentral Account General Ledger API
  slug: open-xentral-general-ledger-api
- collection_type: open
  name: Xentral Account Goods Receipt API
  slug: open-xentral-goods-receipt-api
- collection_type: open
  name: Xentral Account Invoice API
  slug: open-xentral-invoice-api
- collection_type: open
  name: Xentral Account Invoice Tag API
  slug: open-xentral-invoice-tag-api
- collection_type: open
  name: Xentral Account Liability API
  slug: open-xentral-liability-api
- collection_type: open
  name: Xentral Account Matrixproduct API
  slug: open-xentral-matrixproduct-api
- collection_type: open
  name: Xentral Account Offer API
  slug: open-xentral-offer-api
- collection_type: open
  name: Xentral Account Payment Methods API
  slug: open-xentral-payment-methods-api
- collection_type: open
  name: Xentral Account Payment Service Provider API
  slug: open-xentral-payment-service-provider-api
- collection_type: open
  name: Xentral Account Payment Terms Group API
  slug: open-xentral-payment-terms-group-api
- collection_type: open
  name: Xentral Account Payment Transaction API
  slug: open-xentral-payment-transaction-api
- collection_type: open
  name: Xentral Account Point Of Sale API
  slug: open-xentral-point-of-sale-api
- collection_type: open
  name: Xentral Account PriceInquiry API
  slug: open-xentral-priceinquiry-api
- collection_type: open
  name: Xentral Account Print Jobs API
  slug: open-xentral-print-jobs-api
- collection_type: open
  name: Xentral Account Product API
  slug: open-xentral-product-api
- collection_type: open
  name: Xentral Account Product Category API
  slug: open-xentral-product-category-api
- collection_type: open
  name: Xentral Account Product Free Field API
  slug: open-xentral-product-free-field-api
- collection_type: open
  name: Xentral Account Product Label API
  slug: open-xentral-product-label-api
- collection_type: open
  name: Xentral Account Product Media API
  slug: open-xentral-product-media-api
- collection_type: open
  name: Xentral Account Product Merchandise Group API
  slug: open-xentral-product-merchandise-group-api
- collection_type: open
  name: Xentral Account Product Property API
  slug: open-xentral-product-property-api
- collection_type: open
  name: Xentral Account Product Tag API
  slug: open-xentral-product-tag-api
- collection_type: open
  name: Xentral Account ProductCalculation API
  slug: open-xentral-productcalculation-api
- collection_type: open
  name: Xentral Account ProductDeliveryThreshold API
  slug: open-xentral-productdeliverythreshold-api
- collection_type: open
  name: Xentral Account Production API
  slug: open-xentral-production-api
- collection_type: open
  name: Xentral Account ProformaInvoice API
  slug: open-xentral-proformainvoice-api
- collection_type: open
  name: Xentral Account Project API
  slug: open-xentral-project-api
- collection_type: open
  name: Xentral Account Provisional Return API
  slug: open-xentral-provisional-return-api
- collection_type: open
  name: Xentral Account Purchase Order API
  slug: open-xentral-purchase-order-api
- collection_type: open
  name: Xentral Account Purchase Price API
  slug: open-xentral-purchase-price-api
- collection_type: open
  name: Xentral Account PurchaseOrder API
  slug: open-xentral-purchaseorder-api
- collection_type: open
  name: Xentral Account Query API
  slug: open-xentral-query-api
- collection_type: open
  name: Xentral Account Report API
  slug: open-xentral-report-api
- collection_type: open
  name: Xentral Account Report Usage API
  slug: open-xentral-report-usage-api
- collection_type: open
  name: Xentral Account Reporting Settings API
  slug: open-xentral-reporting-settings-api
- collection_type: open
  name: Xentral Account Return API
  slug: open-xentral-return-api
- collection_type: open
  name: Xentral Account Return Reason API
  slug: open-xentral-return-reason-api
- collection_type: open
  name: Xentral Account ReturnOrder API
  slug: open-xentral-returnorder-api
- collection_type: open
  name: Xentral Account Revenue Account Mapping API
  slug: open-xentral-revenue-account-mapping-api
- collection_type: open
  name: Xentral Account Sales Channel API
  slug: open-xentral-sales-channel-api
- collection_type: open
  name: Xentral Account Sales Channels Product Settings API
  slug: open-xentral-sales-channels-product-settings-api
- collection_type: open
  name: Xentral Account Sales Order API
  slug: open-xentral-sales-order-api
- collection_type: open
  name: Xentral Account Sales Price API
  slug: open-xentral-sales-price-api
- collection_type: open
  name: Xentral Account SalesOrder API
  slug: open-xentral-salesorder-api
- collection_type: open
  name: Xentral Account SalesPrice API
  slug: open-xentral-salesprice-api
- collection_type: open
  name: Xentral Account ServiceOrder API
  slug: open-xentral-serviceorder-api
- collection_type: open
  name: Xentral Account Setting API
  slug: open-xentral-setting-api
- collection_type: open
  name: Xentral Account Shipments API
  slug: open-xentral-shipments-api
- collection_type: open
  name: Xentral Account Shipping Methods API
  slug: open-xentral-shipping-methods-api
- collection_type: open
  name: Xentral Account Stock Movement Types API
  slug: open-xentral-stock-movement-types-api
- collection_type: open
  name: Xentral Account Storage Item API
  slug: open-xentral-storage-item-api
- collection_type: open
  name: Xentral Account Storage Location API
  slug: open-xentral-storage-location-api
- collection_type: open
  name: Xentral Account Supplier API
  slug: open-xentral-supplier-api
- collection_type: open
  name: Xentral Account Supplier Delivery Address API
  slug: open-xentral-supplier-delivery-address-api
- collection_type: open
  name: Xentral Account Supplier Tag API
  slug: open-xentral-supplier-tag-api
- collection_type: open
  name: Xentral Account SupplierInvoice API
  slug: open-xentral-supplierinvoice-api
- collection_type: open
  name: Xentral Account Tag API
  slug: open-xentral-tag-api
- collection_type: open
  name: Xentral Account Tax Account Mapping API
  slug: open-xentral-tax-account-mapping-api
- collection_type: open
  name: Xentral Account Tax API
  slug: open-xentral-tax-api
- collection_type: open
  name: Xentral Account Tax Obligation API
  slug: open-xentral-tax-obligation-api
- collection_type: open
  name: Xentral Account Tax Rate API
  slug: open-xentral-tax-rate-api
- collection_type: open
  name: Xentral Account Tax Type API
  slug: open-xentral-tax-type-api
- collection_type: open
  name: Xentral Account Tax Type Mapping API
  slug: open-xentral-tax-type-mapping-api
- collection_type: open
  name: Xentral Account User API
  slug: open-xentral-user-api
- collection_type: open
  name: Xentral Account Warehouse API
  slug: open-xentral-warehouse-api
- collection_type: open
  name: Xentral Account Webhook API
  slug: open-xentral-webhook-api
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/xentral-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.xentral.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.xentral.com/reference/intro
- group: docs
  title: ''
  type: APIReference
  url: https://developer.xentral.com/reference/intro
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.xentral.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.xentral.com
- group: company
  title: ''
  type: Blog
  url: https://xentral.com/de/artikel
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/xentral
- group: commercial
  title: ''
  type: Pricing
  url: https://xentral.com/de/preise
- group: start
  title: ''
  type: SignUp
  url: https://xentral.com/de/jetzt-starten
- group: commercial
  title: ''
  type: TermsOfService
  url: https://xentral.com/de/agb
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://xentral.com/de/datenschutz
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/xentral-rate-limits.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/xentral-events-asyncapi.json
- group: design
  title: ''
  type: Webhooks
  url: https://developer.xentral.com/reference/webhooks
- group: agent
  title: ''
  type: MCPServer
  url: mcp/xentral-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/xentral-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/xentral-packages.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/xentral-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/xentral-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/xentral-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/xentral-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/xentral-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/xentral-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.xentral.com/reference/versioning
- group: design
  title: ''
  type: DataModel
  url: data-model/xentral-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xentral-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/xentral-well-known.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/xentral-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/xentral-documents-api-overlay.yaml
created: '2026-07-17'
description: Xentral is a cloud ERP and business operations platform from Augsburg, Germany that helps small and mid-sized product businesses run sales orders, purchasing, warehousing, fulfillment, invoicing, accounting, POS, and production from one system. It exposes a versioned REST API (v1/v2/v3) with Personal Access Token authentication, a Kafka-backed event system with webhooks, an official OpenAPI specification on GitHub, a hosted MCP server behind its AgentOS, and a published Claude Code plugin with agent skills for automating the ERP.
image: https://eu-central-1-enterprise-euc1.graphassets.com/AwA5KcKRdQcurP6TExnrjz/cmp1bwlva178v07uueip5kbla
layout: provider
mcp_servers:
- description: ''
  name: Xentral MCP Server
  slug: xentral-mcp-server
modified: '2026-07-21'
name: Xentral
nav: Providers
network: true
overview: 'Xentral publishes 90 APIs on the [APIs.io](https://apis.io/) network, including Account API, Accounting Export API, AuthPlatform API, and 87 more. Tagged areas include Company, ERP, E-Commerce, Fulfillment, and Warehousing.


  Xentral''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 24 more developer resources.'
random_paper: 10
rate_limits:
- limit_count: 1
  name: Xentral Rate Limits
  slug: xentral-rate-limits
scopes:
- name: Xentral Scopes
  scope_count: 100
  slug: xentral-scopes
  summary_line: 100 scopes
score:
  band: developing
  composite: 48.3
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 16.7
    contract_quality: 64.3
    developer_ergonomics: 52.4
    discoverability: 66.7
    governance: 16.7
    operational_transparency: 31.6
  previous_composite: 48.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 90
    mcp: first-party
    skills: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/xentral/refs/heads/main/screenshots/xentral-2026-08-17T083012.png
security:
- kind: authentication
  name: Xentral Authentication
  slug: xentral-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Xentral Domain Security
  slug: xentral-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: xentral
tags:
- Company
- ERP
- E-Commerce
- Fulfillment
- Warehousing
- Invoicing
- Accounting
- Order
- Product
- Germany
website: https://developer.xentral.com
---

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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Coupa Agentic Access
  operation_count: 27
  slug: coupa-agentic-access
  summary_line: 27 operations · 19 acting
api_count: 16
apis:
- description: API designed for enterprise integrations with ERP systems and other third-party applications.
  name: Coupa Integration API
  slug: coupa-integration-api
- description: API for supplier-specific operations including supplier information management, catalogs, and supplier collaboration.
  name: Coupa Supplier API
  slug: coupa-supplier-api
- description: API for accessing Coupa's analytics and reporting data for business intelligence and custom reporting needs.
  name: Coupa Analytics API
  slug: coupa-analytics-api
- description: The Coupa Contingent Workforce (CCW) REST API enables customers and partners to build applications and integrate with CCW for managing contingent workforce operations including candidate lookup, worke
  name: Coupa CCW API
  slug: coupa-ccw-api
- description: The Coupa Sourcing Optimization (CSO) API is a RESTful web service for importing and exporting fact sheet data, enabling integration between CSO and third-party systems for sourcing optimization workf
  name: Coupa CSO API
  slug: coupa-cso-api
- description: REST API for retrieving and updating Coupa Treasury Management data such as cash flows and account balances. Treasury APIs follow the Coupa Core API structure but support JSON only.
  name: Coupa Treasury API
  slug: coupa-treasury-api
- description: The Open Buy API provides a faster, standard, and secure interface for searching and purchasing items in real-time. It follows common eCommerce API patterns and supports authentication, search, detail
  name: Coupa Open Buy API
  slug: coupa-open-buy-api
- description: API for managing Coupa Pay invoice payments and expense payments, including retrieval, export tracking, and payment status management. Accessed through the Coupa Pay payments endpoint.
  name: Coupa Payments API
  slug: coupa-payments-api
- description: The Coupa Procurement API provides RESTful endpoints for managing the full procure-to-order lifecycle including requisitions, purchase orders, contracts, and sourcing (quote requests). It enables prog
  name: Coupa Procurement API
  slug: coupa-procurement-api
- description: The Coupa Invoicing API provides RESTful endpoints for creating, updating, and querying invoices associated with purchase orders. It supports the full invoice lifecycle including invoice lines, charge
  name: Coupa Invoicing API
  slug: coupa-invoicing-api
- description: The Coupa Expenses API provides RESTful endpoints for managing expense reports, expense lines, expense categories, and related data. It supports creation, querying, and updating of expense transaction
  name: Coupa Expenses API
  slug: coupa-expenses-api
- description: The Coupa Inventory and Receipts API provides RESTful endpoints for managing receiving transactions, inventory adjustments, inventory consumptions, pick lists, fulfillment reservations, warehouse oper
  name: Coupa Inventory and Receipts API
  slug: coupa-inventory-and-receipts-api
- description: Create, retrieve, update, and manage invoices. Invoices represent billing documents from suppliers for goods or services delivered.
  name: Coupa Invoices API
  slug: coupa-invoices-api
- description: Create, retrieve, update, and manage purchase orders. Purchase orders represent commitments to buy goods or services from suppliers.
  name: Coupa Purchase Orders API
  slug: coupa-purchase-orders-api
- description: Create, retrieve, update, and manage requisitions. Requisitions are internal requests to purchase goods or services that go through approval workflows before becoming purchase orders.
  name: Coupa Requisitions API
  slug: coupa-requisitions-api
- description: Create, retrieve, update, and manage supplier records. Suppliers represent vendor organizations that provide goods or services.
  name: Coupa Suppliers API
  slug: coupa-suppliers-api
artifact_total: 55
collections:
- collection_type: open
  name: Coupa Core API
  slug: open-coupa-core-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coupa-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/coupa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coupa-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/coupa-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/coupa-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coupa
- group: start
  title: ''
  type: DeveloperPortal
  url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation
- group: auth
  title: ''
  type: Authentication
  url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-api/authentication
- group: docs
  title: ''
  type: OAuth2TransitionGuide
  url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/oauth-2.0-and-oidc/oauth-2.0-transition-guide
- group: other
  title: ''
  type: OpenIDConnect
  url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/oauth-2.0-and-oidc/openid-connect-clients
- group: start
  title: ''
  type: GettingStarted
  url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api
- group: operate
  title: ''
  type: RateLimits
  url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/api-rate-limits
- group: design
  title: ''
  type: ErrorCodes
  url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api/exception-handling-and-error-codes
- group: other
  title: ''
  type: APIResources
  url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources
- group: other
  title: ''
  type: TransactionalResources
  url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources
- group: docs
  title: ''
  type: ReferenceDataResources
  url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources
- group: other
  title: ''
  type: IPAddresses
  url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-application-ip-addresses
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://compass.coupa.com/en-us/products/release-notes
- group: build
  title: ''
  type: IntegrationKnowledgeBase
  url: https://compass.coupa.com/en-us/products/total-spend-management-platform/integration-playbooks-and-resources/integration-knowledge-articles
- group: operate
  title: ''
  type: StatusPage
  url: https://trust.coupa.com/
- group: auth
  title: ''
  type: Trust
  url: https://compass.coupa.com/en-us/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coupa.com/company/trust/agreements
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coupa.com/company/trust/privacy
- group: operate
  title: ''
  type: Support
  url: https://compass.coupa.com/en-us/support
- group: operate
  title: ''
  type: Community
  url: https://compass.coupa.com/en-us/community
- group: company
  title: ''
  type: Blog
  url: https://www.coupa.com/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coupa-software
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Coupa
- group: auth
  title: ''
  type: OAuth2AndOIDC
  url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/oauth-2.0-and-oidc
- group: start
  title: ''
  type: OAuth2GettingStarted
  url: https://compass.coupa.com/en-us/products/total-spend-management-platform/integration-playbooks-and-resources/integration-knowledge-articles/oauth-2.0-getting-started-with-coupa-api
- group: other
  title: ''
  type: SharedResources
  url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources
- group: other
  title: ''
  type: APIReturnFormats
  url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api/api-return-formats
- group: other
  title: ''
  type: XMLvsJSON
  url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api/differences-between-xml-and-json-in-coupa
- group: build
  title: ''
  type: SampleRequestsResponses
  url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api/sample-requestsresponses-xml-vs-json
- group: other
  title: ''
  type: SpecialActions
  url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api/special-actions-and-api-notes
- group: other
  title: ''
  type: FlatFileCSV
  url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)
- group: other
  title: ''
  type: FlatFileImport
  url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import
- group: other
  title: ''
  type: FlatFileExport
  url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export
- group: build
  title: ''
  type: IntegrationPlaybooks
  url: https://compass.coupa.com/en-us/products/total-spend-management-platform/integration-playbooks-and-resources/other-integration-playbooks
- group: build
  title: ''
  type: RESTAPIIntegration
  url: https://compass.coupa.com/en-us/products/total-spend-management-platform/integration-playbooks-and-resources/other-integration-playbooks/erp-integration-adapters/build-your-integration/integration-methods/coupa-rest-api-integration
created: '2024-01-01'
description: Coupa is a leading Business Spend Management (BSM) platform that provides cloud-based solutions for procurement, invoicing, expenses, payments, sourcing, contracts, and supply chain design & planning.
finops:
- name: Coupa Finops
  service_category: Business Spend Management
  slug: coupa-finops
graphqls:
- description: Coupa is a business spend management platform covering procurement, invoicing, expense management, pay, and supply chain design. The API covers purchase orders, invoices, suppliers, expense reports, c
  name: Coupa GraphQL API
  slug: coupa-graphql
image: https://www.coupa.com/wp-content/themes/coupa/images/coupa-logo.svg
json_schemas:
- name: AddressReference
  property_count: 8
  slug: coupa-addressreference
- name: ApprovalReference
  property_count: 2
  slug: coupa-approvalreference
- name: CurrencyReference
  property_count: 2
  slug: coupa-currencyreference
- name: DepartmentReference
  property_count: 2
  slug: coupa-departmentreference
- name: Error
  property_count: 1
  slug: coupa-error
- name: Coupa Invoice
  property_count: 85
  slug: coupa-invoice
- name: InvoiceCreate
  property_count: 22
  slug: coupa-invoicecreate
- name: InvoiceLine
  property_count: 16
  slug: coupa-invoiceline
- name: InvoiceUpdate
  property_count: 11
  slug: coupa-invoiceupdate
- name: OrderLine
  property_count: 17
  slug: coupa-orderline
- name: PaymentTermReference
  property_count: 2
  slug: coupa-paymenttermreference
- name: Coupa Purchase Order
  property_count: 42
  slug: coupa-purchase-order
- name: PurchaseOrder
  property_count: 39
  slug: coupa-purchaseorder
- name: PurchaseOrderCreate
  property_count: 14
  slug: coupa-purchaseordercreate
- name: PurchaseOrderUpdate
  property_count: 12
  slug: coupa-purchaseorderupdate
- name: Requisition
  property_count: 34
  slug: coupa-requisition
- name: RequisitionCreate
  property_count: 14
  slug: coupa-requisitioncreate
- name: RequisitionLine
  property_count: 17
  slug: coupa-requisitionline
- name: RequisitionUpdate
  property_count: 12
  slug: coupa-requisitionupdate
- name: ShippingTermReference
  property_count: 2
  slug: coupa-shippingtermreference
- name: Supplier
  property_count: 56
  slug: coupa-supplier
- name: SupplierCreate
  property_count: 23
  slug: coupa-suppliercreate
- name: SupplierReference
  property_count: 3
  slug: coupa-supplierreference
- name: SupplierUpdate
  property_count: 24
  slug: coupa-supplierupdate
- name: UserReference
  property_count: 3
  slug: coupa-userreference
json_structures:
- name: Coupa Structure
  property_count: 0
  slug: coupa-structure
jsonld:
- class_count: 0
  name: Coupa Context
  property_count: 13
  slug: coupa-context
layout: provider
modified: '2026-05-19'
name: Coupa
nav: Providers
network: true
overview: 'Coupa publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Invoices API, Purchase Orders API, Requisitions API, and 1 more. Tagged areas include BSM, Business Spend Management, Cloud Platform, Enterprise, and Financial Management.


  The Coupa catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Coupa''s developer surface includes authentication, getting-started guide, release notes, support, engineering blog, and 35 more developer resources.'
plans:
- name: Coupa Plans Pricing
  plan_count: 1
  slug: coupa-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 1
  name: Coupa Rate Limits
  slug: coupa-rate-limits
rules:
- name: Coupa API Rules
  rule_count: 13
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 6
  slug: coupa-core-api-rules
- name: Coupa API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: coupa-jsonschema-spectral-rules
scopes:
- name: Coupa Scopes
  scope_count: 8
  slug: coupa-scopes
  summary_line: 8 scopes · clientCredentials
score:
  band: developing
  composite: 50.5
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 76.5
    developer_ergonomics: 37.0
    discoverability: 68.5
    governance: 27.1
    operational_transparency: 42.1
  previous_composite: 50.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coupa/refs/heads/main/screenshots/coupa-2026-06-20T175107.png
security:
- kind: authentication
  name: Coupa Authentication
  slug: coupa-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Coupa Domain Security
  slug: coupa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Coupa Vulnerability Disclosure
  slug: coupa-vulnerability-disclosure
  summary_line: disclosure policy published
slug: coupa
tags:
- BSM
- Business Spend Management
- Cloud Platform
- Enterprise
- Financial Management
- Invoicing
- Procurement
- Supply Chain
website: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation
---

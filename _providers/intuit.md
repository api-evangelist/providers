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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Intuit Agentic Access
  operation_count: 17
  slug: intuit-agentic-access
  summary_line: 17 operations · 11 acting
api_count: 1
apis:
- description: Intuit APIs provide developers with access to a wide range of services and functionalities to help them build innovative solutions for financial management, accounting, and tax-related needs. These AP
  name: Intuit APIs
  slug: intuit
- description: The QuickBooks Payments API enables developers to process credit card charges, bank account debits (ACH), and manage payment methods within the QuickBooks ecosystem. It supports tokenized card storage
  name: QuickBooks Payments API
  slug: quickbooks-payments
- description: The QuickBooks Payroll and Time API provides programmatic access to payroll and time-tracking data within QuickBooks Online. It supports use cases including time entry management, payroll compensation
  name: QuickBooks Payroll and Time API
  slug: quickbooks-payroll-time
- description: 'The QuickBooks Desktop API allows developers to integrate with QuickBooks Desktop applications using qbXML messages. It provides capabilities for adding, querying, modifying, and deleting data across '
  name: QuickBooks Desktop API
  slug: quickbooks-desktop
- description: The QuickBooks Projects API is a premium API that provides programmatic access to project data within QuickBooks Online Plus, Advanced, Accountant, and Intuit Enterprise Suite. It enables developers t
  name: QuickBooks Projects API
  slug: quickbooks-projects
- description: The QuickBooks Custom Fields API is a premium API that provides programmatic access to custom field definitions and values in QuickBooks Online and Intuit Enterprise Suite. It allows developers to cre
  name: QuickBooks Custom Fields API
  slug: quickbooks-custom-fields
- description: The QuickBooks Sales Tax API is a premium API that provides programmatic access to the automated sales tax calculation capabilities within QuickBooks Online. It enables developers to leverage QuickBoo
  name: QuickBooks Sales Tax API
  slug: quickbooks-sales-tax
- description: A Customer object represents a consumer of the service or product that the business offers. The Customer entity allows you to categorize customers into jobs and sub-customers.
  name: Intuit Customers API
  slug: intuit-customers-api
- description: An Invoice represents a sales form where the customer pays for a product or service later. QuickBooks records an accounts receivable transaction for each invoice.
  name: Intuit Invoices API
  slug: intuit-invoices-api
- description: An Item represents a product or service that a company buys, sells, or re-sells, such as products, shipping charges, discount, and sales tax (if applicable). Items are used in line items on invoices a
  name: Intuit Items API
  slug: intuit-items-api
- description: A Payment object records a payment received from a customer against one or more invoices or credit memos. Payments can be applied to specific invoices or left as unapplied credits.
  name: Intuit Payments API
  slug: intuit-payments-api
arazzos:
- description: Create an item, create a customer, then invoice them for that item.
  name: Intuit Catalog and Bill Customer
  slug: intuit-catalog-and-bill-customer-workflow
- description: Create an invoice and email it to the customer in one flow.
  name: Intuit Create and Send Invoice
  slug: intuit-create-and-send-invoice-workflow
- description: Create an invoice and void it, carrying the SyncToken forward.
  name: Intuit Create and Void Invoice
  slug: intuit-create-and-void-invoice-workflow
- description: Create a new QuickBooks customer and immediately raise their first invoice.
  name: Intuit Create Customer and Invoice
  slug: intuit-create-customer-and-invoice-workflow
- description: Create a sellable service item and invoice a customer using that item.
  name: Intuit Create Item and Invoice
  slug: intuit-create-item-and-invoice-workflow
- description: Onboard a customer, invoice them, and record their payment end to end.
  name: Intuit Customer Invoice Payment Cycle
  slug: intuit-customer-invoice-payment-workflow
- description: Look up a customer by display name and create it only if missing.
  name: Intuit Find or Create Customer
  slug: intuit-find-or-create-customer-workflow
- description: Raise an invoice and record a customer payment applied against it.
  name: Intuit Invoice and Collect Payment
  slug: intuit-invoice-and-collect-payment-workflow
- description: Create an invoice and retrieve it as a downloadable PDF.
  name: Intuit Invoice to PDF
  slug: intuit-invoice-to-pdf-workflow
- description: Find a customer's oldest open invoice and record a payment against it.
  name: Intuit Pay Customer Open Invoice
  slug: intuit-pay-customer-open-invoice-workflow
- description: Find an invoice by document number and void it with its SyncToken.
  name: Intuit Query and Void Invoice
  slug: intuit-query-and-void-invoice-workflow
- description: Query for unpaid invoices and email a reminder for the first match.
  name: Intuit Remind Overdue Invoice
  slug: intuit-remind-overdue-invoice-workflow
- description: Read an item and apply a new unit price via a sparse update.
  name: Intuit Reprice Item
  slug: intuit-reprice-item-workflow
- description: Find a customer by email, read it, and update its contact details.
  name: Intuit Update Customer by Query
  slug: intuit-update-customer-by-query-workflow
- description: Read a payment for its SyncToken and update its amount and reference.
  name: Intuit Update Payment Amount
  slug: intuit-update-payment-amount-workflow
- description: Read a payment for its SyncToken and then void it.
  name: Intuit Void Payment Safely
  slug: intuit-void-payment-safely-workflow
artifact_total: 130
asyncapis:
- description: QuickBooks Online Webhooks provide near real-time notifications when data changes in a QuickBooks Online company. When an entity is created, updated, merged, deleted, or voided, Intuit sends an HTTP P
  name: QuickBooks Online Webhooks
  slug: quickbooks-webhooks
collections:
- collection_type: postman
  name: QuickBooks Online Accounting API
  slug: postman-quickbooks-accounting
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: QuickBooks Online Accounting Customers API
  slug: open-intuit-customers-api
- collection_type: open
  name: QuickBooks Online Accounting Customers Invoices API
  slug: open-intuit-invoices-api
- collection_type: open
  name: QuickBooks Online Accounting Customers Items API
  slug: open-intuit-items-api
- collection_type: open
  name: QuickBooks Online Accounting Customers Payments API
  slug: open-intuit-payments-api
- collection_type: open
  name: QuickBooks Online Accounting API
  slug: open-quickbooks-accounting
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/intuit-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/intuit-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/intuit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/intuit-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/intuit-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/intuit/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/intuit-catalog-and-bill-customer-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/intuit-create-and-send-invoice-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/intuit-create-and-void-invoice-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/intuit-create-customer-and-invoice-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/intuit-create-item-and-invoice-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/intuit-customer-invoice-payment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/intuit-find-or-create-customer-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/intuit-invoice-and-collect-payment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/intuit-invoice-to-pdf-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/intuit-pay-customer-open-invoice-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/intuit-query-and-void-invoice-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/intuit-remind-overdue-invoice-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/intuit-reprice-item-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/intuit-update-customer-by-query-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/intuit-update-payment-amount-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/intuit-void-payment-safely-workflow.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.intuit.com
- group: start
  title: ''
  type: Signup
  url: https://developer.intuit.com/app/developer/appcard/overview
- group: company
  title: ''
  type: Blog
  url: https://developer.intuit.com/app/developer/blog
- group: operate
  title: ''
  type: Support
  url: https://help.developer.intuit.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.developer.intuit.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.intuit.com/app/developer/qbo/docs/learn/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.intuit.com/privacy/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.intuit.com/app/developer/qbo/docs/develop/authentication-and-authorization/oauth-2.0
- group: start
  title: ''
  type: Sandbox
  url: https://developer.intuit.com/app/developer/qbo/docs/develop/sandboxes/postman
- group: start
  title: ''
  type: Console
  url: https://developer.intuit.com/app/developer/qbo/docs/get-started/get-started-with-the-api-explorer
- group: operate
  title: ''
  type: FAQ
  url: https://developer.intuit.com/app/developer/qbo/docs/get-started/partner-faq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/intuit
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/intuitdeveloper
- group: build
  title: PHP SDK
  type: SDKs
  url: https://github.com/intuit/QuickBooks-V3-PHP-SDK
- group: build
  title: .NET SDK
  type: SDKs
  url: https://github.com/intuit/QuickBooks-V3-DotNET-SDK
- group: build
  title: Java SDK
  type: SDKs
  url: https://github.com/intuit/QuickBooks-V3-Java-SDK
- group: build
  title: Ruby SDK
  type: SDKs
  url: https://github.com/intuit/oauth-rubyclient
- group: build
  title: Node.js SDK
  type: SDKs
  url: https://developer.intuit.com/app/developer/qbo/docs/develop/sdks-and-samples-collections/nodejs
- group: build
  title: Python SDK
  type: SDKs
  url: https://developer.intuit.com/app/developer/qbo/docs/develop/sdks-and-samples-collections/python
- group: operate
  title: ''
  type: ChangeLog
  url: https://blogs.intuit.com/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developer.intuit.com/app/developer/qbo/docs/release-notes/platform-release-notes
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developer.intuit.com/app/developer/qbo/docs/release-notes/general-release-notes
- group: design
  title: ''
  type: Versioning
  url: https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api/minor-versions
- group: operate
  title: ''
  type: RateLimits
  url: https://help.developer.intuit.com/s/article/API-call-limits-and-throttling
- group: auth
  title: ''
  type: Security
  url: https://developer.intuit.com/app/developer/qbo/docs/go-live/publish-app/security-requirements
- group: other
  title: ''
  type: Marketplace
  url: https://quickbooks.intuit.com/app/apps/home/en-global/
- group: other
  title: ''
  type: X
  url: https://x.com/IntuitDev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/intuit-developer
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/intuit/quickbooks-online-mcp-server
created: '2025-03-01'
description: Collection of APIs offered by Intuit for financial and business management services.
examples:
- key_count: 4
  name: Quickbooks Accounting Custom Field Example
  slug: quickbooks-accounting-custom-field-example
- key_count: 23
  name: Quickbooks Accounting Customer Example
  slug: quickbooks-accounting-customer-example
- key_count: 1
  name: Quickbooks Accounting Customer Response Example
  slug: quickbooks-accounting-customer-response-example
- key_count: 1
  name: Quickbooks Accounting Email Address Example
  slug: quickbooks-accounting-email-address-example
- key_count: 2
  name: Quickbooks Accounting Error Example
  slug: quickbooks-accounting-error-example
- key_count: 25
  name: Quickbooks Accounting Invoice Example
  slug: quickbooks-accounting-invoice-example
- key_count: 6
  name: Quickbooks Accounting Invoice Line Example
  slug: quickbooks-accounting-invoice-line-example
- key_count: 1
  name: Quickbooks Accounting Invoice Response Example
  slug: quickbooks-accounting-invoice-response-example
- key_count: 22
  name: Quickbooks Accounting Item Example
  slug: quickbooks-accounting-item-example
- key_count: 1
  name: Quickbooks Accounting Item Response Example
  slug: quickbooks-accounting-item-response-example
- key_count: 2
  name: Quickbooks Accounting Linked Txn Example
  slug: quickbooks-accounting-linked-txn-example
- key_count: 2
  name: Quickbooks Accounting Meta Data Example
  slug: quickbooks-accounting-meta-data-example
- key_count: 13
  name: Quickbooks Accounting Payment Example
  slug: quickbooks-accounting-payment-example
- key_count: 2
  name: Quickbooks Accounting Payment Line Example
  slug: quickbooks-accounting-payment-line-example
- key_count: 1
  name: Quickbooks Accounting Payment Response Example
  slug: quickbooks-accounting-payment-response-example
- key_count: 12
  name: Quickbooks Accounting Physical Address Example
  slug: quickbooks-accounting-physical-address-example
- key_count: 2
  name: Quickbooks Accounting Query Response Example
  slug: quickbooks-accounting-query-response-example
- key_count: 2
  name: Quickbooks Accounting Reference Type Example
  slug: quickbooks-accounting-reference-type-example
- key_count: 6
  name: Quickbooks Accounting Sales Item Line Detail Example
  slug: quickbooks-accounting-sales-item-line-detail-example
- key_count: 1
  name: Quickbooks Accounting Telephone Number Example
  slug: quickbooks-accounting-telephone-number-example
- key_count: 2
  name: Quickbooks Accounting Txn Tax Detail Example
  slug: quickbooks-accounting-txn-tax-detail-example
features:
- description: Secure API access using OAuth 2.0 authorization with OpenID Connect for user identity verification.
  name: OAuth 2.0 Authentication
- description: Real-time event notifications for changes to QuickBooks entities including invoices, payments, and customers.
  name: Webhooks
- description: Backward-compatible API versioning allowing access to newer fields and behaviors without breaking existing integrations.
  name: Minor Versioning
- description: Full-featured sandbox environment for testing and development with sample company data.
  name: Sandbox Environment
- description: Support for transactions in multiple currencies with automatic exchange rate management.
  name: Multi-Currency Support
- description: Extensible metadata system allowing up to 12 custom fields across transaction types.
  name: Custom Fields
finops:
- name: Intuit Finops
  service_category: Accounting and Financial Software
  slug: intuit-finops
graphqls:
- description: Intuit does not offer a native public GraphQL API. Its developer platform exposes REST APIs for QuickBooks Online (Accounting, Payments, Payroll/Time, Projects, Custom Fields, Sales Tax), QuickBooks D
  name: Intuit GraphQL Schema
  slug: intuit-graphql
image: https://developer.intuit.com/app/developer/common/imgs/IntuitDev_Logo.svg
integrations:
- description: Sync e-commerce orders, inventory, and payments between Shopify stores and QuickBooks for automated bookkeeping.
  name: Shopify
- description: Reconcile Stripe payment transactions with QuickBooks invoices and accounts receivable.
  name: Stripe
- description: Import Square POS transactions into QuickBooks for unified financial management.
  name: Square
- description: Connect CRM data with accounting to automate invoice creation from deals and track payment status.
  name: HubSpot
- description: Sync customer and opportunity data between Salesforce CRM and QuickBooks accounting.
  name: Salesforce
json_schemas:
- name: QuickBooks Online Customer
  property_count: 41
  slug: intuit-customer
- name: QuickBooks Online Invoice
  property_count: 36
  slug: intuit-invoice
- name: CustomField
  property_count: 4
  slug: quickbooks-accounting-custom-field
- name: CustomerResponse
  property_count: 1
  slug: quickbooks-accounting-customer-response
- name: Customer
  property_count: 23
  slug: quickbooks-accounting-customer
- name: EmailAddress
  property_count: 1
  slug: quickbooks-accounting-email-address
- name: Error
  property_count: 2
  slug: quickbooks-accounting-error
- name: InvoiceLine
  property_count: 6
  slug: quickbooks-accounting-invoice-line
- name: InvoiceResponse
  property_count: 1
  slug: quickbooks-accounting-invoice-response
- name: Invoice
  property_count: 25
  slug: quickbooks-accounting-invoice
- name: ItemResponse
  property_count: 1
  slug: quickbooks-accounting-item-response
- name: Item
  property_count: 22
  slug: quickbooks-accounting-item
- name: LinkedTxn
  property_count: 2
  slug: quickbooks-accounting-linked-txn
- name: MetaData
  property_count: 2
  slug: quickbooks-accounting-meta-data
- name: PaymentLine
  property_count: 2
  slug: quickbooks-accounting-payment-line
- name: PaymentResponse
  property_count: 1
  slug: quickbooks-accounting-payment-response
- name: Payment
  property_count: 13
  slug: quickbooks-accounting-payment
- name: PhysicalAddress
  property_count: 12
  slug: quickbooks-accounting-physical-address
- name: QueryResponse
  property_count: 2
  slug: quickbooks-accounting-query-response
- name: ReferenceType
  property_count: 2
  slug: quickbooks-accounting-reference-type
- name: SalesItemLineDetail
  property_count: 6
  slug: quickbooks-accounting-sales-item-line-detail
- name: TelephoneNumber
  property_count: 1
  slug: quickbooks-accounting-telephone-number
- name: TxnTaxDetail
  property_count: 2
  slug: quickbooks-accounting-txn-tax-detail
json_structures:
- name: Quickbooks Accounting Custom Field Structure
  property_count: 4
  slug: quickbooks-accounting-custom-field-structure
- name: Quickbooks Accounting Customer Response Structure
  property_count: 1
  slug: quickbooks-accounting-customer-response-structure
- name: Quickbooks Accounting Customer Structure
  property_count: 23
  slug: quickbooks-accounting-customer-structure
- name: Quickbooks Accounting Email Address Structure
  property_count: 1
  slug: quickbooks-accounting-email-address-structure
- name: Quickbooks Accounting Error Structure
  property_count: 2
  slug: quickbooks-accounting-error-structure
- name: Quickbooks Accounting Invoice Line Structure
  property_count: 6
  slug: quickbooks-accounting-invoice-line-structure
- name: Quickbooks Accounting Invoice Response Structure
  property_count: 1
  slug: quickbooks-accounting-invoice-response-structure
- name: Quickbooks Accounting Invoice Structure
  property_count: 25
  slug: quickbooks-accounting-invoice-structure
- name: Quickbooks Accounting Item Response Structure
  property_count: 1
  slug: quickbooks-accounting-item-response-structure
- name: Quickbooks Accounting Item Structure
  property_count: 22
  slug: quickbooks-accounting-item-structure
- name: Quickbooks Accounting Linked Txn Structure
  property_count: 2
  slug: quickbooks-accounting-linked-txn-structure
- name: Quickbooks Accounting Meta Data Structure
  property_count: 2
  slug: quickbooks-accounting-meta-data-structure
- name: Quickbooks Accounting Payment Line Structure
  property_count: 2
  slug: quickbooks-accounting-payment-line-structure
- name: Quickbooks Accounting Payment Response Structure
  property_count: 1
  slug: quickbooks-accounting-payment-response-structure
- name: Quickbooks Accounting Payment Structure
  property_count: 13
  slug: quickbooks-accounting-payment-structure
- name: Quickbooks Accounting Physical Address Structure
  property_count: 12
  slug: quickbooks-accounting-physical-address-structure
- name: Quickbooks Accounting Query Response Structure
  property_count: 2
  slug: quickbooks-accounting-query-response-structure
- name: Quickbooks Accounting Reference Type Structure
  property_count: 2
  slug: quickbooks-accounting-reference-type-structure
- name: Quickbooks Accounting Sales Item Line Detail Structure
  property_count: 6
  slug: quickbooks-accounting-sales-item-line-detail-structure
- name: Quickbooks Accounting Telephone Number Structure
  property_count: 1
  slug: quickbooks-accounting-telephone-number-structure
- name: Quickbooks Accounting Txn Tax Detail Structure
  property_count: 2
  slug: quickbooks-accounting-txn-tax-detail-structure
jsonld:
- class_count: 0
  name: Intuit Context
  property_count: 8
  slug: intuit-context
- class_count: 0
  name: Quickbooks Accounting Context
  property_count: 0
  slug: quickbooks-accounting-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Intuit
nav: Providers
network: true
overview: 'Intuit publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Customers API, Invoices API, Items API, and 1 more. Tagged areas include Accounting, Custom Fields, Financial, Financial-Services, and Invoicing.


  The Intuit catalog on APIs.io includes 1 event-driven AsyncAPI specification, 2 JSON-LD contexts, and 3 Spectral governance rulesets.


  Intuit''s developer surface includes authentication, signup flow, engineering blog, support, sandbox, developer console, FAQ, and 44 more developer resources.'
plans:
- name: Intuit Plans Pricing
  plan_count: 3
  slug: intuit-plans-pricing
press:
- date: '2026-05-25'
  title: Intuit Assist - A new generative AI-powered financial assistant
  url: https://www.intuit.com/intuitassist/
- date: '2026-05-25'
  title: Intuit Unveils Revolutionary System of Intelligence to Help ...
  url: https://investors.intuit.com/news-events/press-releases/detail/1277/intuit-unveils-revolutionary-system-of-intelligence-to-help-businesses-grow-in-the-ai-era
- date: '2026-05-25'
  title: Intuit Responsible AI Principles
  url: https://www.intuit.com/privacy/responsible-ai/
- date: '2026-05-25'
  title: Intuit Launches AI-Powered Intuit Assist for QuickBooks ...
  url: https://investors.intuit.com/news-events/press-releases/detail/1222/intuit-launches-ai-powered-intuit-assist-for-quickbooks-giving-millions-of-businesses-a-competitive-edge
- date: '2026-05-25'
  title: Intuit and OpenAI Join Forces to Revolutionize Financial ...
  url: https://investors.intuit.com/news-events/press-releases/detail/1284/intuit-and-openai-join-forces-to-revolutionize-financial-intelligence-powering-every-person-business-and-dream-with-personalized-experiences
random_paper: 18
rate_limits:
- limit_count: 5
  name: Intuit Rate Limits
  slug: intuit-rate-limits
rules:
- effective_rule_count: 30
  extends:
  - spectral:asyncapi
  name: Intuit API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 1
  slug: intuit-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Intuit API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: intuit-jsonschema-spectral-rules
- effective_rule_count: 60
  extends:
  - spectral:oas
  name: Intuit API Rules
  rule_count: 19
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 11
  slug: intuit-spectral-rules
scopes:
- name: Intuit Scopes
  scope_count: 1
  slug: intuit-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 64.3
  coverage:
    artifact_dirs: 25
    catalog_gap: 59.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 13.6
    contract_quality: 80.1
    developer_ergonomics: 85.7
    discoverability: 50.0
    governance: 13.6
    operational_transparency: 55.3
  previous_composite: 64.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/intuit/refs/heads/main/screenshots/intuit-2026-06-20T183515.png
security:
- kind: authentication
  name: Intuit Authentication
  slug: intuit-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Intuit Domain Security
  slug: intuit-domain-security
  summary_line: TLSv1.2 · DMARC
slug: intuit
tags:
- Accounting
- Custom Fields
- Financial
- Financial-Services
- Invoicing
- Payments
- Payroll
- Project Management
- Sales Tax
- Small Business
- Tax
- Tax Preparation
- Taxes
- Time Tracking
- Fortune 1000
use_cases:
- description: Automate bookkeeping workflows by syncing invoices, payments, and expenses between business systems and QuickBooks.
  name: Accounting Automation
- description: Process credit card and ACH payments linked to QuickBooks invoices for seamless financial reconciliation.
  name: Payment Processing
- description: Integrate payroll and time-tracking data to streamline employee compensation and workforce management.
  name: Payroll Integration
- description: Automate sales tax calculations and ensure tax compliance across different jurisdictions.
  name: Tax Compliance
- description: Build custom financial reports and dashboards by querying QuickBooks accounting data programmatically.
  name: Financial Reporting
website: https://developer.intuit.com
---

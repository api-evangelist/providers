---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 56.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 224
  human_in_the_loop: 8
  name: Avalara Agentic Access
  operation_count: 505
  slug: avalara-agentic-access
  summary_line: 505 operations · 224 acting · 8 human-in-the-loop
api_count: 71
apis:
- description: Automate compliance with Avalara MCP servers for AI-driven tax workflows and APIs. Have your agent call our agent.
  name: Avalara
  slug: avalara
- description: The AvaTax SOAP API exposes the most commonly used features for interacting with the AvaTax service, allowing calculation of tax, modification of documents, and validation of addresses.
  name: AvaTax SOAP API
  slug: avatax-soap-api
- description: The Avalara Tax Content for Retail Configuration API automates tax content delivery for brick-and-mortar businesses, enabling management of configurations, communications, jobs, onboarding, and user r
  name: Avalara Tax Content for Retail Configuration API
  slug: tax-content-for-retail-api
- description: The Avalara Cross Border Tariff Content API classifies products based on provided product information for the specified country of destination, supporting interactive classification dialogues, trade d
  name: Self-Serve Tariff Classification API
  slug: self-serve-tariff-classification-api
- description: The Avalara License Guidance Order API enables placing Avalara License Guidance orders and populating questionnaire responses with known business information, returning order confirmation details incl
  name: License Guidance Order API
  slug: license-guidance-order-api
- description: Create and manage 1099 information returns
  name: Avalara 1099 Forms API
  slug: avalara-1099-forms-api
- description: Manage AvaTax accounts and license keys
  name: Avalara Accounts API
  slug: avalara-accounts-api
- description: Validate and resolve addresses for tax jurisdiction determination
  name: Avalara Addresses API
  slug: avalara-addresses-api
- description: The AdvancedRules API from Avalara — 2 operation(s) for advancedrules.
  name: Avalara AdvancedRules API
  slug: avalara-advancedrules-api
- description: Manage certificate attributes and custom fields
  name: Avalara Attributes API
  slug: avalara-attributes-api
- description: Token management and authentication
  name: Avalara Authentication API
  slug: avalara-authentication-api
- description: The AvaFileForms API from Avalara — 2 operation(s) for avafileforms.
  name: Avalara AvaFileForms API
  slug: avalara-avafileforms-api
- description: Submit and manage batch transaction processing
  name: Avalara Batches API
  slug: avalara-batches-api
- description: Manage business entity records
  name: Avalara Business Entities API
  slug: avalara-business-entities-api
- description: The CertExpressInvites API from Avalara — 3 operation(s) for certexpressinvites.
  name: Avalara CertExpressInvites API
  slug: avalara-certexpressinvites-api
- description: Manage exemption certificates and CertExpress invitations
  name: Avalara Certificates API
  slug: avalara-certificates-api
- description: Classify products into HS Codes and tax codes
  name: Avalara Classification API
  slug: avalara-classification-api
- description: Submit and manage product classification requests
  name: Avalara Classification Requests API
  slug: avalara-classification-requests-api
- description: Manage payer company records
  name: Avalara Companies API
  slug: avalara-companies-api
- description: Manage company contacts
  name: Avalara Contacts API
  slug: avalara-contacts-api
- description: Manage customer records and their certificate associations
  name: Avalara Customers API
  slug: avalara-customers-api
- description: Manage tax profiles, exemptions, and overrides
  name: Avalara Customization API
  slug: avalara-customization-api
- description: The DataSources API from Avalara — 3 operation(s) for datasources.
  name: Avalara DataSources API
  slug: avalara-datasources-api
- description: Query tax content definitions, rates, and jurisdictions
  name: Avalara Definitions API
  slug: avalara-definitions-api
- description: The DistanceThresholds API from Avalara — 3 operation(s) for distancethresholds.
  name: Avalara DistanceThresholds API
  slug: avalara-distancethresholds-api
- description: Submit and manage e-invoice documents
  name: Avalara Documents API
  slug: avalara-documents-api
- description: eCommerce token generation for certificate collection
  name: Avalara eCommerce API
  slug: avalara-ecommerce-api
- description: The ECommerceToken API from Avalara — 1 operation(s) for ecommercetoken.
  name: Avalara ECommerceToken API
  slug: avalara-ecommercetoken-api
- description: Issue and manage electronic fiscal documents
  name: Avalara Electronic Invoices API
  slug: avalara-electronic-invoices-api
- description: E-file forms with the IRS
  name: Avalara Filing API
  slug: avalara-filing-api
- description: Manage VAT filing obligations and calendars
  name: Avalara Filing Calendar API
  slug: avalara-filing-calendar-api
- description: The FirmClientLinkages API from Avalara — 7 operation(s) for firmclientlinkages.
  name: Avalara FirmClientLinkages API
  slug: avalara-firmclientlinkages-api
- description: Free tax rate lookup endpoints
  name: Avalara Free API
  slug: avalara-free-api
- description: The FundingRequests API from Avalara — 2 operation(s) for fundingrequests.
  name: Avalara FundingRequests API
  slug: avalara-fundingrequests-api
- description: Determine tax jurisdictions from addresses
  name: Avalara Geocoding API
  slug: avalara-geocoding-api
- description: Retrieve HS Code classification results
  name: Avalara HS Codes API
  slug: avalara-hs-codes-api
- description: Interoperability and network exchange
  name: Avalara Interop API
  slug: avalara-interop-api
- description: Manage product items and their tax classification
  name: Avalara Items API
  slug: avalara-items-api
- description: The JurisdictionOverrides API from Avalara — 3 operation(s) for jurisdictionoverrides.
  name: Avalara JurisdictionOverrides API
  slug: avalara-jurisdictionoverrides-api
- description: Manage excise licenses
  name: Avalara Licenses API
  slug: avalara-licenses-api
- description: Manage company locations and jurisdictions
  name: Avalara Locations API
  slug: avalara-locations-api
- description: Look up service and transaction type information
  name: Avalara Lookup API
  slug: avalara-lookup-api
- description: Query e-invoicing mandate definitions
  name: Avalara Mandates API
  slug: avalara-mandates-api
- description: Multi-document transaction management
  name: Avalara MultiDocument API
  slug: avalara-multidocument-api
- description: Manage tax nexus declarations for companies
  name: Avalara Nexus API
  slug: avalara-nexus-api
- description: The Notices API from Avalara — 4 operation(s) for notices.
  name: Avalara Notices API
  slug: avalara-notices-api
- description: The Notifications API from Avalara — 3 operation(s) for notifications.
  name: Avalara Notifications API
  slug: avalara-notifications-api
- description: View filing obligations and tax responsibilities
  name: Avalara Obligations API
  slug: avalara-obligations-api
- description: Onboard companies for VAT reporting
  name: Avalara Onboarding API
  slug: avalara-onboarding-api
- description: Create and manage sales orders for Avalara services
  name: Avalara Orders API
  slug: avalara-orders-api
- description: Manage product registrations
  name: Avalara Products API
  slug: avalara-products-api
- description: Manage rental property registrations
  name: Avalara Properties API
  slug: avalara-properties-api
- description: The Provisioning API from Avalara — 2 operation(s) for provisioning.
  name: Avalara Provisioning API
  slug: avalara-provisioning-api
- description: The Registrar API from Avalara — 8 operation(s) for registrar.
  name: Avalara Registrar API
  slug: avalara-registrar-api
- description: Manage partner registrations
  name: Avalara Registrations API
  slug: avalara-registrations-api
- description: Generate and retrieve tax reports
  name: Avalara Reports API
  slug: avalara-reports-api
- description: Manage and file VAT returns
  name: Avalara Returns API
  slug: avalara-returns-api
- description: Manage company settings
  name: Avalara Settings API
  slug: avalara-settings-api
- description: Query account subscriptions
  name: Avalara Subscriptions API
  slug: avalara-subscriptions-api
- description: Calculate Brazilian taxes on transactions
  name: Avalara Tax Calculation API
  slug: avalara-tax-calculation-api
- description: Calculate excise taxes on transactions
  name: Avalara Tax Determination API
  slug: avalara-tax-determination-api
- description: Look up lodging tax rates by location
  name: Avalara Tax Rates API
  slug: avalara-tax-rates-api
- description: The TaxCodes API from Avalara — 3 operation(s) for taxcodes.
  name: Avalara TaxCodes API
  slug: avalara-taxcodes-api
- description: The TaxContent API from Avalara — 5 operation(s) for taxcontent.
  name: Avalara TaxContent API
  slug: avalara-taxcontent-api
- description: Manage tax rules and overrides for companies
  name: Avalara TaxRules API
  slug: avalara-taxrules-api
- description: Manage tax transactions
  name: Avalara Transactions API
  slug: avalara-transactions-api
- description: The Upcs API from Avalara — 3 operation(s) for upcs.
  name: Avalara Upcs API
  slug: avalara-upcs-api
- description: The UserDefinedFields API from Avalara — 2 operation(s) for userdefinedfields.
  name: Avalara UserDefinedFields API
  slug: avalara-userdefinedfields-api
- description: The Users API from Avalara — 5 operation(s) for users.
  name: Avalara Users API
  slug: avalara-users-api
- description: Utility endpoints including ping and health checks
  name: Avalara Utilities API
  slug: avalara-utilities-api
- description: Collect and manage W-9 forms
  name: Avalara W-9 Forms API
  slug: avalara-w-9-forms-api
arazzos:
- description: Retrieve a committed transaction and adjust it with a corrected, documented replacement.
  name: Avalara Adjust a Committed Transaction
  slug: avalara-adjust-committed-transaction-workflow
- description: Validate the ship-to address, calculate tax on a sale, commit it, then read it back.
  name: Avalara Calculate and Commit a Transaction
  slug: avalara-calculate-and-commit-transaction-workflow
- description: Look up tax codes, register a product item with a tax code, then quote tax for that item.
  name: Avalara Classify an Item and Test Its Tax
  slug: avalara-classify-item-and-test-tax-workflow
- description: Create a new company and declare its first tax nexus, then confirm the nexus list.
  name: Avalara Create Company With Nexus
  slug: avalara-create-company-with-nexus-workflow
- description: Get a free estimated rate for an address, then create a full transaction quote there.
  name: Avalara Estimate Rate Then Quote
  slug: avalara-estimate-then-quote-workflow
- description: Initialize a company with recommended defaults, then add an extra nexus declaration.
  name: Avalara Initialize Company With Defaults
  slug: avalara-initialize-company-workflow
- description: Create a customer, attach an exemption certificate, then confirm the certificate list.
  name: Avalara Onboard an Exempt Customer
  slug: avalara-onboard-exempt-customer-workflow
- description: Create an uncommitted sales order to quote tax, then branch on whether tax was charged.
  name: Avalara Quick Tax Quote
  slug: avalara-quick-tax-quote-workflow
- description: Look up a committed sale, then issue a refund transaction against it.
  name: Avalara Refund a Transaction
  slug: avalara-refund-transaction-workflow
- description: List a company's available reports, then retrieve the details of the first one.
  name: Avalara Retrieve a Company Report
  slug: avalara-retrieve-company-report-workflow
- description: Create a transaction-import batch for a company, then confirm it in the batch list.
  name: Avalara Submit a Transaction Batch
  slug: avalara-submit-transaction-batch-workflow
- description: Look up an existing transaction, void it, then recreate a corrected version.
  name: Avalara Void and Recreate a Transaction
  slug: avalara-void-and-recreate-transaction-workflow
artifact_total: 696
asyncapis:
- description: AsyncAPI description of the Avalara CertCapture event surface. CertCapture does not publish HTTP webhooks; instead, Avalara provisions a unique per-client AWS SQS queue and publishes change-notificati
  name: Avalara CertCapture AWS SQS Notifications
  slug: avalara-certcapture-sqs-asyncapi
collections:
- collection_type: postman
  name: Avalara 1099 & W-9 API
  slug: postman-avalara-1099-w9
- collection_type: postman
  name: Avalara Activation Service API
  slug: postman-avalara-activation-service
- collection_type: postman
  name: Avalara AvaTax Brazil API
  slug: postman-avalara-avatax-brazil
- collection_type: postman
  name: Avalara AvaTax REST API
  slug: postman-avalara-avatax-rest
- collection_type: postman
  name: Avalara Business API
  slug: postman-avalara-business
- collection_type: postman
  name: Avalara CertCapture API
  slug: postman-avalara-certcapture
- collection_type: postman
  name: Avalara Communications Tax API
  slug: postman-avalara-communications
- collection_type: postman
  name: Avalara E-Invoicing REST API
  slug: postman-avalara-e-invoicing
- collection_type: postman
  name: Avalara Excise Platform API
  slug: postman-avalara-excise
- collection_type: postman
  name: Avalara Automated Tariff Code Classification API
  slug: postman-avalara-hs-code-classification
- collection_type: postman
  name: Avalara Item Classification API
  slug: postman-avalara-item-classification
- collection_type: postman
  name: Avalara MyLodgeTax API
  slug: postman-avalara-mylodgetax
- collection_type: postman
  name: Avalara Portal OAuth API
  slug: postman-avalara-portal-oauth
- collection_type: postman
  name: Avalara Shared Company Service API
  slug: postman-avalara-shared-company-service
- collection_type: postman
  name: Avalara VAT Reporting API
  slug: postman-avalara-vat-reporting
- collection_type: open
  name: Avalara 1099 & W-9 API
  slug: open-avalara-1099-w9
- collection_type: open
  name: Avalara Activation Service API
  slug: open-avalara-activation-service
- collection_type: open
  name: Avalara AvaTax Brazil API
  slug: open-avalara-avatax-brazil
- collection_type: open
  name: Avalara AvaTax REST API
  slug: open-avalara-avatax-rest
- collection_type: open
  name: Avalara Business API
  slug: open-avalara-business
- collection_type: open
  name: Avalara CertCapture API
  slug: open-avalara-certcapture
- collection_type: open
  name: Avalara Communications Tax API
  slug: open-avalara-communications
- collection_type: open
  name: Avalara E-Invoicing REST API
  slug: open-avalara-e-invoicing
- collection_type: open
  name: Avalara Excise Platform API
  slug: open-avalara-excise
- collection_type: open
  name: Avalara Automated Tariff Code Classification API
  slug: open-avalara-hs-code-classification
- collection_type: open
  name: Avalara Item Classification API
  slug: open-avalara-item-classification
- collection_type: open
  name: Avalara MyLodgeTax API
  slug: open-avalara-mylodgetax
- collection_type: open
  name: Avalara Portal OAuth API
  slug: open-avalara-portal-oauth
- collection_type: open
  name: Avalara Shared Company Service API
  slug: open-avalara-shared-company-service
- collection_type: open
  name: Avalara VAT Reporting API
  slug: open-avalara-vat-reporting
- collection_type: open
  name: Avalara AvaTax APIs
  slug: open-avatax-apis
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/avalara-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/avalara-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/avalara-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/avalara-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/avalara-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/avalara-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/avalara-llms.txt
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/avalara-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/avalara-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/avalara-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/avalara-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/avalara-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/avalara-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/avalara-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/avalara-data-model.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/avalara-trust-center.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/avalara-avatax-rest-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avalara-avatax-apis-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avalara-avatax-brazil-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avalara-communications-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avalara-excise-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avalara-item-classification-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avalara-hs-code-classification-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avalara-vat-reporting-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avalara-mylodgetax-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avalara-certcapture-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avalara-e-invoicing-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avalara-activation-service-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avalara-business-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avalara-portal-oauth-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avalara-shared-company-service-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avalara-1099-w9-overlay.yaml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/avalara-adjust-committed-transaction-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/avalara-calculate-and-commit-transaction-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/avalara-classify-item-and-test-tax-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/avalara-create-company-with-nexus-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/avalara-estimate-then-quote-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/avalara-initialize-company-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/avalara-onboard-exempt-customer-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/avalara-quick-tax-quote-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/avalara-refund-transaction-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/avalara-retrieve-company-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/avalara-submit-transaction-batch-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/avalara-void-and-recreate-transaction-workflow.yml
- group: build
  title: ''
  type: SDKs
  url: https://developer.avalara.com/sdk/
- group: operate
  title: ''
  type: Community
  url: https://developer.avalara.com/developer-community/
- group: company
  title: ''
  type: Blog
  url: https://developer.avalara.com/blogs/
- group: operate
  title: ''
  type: Support
  url: https://developer.avalara.com/resources/support/
- group: operate
  title: ''
  type: Contact
  url: https://knowledge.avalara.com/bundle/xti1670300535545/page/contact_avalara_support.html
- group: other
  title: ''
  type: AskQuestions
  url: https://developercommunity.avalara.com/s/
- group: auth
  title: ''
  type: Certifications
  url: https://developer.avalara.com/certification/avatax/
- group: learn
  title: ''
  type: Webinars
  url: https://www.avalara.com/us/en/learn/webinars.html#developerwebinars
- group: learn
  title: ''
  type: Learning
  url: https://training.avalara.com/pages/product-training
- group: docs
  title: ''
  type: Schema
  url: https://developer.avalara.com/elr-usecases/
- group: start
  title: ''
  type: Portal
  url: https://developer.avalara.com/
- group: other
  title: ''
  type: Explorer
  url: https://developer.avalara.com/api-reference/
- group: agent
  title: ''
  type: MCPServers
  url: https://developer.avalara.com/mcp-servers/
- group: start
  title: ''
  type: Trial
  url: https://developer.avalara.com/freeTrial/
- group: docs
  title: ''
  type: Guide
  url: https://developer.avalara.com/documentation/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.avalara.com/#siteterms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.avalara.com/dpa#privacynotice
- group: other
  title: ''
  type: Customers
  url: https://www.avalara.com/us/en/about/customer-stories.html
- group: company
  title: ''
  type: Careers
  url: https://careers.avalara.com/north-america
- group: company
  title: ''
  type: Partners
  url: https://www.avalara.com/us/en/partners/partner-programs.html
- group: company
  title: ''
  type: Newsroom
  url: https://newsroom.avalara.com/
- group: other
  title: ''
  type: WhitePapers
  url: https://www.avalara.com/us/en/learn/whitepapers.html
- group: other
  title: ''
  type: Events
  url: https://www.avalara.com/us/en/learn/events.html
- group: learn
  title: ''
  type: Training
  url: https://training.avalara.com/pages/product-training
- group: start
  title: ''
  type: Login
  url: https://www.avalara.com/us/en/signin.html
- group: docs
  title: ''
  type: Documentation
  url: https://developer.avalara.com/api-reference/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.avalara.com/patch-notes/
- group: design
  title: ''
  type: Versioning
  url: https://developer.avalara.com/api-versioning/
- group: start
  title: ''
  type: Signup
  url: https://buy.avalara.com/
- group: auth
  title: ''
  type: Compliance
  url: https://legal.avalara.com/compliance?_gl=1*1hevp4p*_gcl_au*MTM1NDY3OTg2MC4xNzYzNjY2Njc5LjEzNjM2NTU5NjEuMTc2MzY2ODQ1OC4xNzYzNjY4NzA3
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/avalara/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/Avalara
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/api-evangelist/avalara/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Avalara
- group: docs
  title: ''
  type: Swagger
  url: https://github.com/Avalara/Swagger
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.avalara.com/get-started/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.avalara.com/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.avalara.com/avatax/authentication-in-rest/
- group: design
  title: ''
  type: ErrorCodes
  url: https://developer.avalara.com/avatax/errors/
- group: start
  title: ''
  type: Sandbox
  url: https://developer.avalara.com/ecommerce-integration-guide/sales-tax-badge/authentication-in-avatax/sandbox-vs-production/
- group: operate
  title: ''
  type: FAQ
  url: https://help.avalara.com/Frequently_Asked_Questions/API_FAQ
- group: design
  title: ''
  type: ErrorsAndOutages
  url: https://developer.avalara.com/avatax/errors-and-outages/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://knowledge.avalara.com/category/release_notes
- group: other
  title: ''
  type: X
  url: https://twitter.com/avalara
- group: design
  title: ''
  type: JSONLD
  url: json-ld/avalara-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/avalara-transaction-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/avalara-company-schema.json
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/avalara/refs/heads/main/rules/avalara-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/avalara/refs/heads/main/vocabulary/avalara-vocabulary.yaml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.avalara.com/llms.txt
created: '2025-11-19'
description: Avalara helps businesses of all sizes get tax compliance right. We deliver cloud-based solutions that work with existing business applications to calculate tax accurately and file returns automatically.
examples:
- key_count: 4
  name: 1099 W9 Filing Response Example
  slug: 1099-w9-filing-response-example
- key_count: 5
  name: 1099 W9 Filing Status Example
  slug: 1099-w9-filing-status-example
- key_count: 3
  name: 1099 W9 Filing Submission Example
  slug: 1099-w9-filing-submission-example
- key_count: 11
  name: 1099 W9 Form1099 Example
  slug: 1099-w9-form1099-example
- key_count: 7
  name: 1099 W9 Payer Company Example
  slug: 1099-w9-payer-company-example
- key_count: 9
  name: 1099 W9 W9 Form Example
  slug: 1099-w9-w9-form-example
- key_count: 5
  name: 1099 W9 W9 Request Example
  slug: 1099-w9-w9-request-example
- key_count: 5
  name: 1099 W9 W9 Request Response Example
  slug: 1099-w9-w9-request-response-example
- key_count: 9
  name: Activation Service Registration Example
  slug: activation-service-registration-example
- key_count: 2
  name: Activation Service Registration List Example
  slug: activation-service-registration-list-example
- key_count: 17
  name: Avalara Company Example
  slug: avalara-company-example
- key_count: 20
  name: Avalara Transaction Example
  slug: avalara-transaction-example
- key_count: 7
  name: Avatax Brazil Brazil Company Example
  slug: avatax-brazil-brazil-company-example
- key_count: 6
  name: Avatax Brazil Brazil Party Example
  slug: avatax-brazil-brazil-party-example
- key_count: 6
  name: Avatax Brazil Brazil Tax Detail Example
  slug: avatax-brazil-brazil-tax-detail-example
- key_count: 10
  name: Avatax Brazil Calculation Line Example
  slug: avatax-brazil-calculation-line-example
- key_count: 2
  name: Avatax Brazil Calculation Request Example
  slug: avatax-brazil-calculation-request-example
- key_count: 2
  name: Avatax Brazil Calculation Response Example
  slug: avatax-brazil-calculation-response-example
- key_count: 3
  name: Avatax Brazil Calculation Result Line Example
  slug: avatax-brazil-calculation-result-line-example
- key_count: 7
  name: Avatax Brazil Invoice Line Example
  slug: avatax-brazil-invoice-line-example
- key_count: 4
  name: Avatax Brazil Invoice Request Example
  slug: avatax-brazil-invoice-request-example
- key_count: 7
  name: Avatax Brazil Invoice Response Example
  slug: avatax-brazil-invoice-response-example
- key_count: 7
  name: Avatax Rest Account Model Example
  slug: avatax-rest-account-model-example
- key_count: 9
  name: Avatax Rest Address Info Example
  slug: avatax-rest-address-info-example
- key_count: 4
  name: Avatax Rest Address Resolution Model Example
  slug: avatax-rest-address-resolution-model-example
- key_count: 8
  name: Avatax Rest Address Validation Info Example
  slug: avatax-rest-address-validation-info-example
- key_count: 2
  name: Avatax Rest Adjust Transaction Model Example
  slug: avatax-rest-adjust-transaction-model-example
- key_count: 8
  name: Avatax Rest Batch Model Example
  slug: avatax-rest-batch-model-example
- key_count: 10
  name: Avatax Rest Certificate Model Example
  slug: avatax-rest-certificate-model-example
- key_count: 1
  name: Avatax Rest Commit Transaction Model Example
  slug: avatax-rest-commit-transaction-model-example
- key_count: 16
  name: Avatax Rest Company Initialization Model Example
  slug: avatax-rest-company-initialization-model-example
- key_count: 15
  name: Avatax Rest Company Model Example
  slug: avatax-rest-company-model-example
- key_count: 2
  name: Avatax Rest Create Multi Document Model Example
  slug: avatax-rest-create-multi-document-model-example
- key_count: 8
  name: Avatax Rest Create Transaction Model Example
  slug: avatax-rest-create-transaction-model-example
- key_count: 11
  name: Avatax Rest Customer Model Example
  slug: avatax-rest-customer-model-example
- key_count: 1
  name: Avatax Rest Error Result Example
  slug: avatax-rest-error-result-example
- key_count: 2
  name: Avatax Rest Fetch Result_ Certificate Model Example
  slug: avatax-rest-fetch-result_-certificate-model-example
- key_count: 2
  name: Avatax Rest Fetch Result_ Company Model Example
  slug: avatax-rest-fetch-result_-company-model-example
- key_count: 2
  name: Avatax Rest Fetch Result_ Customer Model Example
  slug: avatax-rest-fetch-result_-customer-model-example
- key_count: 2
  name: Avatax Rest Fetch Result_ Item Model Example
  slug: avatax-rest-fetch-result_-item-model-example
- key_count: 2
  name: Avatax Rest Fetch Result_ Location Model Example
  slug: avatax-rest-fetch-result_-location-model-example
- key_count: 2
  name: Avatax Rest Fetch Result_ Nexus Model Example
  slug: avatax-rest-fetch-result_-nexus-model-example
- key_count: 2
  name: Avatax Rest Fetch Result_ Tax Code Model Example
  slug: avatax-rest-fetch-result_-tax-code-model-example
- key_count: 6
  name: Avatax Rest Item Model Example
  slug: avatax-rest-item-model-example
- key_count: 8
  name: Avatax Rest Line Item Model Example
  slug: avatax-rest-line-item-model-example
- key_count: 11
  name: Avatax Rest Location Model Example
  slug: avatax-rest-location-model-example
- key_count: 7
  name: Avatax Rest Multi Document Line Item Model Example
  slug: avatax-rest-multi-document-line-item-model-example
- key_count: 12
  name: Avatax Rest Nexus Model Example
  slug: avatax-rest-nexus-model-example
- key_count: 7
  name: Avatax Rest Ping Result Model Example
  slug: avatax-rest-ping-result-model-example
- key_count: 5
  name: Avatax Rest Refund Transaction Model Example
  slug: avatax-rest-refund-transaction-model-example
- key_count: 4
  name: Avatax Rest Tax Authority Info Example
  slug: avatax-rest-tax-authority-info-example
- key_count: 7
  name: Avatax Rest Tax Code Model Example
  slug: avatax-rest-tax-code-model-example
- key_count: 2
  name: Avatax Rest Tax Rate Model Example
  slug: avatax-rest-tax-rate-model-example
- key_count: 11
  name: Avatax Rest Tax Rule Model Example
  slug: avatax-rest-tax-rule-model-example
- key_count: 8
  name: Avatax Rest Transaction Address Model Example
  slug: avatax-rest-transaction-address-model-example
- key_count: 8
  name: Avatax Rest Transaction Line Model Example
  slug: avatax-rest-transaction-line-model-example
- key_count: 13
  name: Avatax Rest Transaction Model Example
  slug: avatax-rest-transaction-model-example
- key_count: 10
  name: Avatax Rest Transaction Summary Example
  slug: avatax-rest-transaction-summary-example
- key_count: 1
  name: Avatax Rest Void Transaction Model Example
  slug: avatax-rest-void-transaction-model-example
- key_count: 7
  name: Business Account Registration Example
  slug: business-account-registration-example
- key_count: 5
  name: Business Account Response Example
  slug: business-account-response-example
- key_count: 4
  name: Business Order Response Example
  slug: business-order-response-example
- key_count: 3
  name: Business Sales Order Example
  slug: business-sales-order-example
- key_count: 4
  name: Certcapture Cert Attribute Example
  slug: certcapture-cert-attribute-example
- key_count: 10
  name: Certcapture Cert Capture Customer Example
  slug: certcapture-cert-capture-customer-example
- key_count: 8
  name: Certcapture Certificate Create Request Example
  slug: certcapture-certificate-create-request-example
- key_count: 11
  name: Certcapture Certificate Example
  slug: certcapture-certificate-example
- key_count: 2
  name: Certcapture Certificate List Response Example
  slug: certcapture-certificate-list-response-example
- key_count: 2
  name: Certcapture Customer List Response Example
  slug: certcapture-customer-list-response-example
- key_count: 2
  name: Communications Calc Adj Request Example
  slug: communications-calc-adj-request-example
- key_count: 1
  name: Communications Calc Taxes Request Example
  slug: communications-calc-taxes-request-example
- key_count: 1
  name: Communications Calc Taxes Response Example
  slug: communications-calc-taxes-response-example
- key_count: 2
  name: Communications Commit Request Example
  slug: communications-commit-request-example
- key_count: 1
  name: Communications Commit Response Example
  slug: communications-commit-response-example
- key_count: 5
  name: Communications Company Data Example
  slug: communications-company-data-example
- key_count: 4
  name: Communications Exclusion Example
  slug: communications-exclusion-example
- key_count: 6
  name: Communications Geocode Request Example
  slug: communications-geocode-request-example
- key_count: 10
  name: Communications Geocode Result Example
  slug: communications-geocode-result-example
- key_count: 5
  name: Communications Invoice Example
  slug: communications-invoice-example
- key_count: 2
  name: Communications Invoice Result Example
  slug: communications-invoice-result-example
- key_count: 8
  name: Communications Line Item Example
  slug: communications-line-item-example
- key_count: 2
  name: Communications Line Item Result Example
  slug: communications-line-item-result-example
- key_count: 7
  name: Communications Location Example
  slug: communications-location-example
- key_count: 2
  name: Communications Service Info Example
  slug: communications-service-info-example
- key_count: 4
  name: Communications Tax Profile Example
  slug: communications-tax-profile-example
- key_count: 16
  name: Communications Tax Result Example
  slug: communications-tax-result-example
- key_count: 4
  name: Communications Ts Pair Model Example
  slug: communications-ts-pair-model-example
- key_count: 11
  name: E Invoicing Document Detail Example
  slug: e-invoicing-document-detail-example
- key_count: 3
  name: E Invoicing Document Event Example
  slug: e-invoicing-document-event-example
- key_count: 2
  name: E Invoicing Document List Example
  slug: e-invoicing-document-list-example
- key_count: 4
  name: E Invoicing Document Status Example
  slug: e-invoicing-document-status-example
- key_count: 3
  name: E Invoicing Document Submission Response Example
  slug: e-invoicing-document-submission-response-example
- key_count: 8
  name: E Invoicing Document Summary Example
  slug: e-invoicing-document-summary-example
- key_count: 4
  name: E Invoicing Interop Document Request Example
  slug: e-invoicing-interop-document-request-example
- key_count: 7
  name: E Invoicing Mandate Example
  slug: e-invoicing-mandate-example
- key_count: 2
  name: E Invoicing Mandate List Example
  slug: e-invoicing-mandate-list-example
- key_count: 4
  name: E Invoicing Party Example
  slug: e-invoicing-party-example
- key_count: 4
  name: E Invoicing Submit Document Request Example
  slug: e-invoicing-submit-document-request-example
- key_count: 5
  name: Excise Business Entity Example
  slug: excise-business-entity-example
- key_count: 6
  name: Excise Excise Address Example
  slug: excise-excise-address-example
- key_count: 7
  name: Excise Excise License Example
  slug: excise-excise-license-example
- key_count: 4
  name: Excise Excise Location Example
  slug: excise-excise-location-example
- key_count: 4
  name: Excise Excise Product Example
  slug: excise-excise-product-example
- key_count: 7
  name: Excise Excise Tax Detail Example
  slug: excise-excise-tax-detail-example
- key_count: 7
  name: Excise Excise Transaction Example
  slug: excise-excise-transaction-example
- key_count: 4
  name: Excise Tax Determination Line Example
  slug: excise-tax-determination-line-example
- key_count: 6
  name: Excise Tax Determination Request Example
  slug: excise-tax-determination-request-example
- key_count: 3
  name: Excise Tax Determination Response Example
  slug: excise-tax-determination-response-example
- key_count: 8
  name: Excise Transaction Line Example
  slug: excise-transaction-line-example
- key_count: 4
  name: Excise Transaction Party Example
  slug: excise-transaction-party-example
- key_count: 4
  name: Hs Code Classification Classification Prediction Example
  slug: hs-code-classification-classification-prediction-example
- key_count: 5
  name: Hs Code Classification Classify Request Example
  slug: hs-code-classification-classify-request-example
- key_count: 4
  name: Hs Code Classification Classify Response Example
  slug: hs-code-classification-classify-response-example
- key_count: 6
  name: Hs Code Classification Hs Code Info Example
  slug: hs-code-classification-hs-code-info-example
- key_count: 4
  name: Item Classification Classification Item Example
  slug: item-classification-classification-item-example
- key_count: 6
  name: Item Classification Classification Request Detail Example
  slug: item-classification-classification-request-detail-example
- key_count: 2
  name: Item Classification Classification Request Example
  slug: item-classification-classification-request-example
- key_count: 2
  name: Item Classification Classification Request List Example
  slug: item-classification-classification-request-list-example
- key_count: 4
  name: Item Classification Classification Request Response Example
  slug: item-classification-classification-request-response-example
- key_count: 5
  name: Item Classification Classification Request Summary Example
  slug: item-classification-classification-request-summary-example
- key_count: 6
  name: Item Classification Classification Result Example
  slug: item-classification-classification-result-example
- key_count: 1
  name: Item Classification Classification Result List Example
  slug: item-classification-classification-result-list-example
- key_count: 7
  name: Item Classification Hs Code Detail Example
  slug: item-classification-hs-code-detail-example
- key_count: 6
  name: Mylodgetax Filing Obligation Example
  slug: mylodgetax-filing-obligation-example
- key_count: 2
  name: Mylodgetax Lodging Tax Rate Response Example
  slug: mylodgetax-lodging-tax-rate-response-example
- key_count: 5
  name: Mylodgetax Rental Property Example
  slug: mylodgetax-rental-property-example
- key_count: 2
  name: Portal Oauth O Auth Error Example
  slug: portal-oauth-o-auth-error-example
- key_count: 5
  name: Portal Oauth Token Response Example
  slug: portal-oauth-token-response-example
- key_count: 2
  name: Shared Company Service Company List Example
  slug: shared-company-service-company-list-example
- key_count: 10
  name: Shared Company Service Shared Company Example
  slug: shared-company-service-shared-company-example
- key_count: 7
  name: Shared Company Service Shared Contact Example
  slug: shared-company-service-shared-contact-example
- key_count: 7
  name: Vat Reporting Filing Calendar Entry Example
  slug: vat-reporting-filing-calendar-entry-example
- key_count: 3
  name: Vat Reporting Onboarding Request Example
  slug: vat-reporting-onboarding-request-example
- key_count: 2
  name: Vat Reporting Return List Example
  slug: vat-reporting-return-list-example
- key_count: 2
  name: Vat Reporting Transaction Batch Example
  slug: vat-reporting-transaction-batch-example
- key_count: 13
  name: Vat Reporting Vat Return Example
  slug: vat-reporting-vat-return-example
- key_count: 11
  name: Vat Reporting Vat Transaction Example
  slug: vat-reporting-vat-transaction-example
features:
- description: Instant sales tax, VAT, and GST calculations for every transaction across all jurisdictions globally.
  name: Real-Time Tax Calculation
- description: Automated collection, validation, and storage of tax exemption certificates through CertCapture.
  name: Exemption Certificate Management
- description: Country-specific e-invoicing mandate support for cross-border and domestic compliance workflows.
  name: E-Invoicing Compliance
- description: Postal address validation and tax jurisdiction determination for US and international addresses.
  name: Address Validation
- description: AI-powered Harmonized System Code and Avalara Tax Code classification for products.
  name: HS Code Classification
- description: Model Context Protocol servers connecting AI applications with Avalara tax compliance systems.
  name: MCP Server Support
- description: AvaTax REST API supports OData query parameters including filter, top, skip, and orderBy.
  name: OData Query Support
- description: Dedicated sandbox environment at sandbox-rest.avatax.com for testing without production impact.
  name: Sandbox Environment
finops:
- name: Avalara Finops
  service_category: Tax Compliance
  slug: avalara-finops
graphqls:
- description: Avalara provides automated tax compliance through a suite of REST APIs. Avalara does not natively offer a GraphQL endpoint. This conceptual GraphQL schema translates the AvaTax REST API v2 surface — a
  name: Avalara GraphQL Schema
  slug: avalara-graphql
image: https://www.avalara.com/us/en/about/newsroom/media-kit/_jcr_content/root/responsivegrid/responsivegrid/columncontrol/par2/image.coreimg.svg/1614712826993/avalara-logo.svg
integrations:
- description: Native Salesforce integration for tax calculation in CPQ, billing, and order management.
  name: Salesforce
- description: SAP ERP integration for automated tax calculation in S/4HANA and Business One.
  name: SAP
- description: NetSuite SuiteApp integration for sales tax automation within the ERP.
  name: NetSuite
- description: Shopify integration for automated sales tax calculation and exemption management.
  name: Shopify
- description: WooCommerce plugin for WordPress e-commerce sales tax automation.
  name: WooCommerce
- description: QuickBooks integration for small business sales tax calculation and filing.
  name: QuickBooks
- description: Adobe Commerce (Magento) integration for tax calculation in e-commerce.
  name: Magento
- description: Microsoft Dynamics 365 integration for enterprise tax automation.
  name: Microsoft Dynamics
json_schemas:
- name: FilingResponse
  property_count: 4
  slug: 1099-w9-filing-response
- name: FilingStatus
  property_count: 5
  slug: 1099-w9-filing-status
- name: FilingSubmission
  property_count: 3
  slug: 1099-w9-filing-submission
- name: Form1099
  property_count: 11
  slug: 1099-w9-form1099
- name: PayerCompany
  property_count: 7
  slug: 1099-w9-payer-company
- name: W9Form
  property_count: 9
  slug: 1099-w9-w9-form
- name: W9RequestResponse
  property_count: 5
  slug: 1099-w9-w9-request-response
- name: W9Request
  property_count: 5
  slug: 1099-w9-w9-request
- name: RegistrationList
  property_count: 2
  slug: activation-service-registration-list
- name: Registration
  property_count: 9
  slug: activation-service-registration
- name: AccountModel
  property_count: 7
  slug: avalara-accountmodel
- name: AccountRegistration
  property_count: 7
  slug: avalara-accountregistration
- name: AccountResponse
  property_count: 5
  slug: avalara-accountresponse
- name: AddressInfo
  property_count: 9
  slug: avalara-addressinfo
- name: AddressResolutionModel
  property_count: 5
  slug: avalara-addressresolutionmodel
- name: AddressValidationInfo
  property_count: 8
  slug: avalara-addressvalidationinfo
- name: AdjustTransactionModel
  property_count: 3
  slug: avalara-adjusttransactionmodel
- name: BatchModel
  property_count: 8
  slug: avalara-batchmodel
- name: BrazilCompany
  property_count: 7
  slug: avalara-brazilcompany
- name: BrazilParty
  property_count: 6
  slug: avalara-brazilparty
- name: BrazilTaxDetail
  property_count: 6
  slug: avalara-braziltaxdetail
- name: BusinessEntity
  property_count: 6
  slug: avalara-businessentity
- name: CalcAdjRequest
  property_count: 3
  slug: avalara-calcadjrequest
- name: CalcTaxesRequest
  property_count: 2
  slug: avalara-calctaxesrequest
- name: CalcTaxesResponse
  property_count: 1
  slug: avalara-calctaxesresponse
- name: CalculationLine
  property_count: 10
  slug: avalara-calculationline
- name: CalculationRequest
  property_count: 2
  slug: avalara-calculationrequest
- name: CalculationResponse
  property_count: 2
  slug: avalara-calculationresponse
- name: CalculationResultLine
  property_count: 3
  slug: avalara-calculationresultline
- name: CertAttribute
  property_count: 4
  slug: avalara-certattribute
- name: CertCaptureCustomer
  property_count: 10
  slug: avalara-certcapturecustomer
- name: Certificate
  property_count: 12
  slug: avalara-certificate
- name: CertificateCreateRequest
  property_count: 8
  slug: avalara-certificatecreaterequest
- name: CertificateListResponse
  property_count: 2
  slug: avalara-certificatelistresponse
- name: CertificateModel
  property_count: 10
  slug: avalara-certificatemodel
- name: ClassificationItem
  property_count: 4
  slug: avalara-classificationitem
- name: ClassificationPrediction
  property_count: 4
  slug: avalara-classificationprediction
- name: ClassificationRequest
  property_count: 2
  slug: avalara-classificationrequest
- name: ClassificationRequestDetail
  property_count: 6
  slug: avalara-classificationrequestdetail
- name: ClassificationRequestList
  property_count: 2
  slug: avalara-classificationrequestlist
- name: ClassificationRequestResponse
  property_count: 4
  slug: avalara-classificationrequestresponse
- name: ClassificationRequestSummary
  property_count: 5
  slug: avalara-classificationrequestsummary
- name: ClassificationResult
  property_count: 6
  slug: avalara-classificationresult
- name: ClassificationResultList
  property_count: 1
  slug: avalara-classificationresultlist
- name: ClassifyRequest
  property_count: 5
  slug: avalara-classifyrequest
- name: ClassifyResponse
  property_count: 4
  slug: avalara-classifyresponse
- name: CommitRequest
  property_count: 2
  slug: avalara-commitrequest
- name: CommitResponse
  property_count: 1
  slug: avalara-commitresponse
- name: CommitTransactionModel
  property_count: 1
  slug: avalara-committransactionmodel
- name: Avalara Company
  property_count: 18
  slug: avalara-company
- name: CompanyData
  property_count: 5
  slug: avalara-companydata
- name: CompanyInitializationModel
  property_count: 16
  slug: avalara-companyinitializationmodel
- name: CompanyList
  property_count: 2
  slug: avalara-companylist
- name: CompanyModel
  property_count: 15
  slug: avalara-companymodel
- name: CreateMultiDocumentModel
  property_count: 2
  slug: avalara-createmultidocumentmodel
- name: CreateTransactionModel
  property_count: 8
  slug: avalara-createtransactionmodel
- name: CustomerListResponse
  property_count: 2
  slug: avalara-customerlistresponse
- name: CustomerModel
  property_count: 11
  slug: avalara-customermodel
- name: DocumentDetail
  property_count: 13
  slug: avalara-documentdetail
- name: DocumentEvent
  property_count: 3
  slug: avalara-documentevent
- name: DocumentList
  property_count: 2
  slug: avalara-documentlist
- name: DocumentStatus
  property_count: 4
  slug: avalara-documentstatus
- name: DocumentSubmissionResponse
  property_count: 3
  slug: avalara-documentsubmissionresponse
- name: DocumentSummary
  property_count: 8
  slug: avalara-documentsummary
- name: ErrorResponse
  property_count: 1
  slug: avalara-errorresponse
- name: ErrorResult
  property_count: 1
  slug: avalara-errorresult
- name: ExciseAddress
  property_count: 6
  slug: avalara-exciseaddress
- name: ExciseLicense
  property_count: 7
  slug: avalara-exciselicense
- name: ExciseLocation
  property_count: 5
  slug: avalara-exciselocation
- name: ExciseProduct
  property_count: 4
  slug: avalara-exciseproduct
- name: ExciseTaxDetail
  property_count: 7
  slug: avalara-excisetaxdetail
- name: ExciseTransaction
  property_count: 7
  slug: avalara-excisetransaction
- name: Exclusion
  property_count: 4
  slug: avalara-exclusion
- name: FetchResult_CertificateModel
  property_count: 2
  slug: avalara-fetchresult-certificatemodel
- name: FetchResult_CompanyModel
  property_count: 2
  slug: avalara-fetchresult-companymodel
- name: FetchResult_CustomerModel
  property_count: 2
  slug: avalara-fetchresult-customermodel
- name: FetchResult_ItemModel
  property_count: 2
  slug: avalara-fetchresult-itemmodel
- name: FetchResult_LocationModel
  property_count: 2
  slug: avalara-fetchresult-locationmodel
- name: FetchResult_NexusModel
  property_count: 2
  slug: avalara-fetchresult-nexusmodel
- name: FetchResult_TaxCodeModel
  property_count: 2
  slug: avalara-fetchresult-taxcodemodel
- name: FilingCalendarEntry
  property_count: 7
  slug: avalara-filingcalendarentry
- name: FilingObligation
  property_count: 6
  slug: avalara-filingobligation
- name: FilingResponse
  property_count: 4
  slug: avalara-filingresponse
- name: FilingStatus
  property_count: 5
  slug: avalara-filingstatus
- name: FilingSubmission
  property_count: 3
  slug: avalara-filingsubmission
- name: Form1099
  property_count: 11
  slug: avalara-form1099
- name: GeocodeRequest
  property_count: 6
  slug: avalara-geocoderequest
- name: GeocodeResult
  property_count: 10
  slug: avalara-geocoderesult
- name: HSCodeDetail
  property_count: 7
  slug: avalara-hscodedetail
- name: HSCodeInfo
  property_count: 6
  slug: avalara-hscodeinfo
- name: InteropDocumentRequest
  property_count: 4
  slug: avalara-interopdocumentrequest
- name: Invoice
  property_count: 6
  slug: avalara-invoice
- name: InvoiceLine
  property_count: 7
  slug: avalara-invoiceline
- name: InvoiceRequest
  property_count: 5
  slug: avalara-invoicerequest
- name: InvoiceResponse
  property_count: 7
  slug: avalara-invoiceresponse
- name: InvoiceResult
  property_count: 2
  slug: avalara-invoiceresult
- name: ItemModel
  property_count: 6
  slug: avalara-itemmodel
- name: LineItem
  property_count: 10
  slug: avalara-lineitem
- name: LineItemModel
  property_count: 8
  slug: avalara-lineitemmodel
- name: LineItemResult
  property_count: 2
  slug: avalara-lineitemresult
- name: Location
  property_count: 7
  slug: avalara-location
- name: LocationModel
  property_count: 11
  slug: avalara-locationmodel
- name: LodgingTaxRateResponse
  property_count: 2
  slug: avalara-lodgingtaxrateresponse
- name: Mandate
  property_count: 7
  slug: avalara-mandate
- name: MandateList
  property_count: 2
  slug: avalara-mandatelist
- name: MultiDocumentLineItemModel
  property_count: 7
  slug: avalara-multidocumentlineitemmodel
- name: NexusModel
  property_count: 12
  slug: avalara-nexusmodel
- name: OAuthError
  property_count: 2
  slug: avalara-oautherror
- name: OnboardingRequest
  property_count: 3
  slug: avalara-onboardingrequest
- name: OrderResponse
  property_count: 4
  slug: avalara-orderresponse
- name: Party
  property_count: 4
  slug: avalara-party
- name: PayerCompany
  property_count: 7
  slug: avalara-payercompany
- name: PingResultModel
  property_count: 7
  slug: avalara-pingresultmodel
- name: RefundTransactionModel
  property_count: 5
  slug: avalara-refundtransactionmodel
- name: Registration
  property_count: 9
  slug: avalara-registration
- name: RegistrationList
  property_count: 2
  slug: avalara-registrationlist
- name: RentalProperty
  property_count: 5
  slug: avalara-rentalproperty
- name: ReturnList
  property_count: 2
  slug: avalara-returnlist
- name: SalesOrder
  property_count: 3
  slug: avalara-salesorder
- name: ServiceInfo
  property_count: 2
  slug: avalara-serviceinfo
- name: SharedCompany
  property_count: 10
  slug: avalara-sharedcompany
- name: SharedContact
  property_count: 7
  slug: avalara-sharedcontact
- name: SubmitDocumentRequest
  property_count: 4
  slug: avalara-submitdocumentrequest
- name: TaxAuthorityInfo
  property_count: 4
  slug: avalara-taxauthorityinfo
- name: TaxCodeModel
  property_count: 7
  slug: avalara-taxcodemodel
- name: TaxDeterminationLine
  property_count: 4
  slug: avalara-taxdeterminationline
- name: TaxDeterminationRequest
  property_count: 8
  slug: avalara-taxdeterminationrequest
- name: TaxDeterminationResponse
  property_count: 3
  slug: avalara-taxdeterminationresponse
- name: TaxProfile
  property_count: 4
  slug: avalara-taxprofile
- name: TaxRateModel
  property_count: 2
  slug: avalara-taxratemodel
- name: TaxResult
  property_count: 16
  slug: avalara-taxresult
- name: TaxRuleModel
  property_count: 11
  slug: avalara-taxrulemodel
- name: TokenResponse
  property_count: 5
  slug: avalara-tokenresponse
- name: Avalara Tax Transaction
  property_count: 20
  slug: avalara-transaction
- name: TransactionAddressModel
  property_count: 8
  slug: avalara-transactionaddressmodel
- name: TransactionBatch
  property_count: 2
  slug: avalara-transactionbatch
- name: TransactionLine
  property_count: 10
  slug: avalara-transactionline
- name: TransactionLineModel
  property_count: 8
  slug: avalara-transactionlinemodel
- name: TransactionModel
  property_count: 13
  slug: avalara-transactionmodel
- name: TransactionParty
  property_count: 5
  slug: avalara-transactionparty
- name: TransactionSummary
  property_count: 10
  slug: avalara-transactionsummary
- name: TSPairModel
  property_count: 4
  slug: avalara-tspairmodel
- name: VATReturn
  property_count: 13
  slug: avalara-vatreturn
- name: VATTransaction
  property_count: 11
  slug: avalara-vattransaction
- name: VoidTransactionModel
  property_count: 1
  slug: avalara-voidtransactionmodel
- name: W9Form
  property_count: 9
  slug: avalara-w9form
- name: W9Request
  property_count: 5
  slug: avalara-w9request
- name: W9RequestResponse
  property_count: 5
  slug: avalara-w9requestresponse
- name: BrazilCompany
  property_count: 7
  slug: avatax-brazil-brazil-company
- name: BrazilParty
  property_count: 6
  slug: avatax-brazil-brazil-party
- name: BrazilTaxDetail
  property_count: 6
  slug: avatax-brazil-brazil-tax-detail
- name: CalculationLine
  property_count: 10
  slug: avatax-brazil-calculation-line
- name: CalculationRequest
  property_count: 2
  slug: avatax-brazil-calculation-request
- name: CalculationResponse
  property_count: 2
  slug: avatax-brazil-calculation-response
- name: CalculationResultLine
  property_count: 3
  slug: avatax-brazil-calculation-result-line
- name: InvoiceLine
  property_count: 7
  slug: avatax-brazil-invoice-line
- name: InvoiceRequest
  property_count: 5
  slug: avatax-brazil-invoice-request
- name: InvoiceResponse
  property_count: 7
  slug: avatax-brazil-invoice-response
- name: AccountModel
  property_count: 7
  slug: avatax-rest-account-model
- name: AddressInfo
  property_count: 9
  slug: avatax-rest-address-info
- name: AddressResolutionModel
  property_count: 5
  slug: avatax-rest-address-resolution-model
- name: AddressValidationInfo
  property_count: 8
  slug: avatax-rest-address-validation-info
- name: AdjustTransactionModel
  property_count: 3
  slug: avatax-rest-adjust-transaction-model
- name: BatchModel
  property_count: 8
  slug: avatax-rest-batch-model
- name: CertificateModel
  property_count: 10
  slug: avatax-rest-certificate-model
- name: CommitTransactionModel
  property_count: 1
  slug: avatax-rest-commit-transaction-model
- name: CompanyInitializationModel
  property_count: 16
  slug: avatax-rest-company-initialization-model
- name: CompanyModel
  property_count: 15
  slug: avatax-rest-company-model
- name: CreateMultiDocumentModel
  property_count: 2
  slug: avatax-rest-create-multi-document-model
- name: CreateTransactionModel
  property_count: 8
  slug: avatax-rest-create-transaction-model
- name: CustomerModel
  property_count: 11
  slug: avatax-rest-customer-model
- name: ErrorResult
  property_count: 1
  slug: avatax-rest-error-result
- name: FetchResult_CertificateModel
  property_count: 2
  slug: avatax-rest-fetch-result_-certificate-model
- name: FetchResult_CompanyModel
  property_count: 2
  slug: avatax-rest-fetch-result_-company-model
- name: FetchResult_CustomerModel
  property_count: 2
  slug: avatax-rest-fetch-result_-customer-model
- name: FetchResult_ItemModel
  property_count: 2
  slug: avatax-rest-fetch-result_-item-model
- name: FetchResult_LocationModel
  property_count: 2
  slug: avatax-rest-fetch-result_-location-model
- name: FetchResult_NexusModel
  property_count: 2
  slug: avatax-rest-fetch-result_-nexus-model
- name: FetchResult_TaxCodeModel
  property_count: 2
  slug: avatax-rest-fetch-result_-tax-code-model
- name: ItemModel
  property_count: 6
  slug: avatax-rest-item-model
- name: LineItemModel
  property_count: 8
  slug: avatax-rest-line-item-model
- name: LocationModel
  property_count: 11
  slug: avatax-rest-location-model
- name: MultiDocumentLineItemModel
  property_count: 7
  slug: avatax-rest-multi-document-line-item-model
- name: NexusModel
  property_count: 12
  slug: avatax-rest-nexus-model
- name: PingResultModel
  property_count: 7
  slug: avatax-rest-ping-result-model
- name: RefundTransactionModel
  property_count: 5
  slug: avatax-rest-refund-transaction-model
- name: TaxAuthorityInfo
  property_count: 4
  slug: avatax-rest-tax-authority-info
- name: TaxCodeModel
  property_count: 7
  slug: avatax-rest-tax-code-model
- name: TaxRateModel
  property_count: 2
  slug: avatax-rest-tax-rate-model
- name: TaxRuleModel
  property_count: 11
  slug: avatax-rest-tax-rule-model
- name: TransactionAddressModel
  property_count: 8
  slug: avatax-rest-transaction-address-model
- name: TransactionLineModel
  property_count: 8
  slug: avatax-rest-transaction-line-model
- name: TransactionModel
  property_count: 13
  slug: avatax-rest-transaction-model
- name: TransactionSummary
  property_count: 10
  slug: avatax-rest-transaction-summary
- name: VoidTransactionModel
  property_count: 1
  slug: avatax-rest-void-transaction-model
- name: AccountRegistration
  property_count: 7
  slug: business-account-registration
- name: AccountResponse
  property_count: 5
  slug: business-account-response
- name: OrderResponse
  property_count: 4
  slug: business-order-response
- name: SalesOrder
  property_count: 3
  slug: business-sales-order
- name: CertAttribute
  property_count: 4
  slug: certcapture-cert-attribute
- name: CertCaptureCustomer
  property_count: 10
  slug: certcapture-cert-capture-customer
- name: CertificateCreateRequest
  property_count: 8
  slug: certcapture-certificate-create-request
- name: CertificateListResponse
  property_count: 2
  slug: certcapture-certificate-list-response
- name: Certificate
  property_count: 12
  slug: certcapture-certificate
- name: CustomerListResponse
  property_count: 2
  slug: certcapture-customer-list-response
- name: CalcAdjRequest
  property_count: 3
  slug: communications-calc-adj-request
- name: CalcTaxesRequest
  property_count: 2
  slug: communications-calc-taxes-request
- name: CalcTaxesResponse
  property_count: 1
  slug: communications-calc-taxes-response
- name: CommitRequest
  property_count: 2
  slug: communications-commit-request
- name: CommitResponse
  property_count: 1
  slug: communications-commit-response
- name: CompanyData
  property_count: 5
  slug: communications-company-data
- name: Exclusion
  property_count: 4
  slug: communications-exclusion
- name: GeocodeRequest
  property_count: 6
  slug: communications-geocode-request
- name: GeocodeResult
  property_count: 10
  slug: communications-geocode-result
- name: InvoiceResult
  property_count: 2
  slug: communications-invoice-result
- name: Invoice
  property_count: 6
  slug: communications-invoice
- name: LineItemResult
  property_count: 2
  slug: communications-line-item-result
- name: LineItem
  property_count: 10
  slug: communications-line-item
- name: Location
  property_count: 7
  slug: communications-location
- name: ServiceInfo
  property_count: 2
  slug: communications-service-info
- name: TaxProfile
  property_count: 4
  slug: communications-tax-profile
- name: TaxResult
  property_count: 16
  slug: communications-tax-result
- name: TSPairModel
  property_count: 4
  slug: communications-ts-pair-model
- name: DocumentDetail
  property_count: 13
  slug: e-invoicing-document-detail
- name: DocumentEvent
  property_count: 3
  slug: e-invoicing-document-event
- name: DocumentList
  property_count: 2
  slug: e-invoicing-document-list
- name: DocumentStatus
  property_count: 4
  slug: e-invoicing-document-status
- name: DocumentSubmissionResponse
  property_count: 3
  slug: e-invoicing-document-submission-response
- name: DocumentSummary
  property_count: 8
  slug: e-invoicing-document-summary
- name: InteropDocumentRequest
  property_count: 4
  slug: e-invoicing-interop-document-request
- name: MandateList
  property_count: 2
  slug: e-invoicing-mandate-list
- name: Mandate
  property_count: 7
  slug: e-invoicing-mandate
- name: Party
  property_count: 4
  slug: e-invoicing-party
- name: SubmitDocumentRequest
  property_count: 4
  slug: e-invoicing-submit-document-request
- name: BusinessEntity
  property_count: 6
  slug: excise-business-entity
- name: ExciseAddress
  property_count: 6
  slug: excise-excise-address
- name: ExciseLicense
  property_count: 7
  slug: excise-excise-license
- name: ExciseLocation
  property_count: 5
  slug: excise-excise-location
- name: ExciseProduct
  property_count: 4
  slug: excise-excise-product
- name: ExciseTaxDetail
  property_count: 7
  slug: excise-excise-tax-detail
- name: ExciseTransaction
  property_count: 7
  slug: excise-excise-transaction
- name: TaxDeterminationLine
  property_count: 4
  slug: excise-tax-determination-line
- name: TaxDeterminationRequest
  property_count: 8
  slug: excise-tax-determination-request
- name: TaxDeterminationResponse
  property_count: 3
  slug: excise-tax-determination-response
- name: TransactionLine
  property_count: 10
  slug: excise-transaction-line
- name: TransactionParty
  property_count: 5
  slug: excise-transaction-party
- name: ClassificationPrediction
  property_count: 4
  slug: hs-code-classification-classification-prediction
- name: ClassifyRequest
  property_count: 5
  slug: hs-code-classification-classify-request
- name: ClassifyResponse
  property_count: 4
  slug: hs-code-classification-classify-response
- name: HSCodeInfo
  property_count: 6
  slug: hs-code-classification-hs-code-info
- name: ClassificationItem
  property_count: 4
  slug: item-classification-classification-item
- name: ClassificationRequestDetail
  property_count: 6
  slug: item-classification-classification-request-detail
- name: ClassificationRequestList
  property_count: 2
  slug: item-classification-classification-request-list
- name: ClassificationRequestResponse
  property_count: 4
  slug: item-classification-classification-request-response
- name: ClassificationRequest
  property_count: 2
  slug: item-classification-classification-request
- name: ClassificationRequestSummary
  property_count: 5
  slug: item-classification-classification-request-summary
- name: ClassificationResultList
  property_count: 1
  slug: item-classification-classification-result-list
- name: ClassificationResult
  property_count: 6
  slug: item-classification-classification-result
- name: HSCodeDetail
  property_count: 7
  slug: item-classification-hs-code-detail
- name: FilingObligation
  property_count: 6
  slug: mylodgetax-filing-obligation
- name: LodgingTaxRateResponse
  property_count: 2
  slug: mylodgetax-lodging-tax-rate-response
- name: RentalProperty
  property_count: 5
  slug: mylodgetax-rental-property
- name: OAuthError
  property_count: 2
  slug: portal-oauth-o-auth-error
- name: TokenResponse
  property_count: 5
  slug: portal-oauth-token-response
- name: CompanyList
  property_count: 2
  slug: shared-company-service-company-list
- name: SharedCompany
  property_count: 10
  slug: shared-company-service-shared-company
- name: SharedContact
  property_count: 7
  slug: shared-company-service-shared-contact
- name: FilingCalendarEntry
  property_count: 7
  slug: vat-reporting-filing-calendar-entry
- name: OnboardingRequest
  property_count: 3
  slug: vat-reporting-onboarding-request
- name: ReturnList
  property_count: 2
  slug: vat-reporting-return-list
- name: TransactionBatch
  property_count: 2
  slug: vat-reporting-transaction-batch
- name: VATReturn
  property_count: 13
  slug: vat-reporting-vat-return
- name: VATTransaction
  property_count: 11
  slug: vat-reporting-vat-transaction
json_structures:
- name: 1099 W9 Filing Response Structure
  property_count: 4
  slug: 1099-w9-filing-response-structure
- name: 1099 W9 Filing Status Structure
  property_count: 5
  slug: 1099-w9-filing-status-structure
- name: 1099 W9 Filing Submission Structure
  property_count: 3
  slug: 1099-w9-filing-submission-structure
- name: 1099 W9 Form1099 Structure
  property_count: 11
  slug: 1099-w9-form1099-structure
- name: 1099 W9 Payer Company Structure
  property_count: 7
  slug: 1099-w9-payer-company-structure
- name: 1099 W9 W9 Form Structure
  property_count: 9
  slug: 1099-w9-w9-form-structure
- name: 1099 W9 W9 Request Response Structure
  property_count: 5
  slug: 1099-w9-w9-request-response-structure
- name: 1099 W9 W9 Request Structure
  property_count: 5
  slug: 1099-w9-w9-request-structure
- name: Activation Service Registration List Structure
  property_count: 2
  slug: activation-service-registration-list-structure
- name: Activation Service Registration Structure
  property_count: 9
  slug: activation-service-registration-structure
- name: Avalara Company Structure
  property_count: 18
  slug: avalara-company-structure
- name: Avalara Structure
  property_count: 0
  slug: avalara-structure
- name: Avatax Brazil Brazil Company Structure
  property_count: 7
  slug: avatax-brazil-brazil-company-structure
- name: Avatax Brazil Brazil Party Structure
  property_count: 6
  slug: avatax-brazil-brazil-party-structure
- name: Avatax Brazil Brazil Tax Detail Structure
  property_count: 6
  slug: avatax-brazil-brazil-tax-detail-structure
- name: Avatax Brazil Calculation Line Structure
  property_count: 10
  slug: avatax-brazil-calculation-line-structure
- name: Avatax Brazil Calculation Request Structure
  property_count: 2
  slug: avatax-brazil-calculation-request-structure
- name: Avatax Brazil Calculation Response Structure
  property_count: 2
  slug: avatax-brazil-calculation-response-structure
- name: Avatax Brazil Calculation Result Line Structure
  property_count: 3
  slug: avatax-brazil-calculation-result-line-structure
- name: Avatax Brazil Invoice Line Structure
  property_count: 7
  slug: avatax-brazil-invoice-line-structure
- name: Avatax Brazil Invoice Request Structure
  property_count: 5
  slug: avatax-brazil-invoice-request-structure
- name: Avatax Brazil Invoice Response Structure
  property_count: 7
  slug: avatax-brazil-invoice-response-structure
- name: Avatax Rest Account Model Structure
  property_count: 7
  slug: avatax-rest-account-model-structure
- name: Avatax Rest Address Info Structure
  property_count: 9
  slug: avatax-rest-address-info-structure
- name: Avatax Rest Address Resolution Model Structure
  property_count: 5
  slug: avatax-rest-address-resolution-model-structure
- name: Avatax Rest Address Validation Info Structure
  property_count: 8
  slug: avatax-rest-address-validation-info-structure
- name: Avatax Rest Adjust Transaction Model Structure
  property_count: 3
  slug: avatax-rest-adjust-transaction-model-structure
- name: Avatax Rest Certificate Model Structure
  property_count: 10
  slug: avatax-rest-certificate-model-structure
- name: Avatax Rest Commit Transaction Model Structure
  property_count: 1
  slug: avatax-rest-commit-transaction-model-structure
- name: Avatax Rest Company Initialization Model Structure
  property_count: 15
  slug: avatax-rest-company-initialization-model-structure
- name: Avatax Rest Company Model Structure
  property_count: 15
  slug: avatax-rest-company-model-structure
- name: Avatax Rest Create Multi Document Model Structure
  property_count: 2
  slug: avatax-rest-create-multi-document-model-structure
- name: Avatax Rest Customer Model Structure
  property_count: 11
  slug: avatax-rest-customer-model-structure
- name: Avatax Rest Error Result Structure
  property_count: 1
  slug: avatax-rest-error-result-structure
- name: Avatax Rest Fetch Result_ Certificate Model Structure
  property_count: 2
  slug: avatax-rest-fetch-result_-certificate-model-structure
- name: Avatax Rest Fetch Result_ Company Model Structure
  property_count: 2
  slug: avatax-rest-fetch-result_-company-model-structure
- name: Avatax Rest Fetch Result_ Customer Model Structure
  property_count: 2
  slug: avatax-rest-fetch-result_-customer-model-structure
- name: Avatax Rest Fetch Result_ Item Model Structure
  property_count: 2
  slug: avatax-rest-fetch-result_-item-model-structure
- name: Avatax Rest Fetch Result_ Location Model Structure
  property_count: 2
  slug: avatax-rest-fetch-result_-location-model-structure
- name: Avatax Rest Fetch Result_ Nexus Model Structure
  property_count: 2
  slug: avatax-rest-fetch-result_-nexus-model-structure
- name: Avatax Rest Fetch Result_ Tax Code Model Structure
  property_count: 2
  slug: avatax-rest-fetch-result_-tax-code-model-structure
- name: Avatax Rest Item Model Structure
  property_count: 6
  slug: avatax-rest-item-model-structure
- name: Avatax Rest Line Item Model Structure
  property_count: 8
  slug: avatax-rest-line-item-model-structure
- name: Avatax Rest Location Model Structure
  property_count: 11
  slug: avatax-rest-location-model-structure
- name: Avatax Rest Multi Document Line Item Model Structure
  property_count: 7
  slug: avatax-rest-multi-document-line-item-model-structure
- name: Avatax Rest Nexus Model Structure
  property_count: 12
  slug: avatax-rest-nexus-model-structure
- name: Avatax Rest Ping Result Model Structure
  property_count: 7
  slug: avatax-rest-ping-result-model-structure
- name: Avatax Rest Refund Transaction Model Structure
  property_count: 5
  slug: avatax-rest-refund-transaction-model-structure
- name: Avatax Rest Tax Authority Info Structure
  property_count: 4
  slug: avatax-rest-tax-authority-info-structure
- name: Avatax Rest Tax Code Model Structure
  property_count: 7
  slug: avatax-rest-tax-code-model-structure
- name: Avatax Rest Tax Rule Model Structure
  property_count: 11
  slug: avatax-rest-tax-rule-model-structure
- name: Avatax Rest Transaction Address Model Structure
  property_count: 8
  slug: avatax-rest-transaction-address-model-structure
- name: Avatax Rest Transaction Line Model Structure
  property_count: 8
  slug: avatax-rest-transaction-line-model-structure
- name: Avatax Rest Transaction Summary Structure
  property_count: 10
  slug: avatax-rest-transaction-summary-structure
- name: Avatax Rest Void Transaction Model Structure
  property_count: 1
  slug: avatax-rest-void-transaction-model-structure
- name: Business Account Registration Structure
  property_count: 7
  slug: business-account-registration-structure
- name: Business Account Response Structure
  property_count: 5
  slug: business-account-response-structure
- name: Business Order Response Structure
  property_count: 4
  slug: business-order-response-structure
- name: Business Sales Order Structure
  property_count: 3
  slug: business-sales-order-structure
- name: Certcapture Cert Attribute Structure
  property_count: 4
  slug: certcapture-cert-attribute-structure
- name: Certcapture Cert Capture Customer Structure
  property_count: 10
  slug: certcapture-cert-capture-customer-structure
- name: Certcapture Certificate Create Request Structure
  property_count: 8
  slug: certcapture-certificate-create-request-structure
- name: Certcapture Certificate List Response Structure
  property_count: 2
  slug: certcapture-certificate-list-response-structure
- name: Certcapture Certificate Structure
  property_count: 12
  slug: certcapture-certificate-structure
- name: Certcapture Customer List Response Structure
  property_count: 2
  slug: certcapture-customer-list-response-structure
- name: Communications Calc Adj Request Structure
  property_count: 3
  slug: communications-calc-adj-request-structure
- name: Communications Calc Taxes Request Structure
  property_count: 2
  slug: communications-calc-taxes-request-structure
- name: Communications Calc Taxes Response Structure
  property_count: 1
  slug: communications-calc-taxes-response-structure
- name: Communications Commit Request Structure
  property_count: 2
  slug: communications-commit-request-structure
- name: Communications Commit Response Structure
  property_count: 1
  slug: communications-commit-response-structure
- name: Communications Company Data Structure
  property_count: 5
  slug: communications-company-data-structure
- name: Communications Exclusion Structure
  property_count: 4
  slug: communications-exclusion-structure
- name: Communications Geocode Request Structure
  property_count: 6
  slug: communications-geocode-request-structure
- name: Communications Geocode Result Structure
  property_count: 10
  slug: communications-geocode-result-structure
- name: Communications Invoice Result Structure
  property_count: 2
  slug: communications-invoice-result-structure
- name: Communications Invoice Structure
  property_count: 6
  slug: communications-invoice-structure
- name: Communications Line Item Result Structure
  property_count: 2
  slug: communications-line-item-result-structure
- name: Communications Line Item Structure
  property_count: 10
  slug: communications-line-item-structure
- name: Communications Location Structure
  property_count: 7
  slug: communications-location-structure
- name: Communications Service Info Structure
  property_count: 2
  slug: communications-service-info-structure
- name: Communications Tax Profile Structure
  property_count: 4
  slug: communications-tax-profile-structure
- name: Communications Tax Result Structure
  property_count: 16
  slug: communications-tax-result-structure
- name: Communications Ts Pair Model Structure
  property_count: 4
  slug: communications-ts-pair-model-structure
- name: E Invoicing Document Detail Structure
  property_count: 13
  slug: e-invoicing-document-detail-structure
- name: E Invoicing Document Event Structure
  property_count: 3
  slug: e-invoicing-document-event-structure
- name: E Invoicing Document List Structure
  property_count: 2
  slug: e-invoicing-document-list-structure
- name: E Invoicing Document Status Structure
  property_count: 4
  slug: e-invoicing-document-status-structure
- name: E Invoicing Document Submission Response Structure
  property_count: 3
  slug: e-invoicing-document-submission-response-structure
- name: E Invoicing Document Summary Structure
  property_count: 8
  slug: e-invoicing-document-summary-structure
- name: E Invoicing Interop Document Request Structure
  property_count: 4
  slug: e-invoicing-interop-document-request-structure
- name: E Invoicing Mandate List Structure
  property_count: 2
  slug: e-invoicing-mandate-list-structure
- name: E Invoicing Mandate Structure
  property_count: 7
  slug: e-invoicing-mandate-structure
- name: E Invoicing Party Structure
  property_count: 4
  slug: e-invoicing-party-structure
- name: E Invoicing Submit Document Request Structure
  property_count: 4
  slug: e-invoicing-submit-document-request-structure
- name: Excise Business Entity Structure
  property_count: 6
  slug: excise-business-entity-structure
- name: Excise Excise Address Structure
  property_count: 6
  slug: excise-excise-address-structure
- name: Excise Excise License Structure
  property_count: 7
  slug: excise-excise-license-structure
- name: Excise Excise Location Structure
  property_count: 5
  slug: excise-excise-location-structure
- name: Excise Excise Product Structure
  property_count: 4
  slug: excise-excise-product-structure
- name: Excise Excise Tax Detail Structure
  property_count: 7
  slug: excise-excise-tax-detail-structure
- name: Excise Excise Transaction Structure
  property_count: 7
  slug: excise-excise-transaction-structure
- name: Excise Tax Determination Line Structure
  property_count: 4
  slug: excise-tax-determination-line-structure
- name: Excise Tax Determination Request Structure
  property_count: 8
  slug: excise-tax-determination-request-structure
- name: Excise Tax Determination Response Structure
  property_count: 3
  slug: excise-tax-determination-response-structure
- name: Excise Transaction Line Structure
  property_count: 10
  slug: excise-transaction-line-structure
- name: Excise Transaction Party Structure
  property_count: 5
  slug: excise-transaction-party-structure
- name: Hs Code Classification Classification Prediction Structure
  property_count: 4
  slug: hs-code-classification-classification-prediction-structure
- name: Hs Code Classification Classify Request Structure
  property_count: 5
  slug: hs-code-classification-classify-request-structure
- name: Hs Code Classification Classify Response Structure
  property_count: 4
  slug: hs-code-classification-classify-response-structure
- name: Hs Code Classification Hs Code Info Structure
  property_count: 6
  slug: hs-code-classification-hs-code-info-structure
- name: Item Classification Classification Item Structure
  property_count: 4
  slug: item-classification-classification-item-structure
- name: Item Classification Classification Request Detail Structure
  property_count: 6
  slug: item-classification-classification-request-detail-structure
- name: Item Classification Classification Request List Structure
  property_count: 2
  slug: item-classification-classification-request-list-structure
- name: Item Classification Classification Request Response Structure
  property_count: 4
  slug: item-classification-classification-request-response-structure
- name: Item Classification Classification Request Structure
  property_count: 2
  slug: item-classification-classification-request-structure
- name: Item Classification Classification Request Summary Structure
  property_count: 5
  slug: item-classification-classification-request-summary-structure
- name: Item Classification Classification Result List Structure
  property_count: 1
  slug: item-classification-classification-result-list-structure
- name: Item Classification Classification Result Structure
  property_count: 6
  slug: item-classification-classification-result-structure
- name: Item Classification Hs Code Detail Structure
  property_count: 7
  slug: item-classification-hs-code-detail-structure
- name: Mylodgetax Filing Obligation Structure
  property_count: 6
  slug: mylodgetax-filing-obligation-structure
- name: Mylodgetax Lodging Tax Rate Response Structure
  property_count: 2
  slug: mylodgetax-lodging-tax-rate-response-structure
- name: Mylodgetax Rental Property Structure
  property_count: 5
  slug: mylodgetax-rental-property-structure
- name: Portal Oauth O Auth Error Structure
  property_count: 2
  slug: portal-oauth-o-auth-error-structure
- name: Portal Oauth Token Response Structure
  property_count: 5
  slug: portal-oauth-token-response-structure
- name: Shared Company Service Company List Structure
  property_count: 2
  slug: shared-company-service-company-list-structure
- name: Shared Company Service Shared Company Structure
  property_count: 10
  slug: shared-company-service-shared-company-structure
- name: Shared Company Service Shared Contact Structure
  property_count: 7
  slug: shared-company-service-shared-contact-structure
- name: Vat Reporting Filing Calendar Entry Structure
  property_count: 7
  slug: vat-reporting-filing-calendar-entry-structure
- name: Vat Reporting Onboarding Request Structure
  property_count: 3
  slug: vat-reporting-onboarding-request-structure
- name: Vat Reporting Return List Structure
  property_count: 2
  slug: vat-reporting-return-list-structure
- name: Vat Reporting Transaction Batch Structure
  property_count: 2
  slug: vat-reporting-transaction-batch-structure
- name: Vat Reporting Vat Return Structure
  property_count: 13
  slug: vat-reporting-vat-return-structure
- name: Vat Reporting Vat Transaction Structure
  property_count: 11
  slug: vat-reporting-vat-transaction-structure
jsonld:
- class_count: 0
  name: Avalara Context
  property_count: 11
  slug: avalara-context
layout: provider
mcp_servers:
- description: ''
  name: avalara-mcp.yml
  slug: avalara-mcpyml
modified: '2026-06-20'
name: Avalara
nav: Providers
network: true
overview: 'Avalara publishes 66 APIs on the [APIs.io](https://apis.io/) network, including 1099 Forms API, Accounts API, Addresses API, and 63 more. Tagged areas include Taxes.


  The Avalara catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Avalara''s developer surface includes authentication, sandbox, changelog, engineering blog, support, developer portal, training material, and 87 more developer resources.'
plans:
- name: Avalara Plans Pricing
  plan_count: 5
  slug: avalara-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 2
  name: Avalara Rate Limits
  slug: avalara-rate-limits
rules:
- name: Avalara API Rules
  rule_count: 3
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 3
  slug: avalara-asyncapi-spectral-rules
- name: Avalara API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: avalara-jsonschema-spectral-rules
- name: Avalara API Rules
  rule_count: 26
  severity_counts:
    error: 10
    hint: 0
    info: 3
    warn: 13
  slug: avalara-spectral-rules
scopes:
- name: Avalara Scopes
  scope_count: 24
  slug: avalara-scopes
  summary_line: 24 scopes
score:
  band: exemplar
  composite: 75.7
  delta: 0.0
  facets:
    commercial_clarity: 89.5
    contract_quality: 76.3
    developer_ergonomics: 71.7
    discoverability: 68.5
    governance: 83.3
    operational_transparency: 57.9
  previous_composite: 75.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 66
    mcp: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/avalara/refs/heads/main/screenshots/avalara-2026-06-20T172715.png
security:
- kind: authentication
  name: Avalara Authentication
  slug: avalara-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Avalara Domain Security
  slug: avalara-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Avalara Trust Center
  slug: avalara-trust-center
  summary_line: SOC 2 Type 2
slug: avalara
tags:
- Taxes
use_cases:
- description: Automatically calculate and collect sales tax on every transaction across all US jurisdictions.
  name: E-Commerce Tax Compliance
- description: Digitally collect and validate tax exemption certificates from B2B customers at checkout.
  name: Exemption Certificate Automation
- description: Calculate import duties, customs fees, and VAT for international shipments.
  name: Cross-Border Import Duties
- description: Comply with country-specific e-invoicing requirements for EU, LATAM, and APAC markets.
  name: E-Invoicing Mandates
- description: Automate collection and e-filing of 1099, W-9, W-2, and 1042-S forms with the IRS.
  name: 1099 Form Filing
- description: Calculate telecom and communications taxes for voice, data, VoIP, and streaming services.
  name: Communications Tax
- description: Manage short-term rental lodging taxes across all US jurisdictions for marketplaces.
  name: Lodging Tax Management
- description: Automate VAT return preparation and filing across European and global jurisdictions.
  name: VAT Return Filing
website: https://developer.avalara.com/
---

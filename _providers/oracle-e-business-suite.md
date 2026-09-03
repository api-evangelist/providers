---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Oracle E Business Suite Agentic Access
  operation_count: 53
  slug: oracle-e-business-suite-agentic-access
  summary_line: 53 operations · 15 acting
api_count: 6
apis:
- description: SOAP-based web services for Oracle E-Business Suite exposed through the Integrated SOA Gateway. Supports synchronous and asynchronous interaction patterns for PL/SQL APIs, Concurrent Programs, and Bus
  name: Oracle EBS Integrated SOA Gateway SOAP Web Services
  slug: oracle-ebs-integrated-soa-gateway-soap-web-services
- description: The PL/SQL API framework provides the core programmatic interface to Oracle E-Business Suite database objects. These stored procedures and functions enable data manipulation across all EBS modules and
  name: Oracle EBS PL/SQL API Framework
  slug: oracle-ebs-plsql-api-framework
- baseURL: https://{instance}.oracle.com/webservices/rest/
  baseurl_source: declared
  description: Accounts Payable invoice and payment operations
  name: Oracle E-Business Suite Accounts Payable API
  slug: oracle-e-business-suite-accounts-payable-api
- baseURL: https://{instance}.oracle.com/webservices/rest/
  baseurl_source: declared
  description: Accounts Receivable invoice and receipt operations
  name: Oracle E-Business Suite Accounts Receivable API
  slug: oracle-e-business-suite-accounts-receivable-api
- baseURL: https://{instance}.oracle.com/webservices/rest/
  baseurl_source: declared
  description: Login, session initialization, and logout operations
  name: Oracle E-Business Suite Authentication API
  slug: oracle-e-business-suite-authentication-api
- baseURL: https://{instance}.oracle.com/webservices/rest/
  baseurl_source: declared
  description: Benefit enrollment management
  name: Oracle E-Business Suite Benefits API
  slug: oracle-e-business-suite-benefits-api
- baseURL: https://{instance}.oracle.com/webservices/rest/
  baseurl_source: declared
  description: BOM and routing management
  name: Oracle E-Business Suite Bills of Material API
  slug: oracle-e-business-suite-bills-of-material-api
- baseURL: https://{instance}.oracle.com/webservices/rest/
  baseurl_source: declared
  description: Cash management and bank account operations
  name: Oracle E-Business Suite Cash Management API
  slug: oracle-e-business-suite-cash-management-api
- baseURL: https://{instance}.oracle.com/webservices/rest/
  baseurl_source: declared
  description: EDI code conversion mapping management
  name: Oracle E-Business Suite Code Conversions API
  slug: oracle-e-business-suite-code-conversions-api
- baseURL: https://{instance}.oracle.com/webservices/rest/
  baseurl_source: declared
  description: Employee and assignment management operations
  name: Oracle E-Business Suite Employee Management API
  slug: oracle-e-business-suite-employee-management-api
- baseURL: https://{instance}.oracle.com/webservices/rest/
  baseurl_source: declared
  description: Fixed asset management operations
  name: Oracle E-Business Suite Fixed Assets API
  slug: oracle-e-business-suite-fixed-assets-api
- baseURL: https://{instance}.oracle.com/webservices/rest/
  baseurl_source: declared
  description: General Ledger journal operations
  name: Oracle E-Business Suite General Ledger API
  slug: oracle-e-business-suite-general-ledger-api
- baseURL: https://{instance}.oracle.com/webservices/rest/
  baseurl_source: declared
  description: Inbound EDI document processing
  name: Oracle E-Business Suite Inbound Transactions API
  slug: oracle-e-business-suite-inbound-transactions-api
- baseURL: https://{instance}.oracle.com/webservices/rest/
  baseurl_source: declared
  description: Inventory items and on-hand quantity management
  name: Oracle E-Business Suite Inventory API
  slug: oracle-e-business-suite-inventory-api
- baseURL: https://{instance}.oracle.com/webservices/rest/
  baseurl_source: declared
  description: Sales order processing and management
  name: Oracle E-Business Suite Order Management API
  slug: oracle-e-business-suite-order-management-api
- baseURL: https://{instance}.oracle.com/webservices/rest/
  baseurl_source: declared
  description: HR organization and position management
  name: Oracle E-Business Suite Organization API
  slug: oracle-e-business-suite-organization-api
- baseURL: https://{instance}.oracle.com/webservices/rest/
  baseurl_source: declared
  description: Outbound EDI document extraction
  name: Oracle E-Business Suite Outbound Transactions API
  slug: oracle-e-business-suite-outbound-transactions-api
- baseURL: https://{instance}.oracle.com/webservices/rest/
  baseurl_source: declared
  description: Payroll processing and run results
  name: Oracle E-Business Suite Payroll API
  slug: oracle-e-business-suite-payroll-api
- baseURL: https://{instance}.oracle.com/webservices/rest/
  baseurl_source: declared
  description: Purchase order, requisition, and supplier management
  name: Oracle E-Business Suite Purchasing API
  slug: oracle-e-business-suite-purchasing-api
- baseURL: https://{instance}.oracle.com/webservices/rest/
  baseurl_source: declared
  description: WADL retrieval and service metadata
  name: Oracle E-Business Suite Service Discovery API
  slug: oracle-e-business-suite-service-discovery-api
- baseURL: https://{instance}.oracle.com/webservices/rest/
  baseurl_source: declared
  description: Invoke deployed REST service methods
  name: Oracle E-Business Suite Service Invocation API
  slug: oracle-e-business-suite-service-invocation-api
- baseURL: https://{instance}.oracle.com/webservices/rest/
  baseurl_source: declared
  description: Shipping delivery management
  name: Oracle E-Business Suite Shipping API
  slug: oracle-e-business-suite-shipping-api
- baseURL: https://{instance}.oracle.com/webservices/rest/
  baseurl_source: declared
  description: Trading partner configuration and management
  name: Oracle E-Business Suite Trading Partners API
  slug: oracle-e-business-suite-trading-partners-api
- baseURL: https://{instance}.oracle.com/webservices/rest/
  baseurl_source: declared
  description: WIP job, operation, and transaction management
  name: Oracle E-Business Suite Work in Process API
  slug: oracle-e-business-suite-work-in-process-api
arazzos:
- description: Read an AP invoice, then branch on whether a matching payment already exists.
  name: Oracle EBS AP Invoice Payment Reconciliation
  slug: oracle-e-business-suite-ap-invoice-payment-reconciliation-workflow
- description: Resolve a bill of material and routing for an assembly, then plan a discrete job from them.
  name: Oracle EBS BOM-to-Job Planning
  slug: oracle-e-business-suite-bom-to-job-planning-workflow
- description: Find an open AR invoice for a customer, then check for a matching cash receipt.
  name: Oracle EBS Customer Receipt Application
  slug: oracle-e-business-suite-customer-receipt-application-workflow
- description: Create a WIP discrete job, issue material to it, then complete the assembly into inventory.
  name: Oracle EBS Discrete Job Execution
  slug: oracle-e-business-suite-discrete-job-execution-workflow
- description: Resolve a trading partner, import an inbound EDI invoice, then confirm it landed.
  name: Oracle EBS EDI Inbound Invoice Processing
  slug: oracle-e-business-suite-edi-inbound-invoice-processing-workflow
- description: Create a purchase order, resolve the supplier trading partner, then extract it as outbound EDI.
  name: Oracle EBS EDI Outbound Purchase Order
  slug: oracle-e-business-suite-edi-outbound-purchase-order-workflow
- description: Resolve organization and position, create an employee, then read the record back.
  name: Oracle EBS Employee Onboarding
  slug: oracle-e-business-suite-employee-onboarding-workflow
- description: Find an employee by number, read the record, then date-tracked update their details.
  name: Oracle EBS Employee Profile Update
  slug: oracle-e-business-suite-employee-profile-update-workflow
- description: Create a General Ledger journal, then read it back from the period to confirm posting status.
  name: Oracle EBS GL Journal Entry and Review
  slug: oracle-e-business-suite-gl-journal-entry-and-review-workflow
- description: Log in, initialize application context, discover a service, invoke a method, then log out.
  name: Oracle EBS ISG Service Invocation
  slug: oracle-e-business-suite-isg-service-invocation-workflow
- description: Resolve an item by number, read its on-hand quantity, and branch on stock availability.
  name: Oracle EBS Item Availability Check
  slug: oracle-e-business-suite-item-availability-check-workflow
- description: Check item availability, create a sales order, confirm it, then raise the AR invoice.
  name: Oracle EBS Order-to-Cash
  slug: oracle-e-business-suite-order-to-cash-workflow
- description: Resolve a payroll definition, read its run results, and confirm an employee's benefit enrollment.
  name: Oracle EBS Payroll Run Review
  slug: oracle-e-business-suite-payroll-run-review-workflow
- description: Resolve a supplier, raise a purchase order, confirm it, then record the matching AP invoice.
  name: Oracle EBS Procure-to-Pay
  slug: oracle-e-business-suite-procure-to-pay-workflow
- description: Find an approved purchase order, read its current state, and amend a line.
  name: Oracle EBS Purchase Order Amendment
  slug: oracle-e-business-suite-purchase-order-amendment-workflow
- description: Find an approved requisition, resolve its supplier, and convert it into a purchase order.
  name: Oracle EBS Requisition-to-Purchase-Order
  slug: oracle-e-business-suite-requisition-to-purchase-order-workflow
- description: Find a customer's booked sales order, then locate its open shipping delivery.
  name: Oracle EBS Shipment Tracking
  slug: oracle-e-business-suite-shipment-tracking-workflow
artifact_total: 438
collections:
- collection_type: postman
  name: Oracle EBS e-Commerce Gateway API
  slug: postman-ecommerce-gateway-api
- collection_type: postman
  name: Oracle EBS Financial Services API
  slug: postman-financial-services-api
- collection_type: postman
  name: Oracle EBS Human Resources API
  slug: postman-human-resources-api
- collection_type: postman
  name: Oracle EBS Integrated SOA Gateway REST API
  slug: postman-isg-rest-api
- collection_type: postman
  name: Oracle EBS Manufacturing API
  slug: postman-manufacturing-api
- collection_type: postman
  name: Oracle EBS Supply Chain Management API
  slug: postman-supply-chain-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Oracle EBS e-Commerce Gateway API
  slug: open-ecommerce-gateway-api
- collection_type: open
  name: Oracle EBS Financial Services API
  slug: open-financial-services-api
- collection_type: open
  name: Oracle EBS Human Resources API
  slug: open-human-resources-api
- collection_type: open
  name: Oracle EBS Integrated SOA Gateway REST API
  slug: open-isg-rest-api
- collection_type: open
  name: Oracle EBS Manufacturing API
  slug: open-manufacturing-api
- collection_type: open
  name: Oracle EBS e-Commerce Gateway Accounts Payable API
  slug: open-oracle-e-business-suite-accounts-payable-api
- collection_type: open
  name: Oracle EBS e-Commerce Gateway Accounts Payable Accounts Receivable API
  slug: open-oracle-e-business-suite-accounts-receivable-api
- collection_type: open
  name: Oracle EBS e-Commerce Gateway Accounts Payable Authentication API
  slug: open-oracle-e-business-suite-authentication-api
- collection_type: open
  name: Oracle EBS e-Commerce Gateway Accounts Payable Benefits API
  slug: open-oracle-e-business-suite-benefits-api
- collection_type: open
  name: Oracle EBS e-Commerce Gateway Accounts Payable Bills of Material API
  slug: open-oracle-e-business-suite-bills-of-material-api
- collection_type: open
  name: Oracle EBS e-Commerce Gateway Accounts Payable Cash Management API
  slug: open-oracle-e-business-suite-cash-management-api
- collection_type: open
  name: Oracle EBS e-Commerce Gateway Accounts Payable Code Conversions API
  slug: open-oracle-e-business-suite-code-conversions-api
- collection_type: open
  name: Oracle EBS e-Commerce Gateway Accounts Payable Employee Management API
  slug: open-oracle-e-business-suite-employee-management-api
- collection_type: open
  name: Oracle EBS e-Commerce Gateway Accounts Payable Fixed Assets API
  slug: open-oracle-e-business-suite-fixed-assets-api
- collection_type: open
  name: Oracle EBS e-Commerce Gateway Accounts Payable General Ledger API
  slug: open-oracle-e-business-suite-general-ledger-api
- collection_type: open
  name: Oracle EBS e-Commerce Gateway Accounts Payable Inbound Transactions API
  slug: open-oracle-e-business-suite-inbound-transactions-api
- collection_type: open
  name: Oracle EBS e-Commerce Gateway Accounts Payable Inventory API
  slug: open-oracle-e-business-suite-inventory-api
- collection_type: open
  name: Oracle EBS e-Commerce Gateway Accounts Payable Order Management API
  slug: open-oracle-e-business-suite-order-management-api
- collection_type: open
  name: Oracle EBS e-Commerce Gateway Accounts Payable Organization API
  slug: open-oracle-e-business-suite-organization-api
- collection_type: open
  name: Oracle EBS e-Commerce Gateway Accounts Payable Outbound Transactions API
  slug: open-oracle-e-business-suite-outbound-transactions-api
- collection_type: open
  name: Oracle EBS e-Commerce Gateway Accounts Payable Payroll API
  slug: open-oracle-e-business-suite-payroll-api
- collection_type: open
  name: Oracle EBS e-Commerce Gateway Accounts Payable Purchasing API
  slug: open-oracle-e-business-suite-purchasing-api
- collection_type: open
  name: Oracle EBS e-Commerce Gateway Accounts Payable Service Discovery API
  slug: open-oracle-e-business-suite-service-discovery-api
- collection_type: open
  name: Oracle EBS e-Commerce Gateway Accounts Payable Service Invocation API
  slug: open-oracle-e-business-suite-service-invocation-api
- collection_type: open
  name: Oracle EBS e-Commerce Gateway Accounts Payable Shipping API
  slug: open-oracle-e-business-suite-shipping-api
- collection_type: open
  name: Oracle EBS e-Commerce Gateway Accounts Payable Trading Partners API
  slug: open-oracle-e-business-suite-trading-partners-api
- collection_type: open
  name: Oracle EBS e-Commerce Gateway Accounts Payable Work in Process API
  slug: open-oracle-e-business-suite-work-in-process-api
- collection_type: open
  name: Oracle EBS Supply Chain Management API
  slug: open-supply-chain-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/oracle-e-business-suite-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oracle-e-business-suite-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oracle-e-business-suite-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oracle-e-business-suite-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/oracle-e-business-suite/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-e-business-suite-ap-invoice-payment-reconciliation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-e-business-suite-bom-to-job-planning-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-e-business-suite-customer-receipt-application-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-e-business-suite-discrete-job-execution-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-e-business-suite-edi-inbound-invoice-processing-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-e-business-suite-edi-outbound-purchase-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-e-business-suite-employee-onboarding-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-e-business-suite-employee-profile-update-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-e-business-suite-gl-journal-entry-and-review-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-e-business-suite-isg-service-invocation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-e-business-suite-item-availability-check-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-e-business-suite-order-to-cash-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-e-business-suite-payroll-run-review-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-e-business-suite-procure-to-pay-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-e-business-suite-purchase-order-amendment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-e-business-suite-requisition-to-purchase-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-e-business-suite-shipment-tracking-workflow.yml
- group: auth
  title: ''
  type: Authentication
  url: https://docs.oracle.com/cd/E26401_01/doc.122/e20927/toc.htm
- group: start
  title: ''
  type: Portal
  url: https://developer.oracle.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/cd/E26401_01/index.htm
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oracle.com/cd/E26401_01/doc.122/e20925/T511175T513043.htm
- group: docs
  title: ''
  type: APIReference
  url: https://docs.oracle.com/cd/E26401_01/doc.122/e22961/toc.htm
- group: operate
  title: ''
  type: Support
  url: https://support.oracle.com
- group: company
  title: ''
  type: Blog
  url: https://blogs.oracle.com/ebstech/
- group: company
  title: ''
  type: Blog
  url: https://blogs.oracle.com/ebs/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.oracle.com/cd/E26401_01/index.htm
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://ocistatus.oraclecloud.com/
- group: start
  title: ''
  type: Signup
  url: https://signup.cloud.oracle.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.oracle.com/applications/ebusiness/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- group: build
  title: ''
  type: SDKs
  url: https://github.com/oracle/oci-java-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/oracle/oci-python-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/oracle/oci-go-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/oracle/oci-dotnet-sdk
- group: build
  title: ''
  type: CLI
  url: https://github.com/oracle/oci-cli
created: '2024-01-01'
description: A collection of APIs for Oracle E-Business Suite (EBS), Oracle's comprehensive suite of integrated, global business applications that supports today's evolving business models across financials, human capital management, supply chain, and manufacturing.
examples:
- key_count: 7
  name: Ecommerce Gateway Code Conversion Example
  slug: ecommerce-gateway-code-conversion-example
- key_count: 5
  name: Ecommerce Gateway Enabled Transaction Example
  slug: ecommerce-gateway-enabled-transaction-example
- key_count: 1
  name: Ecommerce Gateway Error Response Example
  slug: ecommerce-gateway-error-response-example
- key_count: 15
  name: Ecommerce Gateway Inbound Transaction Example
  slug: ecommerce-gateway-inbound-transaction-example
- key_count: 5
  name: Ecommerce Gateway Inbound Transaction Import Example
  slug: ecommerce-gateway-inbound-transaction-import-example
- key_count: 17
  name: Ecommerce Gateway Outbound Transaction Example
  slug: ecommerce-gateway-outbound-transaction-example
- key_count: 5
  name: Ecommerce Gateway Outbound Transaction Extract Example
  slug: ecommerce-gateway-outbound-transaction-extract-example
- key_count: 11
  name: Ecommerce Gateway Trading Partner Example
  slug: ecommerce-gateway-trading-partner-example
- key_count: 11
  name: Financial Services Ap Invoice Create Example
  slug: financial-services-ap-invoice-create-example
- key_count: 25
  name: Financial Services Ap Invoice Example
  slug: financial-services-ap-invoice-example
- key_count: 9
  name: Financial Services Ap Invoice Line Example
  slug: financial-services-ap-invoice-line-example
- key_count: 11
  name: Financial Services Ap Payment Example
  slug: financial-services-ap-payment-example
- key_count: 8
  name: Financial Services Ar Invoice Create Example
  slug: financial-services-ar-invoice-create-example
- key_count: 17
  name: Financial Services Ar Invoice Example
  slug: financial-services-ar-invoice-example
- key_count: 8
  name: Financial Services Ar Invoice Line Example
  slug: financial-services-ar-invoice-line-example
- key_count: 10
  name: Financial Services Ar Receipt Example
  slug: financial-services-ar-receipt-example
- key_count: 10
  name: Financial Services Bank Account Example
  slug: financial-services-bank-account-example
- key_count: 1
  name: Financial Services Error Response Example
  slug: financial-services-error-response-example
- key_count: 14
  name: Financial Services Fixed Asset Example
  slug: financial-services-fixed-asset-example
- key_count: 9
  name: Financial Services Journal Entry Create Example
  slug: financial-services-journal-entry-create-example
- key_count: 16
  name: Financial Services Journal Entry Example
  slug: financial-services-journal-entry-example
- key_count: 7
  name: Financial Services Journal Line Example
  slug: financial-services-journal-line-example
- key_count: 13
  name: Human Resources Address Example
  slug: human-resources-address-example
- key_count: 21
  name: Human Resources Assignment Example
  slug: human-resources-assignment-example
- key_count: 12
  name: Human Resources Benefit Enrollment Example
  slug: human-resources-benefit-enrollment-example
- key_count: 19
  name: Human Resources Employee Create Example
  slug: human-resources-employee-create-example
- key_count: 23
  name: Human Resources Employee Example
  slug: human-resources-employee-example
- key_count: 9
  name: Human Resources Employee Update Example
  slug: human-resources-employee-update-example
- key_count: 1
  name: Human Resources Error Response Example
  slug: human-resources-error-response-example
- key_count: 8
  name: Human Resources Organization Example
  slug: human-resources-organization-example
- key_count: 8
  name: Human Resources Payroll Example
  slug: human-resources-payroll-example
- key_count: 8
  name: Human Resources Payroll Run Example
  slug: human-resources-payroll-run-example
- key_count: 5
  name: Human Resources Phone Example
  slug: human-resources-phone-example
- key_count: 10
  name: Human Resources Position Example
  slug: human-resources-position-example
- key_count: 1
  name: Isg Rest Error Response Example
  slug: isg-rest-error-response-example
- key_count: 1
  name: Isg Rest Initialize Request Example
  slug: isg-rest-initialize-request-example
- key_count: 1
  name: Isg Rest Initialize Response Example
  slug: isg-rest-initialize-response-example
- key_count: 1
  name: Isg Rest Login Response Example
  slug: isg-rest-login-response-example
- key_count: 1
  name: Isg Rest Logout Response Example
  slug: isg-rest-logout-response-example
- key_count: 2
  name: Isg Rest Service Method Request Example
  slug: isg-rest-service-method-request-example
- key_count: 1
  name: Isg Rest Service Method Response Example
  slug: isg-rest-service-method-response-example
- key_count: 11
  name: Manufacturing Bill Of Material Example
  slug: manufacturing-bill-of-material-example
- key_count: 12
  name: Manufacturing Bom Component Example
  slug: manufacturing-bom-component-example
- key_count: 7
  name: Manufacturing Completion Transaction Example
  slug: manufacturing-completion-transaction-example
- key_count: 13
  name: Manufacturing Discrete Job Create Example
  slug: manufacturing-discrete-job-create-example
- key_count: 23
  name: Manufacturing Discrete Job Example
  slug: manufacturing-discrete-job-example
- key_count: 1
  name: Manufacturing Error Response Example
  slug: manufacturing-error-response-example
- key_count: 10
  name: Manufacturing Material Transaction Example
  slug: manufacturing-material-transaction-example
- key_count: 7
  name: Manufacturing Operation Resource Example
  slug: manufacturing-operation-resource-example
- key_count: 9
  name: Manufacturing Routing Example
  slug: manufacturing-routing-example
- key_count: 11
  name: Manufacturing Routing Operation Example
  slug: manufacturing-routing-operation-example
- key_count: 15
  name: Manufacturing Wip Operation Example
  slug: manufacturing-wip-operation-example
- key_count: 6
  name: Oracle E Business Suite Completeassembly Example
  slug: oracle-e-business-suite-completeassembly-example
- key_count: 6
  name: Oracle E Business Suite Createapinvoice Example
  slug: oracle-e-business-suite-createapinvoice-example
- key_count: 6
  name: Oracle E Business Suite Createarinvoice Example
  slug: oracle-e-business-suite-createarinvoice-example
- key_count: 6
  name: Oracle E Business Suite Creatediscretejob Example
  slug: oracle-e-business-suite-creatediscretejob-example
- key_count: 6
  name: Oracle E Business Suite Createemployee Example
  slug: oracle-e-business-suite-createemployee-example
- key_count: 6
  name: Oracle E Business Suite Createjournal Example
  slug: oracle-e-business-suite-createjournal-example
- key_count: 6
  name: Oracle E Business Suite Createpurchaseorder Example
  slug: oracle-e-business-suite-createpurchaseorder-example
- key_count: 6
  name: Oracle E Business Suite Createsalesorder Example
  slug: oracle-e-business-suite-createsalesorder-example
- key_count: 6
  name: Oracle E Business Suite Extractoutboundtransaction Example
  slug: oracle-e-business-suite-extractoutboundtransaction-example
- key_count: 6
  name: Oracle E Business Suite Getapinvoicebyid Example
  slug: oracle-e-business-suite-getapinvoicebyid-example
- key_count: 6
  name: Oracle E Business Suite Getapinvoices Example
  slug: oracle-e-business-suite-getapinvoices-example
- key_count: 6
  name: Oracle E Business Suite Getarinvoices Example
  slug: oracle-e-business-suite-getarinvoices-example
- key_count: 6
  name: Oracle E Business Suite Getassets Example
  slug: oracle-e-business-suite-getassets-example
- key_count: 6
  name: Oracle E Business Suite Getassignments Example
  slug: oracle-e-business-suite-getassignments-example
- key_count: 6
  name: Oracle E Business Suite Getbankaccounts Example
  slug: oracle-e-business-suite-getbankaccounts-example
- key_count: 6
  name: Oracle E Business Suite Getbenefitenrollments Example
  slug: oracle-e-business-suite-getbenefitenrollments-example
- key_count: 6
  name: Oracle E Business Suite Getbillofmaterialbyid Example
  slug: oracle-e-business-suite-getbillofmaterialbyid-example
- key_count: 6
  name: Oracle E Business Suite Getbillsofmaterial Example
  slug: oracle-e-business-suite-getbillsofmaterial-example
- key_count: 6
  name: Oracle E Business Suite Getcodeconversions Example
  slug: oracle-e-business-suite-getcodeconversions-example
- key_count: 6
  name: Oracle E Business Suite Getdeliveries Example
  slug: oracle-e-business-suite-getdeliveries-example
- key_count: 6
  name: Oracle E Business Suite Getdiscretejobbyid Example
  slug: oracle-e-business-suite-getdiscretejobbyid-example
- key_count: 6
  name: Oracle E Business Suite Getdiscretejobs Example
  slug: oracle-e-business-suite-getdiscretejobs-example
- key_count: 6
  name: Oracle E Business Suite Getemployeebyid Example
  slug: oracle-e-business-suite-getemployeebyid-example
- key_count: 6
  name: Oracle E Business Suite Getemployees Example
  slug: oracle-e-business-suite-getemployees-example
- key_count: 6
  name: Oracle E Business Suite Getinboundtransactions Example
  slug: oracle-e-business-suite-getinboundtransactions-example
- key_count: 6
  name: Oracle E Business Suite Getinventoryitems Example
  slug: oracle-e-business-suite-getinventoryitems-example
- key_count: 6
  name: Oracle E Business Suite Getjournals Example
  slug: oracle-e-business-suite-getjournals-example
- key_count: 6
  name: Oracle E Business Suite Getonhandquantities Example
  slug: oracle-e-business-suite-getonhandquantities-example
- key_count: 6
  name: Oracle E Business Suite Getorganizations Example
  slug: oracle-e-business-suite-getorganizations-example
- key_count: 6
  name: Oracle E Business Suite Getoutboundtransactions Example
  slug: oracle-e-business-suite-getoutboundtransactions-example
- key_count: 6
  name: Oracle E Business Suite Getpayments Example
  slug: oracle-e-business-suite-getpayments-example
- key_count: 6
  name: Oracle E Business Suite Getpayrollruns Example
  slug: oracle-e-business-suite-getpayrollruns-example
- key_count: 6
  name: Oracle E Business Suite Getpayrolls Example
  slug: oracle-e-business-suite-getpayrolls-example
- key_count: 6
  name: Oracle E Business Suite Getpositions Example
  slug: oracle-e-business-suite-getpositions-example
- key_count: 6
  name: Oracle E Business Suite Getpurchaseorderbyid Example
  slug: oracle-e-business-suite-getpurchaseorderbyid-example
- key_count: 6
  name: Oracle E Business Suite Getpurchaseorders Example
  slug: oracle-e-business-suite-getpurchaseorders-example
- key_count: 6
  name: Oracle E Business Suite Getreceipts Example
  slug: oracle-e-business-suite-getreceipts-example
- key_count: 6
  name: Oracle E Business Suite Getrequisitions Example
  slug: oracle-e-business-suite-getrequisitions-example
- key_count: 6
  name: Oracle E Business Suite Getroutings Example
  slug: oracle-e-business-suite-getroutings-example
- key_count: 6
  name: Oracle E Business Suite Getsalesorders Example
  slug: oracle-e-business-suite-getsalesorders-example
- key_count: 6
  name: Oracle E Business Suite Getservicewadl Example
  slug: oracle-e-business-suite-getservicewadl-example
- key_count: 6
  name: Oracle E Business Suite Getsuppliers Example
  slug: oracle-e-business-suite-getsuppliers-example
- key_count: 6
  name: Oracle E Business Suite Gettradingpartnerbyid Example
  slug: oracle-e-business-suite-gettradingpartnerbyid-example
- key_count: 6
  name: Oracle E Business Suite Gettradingpartners Example
  slug: oracle-e-business-suite-gettradingpartners-example
- key_count: 6
  name: Oracle E Business Suite Getwipoperations Example
  slug: oracle-e-business-suite-getwipoperations-example
- key_count: 6
  name: Oracle E Business Suite Importinboundtransaction Example
  slug: oracle-e-business-suite-importinboundtransaction-example
- key_count: 6
  name: Oracle E Business Suite Initialize Example
  slug: oracle-e-business-suite-initialize-example
- key_count: 6
  name: Oracle E Business Suite Invokerestmethod Example
  slug: oracle-e-business-suite-invokerestmethod-example
- key_count: 6
  name: Oracle E Business Suite Issuematerial Example
  slug: oracle-e-business-suite-issuematerial-example
- key_count: 6
  name: Oracle E Business Suite Login Example
  slug: oracle-e-business-suite-login-example
- key_count: 6
  name: Oracle E Business Suite Logout Example
  slug: oracle-e-business-suite-logout-example
- key_count: 6
  name: Oracle E Business Suite Updateemployee Example
  slug: oracle-e-business-suite-updateemployee-example
- key_count: 6
  name: Oracle E Business Suite Updatepurchaseorder Example
  slug: oracle-e-business-suite-updatepurchaseorder-example
- key_count: 17
  name: Supply Chain Delivery Example
  slug: supply-chain-delivery-example
- key_count: 1
  name: Supply Chain Error Response Example
  slug: supply-chain-error-response-example
- key_count: 18
  name: Supply Chain Inventory Item Example
  slug: supply-chain-inventory-item-example
- key_count: 9
  name: Supply Chain Onhand Quantity Example
  slug: supply-chain-onhand-quantity-example
- key_count: 10
  name: Supply Chain Purchase Order Create Example
  slug: supply-chain-purchase-order-create-example
- key_count: 21
  name: Supply Chain Purchase Order Example
  slug: supply-chain-purchase-order-example
- key_count: 14
  name: Supply Chain Purchase Order Line Example
  slug: supply-chain-purchase-order-line-example
- key_count: 10
  name: Supply Chain Purchase Order Shipment Example
  slug: supply-chain-purchase-order-shipment-example
- key_count: 2
  name: Supply Chain Purchase Order Update Example
  slug: supply-chain-purchase-order-update-example
- key_count: 10
  name: Supply Chain Requisition Example
  slug: supply-chain-requisition-example
- key_count: 10
  name: Supply Chain Requisition Line Example
  slug: supply-chain-requisition-line-example
- key_count: 8
  name: Supply Chain Sales Order Create Example
  slug: supply-chain-sales-order-create-example
- key_count: 18
  name: Supply Chain Sales Order Example
  slug: supply-chain-sales-order-example
- key_count: 13
  name: Supply Chain Sales Order Line Example
  slug: supply-chain-sales-order-line-example
- key_count: 15
  name: Supply Chain Supplier Example
  slug: supply-chain-supplier-example
- key_count: 11
  name: Supply Chain Supplier Site Example
  slug: supply-chain-supplier-site-example
features:
- Financial management (GL, AP, AR, FA, Cash Management)
- Supply chain management (Purchasing, Inventory, Order Management)
- Human capital management (HR, Payroll, Benefits)
- Manufacturing (Discrete, Process, WIP, BOM)
- EDI transaction processing via e-Commerce Gateway
- RESTful API access through Integrated SOA Gateway
- PL/SQL API framework for programmatic data access
- Multi-org and multi-currency support
finops:
- name: Oracle E Business Suite Finops
  service_category: ERP / Business Applications
  slug: oracle-e-business-suite-finops
image: /assets/icons/oracle-e-business-suite.png
integrations:
- Oracle SOA Suite for service orchestration
- Oracle Integration Cloud for hybrid integration
- EDI translators for ASC X12 and EDIFACT standards
- Oracle BI Publisher for reporting
- Oracle Identity Management for SSO
- Third-party middleware via REST and SOAP APIs
json_schemas:
- name: Oracle EBS Customer
  property_count: 22
  slug: customer
- name: CodeConversion
  property_count: 7
  slug: ecommerce-gateway-code-conversion
- name: EnabledTransaction
  property_count: 5
  slug: ecommerce-gateway-enabled-transaction
- name: ErrorResponse
  property_count: 1
  slug: ecommerce-gateway-error-response
- name: InboundTransactionImport
  property_count: 5
  slug: ecommerce-gateway-inbound-transaction-import
- name: InboundTransaction
  property_count: 15
  slug: ecommerce-gateway-inbound-transaction
- name: OutboundTransactionExtract
  property_count: 5
  slug: ecommerce-gateway-outbound-transaction-extract
- name: OutboundTransaction
  property_count: 17
  slug: ecommerce-gateway-outbound-transaction
- name: TradingPartner
  property_count: 11
  slug: ecommerce-gateway-trading-partner
- name: Oracle EBS Employee
  property_count: 36
  slug: employee
- name: ApInvoiceCreate
  property_count: 11
  slug: financial-services-ap-invoice-create
- name: ApInvoiceLine
  property_count: 9
  slug: financial-services-ap-invoice-line
- name: ApInvoice
  property_count: 25
  slug: financial-services-ap-invoice
- name: ApPayment
  property_count: 11
  slug: financial-services-ap-payment
- name: ArInvoiceCreate
  property_count: 8
  slug: financial-services-ar-invoice-create
- name: ArInvoiceLine
  property_count: 8
  slug: financial-services-ar-invoice-line
- name: ArInvoice
  property_count: 17
  slug: financial-services-ar-invoice
- name: ArReceipt
  property_count: 10
  slug: financial-services-ar-receipt
- name: BankAccount
  property_count: 10
  slug: financial-services-bank-account
- name: ErrorResponse
  property_count: 1
  slug: financial-services-error-response
- name: FixedAsset
  property_count: 14
  slug: financial-services-fixed-asset
- name: JournalEntryCreate
  property_count: 9
  slug: financial-services-journal-entry-create
- name: JournalEntry
  property_count: 16
  slug: financial-services-journal-entry
- name: JournalLine
  property_count: 7
  slug: financial-services-journal-line
- name: Address
  property_count: 13
  slug: human-resources-address
- name: Assignment
  property_count: 21
  slug: human-resources-assignment
- name: BenefitEnrollment
  property_count: 12
  slug: human-resources-benefit-enrollment
- name: EmployeeCreate
  property_count: 19
  slug: human-resources-employee-create
- name: Employee
  property_count: 23
  slug: human-resources-employee
- name: EmployeeUpdate
  property_count: 9
  slug: human-resources-employee-update
- name: ErrorResponse
  property_count: 1
  slug: human-resources-error-response
- name: Organization
  property_count: 8
  slug: human-resources-organization
- name: PayrollRun
  property_count: 8
  slug: human-resources-payroll-run
- name: Payroll
  property_count: 8
  slug: human-resources-payroll
- name: Phone
  property_count: 5
  slug: human-resources-phone
- name: Position
  property_count: 10
  slug: human-resources-position
- name: Oracle EBS Invoice
  property_count: 44
  slug: invoice
- name: ErrorResponse
  property_count: 1
  slug: isg-rest-error-response
- name: InitializeRequest
  property_count: 1
  slug: isg-rest-initialize-request
- name: InitializeResponse
  property_count: 1
  slug: isg-rest-initialize-response
- name: LoginResponse
  property_count: 1
  slug: isg-rest-login-response
- name: LogoutResponse
  property_count: 1
  slug: isg-rest-logout-response
- name: ServiceMethodRequest
  property_count: 2
  slug: isg-rest-service-method-request
- name: ServiceMethodResponse
  property_count: 1
  slug: isg-rest-service-method-response
- name: BillOfMaterial
  property_count: 11
  slug: manufacturing-bill-of-material
- name: BomComponent
  property_count: 12
  slug: manufacturing-bom-component
- name: CompletionTransaction
  property_count: 7
  slug: manufacturing-completion-transaction
- name: DiscreteJobCreate
  property_count: 13
  slug: manufacturing-discrete-job-create
- name: DiscreteJob
  property_count: 23
  slug: manufacturing-discrete-job
- name: ErrorResponse
  property_count: 1
  slug: manufacturing-error-response
- name: MaterialTransaction
  property_count: 10
  slug: manufacturing-material-transaction
- name: OperationResource
  property_count: 7
  slug: manufacturing-operation-resource
- name: RoutingOperation
  property_count: 11
  slug: manufacturing-routing-operation
- name: Routing
  property_count: 9
  slug: manufacturing-routing
- name: WipOperation
  property_count: 15
  slug: manufacturing-wip-operation
- name: Address
  property_count: 13
  slug: oracle-e-business-suite-address
- name: ApInvoice
  property_count: 25
  slug: oracle-e-business-suite-apinvoice
- name: ApInvoiceCreate
  property_count: 11
  slug: oracle-e-business-suite-apinvoicecreate
- name: ApInvoiceLine
  property_count: 9
  slug: oracle-e-business-suite-apinvoiceline
- name: ApPayment
  property_count: 11
  slug: oracle-e-business-suite-appayment
- name: ArInvoice
  property_count: 17
  slug: oracle-e-business-suite-arinvoice
- name: ArInvoiceCreate
  property_count: 8
  slug: oracle-e-business-suite-arinvoicecreate
- name: ArInvoiceLine
  property_count: 8
  slug: oracle-e-business-suite-arinvoiceline
- name: ArReceipt
  property_count: 10
  slug: oracle-e-business-suite-arreceipt
- name: Assignment
  property_count: 21
  slug: oracle-e-business-suite-assignment
- name: BankAccount
  property_count: 10
  slug: oracle-e-business-suite-bankaccount
- name: BenefitEnrollment
  property_count: 12
  slug: oracle-e-business-suite-benefitenrollment
- name: BillOfMaterial
  property_count: 11
  slug: oracle-e-business-suite-billofmaterial
- name: BomComponent
  property_count: 12
  slug: oracle-e-business-suite-bomcomponent
- name: CodeConversion
  property_count: 7
  slug: oracle-e-business-suite-codeconversion
- name: CompletionTransaction
  property_count: 7
  slug: oracle-e-business-suite-completiontransaction
- name: Delivery
  property_count: 17
  slug: oracle-e-business-suite-delivery
- name: DiscreteJob
  property_count: 23
  slug: oracle-e-business-suite-discretejob
- name: DiscreteJobCreate
  property_count: 13
  slug: oracle-e-business-suite-discretejobcreate
- name: Employee
  property_count: 24
  slug: oracle-e-business-suite-employee
- name: EmployeeCreate
  property_count: 19
  slug: oracle-e-business-suite-employeecreate
- name: EmployeeUpdate
  property_count: 9
  slug: oracle-e-business-suite-employeeupdate
- name: EnabledTransaction
  property_count: 5
  slug: oracle-e-business-suite-enabledtransaction
- name: ErrorResponse
  property_count: 1
  slug: oracle-e-business-suite-errorresponse
- name: FixedAsset
  property_count: 14
  slug: oracle-e-business-suite-fixedasset
- name: InboundTransaction
  property_count: 15
  slug: oracle-e-business-suite-inboundtransaction
- name: InboundTransactionImport
  property_count: 5
  slug: oracle-e-business-suite-inboundtransactionimport
- name: InitializeRequest
  property_count: 1
  slug: oracle-e-business-suite-initializerequest
- name: InitializeResponse
  property_count: 1
  slug: oracle-e-business-suite-initializeresponse
- name: InventoryItem
  property_count: 18
  slug: oracle-e-business-suite-inventoryitem
- name: JournalEntry
  property_count: 16
  slug: oracle-e-business-suite-journalentry
- name: JournalEntryCreate
  property_count: 9
  slug: oracle-e-business-suite-journalentrycreate
- name: JournalLine
  property_count: 7
  slug: oracle-e-business-suite-journalline
- name: LoginResponse
  property_count: 1
  slug: oracle-e-business-suite-loginresponse
- name: LogoutResponse
  property_count: 1
  slug: oracle-e-business-suite-logoutresponse
- name: MaterialTransaction
  property_count: 10
  slug: oracle-e-business-suite-materialtransaction
- name: OnhandQuantity
  property_count: 9
  slug: oracle-e-business-suite-onhandquantity
- name: OperationResource
  property_count: 7
  slug: oracle-e-business-suite-operationresource
- name: Organization
  property_count: 8
  slug: oracle-e-business-suite-organization
- name: OutboundTransaction
  property_count: 17
  slug: oracle-e-business-suite-outboundtransaction
- name: OutboundTransactionExtract
  property_count: 5
  slug: oracle-e-business-suite-outboundtransactionextract
- name: Payroll
  property_count: 8
  slug: oracle-e-business-suite-payroll
- name: PayrollRun
  property_count: 8
  slug: oracle-e-business-suite-payrollrun
- name: Phone
  property_count: 5
  slug: oracle-e-business-suite-phone
- name: Position
  property_count: 10
  slug: oracle-e-business-suite-position
- name: PurchaseOrder
  property_count: 21
  slug: oracle-e-business-suite-purchaseorder
- name: PurchaseOrderCreate
  property_count: 10
  slug: oracle-e-business-suite-purchaseordercreate
- name: PurchaseOrderLine
  property_count: 14
  slug: oracle-e-business-suite-purchaseorderline
- name: PurchaseOrderShipment
  property_count: 10
  slug: oracle-e-business-suite-purchaseordershipment
- name: PurchaseOrderUpdate
  property_count: 2
  slug: oracle-e-business-suite-purchaseorderupdate
- name: Requisition
  property_count: 10
  slug: oracle-e-business-suite-requisition
- name: RequisitionLine
  property_count: 10
  slug: oracle-e-business-suite-requisitionline
- name: Routing
  property_count: 9
  slug: oracle-e-business-suite-routing
- name: RoutingOperation
  property_count: 11
  slug: oracle-e-business-suite-routingoperation
- name: SalesOrder
  property_count: 18
  slug: oracle-e-business-suite-salesorder
- name: SalesOrderCreate
  property_count: 8
  slug: oracle-e-business-suite-salesordercreate
- name: SalesOrderLine
  property_count: 13
  slug: oracle-e-business-suite-salesorderline
- name: ServiceMethodRequest
  property_count: 2
  slug: oracle-e-business-suite-servicemethodrequest
- name: ServiceMethodResponse
  property_count: 1
  slug: oracle-e-business-suite-servicemethodresponse
- name: Supplier
  property_count: 15
  slug: oracle-e-business-suite-supplier
- name: SupplierSite
  property_count: 11
  slug: oracle-e-business-suite-suppliersite
- name: TradingPartner
  property_count: 11
  slug: oracle-e-business-suite-tradingpartner
- name: WipOperation
  property_count: 15
  slug: oracle-e-business-suite-wipoperation
- name: Oracle EBS Purchase Order
  property_count: 33
  slug: purchase-order
- name: Oracle EBS Supplier
  property_count: 36
  slug: supplier
- name: Delivery
  property_count: 17
  slug: supply-chain-delivery
- name: ErrorResponse
  property_count: 1
  slug: supply-chain-error-response
- name: InventoryItem
  property_count: 18
  slug: supply-chain-inventory-item
- name: OnhandQuantity
  property_count: 9
  slug: supply-chain-onhand-quantity
- name: PurchaseOrderCreate
  property_count: 10
  slug: supply-chain-purchase-order-create
- name: PurchaseOrderLine
  property_count: 14
  slug: supply-chain-purchase-order-line
- name: PurchaseOrder
  property_count: 21
  slug: supply-chain-purchase-order
- name: PurchaseOrderShipment
  property_count: 10
  slug: supply-chain-purchase-order-shipment
- name: PurchaseOrderUpdate
  property_count: 2
  slug: supply-chain-purchase-order-update
- name: RequisitionLine
  property_count: 10
  slug: supply-chain-requisition-line
- name: Requisition
  property_count: 10
  slug: supply-chain-requisition
- name: SalesOrderCreate
  property_count: 8
  slug: supply-chain-sales-order-create
- name: SalesOrderLine
  property_count: 13
  slug: supply-chain-sales-order-line
- name: SalesOrder
  property_count: 18
  slug: supply-chain-sales-order
- name: Supplier
  property_count: 15
  slug: supply-chain-supplier
- name: SupplierSite
  property_count: 11
  slug: supply-chain-supplier-site
json_structures:
- name: Ecommerce Gateway Code Conversion Structure
  property_count: 7
  slug: ecommerce-gateway-code-conversion-structure
- name: Ecommerce Gateway Enabled Transaction Structure
  property_count: 5
  slug: ecommerce-gateway-enabled-transaction-structure
- name: Ecommerce Gateway Error Response Structure
  property_count: 1
  slug: ecommerce-gateway-error-response-structure
- name: Ecommerce Gateway Inbound Transaction Import Structure
  property_count: 5
  slug: ecommerce-gateway-inbound-transaction-import-structure
- name: Ecommerce Gateway Inbound Transaction Structure
  property_count: 15
  slug: ecommerce-gateway-inbound-transaction-structure
- name: Ecommerce Gateway Outbound Transaction Extract Structure
  property_count: 5
  slug: ecommerce-gateway-outbound-transaction-extract-structure
- name: Ecommerce Gateway Outbound Transaction Structure
  property_count: 17
  slug: ecommerce-gateway-outbound-transaction-structure
- name: Ecommerce Gateway Trading Partner Structure
  property_count: 11
  slug: ecommerce-gateway-trading-partner-structure
- name: Financial Services Ap Invoice Create Structure
  property_count: 11
  slug: financial-services-ap-invoice-create-structure
- name: Financial Services Ap Invoice Line Structure
  property_count: 9
  slug: financial-services-ap-invoice-line-structure
- name: Financial Services Ap Invoice Structure
  property_count: 25
  slug: financial-services-ap-invoice-structure
- name: Financial Services Ap Payment Structure
  property_count: 11
  slug: financial-services-ap-payment-structure
- name: Financial Services Ar Invoice Create Structure
  property_count: 8
  slug: financial-services-ar-invoice-create-structure
- name: Financial Services Ar Invoice Line Structure
  property_count: 8
  slug: financial-services-ar-invoice-line-structure
- name: Financial Services Ar Invoice Structure
  property_count: 17
  slug: financial-services-ar-invoice-structure
- name: Financial Services Ar Receipt Structure
  property_count: 10
  slug: financial-services-ar-receipt-structure
- name: Financial Services Bank Account Structure
  property_count: 10
  slug: financial-services-bank-account-structure
- name: Financial Services Error Response Structure
  property_count: 1
  slug: financial-services-error-response-structure
- name: Financial Services Fixed Asset Structure
  property_count: 14
  slug: financial-services-fixed-asset-structure
- name: Financial Services Journal Entry Create Structure
  property_count: 9
  slug: financial-services-journal-entry-create-structure
- name: Financial Services Journal Entry Structure
  property_count: 16
  slug: financial-services-journal-entry-structure
- name: Financial Services Journal Line Structure
  property_count: 7
  slug: financial-services-journal-line-structure
- name: Human Resources Address Structure
  property_count: 13
  slug: human-resources-address-structure
- name: Human Resources Assignment Structure
  property_count: 21
  slug: human-resources-assignment-structure
- name: Human Resources Benefit Enrollment Structure
  property_count: 12
  slug: human-resources-benefit-enrollment-structure
- name: Human Resources Employee Create Structure
  property_count: 19
  slug: human-resources-employee-create-structure
- name: Human Resources Employee Structure
  property_count: 23
  slug: human-resources-employee-structure
- name: Human Resources Employee Update Structure
  property_count: 9
  slug: human-resources-employee-update-structure
- name: Human Resources Error Response Structure
  property_count: 1
  slug: human-resources-error-response-structure
- name: Human Resources Organization Structure
  property_count: 8
  slug: human-resources-organization-structure
- name: Human Resources Payroll Run Structure
  property_count: 8
  slug: human-resources-payroll-run-structure
- name: Human Resources Payroll Structure
  property_count: 8
  slug: human-resources-payroll-structure
- name: Human Resources Phone Structure
  property_count: 5
  slug: human-resources-phone-structure
- name: Human Resources Position Structure
  property_count: 10
  slug: human-resources-position-structure
- name: Isg Rest Error Response Structure
  property_count: 1
  slug: isg-rest-error-response-structure
- name: Isg Rest Initialize Request Structure
  property_count: 1
  slug: isg-rest-initialize-request-structure
- name: Isg Rest Initialize Response Structure
  property_count: 1
  slug: isg-rest-initialize-response-structure
- name: Isg Rest Login Response Structure
  property_count: 1
  slug: isg-rest-login-response-structure
- name: Isg Rest Logout Response Structure
  property_count: 1
  slug: isg-rest-logout-response-structure
- name: Isg Rest Service Method Request Structure
  property_count: 2
  slug: isg-rest-service-method-request-structure
- name: Isg Rest Service Method Response Structure
  property_count: 1
  slug: isg-rest-service-method-response-structure
- name: Manufacturing Bill Of Material Structure
  property_count: 11
  slug: manufacturing-bill-of-material-structure
- name: Manufacturing Bom Component Structure
  property_count: 12
  slug: manufacturing-bom-component-structure
- name: Manufacturing Completion Transaction Structure
  property_count: 7
  slug: manufacturing-completion-transaction-structure
- name: Manufacturing Discrete Job Create Structure
  property_count: 13
  slug: manufacturing-discrete-job-create-structure
- name: Manufacturing Discrete Job Structure
  property_count: 23
  slug: manufacturing-discrete-job-structure
- name: Manufacturing Error Response Structure
  property_count: 1
  slug: manufacturing-error-response-structure
- name: Manufacturing Material Transaction Structure
  property_count: 10
  slug: manufacturing-material-transaction-structure
- name: Manufacturing Operation Resource Structure
  property_count: 7
  slug: manufacturing-operation-resource-structure
- name: Manufacturing Routing Operation Structure
  property_count: 11
  slug: manufacturing-routing-operation-structure
- name: Manufacturing Routing Structure
  property_count: 9
  slug: manufacturing-routing-structure
- name: Manufacturing Wip Operation Structure
  property_count: 15
  slug: manufacturing-wip-operation-structure
- name: Oracle E Business Suite Structure
  property_count: 0
  slug: oracle-e-business-suite-structure
- name: Supply Chain Delivery Structure
  property_count: 17
  slug: supply-chain-delivery-structure
- name: Supply Chain Error Response Structure
  property_count: 1
  slug: supply-chain-error-response-structure
- name: Supply Chain Inventory Item Structure
  property_count: 18
  slug: supply-chain-inventory-item-structure
- name: Supply Chain Onhand Quantity Structure
  property_count: 9
  slug: supply-chain-onhand-quantity-structure
- name: Supply Chain Purchase Order Create Structure
  property_count: 10
  slug: supply-chain-purchase-order-create-structure
- name: Supply Chain Purchase Order Line Structure
  property_count: 14
  slug: supply-chain-purchase-order-line-structure
- name: Supply Chain Purchase Order Shipment Structure
  property_count: 10
  slug: supply-chain-purchase-order-shipment-structure
- name: Supply Chain Purchase Order Structure
  property_count: 21
  slug: supply-chain-purchase-order-structure
- name: Supply Chain Purchase Order Update Structure
  property_count: 2
  slug: supply-chain-purchase-order-update-structure
- name: Supply Chain Requisition Line Structure
  property_count: 10
  slug: supply-chain-requisition-line-structure
- name: Supply Chain Requisition Structure
  property_count: 10
  slug: supply-chain-requisition-structure
- name: Supply Chain Sales Order Create Structure
  property_count: 8
  slug: supply-chain-sales-order-create-structure
- name: Supply Chain Sales Order Line Structure
  property_count: 13
  slug: supply-chain-sales-order-line-structure
- name: Supply Chain Sales Order Structure
  property_count: 18
  slug: supply-chain-sales-order-structure
- name: Supply Chain Supplier Site Structure
  property_count: 11
  slug: supply-chain-supplier-site-structure
- name: Supply Chain Supplier Structure
  property_count: 15
  slug: supply-chain-supplier-structure
jsonld:
- class_count: 0
  name: context Context
  property_count: 12
  slug: context
- class_count: 0
  name: Ecommerce Gateway Context
  property_count: 0
  slug: ecommerce-gateway-context
- class_count: 0
  name: Financial Services Context
  property_count: 0
  slug: financial-services-context
- class_count: 0
  name: Human Resources Context
  property_count: 0
  slug: human-resources-context
- class_count: 0
  name: Isg Rest Context
  property_count: 0
  slug: isg-rest-context
- class_count: 0
  name: Manufacturing Context
  property_count: 0
  slug: manufacturing-context
- class_count: 0
  name: Supply Chain Context
  property_count: 0
  slug: supply-chain-context
layout: provider
modified: '2026-05-19'
name: Oracle E-Business Suite
nav: Providers
network: true
overview: 'Oracle E-Business Suite publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Accounts Payable API, Accounts Receivable API, Authentication API, and 19 more. Tagged areas include Business Applications, E-Business Suite, Enterprise, ERP, and Oracle.


  The Oracle E-Business Suite catalog on APIs.io includes 7 JSON-LD contexts and 2 Spectral governance rulesets.


  Oracle E-Business Suite''s developer surface includes authentication, developer portal, documentation, getting-started guide, API reference, support, engineering blog, and 35 more developer resources.'
plans:
- name: Oracle E Business Suite Plans Pricing
  plan_count: 4
  slug: oracle-e-business-suite-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Oracle E Business Suite Rate Limits
  slug: oracle-e-business-suite-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Oracle E-Business Suite API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: oracle-e-business-suite-jsonschema-spectral-rules
- effective_rule_count: 59
  extends:
  - spectral:oas
  name: Oracle E-Business Suite API Rules
  rule_count: 18
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 9
  slug: oracle-e-business-suite-spectral-rules
score:
  band: strong
  composite: 61.4
  coverage:
    artifact_dirs: 19
    catalog_gap: 46.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 13.6
    contract_quality: 72.7
    developer_ergonomics: 85.7
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 42.1
  previous_composite: 61.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oracle-e-business-suite/refs/heads/main/screenshots/oracle-e-business-suite-2026-06-20T191127.png
security:
- kind: authentication
  name: Oracle E Business Suite Authentication
  slug: oracle-e-business-suite-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Oracle E Business Suite Domain Security
  slug: oracle-e-business-suite-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oracle-e-business-suite
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
use_cases:
- Automate financial close and journal posting
- Integrate procurement and purchase order workflows
- Manage employee lifecycle and payroll processing
- Track manufacturing work orders and material usage
- Exchange EDI documents with trading partners
- Build custom integrations via REST and SOAP services
- Synchronize EBS data with external systems
website: https://developer.oracle.com/
---

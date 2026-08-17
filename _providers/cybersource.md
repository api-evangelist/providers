---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 120
  human_in_the_loop: 0
  name: Cybersource Agentic Access
  operation_count: 183
  slug: cybersource-agentic-access
  summary_line: 183 operations · 120 acting
api_count: 84
apis:
- description: Securely tokenizes, stores, and manages customer payment credentials and card data. Supports instrument identifiers, payment instruments, customer profiles, network tokens, and cryptograms. Reduces PC
  name: CyberSource Token Management Service (TMS) API
  slug: cybersource-token-management-service-tms-api
- description: Provides AI-powered fraud detection and risk management using machine learning models trained on Visa and CyberSource transaction data. Offers real-time fraud scoring, custom rules, device fingerprint
  name: CyberSource Decision Manager API
  slug: cybersource-decision-manager-api
- description: Enables subscription management and automated recurring payments without storing sensitive card data. Create and manage subscription plans, customer billing agreements, and on-demand charges. Supports
  name: CyberSource Recurring Billing API
  slug: cybersource-recurring-billing-api
- description: 'Delivers funds directly to recipients via eligible Visa and Mastercard debit accounts using Account Funding Transactions (AFT) and Original Credit Transactions (OCT). Supports use cases including gig '
  name: CyberSource Payouts API
  slug: cybersource-payouts-api
- description: PCI DSS-compliant hosted payment field solution that replaces sensitive card input fields with secure CyberSource-hosted iFrame components. Encrypts card data on the customer's device before transmiss
  name: CyberSource Flex Microform API
  slug: cybersource-flex-microform-api
- description: Pre-built, customizable payment acceptance widget supporting multiple payment methods from a single integration. Supports credit/debit cards, digital wallets (Apple Pay, Google Pay, Click to Pay), buy
  name: CyberSource Unified Checkout API
  slug: cybersource-unified-checkout-api
- description: Implements 3D Secure 2.x authentication to reduce fraud liability and enable frictionless payment experiences. Checks enrollment, validates payer authentication responses, and integrates with issuer b
  name: CyberSource Payer Authentication (3D Secure) API
  slug: cybersource-payer-authentication-3d-secure-api
- description: Generates financial, reconciliation, and operational reports covering transaction history, settlement data, chargebacks, and OCT activity. Supports on-demand report generation, scheduled report subscr
  name: CyberSource Reporting API
  slug: cybersource-reporting-api
- description: Enables merchants to query, filter, and retrieve transaction records by various criteria including date range, amount, card type, merchant reference number, and transaction status. Supports both indiv
  name: CyberSource Transaction Search API
  slug: cybersource-transaction-search-api
- description: 'Event-driven notification system that delivers real-time alerts for payment events, fraud decisions, and system state changes to merchant-configured endpoints. Supports digital signatures for payload '
  name: CyberSource Webhooks API
  slug: cybersource-webhooks-api
- description: 'Programmatically creates and manages hierarchical merchant account structures representing business units, divisions, and sub-merchants. Enables ISOs, payment facilitators, and technology partners to '
  name: CyberSource Boarding API
  slug: cybersource-boarding-api
- description: 'Creates and manages payment invoices with customizable fields, due dates, and customer information. Generates shareable payment links, tracks invoice status, and enables merchants to collect payments '
  name: CyberSource Invoicing API
  slug: cybersource-invoicing-api
- description: Identifies card type, issuing bank, country of origin, and fast funds eligibility based on the Bank Identification Number (BIN) extracted from payment card numbers. Helps merchants optimize checkout r
  name: CyberSource BIN Lookup API
  slug: cybersource-bin-lookup-api
- description: Unified API suite for secure, cross-network agent-initiated payments enabling seamless merchant onboarding, card enrollment, and transaction management. Designed to support AI agent workflows, automat
  name: CyberSource Intelligent Commerce API
  slug: cybersource-intelligent-commerce-api
- description: The Visa Bank Account Validation Service is a new standalone product designed to validate customer's routing and bank account number combination for ACH transactions. Merchant's can use this standalon
  name: CyberSource bankAccountValidation API
  slug: cybersource-bankaccountvalidation-api
- description: Once a batch is created its status can be checked using the status resource. When the batch status is COMPLETED its report can then be retrieved.
  name: CyberSource Batches API
  slug: cybersource-batches-api
- description: A billingAgreement is a stand-alone transaction that is not linked to any previous transactions. It takes money from your merchant bank account and returns it to the customer.
  name: CyberSource billingAgreements API
  slug: cybersource-billingagreements-api
- description: The Bin Lookup API from CyberSource — 1 operation(s) for bin lookup.
  name: CyberSource Bin Lookup API
  slug: cybersource-bin-lookup-api
- description: When you are ready to fulfill a customer's order and transfer funds from the customer's bank to your bank, capture the payment for that order.
  name: CyberSource capture API
  slug: cybersource-capture-api
- description: API for requesting Chargeback Details.
  name: CyberSource Chargeback Details API
  slug: cybersource-chargeback-details-api
- description: API for requesting Chargeback Summaries.
  name: CyberSource Chargeback Summaries API
  slug: cybersource-chargeback-summaries-api
- description: API for retrieving conversion data for merchant
  name: CyberSource Conversion Details API
  slug: cybersource-conversion-details-api
- description: Create a new webhook connection
  name: CyberSource Create New Webhooks API
  slug: cybersource-create-new-webhooks-api
- description: MPP (Machine Payment Protocol) token provisioning and encrypted credential generation. Use these APIs to provision encrypted payment credentials for use in MPP Authorization Payment headers. Accepts a
  name: CyberSource Credentials API
  slug: cybersource-credentials-api
- description: A credit is a stand-alone transaction that is not linked to any previous transactions. It takes money from your merchant bank account and returns it to the customer.
  name: CyberSource credit API
  slug: cybersource-credit-api
- description: A Customer can be linked to multiple Payment Instruments and Shipping Addresses. With one Payment Instrument and Shipping Address designated as the default. It stores merchant reference information fo
  name: CyberSource Customer API
  slug: cybersource-customer-api
- description: A Customer Payment Instrument is linked to a Customer and an Instrument Identifier. It stores additional information in relation to a card number(PAN) or bank account (echeck).
  name: CyberSource Customer Payment Instrument API
  slug: cybersource-customer-payment-instrument-api
- description: A Customer Shipping Address is linked to a Customer. It stores shipping information in relation to the Customer.
  name: CyberSource Customer Shipping Address API
  slug: cybersource-customer-shipping-address-api
- description: REST API for the Decision Manager Service
  name: CyberSource Decision Manager API
  slug: cybersource-decision-manager-api
- description: Remove Association of a Device.
  name: CyberSource Device De-Association API
  slug: cybersource-device-de-association-api
- description: Search and Retrieve Devices.
  name: CyberSource Device Search API
  slug: cybersource-device-search-api
- description: API to download report DTDs
  name: CyberSource Download DTD API
  slug: cybersource-download-dtd-api
- description: API to download report XSDs
  name: CyberSource Download XSD API
  slug: cybersource-download-xsd-api
- description: The EMVTagDetails API from CyberSource — 1 operation(s) for emvtagdetails.
  name: CyberSource EMVTagDetails API
  slug: cybersource-emvtagdetails-api
- description: Card enrollment and tokenization for agentic payments. Use these APIs to register a consumer's payment card, creating a tokenized reference that can be used in subsequent purchase instructions and pay
  name: CyberSource Enrollment API
  slug: cybersource-enrollment-api
- description: 'The Flex API enables merchants to securely accept customer payment information captured within a server-side application using a set of APIs. These APIs protect your customer''s primary account number '
  name: CyberSource Flex API API
  slug: cybersource-flex-api-api
- description: Purchase intent lifecycle management for agentic payments. Use these APIs to create, update, and cancel purchase intents (instructions) that define what a consumer wants to buy, including mandates, or
  name: CyberSource Instructions API
  slug: cybersource-instructions-api
- description: An Instrument Identifier represents a unique card number(PAN) or bank account (echeck). It can also be associated with a Network Token that can be used for payment transactions.
  name: CyberSource Instrument Identifier API
  slug: cybersource-instrument-identifier-api
- description: API for requesting Interchange Clearing Level data for an account or a merchant.
  name: CyberSource Interchange Clearing Level Details API
  slug: cybersource-interchange-clearing-level-details-api
- description: Update the settings for the invoice payment page.
  name: CyberSource Invoice Settings API
  slug: cybersource-invoice-settings-api
- description: Offer your customers a simple, convenient, and fast way to pay with the new online invoicing tool.
  name: CyberSource Invoices API
  slug: cybersource-invoices-api
- description: '- Manage your webhooks. This will allow for you to update existing webhooks, test webhooks, or delete them.'
  name: CyberSource Manage Webhooks API
  slug: cybersource-manage-webhooks-api
- description: Manage Boarding Registrations
  name: CyberSource Merchant Boarding API
  slug: cybersource-merchant-boarding-api
- description: The Merchant Defined Fields API from CyberSource — 2 operation(s) for merchant defined fields.
  name: CyberSource Merchant Defined Fields API
  slug: cybersource-merchant-defined-fields-api
- description: The Microform Integration API from CyberSource — 1 operation(s) for microform integration.
  name: CyberSource Microform Integration API
  slug: cybersource-microform-integration-api
- description: API for retrieving the netfunding data for an account or a merchant
  name: CyberSource Net Fundings API
  slug: cybersource-net-fundings-api
- description: A Network Token represents a tokenized version of a card number (PAN) that can be used for payment transactions and, it's represented by a Tokenized Card in TMS.
  name: CyberSource Network Tokens API
  slug: cybersource-network-tokens-api
- description: API for Notification Of Change
  name: CyberSource Notification Of Changes API
  slug: cybersource-notification-of-changes-api
- description: Operations related to creating, retrieving, and updating offers.
  name: CyberSource Offers API
  slug: cybersource-offers-api
- description: An order is a service that is used for initiating a transaction with itemized details, shipping, billing and buyer information.
  name: CyberSource orders API
  slug: cybersource-orders-api
- description: The Payer Authentication API from CyberSource — 3 operation(s) for payer authentication.
  name: CyberSource Payer Authentication API
  slug: cybersource-payer-authentication-api
- description: API for payment batch summary reports
  name: CyberSource Payment Batch Summaries API
  slug: cybersource-payment-batch-summaries-api
- description: A stand-alone Payment Instrument is linked to an Instrument Identifier. It stores additional information in relation to a card number(PAN) or bank account (echeck).
  name: CyberSource Payment Instrument API
  slug: cybersource-payment-instrument-api
- description: Offer your customers a simple, convenient, and fast way to pay with the new online pay by link tool.
  name: CyberSource Payment Links API
  slug: cybersource-payment-links-api
- description: A payment-tokens is a service that is used for retrieving vault details or deleting vault id/payment method.
  name: CyberSource payment-tokens API
  slug: cybersource-payment-tokens-api
- description: A payment authorizes the amount for the transaction. There are a number of supported payment instruments, such as Credit Card, Debit Card, e-Wallet, and Alternative Payments. A payment response includ
  name: CyberSource payments API
  slug: cybersource-payments-api
- description: A payout enables an originator to send funds on behalf of itself, merchants, or customers to credit card accounts using an Original Credit Transaction (OCT). An originator is a merchant, government en
  name: CyberSource Payouts API
  slug: cybersource-payouts-api
- description: Create and manage Plans for subscriptions.
  name: CyberSource Plans API
  slug: cybersource-plans-api
- description: Cybersource Payouts Funds Transfer REST API for Account Funding Transaction (AFT)
  name: CyberSource Pull Funds API
  slug: cybersource-pull-funds-api
- description: API for Purchase and Refund Details
  name: CyberSource Purchase And Refund Details API
  slug: cybersource-purchase-and-refund-details-api
- description: A payout enables an originator to send funds on behalf of itself, merchants, or customers to credit card accounts using an Original Credit Transaction (OCT). An originator is a merchant, government en
  name: CyberSource Push Funds API
  slug: cybersource-push-funds-api
- description: A refund is a follow-on transaction that uses the ID returned from either a payment or capture request.
  name: CyberSource refund API
  slug: cybersource-refund-api
- description: Get report definition information
  name: CyberSource Report Definitions API
  slug: cybersource-report-definitions-api
- description: API for creation and retrieval of Reports
  name: CyberSource Report Downloads API
  slug: cybersource-report-downloads-api
- description: API for creation and retrieval of Report Subscriptions
  name: CyberSource Report Subscriptions API
  slug: cybersource-report-subscriptions-api
- description: API for creation and retrieval of Reports
  name: CyberSource Reports API
  slug: cybersource-reports-api
- description: API for requesting Retrieval Details.
  name: CyberSource Retrieval Details API
  slug: cybersource-retrieval-details-api
- description: API for requesting Retrieval Summaries
  name: CyberSource Retrieval Summaries API
  slug: cybersource-retrieval-summaries-api
- description: An authorization reversal releases the hold that the payment placed on the customer's funds.
  name: CyberSource reversal API
  slug: cybersource-reversal-api
- description: The SearchTransactions API from CyberSource — 2 operation(s) for searchtransactions.
  name: CyberSource SearchTransactions API
  slug: cybersource-searchtransactions-api
- description: The SecureFileShare API from CyberSource — 2 operation(s) for securefileshare.
  name: CyberSource SecureFileShare API
  slug: cybersource-securefileshare-api
- description: Create and manage Recurring Subscriptions. You have option to link subscription to plan or create independent subscriptions.
  name: CyberSource Subscriptions API
  slug: cybersource-subscriptions-api
- description: Create a Follow-On Subscription from an already existing successful Transaction. You have option to link subscription to plan or create independent subscriptions.
  name: CyberSource Subscriptions Follow-Ons API
  slug: cybersource-subscriptions-follow-ons-api
- description: tax calculation service
  name: CyberSource taxes API
  slug: cybersource-taxes-api
- description: An orchestration resource used to combine multiple API calls into a single request.
  name: CyberSource Tokenize API
  slug: cybersource-tokenize-api
- description: Get a list of batch files or details of Individual file processed through the Offline Transaction Submission Services.
  name: CyberSource TransactionBatches API
  slug: cybersource-transactionbatches-api
- description: The TransactionDetails API from CyberSource — 1 operation(s) for transactiondetails.
  name: CyberSource TransactionDetails API
  slug: cybersource-transactiondetails-api
- description: The Transient Token Data v2 API from CyberSource — 3 operation(s) for transient token data v2.
  name: CyberSource Transient Token Data v2 API
  slug: cybersource-transient-token-data-v2-api
- description: The Unified Checkout Capture Context API from CyberSource — 1 operation(s) for unified checkout capture context.
  name: CyberSource Unified Checkout Capture Context API
  slug: cybersource-unified-checkout-capture-context-api
- description: The Unified Checkout V1 Capture Context API from CyberSource — 1 operation(s) for unified checkout v1 capture context.
  name: CyberSource Unified Checkout V1 Capture Context API
  slug: cybersource-unified-checkout-v1-capture-context-api
- description: The UserManagement API from CyberSource — 1 operation(s) for usermanagement.
  name: CyberSource UserManagement API
  slug: cybersource-usermanagement-api
- description: The UserManagementSearch API from CyberSource — 1 operation(s) for usermanagementsearch.
  name: CyberSource UserManagementSearch API
  slug: cybersource-usermanagementsearch-api
- description: The Verification API from CyberSource — 2 operation(s) for verification.
  name: CyberSource Verification API
  slug: cybersource-verification-api
- description: A void cancels a payment or capture. A transaction can be voided only when CyberSource has not already submitted the capture to your processor. You cannot undo a void.
  name: CyberSource void API
  slug: cybersource-void-api
artifact_total: 164
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation API
  slug: open-cybersource-bankaccountvalidation-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Batches API
  slug: open-cybersource-batches-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation billingAgreements API
  slug: open-cybersource-billingagreements-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Bin Lookup API
  slug: open-cybersource-bin-lookup-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation capture API
  slug: open-cybersource-capture-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Chargeback Details API
  slug: open-cybersource-chargeback-details-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Chargeback Summaries API
  slug: open-cybersource-chargeback-summaries-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Conversion Details API
  slug: open-cybersource-conversion-details-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Create New Webhooks API
  slug: open-cybersource-create-new-webhooks-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Credentials API
  slug: open-cybersource-credentials-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation credit API
  slug: open-cybersource-credit-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Customer API
  slug: open-cybersource-customer-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Customer Payment Instrument API
  slug: open-cybersource-customer-payment-instrument-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Customer Shipping Address API
  slug: open-cybersource-customer-shipping-address-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Decision Manager API
  slug: open-cybersource-decision-manager-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Device De-Association API
  slug: open-cybersource-device-de-association-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Device Search API
  slug: open-cybersource-device-search-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Download DTD API
  slug: open-cybersource-download-dtd-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Download XSD API
  slug: open-cybersource-download-xsd-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation EMVTagDetails API
  slug: open-cybersource-emvtagdetails-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Enrollment API
  slug: open-cybersource-enrollment-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Flex API API
  slug: open-cybersource-flex-api-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Instructions API
  slug: open-cybersource-instructions-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Instrument Identifier API
  slug: open-cybersource-instrument-identifier-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Interchange Clearing Level Details API
  slug: open-cybersource-interchange-clearing-level-details-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Invoice Settings API
  slug: open-cybersource-invoice-settings-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Invoices API
  slug: open-cybersource-invoices-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Manage Webhooks API
  slug: open-cybersource-manage-webhooks-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Merchant Boarding API
  slug: open-cybersource-merchant-boarding-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Merchant Defined Fields API
  slug: open-cybersource-merchant-defined-fields-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Microform Integration API
  slug: open-cybersource-microform-integration-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Net Fundings API
  slug: open-cybersource-net-fundings-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Network Tokens API
  slug: open-cybersource-network-tokens-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Notification Of Changes API
  slug: open-cybersource-notification-of-changes-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Offers API
  slug: open-cybersource-offers-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation orders API
  slug: open-cybersource-orders-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Payer Authentication API
  slug: open-cybersource-payer-authentication-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Payment Batch Summaries API
  slug: open-cybersource-payment-batch-summaries-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Payment Instrument API
  slug: open-cybersource-payment-instrument-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Payment Links API
  slug: open-cybersource-payment-links-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation payment-tokens API
  slug: open-cybersource-payment-tokens-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation payments API
  slug: open-cybersource-payments-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Payouts API
  slug: open-cybersource-payouts-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Plans API
  slug: open-cybersource-plans-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Pull Funds API
  slug: open-cybersource-pull-funds-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Purchase And Refund Details API
  slug: open-cybersource-purchase-and-refund-details-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Push Funds API
  slug: open-cybersource-push-funds-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation refund API
  slug: open-cybersource-refund-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Report Definitions API
  slug: open-cybersource-report-definitions-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Report Downloads API
  slug: open-cybersource-report-downloads-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Report Subscriptions API
  slug: open-cybersource-report-subscriptions-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Reports API
  slug: open-cybersource-reports-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Retrieval Details API
  slug: open-cybersource-retrieval-details-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Retrieval Summaries API
  slug: open-cybersource-retrieval-summaries-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation reversal API
  slug: open-cybersource-reversal-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation SearchTransactions API
  slug: open-cybersource-searchtransactions-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation SecureFileShare API
  slug: open-cybersource-securefileshare-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Subscriptions API
  slug: open-cybersource-subscriptions-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Subscriptions Follow-Ons API
  slug: open-cybersource-subscriptions-follow-ons-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation taxes API
  slug: open-cybersource-taxes-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Tokenize API
  slug: open-cybersource-tokenize-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation TransactionBatches API
  slug: open-cybersource-transactionbatches-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation TransactionDetails API
  slug: open-cybersource-transactiondetails-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Transient Token Data v2 API
  slug: open-cybersource-transient-token-data-v2-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Unified Checkout Capture Context API
  slug: open-cybersource-unified-checkout-capture-context-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Unified Checkout V1 Capture Context API
  slug: open-cybersource-unified-checkout-v1-capture-context-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation UserManagement API
  slug: open-cybersource-usermanagement-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation UserManagementSearch API
  slug: open-cybersource-usermanagementsearch-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation Verification API
  slug: open-cybersource-verification-api
- collection_type: open
  name: CyberSource Merged Spec bankAccountValidation void API
  slug: open-cybersource-void-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cybersource-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cybersource-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.cybersource.com/en-us/blog.html
- group: start
  title: ''
  type: Portal
  url: https://developer.cybersource.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cybersource.com/en/main.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started.html
- group: docs
  title: ''
  type: APIReference
  url: https://developer.cybersource.com/api-reference-assets/index.html
- group: build
  title: ''
  type: SDKs
  url: https://developer.cybersource.com/api/developer-guides.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/CyberSource
- group: operate
  title: ''
  type: Status
  url: https://status.cybersource.com/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.cybersource.com/en/release-notes/index.html
- group: operate
  title: ''
  type: Community
  url: https://community.developer.cybersource.com/
- group: operate
  title: ''
  type: Support
  url: https://support.cybersource.com/
- group: start
  title: ''
  type: Sandbox
  url: https://developer.cybersource.com/hello-world/sandbox.html
- group: docs
  title: ''
  type: TestingGuide
  url: https://developer.cybersource.com/hello-world/testing-guide.html
- group: build
  title: ''
  type: ResponseCodes
  url: https://developer.cybersource.com/api/reference/response-codes.html
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/cybersource/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/cybersource/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/cybersource/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: CyberSource, a Visa solution, is a global payment management platform that enables businesses to accept payments online, in-app, and in-person. It provides REST APIs for payment authorization and processing, fraud management via Decision Manager, payment tokenization, recurring billing, payouts, and comprehensive post-transaction reporting. The platform operates across 190+ countries and supports card-present, card-not-present, digital wallets, alternative payment methods, and buy-now-pay-later integrations.
examples:
- key_count: 3
  name: Cybersource Api Examples
  slug: cybersource-api-examples
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cybersource.png
json_schemas:
- name: CyberSource API Schemas
  property_count: 0
  slug: cybersource-api-schemas
jsonld:
- class_count: 6
  name: Cybersource Api Context
  property_count: 0
  slug: cybersource-api
layout: provider
modified: '2026-06-13'
name: CyberSource
nav: Providers
network: true
overview: 'CyberSource publishes 73 APIs on the [APIs.io](https://apis.io/) network, including Decision Manager API, Payouts API, BIN Lookup API, and 70 more. Tagged areas include Payments, Payment Processing, Fraud Management, Tokenization, and Recurring Billing.


  The CyberSource catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CyberSource''s developer surface includes engineering blog, developer portal, documentation, getting-started guide, API reference, GitHub presence, status page, and 12 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 147
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: CyberSource API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cybersource-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.2
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 58.8
    developer_ergonomics: 54.3
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 44.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 70
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 23.4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cybersource/refs/heads/main/screenshots/cybersource-2026-06-20T175413.png
security:
- kind: domain-security
  name: Cybersource Domain Security
  slug: cybersource-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cybersource
tags:
- Payments
- Payment Processing
- Fraud Management
- Tokenization
- Recurring Billing
- Payouts
- Payment Gateway
- Financial Technology
website: https://developer.cybersource.com/
---

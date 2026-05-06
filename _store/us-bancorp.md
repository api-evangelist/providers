---
aid: us-bancorp
url: https://raw.githubusercontent.com/api-evangelist/us-bancorp/refs/heads/main/apis.yml
apis:
  - aid: us-bancorp:us-bank-corporate-account-information
    name: US Bank Corporate Account Information API
    tags:
      - Banking
      - Corporate Banking
      - Account Information
      - Treasury Management
      - Finance
      - Fortune 500
    humanURL: https://developer.usbank.com/solution-areas/treasury-management-apis
    baseURL: https://api.usbank.com
    properties:
      - url: https://developer.usbank.com/solution-areas/treasury-management-apis
        type: Documentation
      - url: https://developer.usbank.com/
        type: DeveloperPortal
      - url: https://developer.usbank.com/getting-started-with-our-apis
        type: GettingStarted
      - url: https://raw.githubusercontent.com/api-evangelist/us-bancorp/refs/heads/main/openapi/us-bank-corporate-account-information-openapi.yml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/us-bancorp/refs/heads/main/json-schema/us-bank-account-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/us-bancorp/refs/heads/main/json-schema/us-bank-transaction-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/us-bancorp/refs/heads/main/json-ld/us-bancorp-context.jsonld
        type: JSONLDContext
    description: The Corporate Account Information API provides access to U.S. Bank deposit account balances and transaction data for corporate customers. It enables retrieval of current-day and previous-day account balances (available, ledger, and collected), transaction history up to 60 days (with optional 12 or 24-month retention), and deposit account statements. Authentication uses OAuth MFA with SinglePoint credentials.
  - aid: us-bancorp:us-bank-rtp
    name: US Bank RTP Real-Time Payments API
    tags:
      - Payments
      - Real-Time Payments
      - RTP
      - Banking
      - Treasury Management
      - Finance
    humanURL: https://developer.usbank.com/solution-areas/corporate-payment-apis
    properties:
      - url: https://developer.usbank.com/solution-areas/corporate-payment-apis
        type: Documentation
      - url: https://developer.usbank.com/products/rtp-credit-transfer-message/v1
        type: CreditTransferDocs
      - url: https://developer.usbank.com/product-suites/rtp-api-product-suite
        type: ProductSuite
      - url: https://raw.githubusercontent.com/api-evangelist/us-bancorp/refs/heads/main/openapi/us-bank-rtp-openapi.yml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/us-bancorp/refs/heads/main/capabilities/treasury-management.yaml
        type: NaftikoCapability
      - url: https://raw.githubusercontent.com/api-evangelist/us-bancorp/refs/heads/main/capabilities/payments.yaml
        type: NaftikoCapability
      - url: https://raw.githubusercontent.com/api-evangelist/us-bancorp/refs/heads/main/rules/us-bank-rules.yml
        type: SpectralRuleset
    description: The RTP Real-Time Payments API enables 24/7/365 real-time payment origination through The Clearing House RTP network. Supports credit transfer messages, request for payment (RFP), and RTP eligibility verification. Transactions settle instantly and are irrevocable once sent.
  - aid: us-bancorp:us-bank-ach-originations
    name: US Bank ACH Originations API
    tags:
      - Payments
      - ACH
      - Banking
      - Corporate Payments
      - Finance
    humanURL: https://developer.usbank.com/products/ach-originations/v1
    properties:
      - url: https://developer.usbank.com/products/ach-originations/v1
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/us-bancorp/refs/heads/main/openapi/us-bank-ach-originations-openapi.yml
        type: OpenAPI
    description: The ACH Originations API enables origination of ACH (Automated Clearing House) payments from U.S. Bank corporate accounts. Supports standard ACH credit and debit transactions for payroll, vendor payments, and customer collections.
  - aid: us-bancorp:us-bank-positive-pay
    name: US Bank Positive Pay API
    tags:
      - Payments
      - Fraud Prevention
      - Check Management
      - Treasury Management
      - Banking
    humanURL: https://developer.usbank.com/products/positive-pay/v1
    properties:
      - url: https://developer.usbank.com/products/positive-pay/v1
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/us-bancorp/refs/heads/main/openapi/us-bank-positive-pay-openapi.yml
        type: OpenAPI
    description: The Positive Pay API helps detect check fraud by electronically matching checks to issued items. Enables retrieval of exception items (checks that don't match issued items), submission of pay/return decisions, and access to exception history. Exceptions are available 9am-3pm local processing time.
  - aid: us-bancorp:us-bank-push-to-card
    name: US Bank Push to Card API
    tags:
      - Payments
      - Disbursements
      - Debit Card
      - Banking
      - Finance
    humanURL: https://developer.usbank.com/products/push-to-card/v1
    properties:
      - url: https://developer.usbank.com/products/push-to-card/v1
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/us-bancorp/refs/heads/main/openapi/us-bank-push-to-card-openapi.yml
        type: OpenAPI
    description: The Push to Card API enables instant fund disbursements directly to Visa and Mastercard debit cards. Ideal for disbursements, refunds, and payouts up to $125,000 per transaction. Transactions are irrevocable once sent and provide immediate fund access to recipients.
  - aid: us-bancorp:us-bank-wire-transfers
    name: US Bank Wire Transfers API
    tags:
      - Payments
      - Wire Transfers
      - Banking
      - Treasury Management
      - Finance
    humanURL: https://developer.usbank.com/products/wire-transfers/v1
    properties:
      - url: https://developer.usbank.com/products/wire-transfers/v1
        type: Documentation
    description: The Wire Transfers API enables domestic and international wire transfer origination from U.S. Bank corporate accounts for large-value, time-sensitive payments.
  - aid: us-bancorp:us-bank-data-toolbox
    name: US Bank Data Toolbox API
    tags:
      - Banking
      - Account Data
      - Retail Banking
      - Finance
      - Open Banking
    humanURL: https://developer.usbank.com/products/data-toolbox/v1
    properties:
      - url: https://developer.usbank.com/products/data-toolbox/v1
        type: Documentation
      - url: https://developer.usbank.com/products/data-toolbox-accounts/v1
        type: AccountsDocs
      - url: https://developer.usbank.com/solution-areas/retail-banking-apis
        type: RetailBankingAPIs
    description: The Data Toolbox API provides access to U.S. Bank retail banking consumer account data including checking, savings, credit card, mortgage, and brokerage account information. Used to build personalized financial management experiences and enable embedded banking.
  - aid: us-bancorp:us-bank-voyager
    name: US Bank Voyager Fleet API
    tags:
      - Fleet Management
      - Transportation
      - Banking
      - Finance
      - Corporate Payments
    humanURL: https://developer.usbank.com/product-suites/voyager-api-product-suite
    properties:
      - url: https://developer.usbank.com/product-suites/voyager-api-product-suite
        type: Documentation
      - url: https://developer.usbank.com/products/voyager-transactions/v2
        type: TransactionsDocs
      - url: https://developer.usbank.com/products/voyager-vehicles/v1
        type: VehiclesDocs
      - url: https://developer.usbank.com/products/voyager-accounts/v1
        type: AccountsDocs
    description: The Voyager Fleet API suite provides fleet management capabilities for the Voyager network, enabling access to fleet transaction data, vehicle management, account information, and reporting for corporate fleet card customers.
  - aid: us-bancorp:us-bank-freight-payment
    name: US Bank Freight Payment API
    tags:
      - Freight Payment
      - Transportation
      - Banking
      - Finance
      - Supply Chain
    humanURL: https://developer.usbank.com/product-suites/freight-payment-api-product-suite
    properties:
      - url: https://developer.usbank.com/product-suites/freight-payment-api-product-suite
        type: Documentation
      - url: https://developer.usbank.com/products/freight-payment-transactions/v1
        type: TransactionsDocs
      - url: https://developer.usbank.com/products/freight-payment-user-management/v1
        type: UserManagementDocs
    description: The Freight Payment API suite provides freight audit and payment processing capabilities, enabling freight shippers to submit and receive transaction data through a single API and manage freight payment users.
  - aid: us-bancorp:us-bank-instant-payments
    name: US Bank Instant Payments API
    tags:
      - Payments
      - Instant Payments
      - Banking
      - Finance
    humanURL: https://developer.usbank.com/products/instant-payments/v2
    properties:
      - url: https://developer.usbank.com/products/instant-payments/v2
        type: Documentation
    description: The Instant Payments API enables instant payment origination supporting FedNow and RTP payment rails for real-time settlement.
  - aid: us-bancorp:us-bank-bank-holidays
    name: US Bank Holidays API
    tags:
      - Banking
      - Holidays
      - Reference Data
      - Finance
    humanURL: https://developer.usbank.com/products/bank-holidays/v1
    properties:
      - url: https://developer.usbank.com/products/bank-holidays/v1
        type: Documentation
    description: The Bank Holidays API provides information about U.S. Bank processing holidays and Federal Reserve banking holidays, useful for payment scheduling and clearing house availability calculations.
name: US Bancorp
tags:
  - Banking
  - Finance
  - Fortune 500
  - Corporate Banking
  - Payments
  - Open Banking
  - Treasury Management
  - Consumer Banking
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-21'
modified: '2026-05-04'
position: Consuming
description: U.S. Bancorp is the parent company of U.S. Bank National Association, one of the largest commercial banks in the United States. U.S. Bank provides a developer portal at developer.usbank.com offering APIs for corporate banking, payments, and treasury management including RTP, ACH, Positive Pay, corporate account information, data toolbox, fleet management (Voyager), freight payment, and push-to-card capabilities. Authentication uses OAuth MFA with SinglePoint credentials.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - type: Features
    data:
      - 'U.S. Bancorp: API access via partner / B2B contracts only'
      - No public API pricing published — contact enterprise sales
      - U.S. Bank APIs are sold to commercial treasury and embedded payment customers via account managers.
    sources:
      - https://www.usbank.com/corporate-and-commercial-banking.html
    updated: '2026-05-04'
---

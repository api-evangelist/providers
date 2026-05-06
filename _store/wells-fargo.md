---
aid: wells-fargo
url: https://raw.githubusercontent.com/api-evangelist/wells-fargo/refs/heads/main/apis.yml
modified: '2026-05-03'
description: Wells Fargo is a diversified, community-based financial services company providing banking, investment, mortgage, and consumer and commercial finance through thousands of stores and digital channels. Wells Fargo operates a comprehensive developer portal at developer.wellsfargo.com offering open banking APIs for payments, account data, and treasury management. The Gateway API platform handles over 1.5 billion API calls annually and supports commercial banking customers with ACH, wire, RTP, FedNow, and data reporting capabilities.
common:
  - type: Website
    url: https://www.wellsfargo.com
  - type: DeveloperPortal
    url: https://developer.wellsfargo.com
  - type: Documentation
    url: https://developer.wellsfargo.com/documentation
  - type: GitHubOrg
    url: https://github.com/wells-fargo
  - type: JSONLDContext
    url: json-ld/wells-fargo-context.jsonld
  - type: Vocabulary
    url: vocabulary/wells-fargo-vocabulary.yml
apis:
  - aid: wells-fargo:gateway-api
    name: Wells Fargo Gateway API
    tags:
      - Banking
      - Financial Services
      - Open Banking
      - Payments
      - Treasury Management
      - Commercial Banking
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.wellsfargo.com
    humanURL: https://developer.wellsfargo.com/
    properties:
      - url: https://developer.wellsfargo.com/apis
        type: Documentation
      - url: openapi/wells-fargo-gateway-api-openapi.yml
        type: OpenAPI
      - url: examples/wells-fargo-gateway-api-listAccounts-example.json
        type: Example
      - url: examples/wells-fargo-gateway-api-createPayment-example.json
        type: Example
      - url: rules/wells-fargo-rules.yml
        type: SpectralRuleset
      - url: capabilities/shared/gateway-api.yaml
        type: NaftikoCapability
    description: The Wells Fargo Gateway API is a comprehensive open banking platform launched in 2016, offering a growing catalog of plug-and-play APIs, SDKs, and webhooks for commercial customers and partners. The platform supports payments, real-time account information, and financial data integration across commercial banking, mortgage, credit card, and brokerage services. Built on RESTful principles with OAuth 2.0 authentication, the Gateway handles over 1.5 billion API calls annually.
  - aid: wells-fargo:account-transactions-api
    name: Wells Fargo Account Transactions API
    tags:
      - Banking
      - Financial Services
      - Account Management
      - Transactions
      - Treasury Management
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.wellsfargo.com
    humanURL: https://developer.wellsfargo.com/documentation/api-references/account-transactions/v3/transaction-detail-api-ref-v3
    properties:
      - url: https://developer.wellsfargo.com/documentation/api-references/account-transactions/v3/transaction-detail-api-ref-v3
        type: Documentation
      - url: openapi/wells-fargo-account-transactions-api-openapi.yml
        type: OpenAPI
      - url: json-schema/wells-fargo-transaction-schema.json
        type: JSONSchema
      - url: json-structure/wells-fargo-transaction-structure.json
        type: JSONStructure
      - url: examples/wells-fargo-account-transactions-api-listAccountTransactions-example.json
        type: Example
      - url: rules/wells-fargo-rules.yml
        type: SpectralRuleset
      - url: capabilities/shared/account-transactions-api.yaml
        type: NaftikoCapability
    description: The Wells Fargo Account Transactions API enables treasury management customers to search and retrieve transaction data from the current day through 180 days prior. The API supports ACH, Wire, and RTP/Instant Payment transactions with unique transaction IDs, intraday and previous day reporting, and pagination for high-volume transaction retrieval.
  - aid: wells-fargo:ach-payments-api
    name: Wells Fargo ACH Payments API
    tags:
      - Banking
      - Financial Services
      - Payments
      - ACH
      - Treasury Management
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.wellsfargo.com
    humanURL: https://developer.wellsfargo.com/documentation/api-references/ach-payments/v2/ach-payments-api-ref-v2
    properties:
      - url: https://developer.wellsfargo.com/documentation/api-references/ach-payments/v2/ach-payments-api-ref-v2
        type: Documentation
      - url: openapi/wells-fargo-ach-payments-api-openapi.yml
        type: OpenAPI
      - url: json-schema/wells-fargo-ach-payment-schema.json
        type: JSONSchema
      - url: json-structure/wells-fargo-ach-payment-structure.json
        type: JSONStructure
      - url: examples/wells-fargo-ach-payments-api-initiateAchPayment-example.json
        type: Example
      - url: rules/wells-fargo-rules.yml
        type: SpectralRuleset
      - url: capabilities/shared/ach-payments-api.yaml
        type: NaftikoCapability
    description: The Wells Fargo ACH Payments API enables commercial banking customers to initiate ACH credit and debit transactions, including same-day ACH, for payroll, vendor payments, and collections. The API integrates with Wells Fargo's intelligent payment routing that automatically selects the optimal rail including RTP, FedNow, and ACH for each transaction.
---

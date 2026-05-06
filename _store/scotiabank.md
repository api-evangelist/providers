---
aid: scotiabank
name: Scotiabank
description: Scotiabank is one of Canada's leading financial institutions and a major international bank. Through its Scotia TranXact developer portal, Scotiabank provides APIs for corporate and commercial customers to integrate banking capabilities into their treasury management, ERP, and CRM systems. APIs cover wire payments, real-time payments via INTERAC e-Transfer, EFT payments, account balance and transaction data, account validation, and payment track and trace.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Banking
  - Finance
  - Payments
  - Canada
  - Open Banking
created: '2026-05-02'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/scotiabank/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: scotiabank:scotia-tranxact
    name: Scotia TranXact APIs
    description: Scotia TranXact APIs provide corporate and commercial customers with programmatic access to Scotiabank's payments and cash management services. APIs support wire payments (domestic and international), real-time INTERAC e-Transfer payments, EFT payment management, account balance and transaction retrieval, account validation, and payment status tracking.
    humanURL: https://developer.scotiabank.com/en.html
    tags:
      - Banking
      - Payments
      - Wire Transfer
      - EFT
      - Account Management
    properties:
      - type: Documentation
        url: https://developer.scotiabank.com/en.html
      - type: DeveloperPortal
        url: https://developer.scotiabank.com/en.html
      - type: GettingStarted
        url: https://developer.scotiabank.com/content/scotiabank/developer/api/en/getting-started.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/scotiabank/refs/heads/main/openapi/scotiabank-tranxact-openapi.yml
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/scotiabank/refs/heads/main/rules/scotiabank-rules.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/scotiabank/refs/heads/main/json-schema/scotiabank-transaction-schema.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/scotiabank/refs/heads/main/json-ld/scotiabank-context.jsonld
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/scotiabank/refs/heads/main/json-structure/scotiabank-wire-payment-structure.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/scotiabank/refs/heads/main/examples/scotiabank-initiate-wire-payment-example.json
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/scotiabank/refs/heads/main/vocabulary/scotiabank-vocabulary.yml
      - type: NaftikoCapabilities
        url: https://raw.githubusercontent.com/api-evangelist/scotiabank/refs/heads/main/capabilities/banking-payments.yaml
  - aid: scotiabank:wire-payments
    name: Wire Payments API
    description: Enables businesses to initiate secure, one-time wire transfers between accounts in the same currency (CAD or USD), domestically within Canada and the U.S., or internationally. Uses the SWIFT GPI-enabled network with Unique End-to-End Transaction Reference (UETR) for real-time tracking.
    humanURL: https://developer.scotiabank.com/content/scotiabank/developer/api/en/products/Payments-and-Cash-Management-APIs.html
    tags:
      - Wire Transfer
      - Payments
      - SWIFT
      - Banking
    properties:
      - type: Documentation
        url: https://developer.scotiabank.com/content/scotiabank/developer/api/en/products/Payments-and-Cash-Management-APIs.html
  - aid: scotiabank:real-time-payments
    name: Real-time Payments API
    description: Provides fast payment capabilities for business transactions via INTERAC e-Transfer for business. Customers can send up to $25,000 per transaction in real time.
    humanURL: https://developer.scotiabank.com/content/scotiabank/developer/api/en/products/Payments-and-Cash-Management-APIs.html
    tags:
      - Real-Time Payments
      - INTERAC
      - Payments
      - Banking
    properties:
      - type: Documentation
        url: https://developer.scotiabank.com/content/scotiabank/developer/api/en/products/Payments-and-Cash-Management-APIs.html
  - aid: scotiabank:eft-payments
    name: EFT Payment API
    description: Supports creation and submission of Electronic Funds Transfers (EFTs), including inquiring on payment and file status, deleting, updating, and recalling or reversing payments.
    humanURL: https://developer.scotiabank.com/content/scotiabank/developer/api/en/products/Payments-and-Cash-Management-APIs.html
    tags:
      - EFT
      - Payments
      - Banking
      - ACH
    properties:
      - type: Documentation
        url: https://developer.scotiabank.com/content/scotiabank/developer/api/en/products/Payments-and-Cash-Management-APIs.html
  - aid: scotiabank:account-balance-transactions
    name: Account Balance and Transactions API
    description: Provides the ability to retrieve account balance for the current day or any prior day along with enriched transaction data for the two years prior, and view a list of eligible deposit accounts.
    humanURL: https://developer.scotiabank.com/content/scotiabank/developer/api/en/products/Payments-and-Cash-Management-APIs.html
    tags:
      - Account Management
      - Transactions
      - Banking
      - Balance
    properties:
      - type: Documentation
        url: https://developer.scotiabank.com/content/scotiabank/developer/api/en/products/Payments-and-Cash-Management-APIs.html
  - aid: scotiabank:account-validation
    name: Account Validation API
    description: Assists clients in determining the validity of an account number's format and indicates the likelihood of account ownership match for Scotiabank accounts.
    humanURL: https://developer.scotiabank.com/content/scotiabank/developer/api/en/products/Payments-and-Cash-Management-APIs.html
    tags:
      - Account Validation
      - Banking
      - Verification
    properties:
      - type: Documentation
        url: https://developer.scotiabank.com/content/scotiabank/developer/api/en/products/Payments-and-Cash-Management-APIs.html
  - aid: scotiabank:payment-track-trace
    name: Payment Track and Trace API
    description: Provides the capability to inquire on the status of wire payments using unique reference numbers, offering real-time payment tracking powered by SWIFT GPI.
    humanURL: https://developer.scotiabank.com/content/scotiabank/developer/api/en/products/Payments-and-Cash-Management-APIs.html
    tags:
      - Payment Tracking
      - Wire Transfer
      - Banking
      - SWIFT
    properties:
      - type: Documentation
        url: https://developer.scotiabank.com/content/scotiabank/developer/api/en/products/Payments-and-Cash-Management-APIs.html
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

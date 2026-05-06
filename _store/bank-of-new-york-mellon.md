---
aid: bank-of-new-york-mellon
url: https://raw.githubusercontent.com/api-evangelist/bank-of-new-york-mellon/refs/heads/main/apis.yml
name: BNY Mellon
tags:
  - Asset Servicing
  - Banking
  - Institutional Banking
  - Payments
  - Treasury
  - Wire Transfers
modified: '2026-04-21'
description: BNY Mellon is a global investments company providing asset servicing, asset management, wealth management, treasury services, and clearance and collateral management for institutions and individuals. The BNY Mellon Marketplace (marketplace.bnymellon.com) and developer portal (developer.bny.com) provide Treasury Services APIs for corporate clients to automate payments, account management, balance reporting, and funds transfers.
apis:
  - aid: bank-of-new-york-mellon:treasury-services-api
    name: BNY Mellon Treasury Services API
    tags:
      - Accounts
      - Balances
      - Funds Transfers
      - Institutional Banking
      - Payments
      - Treasury
      - Wire Transfers
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.bnymellon.com/treasury/v4
    humanURL: https://marketplace.bnymellon.com/treasury/api-central/
    properties:
      - url: https://marketplace.bnymellon.com/treasury/api-central/
        type: Documentation
      - url: https://developer.bny.com/app/
        type: Documentation
        name: BNY Developer Marketplace
      - url: openapi/bny-mellon-treasury-services-api-openapi.yml
        type: OpenAPI
    description: The BNY Mellon Treasury Services API enables institutional clients to programmatically initiate and track payments (wire, ACH, SWIFT, CHIPS), access account balances and transaction history, and manage funds transfers. The API is available via the BNY Mellon Marketplace and supports global treasury operations across multiple currencies.
common:
  - type: Website
    url: https://www.bnymellon.com/
    name: BNY Mellon
  - type: Documentation
    url: https://marketplace.bnymellon.com/treasury/api-central/
    name: Treasury API Central
  - type: Documentation
    url: https://developer.bny.com/app/
    name: BNY Developer Marketplace
  - type: PrivacyPolicy
    url: https://www.bnymellon.com/us/en/disclaimers/privacy-notice.html
    name: Privacy Notice
  - type: SpectralRules
    url: rules/bny-mellon-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/bny-mellon-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/treasury-operations.yaml
  - type: JSON-LD
    url: json-ld/bny-mellon-context.jsonld
  - name: Features
    type: Features
    data:
      - name: Account Management
        description: Access institutional account details and metadata.
      - name: Balance Reporting
        description: Real-time and intraday account balance queries.
      - name: Transaction History
        description: Detailed transaction history with date range filtering.
      - name: Payment Initiation
        description: Initiate wire, ACH, SWIFT, and CHIPS payments globally.
      - name: Funds Transfers
        description: Internal account-to-account funds transfer management.
      - name: OAuth2 Security
        description: Client credentials OAuth2 flow for secure API access.
      - name: Sandbox Environment
        description: UAT sandbox for developer testing and integration validation.
      - name: Multi-Currency
        description: Support for payments and balances across multiple currencies.
  - name: Use Cases
    type: UseCases
    data:
      - name: Treasury Automation
        description: Automate daily cash positioning, balance queries, and payment workflows.
      - name: Payment Processing
        description: Initiate global wire, ACH, and SWIFT payments programmatically.
      - name: Liquidity Management
        description: Real-time account balance visibility for institutional liquidity decisions.
      - name: Reconciliation
        description: Automated transaction downloads for reconciliation and reporting.
      - name: ERP Integration
        description: Connect SAP, Oracle, and other ERP/TMS systems to BNY Mellon treasury APIs.
      - name: Custody Operations
        description: Integrate treasury APIs into asset servicing and custody workflows.
  - name: Integrations
    type: Integrations
    data:
      - name: SAP
      - name: Oracle
      - name: Kyriba
      - name: FIS Quantum
      - name: ION Treasury
      - name: Workday
      - name: Reval
created: '2024-01-01'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---

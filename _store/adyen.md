---
aid: adyen
url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/apis.yml
name: Adyen
tags:
  - Payments
  - Financial Services
  - Fintech
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: '2023-11-13'
modified: '2026-05-04'
description: Adyen is a global payment company that provides businesses with a single platform to accept payments from customers worldwide. Their technology enables companies to accept a wide range of payment methods, including credit cards, digital wallets, and local payment methods, in multiple currencies and countries. Adyen also offers services such as fraud prevention, data analytics, and optimization tools to help businesses streamline their payment processes and improve their overall performance.
specificationVersion: '0.16'
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
apis:
  - aid: adyen:adyen-accounting-notifications-api
    name: Adyen Accounting Notifications API
    tags:
      - Accounting
      - Notifications
      - Webhooks
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://cal-test.adyen.com
    humanURL: https://docs.adyen.com/marketplaces-and-platforms/classic/configure-notifications/
    description: Adyen sends notifications through webhooks to inform your system about incoming and outgoing transfers in your platform. You can use these webhooks to build your implementation. For example, you can use this information to update balances in your own dashboards or to keep track of incoming funds.
    properties:
      - url: https://docs.adyen.com/marketplaces-and-platforms/classic/configure-notifications/
        type: Documentation
      - url: openapi/accounting-notifications-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-account-api
    name: Adyen Account API
    tags:
      - Account
      - Accounts
      - Bank
      - Holders
      - Shareholders
      - Verification
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://cal-test.adyen.com
    humanURL: https://docs.adyen.com/api-explorer/Account/6/overview
    description: This API is used for the classic integration. The Account API provides endpoints for managing account-related entities on your platform. These related entities include account holders, accounts, bank accounts, shareholders, and verification-related documents. The management operations include actions such as creation, retrieval, updating, and deletion of them.
    properties:
      - url: https://docs.adyen.com/api-explorer/Account/6/overview
        type: Documentation
      - url: openapi/accounts-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-authentication-webhooks-api
    name: Adyen Authentication Webhooks API
    tags:
      - Authentication
      - Webhooks
      - 3D Secure
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://cal-test.adyen.com
    humanURL: https://docs.adyen.com/development-resources/webhooks/
    description: Adyen sends webhooks to inform your system about events related to cardholder authentication.
    properties:
      - url: https://docs.adyen.com/development-resources/webhooks/
        type: Documentation
      - url: openapi/authentication-webhooks-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-balance-control-api
    name: Adyen Balance Control API
    tags:
      - Balance
      - Transfers
      - Merchants
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://cal-test.adyen.com
    humanURL: https://docs.adyen.com/api-explorer/BalanceControl/1/overview
    description: The Balance Control API lets you transfer funds between merchant accounts that belong to the same legal entity and are under the same company account.
    properties:
      - url: https://docs.adyen.com/api-explorer/BalanceControl/1/overview
        type: Documentation
      - url: openapi/balance-control-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-binlookup-api
    name: Adyen BinLookup API
    tags:
      - BIN
      - Card
      - 3D Secure
      - Cost Estimation
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://pal-test.adyen.com
    humanURL: https://docs.adyen.com/api-explorer/BinLookup/52/overview
    description: The BIN Lookup API provides endpoints for retrieving information, such as cost estimates, and 3D Secure supported version based on a given BIN.
    properties:
      - url: https://docs.adyen.com/api-explorer/BinLookup/52/overview
        type: Documentation
      - url: openapi/binlookup-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-checkout-api
    name: Adyen Checkout API
    tags:
      - Checkout
      - Payments
      - Sessions
      - Orders
      - Refunds
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://checkout-test.adyen.com
    humanURL: https://docs.adyen.com/api-explorer/Checkout/71/overview
    description: The Checkout API provides a powerful, PCI-compliant way to accept payments online. It supports a broad range of payment methods, including cards, wallets, and local payment methods, with built-in 3D Secure and fraud detection.
    properties:
      - url: https://docs.adyen.com/api-explorer/Checkout/71/overview
        type: Documentation
      - url: openapi/checkout-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-configuration-api
    name: Adyen Configuration API
    tags:
      - Configuration
      - Balance Platform
      - Account Holders
      - Balance Accounts
      - Cards
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://balanceplatform-api-test.adyen.com
    humanURL: https://docs.adyen.com/api-explorer/balanceplatform/2/overview
    description: The Configuration API enables you to create a platform where you can onboard your users as account holders and create balance accounts, cards, and business accounts.
    properties:
      - url: https://docs.adyen.com/api-explorer/balanceplatform/2/overview
        type: Documentation
      - url: openapi/configuration-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-configuration-webhooks-api
    name: Adyen Configuration Webhooks API
    tags:
      - Configuration
      - Webhooks
      - Balance Platform
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://balanceplatform-api-test.adyen.com
    humanURL: https://docs.adyen.com/api-explorer/balanceplatform-webhooks/1/overview
    description: Adyen sends webhooks to inform your system about events that occur in your platform. These events include, for example, when an account holders capabilities are updated, or when a sweep configuration is created or updated.
    properties:
      - url: https://docs.adyen.com/api-explorer/balanceplatform-webhooks/1/overview
        type: Documentation
      - url: openapi/configuration-webhooks-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-data-protection-api
    name: Adyen Data Protection API
    tags:
      - Data Protection
      - GDPR
      - Privacy
      - Erasure
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://ca-test.adyen.com
    humanURL: https://docs.adyen.com/development-resources/data-protection-api/
    description: Adyen Data Protection API provides a way for you to process Subject Erasure Requests as mandated in GDPR. Use our API to submit a request to delete shopper's data, including payment details and other related information.
    properties:
      - url: https://docs.adyen.com/development-resources/data-protection-api/
        type: Documentation
      - url: openapi/data-protection-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-disputes-api
    name: Adyen Disputes API
    tags:
      - Disputes
      - Chargebacks
      - Risk Management
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://ca-test.adyen.com
    humanURL: https://docs.adyen.com/risk-management/disputes-api
    description: You can use the Disputes API to automate the dispute handling process so that you can respond to disputes and chargebacks as soon as they are initiated. The Disputes API lets you retrieve defense reasons, supply and delete defense documents, and accept or defend disputes.
    properties:
      - url: https://docs.adyen.com/risk-management/disputes-api
        type: Documentation
      - url: openapi/disputes-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-funds-api
    name: Adyen Funds API
    tags:
      - Funds
      - Transfers
      - Marketplaces
      - Payouts
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://cal-test.adyen.com
    humanURL: https://docs.adyen.com/marketplaces-and-platforms/classic/fund-transfer/
    description: The Fund API provides endpoints for managing the funds in the accounts on your platform. These management operations include, for example, the transfer of funds from one account to another, the payout of funds to an account holder, and the retrieval of balances in an account.
    properties:
      - url: https://docs.adyen.com/marketplaces-and-platforms/classic/fund-transfer/
        type: Documentation
      - url: openapi/funds-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-hosted-onboarding-api
    name: Adyen Hosted Onboarding API
    tags:
      - Onboarding
      - Verification
      - Marketplaces
      - KYC
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://cal-test.adyen.com
    humanURL: https://docs.adyen.com/marketplaces-and-platforms/collect-verification-details/hosted/
    description: The Hosted Onboarding API provides endpoints for managing the hosted onboarding experience for account holders, allowing you to collect verification details through Adyen's hosted pages.
    properties:
      - url: https://docs.adyen.com/marketplaces-and-platforms/collect-verification-details/hosted/
        type: Documentation
      - url: openapi/hosted-onboarding-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-legal-entity-api
    name: Adyen Legal Entity API
    tags:
      - Legal Entity
      - Verification
      - KYC
      - Compliance
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://kyc-test.adyen.com
    humanURL: https://docs.adyen.com/marketplaces-and-platforms/legal-entity-management-api/
    description: The Legal Entity Management API enables you to manage legal entities that contain information required for verification.
    properties:
      - url: https://docs.adyen.com/marketplaces-and-platforms/legal-entity-management-api/
        type: Documentation
      - url: openapi/legal-entity-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-management-api
    name: Adyen Management API
    tags:
      - Management
      - Merchants
      - Terminals
      - Configuration
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://management-test.adyen.com
    humanURL: https://docs.adyen.com/api-explorer/Management/3/overview
    description: Configure and manage your Adyen company and merchant accounts, stores, and payment terminals.
    properties:
      - url: https://docs.adyen.com/api-explorer/Management/3/overview
        type: Documentation
      - url: openapi/management-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-management-webhooks-api
    name: Adyen Management Webhooks API
    tags:
      - Management
      - Webhooks
      - Merchants
      - Terminals
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://management-test.adyen.com
    humanURL: https://docs.adyen.com/api-explorer/management-webhooks/3/overview
    description: Adyen uses webhooks to inform your system about events that happen with your Adyen company and merchant accounts, stores, payment terminals, and payment methods when using Management API.
    properties:
      - url: https://docs.adyen.com/api-explorer/management-webhooks/3/overview
        type: Documentation
      - url: openapi/management-webhooks-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-notification-configuration-api
    name: Adyen Notification Configuration API
    tags:
      - Notifications
      - Configuration
      - Webhooks
      - Marketplaces
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://cal-test.adyen.com
    humanURL: https://docs.adyen.com/marketplaces-and-platforms/classic/notifications
    description: The Notification Configuration API is used for the classic integration to configure notification subscriptions, endpoints, and settings.
    properties:
      - url: https://docs.adyen.com/marketplaces-and-platforms/classic/notifications
        type: Documentation
      - url: openapi/notification-configurations-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-notification-webhooks-api
    name: Adyen Notification Webhooks API
    tags:
      - Notifications
      - Webhooks
      - Point of Sale
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://cal-test.adyen.com
    humanURL: https://docs.adyen.com/point-of-sale/design-your-integration/notifications/
    description: Adyen sends notifications through webhooks to inform your system about events that occur in the balance platform. These events include, for example, a card user making a payment, or a merchant starting a refund.
    properties:
      - url: https://docs.adyen.com/point-of-sale/design-your-integration/notifications/
        type: Documentation
      - url: openapi/notification-webhooks-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-notifications-api
    name: Adyen Notifications API
    tags:
      - Notifications
      - Webhooks
      - Marketplaces
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://cal-test.adyen.com
    humanURL: https://docs.adyen.com/marketplaces-and-platforms/classic/notifications
    description: The Notification API sends notifications to the endpoints specified in a given subscription. Subscriptions are managed through the Notification Configuration API.
    properties:
      - url: https://docs.adyen.com/marketplaces-and-platforms/classic/notifications
        type: Documentation
      - url: openapi/notifications-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-payments-api
    name: Adyen Payments API
    tags:
      - Payments
      - Cards
      - 3D Secure
      - Tokenization
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://pal-test.adyen.com
    humanURL: https://docs.adyen.com/online-payments/
    description: A set of API endpoints that allow you to initiate, settle, and modify payments on the Adyen payments platform. You can use the API to accept card payments (including One-Click and 3D Secure), bank transfers, ewallets, and many other payment methods.
    properties:
      - url: https://docs.adyen.com/online-payments/
        type: Documentation
      - url: openapi/payments-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-payouts-api
    name: Adyen Payouts API
    tags:
      - Payouts
      - Transfers
      - Online Payments
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://pal-test.adyen.com
    humanURL: https://docs.adyen.com/online-payments/online-payouts
    description: A set of API endpoints that allow you to store payout details, confirm, or decline a payout. For more information, refer to Online payouts.
    properties:
      - url: https://docs.adyen.com/online-payments/online-payouts
        type: Documentation
      - url: openapi/payouts-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-pos-terminal-api
    name: Adyen POS Terminal API
    tags:
      - Point of Sale
      - Terminals
      - In-Person Payments
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://management-test.adyen.com
    humanURL: https://docs.adyen.com/point-of-sale/design-your-integration/terminal-api/
    description: This API provides endpoints for managing your point-of-sale (POS) payment terminals. You can use the API to obtain information about a specific terminal, retrieve overviews of your terminals and stores, and assign terminals to a merchant account or store.
    properties:
      - url: https://docs.adyen.com/point-of-sale/design-your-integration/terminal-api/
        type: Documentation
      - url: openapi/pos-terminal-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-recurring-api
    name: Adyen Recurring API
    tags:
      - Recurring
      - Tokenization
      - Stored Payment Methods
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://pal-test.adyen.com
    humanURL: https://docs.adyen.com/online-payments/tokenization
    description: The Recurring APIs allow you to manage and remove your tokens or saved payment details. Tokens should be created with validation during a payment request.
    properties:
      - url: https://docs.adyen.com/online-payments/tokenization
        type: Documentation
      - url: openapi/recurring-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-report-webhooks-api
    name: Adyen Report Webhooks API
    tags:
      - Reports
      - Webhooks
      - Balance Platform
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://balanceplatform-api-test.adyen.com
    humanURL: https://docs.adyen.com/api-explorer/report-webhooks/1/overview
    description: Adyen sends webhooks to inform your system that reports were generated and are ready to be downloaded. You can download reports programmatically by making an HTTP GET request.
    properties:
      - url: https://docs.adyen.com/api-explorer/report-webhooks/1/overview
        type: Documentation
      - url: openapi/report-webhooks-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-stored-value-api
    name: Adyen Stored Value API
    tags:
      - Stored Value
      - Gift Cards
      - Loyalty
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://pal-test.adyen.com
    humanURL: https://docs.adyen.com/payment-methods/gift-cards/stored-value-api/
    description: A set of API endpoints to manage stored value products.
    properties:
      - url: https://docs.adyen.com/payment-methods/gift-cards/stored-value-api/
        type: Documentation
      - url: openapi/stored-value-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-terminal-api
    name: Adyen Terminal API
    tags:
      - Terminal
      - Point of Sale
      - In-Person Payments
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://terminal-api-test.adyen.com
    humanURL: https://docs.adyen.com/point-of-sale/design-your-integration/terminal-api/terminal-api-reference/
    description: The Adyen Terminal API lets you make payments, issue refunds, collect shopper information, and perform other shopper-terminal interactions using a payment terminal supplied by Adyen.
    properties:
      - url: https://docs.adyen.com/point-of-sale/design-your-integration/terminal-api/terminal-api-reference/
        type: Documentation
      - url: openapi/terminal-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-test-cards-api
    name: Adyen Test Cards API
    tags:
      - Testing
      - Test Cards
      - Development
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://ca-test.adyen.com
    humanURL: https://docs.adyen.com/development-resources/testing/create-test-cards
    description: The Test Cards API provides endpoints for generating custom test card numbers. For more information, refer to Custom test cards documentation.
    properties:
      - url: https://docs.adyen.com/development-resources/testing/create-test-cards
        type: Documentation
      - url: openapi/test-cards-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-transaction-webhooks-api
    name: Adyen Transaction Webhooks API
    tags:
      - Transactions
      - Webhooks
      - Marketplaces
      - Business Accounts
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://balanceplatform-api-test.adyen.com
    humanURL: https://docs.adyen.com/marketplaces-and-platforms/business-accounts/transactions/transaction-webhooks/
    description: Adyen sends webhooks to inform your system about incoming and outgoing transfers in your platform. You can use these webhooks to build your implementation. For example, you can use this information to update balances in your own dashboards or to keep track of incoming funds.
    properties:
      - url: https://docs.adyen.com/marketplaces-and-platforms/business-accounts/transactions/transaction-webhooks/
        type: Documentation
      - url: openapi/transaction-webhooks-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-transfer-webhooks-api
    name: Adyen Transfer Webhooks API
    tags:
      - Transfers
      - Webhooks
      - Balance Platform
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://balanceplatform-api-test.adyen.com
    humanURL: https://docs.adyen.com/api-explorer/transfer-webhooks/3/overview
    description: Adyen sends webhooks to inform your system about incoming and outgoing transfers in your platform. You can use these webhooks to build your implementation. For example, you can use this information to update balances in your own dashboards or to keep track of incoming funds.
    properties:
      - url: https://docs.adyen.com/api-explorer/transfer-webhooks/3/overview
        type: Documentation
      - url: openapi/transfer-webhooks-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-transfers-api
    name: Adyen Transfers API
    tags:
      - Transfers
      - Payouts
      - Balance Platform
      - Marketplaces
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://balanceplatform-api-test.adyen.com
    humanURL: https://docs.adyen.com/marketplaces-and-platforms/payout-to-users/on-demand-payouts
    description: This API provides endpoints that you can use to transfer funds, whether when paying out to a transfer instrument, sending funds to third parties for users with business bank accounts, or to request a payout for a grant offer.
    properties:
      - url: https://docs.adyen.com/marketplaces-and-platforms/payout-to-users/on-demand-payouts
        type: Documentation
      - url: openapi/transfers-openapi-original.yml
        type: OpenAPI
  - aid: adyen:adyen-webhooks-api
    name: Adyen Webhooks API
    tags:
      - Webhooks
      - Notifications
      - Events
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://pal-test.adyen.com
    humanURL: https://docs.adyen.com/development-resources/webhooks
    description: We use webhooks to send you updates about payment status updates, newly available reports, and other events that you can subscribe to.
    properties:
      - url: https://docs.adyen.com/development-resources/webhooks
        type: Documentation
      - url: openapi/webhooks-openapi-original.yml
        type: OpenAPI
common:
  - url: https://www.adyen.com/legal/terms-and-conditions
    type: TermsOfService
  - url: https://www.adyen.com/policies-and-disclaimer/privacy-policy
    type: PrivacyPolicy
  - url: https://docs.adyen.com/development-resources/api-credentials
    type: Authentication
  - url: https://www.adyen.com/pricing
    type: Pricing
  - url: https://docs.adyen.com/
    type: Documentation
  - url: https://docs.adyen.com/get-started-with-adyen/
    type: GettingStarted
  - url: https://www.adyen.com/knowledge-hub
    type: Blog
  - url: https://authn-live.adyen.com/authn/ui/login
    type: Login
  - url: https://ca-test.adyen.com
    type: Sandbox
  - url: https://help.adyen.com/en_US
    type: Support
  - url: https://help.adyen.com/en_US/contact
    type: Contact
  - url: https://help.adyen.com/en_US/academy/webinars
    type: Webinars
  - url: https://status.adyen.com
    type: StatusPage
  - url: https://docs.adyen.com/development-resources/release-notes
    type: ReleaseNotes
  - url: https://github.com/Adyen
    type: GitHubOrganization
  - url: https://github.com/Adyen/adyen-openapi
    type: GitHubRepository
  - url: https://www.adyen.com/newsletter
    type: Newsletter
  - url: https://stackoverflow.com/questions/tagged/adyen
    type: StackOverflow
  - url: https://github.com/Adyen/adyen-web
    type: SDK
    title: Web SDK
  - url: https://github.com/Adyen/adyen-ios
    type: SDK
    title: iOS SDK
  - url: https://github.com/Adyen/adyen-android
    type: SDK
    title: Android SDK
  - url: https://github.com/Adyen/adyen-react-native
    type: SDK
    title: React Native SDK
  - url: https://github.com/Adyen/adyen-flutter
    type: SDK
    title: Flutter SDK
  - url: https://github.com/Adyen/adyen-php-api-library
    type: SDK
    title: PHP SDK
  - url: https://github.com/Adyen/adyen-java-api-library
    type: SDK
    title: Java SDK
  - url: https://github.com/Adyen/adyen-node-api-library
    type: SDK
    title: Node.js SDK
  - url: https://github.com/Adyen/adyen-dotnet-api-library
    type: SDK
    title: .NET SDK
  - url: https://github.com/Adyen/adyen-go-api-library
    type: SDK
    title: Go SDK
  - url: https://github.com/Adyen/adyen-python-api-library
    type: SDK
    title: Python SDK
  - url: https://github.com/Adyen/adyen-ruby-api-library
    type: SDK
    title: Ruby SDK
  - url: https://github.com/Adyen/adyen-apex-api-library
    type: SDK
    title: Apex SDK
  - url: https://github.com/Adyen/adyen-mcp
    type: Tools
    title: MCP Server
  - url: https://github.com/Adyen/adyen-postman
    type: Tools
    title: Postman Collection
  - type: Features
    data:
      - $0.13 fixed processing fee per transaction (no setup/monthly fees)
      - 'Visa/Mastercard: $0.13 + Interchange++ + 0.60%'
      - 'PayPal: $0.13 + direct contract + management fee'
      - 'Klarna: $0.13 + 0.99%-4.99% + currency-specific fees'
      - 'Affirm: $0.13 + 4.19%-5.19% + $0.30'
      - 100 RPS API rate limit per merchant
      - Single integration for 100+ payment methods
      - Interchange++ transparent pricing
      - Flexible payout timing and currency
      - REST API for Payments, Recurring, Modifications
      - Webhooks for transaction events
      - Adyen Drop-In and Components for UI
      - Risk and Revenue Accelerate add-ons
      - Capital and Issuing for embedded finance
      - POS terminals (hardware separate)
      - Custom enterprise contracts with volume discounts
    sources:
      - https://www.adyen.com/pricing
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: Online Checkout
        description: Accept payments on web and mobile with Drop-in or Components, supporting all major payment methods and currencies.
      - name: Point-of-Sale Payments
        description: Process in-person payments using Adyen's Terminal API and supported payment terminals with tap, dip, and swipe capabilities.
      - name: Subscription and Recurring Billing
        description: Manage recurring payments and subscriptions using stored payment methods and tokenization.
      - name: Marketplace and Platform Payouts
        description: Onboard sub-merchants, split payments, and manage payouts to sellers and service providers on marketplace platforms.
      - name: Buy Now Pay Later
        description: Offer BNPL options including Affirm, Afterpay, and Klarna to shoppers at checkout to increase conversion.
      - name: Gift Cards and Stored Value
        description: Issue and manage gift cards and stored value products with balance inquiry, load, and redemption capabilities.
      - name: Dispute and Chargeback Management
        description: Automate dispute handling processes to respond to chargebacks with defense documents and evidence.
      - name: GDPR Data Erasure
        description: Process subject erasure requests to comply with GDPR right-to-be-forgotten requirements for shopper data.
  - url: rules/adyen-spectral-rules.yml
    type: SpectralRules
  - url: vocabulary/adyen-vocabulary.yaml
    type: Vocabulary
  - url: capabilities/online-payment-processing.yaml
    type: NaftikoCapability
    title: Online Payment Processing
  - url: capabilities/merchant-account-management.yaml
    type: NaftikoCapability
    title: Merchant Account Management
  - url: capabilities/balance-platform.yaml
    type: NaftikoCapability
    title: Balance Platform
  - type: Integrations
    data:
      - name: Adobe Commerce (Magento)
        description: Pre-built plugin for Adobe Commerce and Magento e-commerce platforms with full payment method support.
      - name: Salesforce Commerce Cloud
        description: Integration with Salesforce Commerce Cloud for seamless payment processing in SFCC storefronts.
      - name: Shopware
        description: Native plugin for Shopware e-commerce platform supporting all Adyen payment methods.
      - name: SAP Commerce Cloud
        description: Integration with SAP Commerce Cloud for enterprise e-commerce payment processing.
      - name: Shopify
        description: Partner integration with Shopify for accepting Adyen payments through Shopify stores.
      - name: NetSuite
        description: Integration with Oracle NetSuite ERP for payment processing and reconciliation.
      - name: PrestaShop
        description: Plugin for PrestaShop e-commerce platform enabling Adyen payment acceptance.
      - name: CommerceTools
        description: Integration with CommerceTools headless commerce platform for flexible payment experiences.
---

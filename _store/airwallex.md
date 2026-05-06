---
aid: airwallex
url: https://raw.githubusercontent.com/api-evangelist/airwallex/refs/heads/main/apis.yml
apis:
  - aid: airwallex:payment-acceptance
    name: Airwallex Payment Acceptance API
    tags:
      - Payments
      - Checkout
      - Cards
      - Online Payments
    humanURL: https://www.airwallex.com/docs/api#/Introduction
    baseURL: https://api.airwallex.com/api/v1
    description: The Airwallex Payment Acceptance API enables businesses to accept online payments globally. Supports credit and debit cards, local payment methods, and 3D Secure. Available as hosted checkout or embedded via Drop-in UI, Payment Elements, and mobile SDKs for iOS, Android, React Native, and Flutter.
    properties:
      - url: https://www.airwallex.com/docs/api#/Introduction
        type: Documentation
      - url: https://www.airwallex.com/docs/api#/Payment_Acceptance
        type: APIReference
      - url: https://www.airwallex.com/docs/api#/Payment_Acceptance/Authentication
        type: Authentication
      - url: https://github.com/airwallex/airwallex-payment-android
        type: SDK
        title: Android SDK
      - url: https://github.com/airwallex/airwallex-payment-ios
        type: SDK
        title: iOS SDK
      - url: https://github.com/airwallex/airwallex-payment-react-native
        type: SDK
        title: React Native SDK
      - url: https://github.com/airwallex/airwallex-payment-flutter
        type: SDK
        title: Flutter SDK
  - aid: airwallex:global-accounts
    name: Airwallex Global Accounts API
    tags:
      - Accounts
      - Multi-Currency
      - Banking
      - FX
    humanURL: https://www.airwallex.com/docs/api#/Accounts
    baseURL: https://api.airwallex.com/api/v1
    description: The Airwallex Global Accounts API enables businesses to create and manage multi-currency accounts. Supports account creation, balance management, account statements, and receiving funds in multiple currencies with local bank details.
    properties:
      - url: https://www.airwallex.com/docs/api#/Accounts
        type: Documentation
      - url: https://www.airwallex.com/docs/api#/Accounts
        type: APIReference
  - aid: airwallex:payouts
    name: Airwallex Payouts API
    tags:
      - Payouts
      - Cross-Border Payments
      - Transfers
      - International
    humanURL: https://www.airwallex.com/docs/api#/Payouts
    baseURL: https://api.airwallex.com/api/v1
    description: The Airwallex Payouts API enables businesses to send cross-border payments to suppliers, contractors, and employees globally. Supports bank transfers to 150+ countries, bulk payouts, and beneficiary management.
    properties:
      - url: https://www.airwallex.com/docs/api#/Payouts
        type: Documentation
      - url: https://www.airwallex.com/docs/api#/Payouts
        type: APIReference
      - url: https://github.com/airwallex/payouts-web-sdk
        type: SDK
        title: Payouts Web SDK
  - aid: airwallex:fx
    name: Airwallex FX API
    tags:
      - Foreign Exchange
      - Currency Conversion
      - FX
    humanURL: https://www.airwallex.com/docs/api#/FX
    baseURL: https://api.airwallex.com/api/v1
    description: The Airwallex FX API provides access to real-time foreign exchange rates and currency conversion. Supports spot conversions, rate quotes, and conversion history for 60+ currencies.
    properties:
      - url: https://www.airwallex.com/docs/api#/FX
        type: Documentation
      - url: https://www.airwallex.com/docs/api#/FX
        type: APIReference
  - aid: airwallex:issuing
    name: Airwallex Issuing API
    tags:
      - Cards
      - Corporate Cards
      - Issuing
      - Expense Management
    humanURL: https://www.airwallex.com/docs/api#/Issuing
    baseURL: https://api.airwallex.com/api/v1
    description: The Airwallex Issuing API enables businesses to create and manage virtual and physical corporate cards for employee spending. Supports card issuance, spend controls, transaction management, and expense reporting.
    properties:
      - url: https://www.airwallex.com/docs/api#/Issuing
        type: Documentation
      - url: https://www.airwallex.com/docs/api#/Issuing
        type: APIReference
  - aid: airwallex:platform
    name: Airwallex Platform API
    tags:
      - Embedded Finance
      - Platform
      - Marketplace
      - Split Payments
    humanURL: https://www.airwallex.com/docs/api#/Platform
    baseURL: https://api.airwallex.com/api/v1
    description: The Airwallex Platform API enables businesses to embed financial services into their products. Supports merchant onboarding, sub-account management, platform payments, and split payouts for marketplace and SaaS platforms.
    properties:
      - url: https://www.airwallex.com/docs/api#/Platform
        type: Documentation
      - url: https://www.airwallex.com/docs/api#/Platform
        type: APIReference
      - url: https://github.com/airwallex/platform-onboarding-sdk
        type: SDK
        title: Platform Onboarding SDK
name: Airwallex
tags:
  - Cross-Border Payments
  - FinTech
  - Foreign Exchange
  - Payments
  - Global
  - Embedded Finance
  - Multi-Currency
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-17'
modified: '2026-04-19'
position: Consumer
description: Airwallex is a financial technology company that specializes in providing global payment solutions for businesses. Their platform enables companies to accept payments, manage multi-currency accounts, convert currencies at competitive rates, send cross-border payments, issue corporate cards, and embed financial services into their own products. Airwallex serves businesses in over 150 countries with APIs for payment acceptance, FX, accounts, transfers, and embedded finance.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - url: https://www.airwallex.com
    type: Portal
  - url: https://www.airwallex.com/docs/api
    type: GettingStarted
  - url: https://www.airwallex.com/docs/api#/Introduction
    type: Documentation
  - url: https://www.airwallex.com/docs/api#/Payment_Acceptance/Authentication
    type: Authentication
  - url: https://www.airwallex.com/pricing
    type: Pricing
  - url: https://www.airwallex.com/terms
    type: TermsOfService
  - url: https://www.airwallex.com/privacy
    type: PrivacyPolicy
  - url: https://www.airwallex.com/blog
    type: Blog
  - url: https://github.com/airwallex
    type: GitHubOrganization
  - url: https://github.com/airwallex/airwallex-cli
    type: CLI
    title: Airwallex CLI
  - url: https://github.com/airwallex/paymentacceptance-plugin-magento
    type: SDK
    title: Magento Plugin
  - url: https://github.com/airwallex/airwallex-salesforce-commerce-cloud-cartridge
    type: SDK
    title: Salesforce Commerce Cloud
  - type: Features
    data:
      - name: Global Payment Acceptance
        description: Accept payments in 180+ currencies via cards and local payment methods.
      - name: Multi-Currency Accounts
        description: Hold, manage, and convert funds in 60+ currencies.
      - name: Cross-Border Payouts
        description: Send payments to 150+ countries with competitive FX rates.
      - name: FX Conversion
        description: Real-time currency conversion at competitive exchange rates.
      - name: Corporate Card Issuing
        description: Issue virtual and physical Visa cards for employee spending.
      - name: Embedded Finance
        description: Embed Airwallex financial services into your own platform.
      - name: Mobile SDKs
        description: iOS, Android, React Native, and Flutter SDKs for in-app payments.
      - name: Webhooks
        description: Real-time event notifications for payment status changes.
      - name: Risk Management
        description: Built-in fraud detection and risk scoring via the Airwallex Risk SDK.
  - type: UseCases
    data:
      - name: E-Commerce Checkout
        description: Accept global payments on e-commerce stores and marketplaces.
      - name: Cross-Border B2B Payments
        description: Pay international suppliers and contractors efficiently.
      - name: Employee Expense Management
        description: Issue cards and track employee spending globally.
      - name: Multi-Currency Treasury
        description: Manage treasury operations across multiple currencies.
      - name: Marketplace Split Payments
        description: Collect and distribute payments to marketplace sellers.
      - name: SaaS Platform Monetization
        description: Embed payment processing into SaaS platforms.
      - name: Freelancer Payouts
        description: Pay remote workers and freelancers in their local currencies.
  - type: Integrations
    data:
      - name: Magento
        description: Airwallex payment plugin for Magento/Adobe Commerce stores.
      - name: Salesforce Commerce Cloud
        description: Airwallex payment cartridge for Salesforce Commerce Cloud.
      - name: WooCommerce
        description: Payment gateway plugin for WooCommerce stores.
      - name: Xero
        description: Sync Airwallex transactions with Xero accounting software.
      - name: QuickBooks
        description: Accounting integration for Airwallex transactions.
      - name: NetSuite
        description: ERP integration for Airwallex payment data.
  - url: https://raw.githubusercontent.com/api-evangelist/airwallex/refs/heads/main/rules/airwallex-spectral-rules.yml
    type: SpectralRules
  - url: https://raw.githubusercontent.com/api-evangelist/airwallex/refs/heads/main/capabilities/payments-management.yaml
    type: NaftikoCapability
  - url: https://raw.githubusercontent.com/api-evangelist/airwallex/refs/heads/main/vocabulary/airwallex-vocabulary.yaml
    type: Vocabulary
---

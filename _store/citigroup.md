---
aid: citigroup
name: Citigroup
url: https://raw.githubusercontent.com/api-evangelist/citigroup/refs/heads/main/apis.yml
created: '2026-03-23'
modified: '2026-04-23'
type: Index
access: 3rd-Party
position: Consumer
specificationVersion: '0.19'
tags:
  - Banking
  - Financial Services
  - FX
  - Open Banking
  - Payments
  - Treasury
description: Citigroup is a global diversified financial services holding company providing consumers, corporations, governments, and institutions with a broad range of financial products and services. Citi exposes its API surface through the Citi Developer Hub, a unified developer portal spanning the bank's retail, commercial, and Treasury and Trade Solutions (TTS) lines of business. Major API domains include CitiConnect for corporate treasury, Accounts and Transactions for retail, Money Movement for payment initiation, Customer Onboarding, Authorization, and utilities for FX rates and reference data. Authentication uses OAuth 2.0 with mutual TLS for production endpoints.
apis:
  - aid: citigroup:citi-accounts-transactions-api
    name: Citi Accounts and Transactions API
    tags:
      - Accounts
      - Balances
      - Banking
      - Statements
      - Transactions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://sandbox.developerhub.citi.com/api/united-states/retail-bank/accounts/accounts-and-transactions/documentation
    properties:
      - url: https://sandbox.developerhub.citi.com/api/united-states/retail-bank/accounts/accounts-and-transactions/documentation
        type: Documentation
    description: The Citi Accounts and Transactions API provides authorized access to retail customer accounts, balances, and transaction histories. Authentication uses OAuth 2.0 access tokens issued through the Citi Developer Hub authorization flow.
  - aid: citigroup:citi-money-movement-api
    name: Citi Money Movement API
    tags:
      - ACH
      - Money Movement
      - Payment Initiation
      - Payments
      - Wire Transfer
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://sandbox.developerhub.citi.com/api-catalog-list
    properties:
      - url: https://sandbox.developerhub.citi.com/api-catalog-list
        type: Documentation
    description: The Citi Money Movement API enables authorized payment initiation from Citi accounts including domestic ACH, wire, and book transfers. Authentication uses OAuth 2.0 with strong customer authentication flows.
  - aid: citigroup:citi-authorize-api
    name: Citi Authorize API
    tags:
      - Authorization
      - Consent
      - OAuth
      - SCA
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.citi.com/
    properties:
      - url: https://developer.citi.com/
        type: Documentation
    description: The Citi Authorize API handles the OAuth 2.0 authorization-code and consent flows required for third-party applications to access a customer's Citi account data and initiate payments.
  - aid: citigroup:citi-customers-api
    name: Citi Customers API
    tags:
      - Customers
      - Identity
      - KYC
      - Profiles
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.citi.com/
    properties:
      - url: https://developer.citi.com/
        type: Documentation
    description: The Citi Customers API provides authorized access to customer profile information including contact details and demographic data for use in onboarding and KYC workflows.
  - aid: citigroup:citi-onboarding-api
    name: Citi Onboarding API
    tags:
      - Account Opening
      - Customer Onboarding
      - KYC
      - Origination
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.citi.com/
    properties:
      - url: https://developer.citi.com/
        type: Documentation
    description: The Citi Onboarding API enables digital account opening, document submission, and KYC workflows for onboarding new retail customers to Citi products.
  - aid: citigroup:citi-pay-with-points-api
    name: Citi Pay with Points API
    tags:
      - Loyalty
      - Pay with Points
      - Rewards
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.citi.com/
    properties:
      - url: https://developer.citi.com/
        type: Documentation
    description: The Citi Pay with Points API enables Citi cardholders to redeem ThankYou points and other rewards for purchases at merchant checkouts and inside partner applications.
  - aid: citigroup:citi-utilities-api
    name: Citi Utilities API
    tags:
      - FX Rates
      - Locator
      - Reference Data
      - Utilities
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.citi.com/
    properties:
      - url: https://developer.citi.com/
        type: Documentation
    description: The Citi Utilities API provides reference data such as FX rates, branch and ATM locators, and cut-off times used to support transactional workflows across Citi's retail and commercial offerings.
  - aid: citigroup:citiconnect-api
    name: CitiConnect API
    tags:
      - CitiConnect
      - Corporate Banking
      - ERP Integration
      - Treasury
      - TTS
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.citigroup.com/global/insights/citiconnect-api-portal
    properties:
      - url: https://www.citigroup.com/global/insights/citiconnect-api-portal
        type: Documentation
    description: CitiConnect is the corporate treasury and trade integration channel that exposes APIs for real-time payments, FX, statements, direct debits, faster payments, and proof-of-payment for enterprise clients connecting through ERP and TMS systems.
common:
  - type: Website
    url: https://www.citigroup.com
  - type: Portal
    url: https://developer.citi.com/
  - type: Sandbox
    url: https://sandbox.developerhub.citi.com/
  - type: API Catalog
    url: https://sandbox.developerhub.citi.com/api-catalog-list
  - type: CitiConnect
    url: https://www.citigroup.com/global/insights/citiconnect-api-portal
  - type: Documentation
    url: https://developer.citi.com/
  - type: Investor Relations
    url: https://www.citigroup.com/global/investors
  - type: Privacy Policy
    url: https://online.citi.com/US/JRS/pands/detail.do?ID=PrivacyTerms
  - type: Terms of Service
    url: https://online.citi.com/US/JRS/pands/detail.do?ID=Terms
  - type: Security
    url: https://online.citi.com/US/JRS/pands/detail.do?ID=PrivacyTerms
  - type: Support
    url: https://online.citi.com/US/contactus.htm
  - type: JSON-LD
    url: json-ld/citigroup-context.jsonld
  - type: Spectral
    url: rules/citigroup-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/citigroup-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

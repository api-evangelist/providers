---
aid: envestnet
name: Envestnet
description: Envestnet is an ever-evolving network of data-driven services, products, tools, and technologies designed to enable the Intelligent Financial Life. Our robust financial wellness ecosystem offers solutions for every role in the financial advice industry, including the Yodlee account aggregation, verification, credit, insights, and personalized view APIs.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Financial
  - Wealth Management
  - Open Banking
  - Account Aggregation
url: https://raw.githubusercontent.com/api-evangelist/envestnet/refs/heads/main/apis.yml
created: '2023-11-20'
modified: '2026-04-28'
specificationVersion: '0.19'
position: Consumer
access: 3rd-Party
apis:
  - aid: envestnet:envestnet-account-aggregation-api
    name: Envestnet Account Aggregation API
    description: Aggregation APIs give you the power to access accounts at most institutions in the industry, combined with the industry's best data enrichment augmented by powerful AI-driven data analysis, all from a single open-banking-ready platform.
    humanURL: https://developer.envestnet.com/products/yodlee/account-aggregation
    tags:
      - Account Aggregation
      - Open Banking
    properties:
      - type: Documentation
        url: https://developer.envestnet.com/products/yodlee/account-aggregation/docs/api-reference
      - type: OpenAPI
        url: openapi/envestnet-account-aggregation-openapi-original.yml
  - aid: envestnet:envestnet-account-token-api
    name: Envestnet Account Token APIs
    description: Financial institutions or FinTech customers using the account verification product to provide digital payment services can eliminate the risk of storing users' sensitive financial account information by using Account Token endpoints. The endpoints allow customers to create an account-specific token that payment processors can use to retrieve account information.
    humanURL: https://developer.envestnet.com/products/yodlee/account-token/docs/api-reference
    tags:
      - Account Token
      - Payments
    properties:
      - type: Documentation
        url: https://developer.envestnet.com/products/yodlee/account-token/docs/api-reference
      - type: OpenAPI
        url: openapi/envestnet-account-token-openapi-original.yml
  - aid: envestnet:envestnet-account-verification-api
    name: Envestnet Account Verification APIs
    description: Verifying an account using Yodlee enables payments, helps avoid overdrafts, reduces fraud, and more. Verification means your user has authenticated against the account and yields detailed information for the problem you're trying to solve, such as routing number lookup and balance verification.
    humanURL: https://developer.envestnet.com/products/yodlee/account-verification/docs
    tags:
      - Verification
      - Payments
    properties:
      - type: Documentation
        url: https://developer.envestnet.com/products/yodlee/account-verification/docs
      - type: OpenAPI
        url: openapi/envestnet-verification-openapi-original.yml
  - aid: envestnet:envestnet-credit-accelerator-api
    name: Envestnet Credit Accelerator API
    description: The Envestnet D&A Credit LLC Credit Accelerator solution allows consumers to link their accounts across financial institutions and generate a Credit Accelerator File for use in loan underwriting or another credit review and approval process.
    humanURL: https://developer.envestnet.com/resources/yodlee/credit-accelerator/docs/api-reference
    tags:
      - Credit
      - Underwriting
    properties:
      - type: Documentation
        url: https://developer.envestnet.com/resources/yodlee/credit-accelerator/docs/api-reference
      - type: OpenAPI
        url: openapi/envestnet-credit-accelerator-openapi-original.yml
  - aid: envestnet:envestnet-insights-api
    name: Envestnet Insights API
    description: Financial Insights APIs provide intelligent, personalized, and actionable insights to your end-users. This product details the APIs offered as part of the insights product.
    humanURL: https://developer.envestnet.com/products/yodlee/insights/docs/api-reference
    tags:
      - Insights
      - Personalization
    properties:
      - type: Documentation
        url: https://developer.envestnet.com/products/yodlee/insights/docs/api-reference
      - type: OpenAPI
        url: openapi/envestnet-insights-openapi-original.yml
  - aid: envestnet:envestnet-personalized-view-api
    name: Envestnet Personalized View API
    description: Views APIs enable end users to create personalized views of their finances for any expenses, hobbies, or projects relevant to them. A view is a collection of transactions based on rules across any combination of accounts, categories, merchants, locations, transaction types, and more, that are of interest to your users.
    humanURL: https://developer.envestnet.com/products/yodlee/personalized-views/docs/api-reference
    tags:
      - Personalized Views
      - Transactions
    properties:
      - type: Documentation
        url: https://developer.envestnet.com/products/yodlee/personalized-views/docs/api-reference
      - type: OpenAPI
        url: openapi/envestnet-personalized-views-openapi-original.yml
common:
  - type: Website
    url: https://www.envestnet.com/
  - type: Developer Portal
    url: https://developer.envestnet.com/
  - type: Use Cases
    url: https://developer.envestnet.com/use-cases
  - type: Releases
    url: https://developer.envestnet.com/resources?type=release
  - type: Blog
    url: https://developer.envestnet.com/resources?type=blog
  - type: Events
    url: https://developer.envestnet.com/resources?type=events
  - type: Contact
    url: https://developer.envestnet.com/contact-us
  - type: Press
    url: https://www.envestnet.com/press
  - type: PrivacyPolicy
    url: https://www.envestnet.com/privacy
  - type: TermsOfService
    url: https://www.envestnet.com/legal
  - type: LinkedIn
    url: https://www.linkedin.com/company/envestnet/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

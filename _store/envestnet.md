---
aid: envestnet
url: https://raw.githubusercontent.com/apis-json/artisanal/main/apis/envestnet.yml
apis:
  - aid: envestnet:evestnet-account-aggregation-api
    name: Envestnet Account Aggregation API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.envestnet.com/products/yodlee/account-aggregation
    properties:
      - url: >-
          https://developer.envestnet.com/products/yodlee/account-aggregation/docs/api-reference
        type: Documentation
      - url: properties/envestnet-account-aggregation-openapi-original.yml
        type: OpenAPI
    description: >-
      Our Aggregation APIs give you the power to access accounts at most
      institutions in the industry combined with the industry's best data
      enrichment augmented by powerful AI-driven data analysis, all from a
      single open-banking-ready platform.
  - aid: envestnet:evestnet-account-token-api
    name: Envestnet Account Token APIs
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: >-
      https://developer.envestnet.com/products/yodlee/account-token/docs/api-reference
    properties:
      - url: >-
          https://developer.envestnet.com/products/yodlee/account-token/docs/api-reference
        type: Documentation
      - url: properties/envestnet-account-token-openapi-original.yml
        type: OpenAPI
    description: >-
      Financial institutions (FIs) or FinTech customers using the account
      verification product to provide digital payment services can eliminate the
      risk of storing users' sensitive financial account information using
      Account Token endpoints. The endpoints allow customers to create an
      account-specific token that the payment processors can use to retrieve
      account information.
  - aid: envestnet:evestnet-account-verification-api
    name: Envestnet Account Verification APIs
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.envestnet.com/products/yodlee/account-verification/docs
    properties:
      - url: >-
          https://developer.envestnet.com/products/yodlee/account-verification/docs
        type: Documentation
      - url: properties/envestnet-verification-openapi-original.yml
        type: OpenAPI
    description: >-
      This guide will show the basics of verifying accounts using Yodlee.
      Account verification can help enable payments, avoid overdrafts, reduce
      fraud, and more.  Verifying an account simply means your user has
      authenticated against the account, and then you get detailed information
      for the problem you're trying to solve. For instance, for payments, you
      might want to prove a user has access to an account, get the account
      routing number, and check the amount of money in it.
  - aid: envestnet:evestnet-credit-accelerator-api
    name: Envestnet Credit Accelerator API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: >-
      https://developer.envestnet.com/resources/yodlee/credit-accelerator/docs/api-reference
    properties:
      - url: >-
          https://developer.envestnet.com/resources/yodlee/credit-accelerator/docs/api-reference
        type: Documentation
      - url: properties/envestnet-credit-accelerator-openapi-original.yml
        type: OpenAPI
    description: >-
      The Envestnet D&A Credit LLC Credit Accelerator solution allows consumers
      to link their accounts across financial institution(s) and generate a
      Credit Accelerator File for use in loan underwriting or another credit
      review and approval process.
  - aid: envestnet:evestnet-insights-api
    name: Envestnet Insights API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: >-
      https://developer.envestnet.com/products/yodlee/insights/docs/api-reference
    properties:
      - url: >-
          https://developer.envestnet.com/products/yodlee/insights/docs/api-reference
        type: Documentation
      - url: properties/envestnet-insights-openapi-original.yml
        type: OpenAPI
    description: >-
      Financial Insights APIs provide intelligent, personalized, and actionable
      insights to your end-users. This document details the APIs offered as part
      of the insights product.
  - aid: envestnet:evestnet-personalized-view-api
    name: Envestnet Personalized View API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: >-
      https://developer.envestnet.com/products/yodlee/personalized-views/docs/api-reference
    properties:
      - url: >-
          https://developer.envestnet.com/products/yodlee/personalized-views/docs/api-reference
        type: Documentation
      - url: properties/envestnet-personalized-views-openapi-original.yml
        type: OpenAPI
    description: >-
      Views APIs enable your end users to create personalized views of their
      finances for any expenses, hobbies, or projects relevant to them. A view
      is a collection of transactions based on rules - any combination of
      accounts, categories, merchants, locations, transaction types, and more,
      that are of interest to your users. Build preconfigured views and let your
      users further define them with a flexible user experience. This document
      details the APIs offered as part of the views product.
name: Envestnet
tags: []
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
common:
  - url: https://developer.envestnet.com/use-cases
    type: Use Cases
  - url: https://developer.envestnet.com/resources?type=release
    type: Releases
  - url: https://developer.envestnet.com/resources?type=blog
    type: Blog
  - url: https://developer.envestnet.com/resources?type=events
    type: Events
  - url: https://developer.envestnet.com/contact-us
    type: Contact
  - url: https://www.envestnet.com/press
    type: Press
  - url: https://www.envestnet.com/privacy
    type: Privacy Policy
  - url: https://example.comhttps://www.envestnet.com/legal
    type: Terms of Service
  - url: https://www.linkedin.com/company/envestnet/
    type: LinkedIn
created: '2023-11-20T00:00:00.000Z'
modified: '2024-06-07T00:00:00.000Z'
overlays:
  - url: overlays/apis-io-search.yml
    type: APIs.io Search
  - url: overlays/apis-io-search.yml
    type: API Evangelist Ratings
description: >-
  Envestnet is an ever-evolving network of data-driven services, products,
  tools, and technologies designed to enable the Intelligent Financial Life_.
  Our robust financial wellness ecosystem offers solutions for every role in the
  financial advice industry. Supercharge practice growth and enable financial
  wellness.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.18'
---
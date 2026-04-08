---
aid: amazon
url: https://raw.githubusercontent.com/api-evangelist/amazon/refs/heads/main/apis.yml
apis:
- aid: amazon:selling-partner-api
  name: Amazon Selling Partner API
  tags:
  - E-Commerce
  - Fulfillment
  - Marketplace
  - Orders
  - Sellers
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://sellingpartnerapi-na.amazon.com
  humanURL: https://developer-docs.amazon.com/sp-api
  properties:
  - url: https://developer-docs.amazon.com/sp-api
    type: Documentation
  - url: openapi/amazon-selling-partner-api-openapi.yml
    type: OpenAPI
  description: The Amazon Selling Partner API (SP-API) is a RESTful API that enables Amazon sellers and vendors to programmatically manage their marketplace operations including listings, orders, payments, reports, and fulfillment. It replaces the deprecated Amazon Marketplace Web Service (MWS) and provides access to region-specific endpoints for North America, Europe, and Far East marketplaces. The API supports operations for catalog items, inventory management, shipping, and financial reporting.
- aid: amazon:advertising-api
  name: Amazon Advertising API
  tags:
  - Advertising
  - Campaigns
  - Marketing
  - Sponsored Products
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://advertising-api.amazon.com
  humanURL: https://advertising.amazon.com/API/docs/en-us/reference/api-overview
  properties:
  - url: https://advertising.amazon.com/API/docs/en-us/reference/api-overview
    type: Documentation
  - url: openapi/amazon-advertising-api-openapi.yml
    type: OpenAPI
  description: The Amazon Advertising API enables programmatic management of advertising campaigns on Amazon. It provides access to Sponsored Products, Sponsored Brands, and Sponsored Display campaigns across various marketplaces. Developers can create, manage, and optimize advertising campaigns, access reporting data, and manage budgets and targeting through this REST API.
- aid: amazon:product-advertising-api
  name: Amazon Product Advertising API
  tags:
  - Affiliates
  - E-Commerce
  - Products
  - Search
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://webservices.amazon.com/paapi5
  humanURL: https://webservices.amazon.com/paapi5/documentation/
  properties:
  - url: https://webservices.amazon.com/paapi5/documentation/
    type: Documentation
  description: The Amazon Product Advertising API (PA-API) v5.0 allows affiliates and publishers to display Amazon product information and prices on their websites and mobile apps. It provides access to product search, item lookup, browse node navigation, and cart operations. Note that this API is being deprecated in April 2026 in favor of the Amazon Creators API.
- aid: amazon:creators-api
  name: Amazon Creators API
  tags:
  - Affiliates
  - Content Creators
  - E-Commerce
  - Products
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://affiliate-program.amazon.com/creatorsapi
  humanURL: https://affiliate-program.amazon.com/creatorsapi/docs/en-us/introduction
  properties:
  - url: https://affiliate-program.amazon.com/creatorsapi/docs/en-us/introduction
    type: Documentation
  description: The Amazon Creators API is a modern REST-based API providing programmatic access to Amazon product data for publishers, influencers, and affiliate partners. It is the recommended replacement for the Product Advertising API and requires Amazon Associates membership with qualifying sales history. The API enables content creators to search and display Amazon product information in their applications and websites.
- aid: amazon:pay-api
  name: Amazon Pay API
  tags:
  - Checkout
  - E-Commerce
  - Payments
  - Subscriptions
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://pay-api.amazon.com
  humanURL: https://developer.amazon.com/docs/amazon-pay-api-v2/introduction.html
  properties:
  - url: https://developer.amazon.com/docs/amazon-pay-api-v2/introduction.html
    type: Documentation
  - url: openapi/amazon-pay-api-openapi.yml
    type: OpenAPI
  description: The Amazon Pay API enables merchants to integrate Amazon Pay for payment processing on their websites and mobile applications. It supports one-time purchases, subscriptions, and recurring payments. The API provides checkout session management, charge operations, and refund capabilities with both production and sandbox environments for testing.
- aid: amazon:alexa-skills-kit-api
  name: Amazon Alexa Skills Kit API
  tags:
  - Alexa
  - Skills
  - Smart Home
  - Voice
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.amazonalexa.com
  humanURL: https://developer.amazon.com/en-US/docs/alexa/rest-apis/rest-apis.html
  properties:
  - url: https://developer.amazon.com/en-US/docs/alexa/rest-apis/rest-apis.html
    type: Documentation
  description: The Alexa Skills Kit (ASK) REST APIs enable developers to create, manage, test, and deploy custom voice skills for Alexa-enabled devices. The APIs include skill manifest management, skill enablement, interaction model building, and hosted skill management. Developers can build voice experiences ranging from simple Q&A to complex multi-turn conversations and smart home device integrations.
- aid: amazon:appstore-api
  name: Amazon Appstore API
  tags:
  - App Store
  - Apps
  - In-App Purchases
  - Mobile
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://developer.amazon.com/api/appstore
  humanURL: https://www.developer.amazon.com/docs/apps-and-games/documentation.html
  properties:
  - url: https://www.developer.amazon.com/docs/apps-and-games/documentation.html
    type: Documentation
  description: The Amazon Appstore Developer APIs provide tools for managing app submissions, testing, and monetization through in-app purchases on the Amazon Appstore. The APIs include app submission workflows, reporting for revenue and promotions, and the In-App Purchasing SDK for implementing digital goods and subscriptions within Android and Fire OS applications.
name: Amazon
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Welcome to Selling Partner API Documentation. Learn how to get started and build applications with Amazon's REST-based SP-API.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


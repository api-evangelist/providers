---
aid: amazon
name: Amazon
description: Amazon is a global technology and e-commerce company offering a wide range of consumer and developer APIs including the Selling Partner API for marketplace sellers, Advertising API for campaign management, Amazon Pay for payments, Alexa Skills Kit for voice experiences, Amazon Appstore for mobile applications, and the Creators API for affiliate publishers. These APIs power Amazon's ecosystem of sellers, developers, advertisers, and content creators.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/amazon/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-05-04'
specificationVersion: '0.19'
tags:
  - Amazon
  - Advertising
  - Alexa
  - E-Commerce
  - Marketplace
  - Payments
  - Voice
apis:
  - aid: amazon:selling-partner-api
    name: Amazon Selling Partner API
    tags:
      - E-Commerce
      - Fulfillment
      - Marketplace
      - Orders
      - Sellers
    humanURL: https://developer-docs.amazon.com/sp-api
    baseURL: https://sellingpartnerapi-na.amazon.com
    properties:
      - type: Documentation
        url: https://developer-docs.amazon.com/sp-api
      - type: OpenAPI
        url: openapi/amazon-selling-partner-api-openapi.yml
      - type: JSONSchema
        url: json-schema/selling-partner-order-schema.json
    description: The Amazon Selling Partner API (SP-API) is a RESTful API that enables Amazon sellers and vendors to programmatically manage their marketplace operations including listings, orders, payments, reports, and fulfillment. It replaces the deprecated Amazon Marketplace Web Service (MWS) and provides access to region-specific endpoints for North America, Europe, and Far East marketplaces.
  - aid: amazon:advertising-api
    name: Amazon Advertising API
    tags:
      - Advertising
      - Campaigns
      - Marketing
      - Sponsored Products
    humanURL: https://advertising.amazon.com/API/docs/en-us/reference/api-overview
    baseURL: https://advertising-api.amazon.com
    properties:
      - type: Documentation
        url: https://advertising.amazon.com/API/docs/en-us/reference/api-overview
      - type: OpenAPI
        url: openapi/amazon-advertising-api-openapi.yml
    description: The Amazon Advertising API enables programmatic management of advertising campaigns on Amazon including Sponsored Products, Sponsored Brands, and Sponsored Display campaigns across various marketplaces. Developers can create, manage, and optimize campaigns, access reporting data, and manage budgets and targeting.
  - aid: amazon:creators-api
    name: Amazon Creators API
    tags:
      - Affiliates
      - Content Creators
      - E-Commerce
      - Products
    humanURL: https://affiliate-program.amazon.com/creatorsapi/docs/en-us/introduction
    baseURL: https://affiliate-program.amazon.com/creatorsapi
    properties:
      - type: Documentation
        url: https://affiliate-program.amazon.com/creatorsapi/docs/en-us/introduction
    description: The Amazon Creators API provides programmatic access to Amazon product data for publishers, influencers, and affiliate partners. It is the recommended replacement for the Product Advertising API and requires Amazon Associates membership with qualifying sales history.
  - aid: amazon:pay-api
    name: Amazon Pay API
    tags:
      - Checkout
      - E-Commerce
      - Payments
      - Subscriptions
    humanURL: https://developer.amazon.com/docs/amazon-pay-api-v2/introduction.html
    baseURL: https://pay-api.amazon.com
    properties:
      - type: Documentation
        url: https://developer.amazon.com/docs/amazon-pay-api-v2/introduction.html
      - type: OpenAPI
        url: openapi/amazon-pay-api-openapi.yml
    description: The Amazon Pay API enables merchants to integrate Amazon Pay for payment processing on their websites and mobile applications. It supports one-time purchases, subscriptions, and recurring payments with checkout session management, charge operations, and refund capabilities.
  - aid: amazon:alexa-skills-kit-api
    name: Amazon Alexa Skills Kit API
    tags:
      - Alexa
      - Skills
      - Smart Home
      - Voice
    humanURL: https://developer.amazon.com/en-US/docs/alexa/rest-apis/rest-apis.html
    baseURL: https://api.amazonalexa.com
    properties:
      - type: Documentation
        url: https://developer.amazon.com/en-US/docs/alexa/rest-apis/rest-apis.html
    description: The Alexa Skills Kit (ASK) REST APIs enable developers to create, manage, test, and deploy custom voice skills for Alexa-enabled devices including skill manifest management, interaction model building, and hosted skill management for voice experiences and smart home integrations.
  - aid: amazon:appstore-api
    name: Amazon Appstore API
    tags:
      - App Store
      - Apps
      - In-App Purchases
      - Mobile
    humanURL: https://www.developer.amazon.com/docs/apps-and-games/documentation.html
    baseURL: https://developer.amazon.com/api/appstore
    properties:
      - type: Documentation
        url: https://www.developer.amazon.com/docs/apps-and-games/documentation.html
    description: The Amazon Appstore Developer APIs provide tools for managing app submissions, testing, and monetization through in-app purchases on the Amazon Appstore for Android and Fire OS applications.
common:
  - type: Portal
    url: https://developer.amazon.com/
  - type: Website
    url: https://www.amazon.com/
  - type: Documentation
    url: https://developer.amazon.com/docs/
  - type: TermsOfService
    url: https://developer.amazon.com/support/legal/da
  - type: PrivacyPolicy
    url: https://www.amazon.com/gp/help/customer/display.html?nodeId=468496
  - type: Support
    url: https://developer.amazon.com/support
  - type: GitHubOrganization
    url: https://github.com/amzn
  - type: Console
    url: https://developer.amazon.com/dashboard
  - type: SignUp
    url: https://www.amazon.com/ap/register?openid.assoc_handle=aws
  - type: Login
    url: https://developer.amazon.com/login
  - type: Blog
    url: https://developer.amazon.com/blogs/
  - type: YouTube
    url: https://www.youtube.com/c/AmazonDeveloper
  - type: Contact
    url: https://www.amazon.com/gp/help/customer/contact-us
  - type: JSONLD
    url: json-ld/amazon-context.jsonld
  - type: SpectralRules
    url: rules/amazon-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-seller-and-commerce.yaml
  - type: Features
    data:
      - 'Amazon (Web Services + Marketplace + Ads): hundreds of services across Cloud + Commerce'
      - 'Detailed pricing: see https://aws.amazon.com/pricing/'
      - 'Service: EC2 (compute)'
      - 'Service: S3 (object storage)'
      - 'Service: EBS (block storage)'
      - 'Service: RDS (managed SQL)'
      - 'Service: DynamoDB (NoSQL)'
      - 'Service: Lambda (serverless)'
      - 'Service: API Gateway'
      - 'Service: CloudFront (CDN)'
      - 'Service: Route 53 (DNS)'
      - 'Service: VPC (networking)'
      - 'Service: IAM (identity)'
      - 'Service: KMS (encryption)'
      - 'Service: Secrets Manager'
      - 'Service: CloudWatch (monitoring)'
      - 'Service: EKS (Kubernetes)'
      - 'Service: ECS (containers)'
      - 'Service: ECR (container registry)'
      - 'Service: SQS (queue)'
      - 'Service: SNS (pub-sub)'
      - 'Service: SES (email)'
      - 'Service: Bedrock (AI/ML)'
      - 'Service: SageMaker (ML)'
      - 'Service: Comprehend (NLP)'
      - 'Service: Rekognition (vision)'
      - 'Service: Polly (TTS)'
      - 'Service: Transcribe (STT)'
      - 'Service: Translate'
      - 'Service: Athena (SQL on S3)'
      - 'Service: Redshift (data warehouse)'
      - 'Service: Glue (ETL)'
      - 'Service: EMR (Hadoop)'
      - 'Service: Kinesis (streaming)'
      - 'Service: MSK (managed Kafka)'
      - 'Service: OpenSearch'
      - 'Service: QuickSight (BI)'
      - 'Service: Amazon Advertising API'
      - 'Service: Amazon Marketplace API'
      - 'Service: Amazon SP API'
      - 'Service: Amazon Pay'
      - 'Service: Amazon Music API'
      - 'Service: Amazon Drive (deprecated)'
    sources:
      - https://aws.amazon.com/pricing/
      - https://focus.finops.org/
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: Marketplace Seller Automation
        description: Automate product listing creation, price updates, inventory management, and order fulfillment for Amazon marketplace sellers.
      - name: Advertising Campaign Optimization
        description: Build automated bid management and campaign optimization tools using the Amazon Advertising API and performance reporting.
      - name: E-Commerce Payment Integration
        description: Add Amazon Pay as a payment option for external e-commerce sites to reduce checkout friction and increase conversion rates.
      - name: Voice Commerce and Smart Home
        description: Create Alexa skills for voice-driven shopping, home automation, and customer service interactions.
      - name: Affiliate Content Monetization
        description: Build product recommendation engines and affiliate content sites using the Creators API for real-time Amazon product data.
  - type: Integrations
    data:
      - name: Amazon MWS Legacy Migration
        description: SP-API is the modern replacement for the deprecated Amazon Marketplace Web Service (MWS) for all seller operations.
      - name: Alexa Smart Home
        description: Integrate smart home devices and services with Alexa voice control using the Smart Home Skill API.
      - name: Login with Amazon
        description: OAuth 2.0 authentication for all Amazon developer APIs including SP-API, Advertising API, and ASK via Login with Amazon (LWA).
      - name: Amazon Associates Program
        description: Affiliate program integration for the Creators API and Product Advertising API for commission-based product promotion.
      - name: Fire OS and Android
        description: Amazon Appstore SDK for Fire OS and Android apps with in-app purchasing and device targeting capabilities.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

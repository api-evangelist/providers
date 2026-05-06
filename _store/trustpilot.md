---
aid: trustpilot
url: https://raw.githubusercontent.com/api-evangelist/trustpilot/refs/heads/main/apis.yml
name: Trustpilot
description: Trustpilot is a global consumer review platform that connects businesses with their customers to build trust through transparent, verified reviews. Founded in 2007, Trustpilot hosts hundreds of millions of reviews across millions of businesses worldwide. The platform offers business APIs that allow companies to collect, manage, and display reviews programmatically, integrate review data into their own systems, and automate invitation workflows to gather customer feedback at scale. Trustpilot's APIs cover business profile management, service reviews, product reviews, invitation management, consumer profiles, and public review data.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Consumer Reviews
  - Reviews
  - Trust
  - Ratings
  - Business Profiles
  - Product Reviews
access: 3rd-Party
created: '2026-03-24'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: trustpilot:trustpilot-business-units-api
    name: Trustpilot Business Units API
    tags:
      - Business Profiles
      - Reviews
      - Trust
      - Ratings
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.trustpilot.com/v1
    humanURL: https://developers.trustpilot.com/business-units-api
    properties:
      - url: https://developers.trustpilot.com/business-units-api
        type: Documentation
      - url: https://developers.trustpilot.com/authentication
        type: Authentication
      - url: https://raw.githubusercontent.com/api-evangelist/trustpilot/refs/heads/main/openapi/trustpilot-business-units-openapi.yml
        type: OpenAPI
    description: The Trustpilot Business Units API provides endpoints to retrieve company profile information, reviews, images, categories, and web links for specific business units on Trustpilot. Developers can search for business units by name, retrieve public and private reviews with filtering options, access business profile images and logos, and list business categories. Public endpoints use API key authentication; private review endpoints require OAuth 2.0.
  - aid: trustpilot:trustpilot-service-reviews-api
    name: Trustpilot Service Reviews API
    tags:
      - Reviews
      - Consumer Reviews
      - Trust
      - Ratings
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.trustpilot.com/v1
    humanURL: https://developers.trustpilot.com/service-reviews-api/
    properties:
      - url: https://developers.trustpilot.com/service-reviews-api/
        type: Documentation
      - url: https://developers.trustpilot.com/authentication
        type: Authentication
      - url: https://raw.githubusercontent.com/api-evangelist/trustpilot/refs/heads/main/openapi/trustpilot-service-reviews-openapi.yml
        type: OpenAPI
    description: The Trustpilot Service Reviews API enables businesses to manage service reviews, including posting replies, managing tags, finding reviewers, and retrieving review details. Businesses can respond to customer reviews, organize reviews with custom tags, and retrieve the latest reviews by language. Most management endpoints require OAuth 2.0 Business user tokens; public review endpoints are accessible with API keys.
  - aid: trustpilot:trustpilot-invitation-api
    name: Trustpilot Invitation API
    tags:
      - Invitations
      - Consumer Reviews
      - Email
      - Reviews
      - Trust
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.trustpilot.com/v1
    humanURL: https://developers.trustpilot.com/invitation-api
    properties:
      - url: https://developers.trustpilot.com/invitation-api
        type: Documentation
      - url: https://developers.trustpilot.com/authentication
        type: Authentication
      - url: https://raw.githubusercontent.com/api-evangelist/trustpilot/refs/heads/main/openapi/trustpilot-invitation-openapi.yml
        type: OpenAPI
    description: The Trustpilot Invitation API allows businesses to programmatically send review invitations to their customers via email or SMS after a transaction or service interaction. It supports creating invitation links, triggering bulk email invitations for service and product reviews, retrieving invitation templates, and deleting invitation data by email or date range. All endpoints require OAuth 2.0 Business user token authentication.
  - aid: trustpilot:trustpilot-product-reviews-api
    name: Trustpilot Product Reviews API
    tags:
      - Product Reviews
      - Reviews
      - Consumer Reviews
      - Trust
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.trustpilot.com/v1
    humanURL: https://developers.trustpilot.com/product-reviews-api/
    properties:
      - url: https://developers.trustpilot.com/product-reviews-api/
        type: Documentation
      - url: https://developers.trustpilot.com/authentication
        type: Authentication
      - url: https://raw.githubusercontent.com/api-evangelist/trustpilot/refs/heads/main/openapi/trustpilot-product-reviews-openapi.yml
        type: OpenAPI
    description: The Trustpilot Product Reviews API enables management of product-level reviews, including retrieving product review summaries, accessing individual reviews, managing conversations and comments on product reviews, creating product review invitation links, and accessing attribute rating summaries. Supports both public and private endpoints with API key and OAuth 2.0 authentication respectively.
  - aid: trustpilot:trustpilot-consumer-api
    name: Trustpilot Consumer API
    tags:
      - Consumer Reviews
      - Reviews
      - Trust
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.trustpilot.com/v1
    humanURL: https://developers.trustpilot.com/consumer-api
    properties:
      - url: https://developers.trustpilot.com/consumer-api
        type: Documentation
      - url: https://developers.trustpilot.com/authentication
        type: Authentication
    description: The Trustpilot Consumer API provides access to reviews written by individual consumers. Developers can retrieve a consumer's review history with filtering by stars, language, location, and business unit. Supports pagination and sorting and requires API key authentication.
common:
  - url: https://www.trustpilot.com/
    name: Trustpilot Website
    type: Website
  - url: https://developers.trustpilot.com/
    name: Developer Portal
    type: Portal
  - url: https://developers.trustpilot.com/
    name: API Documentation
    type: Documentation
  - url: https://www.trustpilot.com/signup/business
    name: Sign Up
    type: SignUp
  - url: https://businessapp.b2b.trustpilot.com/login
    name: Login
    type: Login
  - url: https://www.trustpilot.com/pricing
    name: Pricing
    type: Pricing
  - url: https://developers.trustpilot.com/authentication
    name: Authentication
    type: Authentication
  - url: https://developers.trustpilot.com/changelog
    name: Changelog
    type: ChangeLog
  - url: https://support.trustpilot.com/
    name: Support
    type: Support
  - url: https://www.trustpilot.com/legal/terms-and-conditions-for-businesses
    name: Terms of Service
    type: TermsOfService
  - url: https://www.trustpilot.com/legal/privacy-policy
    name: Privacy Policy
    type: PrivacyPolicy
  - url: https://blog.trustpilot.com/
    name: Trustpilot Blog
    type: Blog
  - url: https://status.trustpilot.com/
    name: Status Page
    type: Status
  - url: https://twitter.com/trustpilot
    name: Trustpilot on X (Twitter)
    type: X
  - url: https://www.linkedin.com/company/trustpilot
    name: Trustpilot on LinkedIn
    type: LinkedIn
  - url: https://www.facebook.com/trustpilot
    name: Trustpilot on Facebook
    type: Facebook
  - url: https://github.com/trustpilot
    name: Trustpilot on GitHub
    type: GitHub
  - url: https://raw.githubusercontent.com/api-evangelist/trustpilot/refs/heads/main/rules/trustpilot-rules.yml
    name: Spectral Rules
    type: SpectralRules
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

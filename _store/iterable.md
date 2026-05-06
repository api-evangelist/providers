---
aid: iterable
name: Iterable
description: Iterable is an AI customer engagement platform that powers unified cross-channel marketing experiences and empowers marketers to create, optimize, and measure relevant interactions across email, push, SMS, in-app, and web channels. Their developer platform provides REST APIs, export APIs, AsyncAPI webhooks, and native SDKs for web, iOS, Android, and React Native.
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cross-Channel Messaging
  - Customer Engagement
  - Email
  - Marketing Automation
  - Push Notifications
  - SMS
url: https://raw.githubusercontent.com/api-evangelist/iterable/refs/heads/main/apis.yml
created: '2026-03-20'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: iterable:rest-api
    name: Iterable REST API
    tags:
      - Campaigns
      - Cross-Channel Messaging
      - Email
      - Marketing Automation
      - Push Notifications
      - SMS
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.iterable.com
    humanURL: https://api.iterable.com/api/docs
    properties:
      - url: https://api.iterable.com/api/docs
        type: Documentation
      - type: OpenAPI
        url: openapi/iterable-rest-api-openapi.yml
    description: The Iterable REST API provides programmatic access to the Iterable cross-channel marketing automation platform. It exposes endpoints for managing users, campaigns, lists, events, commerce tracking, catalogs, channels, templates, experiments, workflows, and message delivery across email, push, SMS, and in-app channels. The API uses standard HTTP methods, JSON request and response bodies, and supports authentication via API keys or JWT-enabled keys.
  - aid: iterable:export-api
    name: Iterable Export API
    tags:
      - Analytics
      - Data Export
      - Marketing Data
      - Reporting
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.iterable.com
    humanURL: https://support.iterable.com/hc/en-us/articles/204780579-Iterable-API-Endpoints-and-Sample-Payloads
    properties:
      - url: https://support.iterable.com/hc/en-us/articles/204780579-Iterable-API-Endpoints-and-Sample-Payloads
        type: Documentation
      - type: OpenAPI
        url: openapi/iterable-export-api-openapi.yml
    description: The Iterable Export API enables developers to extract data from Iterable projects for analytics, reporting, and data warehousing purposes. It provides asynchronous export endpoints that allow bulk retrieval of user data, event data, campaign metrics, and message engagement information. The export endpoints support filtering by date ranges and other criteria, making it possible to build custom reporting pipelines and synchronize Iterable data with external business intelligence tools.
  - aid: iterable:web-sdk
    name: Iterable Web SDK
    tags:
      - In-App Messaging
      - JavaScript
      - SDK
      - User Tracking
      - Web
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://github.com/Iterable/iterable-web-sdk
    properties:
      - url: https://github.com/Iterable/iterable-web-sdk
        type: Documentation
    description: The Iterable Web SDK enables developers to integrate Iterable's marketing automation capabilities directly into JavaScript and Node.js applications. It provides functions for tracking user events, managing user profiles, displaying in-app messages, and handling web push notifications.
  - aid: iterable:ios-sdk
    name: Iterable iOS SDK
    tags:
      - In-App Messaging
      - iOS
      - Mobile
      - Push Notifications
      - SDK
      - Swift
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://support.iterable.com/hc/en-us/articles/360035018152-Iterable-s-iOS-SDK
    properties:
      - url: https://support.iterable.com/hc/en-us/articles/360035018152-Iterable-s-iOS-SDK
        type: Documentation
    description: The Iterable iOS SDK allows developers to integrate Iterable's marketing automation features into native iOS applications built with Swift or Objective-C. It supports push notifications, in-app messages, deep links, and Mobile Inbox functionality. The SDK can be installed via Swift Package Manager, CocoaPods, or Carthage, and supports iOS 10 and higher. It enables mobile apps to track user events, display targeted in-app content, and participate in Iterable's cross-channel marketing campaigns.
  - aid: iterable:android-sdk
    name: Iterable Android SDK
    tags:
      - Android
      - In-App Messaging
      - Mobile
      - Push Notifications
      - SDK
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://support.iterable.com/hc/en-us/articles/360028925511-Overview-of-Iterable-s-iOS-and-Android-SDKs
    properties:
      - url: https://support.iterable.com/hc/en-us/articles/360028925511-Overview-of-Iterable-s-iOS-and-Android-SDKs
        type: Documentation
    description: The Iterable Android SDK provides native integration between Android applications and the Iterable marketing automation platform. It supports push notifications, in-app messages, deep links, and Mobile Inbox features. The open-source SDK enables Android apps to track user events, manage user profiles, render in-app content, and connect with Iterable's cross-channel campaign orchestration. Developers can use it to deliver personalized marketing experiences within their Android applications.
  - aid: iterable:react-native-sdk
    name: Iterable React Native SDK
    tags:
      - Cross-Platform
      - JavaScript
      - Mobile
      - React Native
      - SDK
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://support.iterable.com/hc/en-us/articles/360045714072-Overview-of-Iterable-s-React-Native-SDK
    properties:
      - url: https://support.iterable.com/hc/en-us/articles/360045714072-Overview-of-Iterable-s-React-Native-SDK
        type: Documentation
    description: The Iterable React Native SDK enables developers to integrate Iterable's marketing automation capabilities into cross-platform mobile applications built with React Native. It wraps Iterable's native iOS and Android SDKs and supports both JavaScript and TypeScript. The SDK provides access to push notifications, in-app messages, Mobile Inbox, user event tracking, and deep linking.
common:
  - type: AsyncAPI
    url: asyncapi/iterable-system-webhooks-asyncapi.yml
  - type: JSON-LD
    url: json-ld/iterable-context.jsonld
  - type: JSONSchema
    url: json-schema/iterable-user-schema.json
  - type: JSONSchema
    url: json-schema/iterable-campaign-schema.json
  - type: JSONSchema
    url: json-schema/iterable-event-schema.json
  - type: JSONSchema
    url: json-schema/iterable-commerce-item-schema.json
  - name: Iterable
    url: https://iterable.com/
    type: Website
  - name: Iterable Developer Documentation
    url: https://api.iterable.com/api/docs
    type: Documentation
  - name: Iterable Support Center
    url: https://support.iterable.com/hc/en-us
    type: Support
  - name: Iterable Blog
    url: https://iterable.com/blog/
    type: Blog
  - name: Iterable Login
    url: https://app.iterable.com/login
    type: Login
  - name: Iterable Privacy Policy
    url: https://iterable.com/trust/privacy-policy/
    type: PrivacyPolicy
  - name: Iterable Terms of Service
    url: https://iterable.com/trust/terms-of-service/
    type: TermsOfService
  - type: Features
    data:
      - 'Growth: $3K-$5K/mo for 10K-50K MAUs'
      - 'Premier: $6K-$15K/mo for 50K-200K MAUs'
      - 'Enterprise: $20K+/mo for 200K+ MAUs'
      - Multi-year + volume discounts
      - Email + Push + SMS + In-App + Web Push + Direct Mail channels
      - Workflow Studio for journey orchestration
      - AI Optimization for send-time and channel selection (Premier+)
      - REST API at api.iterable.com
      - Default 30 req/sec; bulk endpoints up to 1K events/req
      - OAuth + API keys (project-scoped)
      - Webhooks for events and campaign data
      - User profile and event tracking
      - Cross-channel campaigns
      - Smart Ingest for data lake/warehouse loading
      - Real-time event triggers
      - Iterable AI for content suggestions
    sources:
      - https://www.iterable.com/pricing/
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

---
aid: adobe-campaign
url: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/apis.yml
name: Adobe Campaign
description: Adobe Campaign is a comprehensive marketing automation platform that enables businesses to orchestrate personalized customer experiences across multiple channels including email, mobile, social, and web.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
tags:
  - Campaign Management
  - Customer Experience
  - Email Marketing
  - Marketing Automation
  - Multi-Channel Marketing
created: '2024-01-01'
modified: '2026-04-17'
specificationVersion: '0.19'
apis:
  - name: Adobe Campaign Standard API
    description: REST API for Adobe Campaign Standard enabling integration with marketing campaigns, profiles, workflows, and messaging services.
    image: https://www.adobe.com/content/dam/cc/icons/adobe-campaign.svg
    humanURL: https://experienceleague.adobe.com/docs/campaign-standard/using/working-with-apis/about-campaign-standard-apis.html
    baseURL: https://mc.adobe.io/{ORGANIZATION}/campaign
    tags:
      - Email
      - Marketing
      - Profiles
      - REST API
      - Workflows
    properties:
      - type: Documentation
        url: https://experienceleague.adobe.com/docs/campaign-standard/using/working-with-apis/get-started-apis.html
      - type: OpenAPI
        url: openapi/adobe-campaign-standard-openapi-original.yml
      - type: APIReference
        url: https://developer.adobe.com/campaign/api/
      - type: Authentication
        url: https://experienceleague.adobe.com/docs/campaign-standard/using/working-with-apis/authentication.html
      - type: AsyncAPI
        url: asyncapi/adobe-campaign-transactional-messaging-asyncapi-original.yml
    aid: adobe-campaign:standard-api
  - name: Adobe Campaign Classic API
    description: SOAP and JavaScript APIs for Adobe Campaign Classic v7 and v8, providing programmatic access to campaign management, delivery, and data operations.
    image: https://www.adobe.com/content/dam/cc/icons/adobe-campaign.svg
    humanURL: https://experienceleague.adobe.com/docs/campaign-classic/using/configuring-campaign-classic/api/about-web-services.html
    baseURL: https://{instance}.campaign.adobe.com
    tags:
      - Campaign Classic
      - Delivery
      - JavaScript
      - SOAP API
    properties:
      - type: Documentation
        url: https://experienceleague.adobe.com/docs/campaign-classic/using/configuring-campaign-classic/api/web-service-calls.html
      - type: OpenAPI
        url: openapi/adobe-campaign-classic-openapi-original.yml
      - type: JSAPI Reference
        url: https://experienceleague.adobe.com/developer/campaign-api/api/index.html
      - type: SOAP Methods
        url: https://experienceleague.adobe.com/docs/campaign-classic/using/configuring-campaign-classic/api/soap-methods.html
      - type: AsyncAPI
        url: asyncapi/adobe-campaign-transactional-messaging-asyncapi-original.yml
    aid: adobe-campaign:classic-api
  - name: Adobe Campaign Classic JavaScript SDK
    description: An open-source JavaScript SDK that wraps Adobe Campaign Classic SOAP APIs in a simple, expressive, JavaScript-idiomatic interface. The SDK supports asynchronous promise-based operations for querying, data management, workflow control, and session management. It works server-side with Node.js and client-side in the browser, abstracting away SOAP calls, XML-to-JSON conversion, and type formatting. Compatible with Campaign Classic v7 and v8.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://opensource.adobe.com/acc-js-sdk/
    baseURL: https://{instance}.campaign.adobe.com
    tags:
      - Campaign Classic
      - JavaScript SDK
      - Node.js
      - Open Source
      - SOAP Wrapper
    properties:
      - type: Documentation
        url: https://opensource.adobe.com/acc-js-sdk/
      - type: GitHubRepository
        url: https://github.com/adobe/acc-js-sdk
      - type: NPMPackage
        url: https://www.npmjs.com/package/@adobe/acc-js-sdk
    aid: adobe-campaign:classic-javascript-sdk
  - name: Adobe I/O Campaign Standard SDK
    description: A Node.js JavaScript SDK wrapping Adobe Campaign Standard REST APIs for use in Adobe I/O Runtime and App Builder applications. Provides convenience methods for profile management, service operations, workflow control, transactional messaging, GDPR compliance requests, and custom resource management. Handles authentication and API communication for building serverless integrations with Campaign Standard.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://github.com/adobe/aio-lib-campaign-standard
    baseURL: https://mc.adobe.io/{ORGANIZATION}/campaign
    tags:
      - Adobe I/O
      - App Builder
      - Campaign Standard
      - JavaScript SDK
      - Node.js
    properties:
      - type: Documentation
        url: https://github.com/adobe/aio-lib-campaign-standard/blob/master/README.md
      - type: GitHubRepository
        url: https://github.com/adobe/aio-lib-campaign-standard
      - type: NPMPackage
        url: https://www.npmjs.com/package/@adobe/aio-lib-campaign-standard
    aid: adobe-campaign:io-campaign-standard-sdk
  - name: Adobe Experience Platform Mobile SDK - Campaign Extensions
    description: Native mobile SDK extensions for iOS and Android that integrate Adobe Campaign push notifications, in-app messaging, and local notifications into mobile applications. Includes the Campaign Classic extension for v7 and v8 providing device registration and notification click tracking, and the Campaign Standard extension providing push identifier management and message interaction tracking. Part of the Adobe Experience Platform Mobile SDK framework.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.adobe.com/client-sdks/solution/adobe-campaign-classic/
    baseURL: https://api.example.com
    tags:
      - Android
      - In-App Messaging
      - iOS
      - Mobile SDK
      - Push Notifications
    properties:
      - type: Documentation
        url: https://developer.adobe.com/client-sdks/solution/adobe-campaign-classic/
      - type: Documentation
        url: https://developer.adobe.com/client-sdks/solution/adobe-campaign-standard/
      - type: APIReference
        url: https://developer.adobe.com/client-sdks/solution/adobe-campaign-classic/api-reference/
    aid: adobe-campaign:experience-platform-mobile-sdk---campaign-extensions
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Portal
    url: https://developer.adobe.com/
  - type: Authentication
    url: https://developer.adobe.com/developer-console/docs/guides/authentication/
  - type: GettingStarted
    url: https://experienceleague.adobe.com/docs/campaign-learn/tutorials/overview.html
  - type: Support
    url: https://experienceleague.adobe.com/docs/customer-one/using/home.html
  - type: StatusPage
    url: https://status.adobe.com/
  - type: TermsOfService
    url: https://www.adobe.com/legal/terms.html
  - type: PrivacyPolicy
    url: https://www.adobe.com/privacy.html
  - type: Blog
    url: https://business.adobe.com/blog/
  - type: Features
    data:
      - name: Cross-Channel Campaign Orchestration
        description: Design and execute campaigns across email, SMS, push, direct mail, and web channels.
      - name: Profile and Audience Management
        description: Manage customer profiles, segments, and audiences for targeted messaging.
      - name: Email Delivery
        description: Send transactional and marketing emails with personalization and A/B testing.
      - name: Workflow Automation
        description: Build and execute automated marketing workflows with visual workflow designer.
      - name: Real-Time Messaging
        description: Trigger personalized messages in real time based on customer events and behaviors.
      - name: Reporting and Analytics
        description: Access campaign performance metrics, delivery statistics, and audience insights.
      - name: Content Personalization
        description: Dynamic content blocks and personalization fields for tailored messaging.
      - name: Push Notifications
        description: Send mobile push notifications to iOS and Android devices.
      - name: SMS Messaging
        description: Send SMS campaigns and transactional messages to mobile subscribers.
      - name: Landing Pages
        description: Create and manage landing pages for campaign responses and lead capture.
  - type: UseCases
    data:
      - name: Email Marketing Campaigns
        description: Design, personalize, and send email campaigns with tracking and analytics.
      - name: Customer Journey Orchestration
        description: Build multi-step customer journeys with triggers, conditions, and automated actions.
      - name: Transactional Messaging
        description: Send real-time transactional emails and SMS for order confirmations and alerts.
      - name: Lead Nurturing
        description: Automate lead scoring and nurture sequences based on engagement data.
      - name: Audience Segmentation
        description: Build dynamic audience segments for targeted campaign delivery.
      - name: Cross-Channel Coordination
        description: Coordinate messaging across email, SMS, push, and direct mail channels.
  - type: Integrations
    data:
      - name: Adobe Experience Cloud
        description: Native integration with AEM, Analytics, and Target for unified marketing.
      - name: Adobe Experience Platform
        description: Real-time customer profile and audience sharing with AEP.
      - name: Salesforce
        description: CRM integration for syncing contacts, leads, and campaign data.
      - name: Microsoft Dynamics
        description: CRM integration for contact synchronization and campaign tracking.
  - type: Solutions
    data:
      - name: Adobe Campaign Standard
        description: Cloud-native marketing automation with modern REST APIs and visual workflow designer.
      - name: Adobe Campaign Classic
        description: On-premises/hybrid marketing automation with SOAP and JavaScript APIs.
      - name: Adobe Campaign v8
        description: Latest generation combining Campaign Classic power with cloud scalability.
---

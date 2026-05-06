---
aid: at-and-t
name: AT&T
description: AT&T is a multinational telecommunications holding company providing wireless and wireline telecommunications services, broadband, and digital entertainment to consumers and businesses worldwide. AT&T offers a suite of developer APIs spanning messaging, speech, mobile virtual network operations, business voice, wholesale service qualification, enterprise wireline ordering, and mobility management, enabling developers and enterprise partners to integrate AT&T network capabilities into applications and systems.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Telecommunications
  - Wireless
  - Wireline
  - Messaging
  - Speech
  - Mobile
  - Broadband
  - Enterprise
url: https://raw.githubusercontent.com/api-evangelist/at-and-t/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: at-and-t:att-sms-api
    name: AT&T SMS API
    description: A RESTful API enabling established businesses to broadcast SMS short code messages to AT&T subscribers in the United States. Supports sending to up to 50 recipients per call and up to 1 million messaging API calls monthly. Includes delivery status callbacks and GSMA OneAPI-compatible endpoints.
    humanURL: https://developer.att.com/sms
    baseURL: https://api.att.com
    tags:
      - SMS
      - Messaging
      - Short Code
      - Notifications
    properties:
      - type: Documentation
        url: https://developer.att.com/sms/docs
      - type: APIReference
        url: https://developer.att.com/sms/docs/v2
      - type: Authentication
        url: https://developer.att.com/oauth-2/docs
      - type: GettingStarted
        url: https://developer.att.com/sms
      - type: OpenAPI
        url: openapi/at-and-t-sms-api.yaml
  - aid: at-and-t:att-in-app-messaging-api
    name: AT&T In-App Messaging API
    description: A messaging API enabling applications to send, receive, update, and delete MMS and SMS messages on behalf of users with explicit consent. Supports messages to phone numbers, short codes, and email addresses across AT&T and other carriers, with inbox management and delta synchronization.
    humanURL: https://developer.att.com/in-app-messaging
    baseURL: https://api.att.com
    tags:
      - MMS
      - SMS
      - Messaging
      - In-App
      - Inbox
    properties:
      - type: Documentation
        url: https://developer.att.com/in-app-messaging/docs
      - type: Authentication
        url: https://developer.att.com/oauth-2/docs
      - type: OpenAPI
        url: openapi/at-and-t-in-app-messaging-api.yaml
  - aid: at-and-t:att-oauth-api
    name: AT&T OAuth 2.0 API
    description: AT&T OAuth 2.0 authentication API providing access tokens for all AT&T REST APIs. Supports Authorization Code, Client Credentials, and Refresh Token grant types. Scopes include ADS, MMS, SMS, SPEECH, STTC, and TTS.
    humanURL: https://developer.att.com/oauth-2
    baseURL: https://api.att.com
    tags:
      - OAuth
      - Authentication
      - Authorization
      - Security
    properties:
      - type: Documentation
        url: https://developer.att.com/oauth-2/docs
      - type: Authentication
        url: https://developer.att.com/oauth-2/docs
  - aid: at-and-t:att-mvnx-api
    name: AT&T MVNX API
    description: TM Forum-aligned API suite for mobile virtual network operators (MVNOs) enabling subscriber activation, number management, porting operations, device and SIM management, subscriber profile management, service management, and policy and balance management. Follows TMF standards (622, 637, 639, 640, 654, 674, 689, 702, 716, 761).
    humanURL: https://devex-web.att.com/mvnx
    baseURL: https://devex-web.att.com
    tags:
      - MVNO
      - Mobile
      - Subscriber
      - TM Forum
      - Porting
      - SIM
    properties:
      - type: Documentation
        url: https://devex-web.att.com/mvnx/docs/mvnx-quickstart
      - type: GettingStarted
        url: https://devex-web.att.com/mvnx/docs/mvnx-quickstart
      - type: OpenAPI
        url: openapi/at-and-t-mvnx-api.yaml
  - aid: at-and-t:att-alliance-wireline-apis
    name: AT&T Alliance Wireline APIs
    description: Wireline business APIs enabling partners to expedite quoting, service qualification, and ordering of AT&T wireline products. Includes Quick Quote, Product Catalog, Service Qualification, Price Offer, Wireline Ordering, Order Status, AIAB (AT&T Internet Air for Business) Ordering, and Address Search APIs.
    humanURL: https://devex-web.att.com/alliance
    baseURL: https://devex-web.att.com
    tags:
      - Wireline
      - Enterprise
      - Ordering
      - Service Qualification
      - Quoting
    properties:
      - type: Documentation
        url: https://devex-web.att.com/alliance
      - type: GettingStarted
        url: https://devex-web.att.com/order/docs/get-started-with-ordering-api
common:
  - type: Website
    url: https://www.att.com
  - type: Portal
    url: https://developer.att.com/s/
  - type: DeveloperPortal
    url: https://devex-web.att.com/
  - type: Documentation
    url: https://developer.att.com/s/
  - type: Authentication
    url: https://developer.att.com/oauth-2/docs
  - type: Support
    url: https://developer.att.com/support
  - type: FAQ
    url: https://developer.att.com/support/faqs/att-developer-program-and-api-platform-faqs
  - type: TermsOfService
    url: https://www.att.com/gen/general?pid=11561
  - type: PrivacyPolicy
    url: https://www.att.com/gen/privacy-policy?pid=2506
  - type: SignUp
    url: https://developer.att.com/developer/manageMyAccount.jsp
  - type: GitHubOrganization
    url: https://github.com/attdevsupport
  - type: GitHubOrganization
    url: https://github.com/att
  - type: SpectralRules
    url: rules/at-and-t-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/at-and-t-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/messaging.yaml
  - type: NaftikoCapability
    url: capabilities/mvno-operations.yaml
  - type: Features
    data:
      - 'AT&T: API access via partner / B2B contracts only'
      - No public API pricing published — contact enterprise sales
      - AT&T Business APIs (Network APIs, IoT Connectivity, etc.) are sold via partner program with custom contracts.
    sources:
      - https://developer.att.com/
      - https://www.att.com/business/
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: SMS Alerts and Notifications
        description: Send security verification codes, appointment reminders, promotional offers, and customer feedback requests via SMS short code.
      - name: In-App Messaging Integration
        description: Embed MMS and SMS messaging directly into mobile applications with full inbox management capabilities.
      - name: Mobile Virtual Network Operations
        description: Launch and operate MVNO services using AT&T's network with automated subscriber onboarding, porting, and lifecycle management.
      - name: Enterprise Wireline Ordering
        description: Automate service qualification, quoting, and order submission for enterprise connectivity services.
  - type: Integrations
    data:
      - name: IBM Worklight
        description: AT&T API Platform Adapters for IBM Worklight mobile development platform.
      - name: Salesforce Platform
        description: AT&T Toolkit for Salesforce enabling speech and messaging API integration in Salesforce apps.
      - name: TM Forum APIs
        description: MVNX APIs align with TM Forum Open API standards including TMF 622, 637, 639, 640, 654, 674, 689, 702, 716, and 761.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

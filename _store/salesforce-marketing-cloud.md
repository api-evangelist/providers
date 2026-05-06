---
name: Salesforce Marketing Cloud
description: Salesforce Marketing Cloud is a comprehensive digital marketing platform that enables businesses to manage customer journeys, email marketing, mobile messaging, social media marketing, advertising, and data analytics.
image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
url: https://www.salesforce.com/products/marketing-cloud/overview/
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.18'
type:
  - Index
tags:
  - Automation
  - Customer Journey
  - Digital Marketing
  - Email
  - Marketing
  - Personalization
apis:
  - name: Marketing Cloud REST API
    description: Core REST API for interacting with Marketing Cloud features including email, SMS, push notifications, and data extensions. REST API uses JSON request and response bodies and resource endpoints to support multi-channel use.
    image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
    baseURL: https://YOUR_SUBDOMAIN.rest.marketingcloudapis.com
    humanURL: https://developer.salesforce.com/docs/marketing/marketing-cloud/overview
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/rest-api-overview.html
      - type: OpenAPI
        url: openapi/salesforce-marketing-cloud-openapi.yml
      - type: Authentication
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/authentication.html
      - type: APIReference
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/routes.html
      - type: GettingStarted
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/get-started-index.html
      - type: RateLimits
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/rate-limiting.html
      - type: BestPractices
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/rate-limiting-best-practices.html
      - type: Errors
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/rate-limiting-errors.html
    tags:
      - Email
      - Push
      - REST
      - SMS
  - name: SOAP API
    description: Legacy SOAP-based API for Marketing Cloud operations, including email sends, subscriber management, and data extension operations.
    image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
    baseURL: https://YOUR_SUBDOMAIN.soap.marketingcloudapis.com
    humanURL: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/web_service_guide.html
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/web_service_guide.html
      - type: APIReference
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/soap_web_service_objects.html
      - type: GettingStarted
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/getting_started_developers_and_the_exacttarget_api.html
      - type: BestPractices
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/working_with_soap_web_service_api.html
    tags:
      - Legacy
      - SOAP
      - Subscriber
  - name: Transactional Messaging API
    description: Specialized API for sending triggered, transactional messages including order confirmations, password resets, and real-time notifications.
    image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
    baseURL: https://YOUR_SUBDOMAIN.rest.marketingcloudapis.com/messaging/v1
    humanURL: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/transactional-messaging-api.html
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/transactional-messaging-api.html
      - type: GettingStarted
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/getting-started-spec.html
      - type: BestPractices
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/transactional-messaging-best-practices.html
    tags:
      - Messaging
      - Transactional
      - Triggered
  - name: Journey Builder API
    description: API for creating, managing, and automating customer journeys across multiple channels and touchpoints.
    image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
    baseURL: https://YOUR_SUBDOMAIN.rest.marketingcloudapis.com/interaction/v1
    humanURL: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/journey-builder-api-overview.html
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/journey-builder-api-overview.html
      - type: GettingStarted
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/get-started-jb.html
    tags:
      - Automation
      - Journey
      - Orchestration
  - name: Data Extensions API
    description: API for managing data extensions, which are database tables used to store and segment customer data in Marketing Cloud.
    image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
    baseURL: https://YOUR_SUBDOMAIN.rest.marketingcloudapis.com/data/v1
    humanURL: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/data-extensions.html
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/working-with-data-extensions.html
      - type: APIReference
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/data-extension-api.html
    tags:
      - Data
      - Segmentation
      - Storage
  - name: Email Send Definition API
    description: API for creating and managing email send definitions, which define the configuration for sending emails to subscribers.
    image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
    baseURL: https://YOUR_SUBDOMAIN.rest.marketingcloudapis.com/messaging/v1
    humanURL: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/email-send-definition.html
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/email-send-definition.html
      - type: CodeExamples
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/code-examples.html
    tags:
      - Campaigns
      - Email
      - Sending
  - name: Mobile Push API
    description: API for sending push notifications to mobile devices, managing device registrations, and tracking push message engagement.
    image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
    baseURL: https://YOUR_SUBDOMAIN.rest.marketingcloudapis.com/push/v1
    humanURL: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/mobile-push.html
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/push-notifications.html
      - type: SDK
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/mobile-sdk.html
    tags:
      - Mobile
      - Notifications
      - Push
  - name: SMS/MMS API
    description: API for sending SMS and MMS messages, managing mobile numbers, and handling keyword-based subscriptions.
    image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
    baseURL: https://YOUR_SUBDOMAIN.rest.marketingcloudapis.com/sms/v1
    humanURL: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/sms-api.html
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/sms-api.html
      - type: BestPractices
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/sms-best-practices.html
    tags:
      - MMS
      - Mobile Messaging
      - SMS
  - name: Asset API
    description: API for managing marketing assets including images, documents, content blocks, and templates across Marketing Cloud.
    image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
    baseURL: https://YOUR_SUBDOMAIN.rest.marketingcloudapis.com/asset/v1
    humanURL: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/asset-api.html
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/asset-api.html
    tags:
      - Assets
      - Content
      - Templates
  - name: Einstein Recommendations API
    description: API for leveraging AI-powered product and content recommendations to personalize customer experiences.
    image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
    baseURL: https://YOUR_SUBDOMAIN.rest.marketingcloudapis.com/einstein/v1
    humanURL: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/einstein-recommendations.html
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/einstein-recommendations.html
    tags:
      - AI
      - Personalization
      - Recommendations
  - name: Content Builder API
    description: REST API for creating and manipulating marketing content in Content Builder, a single cross-channel repository for emails, images, text, content blocks, and other documents.
    image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
    baseURL: https://YOUR_SUBDOMAIN.rest.marketingcloudapis.com/asset/v1
    humanURL: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/content-api.html
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/content-api.html
    tags:
      - Assets
      - Content
      - Email
      - Templates
  - name: Contacts API
    description: REST API for creating, reading, updating, and deleting contacts in Marketing Cloud.
    image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
    baseURL: https://YOUR_SUBDOMAIN.rest.marketingcloudapis.com/contacts/v1
    humanURL: https://developer.salesforce.com/docs/marketing/marketing-cloud/references/mc_rest_contacts/createContacts.html
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/references/mc_rest_contacts/createContacts.html
    tags:
      - Contacts
      - Data
      - Subscribers
  - name: Automation Studio API
    description: API for initiating and managing marketing automations, including file upload, download, decryption, compression, and decompression operations within Automation Studio.
    image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
    baseURL: https://YOUR_SUBDOMAIN.rest.marketingcloudapis.com/automation/v1
    humanURL: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/automation-studio-api.html
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/automation-studio-api.html
    tags:
      - Automation
      - Scheduling
      - Workflows
  - name: Campaign API
    description: API for managing and performing marketing campaigns within Marketing Cloud.
    image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
    baseURL: https://YOUR_SUBDOMAIN.rest.marketingcloudapis.com/hub/v1
    humanURL: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/campaign.html
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/campaign.html
    tags:
      - Campaigns
      - Execution
      - Marketing
  - name: Event Notification Service API
    description: API for registering callbacks and subscriptions to receive real-time event notifications from Marketing Cloud.
    image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
    baseURL: https://YOUR_SUBDOMAIN.rest.marketingcloudapis.com/platform/v1
    humanURL: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/ens.html
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/ens.html
      - type: GettingStarted
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/ens-get-started.html
    tags:
      - Events
      - Notifications
      - Real-Time
      - Webhooks
common:
  - type: DeveloperPortal
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/overview
  - type: Documentation
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/apis-overview.html
  - type: Authentication
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/authentication.html
  - type: APIReference
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/references
  - type: Support
    url: https://help.salesforce.com/s/
  - type: StatusPage
    url: https://status.salesforce.com/
  - type: SDK
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/sdks.html
  - type: TermsOfService
    url: https://www.salesforce.com/company/legal/
  - type: Pricing
    url: https://www.salesforce.com/products/marketing-cloud/pricing/
  - type: ChangeLog
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/release-notes.html
  - type: RateLimits
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/rate-limiting.html
  - type: GitHubRepository
    url: https://github.com/salesforce-marketingcloud/SFDC-MC-REST-Style-Guide
  - type: Training
    url: https://trailhead.salesforce.com/en/content/learn/trails/get-started-with-marketing-cloud
  - type: Features
    data:
      - name: Email Marketing
        description: Design, send, and track targeted email campaigns with dynamic content, personalization, and A/B testing capabilities.
      - name: Journey Builder
        description: Create automated, multi-step customer journeys across email, SMS, push, and advertising channels with branching logic.
      - name: Contact Management
        description: Centralized contact database with attribute sets, segmentation, and cross-channel identity resolution.
      - name: Transactional Messaging
        description: Send real-time transactional messages like order confirmations and password resets with guaranteed delivery.
      - name: Einstein AI Personalization
        description: Leverage AI-powered recommendations and predictive analytics to personalize content and optimize send times.
      - name: Automation Studio
        description: Schedule and automate data imports, file transfers, SQL queries, and multi-step marketing workflows.
      - name: Content Builder
        description: Centralized content management system for creating, organizing, and reusing marketing assets across channels.
      - name: Event Notifications
        description: Subscribe to real-time webhook notifications for email tracking events, data changes, and audit activities.
  - type: UseCases
    data:
      - name: Customer Onboarding Journeys
        description: Automate multi-step welcome sequences across email and SMS to guide new customers through product adoption.
      - name: Abandoned Cart Recovery
        description: Trigger personalized follow-up emails and push notifications when customers abandon shopping carts.
      - name: Cross-Channel Campaign Orchestration
        description: Coordinate marketing messages across email, SMS, push, and advertising for unified campaign execution.
      - name: Subscriber Lifecycle Management
        description: Manage subscriber preferences, segment audiences, and automate re-engagement campaigns for inactive contacts.
      - name: Real-Time Event-Driven Marketing
        description: React to customer behaviors in real time with triggered messages based on website visits, purchases, or app activity.
  - type: Integrations
    data:
      - name: Salesforce CRM
        description: Bi-directional sync with Sales Cloud and Service Cloud for unified customer profiles and campaign attribution.
      - name: Salesforce Data Cloud
        description: Connect to unified customer data profiles for advanced segmentation and real-time personalization.
      - name: Google Analytics
        description: Track email campaign performance and website conversions with Google Analytics integration.
      - name: Shopify
        description: Sync e-commerce customer data, purchase history, and cart events for targeted marketing automation.
      - name: Salesforce Commerce Cloud
        description: Integrate commerce data for personalized product recommendations and transactional messaging.
  - type: NaftikoCapability
    url: capabilities/marketing-automation.yaml
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
contact:
  - name: Salesforce Marketing Cloud Support
    email: support@salesforce.com
    url: https://help.salesforce.com/s/
---

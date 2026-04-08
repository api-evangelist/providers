---
aid: salesforce-marketing-cloud
url: https://raw.githubusercontent.com/api-evangelist/salesforce-marketing-cloud/refs/heads/main/apis.yml
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
  - type: JSON Schema
    url: json-schema/salesforce-marketing-cloud-contact-schema.json
  - type: JSON-LD
    url: json-ld/salesforce-marketing-cloud-context.jsonld
  - type: Authentication
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/authentication.html
  - type: API Reference
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/routes.html
  - type: Getting Started
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/get-started-index.html
  - type: Rate Limits
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/rate-limiting.html
  - type: Best Practices
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/rate-limiting-best-practices.html
  - type: Error Codes
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/rate-limiting-errors.html
  tags:
  - Email
  - Push
  - Rest
  - Sms
- name: SOAP API
  description: Legacy SOAP-based API for Marketing Cloud operations, including email sends, subscriber management, and data extension operations. SOAP API uses SOAP envelopes to pass information between systems and provides comprehensive access to most email functionality.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
  baseURL: https://YOUR_SUBDOMAIN.soap.marketingcloudapis.com
  humanURL: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/web_service_guide.html
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/web_service_guide.html
  - type: WSDL
    url: https://webservice.exacttarget.com/etframework.wsdl
  - type: API Reference
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/soap_web_service_objects.html
  - type: Getting Started
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/getting_started_developers_and_the_exacttarget_api.html
  - type: WSDL and Endpoint Links
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/wsdl-endpoint-links.html
  - type: Best Practices
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/working_with_soap_web_service_api.html
  tags:
  - Legacy
  - Soap
  - Subscriber
- name: Transactional Messaging API
  description: Specialized API for sending triggered, transactional messages including order confirmations, password resets, and real-time notifications.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
  baseURL: https://YOUR_SUBDOMAIN.rest.marketingcloudapis.com/messaging/v1
  humanURL: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/transactional-messaging-api.html
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/transactional-messaging-api.html
  - type: Getting Started
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/getting-started-spec.html
  - type: Postman Collection
    url: https://www.postman.com/salesforce-developers/workspace/salesforce-developers
  - type: Best Practices
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/transactional-messaging-best-practices.html
  tags:
  - Messaging
  - Transactional
  - Triggered
- name: Journey Builder API
  description: API for creating, managing, and automating customer journeys across multiple channels and touchpoints. The Journey Specification is a structured JSON representation of a single journey used via REST API requests.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
  baseURL: https://YOUR_SUBDOMAIN.rest.marketingcloudapis.com/interaction/v1
  humanURL: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/journey-builder-api-overview.html
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/journey-builder-api-overview.html
  - type: Getting Started
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/get-started-jb.html
  - type: API Specification
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/jb-api-specification.html
  - type: Build Journey
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/getting-started-spec.html
  - type: Fire Entry Event
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/how-to-fire-an-event.html
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
  - type: API Reference
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
  - type: Code Examples
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
  - type: SDK Documentation
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
  - type: Best Practices
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/sms-best-practices.html
  tags:
  - Mms
  - Mobile Messaging
  - Sms
- name: Asset API
  description: API for managing marketing assets including images, documents, content blocks, and templates across Marketing Cloud.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
  baseURL: https://YOUR_SUBDOMAIN.rest.marketingcloudapis.com/asset/v1
  humanURL: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/asset-api.html
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/asset-api.html
  - type: Asset Types
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/asset-types.html
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
  - type: Use Cases
    url: https://help.salesforce.com/s/articleView?id=sf.mc_pers_einstein_recommendations.htm
  tags:
  - Ai
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
  - type: Content Reference
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/content.html
  tags:
  - Assets
  - Content
  - Email
  - Templates
- name: Contacts API
  description: REST API for creating, reading, updating, and deleting contacts in Marketing Cloud. Supports contact search, attribute set management, and address lookups.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
  baseURL: https://YOUR_SUBDOMAIN.rest.marketingcloudapis.com/contacts/v1
  humanURL: https://developer.salesforce.com/docs/marketing/marketing-cloud/references/mc_rest_contacts/createContacts.html
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/references/mc_rest_contacts/createContacts.html
  - type: Update Contacts
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/references/mc_rest_contacts/updateContacts.html
  - type: Search Contacts
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/references/mc_rest_contacts/retrieveContactKey.html
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
  - type: SOAP Integration
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/interacting_with_automation_studio_via_the_web_service_soap_api.html
  tags:
  - Automation
  - Scheduling
  - Workflows
- name: Campaign API
  description: API for managing and performing marketing campaigns within Marketing Cloud, enabling programmatic campaign creation and execution.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
  baseURL: https://YOUR_SUBDOMAIN.rest.marketingcloudapis.com/hub/v1
  humanURL: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/campaign.html
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/campaign.html
  - type: Perform Campaign
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/performing_a_campaign_via_the_web_service_api.html
  tags:
  - Campaigns
  - Execution
  - Marketing
- name: Event Notification Service API
  description: API for registering callbacks and subscriptions to receive real-time event notifications from Marketing Cloud, including email tracking events, data extension changes, and audit events.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
  baseURL: https://YOUR_SUBDOMAIN.rest.marketingcloudapis.com/platform/v1
  humanURL: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/ens.html
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/ens.html
  - type: Getting Started
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/ens-get-started.html
  - type: Supported Events
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/ens-supported-events.html
  - type: Activities
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/ens-activities.html
  tags:
  - Events
  - Notifications
  - Real-Time
  - Webhooks
name: Salesforce Marketing Cloud
tags:
- Automation
- Customer Journey
- Digital Marketing
- Email
- Marketing
- Personalization
type: Contract
image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Salesforce Marketing Cloud is a comprehensive digital marketing platform that enables businesses to manage customer journeys, email marketing, mobile messaging, social media marketing, advertising, and data analytics.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


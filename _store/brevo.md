---
aid: brevo
url: https://raw.githubusercontent.com/api-evangelist/brevo/refs/heads/main/apis.yml
apis:
  - aid: brevo:transactional-email-api
    name: Brevo Transactional Email API
    tags:
      - Email
      - Messaging
      - SMTP
      - Transactional
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.brevo.com/v3
    humanURL: https://developers.brevo.com/docs/send-a-transactional-email
    properties:
      - url: https://developers.brevo.com/docs/send-a-transactional-email
        type: Documentation
      - url: openapi/brevo-transactional-email-openapi.yml
        type: OpenAPI
    description: The Brevo Transactional Email API allows developers to send transactional emails such as order confirmations, password resets, and account notifications programmatically. It supports single and batch sending, scheduled deliveries, template-based emails, and attachment handling. The API also provides endpoints for tracking email activity including opens, clicks, bounces, and delivery status through detailed event logs and real-time webhooks.
  - aid: brevo:email-campaigns-api
    name: Brevo Email Campaigns API
    tags:
      - Automation
      - Campaigns
      - Email
      - Marketing
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.brevo.com/v3
    humanURL: https://developers.brevo.com/docs/getting-started
    properties:
      - url: https://developers.brevo.com/docs/getting-started
        type: Documentation
      - url: openapi/brevo-email-campaigns-openapi.yml
        type: OpenAPI
    description: The Brevo Email Campaigns API enables developers to create, manage, and send marketing email campaigns programmatically. It provides endpoints for building campaigns with HTML content or templates, scheduling sends, segmenting audiences, and managing sender identities. Developers can retrieve campaign statistics including open rates, click rates, and unsubscribes to measure performance and optimize future campaigns.
  - aid: brevo:contacts-api
    name: Brevo Contacts API
    tags:
      - Contacts
      - CRM
      - Lists
      - Segmentation
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.brevo.com/v3
    humanURL: https://developers.brevo.com/docs/how-it-works
    properties:
      - url: https://developers.brevo.com/docs/how-it-works
        type: Documentation
      - url: openapi/brevo-contacts-openapi.yml
        type: OpenAPI
    description: The Brevo Contacts API provides programmatic access to contact management features including creating, updating, and deleting contacts. Developers can organize contacts into lists, apply attributes and tags, import contacts in bulk, and build audience segments for targeted campaigns. The API also supports managing folders, contact attributes, and custom fields to structure contact data according to business needs.
  - aid: brevo:transactional-sms-api
    name: Brevo Transactional SMS API
    tags:
      - Messaging
      - Mobile
      - SMS
      - Transactional
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.brevo.com/v3
    humanURL: https://developers.brevo.com/docs/transactional-sms-endpoints
    properties:
      - url: https://developers.brevo.com/docs/transactional-sms-endpoints
        type: Documentation
      - url: openapi/brevo-transactional-sms-openapi.yml
        type: OpenAPI
    description: The Brevo Transactional SMS API allows developers to send non-promotional SMS messages such as order confirmations, delivery notifications, and verification codes using recipients' phone numbers. It supports sending individual messages with customizable sender names and provides endpoints for tracking SMS delivery status and activity. The API is designed for time-sensitive notifications that require immediate delivery to mobile devices.
  - aid: brevo:whatsapp-api
    name: Brevo WhatsApp API
    tags:
      - Messaging
      - Mobile
      - Transactional
      - WhatsApp
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.brevo.com/v3
    humanURL: https://developers.brevo.com/docs/whatsapp-messages
    properties:
      - url: https://developers.brevo.com/docs/whatsapp-messages
        type: Documentation
      - url: openapi/brevo-whatsapp-openapi.yml
        type: OpenAPI
    description: The Brevo WhatsApp API enables developers to send transactional WhatsApp messages such as order confirmations, status updates, and password reset links through the WhatsApp Business platform. It provides endpoints for sending template-based messages, managing WhatsApp campaigns, and tracking message delivery and read status. The API leverages WhatsApp's high engagement rates to deliver important notifications directly to users on their preferred messaging platform.
  - aid: brevo:ecommerce-api
    name: Brevo eCommerce API
    tags:
      - Categories
      - Ecommerce
      - Orders
      - Products
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.brevo.com/v3
    humanURL: https://developers.brevo.com/docs/import-your-products
    properties:
      - url: https://developers.brevo.com/docs/import-your-products
        type: Documentation
      - url: openapi/brevo-ecommerce-openapi.yml
        type: OpenAPI
    description: The Brevo eCommerce API allows developers to sync product catalogs, categories, and order data with the Brevo platform. It provides endpoints for importing and managing products, organizing them into categories, and tracking customer purchase history. This data integration enables merchants to attribute revenue to marketing campaigns, trigger automated workflows based on purchase behavior, and build product recommendation segments for targeted messaging.
  - aid: brevo:conversations-api
    name: Brevo Conversations API
    tags:
      - Chat
      - Conversations
      - Live Chat
      - Support
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.brevo.com/v3
    humanURL: https://developers.brevo.com/docs/getting-started
    properties:
      - url: https://developers.brevo.com/docs/getting-started
        type: Documentation
      - url: openapi/brevo-conversations-openapi.yml
        type: OpenAPI
    description: The Brevo Conversations API provides programmatic access to live chat and messaging features for customer support and engagement. It enables developers to manage chat conversations, send and receive messages, and integrate Brevo's chat widget into websites and applications. The API supports real-time communication with site visitors and can be used to build custom chat interfaces, automate responses, and route conversations to appropriate team members.
  - aid: brevo:webhooks-api
    name: Brevo Webhooks API
    tags:
      - Automation
      - Events
      - Notifications
      - Webhooks
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.brevo.com/v3
    humanURL: https://developers.brevo.com/docs/transactional-webhooks
    properties:
      - url: https://developers.brevo.com/docs/transactional-webhooks
        type: Documentation
      - url: openapi/brevo-webhooks-openapi.yml
        type: OpenAPI
      - url: asyncapi/brevo-webhooks-asyncapi.yml
        type: AsyncAPI
    description: The Brevo Webhooks API allows developers to receive real-time notifications when events occur across transactional emails, marketing campaigns, and conversations. By configuring webhook subscriptions, applications can automatically receive data for events such as email deliveries, opens, clicks, bounces, spam reports, and unsubscribes. This eliminates the need for polling and enables event-driven integrations that respond immediately to changes in messaging activity.
modified: '2026-03-20'
common:
  - type: JSON-LD
    url: json-ld/brevo-context.jsonld
  - type: JSONSchema
    url: json-schema/brevo-contact-schema.json
  - type: JSONSchema
    url: json-schema/brevo-email-event-schema.json
  - type: JSONSchema
    url: json-schema/brevo-order-schema.json
description: Send transactional emails with static or dynamic content using the Messaging API.
---

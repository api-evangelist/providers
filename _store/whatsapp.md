---
aid: whatsapp
name: WhatsApp
description: APIs for the WhatsApp messaging platform, enabling businesses to communicate with customers through the world's most popular messaging app.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/whatsapp/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-17'
specificationVersion: '0.19'
apis:
  - name: WhatsApp Business Platform API
    description: The Cloud API and On-Premises API that enables medium and large businesses to communicate with customers at scale.
    image: https://www.whatsapp.com/img/fb-post.jpg
    humanURL: https://developers.facebook.com/docs/whatsapp
    baseURL: https://graph.facebook.com/v21.0
    tags:
      - Business
      - Chat
      - Communications
      - Messaging
    properties:
      - type: Documentation
        url: https://developers.facebook.com/docs/whatsapp/cloud-api
      - type: OpenAPI
        url: openapi/whatsapp-cloud-api-openapi.yml
      - type: Authentication
        url: https://developers.facebook.com/docs/whatsapp/business-management-api/get-started
      - type: Documentation
        url: https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks
      - type: AsyncAPI
        url: asyncapi/whatsapp-webhooks-asyncapi.yml
      - type: JSONSchema
        url: json-schema/whatsapp-message-schema.json
      - type: Reference
        url: https://developers.facebook.com/docs/whatsapp/cloud-api/reference/messages
      - type: GettingStarted
        url: https://developers.facebook.com/docs/whatsapp/cloud-api/get-started
      - type: Pricing
        url: https://developers.facebook.com/docs/whatsapp/pricing
      - type: RateLimits
        url: https://developers.facebook.com/docs/whatsapp/cloud-api/overview#throughput
      - type: StatusPage
        url: https://metastatus.com/
      - type: Change Log
        url: https://developers.facebook.com/docs/whatsapp/cloud-api/changelog
      - type: Error Codes
        url: https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes
      - type: PostmanCollection
        url: https://www.postman.com/meta/whatsapp-business-platform/collection/wlk6lh4/whatsapp-cloud-api
      - type: Node.js SDK
        url: https://github.com/WhatsApp/WhatsApp-Nodejs-SDK
      - type: Sandbox
        url: https://business.whatsapp.com/developers/developer-hub
      - type: Migration Guide
        url: https://developers.facebook.com/docs/whatsapp/cloud-api/migrate-to-cloud-api
      - type: Media Reference
        url: https://developers.facebook.com/docs/whatsapp/cloud-api/reference/media
      - type: Phone Numbers Reference
        url: https://developers.facebook.com/docs/whatsapp/cloud-api/reference/phone-numbers
      - type: Business Profiles Reference
        url: https://developers.facebook.com/docs/whatsapp/cloud-api/reference/business-profiles
      - type: Two-Step Verification
        url: https://developers.facebook.com/docs/whatsapp/cloud-api/reference/two-step-verification
      - type: Versioning
        url: https://developers.facebook.com/docs/graph-api/guides/versioning
    contact:
      - type: Support
        url: https://developers.facebook.com/support/
      - type: Twitter
        url: https://twitter.com/WhatsApp
    aid: whatsapp:business-platform-api
  - name: WhatsApp Business Account Management API
    description: API for managing WhatsApp Business Accounts, phone numbers, and messaging templates.
    image: https://www.whatsapp.com/img/fb-post.jpg
    humanURL: https://developers.facebook.com/docs/whatsapp/business-management-api
    baseURL: https://graph.facebook.com/v21.0
    tags:
      - Accounts
      - Business
      - Management
      - Templates
    properties:
      - type: Documentation
        url: https://developers.facebook.com/docs/whatsapp/business-management-api
      - type: OpenAPI
        url: openapi/whatsapp-business-management-api-openapi.yml
      - type: Authentication
        url: https://developers.facebook.com/docs/whatsapp/business-management-api/get-started
      - type: JSONSchema
        url: json-schema/whatsapp-message-template-schema.json
      - type: GettingStarted
        url: https://developers.facebook.com/docs/whatsapp/business-management-api/get-started
      - type: PostmanCollection
        url: https://www.postman.com/meta/whatsapp-business-platform/collection/3kru5r6/whatsapp-business-management-api
      - type: Reference
        url: https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates
      - type: Change Log
        url: https://developers.facebook.com/docs/whatsapp/business-management-api/changelog
      - type: Error Codes
        url: https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes
      - type: RateLimits
        url: https://developers.facebook.com/docs/whatsapp/cloud-api/overview#throughput
    aid: whatsapp:business-account-management-api
  - name: WhatsApp Flows API
    description: API for creating structured, interactive forms and multi-step flows within WhatsApp conversations, enabling appointment booking, surveys, lead capture, and other guided experiences using a JSON-based screen definition format.
    image: https://www.whatsapp.com/img/fb-post.jpg
    humanURL: https://developers.facebook.com/docs/whatsapp/flows
    baseURL: https://graph.facebook.com/v21.0
    tags:
      - Flows
      - Forms
      - Interactive
      - Messaging
    properties:
      - type: Documentation
        url: https://developers.facebook.com/docs/whatsapp/flows
      - type: OpenAPI
        url: openapi/whatsapp-flows-api-openapi.yml
      - type: Reference
        url: https://developers.facebook.com/docs/whatsapp/flows/reference/components
      - type: JSONSchema
        url: json-schema/whatsapp-flow-json-schema.json
      - type: Change Log
        url: https://developers.facebook.com/docs/whatsapp/flows/changelogs
      - type: Error Codes
        url: https://developers.facebook.com/docs/whatsapp/flows/reference/error-codes
      - type: PostmanCollection
        url: https://www.postman.com/meta/whatsapp-business-platform/collection/y5swede/whatsapp-flows-api
      - type: GitHubRepository
        url: https://github.com/WhatsApp/WhatsApp-Flows-Tools
      - type: GettingStarted
        url: https://developers.facebook.com/docs/whatsapp/flows/gettingstarted
      - type: Authentication
        url: https://developers.facebook.com/docs/whatsapp/business-management-api/get-started
    aid: whatsapp:flows-api
  - name: WhatsApp On-Premises API
    description: The self-hosted version of the WhatsApp Business API that allowed businesses to run the API on their own infrastructure. This API was deprecated on October 23, 2025, and all users must migrate to the Cloud API.
    image: https://www.whatsapp.com/img/fb-post.jpg
    humanURL: https://developers.facebook.com/docs/whatsapp/on-premises
    baseURL: https://localhost:443
    tags:
      - Deprecated
      - Messaging
      - On-Premises
      - Self-Hosted
    properties:
      - type: Documentation
        url: https://developers.facebook.com/docs/whatsapp/on-premises
      - type: GettingStarted
        url: https://developers.facebook.com/docs/whatsapp/on-premises/get-started/installation
      - type: Deprecation Notice
        url: https://developers.facebook.com/docs/whatsapp/on-premises
      - type: PostmanCollection
        url: https://www.postman.com/meta/whatsapp-business-platform/collection/vdi189b/whatsapp-on-premises-api-deprecated
      - type: Migration Guide
        url: https://developers.facebook.com/docs/whatsapp/cloud-api/migrate-to-cloud-api
    aid: whatsapp:on-premises-api
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: TermsOfService
    url: https://www.whatsapp.com/legal/business-terms
  - type: PrivacyPolicy
    url: https://www.whatsapp.com/legal/privacy-policy-eea
  - type: Commerce Policy
    url: https://www.whatsapp.com/legal/commerce-policy
  - type: Developer Portal
    url: https://developers.facebook.com/
  - type: GettingStarted
    url: https://developers.facebook.com/docs/whatsapp/cloud-api/get-started
  - type: Authentication
    url: https://developers.facebook.com/docs/whatsapp/business-management-api/get-started
  - type: Best Practices
    url: https://developers.facebook.com/docs/whatsapp/cloud-api/best-practices
  - type: Use Cases
    url: https://business.whatsapp.com/products/business-platform
  - type: Change Log
    url: https://developers.facebook.com/docs/whatsapp/cloud-api/changelog
  - type: StatusPage
    url: https://metastatus.com/
  - type: Blog
    url: https://business.whatsapp.com/blog
  - type: Support
    url: https://developers.facebook.com/support/
  - type: Console
    url: https://developers.facebook.com/apps/
  - type: GitHub Organization
    url: https://github.com/WhatsApp
  - type: Community
    url: https://business.whatsapp.com/developers/developer-hub
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/whatsapp-cloud-api
  - type: Security
    url: https://www.whatsapp.com/security/WhatsApp-Security-Whitepaper.pdf
  - type: PostmanCollection
    url: https://www.postman.com/meta/whatsapp-business-platform/overview
  - type: Pricing
    url: https://business.whatsapp.com/products/platform-pricing
  - type: JSON-LD
    url: json-ld/whatsapp-context.jsonld
  - type: JSONSchema
    url: json-schema/whatsapp-webhook-payload-schema.json
  - type: Node.js SDK
    url: https://github.com/WhatsApp/WhatsApp-Nodejs-SDK
  - type: API Examples
    url: https://github.com/fbsamples/whatsapp-api-examples
  - type: Business Messaging Policy
    url: https://business.whatsapp.com/policy
  - type: Meta Terms
    url: https://www.whatsapp.com/legal/meta-terms-whatsapp-business
  - type: FAQ
    url: https://business.whatsapp.com/resources/faq
  - type: Sandbox
    url: https://business.whatsapp.com/developers/developer-hub
  - type: Versioning
    url: https://developers.facebook.com/docs/graph-api/guides/versioning
  - type: Migration Guide
    url: https://developers.facebook.com/docs/whatsapp/cloud-api/migrate-to-cloud-api
  - type: RateLimits
    url: https://developers.facebook.com/docs/whatsapp/cloud-api/overview#throughput
  - type: Error Codes
    url: https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes
  - type: Features
    data:
      - name: Cloud API
        description: Send and receive messages, media, and interactive content through Meta-hosted WhatsApp infrastructure.
      - name: Message Templates
        description: Pre-approved message templates for proactive customer communication with variable substitution.
      - name: Interactive Messages
        description: Buttons, lists, product catalogs, and flows for rich customer engagement.
      - name: Media Messaging
        description: Send and receive images, videos, documents, audio, stickers, and location data.
      - name: Webhooks
        description: Real-time notifications for incoming messages, delivery status, and account events.
      - name: Business Management API
        description: Manage WhatsApp Business accounts, phone numbers, and messaging limits.
      - name: Flows
        description: Build interactive multi-step forms and workflows within WhatsApp conversations.
      - name: Catalogs and Commerce
        description: Share product catalogs and enable in-chat commerce experiences.
      - name: Encryption
        description: End-to-end encryption for all messages and media.
      - name: Multi-Agent Support
        description: Route conversations to multiple agents with conversation assignment.
  - type: UseCases
    data:
      - name: Customer Support
        description: Provide real-time customer service and support through WhatsApp messaging.
      - name: Order Notifications
        description: Send order confirmations, shipping updates, and delivery notifications.
      - name: Appointment Reminders
        description: Send appointment reminders and allow rescheduling via interactive messages.
      - name: Marketing Campaigns
        description: Send promotional messages using approved templates to opted-in customers.
      - name: Two-Factor Authentication
        description: Send OTP codes and verification messages for account security.
      - name: Chatbot Integration
        description: Build automated conversational bots for FAQs and self-service workflows.
      - name: E-commerce
        description: Share product catalogs, process orders, and send payment reminders.
      - name: Healthcare Communication
        description: Send appointment reminders, test results, and health tips to patients.
  - type: Integrations
    data:
      - name: Meta Business Suite
        description: Manage WhatsApp alongside Facebook and Instagram from a unified dashboard.
      - name: Salesforce
        description: CRM integration for managing customer conversations and contact history.
      - name: Shopify
        description: E-commerce integration for order notifications and customer messaging.
      - name: HubSpot
        description: Marketing and sales integration for lead nurturing via WhatsApp.
      - name: Zendesk
        description: Help desk integration for ticketed WhatsApp customer support.
  - type: Solutions
    data:
      - name: WhatsApp Business Platform
        description: Cloud API and On-Premises API for medium and large businesses at scale.
      - name: WhatsApp Business App
        description: Free mobile app for small businesses with basic messaging features.
      - name: WhatsApp Flows
        description: Interactive forms and workflows within WhatsApp conversations.
type: Index
---

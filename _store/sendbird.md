---
name: Sendbird
description: Sendbird provides APIs and SDKs for in-app chat, voice, video, AI chatbots, and omnichannel business messaging. Used by over 4,000 companies to build real-time communication experiences for customer support, communities, and marketplace platforms.
image: https://sendbird.com/favicon.ico
url: https://sendbird.com
created: '2025-01-14'
modified: '2026-05-02'
specificationVersion: '0.18'
apis:
  - name: Sendbird Platform API
    description: The Sendbird Platform API provides server-side access to manage users, channels, messages, and moderation for chat applications. Supports group channels, open channels, direct messages, push notifications, and webhooks.
    image: https://sendbird.com/favicon.ico
    humanURL: https://sendbird.com/docs/chat/platform-api/
    baseURL: https://api-{application_id}.sendbird.com/v3
    tags:
      - Chat
      - Messaging
      - Real-Time Communication
      - Push Notifications
    properties:
      - type: Documentation
        url: https://sendbird.com/docs/chat/platform-api/
      - type: OpenAPI
        url: openapi/sendbird-platform-openapi.yml
      - type: Authentication
        url: https://sendbird.com/docs/chat/platform-api/v3/authentication
      - type: Rate Limits
        url: https://sendbird.com/docs/chat/platform-api/v3/rate-limits
    contact:
      - FN: Sendbird Support
        url: https://sendbird.com/contact-us/
  - name: Sendbird Calls API
    description: The Sendbird Calls API provides voice and video calling capabilities, enabling real-time one-on-one and group calls within applications.
    image: https://sendbird.com/favicon.ico
    humanURL: https://sendbird.com/docs/calls/
    baseURL: https://api-{application_id}.sendbird.com/v3
    tags:
      - Voice
      - Video
      - Calls
      - Real-Time Communication
    properties:
      - type: Documentation
        url: https://sendbird.com/docs/calls/
    contact:
      - FN: Sendbird Support
        url: https://sendbird.com/contact-us/
  - name: Sendbird Business Messaging API
    description: The Sendbird Business Messaging API enables omnichannel customer engagement through SMS, WhatsApp, and other messaging channels, supporting customer support and marketing use cases.
    image: https://sendbird.com/favicon.ico
    humanURL: https://sendbird.com/docs/business-messaging/
    baseURL: https://api-{application_id}.sendbird.com/v3
    tags:
      - Business Messaging
      - Omnichannel
      - Customer Support
      - WhatsApp
      - SMS
    properties:
      - type: Documentation
        url: https://sendbird.com/docs/business-messaging/
  - name: Sendbird AI Chatbot API
    description: The Sendbird AI Chatbot API enables building and deploying AI-powered chatbots within chat applications, supporting automated customer support and conversational AI experiences.
    image: https://sendbird.com/favicon.ico
    humanURL: https://sendbird.com/docs/ai-chatbot/
    baseURL: https://api-{application_id}.sendbird.com/v3
    tags:
      - AI
      - Chatbot
      - Customer Support
      - Automation
    properties:
      - type: Documentation
        url: https://sendbird.com/docs/ai-chatbot/
common:
  - type: Portal
    url: https://sendbird.com/docs/
  - type: Authentication
    url: https://sendbird.com/docs/chat/platform-api/v3/authentication
  - type: Rate Limits
    url: https://sendbird.com/docs/chat/platform-api/v3/rate-limits
  - type: Webhooks
    url: https://sendbird.com/docs/chat/platform-api/v3/webhooks
  - type: Changelog
    url: https://sendbird.com/release-notes/
  - type: Status
    url: https://status.sendbird.com/
  - type: Support
    url: https://sendbird.com/contact-us/
  - type: Pricing
    url: https://sendbird.com/pricing/
  - type: Blog
    url: https://sendbird.com/blog/
  - type: Privacy Policy
    url: https://sendbird.com/privacy-policy/
  - type: Terms of Service
    url: https://sendbird.com/terms-of-service/
  - type: Website
    url: https://sendbird.com
  - type: Dashboard
    url: https://dashboard.sendbird.com/
  - type: SpectralRules
    url: rules/sendbird-rules.yml
  - type: JSONLDContext
    url: json-ld/sendbird-context.jsonld
  - type: Vocabulary
    url: vocabulary/sendbird-vocabulary.yml
  - type: NaftikoCapabilities
    url: capabilities/customer-support-messaging.yaml
  - type: NaftikoCapabilities
    url: capabilities/community-chat.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---

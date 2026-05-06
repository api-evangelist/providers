---
aid: global-relay
url: https://raw.githubusercontent.com/api-evangelist/global-relay/refs/heads/main/apis.yml
apis:
  - aid: global-relay:conversation-archiving-api
    name: Global Relay Conversation Archiving API
    tags:
      - Archiving
      - Compliance
      - Messaging
    humanURL: https://developers.globalrelay.com/api/conversation-archiving-api/
    properties:
      - url: https://developers.globalrelay.com/api/conversation-archiving-api/
        type: Documentation
      - url: openapi/global-relay-conversation-archiving-api-openapi.yml
        type: OpenAPI
    description: The Global Relay Conversation Archiving API provides a RESTful interface to seamlessly integrate messaging platforms with the Global Relay Archive. It enables secure capture and preservation of one-to-one or multi-party conversations, including text messages, file attachments, reactions, edits, and deletions. The API uses OAuth 2.0 Client Credentials authentication and is rate limited to 1000 requests per minute for conversations and 100 per minute for files.
  - aid: global-relay:email-archiving-api
    name: Global Relay Email Archiving API
    tags:
      - Archiving
      - Compliance
      - Email
    humanURL: https://developers.globalrelay.com/api/email-archiving-api/
    properties:
      - url: https://developers.globalrelay.com/api/email-archiving-api/
        type: Documentation
      - url: openapi/global-relay-email-archiving-api-openapi.yml
        type: OpenAPI
    description: The Global Relay Email Archiving API provides a RESTful interface to capture and archive email content and metadata into the Global Relay Archive. It supports archiving emails with attachments, headers, and full message structure for compliance and regulatory requirements. Rate limited to 1000 requests per minute for emails and 100 per minute for files.
  - aid: global-relay:voice-archiving-api
    name: Global Relay Voice Archiving API
    tags:
      - Archiving
      - Compliance
      - Voice
    humanURL: https://developers.globalrelay.com/api/voice-archiving-api/
    properties:
      - url: https://developers.globalrelay.com/api/voice-archiving-api/
        type: Documentation
      - url: openapi/global-relay-voice-archiving-api-openapi.yml
        type: OpenAPI
    description: The Global Relay Voice Archiving API provides a RESTful interface to capture and archive audio and video recordings, including call recordings and meeting recordings, into the Global Relay Archive. The API ensures all voice and video communications are securely preserved for compliance. The maximum data payload per request is 3.5MB excluding file attachments.
  - aid: global-relay:event-archiving-api
    name: Global Relay Event Archiving API
    tags:
      - Archiving
      - Collaboration
      - Compliance
      - Social Media
    humanURL: https://developers.globalrelay.com/api/event-archiving-api/
    properties:
      - url: https://developers.globalrelay.com/api/event-archiving-api/
        type: Documentation
      - url: openapi/global-relay-event-archiving-api-openapi.yml
        type: OpenAPI
    description: The Global Relay Event Archiving API (EventFeed) provides a RESTful interface to integrate collaboration platforms, customer experience tools, and social media sites with the Global Relay Archive. It enables secure capture of event-based data including posts, comments, reactions, and activity feeds from various digital channels for compliance archiving.
name: Global Relay
tags:
  - Archiving
  - Compliance
  - Data Retention
  - Email Security
  - Regulatory Compliance
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://developers.globalrelay.com/
    name: Global Relay Developers
    type: Portal
    description: 'null'
  - url: https://www.globalrelay.com/connector/conversation-archiving-api/
    name: Conversation Archiving
    type: Documentation
    description: 'null'
  - url: https://www.globalrelay.com/connector/eventfeed-archiving-api/
    name: Event Feed Archiving
    type: Documentation
    description: 'null'
  - url: https://www.globalrelay.com/connector/voice-archiving-api/
    name: Voice Archiving
    type: Documentation
    description: 'null'
created: '2025-01-01'
modified: '2026-04-28'
position: Consumer
description: Global Relay is an enterprise-grade archiving and compliance platform for electronic communications including email, instant messaging, voice, video, and collaboration tools across regulated industries. It provides APIs for archiving conversations, emails, voice recordings, and event feeds from social media and collaboration platforms, ensuring organizations meet their compliance and regulatory requirements through secure, tamper-proof archiving with OAuth 2.0 authenticated REST APIs.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
---

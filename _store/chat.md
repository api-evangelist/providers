---
aid: chat
name: Chat
description: Topic-level profile capturing the Chat API category in the API Evangelist network. This profile defines a reference vocabulary and a generic OpenAPI shape for chat APIs that manage conversations, messages, and participants, and is used as a baseline when cataloguing chat platform APIs (such as Slack, Discord, Microsoft Teams, Twilio Conversations, and conversational AI platforms) into the broader catalogue.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/chat/refs/heads/main/apis.yml
type: Topic
access: 3rd-Party
position: Reference
tags:
  - Chat
  - Conversational AI
  - Conversations
  - Customer Support
  - Messaging
  - Real-time
created: '2024-01-15'
modified: '2026-04-23'
specificationVersion: '0.20'
apis:
  - aid: chat:reference-chat-api
    name: Reference Chat API
    description: Reference REST API shape for chat platforms covering conversation lifecycle (create/list/get), message send and history, participant management, and typing indicator events. Intended as a vocabulary and OpenAPI baseline for cataloguing concrete chat platform APIs.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://github.com/api-evangelist/chat
    baseURL: https://api.example.com/v1/chat
    tags:
      - Chat
      - Conversations
      - Messaging
    properties:
      - type: OpenAPI
        url: openapi/chat-reference-openapi.yml
      - type: Spectral
        url: spectral/chat-spectral.yml
      - type: NaftikoCapabilities
        url: naftiko/chat-capabilities.yml
common:
  - type: Repository
    url: https://github.com/api-evangelist/chat
  - type: Catalog
    url: https://apis.json/
  - type: JSONLD
    url: json-ld/chat-context.jsonld
  - type: JSONSchema
    url: json-schema/chat-conversation-schema.json
  - type: JSONSchema
    url: json-schema/chat-message-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

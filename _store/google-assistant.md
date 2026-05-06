---
aid: google-assistant
name: Google Assistant
description: The Google Assistant API enables developers to embed the Google Assistant into devices and applications. It provides conversational interfaces through gRPC and REST endpoints for sending text or audio queries and receiving responses. The API supports device model and instance registration, custom Actions with intents and scenes, and the Actions SDK for building conversational experiences that extend the Assistant's capabilities.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-assistant/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Actions on Google
  - Conversational AI
  - Google Assistant
  - Natural Language
  - Smart Home
  - Voice Assistant
apis:
  - aid: google-assistant:google-assistant
    name: Google Assistant API
    description: REST and gRPC API for embedding Google Assistant into devices and applications, managing device models and instances, and building conversational Actions.
    humanURL: https://developers.google.com/assistant
    baseURL: https://embeddedassistant.googleapis.com
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/google-assistant/refs/heads/main/openapi/openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/google-assistant/refs/heads/main/json-schema/google-assistant.json
      - type: JSONLD
        url: https://raw.githubusercontent.com/api-evangelist/google-assistant/refs/heads/main/json-ld/google-assistant.jsonld
common:
  - type: Getting Started
    url: https://developers.google.com/assistant/sdk/overview
  - type: Pricing
    url: https://developers.google.com/assistant
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/google-assistant/refs/heads/main/json-ld/google-assistant.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

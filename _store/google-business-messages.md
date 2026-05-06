---
aid: google-business-messages
name: Google Business Messages
description: The Google Business Messages API enables agents to send messages, create events, and manage customer satisfaction surveys within conversations. It allows businesses to communicate with customers directly through Google entry points such as Search and Maps.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-business-messages/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Business Communications
  - Conversations
  - Customer Support
  - Google
  - Messaging
apis:
  - aid: google-business-messages:google-business-messages
    name: Google Business Messages API
    description: Enables agents to send messages, create conversation events, update message receipts, and manage customer satisfaction surveys for business communications through Google.
    humanURL: https://developers.google.com/business-communications/business-messages
    baseURL: https://businessmessages.googleapis.com/v1
    properties:
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: JSONSchema
        url: json-schema/Message.json
    tags:
      - Conversations
      - Messaging
      - Surveys
common:
  - type: Getting Started
    url: https://developers.google.com/business-communications/business-messages/guides
  - type: Pricing
    url: https://developers.google.com/business-communications/business-messages
  - type: JSON-LD
    url: json-ld/context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

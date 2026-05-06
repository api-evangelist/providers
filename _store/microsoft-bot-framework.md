---
aid: microsoft-bot-framework
url: https://raw.githubusercontent.com/api-evangelist/microsoft-bot-framework/refs/heads/main/apis.yml
name: Microsoft Bot Framework
description: Microsoft Bot Framework provides APIs and SDKs for building conversational AI bots that work across multiple channels including Teams, Slack, and custom applications.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Bots
  - Conversational AI
  - Messaging
  - Bot Framework
  - Direct Line
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.20'
apis:
  - aid: microsoft-bot-framework:bot-connector
    name: Bot Connector REST API
    description: Send and receive messages across multiple channels including Teams, Slack, and web chat.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-connector-api-reference
    baseURL: https://api.botframework.com/
    tags:
      - Bots
      - Messaging
      - Conversational AI
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-connector-api-reference
  - aid: microsoft-bot-framework:direct-line
    name: Direct Line API
    description: Custom applications communicate directly with bots through REST and WebSocket connections.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-direct-line-3-0-concepts
    baseURL: https://directline.botframework.com/
    tags:
      - Bots
      - Direct Line
      - Custom Channels
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-direct-line-3-0-concepts
  - aid: microsoft-bot-framework:bot-builder-sdk
    name: Bot Builder SDK
    description: Libraries for building conversational AI bots in C#, JavaScript, Python, and Java.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/azure/bot-service/index-bf-sdk
    tags:
      - Bots
      - SDK
      - Development Framework
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/bot-service/index-bf-sdk
common:
  - type: Portal
    url: https://dev.botframework.com/
  - type: GitHub Organization
    url: https://github.com/microsoft/botframework-sdk
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/bot-services/
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

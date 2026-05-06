---
name: Azure Event Grid
description: Azure Event Grid provides APIs for publishing events to custom topics, managing event subscriptions with filtering, and configuring event delivery to endpoints including webhooks, Azure Functions, Event Hubs, and Storage Queues. It supports dead-lettering, retry policies, and custom event schemas.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Events
  - Event-Driven
  - Pub-Sub
  - Serverless
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.18'
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-event-grid/refs/heads/main/apis.yml
apis:
  - name: Azure Event Grid API
    description: Azure Event Grid provides APIs for publishing events to custom topics, managing event subscriptions with filtering, and configuring event delivery to endpoints including webhooks, Azure Functions, Event Hubs, and Storage Queues. It supports dead-lettering, retry policies, and custom event schemas.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/rest/api/eventgrid/
    baseURL: https://{topic}.{region}.eventgrid.azure.net/
    tags:
      - Events
      - Event-Driven
      - Pub-Sub
      - Serverless
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/eventgrid/
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/
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

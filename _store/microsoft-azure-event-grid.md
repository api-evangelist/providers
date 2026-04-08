---
aid: microsoft-azure-event-grid
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-event-grid/refs/heads/main/apis.yml
apis:
- aid: microsoft-azure-event-grid:azure-event-grid-api
  name: Azure Event Grid API
  tags:
  - Events\n      - Event-Driven\n      - Pub-Sub\n      - Serverless
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://{topic}.{region}.eventgrid.azure.net/
  humanURL: https://learn.microsoft.com/en-us/rest/api/eventgrid/
  properties:
  - url: https://learn.microsoft.com/en-us/rest/api/eventgrid/
    type: Documentation
  description: Azure Event Grid provides APIs for publishing events to custom topics, managing event subscriptions with filtering, and configuring event delivery to endpoints including webhooks, Azure Functions, Event Hubs, and Storage Queues. It supports dead-lettering, retry policies, and custom event schemas.
name: Microsoft Azure Event Grid
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: This article lists REST operation groups for Azure Event Grid.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


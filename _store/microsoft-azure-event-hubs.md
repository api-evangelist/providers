---
aid: microsoft-azure-event-hubs
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-event-hubs/refs/heads/main/apis.yml
apis:
- name: Azure Event Hubs REST API
  description: REST API for managing Event Hubs namespaces, event hubs, consumer groups, and sending/receiving events.
  image: https://azure.microsoft.com/svghandler/event-hubs/
  humanURL: https://learn.microsoft.com/en-us/rest/api/eventhub/
  baseURL: https://management.azure.com
  tags:
  - Events
  - Management
  - Streaming
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/rest/api/eventhub/
  - type: OpenAPI
    url: https://github.com/Azure/azure-rest-api-specs/tree/main/specification/eventhub/resource-manager
  - type: Swagger
    url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/eventhub/resource-manager/Microsoft.EventHub/stable/2021-11-01/eventhub.json
  - type: OpenAPI
    url: openapi/azure-event-hubs-management-openapi.yml
- name: Azure Event Hubs Data Plane API
  description: API for sending and receiving events from Event Hubs.
  image: https://azure.microsoft.com/svghandler/event-hubs/
  humanURL: https://learn.microsoft.com/en-us/rest/api/eventhub/event-hubs-runtime-rest
  baseURL: https://{namespace}.servicebus.windows.net
  tags:
  - Data Plane
  - Receive Events
  - Send Events
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/rest/api/eventhub/event-hubs-runtime-rest
  - type: OpenAPI
    url: https://github.com/Azure/azure-rest-api-specs/tree/main/specification/eventhub/data-plane
  - type: OpenAPI
    url: openapi/azure-event-hubs-data-plane-openapi.yml
- name: Azure Event Hubs Messaging API
  description: Event-driven messaging API for publishing and consuming events via AMQP 1.0, Kafka, and HTTPS protocols. Supports partitioned event streams, consumer groups, and publisher policies.
  image: https://azure.microsoft.com/svghandler/event-hubs/
  humanURL: https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-features
  baseURL: https://{namespace}.servicebus.windows.net
  tags:
  - AMQP
  - AsyncAPI
  - Event Streaming
  - Kafka
  - Messaging
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-features
  - type: AsyncAPI
    url: asyncapi/azure-event-hubs-messaging-asyncapi.yml
- name: Azure Event Hubs SDK
  description: Client libraries for various programming languages to interact with Event Hubs.
  image: https://azure.microsoft.com/svghandler/event-hubs/
  humanURL: https://learn.microsoft.com/en-us/azure/event-hubs/sdks
  baseURL: https://{namespace}.servicebus.windows.net
  tags:
  - Client Library
  - SDK
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/event-hubs/sdks
  - type: .NET SDK
    url: https://www.nuget.org/packages/Azure.Messaging.EventHubs/
  - type: Java SDK
    url: https://mvnrepository.com/artifact/com.azure/azure-messaging-eventhubs
  - type: Python SDK
    url: https://pypi.org/project/azure-eventhub/
  - type: JavaScript SDK
    url: https://www.npmjs.com/package/@azure/event-hubs
  - type: GitHub
    url: https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/eventhub
name: Azure Event Hubs
tags:
- Big Data
- Event Streaming
- IoT
- Message Ingestion
- Real-Time Processing
type: Contract
image: https://azure.microsoft.com/svghandler/event-hubs/
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Azure Event Hubs is a big data streaming platform and event ingestion service that can receive and process millions of events per second. It provides a distributed stream processing platform with low latency and seamless integration with Azure data and analytics services.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


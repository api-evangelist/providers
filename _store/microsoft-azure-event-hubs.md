---
name: Azure Event Hubs
description: Azure Event Hubs is a big data streaming platform and event ingestion service that can receive and process millions of events per second. It provides a distributed stream processing platform with low latency and seamless integration with Azure data and analytics services.
image: https://azure.microsoft.com/svghandler/event-hubs/
tags:
  - Big Data
  - Event Streaming
  - IoT
  - Message Ingestion
  - Real-Time Processing
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.18'
url: https://azure.microsoft.com/en-us/services/event-hubs/
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
common:
  - type: Portal
    url: https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.EventHub%2Fnamespaces
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-quickstart-portal
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/event-hubs/
  - type: Service Level Agreement
    url: https://azure.microsoft.com/en-us/support/legal/sla/event-hubs/
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/event-hubs/authenticate-application
  - type: Best Practices
    url: https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-best-practices
  - type: Samples
    url: https://github.com/Azure/azure-event-hubs/tree/master/samples
  - type: Support
    url: https://azure.microsoft.com/en-us/support/
  - type: Status
    url: https://status.azure.com/
  - type: Blog
    url: https://techcommunity.microsoft.com/t5/messaging-on-azure-and-net/bg-p/MessagingonAzureBlog
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/event-hubs/
  - type: Quotas
    url: https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-quotas
  - type: Terms of Service
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: SDKs
    url: https://learn.microsoft.com/en-us/azure/event-hubs/sdks
  - type: GitHub Organization
    url: https://github.com/Azure
  - type: Website
    url: https://azure.microsoft.com/en-us/services/event-hubs/
  - type: Login
    url: https://portal.azure.com/
  - type: Sign Up
    url: https://azure.microsoft.com/en-us/free/
  - type: Community
    url: https://learn.microsoft.com/en-us/answers/tags/165/azure-event-hubs/
  - type: Security
    url: https://learn.microsoft.com/en-us/azure/event-hubs/network-security
  - type: JSON Schema
    url: json-schema/azure-event-hubs-namespace.json
  - type: JSON Schema
    url: json-schema/azure-event-hubs-eventhub.json
  - type: JSON Schema
    url: json-schema/azure-event-hubs-consumer-group.json
  - type: JSON Schema
    url: json-schema/azure-event-hubs-event-data.json
  - type: JSON Schema
    url: json-schema/azure-event-hubs-schema-group.json
  - type: JSON-LD Context
    url: json-ld/azure-event-hubs-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---

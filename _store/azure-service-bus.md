---
aid: azure-service-bus
name: Azure Service Bus
description: Azure Service Bus is a fully managed enterprise message broker with message queues and publish-subscribe topics, providing reliable message delivery for decoupling applications and services in cloud and hybrid environments.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Azure
  - Cloud
  - Enterprise
  - Message Broker
  - Messaging
  - Pub/Sub
  - Queues
url: https://raw.githubusercontent.com/api-evangelist/azure-service-bus/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-18'
specificationVersion: '0.19'
apis:
  - aid: azure-service-bus:azure-service-bus
    name: Azure Service Bus
    description: Azure Service Bus is a fully managed enterprise message broker supporting message queues and publish-subscribe topics with features like dead-lettering, sessions, scheduled delivery, and transactions for building reliable distributed applications.
    humanURL: https://azure.microsoft.com/en-us/products/service-bus
    tags:
      - Azure
      - Cloud
      - Enterprise
      - Message Broker
      - Messaging
      - Pub/Sub
      - Queues
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/azure-service-bus/refs/heads/main/openapi/azure-service-bus-openapi.yml
      - type: AsyncAPI
        url: https://raw.githubusercontent.com/api-evangelist/azure-service-bus/refs/heads/main/asyncapi/azure-service-bus-asyncapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/azure-service-bus/refs/heads/main/json-schema/azure-service-bus-queue.yml
      - type: JSONLD
        url: https://raw.githubusercontent.com/api-evangelist/azure-service-bus/refs/heads/main/json-ld/azure-service-bus-context.jsonld
common:
  - type: Portal
    url: https://azure.microsoft.com/en-us/products/service-bus
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/service-bus-messaging/
  - type: GettingStarted
    url: https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quickstart-portal
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/service-bus/
  - type: GitHubRepository
    url: https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/servicebus
  - type: Blog
    url: https://azure.microsoft.com/en-us/blog/
  - type: Features
    data:
      - name: Message Queues
        description: Point-to-point messaging with FIFO delivery, sessions, dead-lettering, and duplicate detection for reliable asynchronous communication.
      - name: Publish-Subscribe Topics
        description: One-to-many messaging with topic subscriptions, filters, and actions for event-driven architectures.
      - name: Dead-Letter Queue
        description: Automatic routing of undeliverable or failed messages to a secondary queue for inspection and reprocessing.
      - name: Scheduled Delivery
        description: Schedule messages for future delivery at a specified time without requiring sender availability.
      - name: Transactions
        description: ACID transaction support for grouping multiple operations across queues and topics into atomic units.
      - name: Auto-Forwarding
        description: Automatically forward messages from one queue or subscription to another entity for chaining processing stages.
  - type: UseCases
    data:
      - name: Application Decoupling
        description: Decouple microservices and distributed applications using asynchronous messaging for independent scaling and deployment.
      - name: Load Leveling
        description: Buffer incoming requests during traffic spikes to protect backend services from overload.
      - name: Event-Driven Architecture
        description: Build event-driven systems using publish-subscribe topics to broadcast events to multiple subscribers.
      - name: Workflow Orchestration
        description: Coordinate multi-step business processes using message sessions and scheduled delivery for reliable workflow execution.
  - type: Integrations
    data:
      - name: Azure Functions
        description: Trigger serverless functions automatically when messages arrive in queues or topic subscriptions.
      - name: Azure Logic Apps
        description: Build automated workflows that send and receive Service Bus messages with no-code connectors.
      - name: Azure Event Grid
        description: Route Service Bus events to other Azure services for real-time event processing and monitoring.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

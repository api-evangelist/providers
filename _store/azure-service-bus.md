---
aid: azure-service-bus
url: https://raw.githubusercontent.com/api-evangelist/azure-service-bus/refs/heads/main/apis.yml
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
name: Azure Service Bus
tags:
- Azure
- Cloud
- Enterprise
- Message Broker
- Messaging
- Pub/Sub
- Queues
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Azure Service Bus is a fully managed enterprise message broker with message queues and publish-subscribe topics, providing reliable message delivery for decoupling applications and services in cloud and hybrid environments.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


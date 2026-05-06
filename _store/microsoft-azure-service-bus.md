---
aid: microsoft-azure-service-bus
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-service-bus/refs/heads/main/apis.yml
name: Azure Service Bus
description: Azure Service Bus is a fully managed enterprise message broker with message queues and publish-subscribe topics. It enables decoupling applications and services with reliable asynchronous messaging, supporting sessions, dead-lettering, scheduled delivery, duplicate detection, and transactions.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Enterprise Messaging
  - Message Broker
  - Messaging
  - Publish Subscribe
  - Queues
  - Topics
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.20'
apis:
  - aid: microsoft-azure-service-bus:rest-api
    name: Azure Service Bus REST API
    description: Azure Service Bus REST API provides operations for sending and receiving messages through queues and topics with support for sessions, dead-lettering, scheduled delivery, duplicate detection, and transactions.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/rest/api/servicebus/
    baseURL: https://{namespace}.servicebus.windows.net/
    tags:
      - Messaging
      - Queues
      - Subscriptions
      - Topics
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/servicebus/
      - type: Authentication
        url: https://learn.microsoft.com/en-us/rest/api/eventhub/authenticate-shared-access-signature
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/servicebus/resourceprovider
  - aid: microsoft-azure-service-bus:management-api
    name: Azure Service Bus Management REST API
    description: The management REST API enables namespace, queue, topic, and subscription configuration through Azure Resource Manager, including SKU, network rules, authorization rules, and disaster recovery configuration.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/rest/api/servicebus/controlplane-stable/
    baseURL: https://management.azure.com/
    tags:
      - Management
      - Namespaces
      - Provisioning
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/servicebus/controlplane-stable/
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/active-directory/develop/authentication-flows-app-scenarios
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/service-bus/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/service-bus-messaging/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quickstart-portal
  - type: SDKs
    url: https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-dotnet-get-started-with-queues
  - type: Status
    url: https://azure.status.microsoft/en-us/status
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
  - type: Blog
    url: https://azure.microsoft.com/en-us/blog/product/service-bus/
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/azureservicebus
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

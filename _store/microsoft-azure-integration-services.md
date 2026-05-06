---
aid: microsoft-azure-integration-services
name: Microsoft Azure Integration Services
description: Microsoft Azure Integration Services is a collection of cloud-based integration capabilities that connect applications, data, and processes across cloud and on-premises environments. It includes API Management, Logic Apps, Service Bus, Event Grid, and Event Hubs to enable enterprise integration, messaging, and event-driven architectures.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Management
  - Enterprise
  - Event-Driven
  - Integration
  - Messaging
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-integration-services/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-azure-integration-services:azure-api-management
    name: Azure API Management
    description: Azure API Management is a fully managed service that enables organizations to publish, secure, transform, maintain, and monitor APIs. It provides a gateway for routing API calls, enforcing usage policies, and providing developer portal capabilities for API consumers.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/azure/api-management/
    baseURL: https://management.azure.com/
    tags:
      - API Gateway
      - API Management
      - Azure
      - Developer Portal
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/api-management/
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/apimanagement/
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/api-management/get-started-create-service-instance
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/api-management/
      - type: Change Log
        url: https://learn.microsoft.com/en-us/azure/api-management/release-notes
  - aid: microsoft-azure-integration-services:azure-logic-apps
    name: Azure Logic Apps
    description: Azure Logic Apps is a cloud-based platform for creating and running automated workflows that integrate apps, data, services, and systems. It provides a visual designer and hundreds of pre-built connectors to build workflows without writing code, enabling business process automation and enterprise integration scenarios.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/azure/logic-apps/
    baseURL: https://management.azure.com/
    tags:
      - Azure
      - Integration
      - Low-Code
      - Workflow Automation
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/logic-apps/
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/logic/
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/logic-apps/quickstart-create-example-consumption-workflow
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/logic-apps/
      - type: Change Log
        url: https://learn.microsoft.com/en-us/azure/logic-apps/logic-apps-release-notes
  - aid: microsoft-azure-integration-services:azure-service-bus
    name: Azure Service Bus
    description: Azure Service Bus is a fully managed enterprise message broker with message queues and publish-subscribe topics. It decouples applications and services from each other, providing reliable asynchronous message delivery, ordered messaging, dead-lettering, and session support for complex integration workflows.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/azure/service-bus-messaging/
    baseURL: https://management.azure.com/
    tags:
      - Azure
      - Message Queue
      - Messaging
      - Publish-Subscribe
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/service-bus-messaging/
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/servicebus/
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quickstart-portal
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/service-bus/
      - type: Client Libraries
        url: https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview#client-libraries
  - aid: microsoft-azure-integration-services:azure-event-grid
    name: Azure Event Grid
    description: Azure Event Grid is a highly scalable, fully managed publish-subscribe event distribution service. It enables event-driven architectures by routing events from Azure services and custom sources to event handlers such as Azure Functions, Logic Apps, and webhooks, with support for filtering and fanout.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/azure/event-grid/
    baseURL: https://management.azure.com/
    tags:
      - Azure
      - Event-Driven
      - Eventing
      - Pub-Sub
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/event-grid/
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/eventgrid/
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/event-grid/custom-event-quickstart-portal
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/event-grid/
  - aid: microsoft-azure-integration-services:azure-event-hubs
    name: Azure Event Hubs
    description: Azure Event Hubs is a big data streaming platform and event ingestion service capable of receiving and processing millions of events per second. It is used for telemetry ingestion, application logging, and real-time analytics pipelines, with support for Apache Kafka protocol, AMQP, and HTTPS.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/azure/event-hubs/
    baseURL: https://management.azure.com/
    tags:
      - Azure
      - Big Data
      - Event Streaming
      - Kafka
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/event-hubs/
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/eventhub/
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-create
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/event-hubs/
      - type: Client Libraries
        url: https://learn.microsoft.com/en-us/azure/event-hubs/sdks
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Website
    url: https://azure.microsoft.com/en-us/products/category/integration
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/?product=integration
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/integration-services/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/
  - type: Blog
    url: https://techcommunity.microsoft.com/category/azure/blog/integrationsonazureblog
  - type: Support
    url: https://azure.microsoft.com/en-us/support/
  - type: Status
    url: https://azure.status.microsoft/en-us/status
  - type: Terms of Service
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: GitHub Organization
    url: https://github.com/Azure
  - type: YouTube
    url: https://www.youtube.com/@MicrosoftAzure
  - type: Community
    url: https://techcommunity.microsoft.com/category/azure
  - type: Console
    url: https://portal.azure.com/
  - type: Login
    url: https://portal.azure.com/
  - type: Sign Up
    url: https://azure.microsoft.com/en-us/free/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

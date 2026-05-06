---
name: Azure Web PubSub
description: Azure Web PubSub is a fully-managed service that enables building real-time, two-way messaging applications using publish-subscribe patterns over WebSockets. It supports broadcasting messages to clients in groups, sending messages to specific connections or users, and integrating with serverless event handlers for scalable real-time experiences.
image: https://azure.microsoft.com/svghandler/web-pubsub/
tags:
  - Messaging
  - Pub-Sub
  - Real-Time
  - Serverless
  - WebSockets
created: '2026-03-13'
modified: '2026-04-28'
url: https://azure.microsoft.com/en-us/services/web-pubsub/
specificationVersion: '0.18'
apis:
  - name: Azure Web PubSub Service REST API
    description: Data plane REST API for sending messages to connections, groups, and users on a Web PubSub service instance. Supports broadcast operations, targeted message delivery, and managing client lifecycle including disconnect operations and existence checks.
    image: https://azure.microsoft.com/svghandler/web-pubsub/
    humanURL: https://learn.microsoft.com/en-us/rest/api/webpubsub/dataplane
    baseURL: https://{instance}.webpubsub.azure.com
    tags:
      - Data Plane
      - Messaging
      - Web PubSub
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/webpubsub/dataplane
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/webpubsub/data-plane/WebPubSub/stable/2024-01-01/webpubsub.json
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/webpubsub/dataplane/web-pub-sub
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/howto-generate-client-tokens
  - name: Azure Web PubSub Management REST API
    description: Control plane REST API for provisioning and managing Azure Web PubSub service instances. Supports creating, scaling, configuring, regenerating access keys, and deleting Web PubSub resources through Azure Resource Manager.
    image: https://azure.microsoft.com/svghandler/web-pubsub/
    humanURL: https://learn.microsoft.com/en-us/rest/api/webpubsub
    baseURL: https://management.azure.com
    tags:
      - Control Plane
      - Resource Manager
      - Web PubSub
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/webpubsub
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/webpubsub/resource-manager/Microsoft.SignalRService/stable/2024-03-01/webpubsub.json
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/webpubsub/web-pub-sub
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios
  - name: Azure Web PubSub Hubs REST API
    description: REST API for managing hub configurations within a Web PubSub instance. Hubs provide logical isolation for messaging and allow per-hub configuration of event handlers, anonymous connect policies, and authorization settings.
    image: https://azure.microsoft.com/svghandler/web-pubsub/
    humanURL: https://learn.microsoft.com/en-us/rest/api/webpubsub/web-pub-sub-hubs
    baseURL: https://management.azure.com
    tags:
      - Hubs
      - Resource Manager
      - Web PubSub
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/webpubsub/web-pub-sub-hubs
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/webpubsub/web-pub-sub-hubs?view=rest-webpubsub-2024-03-01
  - name: Azure Web PubSub for Socket.IO REST API
    description: REST API for managing Azure Web PubSub for Socket.IO instances. Provides a fully managed Socket.IO server replacement that allows existing Socket.IO applications to scale to millions of connections without rewriting application code.
    image: https://azure.microsoft.com/svghandler/web-pubsub/
    humanURL: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/socketio-overview
    baseURL: https://management.azure.com
    tags:
      - Resource Manager
      - Socket.IO
      - Web PubSub
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/socketio-overview
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/webpubsub/web-pub-sub?view=rest-webpubsub-2024-03-01
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/socketio-quickstart
  - name: Azure Web PubSub Private Endpoint Connections REST API
    description: REST API for managing private endpoint connections to a Web PubSub service instance. Enables secure, private connectivity from virtual networks to Web PubSub through Azure Private Link without exposing traffic to the public internet.
    image: https://azure.microsoft.com/svghandler/web-pubsub/
    humanURL: https://learn.microsoft.com/en-us/rest/api/webpubsub/web-pub-sub-private-endpoint-connections
    baseURL: https://management.azure.com
    tags:
      - Networking
      - Private Endpoints
      - Resource Manager
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/webpubsub/web-pub-sub-private-endpoint-connections
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/webpubsub/web-pub-sub-private-endpoint-connections?view=rest-webpubsub-2024-03-01
  - name: Azure Web PubSub Shared Private Link Resources REST API
    description: REST API for managing shared private link resources for a Web PubSub service. Enables outbound private connectivity from Web PubSub to other Azure resources such as Key Vault and Storage when configuring upstream event handlers.
    image: https://azure.microsoft.com/svghandler/web-pubsub/
    humanURL: https://learn.microsoft.com/en-us/rest/api/webpubsub/web-pub-sub-shared-private-link-resources
    baseURL: https://management.azure.com
    tags:
      - Networking
      - Private Link
      - Resource Manager
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/webpubsub/web-pub-sub-shared-private-link-resources
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/webpubsub/web-pub-sub-shared-private-link-resources?view=rest-webpubsub-2024-03-01
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Website
    url: https://azure.microsoft.com/en-us/products/web-pubsub
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/howto-generate-client-tokens
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/web-pubsub/
  - type: SLA
    url: https://azure.microsoft.com/en-us/support/legal/sla/web-pubsub/
  - type: Status
    url: https://status.azure.com/
  - type: Blog
    url: https://devblogs.microsoft.com/azure-sdk/
  - type: Support
    url: https://azure.microsoft.com/en-us/support/options/
  - type: Terms of Service
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Sign Up
    url: https://azure.microsoft.com/en-us/free
  - type: Login
    url: https://portal.azure.com
  - type: SDKs
    url: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-server-sdk-js
  - type: SDK - JavaScript
    url: https://www.npmjs.com/package/@azure/web-pubsub
  - type: SDK - Python
    url: https://pypi.org/project/azure-messaging-webpubsubservice/
  - type: SDK - .NET
    url: https://www.nuget.org/packages/Azure.Messaging.WebPubSub
  - type: SDK - Java
    url: https://learn.microsoft.com/en-us/java/api/overview/azure/messaging-webpubsub-readme
  - type: SDK - Go
    url: https://pkg.go.dev/github.com/Azure/azure-sdk-for-go/sdk/messaging/azwebpubsub
  - type: CLI Tools
    url: https://learn.microsoft.com/en-us/cli/azure/webpubsub
  - type: Change Log
    url: https://azure.microsoft.com/en-us/updates/?product=web-pubsub
  - type: GitHub Organization
    url: https://github.com/Azure
  - type: GitHub Samples
    url: https://github.com/Azure/azure-webpubsub
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/azure-webpubsub
  - type: Community
    url: https://learn.microsoft.com/en-us/answers/tags/371/azure-web-pubsub
  - type: FAQ
    url: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/resource-faq
  - type: Quotas
    url: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/concept-billing-model
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

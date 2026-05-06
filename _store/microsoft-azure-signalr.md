---
aid: microsoft-azure-signalr
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-signalr/refs/heads/main/apis.yml
name: Azure SignalR Service
description: Azure SignalR Service REST API enables management of real-time web communication services. It supports creating SignalR instances, managing connections, sending messages to clients and groups, and configuring upstream endpoints for serverless real-time messaging.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Real-Time
  - WebSockets
  - SignalR
  - Messaging
  - Push
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.20'
apis:
  - aid: microsoft-azure-signalr:rest-api
    name: Azure SignalR Service REST API
    description: Azure SignalR Service REST API enables management of real-time web communication services. It supports creating SignalR instances, managing connections, sending messages to clients and groups, and configuring upstream endpoints for serverless real-time messaging.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/rest/api/signalr/
    baseURL: https://management.azure.com/
    tags:
      - Real-Time
      - WebSockets
      - Messaging
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/signalr/
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/active-directory/develop/authentication-flows-app-scenarios
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/signalr-service/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/azure-signalr/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/azure-signalr/signalr-quickstart-azure-signalr-service-arm-template
  - type: Status
    url: https://azure.status.microsoft/en-us/status
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
  - type: Blog
    url: https://azure.microsoft.com/en-us/blog/product/azure-signalr-service/
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/azure-signalr
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

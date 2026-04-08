---
aid: microsoft-copilot
url: https://raw.githubusercontent.com/api-evangelist/microsoft-copilot/refs/heads/main/apis.yml
apis:
- name: Microsoft Copilot API
  description: API for integrating Microsoft Copilot capabilities into applications.
  image: https://www.microsoft.com/en-us/microsoft-copilot/assets/images/copilot-icon.png
  humanUrl: https://learn.microsoft.com/en-us/copilot/
  baseUrl: https://api.copilot.microsoft.com
  tags:
  - AI
  - Chat
  - Completion
  properties:
  - type: documentation
    url: https://learn.microsoft.com/en-us/copilot/overview
  - type: openapi
    url: https://api.copilot.microsoft.com/openapi.json
  - type: authentication
    url: https://learn.microsoft.com/en-us/copilot/authentication
  - type: getting-started
    url: https://learn.microsoft.com/en-us/copilot/get-started
- name: Microsoft Graph API (Copilot Integration)
  description: Microsoft Graph API endpoints for accessing Copilot features within Microsoft 365, including the Copilot namespace with retrieval, chat, search, and meeting insights capabilities.
  humanUrl: https://learn.microsoft.com/en-us/graph/overview
  baseUrl: https://graph.microsoft.com/v1.0
  tags:
  - Integration
  - Microsoft 365
  - Microsoft Graph
  - Productivity
  properties:
  - type: documentation
    url: https://learn.microsoft.com/en-us/graph/api/overview
  - type: openapi
    url: https://graph.microsoft.com/openapi.json
  - type: swagger
    url: https://graph.microsoft.com/swagger.json
  - type: getting-started
    url: https://learn.microsoft.com/en-us/graph/use-the-api
- name: Microsoft 365 Copilot APIs
  description: REST APIs under the Microsoft Graph /copilot/ namespace that enable secure access to Microsoft 365 Copilot capabilities including retrieval, chat, and search, for use in custom applications and agents.
  humanUrl: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/copilot-apis-overview
  baseUrl: https://graph.microsoft.com/v1.0/copilot
  tags:
  - AI
  - Chat
  - Microsoft 365
  - RAG
  - Retrieval
  - Search
  properties:
  - type: documentation
    url: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/copilot-apis-overview
  - type: documentation
    url: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/api/ai-services/retrieval/overview
  - type: documentation
    url: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/api/ai-services/chat/overview
  - type: sdks
    url: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/sdks/api-libraries
  - type: openapi
    url: openapi/microsoft-copilot-openapi.yml
  - type: json-schema
    url: json-schema/microsoft-copilot-interaction-schema.json
  - type: json-ld-context
    url: json-ld/microsoft-copilot-context.jsonld
- name: Microsoft 365 Copilot Connectors API
  description: API for building custom connectors that bring external data into Microsoft Graph to enhance Microsoft 365 Copilot experiences including search and retrieval augmented generation.
  humanUrl: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/overview-copilot-connector
  baseUrl: https://graph.microsoft.com/v1.0
  tags:
  - Connectors
  - External Data
  - Indexing
  - Microsoft Graph
  properties:
  - type: documentation
    url: https://learn.microsoft.com/en-us/graph/connecting-external-content-connectors-api-overview
  - type: documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/connectors-api-overview?view=graph-rest-1.0
  - type: getting-started
    url: https://learn.microsoft.com/en-us/graph/custom-connector-sdk-sample-overview
  - type: sdks
    url: https://learn.microsoft.com/en-us/graph/custom-connector-sdk-overview
- name: Microsoft Copilot Studio API
  description: APIs for building, publishing, and integrating custom agents and copilots using Microsoft Copilot Studio, including Direct Line API for connecting web and custom applications.
  humanUrl: https://learn.microsoft.com/en-us/microsoft-copilot-studio/
  baseUrl: https://directline.botframework.com
  tags:
  - Agents
  - Bots
  - Copilot Studio
  - Direct Line
  - Low-Code
  properties:
  - type: documentation
    url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/
  - type: documentation
    url: https://learn.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-direct-line-3-0-api-reference?view=azure-bot-service-4.0
  - type: authentication
    url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-web-security
  - type: getting-started
    url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-connect-bot-to-custom-application
name: Microsoft Copilot
tags:
- Agents
- AI Assistant
- Artificial Intelligence
- Chatbot
- Copilot
- Extensibility
- Generative AI
- Microsoft 365
- Productivity
type: Contract
image: https://www.microsoft.com/en-us/microsoft-copilot/assets/images/copilot-icon.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Microsoft Copilot is an AI-powered assistant that helps users with productivity tasks, content generation, and information retrieval across Microsoft 365 applications and services.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


---
aid: microsoft-power-virtual-agents
name: Microsoft Power Virtual Agents
description: Microsoft Power Virtual Agents (now Copilot Studio) enables building AI-powered conversational chatbots without coding. It provides APIs for integrating bots with custom applications and managing bot configurations programmatically.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Chatbots
  - Conversational AI
  - Copilot Studio
  - Microsoft
url: https://raw.githubusercontent.com/api-evangelist/microsoft-power-virtual-agents/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-power-virtual-agents:direct-line-api
    name: Copilot Studio Direct Line API
    tags:
      - Chatbots
      - Conversational AI
      - Direct Line
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://directline.botframework.com/
    humanURL: https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-connect-bot-to-custom-application
    properties:
      - url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-connect-bot-to-custom-application
        type: Documentation
    description: The Copilot Studio Direct Line API enables custom applications to communicate with bots built in Microsoft Copilot Studio (formerly Power Virtual Agents). It provides REST endpoints for starting conversations, sending messages, receiving bot responses, and managing conversation sessions for custom channel integrations.
  - aid: microsoft-power-virtual-agents:bot-management-api
    name: Copilot Studio Bot Management API
    tags:
      - Administration
      - Bot Management
      - Copilot Studio
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/microsoft-copilot-studio/
    properties:
      - url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/
        type: Documentation
    description: The Copilot Studio management capabilities enable programmatic configuration and deployment of conversational AI agents. Developers can manage topics, entities, authentication settings, and channel configurations through Power Platform APIs and Dataverse integration.
common:
  - type: Portal
    url: https://copilotstudio.microsoft.com/
  - type: Website
    url: https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio
  - type: Documentation
    url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-get-started
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
  - type: Community
    url: https://community.powerplatform.com/forums/thread/?threadid=7de87c01-da4e-ef11-9f89-7c1e52206d8b
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

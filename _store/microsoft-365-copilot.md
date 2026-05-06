---
name: Microsoft 365 Copilot
description: Microsoft 365 Copilot is an AI-powered productivity tool that combines large language models (LLMs) with Microsoft 365 apps and business data to enhance creativity, productivity, and skills across Microsoft 365 applications.
image: https://www.microsoft.com/en-us/microsoft-365/copilot/copilot-logo.png
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.18'
url: https://www.microsoft.com/en-us/microsoft-365/copilot/apis.json
apis:
  - name: Microsoft Graph API
    description: The Microsoft Graph API provides access to Microsoft 365 data and services, enabling developers to integrate Copilot functionality with user data, documents, emails, calendar, and more.
    image: https://docs.microsoft.com/graph/images/microsoft-graph.png
    humanURL: https://developer.microsoft.com/en-us/graph
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - AI
      - Data Integration
      - Microsoft 365
      - Productivity
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/graph/overview
      - type: OpenAPI
        url: https://developer.microsoft.com/en-us/graph/docs/concepts/openapi
      - type: Authentication
        url: https://docs.microsoft.com/en-us/graph/auth/
      - type: SDKs
        url: https://docs.microsoft.com/en-us/graph/sdks/sdks-overview
      - type: Changelog
        url: https://developer.microsoft.com/en-us/graph/changelog
  - name: Microsoft Copilot Studio API
    description: Microsoft Copilot Studio allows developers to create, customize, and extend Copilot experiences with custom plugins and connectors to integrate business-specific data and workflows.
    image: https://www.microsoft.com/en-us/copilot/studio-icon.png
    humanURL: https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio
    baseURL: https://api.powerplatform.com/
    tags:
      - AI Development
      - Automation
      - Custom Plugins
      - Low Code
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-get-started
      - type: Plugin Development
        url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/copilot-plugins-overview
      - type: Connectors
        url: https://learn.microsoft.com/en-us/connectors/
      - type: Tutorials
        url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/tutorials
  - name: Microsoft 365 Copilot Extensibility API
    description: API for extending Microsoft 365 Copilot with custom skills, plugins, and connectors to integrate third-party services and enterprise data sources.
    image: https://www.microsoft.com/en-us/microsoft-365/copilot/extensibility-icon.png
    humanURL: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/
    baseURL: https://api.microsoft365.com/copilot/v1
    tags:
      - Custom Skills
      - Extensibility
      - Integration
      - Plugins
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/
      - type: Plugin Manifest
        url: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/create-plugin
      - type: Teams Message Extensions
        url: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/build-message-extensions
      - type: API Plugins
        url: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/api-plugins
      - type: Samples
        url: https://github.com/microsoft/copilot-plugins-samples
  - name: Azure OpenAI Service API
    description: Azure OpenAI Service provides REST API access to OpenAI's language models, which power Microsoft 365 Copilot's AI capabilities with enterprise-grade security and compliance.
    image: https://azure.microsoft.com/en-us/services/openai/openai-icon.png
    humanURL: https://azure.microsoft.com/en-us/products/ai-services/openai-service
    baseURL: https://{resource-name}.openai.azure.com/
    tags:
      - AI
      - Azure
      - GPT
      - Language Models
      - Machine Learning
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/ai-services/openai/
      - type: API Reference
        url: https://learn.microsoft.com/en-us/azure/ai-services/openai/reference
      - type: Quickstart
        url: https://learn.microsoft.com/en-us/azure/ai-services/openai/quickstart
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/cognitive-services/openai-service/
      - type: Models
        url: https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Developer Portal
    url: https://developer.microsoft.com/
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
  - type: Blog
    url: https://www.microsoft.com/en-us/microsoft-365/blog/
  - type: Status
    url: https://status.azure.com/
  - type: GitHub Organization
    url: https://github.com/microsoft
maintainers:
  - name: Microsoft
    email: support@microsoft.com
    url: https://www.microsoft.com/
tags:
  - Artificial Intelligence
  - Copilot
  - Enterprise
  - LLM
  - Microsoft 365
  - Natural Language Processing
  - Productivity
---

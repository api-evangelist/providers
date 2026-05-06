---
name: Microsoft Copilot
description: Microsoft Copilot is an AI-powered assistant that helps users with productivity tasks, content generation, and information retrieval across Microsoft 365 applications and services.
image: https://www.microsoft.com/en-us/microsoft-copilot/assets/images/copilot-icon.png
url: https://copilot.microsoft.com
created: '2024-01-15'
modified: '2026-04-18'
specificationVersion: '0.18'
type: Contract
access: 3rd-Party
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
apis:
  - name: Microsoft Copilot API
    description: API for integrating Microsoft Copilot capabilities into applications.
    image: https://www.microsoft.com/en-us/microsoft-copilot/assets/images/copilot-icon.png
    humanURL: https://learn.microsoft.com/en-us/copilot/
    baseURL: https://api.copilot.microsoft.com
    tags:
      - AI
      - Chat
      - Completion
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/copilot/overview
      - type: OpenAPI
        url: https://api.copilot.microsoft.com/openapi.json
      - type: Authentication
        url: https://learn.microsoft.com/en-us/copilot/authentication
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/copilot/get-started
  - name: Microsoft Graph API (Copilot Integration)
    description: Microsoft Graph API endpoints for accessing Copilot features within Microsoft 365, including the Copilot namespace with retrieval, chat, search, and meeting insights capabilities.
    humanURL: https://learn.microsoft.com/en-us/graph/overview
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Integration
      - Microsoft 365
      - Microsoft Graph
      - Productivity
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/overview
      - type: OpenAPI
        url: https://graph.microsoft.com/openapi.json
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/graph/use-the-api
  - name: Microsoft 365 Copilot APIs
    description: REST APIs under the Microsoft Graph /copilot/ namespace that enable secure access to Microsoft 365 Copilot capabilities including retrieval, chat, and search, for use in custom applications and agents.
    humanURL: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/copilot-apis-overview
    baseURL: https://graph.microsoft.com/v1.0/copilot
    tags:
      - AI
      - Chat
      - Microsoft 365
      - RAG
      - Retrieval
      - Search
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/copilot-apis-overview
      - type: Documentation
        url: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/api/ai-services/retrieval/overview
        title: Retrieval API
      - type: Documentation
        url: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/api/ai-services/chat/overview
        title: Chat API
      - type: SDK
        url: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/sdks/api-libraries
      - type: OpenAPI
        url: openapi/microsoft-copilot-openapi.yml
      - type: JSONSchema
        url: json-schema/microsoft-copilot-interaction-schema.json
      - type: JSONLD
        url: json-ld/microsoft-copilot-context.jsonld
  - name: Microsoft 365 Copilot Connectors API
    description: API for building custom connectors that bring external data into Microsoft Graph to enhance Microsoft 365 Copilot experiences including search and retrieval augmented generation.
    humanURL: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/overview-copilot-connector
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Connectors
      - External Data
      - Indexing
      - Microsoft Graph
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/connecting-external-content-connectors-api-overview
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/connectors-api-overview?view=graph-rest-1.0
        title: Connectors API Reference
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/graph/custom-connector-sdk-sample-overview
      - type: SDK
        url: https://learn.microsoft.com/en-us/graph/custom-connector-sdk-overview
  - name: Microsoft Copilot Studio API
    description: APIs for building, publishing, and integrating custom agents and copilots using Microsoft Copilot Studio, including Direct Line API for connecting web and custom applications.
    humanURL: https://learn.microsoft.com/en-us/microsoft-copilot-studio/
    baseURL: https://directline.botframework.com
    tags:
      - Agents
      - Bots
      - Copilot Studio
      - Direct Line
      - Low-Code
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-direct-line-3-0-api-reference?view=azure-bot-service-4.0
        title: Direct Line API Reference
      - type: Authentication
        url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-web-security
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-connect-bot-to-custom-application
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: GettingStarted
    url: https://learn.microsoft.com/en-us/copilot/get-started
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/active-directory/develop/
  - type: TermsOfService
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Pricing
    url: https://www.microsoft.com/en-us/microsoft-copilot/pricing
  - type: Support
    url: https://support.microsoft.com/copilot
  - type: Blog
    url: https://blogs.microsoft.com/blog/tag/copilot/
  - type: StatusPage
    url: https://status.microsoft.com
  - type: Portal
    url: https://developer.microsoft.com/en-us/microsoft-365/copilot
  - type: SDK
    url: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/sdks/api-libraries
  - type: CodeExamples
    url: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/samples
  - type: ChangeLog
    url: https://learn.microsoft.com/en-us/copilot/microsoft-365/release-notes
  - type: ReleaseNotes
    url: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/whats-new
  - type: Security
    url: https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-privacy
  - type: GitHubRepository
    url: https://github.com/microsoft/CopilotStudioSamples
  - type: Features
    data:
      - name: Retrieval API
        description: Retrieve relevant enterprise content from Microsoft 365 using AI-powered retrieval augmented generation with permissions and sensitivity label awareness.
      - name: Search API
        description: Perform semantic search across Microsoft 365 content including SharePoint, OneDrive, and Exchange with AI-enhanced ranking.
      - name: Chat API
        description: Programmatically start and continue conversations with Microsoft 365 Copilot grounded in enterprise and web search data.
      - name: Interaction Export
        description: Export and audit Copilot interaction history across the organization for compliance and governance purposes.
      - name: Change Notifications
        description: Subscribe to real-time notifications for Copilot interactions and events across Microsoft 365.
      - name: Copilot Studio
        description: Low-code platform for building custom agents, copilots, and conversational AI experiences.
      - name: Connectors
        description: Bring external data into Microsoft Graph to enhance Copilot search and retrieval capabilities.
      - name: Extensibility
        description: Extend Copilot with custom plugins, agents, and API integrations using declarative or code-first approaches.
  - type: UseCases
    data:
      - name: Enterprise Knowledge Retrieval
        description: Build applications that retrieve relevant enterprise content from Microsoft 365 while respecting permissions and compliance controls.
      - name: AI-Assisted Productivity
        description: Integrate Copilot capabilities into line-of-business applications for document summarization, drafting, and data analysis.
      - name: Custom Agent Development
        description: Create domain-specific AI agents using Copilot Studio that automate workflows and answer questions from custom data sources.
      - name: Compliance and Governance
        description: Monitor and audit Copilot usage across the organization with interaction history export and change notifications.
  - type: Integrations
    data:
      - name: Microsoft 365
        description: Deep integration with Word, Excel, PowerPoint, Outlook, Teams, and other Microsoft 365 applications.
      - name: Microsoft Graph
        description: Access organizational data through the Microsoft Graph API for retrieval, search, and chat capabilities.
      - name: Azure Active Directory
        description: Enterprise authentication and authorization using Azure AD with OAuth 2.0 and OIDC.
      - name: Power Platform
        description: Connect Copilot with Power Automate, Power Apps, and Power BI for end-to-end workflow automation.
---

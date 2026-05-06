---
aid: microsoft-products
name: Microsoft Products
description: A collection of APIs for various Microsoft products and services.
image: https://www.microsoft.com/favicon.ico
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Cloud
  - Enterprise
  - Microsoft
  - Productivity
url: https://raw.githubusercontent.com/api-evangelist/microsoft-products/refs/heads/main/apis.yml
apis:
  - name: Microsoft Graph API
    description: Unified API endpoint for accessing Microsoft 365, Windows, and Enterprise Mobility + Security services.
    image: https://docs.microsoft.com/favicon.ico
    humanUrl: https://developer.microsoft.com/en-us/graph
    baseUrl: https://graph.microsoft.com
    tags:
      - Azure-Ad
      - Graph
      - Microsoft-365
      - Unified-Api
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/graph/overview
      - type: OpenAPI
        url: https://raw.githubusercontent.com/microsoftgraph/msgraph-metadata/master/openapi/v1.0/openapi.yaml
      - type: Authentication
        url: https://docs.microsoft.com/en-us/graph/auth/
      - type: SDKs
        url: https://docs.microsoft.com/en-us/graph/sdks/sdks-overview
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/active-directory/
  - name: Azure REST API
    description: APIs for managing Azure resources and services.
    image: https://azure.microsoft.com/favicon.ico
    humanUrl: https://azure.microsoft.com/en-us/develop/
    baseUrl: https://management.azure.com
    tags:
      - Azure
      - Cloud
      - Iaas
      - Infrastructure
      - Paas
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/rest/api/azure/
      - type: OpenAPI
        url: https://github.com/Azure/azure-rest-api-specs
      - type: Authentication
        url: https://docs.microsoft.com/en-us/azure/active-directory/develop/
      - type: Portal
        url: https://portal.azure.com
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/
  - name: Microsoft 365 API
    description: APIs for Microsoft 365 services including Exchange, SharePoint, and Teams.
    image: https://www.microsoft.com/microsoft-365/favicon.ico
    humanUrl: https://developer.microsoft.com/en-us/microsoft-365
    baseUrl: https://api.office.com
    tags:
      - Collaboration
      - Exchange
      - Office-365
      - Productivity
      - Sharepoint
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/office/
      - type: Developer Portal
        url: https://developer.microsoft.com/en-us/microsoft-365/dev-program
      - type: SDKs
        url: https://docs.microsoft.com/en-us/office/dev/add-ins/
  - name: Microsoft Teams API
    description: API for building apps and bots for Microsoft Teams.
    image: https://docs.microsoft.com/favicon.ico
    humanUrl: https://developer.microsoft.com/en-us/microsoft-teams
    baseUrl: https://graph.microsoft.com/v1.0/teams
    tags:
      - Chat
      - Collaboration
      - Meetings
      - Teams
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/microsoftteams/platform/
      - type: Bot Framework
        url: https://dev.botframework.com/
      - type: App Studio
        url: https://docs.microsoft.com/en-us/microsoftteams/platform/concepts/build-and-test/app-studio-overview
  - name: Azure Cognitive Services API
    description: AI and machine learning APIs for vision, speech, language, and decision making.
    image: https://azure.microsoft.com/favicon.ico
    humanUrl: https://azure.microsoft.com/en-us/services/cognitive-services/
    baseUrl: https://api.cognitive.microsoft.com
    tags:
      - Ai
      - Cognitive-Services
      - Computer-Vision
      - Machine-Learning
      - Nlp
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/azure/cognitive-services/
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/cognitive-services/
      - type: SDKs
        url: https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-apis-create-account
  - name: Power Platform API
    description: APIs for Power Apps, Power Automate, and Power BI.
    image: https://powerplatform.microsoft.com/favicon.ico
    humanUrl: https://powerplatform.microsoft.com/
    baseUrl: https://api.powerplatform.com
    tags:
      - Automation
      - Business-Intelligence
      - Low-Code
      - Power-Platform
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/power-platform/
      - type: Connectors
        url: https://docs.microsoft.com/en-us/connectors/
      - type: Power BI REST API
        url: https://docs.microsoft.com/en-us/rest/api/power-bi/
  - name: Dynamics 365 API
    description: APIs for Dynamics 365 business applications.
    image: https://dynamics.microsoft.com/favicon.ico
    humanUrl: https://dynamics.microsoft.com/
    baseUrl: https://api.businesscentral.dynamics.com
    tags:
      - Business-Applications
      - Crm
      - Dynamics
      - Erp
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/dynamics365/
      - type: Web API
        url: https://docs.microsoft.com/en-us/dynamics365/customer-engagement/web-api/
      - type: Developer Guide
        url: https://docs.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/
  - name: Xbox Live API
    description: APIs for Xbox Live gaming services.
    image: https://www.xbox.com/favicon.ico
    humanUrl: https://developer.microsoft.com/en-us/games/xbox
    baseUrl: https://xboxlive.com
    tags:
      - Achievements
      - Gaming
      - Multiplayer
      - Xbox
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/gaming/xbox-live/
      - type: Developer Portal
        url: https://developer.microsoft.com/en-us/games/
      - type: Unity Plugin
        url: https://github.com/microsoft/xbox-live-unity-plugin
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Portal
    url: https://developer.microsoft.com/
  - type: Authentication
    url: https://docs.microsoft.com/en-us/azure/active-directory/develop/
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/
  - type: Support
    url: https://support.microsoft.com/
  - type: Status
    url: https://status.azure.com/
---

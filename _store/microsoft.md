---
name: Microsoft
description: Collection of Microsoft's primary APIs and developer resources.
image: https://www.microsoft.com/favicon.ico
url: https://www.microsoft.com
created: '2024'
modified: '2026-05-04'
apis:
  - name: Microsoft Graph API
    description: Unified API endpoint for accessing Microsoft 365, Windows, and Enterprise Mobility + Security services.
    image: https://learn.microsoft.com/en-us/graph/images/microsoft-graph.png
    humanURL: https://developer.microsoft.com/en-us/graph
    baseURL: https://graph.microsoft.com
    tags:
      - Azure AD
      - Office 365
      - OneDrive
      - Outlook
      - Teams
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/overview
      - type: OpenAPI
        url: https://learn.microsoft.com/en-us/graph/api/overview
      - type: Authentication
        url: https://learn.microsoft.com/en-us/graph/auth/
      - type: SDKs
        url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
      - type: Graph Explorer
        url: https://developer.microsoft.com/en-us/graph/graph-explorer
      - type: Changelog
        url: https://learn.microsoft.com/en-us/graph/whats-new-overview
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/graph/use-the-api
      - type: OpenAPI
        url: openapi/microsoft-graph-openapi.yml
      - type: JSONSchema
        url: json-schema/microsoft-graph-user-schema.json
      - type: JSONSchema
        url: json-schema/microsoft-graph-group-schema.json
  - name: Azure REST API
    description: REST APIs for managing Azure resources and services.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/
    baseURL: https://management.azure.com
    tags:
      - Azure
      - Cloud
      - Infrastructure
      - Resources
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/
      - type: API Reference
        url: https://learn.microsoft.com/en-us/rest/api/?view=Azure
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/active-directory/develop/
      - type: SDKs
        url: https://azure.microsoft.com/en-us/downloads/
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/
      - type: OpenAPI
        url: openapi/microsoft-azure-rest-openapi.yml
      - type: JSONSchema
        url: json-schema/microsoft-azure-resource-group-schema.json
  - name: Azure OpenAI Service API
    description: Access to OpenAI's powerful language models through Azure.
    humanURL: https://azure.microsoft.com/en-us/products/ai-services/openai-service
    baseURL: https://{resource-name}.openai.azure.com
    tags:
      - AI
      - GPT
      - Machine Learning
      - OpenAI
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/ai-services/openai/
      - type: API Reference
        url: https://learn.microsoft.com/en-us/azure/ai-services/openai/reference
      - type: Quickstart
        url: https://learn.microsoft.com/en-us/azure/ai-services/openai/quickstart
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/cognitive-services/openai-service/
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/managed-identity
      - type: OpenAPI
        url: openapi/microsoft-azure-openai-openapi.yml
  - name: Azure Cognitive Services API
    description: APIs for vision, speech, language, and decision-making AI capabilities.
    humanURL: https://azure.microsoft.com/en-us/products/ai-services/
    baseURL: https://{region}.api.cognitive.microsoft.com
    tags:
      - AI
      - Computer Vision
      - Language
      - Machine Learning
      - Speech
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/ai-services/
      - type: API Reference
        url: https://learn.microsoft.com/en-us/rest/api/cognitiveservices/
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/cognitive-services/
      - type: SDKs
        url: https://learn.microsoft.com/en-us/azure/ai-services/cognitive-services-apis-create-account-client-library
      - type: OpenAPI
        url: openapi/microsoft-azure-cognitive-services-openapi.yml
  - name: Microsoft Teams API
    description: Build apps and bots for Microsoft Teams.
    humanURL: https://developer.microsoft.com/en-us/microsoft-teams
    baseURL: https://graph.microsoft.com/v1.0/teams
    tags:
      - Chat
      - Collaboration
      - Messaging
      - Teams
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/microsoftteams/platform/
      - type: API Reference
        url: https://learn.microsoft.com/en-us/graph/teams-concept-overview
      - type: App Templates
        url: https://learn.microsoft.com/en-us/microsoftteams/platform/samples/app-templates
      - type: SDKs
        url: https://learn.microsoft.com/en-us/microsoftteams/platform/get-started/get-started-overview
      - type: OpenAPI
        url: openapi/microsoft-teams-openapi.yml
      - type: JSONSchema
        url: json-schema/microsoft-teams-team-schema.json
  - name: OneDrive API
    description: Access and manage files stored in OneDrive and SharePoint.
    humanURL: https://developer.microsoft.com/en-us/onedrive
    baseURL: https://graph.microsoft.com/v1.0/me/drive
    tags:
      - Files
      - OneDrive
      - SharePoint
      - Storage
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/onedrive/developer/
      - type: API Reference
        url: https://learn.microsoft.com/en-us/onedrive/developer/rest-api/
      - type: Samples
        url: https://github.com/OneDrive/samples
      - type: OpenAPI
        url: openapi/microsoft-onedrive-openapi.yml
      - type: JSONSchema
        url: json-schema/microsoft-drive-item-schema.json
  - name: Power Platform API
    description: APIs for Power Apps, Power Automate, and Power BI.
    humanURL: https://learn.microsoft.com/en-us/power-platform/
    baseURL: https://api.powerplatform.com
    tags:
      - Automation
      - Business Intelligence
      - Low Code
      - Power Apps
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/power-platform/admin/programmability-overview
      - type: Power Apps API
        url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview
      - type: Power Automate API
        url: https://learn.microsoft.com/en-us/power-automate/web-api
      - type: OpenAPI
        url: openapi/microsoft-power-platform-openapi.yml
  - name: Bing Search APIs
    description: Integrate Bing search capabilities into applications.
    humanURL: https://www.microsoft.com/en-us/bing/apis/bing-web-search-api
    baseURL: https://api.bing.microsoft.com/v7.0
    tags:
      - Bing
      - Image Search
      - Search
      - Web Search
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/bing/search-apis/
      - type: API Reference
        url: https://learn.microsoft.com/en-us/bing/search-apis/bing-web-search/reference/endpoints
      - type: Pricing
        url: https://www.microsoft.com/en-us/bing/apis/pricing
      - type: OpenAPI
        url: openapi/microsoft-bing-search-openapi.yml
  - name: SharePoint REST API
    description: REST service for remotely interacting with SharePoint data using standard REST and OData web protocol standards.
    humanURL: https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/get-to-know-the-sharepoint-rest-service
    baseURL: https://{tenant}.sharepoint.com/_api
    tags:
      - Collaboration
      - Content Management
      - Documents
      - SharePoint
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/get-to-know-the-sharepoint-rest-service
      - type: API Reference
        url: https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/complete-basic-operations-using-sharepoint-rest-endpoints
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/sharepoint/dev/apis/sharepoint-rest-graph
      - type: Microsoft Graph Integration
        url: https://learn.microsoft.com/en-us/graph/sharepoint-concept-overview
      - type: OpenAPI
        url: openapi/microsoft-sharepoint-openapi.yml
  - name: Power BI REST API
    description: REST APIs for embedded analytics, administration, governance, and content management in Power BI.
    humanURL: https://learn.microsoft.com/en-us/power-bi/developer/
    baseURL: https://api.powerbi.com/v1.0/myorg
    tags:
      - Analytics
      - Business Intelligence
      - Dashboards
      - Reports
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/power-bi/developer/
      - type: API Reference
        url: https://learn.microsoft.com/en-us/rest/api/power-bi/
      - type: SDKs
        url: https://learn.microsoft.com/en-us/power-bi/developer/embedded/
      - type: Authentication
        url: https://learn.microsoft.com/en-us/power-bi/developer/embedded/register-app
      - type: OpenAPI
        url: openapi/microsoft-power-bi-openapi.yml
  - name: Azure DevOps REST API
    description: REST APIs for managing Azure DevOps Services including projects, pipelines, repositories, and work items.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/
    baseURL: https://dev.azure.com/{organization}/_apis
    tags:
      - CI/CD
      - DevOps
      - Git
      - Pipelines
      - Work Items
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/devops/integrate/how-to/call-rest-api
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/authentication-guidance
      - type: Samples
        url: https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/rest/samples
      - type: OpenAPI
        url: openapi/microsoft-azure-devops-openapi.yml
  - name: Dynamics 365 REST API
    description: REST APIs for Dynamics 365 business applications including Customer Engagement, Business Central, and Dataverse.
    humanURL: https://learn.microsoft.com/en-us/rest/dynamics365/
    baseURL: https://{org}.api.crm.dynamics.com/api/data/v9.2
    tags:
      - Business Applications
      - CRM
      - Dynamics
      - ERP
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/dynamics365/
      - type: API Reference
        url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/reference/about
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview
      - type: Authentication
        url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/authenticate-oauth
      - type: OpenAPI
        url: openapi/microsoft-dynamics-365-openapi.yml
  - name: LinkedIn API
    description: APIs for LinkedIn integrations covering consumer, marketing, sales, talent, learning, and compliance solutions.
    humanURL: https://developer.linkedin.com/
    baseURL: https://api.linkedin.com/v2
    tags:
      - Marketing
      - Professional Network
      - Recruiting
      - Social
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/linkedin/
      - type: Authentication
        url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/getting-access
      - type: API Reference
        url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts
      - type: SDKs
        url: https://learn.microsoft.com/en-us/linkedin/shared/development-resources/api-clients
      - type: OpenAPI
        url: openapi/microsoft-linkedin-openapi.yml
  - name: Azure Communication Services API
    description: Multichannel communication APIs for adding voice, video, chat, SMS, and email to applications.
    humanURL: https://learn.microsoft.com/en-us/azure/communication-services/
    baseURL: https://{resource}.communication.azure.com
    tags:
      - Chat
      - Communication
      - Email
      - SMS
      - Video
      - Voice
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/communication-services/
      - type: API Reference
        url: https://learn.microsoft.com/en-us/rest/api/communication/
      - type: SDKs
        url: https://learn.microsoft.com/en-us/azure/communication-services/concepts/sdk-options
      - type: Pricing
        url: https://azure.microsoft.com/en-us/products/communication-services/#pricing
      - type: GitHub
        url: https://github.com/Azure/Communication
      - type: OpenAPI
        url: openapi/microsoft-azure-communication-services-openapi.yml
  - name: Microsoft Entra ID API
    description: APIs for identity and access management including user authentication, authorization, and directory services via Microsoft Graph.
    humanURL: https://learn.microsoft.com/en-us/entra/identity-platform/
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Authentication
      - Authorization
      - Directory
      - Identity
      - Security
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/entra/identity-platform/
      - type: API Reference
        url: https://learn.microsoft.com/en-us/graph/identity-network-access-overview
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app
      - type: Authentication
        url: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview
      - type: OpenAPI
        url: openapi/microsoft-entra-id-openapi.yml
  - name: Microsoft Outlook API
    description: APIs for integrating with Outlook mail, calendar, and contacts through Microsoft Graph.
    humanURL: https://developer.microsoft.com/en-us/outlook
    baseURL: https://graph.microsoft.com/v1.0/me
    tags:
      - Calendar
      - Contacts
      - Email
      - Outlook
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/outlook/
      - type: Mail API Reference
        url: https://learn.microsoft.com/en-us/graph/outlook-mail-concept-overview
      - type: Calendar API Reference
        url: https://learn.microsoft.com/en-us/graph/outlook-calendar-concept-overview
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/outlook/rest/get-started
      - type: OpenAPI
        url: openapi/microsoft-outlook-openapi.yml
  - name: Microsoft Intune API
    description: APIs for managing devices, apps, and compliance policies through Microsoft Graph for enterprise mobility management.
    humanURL: https://learn.microsoft.com/en-us/graph/intune-concept-overview
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Compliance
      - Device Management
      - Endpoint Management
      - Mobile
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/intune-concept-overview
      - type: API Reference
        url: https://learn.microsoft.com/en-us/graph/api/resources/intune-graph-overview
      - type: Authentication
        url: https://learn.microsoft.com/en-us/intune/intune-service/developer/intune-graph-apis
      - type: SDKs
        url: https://learn.microsoft.com/en-us/intune/intune-service/developer/app-sdk-get-started
      - type: OpenAPI
        url: openapi/microsoft-intune-openapi.yml
      - type: JSONSchema
        url: json-schema/microsoft-managed-device-schema.json
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
common:
  - type: Developer Portal
    url: https://developer.microsoft.com/
  - type: Azure Portal
    url: https://portal.azure.com
  - type: Status Page
    url: https://status.azure.com/
  - type: Support
    url: https://support.microsoft.com/
  - type: Privacy Policy
    url: https://privacy.microsoft.com/
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Blog
    url: https://devblogs.microsoft.com/
  - type: Authentication
    url: https://learn.microsoft.com/en-us/entra/identity-platform/
  - type: Sign Up
    url: https://developer.microsoft.com/en-us/microsoft-365/dev-program
  - type: Forum
    url: https://learn.microsoft.com/en-us/answers/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/calculator/
  - type: GitHub
    url: https://github.com/microsoft
  - type: JSON-LD
    url: json-ld/microsoft-context.jsonld
  - type: JSON-LD
    url: json-ld/microsoft-graph-context.jsonld
  - type: JSONSchema
    url: json-schema/microsoft-graph-user-schema.json
  - type: JSONSchema
    url: json-schema/microsoft-graph-group-schema.json
  - type: JSONSchema
    url: json-schema/microsoft-azure-resource-group-schema.json
  - type: JSONSchema
    url: json-schema/microsoft-teams-team-schema.json
  - type: JSONSchema
    url: json-schema/microsoft-drive-item-schema.json
  - type: JSONSchema
    url: json-schema/microsoft-managed-device-schema.json
  - type: Features
    data:
      - 'Microsoft (Azure + 365 + Foundry + Graph): hundreds of services across Cloud + Productivity + AI'
      - 'Detailed pricing: see https://www.microsoft.com/en-us/microsoft-365/business/compare-all-plans'
      - 'Service: Virtual Machines'
      - 'Service: Blob Storage'
      - 'Service: SQL Database'
      - 'Service: Cosmos DB'
      - 'Service: Functions'
      - 'Service: API Management'
      - 'Service: Front Door (CDN)'
      - 'Service: DNS'
      - 'Service: Virtual Network'
      - 'Service: Entra ID (formerly AD)'
      - 'Service: Key Vault'
      - 'Service: Monitor'
      - 'Service: Log Analytics'
      - 'Service: AKS (Kubernetes)'
      - 'Service: Container Apps'
      - 'Service: Container Registry'
      - 'Service: Service Bus'
      - 'Service: Event Grid'
      - 'Service: Event Hubs'
      - 'Service: Microsoft Foundry / OpenAI Service'
      - 'Service: Cognitive Services (Speech, Vision, Language, Translator)'
      - 'Service: Synapse Analytics'
      - 'Service: Data Factory'
      - 'Service: Stream Analytics'
      - 'Service: Databricks (Azure)'
      - 'Service: Power BI'
      - 'Service: Bot Service'
      - 'Service: Communication Services'
      - 'Service: Microsoft 365 (Business / Enterprise)'
      - 'Service: Microsoft Graph API'
      - 'Service: Bing Search API'
      - 'Service: Microsoft Foundry (OpenAI + Mistral + others)'
      - 'Service: Power Platform APIs'
      - 'Service: Dynamics 365 APIs'
      - 'Service: Microsoft Defender APIs'
      - 'Service: Intune'
      - 'Service: Teams'
      - 'Service: GitHub (separate billing)'
    sources:
      - https://www.microsoft.com/en-us/microsoft-365/business/compare-all-plans
      - https://focus.finops.org/
    updated: '2026-05-04'
---

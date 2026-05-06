---
name: Power BI
description: Microsoft Power BI is a business analytics service that delivers insights to enable fast, informed decisions. It provides interactive visualizations and business intelligence capabilities with an interface simple enough for end users to create their own reports and dashboards.
image: https://powerbi.microsoft.com/pictures/shared/social/social-default-image.png
url: https://powerbi.microsoft.com
created: '2024'
modified: '2026-04-18'
specificationVersion: '0.18'
type: Index
access: 3rd-Party
position: Consumer
tags:
  - Analytics
  - Business Intelligence
  - Dashboards
  - Data Analysis
  - Reporting
  - Visualization
apis:
  - name: Power BI REST API
    description: The Power BI REST API provides service endpoints for embedding, administration, governance, and user resources.
    image: https://powerbi.microsoft.com/pictures/shared/social/social-default-image.png
    humanURL: https://docs.microsoft.com/en-us/rest/api/power-bi/
    baseURL: https://api.powerbi.com
    tags:
      - Dashboards
      - Datasets
      - Embeddings
      - Reports
      - REST
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/rest/api/power-bi/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/powerbi/data-plane/Microsoft.PowerBI/stable/v1.0/powerbi.json
      - type: OpenAPI
        url: openapi/power-bi-rest-api-openapi.yml
      - type: JSONLD
        url: json-ld/power-bi-rest-context.jsonld
      - type: Authentication
        url: https://docs.microsoft.com/en-us/power-bi/developer/embedded/get-azuread-access-token
      - type: GettingStarted
        url: https://docs.microsoft.com/en-us/power-bi/developer/embedded/embedding-content
      - type: RateLimits
        url: https://docs.microsoft.com/en-us/power-bi/developer/automation/api-rest-api-limitations
      - type: SDK
        url: https://docs.microsoft.com/en-us/javascript/api/overview/powerbi/
        title: JavaScript SDK
      - type: ChangeLog
        url: https://docs.microsoft.com/en-us/power-bi/developer/embedded/embedded-analytics-power-bi-changelog
      - type: Troubleshooting
        url: https://learn.microsoft.com/en-us/power-bi/developer/embedded/troubleshoot-rest-api
  - name: Power BI Embedded
    description: Azure service that enables ISVs and developers to embed Power BI visuals, reports, and dashboards into their applications.
    image: https://powerbi.microsoft.com/pictures/shared/social/social-default-image.png
    humanURL: https://azure.microsoft.com/en-us/services/power-bi-embedded/
    baseURL: https://api.powerbi.com
    tags:
      - Azure
      - Embedded
      - Integration
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/power-bi/developer/embedded/
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/power-bi-embedded/
      - type: Sandbox
        url: https://playground.powerbi.com/
      - type: CodeExamples
        url: https://github.com/Microsoft/PowerBI-Developer-Samples
      - type: APIReference
        url: https://learn.microsoft.com/en-us/rest/api/power-bi-embedded/
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/power-bi/developer/embedded/embed-organization-app
      - type: Authentication
        url: https://learn.microsoft.com/en-us/power-bi/developer/embedded/embed-tokens
      - type: SDK
        url: https://learn.microsoft.com/en-us/javascript/api/overview/powerbi/embedded-analytics-client-api
        title: JavaScript SDK
      - type: SDK
        url: https://github.com/microsoft/PowerBI-CSharp
        title: .NET SDK
  - name: Power BI Management API
    description: API for managing Power BI capacity, workspaces, and tenant settings.
    image: https://powerbi.microsoft.com/pictures/shared/social/social-default-image.png
    humanURL: https://docs.microsoft.com/en-us/rest/api/power-bi/admin
    baseURL: https://api.powerbi.com/v1.0/myorg/admin
    tags:
      - Administration
      - Governance
      - Management
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/rest/api/power-bi/admin
      - type: Authentication
        url: https://docs.microsoft.com/en-us/power-bi/admin/service-admin-reference
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/power-bi/admin/service-admin-health
  - name: Power BI Push Datasets API
    description: The Push Datasets API enables real-time data streaming by allowing applications to create push datasets and post rows of data directly into Power BI datasets.
    image: https://powerbi.microsoft.com/pictures/shared/social/social-default-image.png
    humanURL: https://learn.microsoft.com/en-us/rest/api/power-bi/push-datasets
    baseURL: https://api.powerbi.com
    tags:
      - Datasets
      - Push
      - Real-Time
      - Streaming
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/power-bi/push-datasets
      - type: RateLimits
        url: https://learn.microsoft.com/en-us/power-bi/developer/embedded/push-datasets-limitations
      - type: Authentication
        url: https://learn.microsoft.com/en-us/power-bi/developer/embedded/get-azuread-access-token
  - name: Power BI Report Server REST API
    description: The Power BI Report Server REST API provides programmatic access to report server catalog objects such as folders, reports, KPIs, data sources, datasets, refresh plans, and subscriptions.
    image: https://powerbi.microsoft.com/pictures/shared/social/social-default-image.png
    humanURL: https://learn.microsoft.com/en-us/rest/api/power-bi-report/
    baseURL: https://api.powerbi.com
    tags:
      - On-Premises
      - Report Server
      - Reports
      - SSRS
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/power-bi-report/
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/power-bi/report-server/rest-api
      - type: ChangeLog
        url: https://learn.microsoft.com/en-us/power-bi/report-server/changelog
      - type: ReleaseNotes
        url: https://learn.microsoft.com/en-us/power-bi/report-server/whats-new
  - name: Power BI Visuals API
    description: The Power BI Visuals API enables developers to create custom visuals that can be used in Power BI reports and dashboards, extending the built-in visualization capabilities.
    image: https://powerbi.microsoft.com/pictures/shared/social/social-default-image.png
    humanURL: https://learn.microsoft.com/en-us/power-bi/developer/visuals/
    baseURL: https://api.powerbi.com
    tags:
      - Charts
      - Custom Visuals
      - Visualization
      - Visuals
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/power-bi/developer/visuals/
      - type: APIReference
        url: https://learn.microsoft.com/en-us/power-bi/developer/visuals/visual-api
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/power-bi/developer/visuals/develop-power-bi-visuals
      - type: ChangeLog
        url: https://learn.microsoft.com/en-us/power-bi/developer/visuals/changelog
      - type: Authentication
        url: https://learn.microsoft.com/en-us/power-bi/developer/visuals/authentication-api
common:
  - type: Portal
    url: https://app.powerbi.com
  - type: DeveloperPortal
    url: https://powerbi.microsoft.com/en-us/developers/
  - type: Blog
    url: https://powerbi.microsoft.com/en-us/blog/
  - type: Support
    url: https://powerbi.microsoft.com/en-us/support/
  - type: StatusPage
    url: https://powerbi.microsoft.com/en-us/status/
  - type: TermsOfService
    url: https://powerbi.microsoft.com/en-us/terms-of-service/
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: GitHubRepository
    url: https://github.com/Microsoft/PowerBI-JavaScript
  - type: GitHubRepository
    url: https://github.com/microsoft/PowerBI-Developer-Samples
    title: Developer Samples
  - type: LinkedIn
    url: https://www.linkedin.com/showcase/microsoft-power-bi/
  - type: X
    url: https://twitter.com/MSPowerBI
  - type: YouTube
    url: https://www.youtube.com/user/mspowerbi
  - type: Documentation
    url: https://learn.microsoft.com/en-us/power-bi/
  - type: Pricing
    url: https://www.microsoft.com/en-us/power-platform/products/power-bi/pricing
  - type: SignUp
    url: https://app.powerbi.com/signupredirect?pbi_source=web
  - type: Login
    url: https://app.powerbi.com/signin
  - type: ReleaseNotes
    url: https://learn.microsoft.com/en-us/power-bi/fundamentals/whats-new
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/powerbi
  - type: JSONLD
    url: json-ld/power-bi-context.jsonld
  - type: JSONSchema
    url: json-schema/power-bi-dataset-schema.json
  - type: JSONSchema
    url: json-schema/power-bi-report-schema.json
  - type: SDK
    url: https://github.com/microsoft/PowerBI-CSharp
    title: .NET SDK
  - type: Features
    data:
      - name: Interactive Dashboards
        description: Create and share interactive dashboards with real-time data visualizations and drill-down capabilities.
      - name: Natural Language Queries
        description: Ask questions about your data in plain English and get instant visualizations with Q&A.
      - name: Data Connectivity
        description: Connect to hundreds of data sources including databases, cloud services, files, and streaming data.
      - name: Embedded Analytics
        description: Embed Power BI reports and dashboards into custom applications using REST APIs and JavaScript SDK.
      - name: Paginated Reports
        description: Create pixel-perfect, print-ready reports designed for printing or PDF generation.
      - name: Real-Time Streaming
        description: Push real-time data to dashboards with streaming datasets and live tile updates.
      - name: Row-Level Security
        description: Control data access at the row level based on user identity and roles.
      - name: Dataflows
        description: Self-service data preparation with Power Query Online for creating reusable data transformation logic.
  - type: UseCases
    data:
      - name: Executive Dashboards
        description: Provide C-suite executives with real-time KPI dashboards for data-driven decision making.
      - name: Sales Analytics
        description: Track sales performance, pipeline metrics, and revenue forecasting with interactive reports.
      - name: Financial Reporting
        description: Automate financial reporting with scheduled refreshes and pixel-perfect paginated reports.
      - name: Embedded Analytics for ISVs
        description: Embed Power BI visualizations into SaaS applications to provide analytics to end customers.
      - name: IoT Monitoring
        description: Visualize real-time IoT sensor data with streaming datasets and live dashboard tiles.
      - name: HR Analytics
        description: Analyze workforce metrics, retention rates, and employee engagement across the organization.
  - type: Integrations
    data:
      - name: Microsoft Teams
        description: View and interact with Power BI reports directly within Microsoft Teams channels and chats.
      - name: Excel
        description: Analyze Power BI datasets in Excel with connected tables and PivotTables.
      - name: SharePoint
        description: Embed Power BI reports in SharePoint Online pages for enterprise-wide distribution.
      - name: Azure Synapse Analytics
        description: Connect to Azure Synapse workspaces for big data analytics and data warehousing.
      - name: Dynamics 365
        description: Pre-built analytics templates and data connectors for Dynamics 365 business applications.
      - name: Power Automate
        description: Trigger automated workflows based on Power BI data alerts and refresh events.
      - name: Azure Active Directory
        description: Enterprise authentication and authorization with Azure AD for secure API access.
      - name: Salesforce
        description: Connect to Salesforce data with native connectors for CRM analytics and reporting.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---

---
aid: power-bi
url: https://raw.githubusercontent.com/api-evangelist/power-bi/refs/heads/main/apis.yml
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
  - type: Authentication
    url: https://docs.microsoft.com/en-us/power-bi/developer/embedded/get-azuread-access-token
  - type: Getting Started
    url: https://docs.microsoft.com/en-us/power-bi/developer/embedded/embedding-content
  - type: Rate Limits
    url: https://docs.microsoft.com/en-us/power-bi/developer/automation/api-rest-api-limitations
  - type: SDKs
    url: https://docs.microsoft.com/en-us/javascript/api/overview/powerbi/
  - type: Changelog
    url: https://docs.microsoft.com/en-us/power-bi/developer/embedded/embedded-analytics-power-bi-changelog
  - type: Troubleshooting
    url: https://learn.microsoft.com/en-us/power-bi/developer/embedded/troubleshoot-rest-api
  - type: Push Datasets Limitations
    url: https://learn.microsoft.com/en-us/power-bi/developer/embedded/push-datasets-limitations
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
  - type: Playground
    url: https://playground.powerbi.com/
  - type: Code Samples
    url: https://github.com/Microsoft/PowerBI-Developer-Samples
  - type: Reference
    url: https://learn.microsoft.com/en-us/rest/api/power-bi-embedded/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/power-bi/developer/embedded/embed-organization-app
  - type: Authentication
    url: https://learn.microsoft.com/en-us/power-bi/developer/embedded/embed-tokens
  - type: SDKs
    url: https://learn.microsoft.com/en-us/javascript/api/overview/powerbi/embedded-analytics-client-api
  - type: .NET SDK
    url: https://github.com/microsoft/PowerBI-CSharp
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
  - type: Getting Started
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
  - type: Limitations
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
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/power-bi/report-server/rest-api
  - type: Changelog
    url: https://learn.microsoft.com/en-us/power-bi/report-server/changelog
  - type: What's New
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
  - type: Reference
    url: https://learn.microsoft.com/en-us/power-bi/developer/visuals/visual-api
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/power-bi/developer/visuals/develop-power-bi-visuals
  - type: Changelog
    url: https://learn.microsoft.com/en-us/power-bi/developer/visuals/changelog
  - type: Authentication
    url: https://learn.microsoft.com/en-us/power-bi/developer/visuals/authentication-api
name: Power BI
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Analysis
- Reporting
- Visualization
type: Contract
image: https://powerbi.microsoft.com/pictures/shared/social/social-default-image.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Microsoft Power BI is a business analytics service that delivers insights to enable fast, informed decisions. It provides interactive visualizations and business intelligence capabilities with an interface simple enough for end users to create their own reports and dashboards.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


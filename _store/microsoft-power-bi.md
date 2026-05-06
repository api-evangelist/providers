---
aid: microsoft-power-bi
name: Microsoft Power BI
description: Microsoft Power BI is a business analytics service that delivers insights to enable fast, informed decisions. It provides REST APIs for accessing and managing Power BI resources including reports, dashboards, datasets, and workspaces programmatically.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Business Intelligence
  - Dashboards
  - Microsoft
  - Reports
url: https://raw.githubusercontent.com/api-evangelist/microsoft-power-bi/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-power-bi:rest-api
    name: Power BI REST API
    tags:
      - Analytics
      - Business Intelligence
      - Dashboards
      - Reports
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.powerbi.com/v1.0/myorg/
    humanURL: https://learn.microsoft.com/en-us/rest/api/power-bi/
    properties:
      - url: https://learn.microsoft.com/en-us/rest/api/power-bi/
        type: Documentation
      - url: https://learn.microsoft.com/en-us/rest/api/power-bi/datasets
        type: Reference
    description: The Power BI REST API enables programmatic access to Power BI resources including datasets, reports, dashboards, workspaces, and dataflows. Developers can automate report deployment, manage workspace permissions, refresh datasets, export reports, and embed Power BI content in custom applications.
  - aid: microsoft-power-bi:embedded-api
    name: Power BI Embedded API
    tags:
      - Business Intelligence
      - Embedded Analytics
      - White Label
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.powerbi.com/v1.0/myorg/
    humanURL: https://learn.microsoft.com/en-us/power-bi/developer/embedded/
    properties:
      - url: https://learn.microsoft.com/en-us/power-bi/developer/embedded/
        type: Documentation
    description: Power BI Embedded enables developers to embed interactive Power BI reports, dashboards, and tiles into custom applications. It provides client-side JavaScript APIs for rendering and interacting with embedded content, supporting scenarios like white-label analytics, custom filtering, and programmatic report navigation.
  - aid: microsoft-power-bi:admin-api
    name: Power BI Admin REST API
    tags:
      - Administration
      - Governance
      - Tenant Management
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.powerbi.com/v1.0/myorg/admin/
    humanURL: https://learn.microsoft.com/en-us/rest/api/power-bi/admin
    properties:
      - url: https://learn.microsoft.com/en-us/rest/api/power-bi/admin
        type: Documentation
    description: The Power BI Admin REST API provides tenant-level administrative capabilities for managing Power BI across an organization. It enables administrators to audit user activities, manage workspaces, scan datasets for governance, retrieve tenant settings, and monitor capacity usage and performance metrics.
  - aid: microsoft-power-bi:push-datasets-api
    name: Power BI Push Datasets API
    tags:
      - Datasets
      - Real-Time Data
      - Streaming
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.powerbi.com/v1.0/myorg/
    humanURL: https://learn.microsoft.com/en-us/power-bi/developer/automation/api-automatic-retention-policy-for-real-time-data
    properties:
      - url: https://learn.microsoft.com/en-us/power-bi/developer/automation/api-automatic-retention-policy-for-real-time-data
        type: Documentation
    description: The Power BI Push Datasets API enables real-time data streaming into Power BI datasets. Developers can push rows of data directly to streaming datasets for real-time dashboard visualizations, supporting IoT scenarios, live monitoring, and event-driven analytics without requiring scheduled data refreshes.
common:
  - type: Portal
    url: https://app.powerbi.com/
  - type: Website
    url: https://powerbi.microsoft.com/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/power-bi/
  - type: Pricing
    url: https://powerbi.microsoft.com/en-us/pricing/
  - type: Authentication
    url: https://learn.microsoft.com/en-us/power-bi/developer/embedded/get-azuread-access-token
  - type: SDKs
    url: https://learn.microsoft.com/en-us/power-bi/developer/embedded/
  - type: Community
    url: https://community.fabric.microsoft.com/t5/Power-BI-forums/ct-p/pbi_english
  - type: Blog
    url: https://powerbi.microsoft.com/en-us/blog/
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
  - type: Status
    url: https://status.powerplatform.microsoft.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

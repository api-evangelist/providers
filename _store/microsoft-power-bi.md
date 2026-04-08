---
aid: microsoft-power-bi
url: https://raw.githubusercontent.com/api-evangelist/microsoft-power-bi/refs/heads/main/apis.yml
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
name: Microsoft Power BI
tags:
- Analytics
- Business Intelligence
- Dashboards
- Microsoft
- Reports
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Microsoft Power BI is a business analytics service that delivers insights to enable fast, informed decisions. It provides REST APIs for accessing and managing Power BI resources including reports, dashboards, datasets, and workspaces programmatically.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


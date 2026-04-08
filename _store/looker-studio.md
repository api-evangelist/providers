---
aid: looker-studio
url: https://raw.githubusercontent.com/api-evangelist/looker-studio/refs/heads/main/apis.yml
apis:
- name: Looker Studio API
  description: The Looker Studio API enables developers to programmatically manage reports, data sources, and permissions. It provides methods for searching assets and managing asset permissions including getting, updating, adding, and removing members.
  image: https://www.gstatic.com/analytics-suite/header/suite/v2/ic_data_studio.svg
  humanURL: https://developers.google.com/looker-studio/integrate/api
  baseURL: https://datastudio.googleapis.com/v1
  tags:
  - Assets
  - Automation
  - Data Sources
  - Permissions
  - Reports
  properties:
  - type: Documentation
    url: https://developers.google.com/looker-studio/integrate/api
  - type: Reference
    url: https://developers.google.com/looker-studio/integrate/api/reference
  - type: OpenAPI
    url: openapi/looker-studio-api-openapi.yml
  - type: OpenAPI
    url: https://lookerstudio.googleapis.com/$discovery/rest?version=v1
  - type: Authentication
    url: https://developers.google.com/looker-studio/api/authentication
  - type: Getting Started
    url: https://developers.google.com/looker-studio/api/quickstart
  - type: SDKs
    url: https://developers.google.com/looker-studio/api/client-libraries
  - type: Rate Limits
    url: https://developers.google.com/looker-studio/api/quotas
  - type: Errors
    url: https://developers.google.com/looker-studio/api/errors
  - type: JSON Schema
    url: json-schema/looker-studio-asset-schema.json
  - type: JSON Schema
    url: json-schema/looker-studio-permissions-schema.json
  - type: JSON Schema
    url: json-schema/looker-studio-report-schema.json
  - type: JSON Schema
    url: json-schema/looker-studio-data-source-schema.json
- name: Looker Studio Linking API
  description: The Looker Studio Linking API enables the creation of dynamic URLs that link to pre-configured reports. It allows developers to define data sources, control report behavior, and customize settings through URL parameters.
  humanURL: https://developers.google.com/looker-studio/integrate/linking-api
  baseURL: https://lookerstudio.google.com
  tags:
  - Data Sources
  - Integration
  - Linking
  - Reports
  - URL Parameters
  properties:
  - type: Documentation
    url: https://developers.google.com/looker-studio/integrate/linking-api
  - type: OpenAPI
    url: openapi/looker-studio-linking-api-openapi.yml
- name: Looker Studio Embedding API
  description: Embed Looker Studio reports in your applications using HTML iframe tags, oEmbed, and Open Graph Tags with customizable parameters and filtering options. Supports embedding on platforms like Medium and Reddit.
  humanURL: https://developers.google.com/looker-studio/integrate/embed
  baseURL: https://lookerstudio.google.com/embed
  tags:
  - Embedding
  - Iframe
  - Integration
  - Reports
  - Sharing
  properties:
  - type: Documentation
    url: https://developers.google.com/looker-studio/integrate/embed
  - type: OpenAPI
    url: openapi/looker-studio-embedding-api-openapi.yml
  - type: Getting Started
    url: https://developers.google.com/looker-studio/integrate/embedding-api/get-started
  - type: Security
    url: https://developers.google.com/looker-studio/connector/embed-row-level-security
- name: Looker Studio Community Connector API
  description: 'Build custom data connectors to bring data from any source into Looker Studio. Connectors are built using Google Apps Script and implement three core functions: getConfig(), getSchema(), and getData().'
  humanURL: https://developers.google.com/looker-studio/connector
  baseURL: https://datastudio.google.com/datasources/create
  tags:
  - Apps Script
  - Connectors
  - Custom Integration
  - Data Sources
  - ETL
  properties:
  - type: Documentation
    url: https://developers.google.com/looker-studio/connector
  - type: Reference
    url: https://developers.google.com/looker-studio/connector/reference
  - type: OpenAPI
    url: openapi/looker-studio-community-connector-api-openapi.yml
  - type: Getting Started
    url: https://developers.google.com/looker-studio/connector/build
  - type: Examples
    url: https://developers.google.com/looker-studio/connector/examples
  - type: Gallery
    url: https://lookerstudio.google.com/data
  - type: Change Log
    url: https://developers.google.com/looker-studio/connector/changelog
  - type: Publishing
    url: https://developers.google.com/looker-studio/connector/publish-connector
  - type: Sharing
    url: https://developers.google.com/looker-studio/connector/share
  - type: Direct Links
    url: https://developers.google.com/looker-studio/connector/direct-links
  - type: Codelabs
    url: https://codelabs.developers.google.com/codelabs/community-connectors
  - type: JSON Schema
    url: json-schema/looker-studio-connector-schema.json
- name: Looker Studio Community Visualization API
  description: Build and deploy custom visualizations for Looker Studio using any JavaScript visualization library. The dscc helper library simplifies development by providing functions for data subscriptions, component dimensions, and user interactions.
  humanURL: https://developers.google.com/looker-studio/visualization
  baseURL: https://lookerstudio.google.com/visualization
  tags:
  - Components
  - Custom Charts
  - Data Visualization
  - JavaScript
  - Visualizations
  properties:
  - type: Documentation
    url: https://developers.google.com/looker-studio/visualization
  - type: Reference
    url: https://developers.google.com/looker-studio/visualization/library-reference
  - type: OpenAPI
    url: openapi/looker-studio-community-visualization-api-openapi.yml
  - type: Getting Started
    url: https://developers.google.com/looker-studio/visualization/write-viz
  - type: SDKs
    url: https://developers.google.com/looker-studio/visualization/library
  - type: Local Development
    url: https://developers.google.com/looker-studio/visualization/local-dev
  - type: Open Source
    url: https://developers.google.com/looker-studio/visualization/open-source
  - type: Interactions
    url: https://developers.google.com/looker-studio/visualization/interactions-guide
  - type: Support
    url: https://developers.google.com/looker-studio/visualization/support
  - type: Codelabs
    url: https://codelabs.developers.google.com/codelabs/community-visualization
  - type: JSON Schema
    url: json-schema/looker-studio-visualization-schema.json
name: Looker Studio
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Visualization
- Google
- Reports
type: Contract
image: https://www.gstatic.com/analytics-suite/header/suite/v2/ic_data_studio.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Looker Studio (formerly Google Data Studio) is a free tool that turns your data into informative, easy to read, easy to share, and fully customizable dashboards and reports. The API allows developers to programmatically manage assets, build custom connectors and visualizations, embed reports, and automate workflows.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


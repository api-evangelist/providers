---
aid: google-data-studio
url: https://raw.githubusercontent.com/api-evangelist/google-data-studio/refs/heads/main/apis.yml
apis:
- name: Google Data Studio API
  description: The Looker Studio API enables programmatic management of Looker Studio assets, including searching for assets and managing permissions within Google Workspace or Cloud Identity organizations.
  image: https://www.gstatic.com/analytics-suite/header/suite/v2/ic_data_studio.svg
  humanURL: https://developers.google.com/looker-studio/integrate/api
  baseURL: https://datastudio.googleapis.com
  tags:
  - Assets
  - Data Sources
  - Permissions
  - Reports
  properties:
  - type: Documentation
    url: https://developers.google.com/looker-studio/integrate/api
  - type: OpenAPI
    url: openapi/google-data-studio-api-openapi.yml
  - type: OpenAPI
    url: https://datastudio.googleapis.com/$discovery/rest?version=v1
  - type: Reference
    url: https://developers.google.com/looker-studio/integrate/api/reference
  - type: Authentication
    url: https://developers.google.com/looker-studio/integrate/api
  - type: Change Log
    url: https://developers.google.com/looker-studio/integrate/api/changelog
- name: Looker Studio Linking API
  description: The Linking API provides a reliable interface to configure and forward users directly to a pre-configured Looker Studio report via URL parameters, enabling one-click report creation experiences.
  image: https://www.gstatic.com/analytics-suite/header/suite/v2/ic_data_studio.svg
  humanURL: https://developers.google.com/looker-studio/integrate/linking-api
  tags:
  - Embedding
  - Integration
  - Linking
  - Reports
  properties:
  - type: Documentation
    url: https://developers.google.com/looker-studio/integrate/linking-api
  - type: OpenAPI
    url: openapi/google-data-studio-linking-api-openapi.yml
- name: Looker Studio Community Connectors
  description: Community Connectors enable direct connections from Looker Studio to any internet-accessible data source using Google Apps Script. Developers implement getAuthType, getConfig, getSchema, and getData functions to build custom connectors.
  image: https://www.gstatic.com/analytics-suite/header/suite/v2/ic_data_studio.svg
  humanURL: https://developers.google.com/looker-studio/connector
  tags:
  - Apps Script
  - Connectors
  - Data Sources
  - Integration
  properties:
  - type: Documentation
    url: https://developers.google.com/looker-studio/connector
  - type: Reference
    url: https://developers.google.com/looker-studio/connector/reference
  - type: Getting Started
    url: https://developers.google.com/looker-studio/connector/build
  - type: Change Log
    url: https://developers.google.com/looker-studio/connector/changelog
  - type: Codelabs
    url: https://codelabs.developers.google.com/codelabs/community-connectors
- name: Looker Studio Community Visualizations
  description: Community Visualizations allow developers to build and share custom JavaScript visualizations in Looker Studio using the dscc helper library, extending the platform with custom chart types and visual components.
  image: https://www.gstatic.com/analytics-suite/header/suite/v2/ic_data_studio.svg
  humanURL: https://developers.google.com/looker-studio/visualization
  tags:
  - Charts
  - Custom Components
  - JavaScript
  - Visualizations
  properties:
  - type: Documentation
    url: https://developers.google.com/looker-studio/visualization
  - type: Getting Started
    url: https://developers.google.com/looker-studio/visualization/get-started
  - type: Reference
    url: https://developers.google.com/looker-studio/visualization/library-reference
  - type: Libraries
    url: https://developers.google.com/looker-studio/visualization/library
  - type: Codelabs
    url: https://codelabs.developers.google.com/codelabs/community-visualization
  - type: Open Source
    url: https://developers.google.com/looker-studio/visualization/open-source
name: Google Data Studio
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data
- Reporting
- Visualization
type: Contract
image: https://www.gstatic.com/analytics-suite/header/suite/v2/ic_data_studio.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Data Studio, now rebranded as Looker Studio, is a free data visualization and business intelligence tool from Google that transforms data into customizable, shareable dashboards and reports. It connects to a wide range of data sources and supports community connectors and visualizations for extensibility.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

